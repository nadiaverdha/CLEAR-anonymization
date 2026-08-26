# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-21T11:43:43.727308

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-20_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 1000 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 800 |
| Validation documents | 200 |
| Test documents | 477 |
| Train sentences | 13382 |
| Validation sentences | 3940 |
| Test sentences | 22727 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 100 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | True |
| Critic Interval | 20 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 50 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 92.6% |
| True Positives | 1195 |
| False Positives | 783 |
| False Negatives | 2819 |
| Total Gold Entities | 4014 |
| Micro Precision | 60.4% |
| Micro Recall | 29.8% |
| Micro F1 | 39.9% |
| Macro F1 | 39.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Oberster Gerichtshof` | 39.5% | 100.0% | 24.6% | 987 | 987 | 0 |
| `Verfassungsgerichtshof` | 1.1% | 100.0% | 0.6% | 23 | 23 | 0 |
| `Wiener Gebietskrankenkasse` | 0.2% | 100.0% | 0.1% | 4 | 4 | 0 |
| `BEURLE Rechtsanwälte GmbH & Co KG` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Landesgericht für Zivilrechtssachen` | 0.5% | 100.0% | 0.2% | 10 | 10 | 0 |
| `Landesgericht für Strafsachen` | 0.7% | 100.0% | 0.3% | 14 | 14 | 0 |
| `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Magistrat der Stadt Wien with Dept` | 0.4% | 100.0% | 0.2% | 8 | 8 | 0 |
| `Bezirksgericht` | 3.6% | 76.5% | 1.9% | 98 | 75 | 23 |
| `ÖBB Abbreviation` | 0.4% | 69.2% | 0.2% | 13 | 9 | 4 |
| `GmbH Preceded by Article` | 0.8% | 51.5% | 0.4% | 33 | 17 | 16 |
| `Landesgericht with Location` | 1.1% | 45.1% | 0.6% | 51 | 23 | 28 |
| `KG Entities` | 0.6% | 32.4% | 0.3% | 37 | 12 | 25 |
| `Aktiengesellschaft Compound` | 0.5% | 12.6% | 0.3% | 87 | 11 | 76 |
| `m.b.H. Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgerichtshof` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzpolizei` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FAÖ Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vorbrodt Sanitär` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Snajdr E-Commerce GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Glanzder-Automotive GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Jackobi und Horbank KI GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KAG Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fa. GmbH Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ÖGK Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KPMG Alpen-Treuhand GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht (BFG) Combined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Pensionsversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Universität Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMI Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Derdonal-Garten AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Energie Verdorfwald GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schlaich Bau KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `St. Johann Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `APP Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gerichtshof der Europäischen Union` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `Landesgericht Standalone` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `Nieder Unisyn Manufaktur GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schniederjahn Software KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unverdroß Planung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Salzburg-Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamt für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgericht Wien` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `COFAG Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BHAG Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `technoRent International GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Südb Consynkel KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Glatzhofer & Matschek mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag. Manfred Reumiller GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgerichtshof Genitive` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `Finanzamt Steiermark Mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Feldkirch` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Süd Consynkel KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Reinhard Stulik Steuerberatungs GmbH & Co OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SK Telecom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BDO Assurance` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wald Zorwaldmon KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Alpen-KI GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Amtes für Betrugsbekämpfung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Zollamt` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `XY GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFG Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Amt für Betrugsbekämpfung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FB + KG Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FB + KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Oststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hallas & Partner GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrats der Stadt Wien with Dept` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schabetsberger & Partner GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schaar Wirtschaftstreuhand OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Süd Ostfen Institut AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kailuhn KI AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Zollamt with Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Linien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Gemeindebezirk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `APK Pensionskasse AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deutschen Rentenversicherung Bund` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WGKK Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministerium für Inneres` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Mur Steinstein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wirtschaftsuniversität Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt für Gebühren` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirektion State` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzstrafsenat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirektion Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UniCredit Bank Austria AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Reiffenstuel Pflege GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Garantie - Wirtschaftstreuhand- gesellschaft m.b.H.` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Djuric & Oberger Wth OG Steuerberatungsgesellschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `G & W Steuerberatungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien 9/18/19 Klosterneuburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Baden Mödling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Wien 4/5/10` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lexlog Automotive GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Textil Berdon KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BKS Steuerberatungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verlag Derkel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `kaubek & partner GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Central Liaison Office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Europäische Gerichtshof` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Fa. GmbH Entities (No Space)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Analyse Allexwald GmbH` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `c Stahl und Anlagenbau GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `D-Stahl und Anlagenbau GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirektion Standalone` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Finanzamts Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hans Bühler KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KRW Kärnten Steuerberatungsgesellschaft mbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMF Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Billa Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Gemeindebezirkes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steuerberatungspartnerschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WestImmobilien GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OstLextraMedien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat Klagenfurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Erste Bank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GKK Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GKK Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fuchshuber Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `S Projektenwicklung und Beteiligungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Seidlmayer Software GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt Klagenfurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gwen Bozdag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LG für ZRS Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KAPAS Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt für Großbetriebe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Amstetten Melk Scheibbs` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Neunkirchen Wiener Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt End of Sentence` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Wiener Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Quappill & Lechbauer Technik GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ELDA Competence Center` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Quappill & Lechbauer Technik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lieferant-C KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Wien Numbers` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Versorgungskasse VVaG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gronmeier Robotik GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Abbreviation with Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Universität Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Höllermeier Schaller & Partner Steuerberatung Hallein GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ernst & Young Steuerberatungsgesellschaft m.b.H.` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wirtschaftskammer Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `RheinDertriHandel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr. Obermayer Rechtsanwalt GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Claus & Berthold Rechtsanwaltspartnerschaft KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FLAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KG Standalone` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Höhere Lehranstalt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht/BFG Compound` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hennicke Robotik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Quoted Company Name` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Landesgerichtes für ZRS` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kraftbachstein-Energie GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerische Ausgleichskasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht Standalone` | 0.0% | 0.0% | 0.0% | 26 | 0 | 26 |
| `Glanzber E-Commerce GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vercon-Holz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WKO Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Österreich FAÖ Combined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Österreich/FAÖ Combined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SUVA Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Paracelsus Medizinische Privatuniversität` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Universität Salzburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Yang + Jannowsky Handel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hauer & Partner Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GKA Gao u Keki-Angermann RA GesbR` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `DR. NIKOLAUS Wirtschaftstreuhand GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BG&P Binder Grossek & Partner Steuerberatung und Wirtschafts- prüfung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Spittal Villach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Braunau Ried` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Braunau Ried Schärding` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BDO Austria GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ernst & Young Steuerberatungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Krüger/Bauer Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Abbreviation` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `GmbH Missing Space` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lognexuni-Lebensmittel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Zorglanzsyn-Software GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Gänserndorf Mistelbach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt St. Johann Tamsweg Zell am See` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Leoben` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Logsudglanz-Versand GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wilsee IT Werke GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Zachmann & Partner Rechtsanwälte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steuerberater Metzler & Adelsberger OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ARTUS Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kleiner Eberl Brandstätter Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiech und Gökcek Transport GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WaldHolz OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ikea Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Obi Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Leiner Organization` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Möbelix Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `MömaX Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Otto.de Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `xxxLutz Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Graz-Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Neunkirchen Wr. Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Kirchdorf Perg Steyr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Gemeindebezirks` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Bundesamt für Soziales und Behindertenwesen Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Arbeits- und Sozialgericht Wien` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `Inn Talwerk Services GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Leybrand&Weinforth Medien GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bayer Finanzen OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Bruck Eisenstadt Oberwart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stadt Wien Double Space` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Arbeits- und Sozialgericht` | 0.0% | 0.0% | 0.0% | 24 | 0 | 24 |
| `ZMH Planung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Waldwil-Daten GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `CQLA Solar Systeme GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gneist Consulting Team Wien Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Erlacher & Erlacher-Philadelphy Rechtsanwälte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FRONTEX` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Oberbank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steuerberatungsgesellschaft KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bärje Pharma GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lenfeld Leys Sonderegger Rechtsanwälte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BergEnergie GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Könning und Wilmesmaier Bau GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KMG AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Standalone` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Bachkelber-Bildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stanley Versand GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `A-Klinikum GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Vorarlberg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien 1/23` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AT Tax Advisory & Trustee Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SOLIDUS Steuerberatungs- und Wirtschaftstreuhand GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Keuler u. Symmat Chemie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Johann Sch Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FEGA Services Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `NordRecycling Betriebe AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lemtalheim-Energie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Nieder\u00f6sterreich Mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Graf & Partner Steuerberatungs- gesellschaft m.b.H.` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Graz-Umgebung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gambi Luftfahrt GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Weber Harrer Rechtsanwälte GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `3Partner Steuerberatung OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `B & S Steuer- und Unternehmensberatungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Eckhardt Wirtschaftsprüfung u SteuerberatungsgmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr. Obermoser Wirtschaftstreuhand GmbH, Steuerberatungsgesellschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Grieskirchen Wels` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LG Abbreviation Court` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Bundesfinanzgericht with Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Bregenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kohl-Verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Waldviertel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Tirol Ost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Freistadt Rohrbach Urfahr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Salzburg-Land` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Abbreviation with Location (Extended)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag. Thonhauser Steuerberater GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFP Wirtschaftsprüfungs- u STB GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ERNST & YOUNG Wirtschaftsprüfungs und Steuerberatungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien 2/20/21/22` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Enns-Holz Betriebe GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Gemeinderat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Gemeinderates` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Diezelmüller Pflege GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TalBachvertraSoftware Services GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Period-Prefixed GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Period-Prefixed KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dreismickenbecker Logistik GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Freiert Garten GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisen Digital Bank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Salzburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lebensmittel Zorder GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stb. & Partner GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hendlmaier Möbel AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mikloweit Bau AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `X GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Riegerl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verfassungsgerichtshof/Verwaltungsgerichtshof Compound` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgerichtes Standalone` | 0.0% | 0.0% | 0.0% | 470 | 0 | 470 |
| `BFH Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Bruck Leoben Mürzzuschlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Judenburg Liezen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stadt Wien` | 0.0% | 0.0% | 0.0% | 32 | 0 | 32 |
| `OECD` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Oberster Gerichtshof` 🏆

**F1:** 0.395 | **Precision:** 1.000 | **Recall:** 0.246  

**Format:** `regex`  
**Rule ID:** `3c17c7a1`  
**Description:**
Matches 'Oberster Gerichtshof', 'Oberste Gerichtshof', and their genitive forms 'Obersten Gerichtshofes' or 'Obersten Gerichtshof'.

**Content:**
```
(?<!\w)(Oberster\s+Gerichtshof(?:es)?|Oberste\s+Gerichtshof(?:es)?|Obersten\s+Gerichtshof(?:es)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.246 | 0.395 | 987 | 987 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 987 | 0 | 3026 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Nowotny` (person)
- `Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Selma Einoeder` (person)
- `Mag. Alexander Gerngross` (person)
- `Mag. Klaus Köck` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_14`)


Das Erstgericht legte den Akt dem Obersten Gerichtshof unter Hinweis auf den Verfahrensstand, aber entgegen § 31 Abs 3 JN ohne eigene Stellungnahme zur Zweckmäßigkeit, zur Entscheidung über den Delegierungsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Kordelia Meelis` (person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft` (organisation)
- `Fatima Tengel` (person)
- `Mag. Ernst Michael Lang` (person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_23`)


2.1 Als Grundlage für eine Ordination kommt daher nur der Fall des § 28 Abs 1 Z 2 JN in Betracht, wonach die Bestimmung eines örtlich zuständigen Gerichts durch den Obersten Gerichtshof dann zulässig ist, wenn der Antragsteller seinen Wohnsitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre (RIS-Justiz RS0112108).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Landesgericht Linz` (organisation)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Linz` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schramm` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Judenburg` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Mödling` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_8`)


Andernfalls könnte eine Verschiebung der funktionellen Zuständigkeit eintreten, weil mangels Bestätigung des Übertragungsbeschlusses durch das Rekursgericht gar keine Grundlage für die Genehmigung einer Zuständigkeitsübertragung durch den Obersten Gerichtshof bestünde (9 Nc 15/14a;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Marlene Friss` (person)
- `WestTelekom GmbH` (organisation)
- `Rehwald 11, 4723 Fronberg, Österreich` (address)
- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_4`)


Text Begründung: Mit ihrer erkennbar an den Obersten Gerichtshof gerichteten Eingabe vom 6.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Gerhard Lohrmann` (person)
- `10. August 1983` (date)
- `Veit Künneken` (person)
- `31. Mai 1967` (date)
- `Bezirksgerichts Feldkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_9`)


Das übertragende Gericht legte aufgrund dieser Weigerung den Akt dem Obersten Gerichtshof als gemeinsam übergeordnetem Gericht zur Entscheidung gemäß § 111 Abs 2 JN vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Nowotny` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Selma Eichler, LLM` (person)
- `13. September` (date)
- `Bezirksgerichts Graz-West` (organisation)
- `Bezirksgericht Graz-West` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-West` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Ober-Automotive GmbH` (organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich` (address)
- `Mag. Alexander Rimser` (person)
- `Katharina Rothschadl` (person)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_15`)


Das Erstgericht wies die Klage wegen Fehlens eines inländischen Gerichtsstands und somit der österreichischen internationalen Zuständigkeit rechtskräftig zurück und legte daraufhin den Akt dem Obersten Gerichtshof zur Entscheidung über den hilfsweise gestellten Ordinationsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Dietlind Schiewick` (person)
- `23. Oktober` (date)
- `Bezirkshauptmannschaft Vöcklabruck` (organisation)
- `Gisela Akcakaya, MSc` (person)
- `Ernst Hartjens` (person)
- `Bezirksgericht Josefstadt` (organisation)
- `Bezirksgericht Villach` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Josefstadt` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Villach` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_24`)


Dies gilt jedenfalls dann, wenn das für die Entscheidung über einen Rekurs gegen den Übertragungsbeschluss zuständige Gericht mit dem zur Genehmigung nach § 111 Abs 2 JN berufenen Gericht (hier der Oberste Gerichtshof) nicht ident ist (RS0047067 [T14]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)
- `Bezirksgericht Schwechat` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_6`)


Rechtliche Beurteilung Nach § 28 Abs 1 Z 2 JN hat der Oberste Gerichtshof, wenn für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts im Sinne dieses Gesetzes oder einer anderen Rechtsvorschrift nicht gegeben oder nicht zu ermitteln sind, aus den sachlich zuständigen Gerichten eines zu bestimmen, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn unter anderem der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_7`)


Der Oberste Gerichtshof hat in gleich gelagerten Fällen (4 Nc 11/19h, 6 Nc 1/19b, 7 Nc 23/19w) die Ordination bewilligt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Paulina Nüsken` (person)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Oliver Eylart` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_14`)


An die rechtskräftige Verneinung der internationalen Zuständigkeit des vom Kläger angerufenen Bezirksgerichts Schwechat ist der Oberste Gerichtshof gebunden (RIS-Justiz RS0046568).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgerichts Schwechat` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_16`)


Für den Fall, dass für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts nicht gegeben oder nicht zu ermitteln sind, bestimmt § 28 Abs 1 Z 2 JN, dass der Oberste Gerichtshof aus den sachlich zuständigen Gerichten eines zu bestimmen hat, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_21`)


[7] 4.1 Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (zB 6 Nc 1/19b ZVR 2019/114, 259 [Mayr];

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Bezirksgerichts Kitzbühel` (organisation)
- `Karin Ciliberto` (person)
- `Mag. Maximilian Kocher` (person)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht Linz` (organisation)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Dr. Roland Kassowitz` (person)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
- `Landesgerichts Linz` (organisation)
- `Handelsgericht Wien` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_40`)


2.2. Die Ansicht vonMayr(Die Delegation im zivilgerichtlichen Verfahren, JBl 1983, 293 [299]; in diesem Sinn auchSchneiderinFasching/Konecny3§ 31 JN Rz 18), der Vereinbarung des Gerichtsstands oder des Erfüllungsorts sei kein größeres Gewicht beizumessen als der gesetzlichen Zuständigkeit, hat der Oberste Gerichtshof bereits abgelehnt (RIS-Justiz RS0046198 [T10]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mur Dorftalnex Technologien -GmbH` (organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich` (address)
- `Dr. Peter Lechner` (person)
- `Dr. Hermann Pfurtscheller` (person)
- `Ober Dertri GmbH` (organisation)
- `Hintereggweg 93, 2070 Kleinhöflein, Österreich` (address)
- `Dr. Thomas Girardi` (person)
- `Rudolf Ketelhut` (person)
- `Fiebrichgasse 17, 5120 Seeleiten, Österreich` (address)
- `Dr. Bernhard Hämmerle GmbH` (organisation)
- `Völkertz Energie GmbH` (organisation)
- `Brunnbachweg 19, 4653 Mayersdorf, Österreich` (address)
- `Dr. Franz Pechmann` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_54`)


1. Auf die Ausführungen der Revision, die sich gegen die dem Aufhebungsbeschluss zugrundeliegende rechtliche Beurteilung des Berufungsgerichts wenden, ist vom Obersten Gerichtshof mangels Bekämpfbarkeit des Aufhebungsbeschlusses derzeit nicht einzugehen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Stefula` (person)
- `Schneidergruberweg 37, 5132 Reith, Österreich` (address)
- `Dr. Alois Schneider` (person)
- `Dario von Ebers` (person)
- `Dr. Walter Hausberger` (person)
- `Dr. Katharina Moritz` (person)
- `Dr. Alfred Schmidt` (person)
- `Landesgerichts Innsbruck` (organisation)
- `Bezirksgerichts Rattenberg` (organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Eva Abdelrahman` (person)
- `Dr. Karl-Heinz Plankel` (person)
- `Hochenadel Immobilien GmbH` (organisation)
- `Ritterhof 11, 2661 Graben, Österreich` (address)
- `Lederer Rechtsanwalt GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_65`)


Die Klage wurde daher lange vor Ablauf der Verjährungsfrist eingebracht und der Fortsetzungsantrag rund sechs Monate nach dem Ablauf der ursprünglichen Verjährungsfrist gestellt. In der Entscheidung 6 Ob 822/81 (RIS-Justiz RS0034674) ist der Oberste Gerichtshof in einem Fall, in dem Ruhen des Verfahrens eingetreten war und beinahe ein Jahr nach Ablauf der dreijährigen Verjährungsfrist andauerte, von einer Verjährung mangels gehöriger Fortsetzung ausgegangen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Dr. Ralph Trischler` (person)
- `Bundesbeschaffung GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_23`)


Rechtliche Beurteilung Der Revisionsrekurs des Bundes ist entgegen dem den Obersten Gerichtshof nicht bindenden Ausspruch des Rekursgerichts (§ 71 Abs 1 AußStrG) mangels einer Rechtsfrage im Sinn des § 62 Abs 1 AußStrG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Ludmilla von Amelunxen` (person)
- `Dr. Bernhard Birek` (person)
- `Svetlana Leinhäuser` (person)
- `Dr. Thomas Brückl` (person)
- `Mag. Christian Breit` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_95`)


In einem solchen Fall kann der Oberste Gerichtshof durch Urteil in der Sache selbst erkennen (§ 519 Abs 2 Satz 3 ZPO), sodass der Beschluss des Berufungsgerichts aufzuheben und die klageabweisende Entscheidung des Erstgerichts wiederherzustellen war.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Kevin Maassen` (person)
- `Dr. Clemens Lintschinger` (person)
- `Hon.-Prof. Friedhelm Adde` (person)
- `Mag. Dr. Georg Backhausen` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_20`)


Dieser Fall liegt hier aber nach den den Obersten Gerichtshof bindenden Feststellungen nicht vor, weil der Beklagte - entgegen den Ausführungen des Revisionswerbers - die aufgekündigte Wohnungnichtregelmäßig zu Wohnzwecken verwendet, sondern lediglich sporadisch, als Absteigequartier.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_27`)


Ein Kostenersatz für die ohne Freistellung durch den Obersten Gerichtshof eingebrachte Revisionsbeantwortung steht der Klägerin nach § 508a Abs 2 Satz 2 ZPO nicht zu (RIS-Justiz RS0043690 [T6, T7]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Nowotny` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Dr. Wallner-Friedl` (person)
- `Ing. Mag. Pamela Gotterbauer` (person)
- `Mag. Helwig Schuster` (person)

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_144`)


Das Berufungsgericht hat – ausgehend von seiner vom Obersten Gerichtshof nicht geteilten Rechtsansicht – sowohl die Mängelrüge (Nichteinholung eines Gutachtens für den Bereich Pferdehaltung und Pferdesport) als auch die (auch) die Feststellungen zu den behaupteten Mängeln betreffende Beweisrüge der Berufung nicht erledigt, weshalb sein Verfahren mangelhaft geblieben ist.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Verein für Konsumenteninformation` (organisation)
- `Dr. Walter Reichholf` (person)
- `SüdSanitär Gruppe GmbH` (organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich` (address)
- `Kraft & Winternitz Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Steger` (person)
- `Dr. Annerl` (person)
- `Dr. Wallner-Friedl` (person)
- `Ralph Prusseit` (person)
- `Mag. Franz Eckl` (person)
- `Akbayrak Metall GmbH` (organisation)
- `Schroateck 57, 4710 Niederweng, Österreich` (address)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Krems an der Donau` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_56`)


Der Oberste Gerichtshof habe festgehalten, dass die Weigerung des Netzbenutzers, dem Netzbetreiber für einen geplanten Zählertausch Zutritt zu einem Objekt zu gewähren, es nicht rechtfertige, anstelle der Inanspruchnahme gerichtlicher Hilfe faktisch zur Selbsthilfe im Wege der (Androhung der) Stromabschaltung zu greifen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_75`)


[17]5.Der Oberste Gerichtshof hat zu 9 Ob 95/24x, 7 Ob 167/24w und 3 Ob 191/24w (betreffend vergleichbare AB-VN einer anderen Netzbetreiberin) dargelegt, dass die Weigerung des Netzbenutzers, der Netzbetreiberin Zugang zu seinem Objekt zu gewähren, damit sie einen (grundsätzlich funktionsfähigen) Stromzähler austauschen kann, qualitativ nicht den Fällen des Zahlungsverzugs und der Verweigerung einer Vorauszahlung oder Sicherheitsleistung gleichzuhalten sei.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Heimcon Software GmbH` (organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich` (address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH` (organisation)
- `Gunter Landwirtschaft GmbH` (organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich` (address)
- `Stolz & Schartner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_50`)


4. 2011 enthaltenen Hinweise weitere Aufträge erteilt habe, werden keine Umstände aufgezeigt, die einen vom Obersten Gerichtshof aufzugreifenden Fehler in der Beurteilung des Berufungsgerichts, der nicht fachkundigen Klägerin könne kein Mitverschulden am Entstehen des Schadens angelastet werden, begründen könnten.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `DDr.in Cornelia Rinaldo` (person)
- `Dr. Sven Rudolf Thorstensen` (person)
- `Conmon-Verlag Limited` (organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich` (address)
- `Brandl Talos Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_9`)


Die Revision der Beklagten ist entgegen dem – den Obersten Gerichtshof nicht bindenden – Zulassungsausspruch mangels Vorliegens einer Rechtsfrage von erheblicher Bedeutung im Sinn des § 502 Abs 1 ZPO nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_11`)


Das Vorliegen einer Rechtsfrage von erheblicher Bedeutung ist nach dem Zeitpunkt der Entscheidung über das Rechtsmittel durch den Obersten Gerichtshof zu beurteilen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_15`)


2010 geltenden Fassung des GSpG hat der Oberste Gerichtshof bereits in der – einen nahezu identen Sachverhalt betreffenden – Entscheidung 6 Ob 229/21a klargestellt, dass zwar das in § 21 Abs 2 Z 1 GSpG (bzw § 14 Abs 2 Z 1 GSpG) idF vor dem Budgetbegleitgesetz 2011 normierte Sitzerfordernis unionsrechtswidrig war und nach der Rechtsprechung des EuGH ein Mitgliedstaat keine (verwaltungs-)strafrechtlichen Sanktionen wegen einer nicht erfüllten Verwaltungsformalität verhängen darf, wenn er die Erfüllung dieser Formalität unter Verstoß gegen das Unionsrecht abgelehnt oder vereitelt hat, dass aber dieser Grundsatz schon deshalb nicht auf die vorliegende Konstellation übertragbar ist, weil die „Nichtigkeitssanktion“ im Sinn des § 879 Abs 1 ABGB keine vergleichbare staatliche Sanktion repressiver Natur darstellt. Weiters führte der Oberste Gerichtshof in der zitierten Entscheidung 6 Ob 229/21a aus, dass die zivilrechtliche Unerlaubtheit des Spiels eine Strafbarkeit im Sinn des § 168 StGB nicht voraussetzt (4 Ob 70/22f mwH; RS0102178 [T10]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_20`)


Der Oberste Gerichtshof hat mittlerweile auch die Passivlegitimation der Beklagten für den vom Kläger mit Leistungskondiktion begehrten Ersatz seiner Spielverluste aus Online-Pokerspielen in vergleichbaren Verfahren bereits mehrfach bejaht (6 Ob 229/21a;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_59`)


2.2 In der – bereits von den Vorinstanzen zitierten und verwerteten – Entscheidung 1 Ob 158/15i hat der Oberste Gerichtshof das folgende, in der Entscheidung 8 Ob 89/17x fortgeschriebene Modell für die Festsetzung des Differenzunterhalts entwickelt: Zunächst ist der fiktive Geldunterhaltsanspruch des Kindes gegen jeden Elternteil nach der Prozentmethode – bei weit überdurchschnittlichem Einkommen des besser verdienenden Elternteils unter Bedachtnahme auf die sogenannte Luxusgrenze – zu ermitteln.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr.Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei AXA Software Institut Gesellschaft mbH, Fuchsgrabengasse 27K, 8330 Untergiem, Österreich, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr.Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `AXA Software Institut Gesellschaft mbH` (organisation)
- `Fuchsgrabengasse 27K, 8330 Untergiem, Österreich` (address)
- `Mag. Oliver Simoncic` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei James Jooß, vertreten durch Dr. Klaus Schiller, Rechtsanwalt in Schwanenstadt, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `James Jooß` (person)
- `Dr. Klaus Schiller` (person)

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_79`)


Rechtliche Beurteilung DieRevisionist entgegen dem - den Obersten Gerichtshof nicht bindenden (§ 508 Abs 1 ZPO) - Ausspruch des Berufungsgerichts zulässig, weil das Berufungsgericht von der ständigen Rechtsprechung des Obersten Gerichtshofs zur Beurteilung von Kündigungserklärungen abweicht;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_108`)


Dabei wird übersehen, dass im Rechtsmittelverfahren vor dem Obersten Gerichtshof Verweise in der Revision bzw Revisionsbeantwortung auf Ausführungen in anderen Schriftsätzen (zB der Berufung) nach ständiger Rechtsprechung unzulässig und unbeachtlich sind (RIS-Justiz RS0043579 und RS0043616; vgl auch RS0007029).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 68** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Brigitte Martz` (person)
- `16. November 1978` (date)
- `Dr. Gustav Thöning` (person)
- `Pieler & Pieler & Partner KG` (organisation)
- `Dr. Madeleine Musialik` (person)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_4`)


Begründung:  Rechtliche Beurteilung Der Oberste Gerichtshof befasste sich in seinem Aufhebungsbeschluss vom 13.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 70** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_39`)


2.1 Der gegen den abändernden Teil der Rekursentscheidung gerichtete – nach Freistellung durch den Obersten Gerichtshof vomVater beantwortete– Revisionsrekurs ist hingegen zulässig und im Sinne einer Aufhebung berechtigt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 71** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Bau Zorostfurt GmbH` (organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich` (address)
- `Dr. Alexandra Slama` (person)
- `Buitenkamp und Rothauge Landwirtschaft GmbH` (organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich` (address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Mag. Herwig Bortzlaff` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_16`)


Die Verhängung der Ordnungsstrafe hingegen sei grundsätzlich durch Rekurs an den Obersten Gerichtshof bekämpfbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 74** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_19`)


Mit dem dagegen erhobenen Rekurs an den Obersten Gerichtshof verband der Rechtsmittelwerber einen Ablehnungsantrag gegen die Vorsitzende und die beiden weiteren Mitglieder des 13.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 75** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_25`)


Der Beschluss ist daher, da dem Ablehnungsantrag nicht stattgegeben wurde, gemäß § 24 Abs 2 JN uneingeschränkt an den Obersten Gerichtshof anfechtbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 76** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_27`)


Vor Eingehen auf das Rechtsmittel selbst ist vorerst die Frage zu prüfen, ob die Rekursschrift von einem Rechtsanwalt zu fertigen und daher durch den Obersten Gerichtshof das Verbesserungsverfahren einzuleiten wäre.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 77** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_31`)


Das Oberlandesgericht Wien hat funktionell als Erstgericht entschieden, der Oberste Gerichtshof entscheidet daher im vorliegenden Fall als Rekursgericht.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Jaden Meyerjohann` (person)
- `3. Juli 2020` (date)
- `Leroy Jungschmidt` (person)
- `28. Mai 1965` (date)
- `Clemens Theocharakis` (person)
- `25. März 1999` (date)
- `Emanuela Janischefsky` (person)
- `Bezirkshauptmannschaft Feldkirch` (organisation)
- `Ashley Biesert` (person)
- `Mag. Hans-Christian Obernberger` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_19`)


Nach Vorlage des Revisionsrekurses stellte der Oberste Gerichtshof mit Beschluss vom 25.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 80** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_26`)


Mit Beschluss des Erstgerichts vom 29. 11. 2013 (zugestellt am 9. 12. 2013) wurde dem Vertreter des Vaters in der Folge auch der ordentliche Revisionsrekurs „vom31. 1. 2013(ON 82)“ zur Verbesserung binnen 14 Tagen (gemäß dem Beschluss 10 Ob 29/13g [ON 93]) zurückgestellt. Den am 10. 12. 2013 im ERV eingebrachten verbesserten Revisionsrekurs legt das Erstgericht neuerlich dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 81** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_35`)


das ordentliche Rechtsmittel ist jedoch entgegen dem - gemäß § 71 Abs 1 AußStrG den Obersten Gerichtshof nicht bindenden - Ausspruch des Rekursgerichts wegen Fehlens einer erheblichen Rechtsfrage nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 82** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_54`)


3. Entgegen den Ausführungen zur Zulässigkeit des Revisionsrekurses hat sich der Oberste Gerichtshof bereits ausdrücklich mit der Frage befasst, ob die (wenn auch nur mögliche) Anwendung europäischen Primär- und Sekundärrechtes oder völkerrechtlicher Abkommen der EU mit anderen Staaten (unabhängig davon, ob eine „schwierige Rechtsfrage“ zu lösen ist) dem Begriff „ausländisches Recht“ im Sinn des § 16 Abs 2 Z 6 RpflG zuzurechnen ist und demgemäß auch dem Richtervorbehalt unterliegt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 83** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Karsten Alberter` (person)
- `2. April 2010` (date)
- `Helmut Dreilich` (person)
- `Landesgerichts Korneuburg` (organisation)
- `Bezirksgerichts Schwechat` (organisation)
- `Lena Amini` (person)

**Example 84** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_10`)


Das Erstgericht wertete dieses Rechtsmittel als außerordentlichen Revisionsrekurs und ging davon aus, dass dieser sogleich dem Obersten Gerichtshof vorzulegen sei.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 85** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_15`)


Daraufhin legte das Erstgericht das Rechtsmittel dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 86** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_20`)


Steht dem Rechtsmittelwerber nur der Rechtsbehelf der Zulassungsvorstellung nach § 63 Abs 1 AußStrG zur Verfügung, ist das Rechtsmittel nicht dem Obersten Gerichtshof vorzulegen, weil im Streitwertbereich des § 63 AußStrG Rechtsmittel gegen Entscheidungen, gegen die nach dem Ausspruch des § 59 Abs 1 Z 2 AußStrG der ordentliche Revisionsrekurs nicht zulässig ist, dem Gericht zweiter Instanz vorzulegen sind (§ 69 Abs 3 AußStrG).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 87** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_22`)


Der Oberste Gerichtshof ist für deren Erledigung - somit auch für eine allfällige Zurückweisung - funktionell unzuständig.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 88** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Maja Dolleschell` (person)
- `14. August` (date)
- `Bezirkshauptmannschaft Melk` (organisation)
- `Landesgerichts St. Pölten` (organisation)
- `Bezirksgerichts Melk` (organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Leander Andermann` (person)
- `Dr. Martin Leitner` (person)
- `Ing. Ferdinand Abramova` (person)
- `Mag. Wilhelm Deutschmann MBA` (person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Langhansl+Antonewitz Chemie AG` (organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich` (address)
- `Poinstingl & Partner Rechtsanwälte OG` (organisation)
- `Drau-Pharma GmbH` (organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich` (address)
- `Mag. Johannes Bügler` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_40`)


Der Rekurs an den Obersten Gerichtshof sei zulässig, weil eine Klarstellung geboten erscheine, dass die bei Zwischenurteilen angenommene erweiterte Bindungswirkung auf die vorliegende Konstellation einer späteren Klagsausdehnung nach einem von der beklagten Partei unbekämpft gebliebenen Ausspruch über einen Teilausspruch keine Anwendung finde.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 92** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_44`)


Rechtliche Beurteilung Der Rekurs ist entgegen dem - den Obersten Gerichtshof nicht bindenden (§ 526 Abs 2 ZPO) - Ausspruch des Berufungsgerichts nicht zulässig, weil die im Zulassungsausspruch umschriebene Rechtsfrage nicht die Qualifikation des § 502 Abs 1 ZPO erfüllt. 1. Die klagende Partei macht geltend, dass das Erstgericht einen hypothetischen Kausalverlauf im Fall pflichtgemäßer Aufklärung sehr wohl thematisiert habe.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 93** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_54`)


Auch bei Teilurteilen sei eine Bindungswirkung vom Obersten Gerichtshof bejaht worden, wenn sowohl die Identität der Parteien als auch des rechtserzeugenden Sachverhalts gegeben sei, aber anstelle der inhaltlichen und wörtlichen Identität des Begehrens ein im Gesetz gegründeter Sachzusammenhang zwischen beiden Begehren bestehe.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 94** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Dr. Wallner-Friedl` (person)
- `Karim Mielewczik` (person)
- `Dr. Sandro Gädecken` (person)
- `Ing. Dr. Stefan Krall` (person)
- `Dr. Oliver Kühnl` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Seekirchen` (organisation)

**Example 95** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Maja Pirkmayr` (person)
- `Dr. Georg Gorton` (person)
- `DDr. Birgit Gorton` (person)
- `Ing. Emanuel Puff` (person)
- `Dr. Gottfried Kassin` (person)
- `Landesgerichts Klagenfurt` (organisation)

**Example 96** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_32`)


Demzufolge bestand für die zweite Instanz kein Hindernis, in der Berufungsentscheidung - für den Obersten Gerichtshof mangels offenkundiger Überbewertung bindend (RIS-Justiz RS0042515;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 97** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_21`)


Den Revisionsrekurs ließ das Rekursgericht zu, weil der Oberste Gerichtshof zur Notwendigkeit und zum Umfang der Prüfung der Flüchtlingseigenschaft syrischer Staatsbürger, denen erst kürzlich Asyl gewährt worden sei, noch nicht Stellung genommen habe.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 99** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_24`)


Der Revisionsrekurs ist entgegen dem – den Obersten Gerichtshof nicht bindenden (§ 71 Abs 1 AußStrG) – Ausspruch des Rekursgerichts nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

</details>

---

## `Verfassungsgerichtshof` 🏆

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `f0f1e863`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofs', capturing the full name.

**Content:**
```
(?<!\w)(Verfassungsgerichtshof(?:es|s)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 3713 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_93`)


Die nach den Vorgaben des Verfassungsgerichtshofs gebotene steuerliche Entlastung des Geldunterhaltspflichtigen basiert auf dem Modell der getrennten Haushaltsführung (vgl RIS-Justiz RS0117015), in dem ein Elternteil seine Unterhaltspflicht durch Betreuungsleistungen und der andere durch Geldleistungen (allenfalls kombiniert mit anzurechnenden Naturalleistungen) erfüllt. Bei getrennter Haushaltsführung hat die Familienbeihilfe die Funktion, Betreuungsleistungen abzugelten und die steuerliche Entlastung des Geldunterhaltspflichtigen zu bewirken (RIS-Justiz RS0117015 [T20]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_91`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_147`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_158`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_159`)


Nach einhelliger Rechtsprechung steht den Parteien eines Gerichtsverfahrens kein Recht auf Antragstellung hinsichtlich einer Befassung des Verfassungsgerichtshofs zu. Die Parteien können eine solche Antragstellung nur anregen (RIS-Justiz RS0056514;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_162`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/3Ob229_14v`) (sent_id: `deanon_260716_TRAIN/3Ob229_14v_44`)


Auch der Verfassungsgerichtshof hat in der vom Kläger zitierten Entscheidung B 97/91, B 284/91-303/91 (= VfSlg 13.006) zu einer - nicht dem § 38 Abs 6 OÖ ROG entsprechenden - Norm des früheren OÖ ROG 1972 eingeräumt, dass unter dem auch dort verwendeten Begriff „Grundstück“ nicht unbedingt nur ein einzelnes Grundstück verstanden werden kann, sondern gegebenenfalls auch mehrere Grundstücke, die miteinander eine „Einheit“ bilden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_47`)


Die Klägerin führt dagegen ins Treffen, dass die beschlussmäßige Umwidmung eines Grundstücks nach der Rechtsprechung des Verfassungsgerichtshofs erst dann erfolgen könne, wenn die Gemeinde bereits Eigentümerin des betroffenen Grundstücks sei; nur wenn es sich beim Grundstück um eine Privatstraße gehandelt hätte, die über Antrag des Eigentümers umgewidmet werden sollte, wäre eine Beschlussfassung nach § 27 Abs 2 Sbg LStG 1966 durch die Gemeinde vor Eigentumserwerb möglich gewesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 8** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_50`)


Der von der Klägerin in diesem Zusammenhang zitierten Entscheidung des Verfassungsgerichtshofs vom 27. September 2003, V 108/01, lag nämlich der Sachverhalt zugrunde, dass der dort streitgegenständliche (Verbindungs-)Weg im Zeitpunkt der (vor der Enteignung des Grundstücks erfolgten) Widmung als Gemeindestraße schon seit Jahren als Privatstraße diente.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 9** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_51`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 11** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_147`)


3.2.6.Auch der Verfassungsgerichtshof hat sich bereits mehrfach (G 164/2014;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_152`)


Der Verfassungsgerichtshof führte allerdings aus, dass die Bestimmungen des Fern- und Auswärtsgeschäfte-Gesetzes den Vorschriften der Verbraucherrechte-RL entsprächen, welche den Mitgliedstaaten keinen Spielraum bei der Umsetzung einräumten;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_154`)


Auch von einem Vorabentscheidungsersuchen an den EuGH sah der Verfassungsgerichtshof ab (ErwG 74).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_155`)


Darüber hinaus setzte sich der Verfassungsgerichtshof in diesem Erkenntnis mit Art 14 Abs 2 der Verbraucherrechte-RL, der durch § 15 Abs 4 FAGG umgesetzt wurde, auseinander und äußerte keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz (entspricht § 15 Abs 4 letzter Satz FAGG): Der Verfassungsgerichtshof hat keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 15** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_159`)


Der Verfassungsgerichtshof kann nun nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL diesen von der Rechtsprechung des Gerichtshofes der Europäischen Union aufgestellten Kriterien im Rahmen der Verhältnismäßigkeitsprüfung eines Unionsrechtsakts widerspricht: Die Bestimmungen der Verbraucherrechte-RL verfolgen das Ziel eines umfassenden Verbraucherschutzes bei Fernabsatzverträgen und außerhalb von Geschäftsräumen geschlossenen Verträgen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 16** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_161`)


Der Verfassungsgerichtshof hat keine Zweifel, dass die in Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL normierte Rechtsfolge für den Unternehmer bei mangelnder Belehrung über das Widerrufsrecht geeignet ist, das Ziel des umfassenden Verbraucherschutzes bei Fernabsatzverträgen und bei außerhalb von Geschäftsräumen geschlossenen Verträgen zu erreichen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 17** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_162`)


Der Verfassungsgerichtshof kann auch nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL über das hinausgeht, was zur Verfolgung des mit der Regelung verfolgten Ziels des umfassenden Verbraucherschutzes erforderlich ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 18** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_165`)


Der Verfassungsgerichtshof hat sohin keine Zweifel an deren Gültigkeit.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 19** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `ÖBB` (organisation)

</details>

---

## `Wiener Gebietskrankenkasse` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `57de6ca5`  
**Description:**
Matches 'Wiener Gebietskrankenkasse' as an organisation.

**Content:**
```
(?<!\w)(Wiener\s+Gebietskrankenkasse)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 3512 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Fichtenau` (person)
- `KR Hermann Furtner` (person)
- `AR Angelika Neuhauser` (person)
- `Birgit Jaros` (person)
- `Dr. Herbert Pochieser` (person)
- `Dr. Heinz Edelmann` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Sailer, den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und den Hofrat Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Dr. Johannes Müller, Rechtsanwalt, Wien 3, Ditscheinergasse 2, als Masseverwalter im Konkurs der Wald-Event GmbH, gegen die beklagte Partei Wiener Gebietskrankenkasse, Wien 10, Wienerbergstraße 15-19, vertreten durch Preslmayr Rechtsanwälte OG in Wien, und der Nebenintervenienten auf der Seite der beklagten Partei 1.)

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Hon.-Prof. Dr. Sailer` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Johannes Müller` (person)
- `Wald-Event GmbH` (organisation)
- `Preslmayr Rechtsanwälte OG` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_22`)


7. den offenen Saldo bei der Wiener Gebietskrankenkasse im Ausmaß von EUR 86.000 (nach Ausdehnung des Zahlungsziels) zu bezahlen.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 3** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_24`)


Die Folgen einer Nichtbezahlung des offenen Saldos bei der Wiener Gebietskrankenkasse sind Ihnen bekannt.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

</details>

---

## `BEURLE Rechtsanwälte GmbH & Co KG` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ed4c2bc0`  
**Description:**
Matches the specific entity 'BEURLE Rechtsanwälte GmbH & Co KG'.

**Content:**
```
(?<!\w)BEURLE\s+Rechtsanw\u00e4lte\s+GmbH\s+&\s+Co\s+KG(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 2169 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `BEURLE Rechtsanwälte GmbH & Co KG` | `BEURLE Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `MMag. Sloboda` (person)
- `Dr. Kikinger` (person)
- `Mag. Fitz` (person)
- `Denise Markstaler` (person)
- `Weber Rechtsanwälte GmbH & Co KG` (organisation)
- `Rut Adamheit` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

</details>

---

## `Landesgericht für Zivilrechtssachen` 

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `2730c6c0`  
**Description:**
Matches 'Landesgericht für Zivilrechtssachen' followed by a city name, capturing the full court name.

**Content:**
```
(?<!\w)(Landesgericht\s+für\s+Zivilrechtssachen\s+[A-Z][a-zA-Z]+)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 0 | 3686 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mag. Herwig Bortzlaff` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_5`)


Im Zusammenhang mit diesem Verfahren wies das Landesgericht für Zivilrechtssachen Wien mit Beschluss vom 26.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_12`)


Da mehrere Senate des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht an dem genannten Verhalten beteiligt gewesen seien, sei auch das gesamte Landesgericht für Zivilrechtssachen Wien als befangen anzusehen, über den nunmehr geltend gemachten Unterhaltsanspruch zu entscheiden.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Dr. Grohmann als weitere Richter in der beim Landesgericht für Zivilrechtssachen Wien zu AZ 33 Cg 21/10s anhängigen Rechtssache der klagenden Partei Bachkraft Gesellschaft mbH, Salmweg 829, 4891 Schachen, Österreich, vertreten durch Dr. Gerhard Kornek, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 53.176,92 EUR sA, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Bachkraft Gesellschaft mbH` (organisation)
- `Salmweg 829, 4891 Schachen, Österreich` (address)
- `Dr. Gerhard Kornek` (person)

**Example 4** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_8`)


Das Landesgericht für Zivilrechtssachen Wien legte die Akten dem Obersten Gerichtshof gemäß § 9 Abs 4 AHG vor.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_8`)


Das Landesgericht für Zivilrechtssachen Wien gab der gegen das Ersturteil gerichteten Berufung des Beklagten mit dem (dessen Verfahrenshelfer am 17.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_11`)


diese Entscheidung wurde vom Landesgericht für Zivilrechtssachen Wien später bestätigt.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 7** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_5`)


Diesen Ablehnungsantrag hat das Landesgericht für Zivilrechtssachen Wien am 19.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 8** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_11`)


9. 2009 hat das Landesgericht für Zivilrechtssachen Wien am 12.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 9** (doc_id: `deanon_260716_TRAIN/4Nc30_22g`) (sent_id: `deanon_260716_TRAIN/4Nc30_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Iris Gscheider, vertreten durch Dr. Sabine C.M. Deutsch, Rechtsanwältin in Riegersburg, gegen die beklagte Partei Mag. Annette Salzbauer, als Masseverwalter im Konkursverfahren über das Vermögen von Lynn Galleitner (AZ 26 S 10/21x des Landesgerichts für Zivilrechtssachen Graz), vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Graz, wegen Unterlassung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der unmittelbar beim Obersten Gerichtshof eingebrachte Delegierungsantrag samt Beilagen wird dem Landesgericht für Zivilrechtssachen Graz als Erstgericht zu AZ 10 Cg 83/22z zur geschäftsordnungsgemäßen Behandlung übermittelt. Begründung:  Rechtliche Beurteilung [1]

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Graz` | `Landesgericht für Zivilrechtssachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Schwarzenbacher` (person)
- `MMag. Matzka` (person)
- `Iris Gscheider` (person)
- `Dr. Sabine C.M. Deutsch` (person)
- `Mag. Annette Salzbauer` (person)
- `Lynn Galleitner` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `GRAF ISOLA Rechtsanwälte GmbH` (organisation)
- `Obersten Gerichtshof` (organisation)

</details>

---

## `Landesgericht für Strafsachen` 🏆

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `82348475`  
**Description:**
Matches 'Landesgericht für Strafsachen' followed by a city name.

**Content:**
```
(?<!\w)(Landesgericht\s+für\s+Strafsachen\s+[A-Z][a-zA-Z]+)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 14 | 14 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 0 | 3232 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Viktor Meisterernst` (person)
- `Dr. Stefan Tydeck` (person)

**Example 1** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__4`)


Text Gründe: Das Landesgericht für Strafsachen Wien verhängte mit Beschluss vom 9. Dezember 2011 über Mag. Türkan Kirstin Bierwolf die Untersuchungshaft aus den Gründen der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit b und lit d StPO (ON 12).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Kirstin Bierwolf` (person)

**Example 2** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__6`)


Dem Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß §§ 14 und 15 dieser Verordnung aufgetragen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 3** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__28`)


8. Das Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 4** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__30`)


Mit Blick auf § 292 letzter Satz StPO sah sich der Oberste Gerichtshof veranlasst, dem Landesgericht für Strafsachen Graz aufzutragen, gemäß §§ 14 und 15 der Kaiserlichen Verordnung vorzugehen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_5`)


Dieser Beschluss wird aufgehoben und es wird dem Landesgericht für Strafsachen Graz aufgetragen, im Verfahren AZ 16 Hv 32/15a über den Widerruf zu entscheiden.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 6** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_14`)


Die Sanktionsrüge (Z 11 zweiter Fall) wendet sich gegen die als nach § 33 Abs 1 Z 2 StGB strafschärfend gewertete Verurteilung des Angeklagten durch das Landesgericht für Strafsachen Wien vom 16. Februar 2012, AZ 62 Hv 10/12m, (ua) wegen Vergehen des unerlaubten Umgangs mit Suchtmitteln (US 4, 9; ON 97).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Example 7** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Landesgerichts für Strafsachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__9`)


Die am 22. Februar 2019 – innerhalb der Frist des § 467 Abs 1 StPO (vgl Zustellnachweis an ON 19) – ausgeführte Berufung des Robert Unterdörfer (ON 21) wies das Landesgericht für Strafsachen Wien als Berufungsgericht mit Beschluss vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), gemäß § 470 Z 1 StPO als unzulässig zurück, weil die am 27. November 2018 zur Post gegebene Rechtsmittelanmeldung gegen das am 23. November 2018 verkündete Urteil verspätet gewesen sei.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Robert Unterdörfer` (person)

**Example 9** (doc_id: `deanon_260716_TRAIN/14Ns5_20a`) (sent_id: `deanon_260716_TRAIN/14Ns5_20a_5`)


Die Akten werden dem Oberlandesgericht Wien zurückgestellt. Gründe:  Rechtliche Beurteilung Der Wohnsitz des Angeklagten und Antragsgegners im Sprengel eines anderen Gerichts (ON 16 iVm ON 15 und ON 1 S 4 und 6) ist ebensowenig ein wichtiger Grund im Sinn des § 39 Abs 1 StPO wie der Umstand, dass sich der – von der Mindestsicherung lebende – Angeklagte die Kosten für die Anreise zum Landesgericht für Strafsachen Wien ersparen würde (RIS-Justiz RS0129146;

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_4`)


Text Gründe: Gegen Tomsilav Ayik ist beim Landesgericht für Strafsachen Wien ein - im Stadium der Hauptverhandlung befindliches - Verfahren wegen der Verbrechen des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG anhängig, in dem sich der Angeklagte seit 5. April 2010 in Untersuchungshaft befindet (ON 20).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Ayik` (person)

**Example 11** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_10`)


Aus Anlass eines vom Angeklagten am 17. Februar 2017 eingebrachten Antrags auf Aufhebung der Untersuchungshaft (ON 95) setzte das Landesgericht für Strafsachen Graz mit Beschluss vom 23. Februar 2017 die am 7. September 2016 verhängte (ON 11) – und danach wiederholt prolongierte (ON 32, 71) – Untersuchungshaft aus den Haftgründen der Flucht- und der Tatbegehungsgefahr nach § 173 Abs 2 Z 1 und Z 3 lit a StPO fort (ON 100).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 12** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__57`)


Das Landesgericht für Strafsachen Wien und das Oberlandesgericht Wien als Berufungsgericht haben somit die (grundsätzliche) Verwirklichung des Entschädigungsanspruchs nach § 6 Abs 1 MedienG in Bezug auf die am 4. Juni 2017 auf dem Facebook-Account von www.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Dr. Wieland Skocdopole` (person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc` (person)
- `Wald Fenkraftal GmbH & Co KG` (organisation)

</details>

---

## `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dd53719d`  
**Description:**
Matches the specific entity 'Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH'.

**Content:**
```
(?<!\w)Zacherl\s+Schallab\u00f6ck\s+Proksch\s+Manak\s+Kraft\s+Rechtsanw\u00e4lte\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 2573 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_5`)


Zlatan Schempf, alle vertreten durch die Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH, Wien, wegen Feststellung und Räumung, über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2020, GZ 2 R 122/20d-54, mit dem das Urteil des Landesgerichts Wels vom 27. Juli 2020, GZ 2 Cg 84/18g-47, in der Hauptsache bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH` | `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Zlatan Schempf` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

</details>

---

## `Magistrat der Stadt Wien with Dept` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `36ddca9e`  
**Description:**
Matches 'Magistrat' or 'Magistrats' with 'der Stadt Wien' and includes the department info (e.g., 'Magistratsabteilung 67') if present, to capture the full entity.

**Content:**
```
(?<!\w)(Magistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s*,\s*Magistratsabteilung\s+\d+)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 3858 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_17`)


5. 2009 auch dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten des Jugendamts übernommen wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_52`)


Nach dem im Akt befindlichen Rückschein wurde der Beschluss über die pflegschaftsgerichtliche Genehmigung des Scheidungsvergleichs richtigerweise dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten dieser Dienststelle übernommen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Emma Mittelstaedt` (person)
- `21. Mai 2025` (date)
- `Milena Roesche` (person)
- `25. Juni 1957` (date)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/7Ob119_18b`) (sent_id: `deanon_260716_TRAIN/7Ob119_18b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Geraldine Moßmann, geboren am 7. November 2010, 26. Mai 2013, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Pia Birkenkötter, Vater Lea Schameitat, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Der Vater verpflichtete sich zunächst mit Vergleich des Bezirksgerichts Meidling vom 1. 10. 2010, GZ 1 C 9/10k-9, zu einer monatlichen Unterhaltsleistung von 180 EUR.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Dr. E. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Geraldine Moßmann` (person)
- `7. November` (date)
- `26. Mai 2013` (date)
- `Pia Birkenkötter` (person)
- `Lea Schameitat` (person)
- `Dr. Tassilo Wallentin` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Meidling` (organisation)
- `Bezirksgerichts Meidling` (organisation)

</details>

---

## `Bezirksgericht` 🏆

**F1:** 0.036 | **Precision:** 0.765 | **Recall:** 0.019  

**Format:** `regex`  
**Rule ID:** `8b382c12`  
**Description:**
Matches 'Bezirksgericht' followed by a location, strictly excluding dates (vom) and verbs (eine, gegen, eingereicht, Beschwerde, ein, entrichtet, diesem) and prepositions (zu) immediately following.

**Content:**
```
(?<!\w)(Bezirksgericht\s+(?!vom)(?!eine)(?!gegen)(?!eingereicht)(?!entrichtet)(?!diesem)(?!Beschwerde)(?!ein)(?!zu)(?!bestellten)(?!als)[A-Z][a-zA-Z\s-]+?)(?=[\s.,;:!?]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.765 | 0.019 | 0.036 | 98 | 75 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 75 | 23 | 3938 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Selma Einoeder` (person)
- `Mag. Alexander Gerngross` (person)
- `Mag. Klaus Köck` (person)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_8`)


[3] Mit Antrag vom 21. 2. 2025 beantragte der Kläger – noch vor der vorbereitenden Tagsatzung – die Delegierung der Rechtssache an das Bezirksgericht Dornbirn, weil nicht nur er sowie das Unternehmen, in dessen Kfz-Werkstatt das Fahrzeug repariert worden sei, und dem er im Verfahren den Streit verkündet habe, sondern auch die von ihm in großer Zahl namhaft gemachten Zeugen ihren (Wohn-)Sitz in Vorarlberg hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-Ost` | `Bezirksgericht Graz-Ost` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Judenburg` | `Bezirksgericht Judenburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Gerhard Lohrmann` (person)
- `10. August 1983` (date)
- `Veit Künneken` (person)
- `31. Mai 1967` (date)
- `Bezirksgerichts Feldkirchen` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Feldkirchen` | `Bezirksgericht Feldkirchen` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Nowotny` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Selma Eichler, LLM` (person)
- `13. September` (date)
- `Bezirksgerichts Graz-West` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Bezirksgericht Braunau am Inn` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Dietlind Schiewick` (person)
- `23. Oktober` (date)
- `Bezirkshauptmannschaft Vöcklabruck` (organisation)
- `Gisela Akcakaya, MSc` (person)
- `Ernst Hartjens` (person)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_7`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Kreutzerstraße 7, 4851 Haunolding, Österreich aufhalte (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Bezirksgericht Vöcklabruck` (organisation)
- `Kreutzerstraße 7, 4851 Haunolding, Österreich` (address)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_9`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_13`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_15`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_17`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_20`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_5`)


Das von der Klägerin mit ihrer Klage angerufene Bezirksgericht Schwechat hat die internationale und örtliche Zuständigkeit rechtskräftig verneint (RIS-Justiz RS0046450).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_11`)


Unter Berücksichtigung dieser Vorgaben erscheint eine Zuweisung der Sache an das Bezirksgericht Schwechat als zweckmäßig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Paulina Nüsken` (person)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Oliver Eylart` (person)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_7`)


Das vom Kläger angerufene Bezirksgericht Schwechat sprach rechtskräftig seine (internationale) Unzuständigkeit aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_38`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel und wurde zum anderen die Klage bereits bei diesem Gericht behandelt (6 Nc 31/20s mwN ua).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_8`)


Am 20. 9. 2016 beantragte die Antragstellerin beim Bezirksgericht Josefstadt die Erhöhung der monatlichen Unterhaltszahlung auf 440 EUR ab 1. 9. 2016.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 31** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 32** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 33** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Missed by this rule (FN):**

- `Nenad Panagiotakopoulou` (person)

**Example 34** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__6`)


Das Urteil, das im Übrigen unberührt bleibt, wird in seinem Strafausspruch aufgehoben und dem Bezirksgericht Kufstein im Umfang der Aufhebung die neuerliche Verhandlung und Entscheidung aufgetragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 35** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__22`)


Durch die Verhängung einer (Zusatz-)Geldstrafe von 200 Tagessätzen in Missachtung des durch § 5 Z 5 JGG geänderten Strafrahmens bei ersichtlicher Nichtanwendung des § 37 Abs 1 StGB und demzufolge auch der bei Zusatzstrafen anzuwendenden Strafbemessungsvorschrift des § 31 Abs 1 zweiter Satz StGB hat das Bezirksgericht Kufstein das Gesetz in den genannten Bestimmungen zum Nachteil der Verurteilten verletzt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 36** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__23`)


Der Oberste Gerichtshof sah sich daher gemäß § 292 letzter Satz StPO veranlasst, das Urteil im Strafausspruch aufzuheben und dem Bezirksgericht Kufstein in diesem Umfang die Verfahrenserneuerung aufzutragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Mann` (person)
- `Mag. Anscheringer` (person)
- `Natascha von Bohr` (person)
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Bezirksgerichts Linz` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_5`)


Das Bezirksgericht Linz überwies die Sache dem Bezirksgericht Innere Stadt Wien mit der Begründung örtlicher Unzuständigkeit (vgl ON 1 S 3: „erste Taten in Wien“).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_9`)


In diesem Fall kommt das Verfahren (soweit hier von Interesse) gemäß § 37 Abs 2 zweiter Satz StPO jenem Gericht zu, in dessen Zuständigkeit die frühere Straftat fällt. Zutreffend weist das Bezirksgericht Innere Stadt darauf hin, dass nach der Aktenlage kein Anhaltspunkt für einen Tatort in Wien besteht.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere` | `Bezirksgericht Innere` |

**Example 40** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_4`)


2005 den Beschluss gefasst:  Spruch Für die Durchführung des Strafverfahrens ist das Bezirksgericht Linz zuständig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Example 41** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_5`)


Gründe:  Rechtliche Beurteilung Mit beim Bezirksgericht Linz eingebrachtem Strafantrag vom 28. Juni 2018 (ON 12) legte die Staatsanwaltschaft Linz Daniel Berlage ein „ab ca Mitte Mai 2016 bis … 18. Jänner 2018“ (1) und am 18. Jänner 2018 „in Linz“ (2) gesetztes, als die Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 erster und zweiter Fall, Abs 2 SMG beurteiltes Verhalten zur Last.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Daniel Berlage` (person)

**Example 42** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_12`)


Das Bezirksgericht Linz überwies die Sache „gemäß § 37 Abs 2 StPO“ unter Hinweis auf eine im letztgenannten Verfahren durchgeführte Abfrage aus dem Zentralen Melderegister, aus der sich ergab, dass der Angeklagte von 20. März 2014 bis 5. Mai 2017, sohin zu Beginn des von der Anklage umfassten Tatzeitraums, im Bezirk Amstetten polizeilich gemeldet war (ON 14), wegen örtlicher Unzuständigkeit dem Bezirksgericht St. Pölten (ON 1 S 3 verso).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Bezirksgericht St. Pölten` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_17`)


Die vom Bezirksgericht Linz vertretene Ansicht, die früheste vom Anklagevorwurf erfasste Tat sei an jenem Ort verübt worden, an dem der Angeklagte zur Zeit ihrer Begehung polizeilich gemeldet gewesen sei, findet im Gesetz keine Stütze;

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Example 44** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_7`)


Mit unangefochten in Rechtskraft erwachsenem Beschluss vom 7. Mai 2013 (ON 39) bestimmte das Bezirksgericht Steyr die vom Privatankläger zu ersetzenden „Kosten der Vertretung des Privatangeklagten“ – nämlich für eine Intervention beim Bezirksgericht Steyr, für die Teilnahme an der Hauptverhandlung und für den Kostenbestimmungsantrag unter gleichzeitiger Abweisung des Mehrbegehrens – (aufgrund eines Rechenfehlers statt mit 544,44 Euro) mit 342,08 Euro (1./) sowie vom Angeklagten für sein Erscheinen vor Gericht geltend gemachte (Fahrt-)Kosten (ON 32a S 2) mit 15,40 Euro (2./).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 45** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_8`)


Über Antrag des Verfahrenshilfeverteidigers berichtigte das Bezirksgericht Steyr mit Beschluss vom 4. November 2015 (ON 44) den „Rechnungsendbetrag“ zu 1./ (als offenkundigen Rechenfehler) auf 544,44 Euro.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 46** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_13`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, verletzt der Vorgang, dass es das Bezirksgericht Innsbruck unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Gaisert im Verfahren AZ 23 BE29/06a des Landesgerichts Innsbruck gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich das Vollzugsgericht in Kenntnis zu setzen, § 494a Abs 7 StPO, wonach das erkennende Gericht all jene Gerichte unverzüglich zu verständigen hat, deren Vorentscheidungen von einer Entscheidung nach § 494a Abs 1 und 6 StPO betroffen sind.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Missed by this rule (FN):**

- `Andreas Gaisert` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_16`)


Das Bezirksgericht Innsbruck hätte daher sogleich nach Fassung seines Probezeitverlängerungsbeschlusses - und nicht erst im Zuge der Endverfügung vom 31. März 2010 - das Vollzugsgericht davon in Kenntnis setzen müssen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 48** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_6`)


Nach dem Klagsvorbringen sei er am 19. 8. 2009 im Strandbad Bezirksgericht Donaustadt beim Verlassen des Wassers von einem ca zwei Fäuste großen Stein ins Gesicht getroffen worden, der vom damals sechsjährigen Beklagten geworfen worden sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Donaustadt` | `Bezirksgericht Donaustadt` |

**Example 49** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_17`)


Verwiesen werde auf einen Akt der Staatsanwaltschaft Bezirksgericht Voitsberg, in welchem gegen den Schädiger Vorerhebungen geführt, jedoch mangels Deliktsfähigkeit eingestellt worden seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Voitsberg` | `Bezirksgericht Voitsberg` |

**Example 50** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Xaver Springinsgut, Rechtsanwalt in St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jähnel in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Alpen Nexlex AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Schulgartenweg 18, 9872 Grantsch, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Jiran, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Amstetten` | `Bezirksgericht Amstetten` |

**Missed by this rule (FN):**

- `Dr. Xaver Springinsgut` (person)
- `St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich` (address)
- `Elfriede Jähnel` (person)
- `Bezirksgerichts Innsbruck` (organisation)
- `Bezirksgerichts Amstetten` (organisation)
- `Landesgericht Linz` (organisation)
- `Alpen Nexlex AG` (organisation)
- `Schulgartenweg 18, 9872 Grantsch, Österreich` (address)
- `Roman Jiran` (person)

**Example 51** (doc_id: `deanon_260716_TRAIN/3Nc11_13t`) (sent_id: `deanon_260716_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Mikulska Textil GmbH, Kohleck 4, 6794 Partenen, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin TraunWind GmbH, Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Dr. Neumayr` (person)
- `Dr. Jensik` (person)
- `Mikulska Textil GmbH` (organisation)
- `Kohleck 4, 6794 Partenen, Österreich` (address)
- `Dr. Clemens Thiele` (person)
- `TraunWind GmbH` (organisation)
- `Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich` (address)

**Example 52** (doc_id: `deanon_260716_TRAIN/3Nc32_19i`) (sent_id: `deanon_260716_TRAIN/3Nc32_19i_5`)


Das Bezirksgericht Telfs legte den Akt unmittelbar (dh ohne jede sonstige Erledigung) von Amts wegen dem Obersten Gerichtshof zwecks Entscheidung über eine Ordination nach § 28 JN vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Telfs` | `Bezirksgericht Telfs` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/3Nc32_19i`) (sent_id: `deanon_260716_TRAIN/3Nc32_19i_8`)


Da das angerufene Bezirksgericht Telfs bislang noch nicht negativ über seine Zuständigkeit entschieden hat, kommt eine Ordination nach § 28 JN nicht in Betracht.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Telfs` | `Bezirksgericht Telfs` |

**Example 54** (doc_id: `deanon_260716_TRAIN/3Nc39_24a`) (sent_id: `deanon_260716_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei PhD Miklos Juergens, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Dumberger Technik Limited, Dr.-Franz-Reinprecht-Weg 33, 9913 Abfaltersbach, Österreich, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Kodek` (person)
- `PhD Miklos Juergens` (person)
- `Dr. Florian Johann Ernst Knaipp` (person)
- `Dumberger Technik Limited` (organisation)
- `Dr.-Franz-Reinprecht-Weg 33, 9913 Abfaltersbach, Österreich` (address)

**Example 55** (doc_id: `deanon_260716_TRAIN/3Nc39_24a`) (sent_id: `deanon_260716_TRAIN/3Nc39_24a_29`)


Als örtlich zuständiges Exekutionsgericht für die beabsichtigte Rechteexekution ist das Bezirksgericht Salzburg zu bestimmen, weil die Rhein Kraftnor.at GmbH als Registrierungsstelle der von der beabsichtigten Exekutionsführung betroffenen Domain der Verpflichteten im Sprengel dieses Gerichts ihren Sitz hat.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Missed by this rule (FN):**

- `Rhein Kraftnor.at` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Kosfelder+Gerasimowitsch KI GmbH, Webergarten 4c, 2534 Maria Raisenmarkt, Österreich, vertreten durch Dr. Christian Fuchshuber LL.M., Rechtsanwalt in Innsbruck, gegen die beklagte Partei Gastronomie Seezor GmbH, Psaltersteig 61, 4624 Felling, Österreich, vertreten durch Dr. Gerhard Strobich, Rechtsanwalt in Trofaiach, wegen 5.873,18 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag, zur Verhandlung und Entscheidung in dieser Rechtssache anstelle des Bezirksgerichts Innsbruck das Bezirksgericht Leoben zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leoben` | `Bezirksgericht Leoben` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Kosfelder+Gerasimowitsch KI GmbH` (organisation)
- `Webergarten 4c, 2534 Maria Raisenmarkt, Österreich` (address)
- `Dr. Christian Fuchshuber LL.M.` (person)
- `Gastronomie Seezor GmbH` (organisation)
- `Psaltersteig 61, 4624 Felling, Österreich` (address)
- `Dr. Gerhard Strobich` (person)
- `Bezirksgerichts Innsbruck` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_4`)


Text Begründung: Die Klägerin mit Sitz in Innsbruck begehrt mit ihrer beim Bezirksgericht Innsbruck eingebrachten Klage 5.873,18 EUR sA für der Beklagten vereinbarungsgemäß erbrachte Reisedienstleistungen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 58** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_8`)


Die Beklagte beantragte die Delegierung der Rechtssache an das Bezirksgericht Leoben.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leoben` | `Bezirksgericht Leoben` |

**Example 59** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_14`)


Das Bezirksgericht Innsbruck sprach sich gleichermaßen gegen die beantragte Delegierung aus, verwies auf die Möglichkeit der Zeugenvernehmung mittels Videokonferenz nach § 277 ZPO und (deswegen) auf den fehlenden Vorteil für die Parteien, der mit einer allfälligen Delegierung verbunden wäre.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 60** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und den Hofrat Dr. Steger als weitere Richter in der Pflegschaftssache des mj Aron Margwarth, geboren am 29. März 1957, Vater Klaus Rufer, vertreten durch Prof. Dr. Georg Zanger, Rechtsanwalt in Wien, wegen Obsorge, über den Delegierungsantrag der Mutter Rafaela Erreth, vertreten durch Mag. Britta Schönhart-Loinig, Rechtsanwältin in Wien, den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Pflegschaftssache vom Bezirksgericht Gänserndorf an das Bezirksgericht Villach wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Dr. Grohmann` (person)
- `Dr. Steger` (person)
- `Aron Margwarth` (person)
- `29. März 1957` (date)
- `Klaus Rufer` (person)
- `Prof. Dr. Georg Zanger` (person)
- `Rafaela Erreth` (person)
- `Mag. Britta Schönhart-Loinig` (person)
- `Bezirksgericht Gänserndorf` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_22`)


7. 2019 die Delegierung der Pflegschaftssache an das Bezirksgericht Villach nach § 31 Abs 1 JN.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 62** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_28`)


Da der Mittelpunkt der Lebensführung des Kindes nunmehr in Velden liege und offene Anträge nicht gegen eine Zuständigkeitsübertragung sprächen, sei das Bezirksgericht Villach besser in der Lage, die pflegschaftsgerichtlichen Agenden zu besorgen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 63** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_36`)


Die Handhabung des pflegschaftsgerichtlichen Schutzes des Kindes sei durch das Bezirksgericht Gänserndorf wirksamer gestaltbar als durch das Bezirksgericht Villach, das die Familie überhaupt noch nicht kenne.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Bezirksgericht Gänserndorf` (organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_57`)


das delegierte Bezirksgericht Villach müsste sich in den mittlerweile bereits umfangreichen Pflegschaftsakt erst einarbeiten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 65** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_61`)


Dass in diesem Verfahrensstadium die Delegierung der Pflegschaftssache an das Bezirksgericht Villach dem Kindeswohl besser entsprechen würde als die Weiterführung des Obsorge- und Kontaktrechtsverfahrens durch den bisher zuständigen Richter des Bezirksgerichts Gänserndorf, ist ebensowenig zu erkennen wie eine dadurch erzielbare Verfahrensbeschleunigung und Erleichterung des Gerichtszugangs für sämtliche Beteiligte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Bezirksgerichts Gänserndorf` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_62`)


Der Umstand, dass der Minderjährige derzeit im Sprengel des Bezirksgerichts Villach wohnt und für die Mutter seine Betreuung bei Terminen am Bezirksgericht Villach leichter zu organisieren wäre als beim Bezirksgericht Gänserndorf, reicht daher für eine Bejahung der Zweckmäßigkeit iSd § 31 Abs 1 JN nicht aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Bezirksgerichts Villach` (organisation)
- `Bezirksgericht Gänserndorf` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/6Ob199_10y`) (sent_id: `deanon_260716_TRAIN/6Ob199_10y_4`)


Im vorliegenden Verfahren geht es um die pflegschaftsbehördliche Genehmigung eines Vergleichs vor dem Bezirksgericht Meidling.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Meidling` | `Bezirksgericht Meidling` |

**Example 68** (doc_id: `deanon_260716_TRAIN/9Nc65_19m`) (sent_id: `deanon_260716_TRAIN/9Nc65_19m_4`)


Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 69** (doc_id: `deanon_260716_TRAIN/9Nc65_19m`) (sent_id: `deanon_260716_TRAIN/9Nc65_19m_27`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung der vorliegenden Rechtssache an das Bezirksgericht Schwechat zu erfolgen, weil der Abflugort im Sprengel dieses Gerichts gelegen war.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Marlene Friss`(person)
- `WestTelekom GmbH`(organisation)
- `Rehwald 11, 4723 Fronberg, Österreich`(address)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Braunau` — partial — pred is substring of gold: `Bezirksgericht Braunau am Inn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Bezirksgericht Braunau am Inn`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_26`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Hall (in Tirol) verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Hall (in Tirol)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hall (in Tirol)`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Basil Biewer anhängig.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)
- `Basil Biewer`(person)

**Example 5** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_10`)


Für ihn ist ein Sachwalter bestellt, der seit 2011 alle Angelegenheiten (§ 268 Abs 3 Z 3 ABGB) zu besorgen hat (siehe den Beschluss des Bezirksgericht Bezirksgericht Freistadt vom 15.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Freistadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Freistadt`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_5`)


Das Bezirksgericht Linz überwies die Sache dem Bezirksgericht Innere Stadt Wien mit der Begründung örtlicher Unzuständigkeit (vgl ON 1 S 3: „erste Taten in Wien“).

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Linz`(organisation)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__10`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_12`)


Das Bezirksgericht Linz überwies die Sache „gemäß § 37 Abs 2 StPO“ unter Hinweis auf eine im letztgenannten Verfahren durchgeführte Abfrage aus dem Zentralen Melderegister, aus der sich ergab, dass der Angeklagte von 20. März 2014 bis 5. Mai 2017, sohin zu Beginn des von der Anklage umfassten Tatzeitraums, im Bezirk Amstetten polizeilich gemeldet war (ON 14), wegen örtlicher Unzuständigkeit dem Bezirksgericht St. Pölten (ON 1 S 3 verso).

**False Positives:**

- `Bezirksgericht St` — partial — pred is substring of gold: `Bezirksgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Linz`(organisation)
- `Bezirksgericht St. Pölten`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_5`)


Text Begründung: Die Obsorge für den Minderjährigen steht allein der Mutter zu. Mit der am 20. 8. 2012 beim Bezirksgericht Bezirksgericht Bregenz eingebrachten Klage begehrte der Minderjährige von einem in Deutschland wohnhaften minderjährigen Beklagten Schadenersatz von 3.850 EUR sA und die Feststellung seiner Haftung für sämtliche aus dessen Steinwurf resultierenden Spät- und Dauerfolgen.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Bregenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Bregenz`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_67`)


8. 2012 beim gemäß Art 5 Nr 3 EuGVVO zuständigen Bezirksgericht Bezirksgericht Baden (Gericht des Ortes, an dem das schädigende Ereignis eingetreten ist) im Elektronischen Rechtsverkehr eingebracht.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Baden`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Baden`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_7`)


Text Begründung: [1] Beim Bezirksgericht St. Johann im Pongau ist zu AZ 455 A 78/22f das Verlassenschaftsverfahren nach dem 2022 verstorbenen Erblasser anhängig.

**False Positives:**

- `Bezirksgericht St` — partial — pred is substring of gold: `Bezirksgericht St. Johann im Pongau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht St. Johann im Pongau`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_6`)


Für die Bewilligung und die Vollziehung der beabsichtigten Exekution gegen die Zweitbeklagte auf Urteilsveröffentlichung wird das Bezirksgericht Innere Stadt Wien als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_9`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_19`)


Die Ordinationsvoraussetzungen gemäß § 28 Abs 1 Z 2 JN sind daher erfüllt. Dem Ordinationsantrag ist somit stattzugeben und zweckmäßigerweise das Bezirksgericht Innere Stadt Wien als zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_4`)


Lieselotte Sedlmair, und 2. Yorick Bergbauer, wegen Erlassung einer einstweiligen Verfügung, infolge der Vorlage des Aktes 1 C 16/12t des Bezirksgerichts Wiener Neustadt zur Entscheidung über den negativen Kompetenzkonflikt mit dem Bezirksgericht Mürzzuschlag nach § 47 JN den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag auf Erlassung der einstweiligen Verfügung ist das Bezirksgericht Wiener Neustadt zuständig.

**False Positives:**

- `Bezirksgericht Wiener` — partial — pred is substring of gold: `Bezirksgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Sedlmair`(person)
- `Yorick Bergbauer`(person)
- `Bezirksgerichts Wiener Neustadt`(organisation)
- `Bezirksgericht Mürzzuschlag`(organisation)
- `Bezirksgericht Wiener Neustadt`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_7`)


Das Bezirksgericht Mürzzuschlag erklärte sich mit am selben Tag gefasstem Beschluss gemäß § 387 Abs 4 EO für unzuständig und überwies das Verfahren nach § 44 JN an das nicht offenbar unzuständige Bezirksgericht Wiener Neustadt.

**False Positives:**

- `Bezirksgericht Wiener` — partial — pred is substring of gold: `Bezirksgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mürzzuschlag`(organisation)
- `Bezirksgericht Wiener Neustadt`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_9`)


Das Bezirksgericht Wiener Neustadt stellte den Provisorialantrag zunächst den Antragsgegnern zur Äußerung zu. Es fasste nach einer Anfrage beim Zentralen Melderegister dann aber am 8.

**False Positives:**

- `Bezirksgericht Wiener` — partial — pred is substring of gold: `Bezirksgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Wiener Neustadt`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_12`)


Das Bezirksgericht Wiener Neustadt könne daher seine Unzuständigkeit aussprechen.

**False Positives:**

- `Bezirksgericht Wiener` — partial — pred is substring of gold: `Bezirksgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Wiener Neustadt`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_15`)


Das Bezirksgericht Wiener Neustadt legte den Akt dem Obersten Gerichtshof zur Entscheidung über den negativen Kompetenzkonflikt nach § 47 JN vor.

**False Positives:**

- `Bezirksgericht Wiener` — partial — pred is substring of gold: `Bezirksgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Wiener Neustadt`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/7Ob4_12g`) (sent_id: `deanon_260716_TRAIN/7Ob4_12g_5`)


Text Begründung: Über Einrede der örtlichen Unzuständigkeit erklärte sich das zunächst angerufene Bezirksgericht Hall in Tirol für unzuständig und überwies die Rechtssache aufgrund des (Eventual-)Antrags der Klägerin („für den Fall, dass das [Erst-]Gericht seine Unzuständigkeit ausspricht“) gemäß § 261 Abs 6 ZPO an das nicht offenbar unzuständige Bezirksgericht Wolfsberg, in dessen Sprengel sich der Sitz der Beklagten befindet.

**False Positives:**

- `Bezirksgericht Hall` — partial — pred is substring of gold: `Bezirksgericht Hall in Tirol`
- `Bezirksgericht Wolfsberg` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Hall in Tirol`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/7Ob4_12g`) (sent_id: `deanon_260716_TRAIN/7Ob4_12g_7`)


das Bezirksgericht Wolfsberg als allgemeiner Gerichtsstand der Beklagten, welche dessen - durch Parteienvereinbarung begründbare - Zuständigkeit ebenfalls heranziehe, sei hingegen „nicht offenbar unzuständig“.

**False Positives:**

- `Bezirksgericht Wolfsberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `ÖBB Abbreviation` 🏆

**F1:** 0.004 | **Precision:** 0.692 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `adbc5b3b`  
**Description:**
Matches the abbreviation ÖBB (Österreichische Bundesbahnen).

**Content:**
```
(?<!\w)(\u00d6BB)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.692 | 0.002 | 0.004 | 13 | 9 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 4 | 2516 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `ÖBB-Holding AG` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_80`)


Auch im ÖBB-Dienstrecht der 'Allgemeinen Vertragsbedingungen für Dienstverträge bei den Österreichischen Bundesbahnen' (AVB), die als Vertragsschablone für die ÖBB-Angestellten mit einem Eintritt vor dem 01.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |
| `ÖBB` | `ÖBB` |

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_83`)


Von dieser Regelung betroffen sind rund 27.000 ÖBB-Angestellte.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_86`)


Ohne eine Neuregelung werden die betroffenen ÖBB-Angestellten (auch wenn sie bereits im Ruhestand sind) die Neufestsetzung ihres Vorrückungsstichtages begehren und die Gehaltsdifferenz der letzten 3 Jahre (Verjährungsfrist) geltend machen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 4** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_87`)


Daraus ergibt sich auch für die Zukunft eine finanzielle Belastung für die ÖBB, sowie eine höhere Belastung des Bundes aus den künftigen Ruhegenüssen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_213`)


GP 1) wird dazu ausgeführt, dass ohne Neuregelung die betroffenen ÖBB-Angestellten die Neufestsetzung ihres Vorrückungsstichtags begehren und die Gehaltsdifferenz in den letzten drei Jahren (Verjährungsfrist) geltend machen werden.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_214`)


Daraus ergebe sich eine finanzielle Belastung für die ÖBB und für den Bund.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Verfassungsgerichtshofs` (organisation)
- `Verfassungsgerichtshof` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob169_15g`) (sent_id: `deanon_260716_TRAIN/1Ob169_15g_55`)


C-417/13,ÖBB-Personenverkehr, ECLI:EU:C:2015:38, Rn 66 f).

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob99_24h`) (sent_id: `deanon_260716_TRAIN/2Ob99_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende und die Hofräte MMag. Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei ÖBB-Infrastruktur Aktiengesellschaft, Kathreinweg 48, 4572 Schalchgraben, Österreich, vertreten durch Dr. Martin Wandl und Dr. Wolfgang Krempl, Rechtsanwälte in St. Pölten, gegen die beklagten Parteien 1. Melina McNaughtan, 2. Ophelia Middelkamp, und 3. ÖkR HR Karlheinz Göttl, alle vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, wegen 54.038,42 EUR sA, über die Revisionen sämtlicher Streitteile gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. März 2024, GZ 11 R 5/24w-61, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Linz vom 28. November 2023, GZ 5 Cg 82/22m-54, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Infrastruktur Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `ÖBB-Infrastruktur Aktiengesellschaft`(organisation)
- `Kathreinweg 48, 4572 Schalchgraben, Österreich`(address)
- `Dr. Martin Wandl`(person)
- `Dr. Wolfgang Krempl`(person)
- `Melina McNaughtan`(person)
- `Ophelia Middelkamp`(person)
- `ÖkR HR Karlheinz Göttl`(person)
- `Dr. Peter Lindinger`(person)
- `Dr. Andreas Pramer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Personenverkehr AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Monika Lanz`(person)
- `Wolfgang Cadilek`(person)
- `Hon.-Prof. Dieter Kovacs`(person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte`(organisation)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

**False Positives:**

- `ÖBB` — similar text (different position): `ÖBB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB`(organisation)
- `ÖBB-Holding AG`(organisation)

</details>

---

## `GmbH Preceded by Article` 🏆

**F1:** 0.008 | **Precision:** 0.515 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `252d45b4`  
**Description:**
Matches 'GmbH' entities preceded by articles ('der', 'die', 'das') or 'Firma', but strictly limits the preceding word to a multi-letter capitalized noun or 'Firma', excluding the prefix from the capture group.

**Content:**
```
(?<!\w)(?:der|die|das|Firma)\s+([A-Z][a-zA-Z]{2,}(?:\s+[A-Z][a-zA-Z]+)*(?:\s+&\s+[A-Z][a-zA-Z]+)*(?:\s+Medien)?\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.515 | 0.004 | 0.008 | 33 | 17 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 17 | 16 | 3699 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_15`)


Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Albrucklog Event GmbH als übernehmende Gesellschaft verschmolzen, die am 26.

| Predicted | Gold |
|---|---|
| `Albrucklog Event GmbH` | `Albrucklog Event GmbH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der QVAO Planung GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

| Predicted | Gold |
|---|---|
| `QVAO Planung GmbH` | `QVAO Planung GmbH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Medien Lexsudtal GmbH hinweist.

| Predicted | Gold |
|---|---|
| `Medien Lexsudtal GmbH` | `Medien Lexsudtal GmbH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_9`)


Den weiters mit Strafantrag vom 1. September 2011 (ON 3) erhobenen Vorwurf, der Angeklagte habe am 8. Juli 2010 die Verfügungsberechtigten der Nexlexlog Holding GmbH auch zur leihweisen Überlassung einer Kaffeemaschine im Wert von 390 Euro und eines sogenannten Schokodispensers Exquisit im Wert von 1.328 Euro veranlasst, erachtete das Erstgericht für nicht erweislich.

| Predicted | Gold |
|---|---|
| `Nexlexlog Holding GmbH` | `Nexlexlog Holding GmbH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ludmilla Bonauer, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Henriette Geißendorf, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Korp Rechtsanwalts GmbH` | `Korp Rechtsanwalts GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Ludmilla Bonauer` (person)
- `Henriette Geißendorf` (person)
- `Puttinger Vogl Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob139_18z`) (sent_id: `deanon_260716_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Verena Tappendorff Inc., Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Sabine Martinsson, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Touristik Synberbruck GmbH, Fridau 56l, 7433 Bergwerk, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Touristik Synberbruck GmbH` | `Touristik Synberbruck GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Verena Tappendorff` (person)
- `Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich` (address)
- `Mag. Ralph Kilches` (person)
- `Mag. Sabine Martinsson` (person)
- `Fridau 56l, 7433 Bergwerk, Österreich` (address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/3Ob139_20t`) (sent_id: `deanon_260716_TRAIN/3Ob139_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der gefährdeten Partei Dr. Günter Geusau, Rechtsanwalt in Wels, als Masseverwalter über das Vermögen der Kelwald GmbH, Friedelstraße 1, 8350 Pertlstein, Österreich, gegen die Gegnerin der gefährdeten Partei Füsslin Telekom GmbH, Kaltbach 4, 8733 Hof, Österreich, vertreten durch Stock Rechtsanwälte PartnerschaftsgesellschaftmbB in Siegen, Deutschland, im Einvernehmen mit Mag. Martin Schönmair, Rechtsanwalt in Wels, wegen einstweiliger Verfügung nach § 381 Z 1 EO (265.239,60 EUR), aus Anlass des außerordentlichen Revisionsrekurses der gefährdeten Partei gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 1. Juli 2020, GZ 22 R 129/20g-12, mit dem der Beschluss des Bezirksgerichts Wels vom 3. April 2020, GZ 8 C 302/20g-2, abgeändert wurde, den Beschluss gefasst:  Spruch Aus Anlass des Revisionsrekurses der gefährdeten Partei wird der Beschluss des Rekursgerichts, mit dem über den Rekurs der Gegnerin der gefährdeten Partei meritorisch entschieden wurde, als nichtig aufgehoben, und dem Erstgericht aufgetragen, den Schriftsatz der Gegnerin der gefährdeten Partei vom 29. April 2020 (nur) als Widerspruch gegen die Einstweilige Verfügung des Erstgerichts vom 3. April 2020, GZ 8 C 302/20g-2, zu behandeln und darüber das gesetzmäßige Verfahren einzuleiten.

| Predicted | Gold |
|---|---|
| `Kelwald GmbH` | `Kelwald GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Roch` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Dr. Günter Geusau` (person)
- `Friedelstraße 1, 8350 Pertlstein, Österreich` (address)
- `Füsslin Telekom GmbH` (organisation)
- `Kaltbach 4, 8733 Hof, Österreich` (address)
- `Stock Rechtsanwälte PartnerschaftsgesellschaftmbB` (organisation)
- `Mag. Martin Schönmair` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Wels` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_10`)


Text Entscheidungsgründe: Folgender vom Berufungsgericht übernommener und nach dem Akteninhalt ergänzter Sachverhalt ist unstrittig: Mit Beschluss des Erstgerichts vom 18. Juli 2006 wurde über das Vermögen der Derder GmbH (in der Folge: Gemeinschuldnerin) der Konkurs eröffnet.

| Predicted | Gold |
|---|---|
| `Derder GmbH` | `Derder GmbH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der RheinLebensmittel Systeme GmbH, FN FN982022c, wegen § 10 Abs 2 FBG, über den Revisionsrekurs des Österreichischen Verbandes Gemeinnütziger Bauvereinigungen Revisionsverband, 1010 Wien, Bösendorferstraße 7, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 3. September 2020, GZ 6 R 158/20d-6, womit der Rekurs gegen den Beschluss des Handelsgerichts Wien vom 20. Juli 2020, GZ 72 Fr 3266/20f-3, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `RheinLebensmittel Systeme GmbH` | `RheinLebensmittel Systeme GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `FN982022c` (business_register_number)
- `KWR Karasek Wietrzyk Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_9`)


Ihre ersten Gesellschafter waren Dr. Jeanne Ponzio mit einer voll eingezahlten Stammeinlage von 22.400 EUR sowie die Alwaldtra Vertrieb GmbH mit einer voll eingezahlten Stammeinlage von 12.600 EUR.

| Predicted | Gold |
|---|---|
| `Alwaldtra Vertrieb GmbH` | `Alwaldtra Vertrieb GmbH` |

**Missed by this rule (FN):**

- `Dr. Jeanne Ponzio` (person)

**Example 10** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN401718s ist im Firmenbuch des Handelsgerichts Wien die Bosman Gastronomie GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

| Predicted | Gold |
|---|---|
| `Bosman Gastronomie GmbH` | `Bosman Gastronomie GmbH` |

**Missed by this rule (FN):**

- `FN401718s` (business_register_number)
- `Handelsgerichts Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/6Ob69_23z`) (sent_id: `deanon_260716_TRAIN/6Ob69_23z_12`)


Eine – diese betreffende und nur für eine Übergangszeit bis Ende August 2019 gültige – Vereinbarung sei nicht mit ihm, sondern mit der Wahnschafe IT GmbH (im Weiteren kurz: GmbH) geschlossen worden.

| Predicted | Gold |
|---|---|
| `Wahnschafe IT GmbH` | `Wahnschafe IT GmbH` |

**Example 12** (doc_id: `deanon_260716_TRAIN/7Ob137_17y`) (sent_id: `deanon_260716_TRAIN/7Ob137_17y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Elias Hemerle, vertreten durch die Breiteneder Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Mooshuber Planung AG, Schustergasse 57, 4682 Brunau, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Mai 2017, GZ 4 R 19/17v-16, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Breiteneder Rechtsanwalt GmbH` | `Breiteneder Rechtsanwalt GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Dr. E. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Dr. Elias Hemerle` (person)
- `Mooshuber Planung AG` (organisation)
- `Schustergasse 57, 4682 Brunau, Österreich` (address)
- `Binder Grösswang Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_14`)


2012 beauftragte sie die WestMedien GmbH (in Hinkunft: Werkunternehmerin) mit der Errichtung eines Wintergartens.

| Predicted | Gold |
|---|---|
| `WestMedien GmbH` | `WestMedien GmbH` |

**Example 14** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_15`)


Diese zog für die Lieferung der Isolierglasscheiben die Chmieleffski Umwelt GmbH (in Hinkunft Subunternehmerin) bei.

| Predicted | Gold |
|---|---|
| `Chmieleffski Umwelt GmbH` | `Chmieleffski Umwelt GmbH` |

**Example 15** (doc_id: `deanon_260716_TRAIN/7Ob21_20v`) (sent_id: `deanon_260716_TRAIN/7Ob21_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Bernhard Freyberg, vertreten durch die Niedermayr Rechtsanwalt GmbH in Steyr, gegen die beklagte Partei Dr. Flora Precht, vertreten durch Dr. Heinz Stöger, Rechtsanwalt in Wien, wegen 585.800 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2019, GZ 1 R 150/19i-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Niedermayr Rechtsanwalt GmbH` | `Niedermayr Rechtsanwalt GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Bernhard Freyberg` (person)
- `Dr. Flora Precht` (person)
- `Dr. Heinz Stöger` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_14`)


2015 teilte die Holz Bersud GmbH, Großhandel SKODA Österreich, dem Kläger mit, dass an seinem Fahrzeug Nacharbeiten erforderlich seien.

| Predicted | Gold |
|---|---|
| `Holz Bersud GmbH` | `Holz Bersud GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_27`)


Der Kläger konsumierte die bewilligten Leistungen im September und November 2009 bei der Pharma Glanzsynstein GmbH.

**False Positives:**

- `Pharma Glanzsynstein GmbH` — partial — pred is substring of gold: `Pharma Glanzsynstein GmbH.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pharma Glanzsynstein GmbH.`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__3`)


Kopf Der Oberste Gerichtshof hat am 11. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Leitner als Schriftführerin in der Medienrechtssache des Antragstellers Georgia Bruckmeir gegen die Antragsgegnerin MittelForschung GmbH und eine weitere Antragsgegnerin wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Urteile des Landesgerichts für Strafsachen Wien vom 26. März 2018 (ON 65 der Hv-Akten) und des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, des Vertreters des Antragstellers, Dr. Bauer, und des Vertreters der Antragsgegnerin Analyse Fenheim GmbH, Mag. Bauer, zu Recht erkannt:  Spruch

**False Positives:**

- `Antragsgegnerin MittelForschung GmbH` — partial — gold is substring of pred: `MittelForschung GmbH`
- `Antragsgegnerin Analyse Fenheim GmbH` — partial — gold is substring of pred: `Analyse Fenheim GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Dr. Setz-Hummel`(person)
- `Mag. Leitner`(person)
- `Georgia Bruckmeir`(person)
- `MittelForschung GmbH`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Holzleithner`(person)
- `Dr. Bauer`(person)
- `Analyse Fenheim GmbH`(organisation)
- `Mag. Bauer`(person)

**Example 2** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__4`)


In der Medienrechtssache des Antragstellers Univ.-Prof.in Laurin Schramm gegen die Antragsgegnerin CDL Luftfahrt GmbH wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, verletzen die Urteile 1./ dieses Gerichts vom 26. März 2018 (ON 65) in seinem Punkt III./, womit der Antrag des Antragstellers, der Antragsgegnerin Drau-IT GmbH auch für die am 4. Juni 2017 auf dem Facebook-Account von www.

**False Positives:**

- `Antragsgegnerin CDL Luftfahrt GmbH` — partial — gold is substring of pred: `CDL Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Laurin Schramm`(person)
- `CDL Luftfahrt GmbH`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Drau-IT GmbH`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__7`)


Text Gründe: I./ In der Medienrechtssache des Antragstellers StR Anna Barkhausen gegen die Antragsgegnerin Tramoncon KI Consulting GmbH (als Medieninhaberin der Websites www.

**False Positives:**

- `Antragsgegnerin Tramoncon KI Consulting GmbH` — partial — gold is substring of pred: `Tramoncon KI Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Anna Barkhausen`(person)
- `Tramoncon KI Consulting GmbH`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__10`)


für die dadurch zugefügte Kränkung wurde die Antragsgegnerin Tenholt Holz GmbH nach § 6 Abs 1 MedienG zur Zahlung einer Entschädigung sowie nach § 8a Abs 6 MedienG iVm § 34 Abs 1 MedienG zur Urteilsveröffentlichung verpflichtet.

**False Positives:**

- `Antragsgegnerin Tenholt Holz GmbH` — partial — gold is substring of pred: `Tenholt Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tenholt Holz GmbH`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__11`)


Hingegen wurde (ua) der Antrag des Antragstellers, der Antragsgegnerin TraunMarine GmbH für die am selben Tag auf dem Facebook-Account von www.

**False Positives:**

- `Antragsgegnerin TraunMarine GmbH` — partial — gold is substring of pred: `TraunMarine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunMarine GmbH`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__34`)


Die Haftung des auf eigene Inhalte Verlinkenden als Content-Provider richtet sich daher nach den allgemeinen (straf-)rechtlichen Normen und soweit dieser – wie vorliegend – Medieninhaber ist, nach dem Mediengesetz (Reindl-Krauskopf/Salimi/Stricker, IT-Strafrecht [2018] Rz 3.3, 3.10 und 3.33;Koziol, Haftpflichtrecht II³ A/6/Rz 204;Zankl, E-Commerce-Gesetz, Kommentar2Rz 277), sodass § 17 ECG der geltend gemachten Verantwortlichkeit der Antragsgegnerin Kirmayer Heizung GmbH nach § 6 Abs 1 MedienG nicht entgegensteht.

**False Positives:**

- `Antragsgegnerin Kirmayer Heizung GmbH` — partial — gold is substring of pred: `Kirmayer Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kirmayer Heizung GmbH`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__40`)


Voraussetzung für die geltend gemachte Haftung der Antragsgegnerin TUEU Garten GmbH nach § 6 Abs 1 MedienG ist, dass im Medium „Website“ (§ 1 Abs 1 Z 5a lit b MedienG) der objektive Tatbestand der üblen Nachrede hergestellt wurde.

**False Positives:**

- `Antragsgegnerin TUEU Garten GmbH` — partial — gold is substring of pred: `TUEU Garten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TUEU Garten GmbH`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__60`)


Da sich diese Gesetzesverletzung nicht zum Nachteil der Antragsgegnerin Heimnexfen Planung Entwicklung GmbH, der als Medieninhaberin die Rechte des Angeklagten zukommen (§ 41 Abs 6 zweiter Satz MedienG), auswirkt, kommt ein Vorgehen nach § 292 letzter Satz StPO nicht in Betracht und hat es mit der Feststellung des Gesetzesverstoßes sein Bewenden.

**False Positives:**

- `Antragsgegnerin Heimnexfen Planung Entwicklung GmbH` — partial — gold is substring of pred: `Heimnexfen Planung Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heimnexfen Planung Entwicklung GmbH`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_4`)


In der Medienrechtssache der Antragsteller Dr. Patrick Schneeweiss und Chen Hölzle gegen die Antragsgegnerin TQGK Versicherung Holding GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p, verletzt der Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), § 395 Abs 2 StPO (iVm § 41 Abs 1 MedienG).

**False Positives:**

- `Antragsgegnerin TQGK Versicherung Holding GmbH` — positional overlap with gold: `TQGK Versicherung Holding GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Patrick Schneeweiss`(person)
- `Chen Hölzle`(person)
- `TQGK Versicherung Holding GmbH & Co KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `Antragsgegnerin Wald Fenkraftal GmbH` — positional overlap with gold: `Wald Fenkraftal GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wieland Skocdopole`(person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc`(person)
- `Wald Fenkraftal GmbH & Co KG`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/3Nc11_13t`) (sent_id: `deanon_260716_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Mikulska Textil GmbH, Kohleck 4, 6794 Partenen, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin TraunWind GmbH, Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Antragstellerin Mikulska Textil GmbH` — partial — gold is substring of pred: `Mikulska Textil GmbH`
- `Antragsgegnerin TraunWind GmbH` — partial — gold is substring of pred: `TraunWind GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Dr. Neumayr`(person)
- `Dr. Jensik`(person)
- `Mikulska Textil GmbH`(organisation)
- `Kohleck 4, 6794 Partenen, Österreich`(address)
- `Dr. Clemens Thiele`(person)
- `TraunWind GmbH`(organisation)
- `Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich`(address)
- `Bezirksgericht Salzburg`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/5Ob146_16f`) (sent_id: `deanon_260716_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Pamela Keilonat, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Hoch Dorfder GmbH & Co KG, Lichtensternweg 19, 4714 Meggenhofen, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt. Begründung:  Rechtliche Beurteilung Der Antragsteller begehrt Rechnungslegung nach § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002.

**False Positives:**

- `Antragsgegnerin Hoch Dorfder GmbH` — positional overlap with gold: `Hoch Dorfder GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Höllwerth`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Mag. Pamela Keilonat`(person)
- `Dr. Anke Reisch`(person)
- `Hoch Dorfder GmbH & Co KG`(organisation)
- `Lichtensternweg 19, 4714 Meggenhofen, Österreich`(address)
- `Dr. Lisbeth Lass`(person)
- `Dr. Hans Christian Lass`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Kitzbühel`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/5Ob174_15x`) (sent_id: `deanon_260716_TRAIN/5Ob174_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der außerstreitigen Wohnrechtssache der Antragstellerin Ulrike Richardson, vertreten durch Mag. Valerie Gröschl, Mietervereinigung Österreichs, 1010 Wien, Reichsratsstraße 15, gegen die Antragsgegnerin Traun Nortriost Holding GmbH, Prof.-Ernst-Schandl-Park 18J, 4343 Inzing, Österreich, vertreten durch Mag. Günter Petzelbauer, Rechtsanwalt in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den außerordentlichen Revisionsrekurs der Antragsgegnerin gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. Mai 2015, GZ 39 R 136/15m-17, mit dem der Sachbeschluss des Bezirksgerichts Hernals vom 30. Dezember 2014, GZ 5 Msch 15/14g-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Antragsgegnerin Traun Nortriost Holding GmbH` — partial — gold is substring of pred: `Traun Nortriost Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Höllwerth`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Ulrike Richardson`(person)
- `Mag. Valerie Gröschl`(person)
- `Traun Nortriost Holding GmbH`(organisation)
- `Prof.-Ernst-Schandl-Park 18J, 4343 Inzing, Österreich`(address)
- `Mag. Günter Petzelbauer`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Hernals`(organisation)

</details>

---

## `Landesgericht with Location` 🏆

**F1:** 0.011 | **Precision:** 0.451 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `29a7c692`  
**Description:**
Matches 'Landesgericht' followed by a location name, strictly excluding single-letter placeholders, 'zu GZ' prefixes, and prepositions. Requires a valid city name pattern (2+ letters) and stops before specific delimiters to prevent over-capture of 'Landesgericht Leoben' when 'Leoben' is part of a different phrase.

**Content:**
```
(?<!\w)(Landesgericht\s+([A-Z][a-zA-Z]{2,}(?:\s+[A-Z][a-zA-Z]{2,})*))(?!\s+(?:zu|zur|zum|als|bei|in|an|auf|mit|von|f\u00fcr|nach|vor|\u00fcber|unter|ohne|gegen|durch|seit|neben|zwischen|hinter|Konkursgericht|erfolgte|wurde|ist|hat|hatte|sind|waren|konnte|kann|GZ|G\.Z\.|eine|gegen|eingereicht|Beschwerde|ein|entrichtet|diesem|zu\s+GZ|zu\s+G\.Z\.|zu\s+Akten|zu\s+Verfahren|zu\s+G\.Z\.\s+vom|vom|am|im|bei|f\u00fcr|nach|vor|\u00fcber|unter|ohne|gegen|durch|seit|neben|zwischen|hinter|zur\s+FN|zu\s+FN|\d{1,2}\.\s+(?:Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|Jan|Feb|M\u00e4r|Apr|Jun|Jul|Aug|Sep|Okt|Nov|Dez|Sept|Okt|Nov|Dez)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.451 | 0.006 | 0.011 | 51 | 23 | 28 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 28 | 3972 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_12`)


[3] Bereits in der Klage beantragt dieKlägerindie Delegierung der Rechtssache an das Landesgericht Korneuburg.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 4** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_5`)


Der zuletzt bezeichnete Beschluss wird aufgehoben und die Sache zu neuer Entscheidung über den Antrag der Staatsanwaltschaft vom 12. März 2014 auf Wiederaufnahme des Strafverfahrens (ON 29) an das Landesgericht Feldkirch verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_9`)


Nachdem die Angeklagte Sabrina Heckel in der Hauptverhandlung am 24. Juli 2013 angegeben hatte, als Zeugin nicht vor der Polizei, sondern in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Butze falsch ausgesagt zu haben, gab die Staatsanwaltschaft noch in dieser Hauptverhandlung eine Alternativanklage zu Protokoll, der zufolge sie als Zeugin in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Bulthaup vor dem Landesgericht Feldkirch die Vergehen der falschen Beweisaussage nach § 288 Abs 1 StGB (III./) und der Begünstigung nach § 299 Abs 1 StGB (IV./) begangen habe (ON 10 S 3 f des Aktes AZ 51 Hv 46/13y des Landesgerichts Feldkirch).

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Missed by this rule (FN):**

- `Sabrina Heckel` (person)
- `Johannes Butze` (person)
- `Johannes Bulthaup` (person)
- `Landesgerichts Feldkirch` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_18`)


Am 1. Oktober 2014 verfügte das Landesgericht Feldkirch die Zustellung der „ON 35“ (gemeint sichtlich: des Beschlusses auf Wiederaufnahme des Strafverfahrens ON 35 im Akt AZ 51 Hv 32/13i und ON 47 im Akt AZ 39 Hv 64/14h jeweils des Landesgerichts Feldkirch) an „die Erziehungsberechtigte des Johannes Bauckloh “, worauf der seinerzeitigen gesetzlichen Vertreterin (der Mutter) des nunmehr volljährigen Angeklagten der Beschluss am 3. Oktober 2014 eigenhändig zugestellt wurde (ON 42 S 3).

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Missed by this rule (FN):**

- `Landesgerichts Feldkirch` (organisation)
- `Johannes Bauckloh` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__5`)


Das Urteil des Landesgerichts Eisenstadt vom 6. Juni 2017 (ON 155) wird aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Eisenstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Eisenstadt` | `Landesgericht Eisenstadt` |

**Missed by this rule (FN):**

- `Landesgerichts Eisenstadt` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__5`)


Das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das im Übrigen unberührt bleibt, wird im Nikola Meine betreffenden Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Landesgerichts Salzburg` (organisation)
- `Nikola Meine` (person)

**Example 10** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_24`)


Wenngleich eine Vorverlegung des Zeitpunktes der bedingten Entlassung nicht mehr in Betracht kommt, wäre der Beschluss über die bedingte Entlassung zur Vermeidung nachteiliger Auswirkungen aufzuheben (§ 292 letzter Satz StPO) und - zufolge rechtslogischer Beseitigung der zwischenzeitigen Verfahrensabtretung nach '§ 179 StVG' (vgl RIS-Justiz RS0100444) - dem Landesgericht Wiener Neustadt die Entscheidung über den Antrag der Radmila Mölder auf bedingte Entlassung aufzutragen.“

| Predicted | Gold |
|---|---|
| `Landesgericht Wiener Neustadt` | `Landesgericht Wiener Neustadt` |

**Missed by this rule (FN):**

- `Radmila Mölder` (person)

**Example 11** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in Punkt A./2./ des Schuldspruchs sowie im Strafausspruch aufgehoben und es wird die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 12** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Freispruch unberührt bleibt, im Schuldspruch, demgemäß auch im Straf- und im Kostenausspruch, aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache im Umfang der Aufhebung an das Landesgericht Feldkirch verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 13** (doc_id: `deanon_260716_TRAIN/1Nc10_18p`) (sent_id: `deanon_260716_TRAIN/1Nc10_18p_4`)


Text Begründung: Das Landesgericht Klagenfurt entzog mit Beschluss vom 28.

| Predicted | Gold |
|---|---|
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Example 14** (doc_id: `deanon_260716_TRAIN/1Nc1_15k`) (sent_id: `deanon_260716_TRAIN/1Nc1_15k_7`)


Die Klägerin begehrte die Delegierung des Verfahrens gemäß § 31 JN an das Landesgericht Feldkirch.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 15** (doc_id: `deanon_260716_TRAIN/1Nc1_15k`) (sent_id: `deanon_260716_TRAIN/1Nc1_15k_23`)


Im vorliegenden Fall haben sowohl die Klägerin als auch das vorlegende Gericht zutreffend auf jene Umstände hingewiesen, die insgesamt eine Delegierung an das Landesgericht Feldkirch zweckmäßig erscheinen lassen (vgl dazu RIS-Justiz RS0046540), kann doch vor diesem Gericht unter Wahrung des Unmittelbarkeitsgrundsatzes das gesamte Beweisverfahren in einem Zug durchgeführt werden, was typischerweise nicht nur zu einer Erleichterung der Gerichtstätigkeit, sondern auch zu einer Verbilligung und Verkürzung des Verfahrens führt.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 16** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_6`)


Nach Zurück- bzw Abweisung seiner Begehren in erster Instanz lehnte er wiederholt Richter des Landesgerichts Leoben und des Oberlandesgerichts Graz erfolglos ab (vgl Landesgericht Leoben 2 Nc 24/11d, 2 Nc 25/11a, 2 Nc 28/11t;

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Missed by this rule (FN):**

- `Landesgerichts Leoben` (organisation)
- `Oberlandesgerichts Graz` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_11`)


Diese Ablehnung wies der Ablehnungssenat beim Landesgericht Leoben (ohne Beteiligung des abgelehnten Richters) mit Beschluss vom 4. Dezember 2013, 2 Nc 31/13m, zurück.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 18** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Kelkel-Versicherung GmbH, Walkersdorf 16, 9761 Tröbelsberg, Österreich, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Zorzorzor GmbH, Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Wien` | `Landesgericht Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Landesgericht Innsbruck` (organisation)
- `Kelkel-Versicherung GmbH` (organisation)
- `Walkersdorf 16, 9761 Tröbelsberg, Österreich` (address)
- `Mag. Heinz Heher` (person)
- `Zorzorzor GmbH` (organisation)
- `Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich` (address)
- `Dr. Adrian Hollaender` (person)
- `Handelsgericht Wien` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_11`)


Nach Einbringen der Klagebeantwortung beantragte sie die Delegierung an das „Landesgericht Wien“.

| Predicted | Gold |
|---|---|
| `Landesgericht Wien` | `Landesgericht Wien` |

**Example 20** (doc_id: `deanon_260716_TRAIN/6Ob240_20t`) (sent_id: `deanon_260716_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN103376a beim Landesgericht Landesgericht Krems an der Donau eingetragenen Taltalgart-Gastronomie GmbH mit Sitz in der politischen Gemeinde Landesgericht Salzburg, über den Revisionsrekurs der Telekom Mongart gesellschaft mbH, Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `FN103376a` (business_register_number)
- `Landesgericht Krems an der Donau` (organisation)
- `Taltalgart-Gastronomie GmbH` (organisation)
- `Telekom Mongart gesellschaft mbH` (organisation)
- `Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich` (address)
- `Dr. Robert Mogy` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_17`)


[4] In dem von der Werkunternehmerin gegen die Subunternehmerin vor dem Landesgericht Steyr geführten Verfahren (AZ 3 Cg 59/19z) wurde mit Beschluss vom 1. 3. 2016 DI Corvin Ißner (in Hinkunft: gerichtlicher Sachverständiger) zum Sachverständigen bestellt. Er wurde insbesondere mit der Beantwortung der Fragen beauftragt, ob eine Verflüssigung des Randverbundes der Isolierglasscheiben vorliege, worauf diese Veränderung zurückzuführen sei, ob dies auf die von der beklagten Subunternehmerin gelieferten Isolierglasscheiben oder auf die von der klagenden Werkunternehmerin durchgeführten Einbaumaßnahmen zurückzuführen sei, welche Beeinträchtigungen damit verbunden seien, ob eine Verbesserung möglich sei und welche Kosten damit verbunden seien.

| Predicted | Gold |
|---|---|
| `Landesgericht Steyr` | `Landesgericht Steyr` |

**Missed by this rule (FN):**

- `DI Corvin Ißner` (person)

**Example 22** (doc_id: `deanon_260716_TRAIN/8ObS8_22t`) (sent_id: `deanon_260716_TRAIN/8ObS8_22t_7`)


Das Landesgericht Innsbruck eröffnete mit Beschluss vom 24.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht Lin` — partial — pred is substring of gold: `Landesgericht Linz`
- `Landesgericht Korneubur` — partial — pred is substring of gold: `Landesgericht Korneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Landesgericht Linz`(organisation)
- `Hollengk Planung GmbH`(organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich`(address)
- `Huber Berchtold Rechtsanwälte OG`(organisation)
- `Wind Nexheimval GmbH`(organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich`(address)
- `ScherbaumSeebacher Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Linz`(organisation)
- `Landesgericht Korneuburg`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_6`)


Die in Wien ansässige klagende Gesellschaft nimmt die in Linz ansässige beklagte Gesellschaft beim Landesgericht Linz auf restliche Honorare für Planungsleistungen für ein Bauvorhaben in Klosterneuburg bei Wien in Anspruch.

**False Positives:**

- `Landesgericht Lin` — partial — pred is substring of gold: `Landesgericht Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Linz`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_29`)


Die Rechtssache weist keinen eindeutigen Schwerpunkt zum Landesgericht Korneuburg auf.

**False Positives:**

- `Landesgericht Korneubur` — partial — pred is substring of gold: `Landesgericht Korneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_32`)


Damit kann nicht gesagt werden, dass die Gründe für eine Übertragung der Rechtssache vom Landesgericht Linz an das Landesgericht Korneuburg überwiegen.

**False Positives:**

- `Landesgericht Lin` — partial — pred is substring of gold: `Landesgericht Linz`
- `Landesgericht Korneubur` — partial — pred is substring of gold: `Landesgericht Korneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Linz`(organisation)
- `Landesgericht Korneuburg`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Landesgericht Lin` — partial — pred is substring of gold: `Landesgericht Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Landesgericht Linz`(organisation)
- `Steidlen+Ysner Daten GmbH`(organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich`(address)
- `Dr. Roland Kassowitz`(person)
- `Verlag Waldlemder GmbH`(organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich`(address)
- `Prof. Haslinger`(person)
- `Landesgerichts Linz`(organisation)
- `Handelsgericht Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_19`)


Am 17. Oktober 2014 langte beim Landesgericht Feldkirch zu AZ 51 Hv 32/13i eine vom Verfahrenshilfeverteidiger im Verfahren AZ 39 Hv 64/14h dieses Landesgerichts verfasste Beschwerde des Angeklagten Johannes Bartlmäß (ON 42 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch) gegen den Beschluss des Landesgerichts Feldkirch vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens ein.

**False Positives:**

- `Landesgericht Feldkirc` — partial — pred is substring of gold: `Landesgericht Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Feldkirch`(organisation)
- `Johannes Bartlmäß`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Landesgerichts Feldkirch`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_10`)


Das Landesgericht Innsbruck als Berufungsgericht gab dieser Berufung der Staatsanwaltschaft wegen des Ausspruchs über die Strafe schließlich mit Urteil vom 9. März 2010, AZ 21 B1 478/09s (= ON 26 im Erkenntnisakt) Folge und erhöhte die Freiheitsstrafe auf drei Monate.

**False Positives:**

- `Landesgericht Innsbruc` — partial — pred is substring of gold: `Landesgericht Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Innsbruck`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/18OCg2_24d`) (sent_id: `deanon_260716_TRAIN/18OCg2_24d_5`)


Text Begründung: [1] DerKlägerbegehrt mit seiner beim Landesgericht Klagenfurt als Arbeits- und Sozialgericht eingebrachten Klage, das Erkenntnis des Schiedsgerichts der beklagten Glaubensgemeinschaft vom 18.

**False Positives:**

- `Landesgericht Klagenfur` — partial — pred is substring of gold: `Landesgericht Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Klagenfurt`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/18OCg2_24d`) (sent_id: `deanon_260716_TRAIN/18OCg2_24d_17`)


[5] DerKlägerbeantragte für den Fall, dass sich das angerufene Landesgericht Klagenfurt für unzuständig erklären sollte, die Überweisung an den nicht offenbar unzuständigen Obersten Gerichtshof.

**False Positives:**

- `Landesgericht Klagenfur` — partial — pred is substring of gold: `Landesgericht Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Klagenfurt`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/1Nc1_15k`) (sent_id: `deanon_260716_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Große-Schulte & Seufer E‑Commerce GmbH, Untererb 31, 3033 Altlengbach, Österreich, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Wilbachkel Luftfahrt GmbH, Andrä Idl-Straße 79, 4791 Haselbach, Österreich, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Landesgericht Wiener Neustad` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`
- `Landesgericht Feldkirc` — partial — pred is substring of gold: `Landesgericht Feldkirch`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Landesgericht Wiener Neustadt`(organisation)
- `Große-Schulte & Seufer E‑Commerce GmbH`(organisation)
- `Untererb 31, 3033 Altlengbach, Österreich`(address)
- `Dr. Andreas Oberbichler`(person)
- `Dr. Michael Kramer`(person)
- `Wilbachkel Luftfahrt GmbH`(organisation)
- `Andrä Idl-Straße 79, 4791 Haselbach, Österreich`(address)
- `Mag. Maximilian Kocher`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_5`)


2. Zur Entscheidung und Verhandlung in dieser Rechtssache wird das Landesgericht Linz als zuständig bestimmt.

**False Positives:**

- `Landesgericht Lin` — partial — pred is substring of gold: `Landesgericht Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Linz`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben Amtshaftungsanspr` — partial — gold is substring of pred: `Landesgericht Leoben`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Leoben`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_9`)


Am 26. Februar 2013 lehnte er den Vorsitzenden des Ablehnungssenats beim Landesgericht Leoben als befangen und nach Zurückweisung dieses Antrags (2 Nc 3/13v) die Entscheidungsträger dieses Beschlusses als befangen ab.

**False Positives:**

- `Landesgericht Leobe` — partial — pred is substring of gold: `Landesgericht Leoben`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Leoben`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_260716_TRAIN/1Ob66_13g_1Ob67_13d__5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben Amtshaftungsanspr` — partial — gold is substring of pred: `Landesgericht Leoben`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Leoben`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Xaver Springinsgut, Rechtsanwalt in St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jähnel in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Alpen Nexlex AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Schulgartenweg 18, 9872 Grantsch, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Jiran, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Landesgericht Lin` — partial — pred is substring of gold: `Landesgericht Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Xaver Springinsgut`(person)
- `St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich`(address)
- `Elfriede Jähnel`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `Bezirksgerichts Amstetten`(organisation)
- `Landesgericht Linz`(organisation)
- `Bezirksgericht Amstetten`(organisation)
- `Alpen Nexlex AG`(organisation)
- `Schulgartenweg 18, 9872 Grantsch, Österreich`(address)
- `Roman Jiran`(person)

**Example 15** (doc_id: `deanon_260716_TRAIN/2Nc25_11s`) (sent_id: `deanon_260716_TRAIN/2Nc25_11s_7`)


Der Kläger brachte beim Landesgericht Innsbruck eine Klage ein, mit der er aus diesem Unfall (nach Ausdehnung) die Bezahlung von 21.664,61 EUR sA verlangt;

**False Positives:**

- `Landesgericht Innsbruc` — partial — pred is substring of gold: `Landesgericht Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Innsbruck`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/3Ob32_17b`) (sent_id: `deanon_260716_TRAIN/3Ob32_17b_6`)


Text Begründung: Am 4. Oktober 2010 erließ das Landesgericht Mailand (Tribunale Ordinario di Milano) über Antrag der Betreibenden, einer Gesellschaft mit Sitz in Italien, den elektronischen Mahnbescheid (decreto ingiunitivo telematico) zur Zahl 34300/2010, mit dem der Verpflichteten, einer GmbH mit Sitz in Wien, die in Geschäftsverbindung mit der Betreibenden stand, die Zahlung von 522.094,53 EUR sA an die Betreibende innerhalb von 50 Tagen nach Bekanntmachung des Mahnbescheids aufgetragen wurde.

**False Positives:**

- `Landesgericht Mailand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/3Ob32_17b`) (sent_id: `deanon_260716_TRAIN/3Ob32_17b_7`)


Dieser enthielt den Hinweis, dass die Verpflichtete Anspruch darauf habe, vor dem Landesgericht Mailand innerhalb von 50 Tagen nach der Bekanntmachung Einspruch zu erheben, widrigenfalls der Mahnbescheid für endgültig und vollstreckbar erklärt werde.

**False Positives:**

- `Landesgericht Mailan` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Kelkel-Versicherung GmbH, Walkersdorf 16, 9761 Tröbelsberg, Österreich, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Zorzorzor GmbH, Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Landesgericht Innsbruc` — partial — pred is substring of gold: `Landesgericht Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Landesgericht Innsbruck`(organisation)
- `Kelkel-Versicherung GmbH`(organisation)
- `Walkersdorf 16, 9761 Tröbelsberg, Österreich`(address)
- `Mag. Heinz Heher`(person)
- `Zorzorzor GmbH`(organisation)
- `Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich`(address)
- `Dr. Adrian Hollaender`(person)
- `Landesgericht Wien`(organisation)
- `Handelsgericht Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_6`)


Die Klägerin brachte beim Landesgericht Innsbruck eine Unterlassungs- und Zahlungsklage ein.

**False Positives:**

- `Landesgericht Innsbruc` — partial — pred is substring of gold: `Landesgericht Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Innsbruck`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/4Ob68_14z`) (sent_id: `deanon_260716_TRAIN/4Ob68_14z_21`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `Landesgericht Innsbruc` — partial — pred is substring of gold: `Landesgericht Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Innsbruck`(organisation)
- `Oberlandesgericht Innsbruck`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/6Ob240_20t`) (sent_id: `deanon_260716_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN103376a beim Landesgericht Landesgericht Krems an der Donau eingetragenen Taltalgart-Gastronomie GmbH mit Sitz in der politischen Gemeinde Landesgericht Salzburg, über den Revisionsrekurs der Telekom Mongart gesellschaft mbH, Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Landesgericht Landesgericht Krem` — positional overlap with gold: `Landesgericht Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `FN103376a`(business_register_number)
- `Landesgericht Krems an der Donau`(organisation)
- `Taltalgart-Gastronomie GmbH`(organisation)
- `Landesgericht Salzburg`(organisation)
- `Telekom Mongart gesellschaft mbH`(organisation)
- `Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich`(address)
- `Dr. Robert Mogy`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_28`)


Die Klägerin brachte daraufhin Mahnklage gegen den gerichtlichen Sachverständigen vor dem Landesgericht Wels zu AZ 5 Cg 113/19w ein.

**False Positives:**

- `Landesgericht Wel` — partial — pred is substring of gold: `Landesgericht Wels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wels`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/9Nc4_10b`) (sent_id: `deanon_260716_TRAIN/9Nc4_10b_6`)


Sie hat nach § 31 JN die Delegation an das Landesgericht Eisenstadt als Arbeits- und Sozialgericht beantragt.

**False Positives:**

- `Landesgericht Eisenstad` — partial — pred is substring of gold: `Landesgericht Eisenstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Eisenstadt`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/9Nc4_10b`) (sent_id: `deanon_260716_TRAIN/9Nc4_10b_14`)


Da sowohl das Arbeits- und Sozialgericht Wien als auch das Landesgericht Eisenstadt im Sprengel des Oberlandesgerichts Wien liegen, ist der Oberste Gerichtshof zur Entscheidung über den Delegierungsantrag nicht zuständig.

**False Positives:**

- `Landesgericht Eisenstad` — partial — pred is substring of gold: `Landesgericht Eisenstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Eisenstadt`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Oberste Gerichtshof`(organisation)

</details>

---

## `KG Entities` 🏆

**F1:** 0.006 | **Precision:** 0.324 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `c45a37db`  
**Description:**
Matches company names ending in 'KG' or 'GmbH & Co KG'. STRICTLY requires a capitalized name prefix (letters, ampersands, hyphens, spaces) immediately before 'KG'. Excludes trailing non-name characters like 'xxxxx' or 'bzw.' and ensures the prefix is not a person's name followed by 'Rechtsanwälte'.

**Content:**
```
(?<!\w)((?:[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*(?:\s+&\s+[A-Z][a-zA-Z]+)*(?:\s+Medien)?(?:\s+Dr\.?\s+[A-Z][a-zA-Z]+)?(?:\s+Mag\.?\s+[A-Z][a-zA-Z]+)?(?:\s+und\s+[A-Z][a-zA-Z]+)*(?:\s+Steuerberatungs-?|\s+Rechtsanwalts-?|\s+Wirtschaftspr\u00fcfungs-?|\s+Steuerberatungsgesellschaft-?|\s+Steuerberatung-?|\s+Rechtsanw\u00e4lte-?|\s+OG-?|\s+GmbH-?|\s+AG-?|\s+KG-?|\s+mbH-?|\s+GesbR-?|\s+Partnerschaft-?|\s+Gesellschaft-?|\s+Unternehmensberatungs-?|\s+Transport-?|\s+Handel-?|\s+IT-?|\s+Software-?|\s+Technik-?|\s+Energie-?|\s+Versand-?|\s+Planung-?|\s+Consulting-?|\s+Team-?|\s+Service-?|\s+Zahlungs-?|\s+Logistik-?|\s+Immobilien-?|\s+Bau-?|\s+Medizin-?|\s*\d+)?(?:\s+&\s+Co)?))(?:\s+GmbH\s+&\s+Co\s+KG|\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.324 | 0.003 | 0.006 | 37 | 12 | 25 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 25 | 3710 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_4`)


Norsee Technologien GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Norsee Technologien GmbH & Co KG` | `Norsee Technologien GmbH & Co KG` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Pieler & Pieler & Partner KG` | `Pieler & Pieler & Partner KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Brigitte Martz` (person)
- `16. November 1978` (date)
- `Dr. Gustav Thöning` (person)
- `Dr. Madeleine Musialik` (person)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

| Predicted | Gold |
|---|---|
| `TraunTouristik Werke GesmbH & Co KG` | `TraunTouristik Werke GesmbH & Co KG` |

**Missed by this rule (FN):**

- `Bernhard Berti` (person)
- `Norbert Wierich` (person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich` (address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG` (organisation)
- `Susanne Schwarzhuber` (person)
- `Donau-Transport GmbH` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Steen vertretenen Prentl Handel GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

| Predicted | Gold |
|---|---|
| `Prentl Handel GesmbH & Co KG` | `Prentl Handel GesmbH & Co KG` |

**Missed by this rule (FN):**

- `Susanna Steen` (person)

**Example 4** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Weber Rechtsanwälte GmbH & Co KG` | `Weber Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `MMag. Sloboda` (person)
- `Dr. Kikinger` (person)
- `Mag. Fitz` (person)
- `Denise Markstaler` (person)
- `Rut Adamheit` (person)
- `BEURLE Rechtsanwälte GmbH & Co KG` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bichler Zrzavy Rechtsanwälte GmbH & Co KG` | `Bichler Zrzavy Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `APHU Solar GmbH & Co KG` (organisation)
- `Hochkreuth 39, 8144 Bischofegg, Österreich` (address)
- `DDr. Heinz Dietmar Schimanko` (person)
- `Traun-Transport GmbH` (organisation)
- `Stauderstraße 30, 8200 Pircha, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Nimtz Pharma GmbH, Mildenbergstraße 11, 3072 Furth, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1) Unikel Landwirtschaft GmbH & Co KG und 2) Gode+Panköker Getränke GmbH, Martinsplatz 1-31, 9831 Kleindorf, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Provisorialverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 6. August 2010, GZ 5 R 150/10f-7, womit der Beschluss des Handelsgerichts Wien vom 24. Juni 2010, GZ 11 Cg 117/10h-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Unikel Landwirtschaft GmbH & Co KG` | `Unikel Landwirtschaft GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `Nimtz Pharma GmbH` (organisation)
- `Mildenbergstraße 11, 3072 Furth, Österreich` (address)
- `Berger Saurer Zöchbauer, Rechtsanwälte` (organisation)
- `Gode+Panköker Getränke GmbH` (organisation)
- `Martinsplatz 1-31, 9831 Kleindorf, Österreich` (address)
- `Gheneff - Rami - Sommer Rechtsanwälte KG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_4`)


Monderdorf Cloud GmbH, R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ruggenthaler Rechtsanwalts KG` | `Ruggenthaler Rechtsanwalts KG` |

**Missed by this rule (FN):**

- `Monderdorf Cloud GmbH` (organisation)
- `R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/5Ob259_15x`) (sent_id: `deanon_260716_TRAIN/5Ob259_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Shoshana Dimpfel, vertreten durch Hofbauer & Wagner Rechtsanwälte KG in St. Pölten, gegen den Antragsgegner Adolf Beehr, vertreten durch Dr. Franz Gütlbauer, Dr. Siegfried Sieghartsleitner, Dr. Michael Pichlmair, Rechtsanwälte in Wels, wegen § 8 Abs 2 MRG (hier: wegen Abänderung des Sachbeschlusses des Bezirksgerichts Traun vom 18. März 2014, GZ 17 Msch 6/13m-8) über den „Rekurs“ des Antragsgegners gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 8. Oktober 2015, GZ 14 R 56/15a-22, mit dem der Beschluss des Bezirksgerichts Traun vom 25. Februar 2015, GZ 17 Msch 6/13m-18, bestätigt wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hofbauer & Wagner Rechtsanwälte KG` | `Hofbauer & Wagner Rechtsanwälte KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Höllwerth` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Shoshana Dimpfel` (person)
- `Adolf Beehr` (person)
- `Dr. Franz Gütlbauer` (person)
- `Dr. Siegfried Sieghartsleitner` (person)
- `Dr. Michael Pichlmair` (person)
- `Bezirksgerichts Traun` (organisation)
- `Landesgerichts Linz` (organisation)
- `Bezirksgerichts Traun` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Josefine Fretschner, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei AlpenDerlogverEvent GmbH, Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

| Predicted | Gold |
|---|---|
| `Wolf Theiss Rechtsanwälte GmbH & Co KG` | `Wolf Theiss Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `Dr. Pfurtscheller` (person)
- `Josefine Fretschner` (person)
- `Poduschka Anwaltsgesellschaft mbH` (organisation)
- `AlpenDerlogverEvent GmbH` (organisation)
- `Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich` (address)
- `Landesgerichts Steyr` (organisation)
- `Bezirksgerichts Steyr` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/6Ob105_20i`) (sent_id: `deanon_260716_TRAIN/6Ob105_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Jaden Ince, vertreten durch Mag. Erwin Falkner, Rechtsanwalt in Wien, gegen die beklagte Partei R. Enns Verfurt GmbH, Greifenberg 38, 4972 Windhag, Österreich, vertreten durch Hoffmann & Sykora Rechtsanwälte KG in Tulln, wegen 6.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 13. November 2019, GZ 21 R 208/19z-53, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Tulln vom 23. Juni 2019, GZ 11 C 276/18p-49, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hoffmann & Sykora Rechtsanwälte KG` | `Hoffmann & Sykora Rechtsanwälte KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `Jaden Ince` (person)
- `Mag. Erwin Falkner` (person)
- `Enns Verfurt GmbH` (organisation)
- `Greifenberg 38, 4972 Windhag, Österreich` (address)
- `Landesgerichts St. Pölten` (organisation)
- `Bezirksgerichts Tulln` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/6Ob146_18s`) (sent_id: `deanon_260716_TRAIN/6Ob146_18s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei RgR Dr.in Manuela Künemund, vertreten durch Mag. Max Verdino und andere Rechtsanwälte in St. Veit an der Glan, gegen die beklagte Partei Kleuß Maschinenbau GmbH, Friedensring 38, 9815 Penk, Österreich, vertreten durch PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG in Wien, wegen 18.664,48 EUR und Feststellung, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 6. Juni 2018, GZ 4 R 51/18d-12, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2018, GZ 28 Cg 75/17s-8, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG` | `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `RgR Dr.in Manuela Künemund` (person)
- `Mag. Max Verdino` (person)
- `Kleuß Maschinenbau GmbH` (organisation)
- `Friedensring 38, 9815 Penk, Österreich` (address)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der GBJU Getränke GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `GBJU Getränke GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GBJU Getränke GmbH & Co KG`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Mesarec Medien GesmbH & Co KG` — partial — pred is substring of gold: `Hauenschildt&Mesarec Medien GesmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Berti`(person)
- `Norbert Wierich`(person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich`(address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG`(organisation)
- `Susanne Schwarzhuber`(person)
- `Donau-Transport GmbH`(organisation)
- `TraunTouristik Werke GesmbH & Co KG`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

**False Positives:**

- `Medien GmbH & Co KG` — partial — pred is substring of gold: `Synzortal-Medien GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Dr. Mann`(person)
- `Dr. Koller`(person)
- `Dr. Ludger Schäpan`(person)
- `Moses Rüßbült`(person)
- `Synzortal-Medien GmbH & Co KG`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Wachberger`(person)
- `Dr. Windhager`(person)
- `Mag. Hermetter`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Harald Adolphsen KG, FN FN214876m, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Alpen Donalcon “ OXS Bildung gmbH, FN FN067476g, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Harald Adolphsen KG` — partial — gold is substring of pred: `Harald Adolphsen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Musger`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Dr. Parzmayr`(person)
- `Harald Adolphsen`(person)
- `FN214876m`(business_register_number)
- `Dr. Eva-Maria Bachmann`(person)
- `Dr. Christian Bachmann`(person)
- `Alpen Donalcon`(organisation)
- `OXS Bildung gmbH`(organisation)
- `FN067476g`(business_register_number)
- `GRAF ISOLA Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob29_20a`) (sent_id: `deanon_260716_TRAIN/1Ob29_20a_19`)


Der Mann hat sich an einem Immobilienprojekt, das von einer GmbH & Co KG verwirklicht wird, beteiligt.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Haßtenteufel Umwelt GmbH & Co KG, Peter Zauner Weg 324, 5273 Wesen, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Klagenfurt, gegen die beklagte Partei Isaak Tomzak, vertreten durch Dr. Maximilian Motschiunig, Rechtsanwalt in Klagenfurt, wegen Vertragsaufhebung und Abgabe einer Willenserklärung (Streitwert 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 1. Oktober 2019, GZ 2 R 141/19a, 2 R 142/19y-95, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Umwelt GmbH & Co KG` — partial — pred is substring of gold: `Haßtenteufel Umwelt GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. Solé`(person)
- `Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Haßtenteufel Umwelt GmbH & Co KG`(organisation)
- `Peter Zauner Weg 324, 5273 Wesen, Österreich`(address)
- `Gheneff - Rami - Sommer Rechtsanwälte OG`(organisation)
- `Isaak Tomzak`(person)
- `Dr. Maximilian Motschiunig`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_4`)


Silvana Roellgen, MBA KG und 2. Dr. Nancy Achatzy, vertreten durch die erstklagende Partei, wider die beklagte Partei Dr. Theodora Jungverdorben, vertreten durch BMA Brandstätter Rechtsanwälte GmbH in Wien, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. April 2014, GZ 46 R 135/13p-43, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Jänner 2013, GZ 75 C 17/11x-37, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `MBA KG` — positional overlap with gold: `Silvana Roellgen, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Silvana Roellgen, MBA`(person)
- `Dr. Nancy Achatzy`(person)
- `Dr. Theodora Jungverdorben`(person)
- `BMA Brandstätter Rechtsanwälte GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_5`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Druck Steinnex GmbH, Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Maur & Partner Rechtsanwälte GmbH & Co KG` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Druck Steinnex GmbH`(organisation)
- `Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich`(address)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei APHU Solar GmbH & Co KG` — partial — gold is substring of pred: `APHU Solar GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `APHU Solar GmbH & Co KG`(organisation)
- `Hochkreuth 39, 8144 Bischofegg, Österreich`(address)
- `DDr. Heinz Dietmar Schimanko`(person)
- `Traun-Transport GmbH`(organisation)
- `Stauderstraße 30, 8200 Pircha, Österreich`(address)
- `Bichler Zrzavy Rechtsanwälte GmbH & Co KG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/3Ob223_19v`) (sent_id: `deanon_260716_TRAIN/3Ob223_19v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei WestLebensmittel Betriebe GesmbH, Adalbert-Stifter-Platz 4, 3143 Gattring-Raking, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die verpflichtete Partei Dkfm.

**False Positives:**

- `Maur & Partner Rechtsanwälte GmbH & Co KG` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Roch`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Mag. Wessely-Kristöfel`(person)
- `WestLebensmittel Betriebe GesmbH`(organisation)
- `Adalbert-Stifter-Platz 4, 3143 Gattring-Raking, Österreich`(address)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/3Ob45_19t`) (sent_id: `deanon_260716_TRAIN/3Ob45_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Mag. Daniel Kutluk, vertreten durch Dr. Johannes Eltz, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Ferdinand Rittgerott, vertreten durch Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG in Graz, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die „außerordentliche“ Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 25. September 2018, GZ 4 R 102/18a-11, womit das Urteil des Bezirksgerichts Graz-West vom 27. Februar 2018, GZ 211 C 2/17g-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die „außerordentliche“ Revision wird zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Mag. Daniel Kutluk`(person)
- `Dr. Johannes Eltz`(person)
- `Mag. Ferdinand Rittgerott`(person)
- `Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Graz-West`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/3Ob49_11v`) (sent_id: `deanon_260716_TRAIN/3Ob49_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Julius ZYR Automotive GmbH & Co KG, Schamingstraße 16, 8262 Reigersberg, Österreich, vertreten durch Dr. Wolfgang Dartmann und andere Rechtsanwälte in Linz, wider die beklagten Parteien 1. Friedrich Strahsburg und 2.

**False Positives:**

- `Partei Julius ZYR Automotive GmbH & Co KG` — partial — gold is substring of pred: `ZYR Automotive GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `ZYR Automotive GmbH & Co KG`(organisation)
- `Schamingstraße 16, 8262 Reigersberg, Österreich`(address)
- `Dr. Wolfgang Dartmann`(person)
- `Friedrich Strahsburg`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/4Ob100_13d`) (sent_id: `deanon_260716_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Karen Böckel, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Düwall + Rief Daten -Aktiengesellschaft, Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ Eberhard Besemer ” Linda Hukauf, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Wehrle & Langer Rechtsanwälte KG` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Karen Böckel`(person)
- `Kosesnik-Wehrle & Langer Rechtsanwälte KG`(organisation)
- `Düwall + Rief Daten -Aktiengesellschaft`(organisation)
- `Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich`(address)
- `Raits Bleiziffer Rechtsanwälte GmbH`(organisation)
- `Eberhard Besemer`(person)
- `Linda Hukauf`(person)
- `Dr. Peter Zöchbauer`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/4Ob119_22m`) (sent_id: `deanon_260716_TRAIN/4Ob119_22m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek sowie die Hofräte Dr. Schwarzenbacher, Dr. Nowotny und Hon.-Prof. PD Dr. Rassi und die Hofrätin Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Silvester Schusterius KG, Brunnsteinweg 3, 9602 Draschitz, Österreich, vertreten durch Dr. Franz Krainer, Rechtsanwalt in Graz, gegen die beklagte Partei TalVerlag Manufaktur GmbH, Dr. Leopold Bauer-Gasse 105, 4843 Hinterschlagen, Österreich, vertreten durch die Hohenberg Rechtsanwälte GmbH in Graz, wegen 84.521,61 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz vom 12. Mai 2022, GZ 5 R 170/21s-33, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Silvester Schusterius KG` — partial — gold is substring of pred: `Silvester Schusterius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Mag. Istjan, LL.M.`(person)
- `Silvester Schusterius`(person)
- `Brunnsteinweg 3, 9602 Draschitz, Österreich`(address)
- `Dr. Franz Krainer`(person)
- `TalVerlag Manufaktur GmbH`(organisation)
- `Dr. Leopold Bauer-Gasse 105, 4843 Hinterschlagen, Österreich`(address)
- `Hohenberg Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Nimtz Pharma GmbH, Mildenbergstraße 11, 3072 Furth, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1) Unikel Landwirtschaft GmbH & Co KG und 2) Gode+Panköker Getränke GmbH, Martinsplatz 1-31, 9831 Kleindorf, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Provisorialverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 6. August 2010, GZ 5 R 150/10f-7, womit der Beschluss des Handelsgerichts Wien vom 24. Juni 2010, GZ 11 Cg 117/10h-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Sommer Rechtsanwälte KG` — partial — pred is substring of gold: `Gheneff - Rami - Sommer Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Nimtz Pharma GmbH`(organisation)
- `Mildenbergstraße 11, 3072 Furth, Österreich`(address)
- `Berger Saurer Zöchbauer, Rechtsanwälte`(organisation)
- `Unikel Landwirtschaft GmbH & Co KG`(organisation)
- `Gode+Panköker Getränke GmbH`(organisation)
- `Martinsplatz 1-31, 9831 Kleindorf, Österreich`(address)
- `Gheneff - Rami - Sommer Rechtsanwälte KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Lemlemcon GmbH, Albert-Schultz-Eishalle 4, 6863 Großdorf, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1. Koldere und Heddrich Versicherung GmbH & Co KG, 2.

**False Positives:**

- `Heddrich Versicherung GmbH & Co KG` — partial — pred is substring of gold: `Koldere und Heddrich Versicherung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Lemlemcon GmbH`(organisation)
- `Albert-Schultz-Eishalle 4, 6863 Großdorf, Österreich`(address)
- `Berger Saurer Zöchbauer, Rechtsanwälte`(organisation)
- `Koldere und Heddrich Versicherung GmbH & Co KG`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/6Ob139_19p`) (sent_id: `deanon_260716_TRAIN/6Ob139_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Balthasar Teske, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagte Partei Prof. Dr. Roderich Claaßens, vertreten durch Brauneis Klauser Prändl Rechtsanwälte GmbH in Wien, wegen Rechnungslegung und Zahlung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. April 2019, GZ 14 R 152/18b-16, womit das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 27. September 2018, GZ 4 Cg 50/17b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Maur & Partner Rechtsanwälte GmbH & Co KG` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Balthasar Teske`(person)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`(organisation)
- `Dr. Roderich Claaßens`(person)
- `Brauneis Klauser Prändl Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei QUMV Pflege GmbH, Nordring 89q, 2770 Gutenstein, Österreich, vertreten durch Dr. Peter Lindinger Dr. Andreas Pramer GesbR, Rechtsanwälte in Linz, wegen Unterlassung und Urteilsveröffentlichung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2019, GZ 3 R 141/18b-17, mit dem über Berufungen der klagenden und der beklagten Partei das Urteil des Landesgerichts Linz vom 2. September 2018, GZ 31 Cg 4/18a-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Wehrle & Langer Rechtsanwälte KG` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Verein für Konsumenteninformation`(organisation)
- `Kosesnik-Wehrle & Langer Rechtsanwälte KG`(organisation)
- `QUMV Pflege GmbH`(organisation)
- `Nordring 89q, 2770 Gutenstein, Österreich`(address)
- `Dr. Peter Lindinger`(person)
- `Dr. Andreas Pramer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/8Ob86_22p`) (sent_id: `deanon_260716_TRAIN/8Ob86_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen und Hofräte Dr. Tarmann-Prentner, Mag. Korn, Dr. Stefula und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Roland Buehn, Bakk. techn., vertreten durch Dr. Hannes Paulweber, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Silvius Tomzig, vertreten durch Dr. Roland Gabl Rechtsanwalts KG in Linz, wegen Unterhalt, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 2. Juni 2022, GZ 4 R 93/22p-66, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Roland Gabl Rechtsanwalts KG` — partial — pred is substring of gold: `Dr. Roland Gabl Rechtsanwalts KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Dr. Thunhart`(person)
- `Roland Buehn, Bakk. techn.`(person)
- `Dr. Hannes Paulweber`(person)
- `Silvius Tomzig`(person)
- `Dr. Roland Gabl Rechtsanwalts KG`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, MMag. Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Niels Doerfel, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Gudrun Kovalschuk Gesellschaft m.b.H. (FN FN119735f ), FN297530m, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Mag. Korn`(person)
- `MMag. Sloboda`(person)
- `Dr. Annerl`(person)
- `Niels Doerfel`(person)
- `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG`(organisation)
- `Gudrun Kovalschuk`(person)
- `FN119735f`(business_register_number)
- `FN297530m`(business_register_number)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/9ObA124_19d`) (sent_id: `deanon_260716_TRAIN/9ObA124_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hopf als Vorsitzenden, die Hofrätin Dr. Fichtenau und den Hofrat Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Bartscherer und Wagenknecht Holz GmbH & Co KG, Gotthelfgasse 57 - 74, 9361 Leimersberg, Österreich, vertreten durch Burgstaller & Preyer Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Richard Armgart, vertreten durch Mag. Franjo Schruiff, LL.M. Rechtsanwalt in Wien, wegen 14.927,23 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. August 2019, GZ 10 Ra 33/19z-30, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Wagenknecht Holz GmbH & Co KG` — partial — pred is substring of gold: `Bartscherer und Wagenknecht Holz GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hopf`(person)
- `Dr. Fichtenau`(person)
- `Dr. Hargassner`(person)
- `Dr. Peter Zeitler`(person)
- `Bartscherer und Wagenknecht Holz GmbH & Co KG`(organisation)
- `Gotthelfgasse 57 - 74, 9361 Leimersberg, Österreich`(address)
- `Burgstaller & Preyer Rechtsanwälte GmbH`(organisation)
- `Richard Armgart`(person)
- `Mag. Franjo Schruiff, LL.M.`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/9ObA144_14p`) (sent_id: `deanon_260716_TRAIN/9ObA144_14p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Franziska Schönmeier, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Heizung Bachkraftlog GmbH & Co KG, Schlangglfeld 48, 4980 Viehausen, Österreich, vertreten durch die Klein, Wuntschek & Partner Rechtsanwälte GmbH in Graz, wegen Kündigungsanfechtung, über die außerordentliche Revision und den „Kostenrekurs“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2014, GZ 7 Ra 66/14a-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Heizung Bachkraftlog GmbH & Co KG` — partial — gold is substring of pred: `Heizung Bachkraftlog GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Hargassner`(person)
- `KR Mag. Paul Kunsky`(person)
- `Harald Kohlruss`(person)
- `Franziska Schönmeier`(person)
- `Held Berdnik Astner & Partner Rechtsanwälte GmbH`(organisation)
- `Heizung Bachkraftlog GmbH & Co KG`(organisation)
- `Schlangglfeld 48, 4980 Viehausen, Österreich`(address)
- `Klein, Wuntschek & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/9ObA76_13m`) (sent_id: `deanon_260716_TRAIN/9ObA76_13m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Ernst Bassler als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adrian Leiße, BSc, vertreten durch Dr. H. Burmann ua, Rechtsanwälte in Innsbruck, gegen die beklagten Parteien 1. Logkraft-Verlag GmbH & Co KG, 2.

**False Positives:**

- `Verlag GmbH & Co KG` — partial — pred is substring of gold: `Logkraft-Verlag GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Mag. Dr. Rolf Gleißner`(person)
- `Mag. Ernst`(person)
- `Adrian Leiße, BSc`(person)
- `Logkraft-Verlag GmbH & Co KG`(organisation)

</details>

---

## `Aktiengesellschaft Compound` 🏆

**F1:** 0.005 | **Precision:** 0.126 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `823d2f2a`  
**Description:**
Matches compound organization names ending in 'Aktiengesellschaft' or 'AG', allowing for possessive adjectives and specific names. STRICTLY requires a capitalized name prefix before the suffix.

**Content:**
```
(?<!\w)([A-Z][a-zA-Z0-9\-\.]+(?:\s+[A-Z][a-zA-Z\-\.]+)*(?:\s+und\s+der\s+[A-Z][a-zA-Z\-\.]+)*(?:\s+\u00d6sterreichischen\s+[A-Z][a-zA-Z\-\.]+)*(?:\s+Aktiengesellschaft|\s+AG))(?!\s+(?:an|der|die|das|und|von|mit|in|auf|bei|f\u00fcr|zur|am|im|vom|bis|nach|vor|\u00fcber|unter|ohne|gegen|durch|f\u00fcr|seit|neben|zwischen|hinter|\.|,|\)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.126 | 0.003 | 0.005 | 87 | 11 | 76 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 76 | 3990 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Unter-Analyse Aktiengesellschaft` | `Unter-Analyse Aktiengesellschaft` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Mag. Malesich` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Pascal Alsweh` (person)
- `Stephan Briem Rechtsanwalt GmbH` (organisation)
- `Dr. Simone Pittruff` (person)
- `Shamiyeh & Reiser Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_34`)


Der von den Beklagten erhobene (und mit dem Fehlen der Passivlegitimation verbundene) Einwand, es sei auch das Ersitzungsverbot öffentlichen Wasserguts (oder eine Ersitzung gegenüber der Österreichische Bundesforste AG bzw deren Rechtsvorgänger) zu prüfen, scheitert schon daran.

| Predicted | Gold |
|---|---|
| `Bundesforste AG` | `Bundesforste AG` |

**Example 2** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_4`)


Wien Derconlex AG, Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich, vertreten durch Mag. Klemens Mayer, Mag. Stefan Herrmann Rechtsanwälte in Wien, wegen 410.325,23 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Mai 2020, GZ 30 R 106/20h-73, mit dem das Urteil des Handelsgerichts Wien vom 15. Jänner 2020, GZ 10 Cg 15/16k-69, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wien Derconlex AG` | `Wien Derconlex AG` |

**Missed by this rule (FN):**

- `Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich` (address)
- `Mag. Klemens Mayer` (person)
- `Mag. Stefan Herrmann` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Xaver Springinsgut, Rechtsanwalt in St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jähnel in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Alpen Nexlex AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Schulgartenweg 18, 9872 Grantsch, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Jiran, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Alpen Nexlex AG` | `Alpen Nexlex AG` |

**Missed by this rule (FN):**

- `Dr. Xaver Springinsgut` (person)
- `St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich` (address)
- `Elfriede Jähnel` (person)
- `Bezirksgerichts Innsbruck` (organisation)
- `Bezirksgerichts Amstetten` (organisation)
- `Landesgericht Linz` (organisation)
- `Bezirksgericht Amstetten` (organisation)
- `Schulgartenweg 18, 9872 Grantsch, Österreich` (address)
- `Roman Jiran` (person)

**Example 4** (doc_id: `deanon_260716_TRAIN/2Nc25_11s`) (sent_id: `deanon_260716_TRAIN/2Nc25_11s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Laurence Voelkers, Bakk. techn., vertreten durch Dr. Thomas Praxmarer, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1) HR Birgit Krolitzki, und 2) DonauBau Versicherungs AG Am Schierlinggrund 4, 8490 Hummersdorf, Österreich, beide vertreten durch Dr. Heribert Schar, Dr. Bernhard Schmidhammer, Rechtsanwälte in Innsbruck, wegen 21.664,61 EUR und Feststellung den Beschluss gefasst:  Spruch Es wird die Befangenheit sämtlicher Richterinnen und Richter des Oberlandesgerichts Innsbruck festgestellt. Zur (Verhandlung und) Entscheidung als Berufungsgericht im Verfahren 41 Cg 23/10s des Landesgerichts Innsbruck wird das Oberlandesgericht Linz als zuständig bestimmt (§ 30 JN).

| Predicted | Gold |
|---|---|
| `DonauBau Versicherungs AG` | `DonauBau Versicherungs AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Baumann` (person)
- `Dr. Veith` (person)
- `Dr. E. Solé` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Nowotny` (person)
- `Laurence Voelkers, Bakk. techn.` (person)
- `Dr. Thomas Praxmarer` (person)
- `HR Birgit Krolitzki` (person)
- `Am Schierlinggrund 4, 8490 Hummersdorf, Österreich` (address)
- `Dr. Heribert Schar` (person)
- `Dr. Bernhard Schmidhammer` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)
- `Oberlandesgericht Linz` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Uniber-Verlag AG` | `Uniber-Verlag AG` |
| `Fenuni AG` | `Fenuni AG` |

**Missed by this rule (FN):**

- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)
- `Liebenwein Rechtsanwälte GmbH` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_4`)


Guntram Wellenbring, vertreten durch Dr. Peter Sparer, Rechtsanwalt in Innsbruck, 2. Verbruckal AG, Stäpfle 16, 1020 Wien, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `Verbruckal AG` | `Verbruckal AG` |

**Missed by this rule (FN):**

- `Guntram Wellenbring` (person)
- `Dr. Peter` (person)
- `Stäpfle 16, 1020 Wien, Österreich` (address)
- `Dr. Harald Burmann` (person)

**Example 7** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_5`)


See-Umwelt Manufaktur AG, Zosen 244, 9543 Sauboden, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `See-Umwelt Manufaktur AG` | `See-Umwelt Manufaktur AG` |

**Missed by this rule (FN):**

- `Zosen 244, 9543 Sauboden, Österreich` (address)
- `Dr. Walter Heel` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/4Ob9_20g`) (sent_id: `deanon_260716_TRAIN/4Ob9_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ingrid Marke, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) ZTYW Solar Vertrieb GmbH, Hans-Woerle-Weg 13, 4852 Gahberg, Österreich, und 2) Hoch Fenfurtmon Systeme AG, Raxer Straße 24, 8952 Kienach, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `Hoch Fenfurtmon Systeme AG` | `Hoch Fenfurtmon Systeme AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Vogel` (person)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `Ingrid Marke` (person)
- `Poduschka Anwaltsgesellschaft mbH` (organisation)
- `ZTYW Solar Vertrieb GmbH` (organisation)
- `Hans-Woerle-Weg 13, 4852 Gahberg, Österreich` (address)
- `Raxer Straße 24, 8952 Kienach, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_8`)


Hätte sie pflichtgemäß gehandelt und den von ihr geprüften Jahresabschlüssen den Bestätigungsvermerk versagt, hätte er die Aktien nicht gekauft und damit – wegen der kurz nach seinen Käufen von der EnnsMaschinenbau AG beantragten Insolvenzeröffnung – keinen Schaden erlitten.

| Predicted | Gold |
|---|---|
| `EnnsMaschinenbau AG` | `EnnsMaschinenbau AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Antonewitz Chemie AG` — partial — pred is substring of gold: `Langhansl+Antonewitz Chemie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Mag. Johannes Bügler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__16`)


Mit Urteil desselben Tages erkannte das Gericht den Angeklagten „im Sinne der Anklageschrift“ des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie mehrerer Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB schuldig, verhängte über ihn eine Freiheitsstrafe und verpflichtete ihn, an die Privatbeteiligte St Donau Triheim AG einen Geldbetrag zu bezahlen.

**False Positives:**

- `Privatbeteiligte St Donau Triheim AG` — partial — gold is substring of pred: `Donau Triheim AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donau Triheim AG`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_5`)


Text Begründung: Die Nortal-Energie Aktiengesellschaft (im Folgenden: Schuldnerin) betrieb einen Ferienclub.

**False Positives:**

- `Die Nortal-Energie Aktiengesellschaft` — partial — gold is substring of pred: `Nortal-Energie Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nortal-Energie Aktiengesellschaft`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen, Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bachfen Entwicklung AG, Reisedt 4, 4770 Radlern, Österreich, vertreten durch Mag. Markus Stender, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Musialek Getränke GmbH, 2.

**False Positives:**

- `Partei Bachfen Entwicklung AG` — partial — gold is substring of pred: `Bachfen Entwicklung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Mag. Korn`(person)
- `Bachfen Entwicklung AG`(organisation)
- `Reisedt 4, 4770 Radlern, Österreich`(address)
- `Mag. Markus Stender`(person)
- `Musialek Getränke GmbH`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob163_21h`) (sent_id: `deanon_260716_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Christine Neemeyer, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Synbach-Holz Bank AG, Bergbahnweg 7j, 4632 Oberthambach, Österreich, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Synbach-Holz Bank AG` — partial — gold is substring of pred: `Synbach-Holz Bank`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Christine Neemeyer`(person)
- `Mag. Dieter Koch`(person)
- `Mag. Natascha Jilek`(person)
- `Synbach-Holz Bank`(organisation)
- `Bergbahnweg 7j, 4632 Oberthambach, Österreich`(address)
- `Mag. Martina Hosp`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partei MittelEnergie Werke Bank AG` — partial — gold is substring of pred: `MittelEnergie Werke Bank`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Florenzia Münsterer`(person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `MittelEnergie Werke Bank`(organisation)
- `Altlassing 110, 4183 Ahorn, Österreich`(address)
- `Urbanek Lind Schmied Reisch Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_52`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_4`)


Gloria Hackenbuchner GmbH, Untere Kanalstraße 187, 2471 Hollern, Österreich, vertreten durch Mag. Manfred Sommerbauer und MMag. Dr. Michael Dohr LL.M., Rechtsanwälte in Wiener Neustadt, und 2. Nelleßen + Stümpfel Automotive AG, Villengasse 31, 8670 Krieglach, Österreich, vertreten durch die Kosch & Partner Rechtsanwälte GmbH, Wiener Neustadt, wegen 76.444,01 EUR sA über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2017, GZ 1 R 164/16v-174, mit dem das Urteil des Handelsgerichts Wien vom 12. August 2016, GZ 65 Cg 12/15x-169, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Automotive AG` — partial — pred is substring of gold: `Nelleßen + Stümpfel Automotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gloria Hackenbuchner`(person)
- `Untere Kanalstraße 187, 2471 Hollern, Österreich`(address)
- `Mag. Manfred Sommerbauer`(person)
- `MMag. Dr. Michael Dohr LL.M.`(person)
- `Nelleßen + Stümpfel Automotive AG`(organisation)
- `Villengasse 31, 8670 Krieglach, Österreich`(address)
- `Kosch & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_9`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Bornwasser & Plöckinger Druck AG; von derselben intendierte Verwertung der Liegenschaften in Thalstraße 358X, 5232 Aigen, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Am Weinbühel 2, 5201 Wimm, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Druck AG` — partial — pred is substring of gold: `Bornwasser & Plöckinger Druck AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bornwasser & Plöckinger Druck AG`(organisation)
- `Thalstraße 358X, 5232 Aigen, Österreich`(address)
- `Am Weinbühel 2, 5201 Wimm, Österreich`(address)

**Example 10** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Schwarzig Medien Aktiengesellschaft, Balthasar-Waltl-Weg 227, 3921 Kehrbach, Österreich, vertreten durch die Kunz Schima Wallentin Rechtsanwälte OG in Wien, und der Nebenintervenientinnen auf Seiten der klagenden Partei 1.

**False Positives:**

- `Partei Schwarzig Medien Aktiengesellschaft` — partial — gold is substring of pred: `Schwarzig Medien Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Baumann`(person)
- `Dr. Veith`(person)
- `Dr. E. Solé`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Schwarzig Medien Aktiengesellschaft`(organisation)
- `Balthasar-Waltl-Weg 227, 3921 Kehrbach, Österreich`(address)
- `Kunz Schima Wallentin Rechtsanwälte OG`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/2Ob216_18f`) (sent_id: `deanon_260716_TRAIN/2Ob216_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Sandra Olbrechts, vertreten durch Mag. Martin Paar und Mag. Hermann Zwanzger, Rechtsanwälte in Wien, gegen die beklagte Partei Inn Kraftfengart AG, Julius Jax-Gasse 64, 4623 Waldenberg, Österreich, vertreten durch Dr. Helmut Weinzettl, Rechtsanwalt in Wiener Neustadt, wegen 14.817,50 EUR sA, über die Revisionen beider Parteien gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Juni 2018, GZ 18 R 11/18y-64, mit welchem das Urteil des Bezirksgerichts Baden vom 28. Dezember 2017, GZ 7 C 1010/15x-58, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `Partei Inn Kraftfengart AG` — partial — gold is substring of pred: `Inn Kraftfengart AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Sandra Olbrechts`(person)
- `Mag. Martin Paar`(person)
- `Mag. Hermann Zwanzger`(person)
- `Inn Kraftfengart AG`(organisation)
- `Julius Jax-Gasse 64, 4623 Waldenberg, Österreich`(address)
- `Dr. Helmut Weinzettl`(person)
- `Landesgerichts Wiener Neustadt`(organisation)
- `Bezirksgerichts Baden`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/2Ob256_12d`) (sent_id: `deanon_260716_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Winkelmayer KI Aktiengesellschaft, Hetzendorf Frachtenbahnhof 69, 4074 Knieparz ob der Leiten, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei Tatjana Adameit, vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Winkelmayer KI Aktiengesellschaft` — partial — gold is substring of pred: `Winkelmayer KI Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Baumann`(person)
- `Dr. Veith`(person)
- `Dr. E. Solé`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Winkelmayer KI Aktiengesellschaft`(organisation)
- `Hetzendorf Frachtenbahnhof 69, 4074 Knieparz ob der Leiten, Österreich`(address)
- `Dr. Manfred Steininger`(person)
- `Tatjana Adameit`(person)
- `ANWALTGMBH Rinner Teuchtmann`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/2Ob71_18g`) (sent_id: `deanon_260716_TRAIN/2Ob71_18g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Adrian Niel, vertreten durch Dr. Robert Eiter, Rechtsanwalt in Landeck, gegen die beklagte Partei Nexzor AG, Obernreith 59, 6094 Kristen, Österreich, Deutschland, vertreten durch Dr. Andreas Kolar, Rechtsanwalt in Innsbruck, wegen 17.260,29 EUR sA, über die Revision der klagenden Partei gegen das Teilurteil des Landesgerichts Innsbruck als Berufungsgericht vom 14. November 2017, GZ 1 R 188/17d-69, mit welchem das Urteil des Bezirksgerichts Landeck vom 18. Mai 2017, GZ 2 C 123/14w-63, teilweise abgeändert wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Nexzor AG` — partial — gold is substring of pred: `Nexzor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `Adrian Niel`(person)
- `Dr. Robert Eiter`(person)
- `Nexzor AG`(organisation)
- `Obernreith 59, 6094 Kristen, Österreich`(address)
- `Dr. Andreas Kolar`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Landeck`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Niklas Nikoloff, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Wetzlau+Härdle Versicherung AG, Maulwurfgasse 2, 4090 Stadl, Österreich, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Versicherung AG` — partial — pred is substring of gold: `Wetzlau+Härdle Versicherung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Baumann`(person)
- `Dr. Veith`(person)
- `Dr. E. Solé`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Niklas Nikoloff`(person)
- `Mag. Michael Hirm`(person)
- `Wetzlau+Härdle Versicherung AG`(organisation)
- `Maulwurfgasse 2, 4090 Stadl, Österreich`(address)
- `Dr. Martin Wuelz`(person)

**Example 15** (doc_id: `deanon_260716_TRAIN/2Ob99_24h`) (sent_id: `deanon_260716_TRAIN/2Ob99_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende und die Hofräte MMag. Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei ÖBB-Infrastruktur Aktiengesellschaft, Kathreinweg 48, 4572 Schalchgraben, Österreich, vertreten durch Dr. Martin Wandl und Dr. Wolfgang Krempl, Rechtsanwälte in St. Pölten, gegen die beklagten Parteien 1. Melina McNaughtan, 2. Ophelia Middelkamp, und 3. ÖkR HR Karlheinz Göttl, alle vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, wegen 54.038,42 EUR sA, über die Revisionen sämtlicher Streitteile gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. März 2024, GZ 11 R 5/24w-61, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Linz vom 28. November 2023, GZ 5 Cg 82/22m-54, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `Infrastruktur Aktiengesellschaft` — partial — pred is substring of gold: `ÖBB-Infrastruktur Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `ÖBB-Infrastruktur Aktiengesellschaft`(organisation)
- `Kathreinweg 48, 4572 Schalchgraben, Österreich`(address)
- `Dr. Martin Wandl`(person)
- `Dr. Wolfgang Krempl`(person)
- `Melina McNaughtan`(person)
- `Ophelia Middelkamp`(person)
- `ÖkR HR Karlheinz Göttl`(person)
- `Dr. Peter Lindinger`(person)
- `Dr. Andreas Pramer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Garten AG` — partial — pred is substring of gold: `Lützeler Garten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Roch`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `James Weyand, MA`(person)
- `Dr. Nader Karl Mahdi`(person)
- `Lützeler Garten AG`(organisation)
- `Esteplatz 2, 9064 Schöpfendorf, Österreich`(address)
- `Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH`(organisation)
- `Demeyer u. Köktas Analyse GmbH`(organisation)
- `Zinkendorferstraße 100, 9321 Schöttlhof, Österreich`(address)
- `Dr. Christian Girardi, LL.M.`(person)
- `Ing. Dr. Stefan Schwärzler`(person)
- `Mag. Daniel Pichler`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei GDH Metall AG, Weinzierl-Josef Pfeiffer-Str. 6, 3443 Gerersdorf, Österreich, vertreten durch Dr. Hartmut Mayer, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Finn Hierle, vertreten durch Mag. Gerhard Pilz, Rechtsanwalt, als Verfahrenshelfer, wegen 3.330,19 EUR sA (AZ 35 R 24/09b des Landesgerichts für Zivilrechtssachen Wien), zum Fristsetzungsantrag der beklagten Partei vom 28. Oktober 2009 an den Obersten Gerichtshof im Ablehnungsverfahren den Beschluss gefasst:  Spruch Der Fristsetzungsantrag wird zurückgewiesen.

**False Positives:**

- `Partei GDH Metall AG` — partial — gold is substring of pred: `GDH Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `GDH Metall AG`(organisation)
- `Weinzierl-Josef Pfeiffer-Str. 6, 3443 Gerersdorf, Österreich`(address)
- `Dr. Hartmut Mayer`(person)
- `Mag. Finn Hierle`(person)
- `Mag. Gerhard Pilz`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_5`)


Sanitär Norfurtwerk AG, Piburger Straße 20, 4204 Hadersdorf, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Norfurtwerk AG` — partial — pred is substring of gold: `Sanitär Norfurtwerk AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sanitär Norfurtwerk AG`(organisation)
- `Piburger Straße 20, 4204 Hadersdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/4Ob165_09g`) (sent_id: `deanon_260716_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei DRH Cloud AG, Viertlerweg 451, 2533 Glashütten, Österreich, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei West Steinfen AG, Josef-Kainzmayer-Gasse 9, 4271 Witzelsberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Partei DRH Cloud AG` — partial — gold is substring of pred: `DRH Cloud AG`
- `Partei West Steinfen AG` — partial — gold is substring of pred: `West Steinfen AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `DRH Cloud AG`(organisation)
- `Viertlerweg 451, 2533 Glashütten, Österreich`(address)
- `Ewald Weninger Rechtsanwalts GmbH`(organisation)
- `West Steinfen AG`(organisation)
- `Josef-Kainzmayer-Gasse 9, 4271 Witzelsberg, Österreich`(address)
- `Schönherr Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/4Ob174_24b`) (sent_id: `deanon_260716_TRAIN/4Ob174_24b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Greule Recycling GmbH, Staudenweg, Oberau 49, 3571 Stallegg, Österreich, vertreten durch Mag. Dieter Koch, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei HEWQ IT Institut AG, Enengl-Florianiweg 15, 4892 Grubleiten, Österreich, vertreten durch die AHP Rechtsanwälte OG in Klagenfurt am Wörthersee, wegen 171.573,05 CHF sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 11. Juli 2024, GZ 4 R 62/24f-26, mit dem das Urteil des Landesgerichts Klagenfurt vom 31. Jänner 2024, GZ 20 Cg 40/23v-20, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei HEWQ IT Institut AG` — partial — gold is substring of pred: `HEWQ IT Institut AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Waldstätten`(person)
- `Dr. Stiefsohn`(person)
- `Greule Recycling GmbH`(organisation)
- `Staudenweg, Oberau 49, 3571 Stallegg, Österreich`(address)
- `Mag. Dieter Koch`(person)
- `HEWQ IT Institut AG`(organisation)
- `Enengl-Florianiweg 15, 4892 Grubleiten, Österreich`(address)
- `AHP Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/4Ob19_10p`) (sent_id: `deanon_260716_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Planung gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei Deecken Event AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Deecken Event AG` — partial — gold is substring of pred: `Deecken Event AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `StadtEnergie Planung gesellschaft mbH`(organisation)
- `Prof. Haslinger & Partner, Rechtsanwälte`(organisation)
- `Deecken Event AG`(organisation)
- `Oberlandesgerichts Graz`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Florentin Jakobautzki, vertreten durch die Konrad Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Lischke&Rohleff Solar AG, Volkshausplatz 46, 3830 Pyhra, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 106.196,74 EUR sA und Feststellung (Streitwert 156.303,26 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Oktober 2017, GZ 129 R 24/17y-24, womit das Urteil des Handelsgerichts Wien vom 2. August 2017, GZ 10 Cg 1/16a-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohleff Solar AG` — partial — pred is substring of gold: `Lischke&Rohleff Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Vogel`(person)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Rassi`(person)
- `MMag. Matzka`(person)
- `Mag. Florentin Jakobautzki`(person)
- `Konrad Rechtsanwälte GmbH`(organisation)
- `Lischke&Rohleff Solar AG`(organisation)
- `Volkshausplatz 46, 3830 Pyhra, Österreich`(address)
- `Binder Grösswang Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/5Ob102_24x`) (sent_id: `deanon_260716_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei ÖkR KzlR Sonja Doganoglu, wider die beklagte Partei Stoeberl Bau AG, Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Stoeberl Bau AG` — partial — gold is substring of pred: `Stoeberl Bau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `ÖkR KzlR Sonja Doganoglu`(person)
- `Stoeberl Bau AG`(organisation)
- `Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Ried im Innkreis`(organisation)
- `Bezirksgerichts Schärding`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Svenja Brochtrup, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei EnnsFinanzen AG, Bartlstraße 9, 8490 Zelting, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Partei EnnsFinanzen AG` — partial — gold is substring of pred: `EnnsFinanzen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Svenja Brochtrup`(person)
- `EnnsFinanzen AG`(organisation)
- `Bartlstraße 9, 8490 Zelting, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/5Ob221_22v`) (sent_id: `deanon_260716_TRAIN/5Ob221_22v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Berg-E‑Commerce Dienstleistungen GmbH in Liquidation, Rotundenplatz 78, 8403 Stangersdorf-Gewerbegebiet, Österreich, vertreten durch Mag. Gottfried Tazol, Rechtsanwalt in Völkermarkt, gegen die beklagte Partei Logistik Waldseecon AG, Am Kurplatz 2, 5761 Bachwinkl, Österreich, vertreten durch Mag. Alexander Todor-Kostic LL.M., Mag. Silke Todor-Kostic, Rechtsanwälte in Velden am Wörthersee, wegen 84.999,13 EUR sA, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 62.200,50 EUR sA) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. Oktober 2022, GZ 5 R 74/22z-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Logistik Waldseecon AG` — partial — gold is substring of pred: `Logistik Waldseecon AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Berg-E‑Commerce Dienstleistungen GmbH`(organisation)
- `Rotundenplatz 78, 8403 Stangersdorf-Gewerbegebiet, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Logistik Waldseecon AG`(organisation)
- `Am Kurplatz 2, 5761 Bachwinkl, Österreich`(address)
- `Mag. Alexander Todor-Kostic`(person)
- `Mag. Silke Todor-Kostic`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/6Ob10_22x`) (sent_id: `deanon_260716_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Tralog-KI Versicherungs AG, Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei WaldRecycling GmbH, Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Tralog-KI Versicherungs AG` — partial — gold is substring of pred: `Tralog-KI Versicherungs AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Dr. Nowotny`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `Tralog-KI Versicherungs AG`(organisation)
- `Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich`(address)
- `Musey Rechtsanwalt GmbH`(organisation)
- `WaldRecycling GmbH`(organisation)
- `Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Tiffany Jähncke, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei Sudconbach-Bau AG, Hart, Akazienstraße 15v, 4064 Oftering, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Partei Sudconbach-Bau AG` — partial — gold is substring of pred: `Sudconbach-Bau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Hon.-Prof. Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `Dr. Weber`(person)
- `Mag. Nigl`(person)
- `Ing. Tiffany Jähncke`(person)
- `Poduschka Partner Anwaltsgesellschaft mbH`(organisation)
- `Sudconbach-Bau AG`(organisation)
- `Hart, Akazienstraße 15v, 4064 Oftering, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Linz`(organisation)
- `Bezirksgerichts Traun`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_137`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/6Ob47_25t`) (sent_id: `deanon_260716_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Kimberly Schnellhardt, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Digital Trasudwerk AG, Galles 5, 8453 Kitzelsdorf, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Partei Digital Trasudwerk AG` — partial — gold is substring of pred: `Digital Trasudwerk AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `Dr. Weber`(person)
- `Mag. Nigl`(person)
- `Kimberly Schnellhardt`(person)
- `Dr. Alexander Amann LL.M.`(person)
- `Digital Trasudwerk AG`(organisation)
- `Galles 5, 8453 Kitzelsdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/6Ob51_21z`) (sent_id: `deanon_260716_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Fabienne Müffler, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei See Conlemgart Gruppe Bank Schlötels&Katzenberg Digital AG, C - Obersee 27A, 4963 Nöfing, Österreich, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

**False Positives:**

- `Katzenberg Digital AG` — partial — pred is substring of gold: `Schlötels&Katzenberg Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Fabienne Müffler`(person)
- `Dr. Wolfgang Haslinger, LL.M.`(person)
- `See Conlemgart Gruppe Bank`(organisation)
- `Schlötels&Katzenberg Digital AG`(organisation)
- `C - Obersee 27A, 4963 Nöfing, Österreich`(address)
- `Dr. Anton Ehm`(person)
- `Mag. Thomas Mödlagl`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/7Nc6_13m`) (sent_id: `deanon_260716_TRAIN/7Nc6_13m_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Sabrina Dijkman, vertreten durch Dr. Clemens Gärner, Rechtsanwalt in Wien, gegen die beklagte Partei FPZE Metall AG, Jeitnerweg 110, 8773 Seiz, Österreich, vertreten durch Dr. Helmut Engelbrecht und andere Rechtsanwälte in Wien, wegen 4.868,07 EUR sA und Feststellung, über die Befangenheitsanzeige des Hofrats des Obersten Gerichtshofs Dr. Richard Hargassner im Verfahren 9 ObA 29/13z den Beschluss gefasst:  Spruch Der Hofrat des Obersten Gerichtshofs Dr. Richard Hargassner ist ausgeschlossen.

**False Positives:**

- `Partei FPZE Metall AG` — partial — gold is substring of pred: `FPZE Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Dr. Sabrina Dijkman`(person)
- `Dr. Clemens Gärner`(person)
- `FPZE Metall AG`(organisation)
- `Jeitnerweg 110, 8773 Seiz, Österreich`(address)
- `Dr. Helmut Engelbrecht`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Richard Hargassner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Richard Hargassner`(person)

**Example 32** (doc_id: `deanon_260716_TRAIN/7Ob110_13x`) (sent_id: `deanon_260716_TRAIN/7Ob110_13x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Gerdelbracht Telekom AG, KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, gegen die beklagte Partei Mag. (FH) Franz Burgschmidt, vertreten durch Binder Grösswang Rechtsanwälte OG in Wien, wegen Erteilung von Auskünften, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. April 2013, GZ 11 R 75/13z-12, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Gerdelbracht Telekom AG` — partial — gold is substring of pred: `Gerdelbracht Telekom AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Gerdelbracht Telekom AG`(organisation)
- `KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich`(address)
- `Kunz Schima Wallentin Rechtsanwälte OG`(organisation)
- `Mag. (FH) Franz Burgschmidt`(person)
- `Binder Grösswang Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/7Ob113_17v`) (sent_id: `deanon_260716_TRAIN/7Ob113_17v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Camilla Löble, vertreten durch Waltl & Partner, Rechtsanwälte in Zell am See, gegen die beklagte Partei Sieckkötter Medien AG, 6.

**False Positives:**

- `Medien AG` — partial — pred is substring of gold: `Sieckkötter Medien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Camilla Löble`(person)
- `Sieckkötter Medien AG`(organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/7Ob129_10m`) (sent_id: `deanon_260716_TRAIN/7Ob129_10m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Mario Maiers AG, Krippau 33, 5652 Dienten am Hochkönig, Österreich, vertreten durch Mag. Dr. Hans Herwig Toriser, Rechtsanwalt in Klagenfurt, gegen die beklagte Partei Merlin Paolini, vertreten durch Dr. Erich Moser, Rechtsanwalt in Murau, wegen 11.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. April 2010, GZ 2 R 45/10w-27, womit das Urteil des Landesgerichts Leoben vom 28. Jänner 2010, GZ 7 Cg 130/09k-23, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Mario Maiers AG` — partial — gold is substring of pred: `Mario Maiers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Huber`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schaumüller`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Dr. Grohmann`(person)
- `Mario Maiers`(person)
- `Krippau 33, 5652 Dienten am Hochkönig, Österreich`(address)
- `Mag. Dr. Hans Herwig Toriser`(person)
- `Merlin Paolini`(person)
- `Dr. Erich Moser`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Leoben`(organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/7Ob137_17y`) (sent_id: `deanon_260716_TRAIN/7Ob137_17y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Elias Hemerle, vertreten durch die Breiteneder Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Mooshuber Planung AG, Schustergasse 57, 4682 Brunau, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Mai 2017, GZ 4 R 19/17v-16, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Mooshuber Planung AG` — partial — gold is substring of pred: `Mooshuber Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Elias Hemerle`(person)
- `Breiteneder Rechtsanwalt GmbH`(organisation)
- `Mooshuber Planung AG`(organisation)
- `Schustergasse 57, 4682 Brunau, Österreich`(address)
- `Binder Grösswang Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/7Ob137_20b`) (sent_id: `deanon_260716_TRAIN/7Ob137_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätin und die Hofräte Hon.-Prof. Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Edwin Bornemeyer, vertreten durch die Pilz & Burghofer Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Thönniß Immobilien AG, Dürnstein in der Steiermark 55, 3920 Josefsdorf, Österreich, vertreten durch Mag. Dr. Otto Ranzenhofer, Rechtsanwalt in Wien, wegen 300.000 EUR sA, den Beschluss gefasst:  Spruch Das Urteil des Obersten Gerichtshofs vom 25. November 2020, AZ 7 Ob 137/20b, wird wie folgt berichtigt: Im Spruchpunkt 2. hat die Wortfolge: „samt 4 % Zinsen seit 3. 11. 2014“ zu entfallen.

**False Positives:**

- `Immobilien AG` — partial — pred is substring of gold: `Thönniß Immobilien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Mag. Edwin Bornemeyer`(person)
- `Pilz & Burghofer Rechtsanwalts GmbH`(organisation)
- `Thönniß Immobilien AG`(organisation)
- `Dürnstein in der Steiermark 55, 3920 Josefsdorf, Österreich`(address)
- `Mag. Dr. Otto Ranzenhofer`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/7Ob162_20d`) (sent_id: `deanon_260716_TRAIN/7Ob162_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dorothea Waeger, Bakk. techn. BEd, vertreten durch Mag. Marco und Mag. Amelie Kunczicky, Rechtsanwälte in Mayrhofen, gegen die beklagte Partei OberVerlag AG, Thomas Alva Edison-Straße 158, 4843 Wörmansedt, Österreich, vertreten durch Mag. Thomas Anker und DI Mag. Nikolaus Gratl, Rechtsanwäte in Innsbruck, wegen Urkundeneinsicht, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Juni 2020, GZ 4 R 55/20z-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei OberVerlag AG` — partial — gold is substring of pred: `OberVerlag AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dorothea Waeger, Bakk. techn. BEd`(person)
- `Mag. Marco`(person)
- `Mag. Amelie Kunczicky`(person)
- `OberVerlag AG`(organisation)
- `Thomas Alva Edison-Straße 158, 4843 Wörmansedt, Österreich`(address)
- `Mag. Thomas Anker`(person)
- `DI Mag. Nikolaus Gratl`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätin und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, MMag. Matzka und Dr. Weber als weitere Richter in der Rechtssache der klagenden Partei Dr. Shirley Steidten, vertreten durch Koch Jilek Rechtsanwälte Partnerschaft in Bruck an der Mur, gegen die beklagte Partei WienMonlemalTextil Aktiengesellschaft, Ernst Wolf-Gasse 216, 4650 Schußstatt, Österreich, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 15. Juli 2021, GZ 4 R 53/21b-25, womit das Urteil des Landesgerichts Leoben vom 16. Dezember 2020, GZ 5 Cg 57/19z-19, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei WienMonlemalTextil Aktiengesellschaft` — partial — gold is substring of pred: `WienMonlemalTextil Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Weber`(person)
- `Dr. Shirley Steidten`(person)
- `Koch Jilek Rechtsanwälte Partnerschaft`(organisation)
- `WienMonlemalTextil Aktiengesellschaft`(organisation)
- `Ernst Wolf-Gasse 216, 4650 Schußstatt, Österreich`(address)
- `Dr. Andreas A. Lintl`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Leoben`(organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/7Ob192_16k`) (sent_id: `deanon_260716_TRAIN/7Ob192_16k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Mikolaj Frosch, vertreten durch Mag. Klaus Fürlinger und andere Rechtsanwälte in Linz, gegen die beklagte Partei RheinMarine AG, Zeiseleck 30, 4170 Sankt Oswald bei Haslach, Österreich, vertreten durch Mag. Gerlach Bachinger, Rechtsanwalt in Traun, wegen 25.452,37 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 30. August 2016, GZ 6 R 148/16a-14, womit das Urteil des Landesgerichts Linz vom 20. Mai 2016, GZ 5 Cg 11/16m-10, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Partei RheinMarine AG` — partial — gold is substring of pred: `RheinMarine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Mag. Mikolaj Frosch`(person)
- `Mag. Klaus Fürlinger`(person)
- `RheinMarine AG`(organisation)
- `Zeiseleck 30, 4170 Sankt Oswald bei Haslach, Österreich`(address)
- `Mag. Gerlach Bachinger`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, 1041 Wien, Prinz-Eugen-Straße 20-22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Sudlex Heizung AG, Weißenbachstraße 12, 9376 Lichtegg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2011, GZ 2 R 203/11d-11, womit das Urteil des Handelsgerichts Wien vom 26. Juni 2011, GZ 19 Cg 49/11v-5, teilweise abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Sudlex Heizung AG` — partial — gold is substring of pred: `Sudlex Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Dr. Walter Reichholf`(person)
- `Sudlex Heizung AG`(organisation)
- `Weißenbachstraße 12, 9376 Lichtegg, Österreich`(address)
- `Schönherr Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_256`)


Von § 28a Abs 1 KSchG sollen also gerade Fälle wie der vorliegende erfasst werden, bei denen ein gesetzwidriges Verhalten gesetzt wird, ohne dass der Unternehmer AGB oder allgemeine Vertragsformblätter verwendet.

**False Positives:**

- `Unternehmer AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Technik AG` — partial — pred is substring of gold: `Plönnigs Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `Dr. Weber`(person)
- `Mag. Fitz`(person)
- `Mag. Jelinek`(person)
- `Gundula Aichmann`(person)
- `Poduschka Partner Anwaltsgesellschaft mbH`(organisation)
- `Plönnigs Technik AG`(organisation)
- `Wieden 35, 3390 Spielberg, Österreich`(address)
- `Themmer, Toth & Partner Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)
- `Bezirksgerichts für Handelssachen Wien`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/7Ob45_19x`) (sent_id: `deanon_260716_TRAIN/7Ob45_19x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Arabella Venczel, vertreten durch Dr. Stefan Gloyer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Berkenheger Analyse AG, Ebendorfer Hauptstraße 3, 8054 Graz, Österreich, vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, wegen 53.526,48 EUR sA und Feststellung, den Beschluss gefasst:  Spruch Das Urteil des Obersten Gerichtshofs vom 26. Juni 2019, zu 7 Ob 45/19x wird in seinen Entscheidungsgründen dahin berichtigt, dass es auf Seite 8 in Absatz 4 anstelle „Die Revision ist zulässig, sie ist im Sinn des Aufhebungsantrags auch berechtigt“ richtig „Die Revision ist zulässig, sie ist aber nicht berechtigt“ zu lauten hat.

**False Positives:**

- `Partei Berkenheger Analyse AG` — partial — gold is substring of pred: `Berkenheger Analyse AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Arabella Venczel`(person)
- `Dr. Stefan Gloyer`(person)
- `Berkenheger Analyse AG`(organisation)
- `Ebendorfer Hauptstraße 3, 8054 Graz, Österreich`(address)
- `Dr. Herbert Salficky`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Seetal Consulting GmbH, Diakoniestraße 19, 3251 Ameishaufen, Österreich, vertreten durch Aigner Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Rhein-Landwirtschaft AG, Starfach-Hohe Wand Weg 97, 3386 Würmling, Österreich, vertreten durch Dr. Josef Milchram, Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen 1.373.171,48 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 20. Jänner 2017, GZ 1 R 160/16d-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Rhein-Landwirtschaft AG` — partial — gold is substring of pred: `Rhein-Landwirtschaft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Seetal Consulting GmbH`(organisation)
- `Diakoniestraße 19, 3251 Ameishaufen, Österreich`(address)
- `Aigner Rechtsanwalts GmbH`(organisation)
- `Rhein-Landwirtschaft AG`(organisation)
- `Starfach-Hohe Wand Weg 97, 3386 Würmling, Österreich`(address)
- `Dr. Josef Milchram`(person)
- `Dr. Anton Ehm`(person)
- `Mag. Thomas Mödlagl`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/7Ob54_20x`) (sent_id: `deanon_260716_TRAIN/7Ob54_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Techn R Ramona Rössler, vertreten durch Mag. Astrid Roblyek, Rechtsanwältin in Klagenfurt am Wörthersee, gegen die beklagte Partei ZED Planung AG Haberditzlgasse 29, 9341 Kreuth, Österreich, vertreten durch Jarolim Partner Rechtsanwälte GmbH in Wien, wegen 7.339,70 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 31. Oktober 2019, GZ 4 R 325/19i-15, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 15. Juli 2019, GZ 15 C 998/18y-11, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei ZED Planung AG` — partial — gold is substring of pred: `ZED Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Techn R Ramona Rössler`(person)
- `Mag. Astrid Roblyek`(person)
- `ZED Planung AG`(organisation)
- `Haberditzlgasse 29, 9341 Kreuth, Österreich`(address)
- `Jarolim Partner Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/7Ob60_18a`) (sent_id: `deanon_260716_TRAIN/7Ob60_18a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Nadja Schlegermann, vertreten durch Dr. Josef Sailer, Rechtsanwalt in Bruck an der Leitha, gegen die beklagte Partei Felmerig Lebensmittel AG, Kleinmollsberg 18, 8213 Oberrettenbach, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2018, GZ 1 R 127/17d-15, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Felmerig Lebensmittel AG` — partial — gold is substring of pred: `Felmerig Lebensmittel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Nadja Schlegermann`(person)
- `Dr. Josef Sailer`(person)
- `Felmerig Lebensmittel AG`(organisation)
- `Kleinmollsberg 18, 8213 Oberrettenbach, Österreich`(address)
- `Mag. Wolfgang Weilguni`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. Roderich Florczyk, vertreten durch Dr. Norbert Nowak, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel-Energie AG, Gaunitzhof 8, 4632 Breitwies, Österreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen 6.342,73 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 8. November 2018, GZ 60 R 98/18v-12, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 15. Juni 2018, GZ 18 C 109/18p-8, abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Mittel-Energie AG` — partial — gold is substring of pred: `Mittel-Energie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Ing. Roderich Florczyk`(person)
- `Dr. Norbert Nowak`(person)
- `Mittel-Energie AG`(organisation)
- `Gaunitzhof 8, 4632 Breitwies, Österreich`(address)
- `Schönherr Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)
- `Bezirksgerichts für Handelssachen Wien`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/7Ob79_10h`) (sent_id: `deanon_260716_TRAIN/7Ob79_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Pascal Sitzman, vertreten durch Dr. Arnold Mayrhofer, Rechtsanwalt in Linz, gegen die beklagte Partei Achtermeier Handel AG, Stöbergasse 14, 3643 Loitzendorf, Österreich, vertreten durch Dr. Christian Ransmayr, Rechtsanwalt in Linz, wegen Feststellung, über die außerordentliche Revision des Klägers gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 8. März 2010, GZ 2 R 130/09i-82, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Achtermeier Handel AG` — partial — gold is substring of pred: `Achtermeier Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Huber`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schaumüller`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Dr. Roch`(person)
- `Pascal Sitzman`(person)
- `Dr. Arnold Mayrhofer`(person)
- `Achtermeier Handel AG`(organisation)
- `Stöbergasse 14, 3643 Loitzendorf, Österreich`(address)
- `Dr. Christian Ransmayr`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_4`)


Isabel Nestle AG, Reinsbach 186, 9131 Dolina, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2.

**False Positives:**

- `Isabel Nestle AG` — partial — gold is substring of pred: `Isabel Nestle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isabel Nestle`(person)
- `Reinsbach 186, 9131 Dolina, Österreich`(address)
- `Jank Weiler Operenyi Rechtsanwälte OG`(organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Karen Jansonius, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Schopf Automotive AG Grebien-Gasse 50, 4675 Dirisam, Österreich, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Schopf Automotive AG` — partial — gold is substring of pred: `Schopf Automotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Karen Jansonius`(person)
- `Dr. Herwig Ernst`(person)
- `Schopf Automotive AG`(organisation)
- `Grebien-Gasse 50, 4675 Dirisam, Österreich`(address)
- `Dr. Herbert Laimböck`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/7Ob94_20d`) (sent_id: `deanon_260716_TRAIN/7Ob94_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Juliana Mündelein, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ACBK Elektro Solutions AG, Schwarzenseer Straße 25, 9560 Steuerberg, Österreich, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei ACBK Elektro Solutions AG` — partial — gold is substring of pred: `ACBK Elektro Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Mag. Juliana Mündelein`(person)
- `Brand Rechtsanwälte GmbH`(organisation)
- `ACBK Elektro Solutions AG`(organisation)
- `Schwarzenseer Straße 25, 9560 Steuerberg, Österreich`(address)
- `Dorda Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/8Ob35_23i`) (sent_id: `deanon_260716_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Bergstreser&Svarc Pharma, und 2. Hoppstetter + Roloff Solar AG, L.-Forstner-Straße 4, 9341 Edling, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Edmund Wewerinck, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Roloff Solar AG` — partial — pred is substring of gold: `Hoppstetter + Roloff Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Dr. Thunhart`(person)
- `Bergstreser&Svarc Pharma`(organisation)
- `Hoppstetter + Roloff Solar AG`(organisation)
- `L.-Forstner-Straße 4, 9341 Edling, Österreich`(address)
- `Dr. Heinrich`(person)
- `DI Edmund Wewerinck`(person)
- `Dr. Andreas A. Lintl`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_12`)


Die OberSoftware AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die OberSoftware AG` — partial — gold is substring of pred: `OberSoftware AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OberSoftware AG`(organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/8ObA18_17f`) (sent_id: `deanon_260716_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei MedR Clemens Schepper, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei Muehleis & Klaese Technik AG, Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Klaese Technik AG` — partial — pred is substring of gold: `Muehleis & Klaese Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Bernhard Gruber`(person)
- `Harald Kohlruss`(person)
- `MedR Clemens Schepper`(person)
- `Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH`(organisation)
- `Muehleis & Klaese Technik AG`(organisation)
- `Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich`(address)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `Personenverkehr AG` — partial — pred is substring of gold: `ÖBB-Personenverkehr AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Monika Lanz`(person)
- `Wolfgang Cadilek`(person)
- `Hon.-Prof. Dieter Kovacs`(person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte`(organisation)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

**False Positives:**

- `Holding AG` — partial — pred is substring of gold: `ÖBB-Holding AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB`(organisation)
- `ÖBB-Holding AG`(organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/8ObA60_19k`) (sent_id: `deanon_260716_TRAIN/8ObA60_19k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michaela Puhm (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden und widerbeklagten Partei KzlR Titus Tielken, vertreten durch Mag. Martin Stärker, Rechtsanwalt in Wien, gegen die beklagte und widerklagende Partei Alwaldnex Bau AG, Ebereschenweg 13, 4616 Bergern, Österreich, vertreten durch Dr. Max Pichler, Rechtsanwalt in Wien, wegen 115.729,26 EUR brutto sA und Feststellung (Streitwert 21.455,46 EUR) (AZ 23 Cga 20/18f) und 3.421,39 EUR sA (AZ 23 Cga 73/18z), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 28. August 2019, GZ 8 Ra 12/19x-19, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Alwaldnex Bau AG` — partial — gold is substring of pred: `Alwaldnex Bau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Johannes Püller`(person)
- `Mag. Michaela Puhm`(person)
- `KzlR Titus Tielken`(person)
- `Mag. Martin Stärker`(person)
- `Alwaldnex Bau AG`(organisation)
- `Ebereschenweg 13, 4616 Bergern, Österreich`(address)
- `Dr. Max Pichler`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/8ObA69_19h`) (sent_id: `deanon_260716_TRAIN/8ObA69_19h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Hofrätin Dr. Tarmann-Prentner als Vorsitzende, die Hofrätin Mag. Korn und den Hofrat Dr. Stefula als weitere Richter sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Mag. Ingolf Marszalek, vertreten durch MMag. Dr. Susanne Binder-Novak, Rechtsanwältin in St. Pölten, gegen die beklagte Partei Tal Werklexlem AG, Waizbauerweg 12, 9651 Strajach, Österreich, vertreten durch Dr. Helmut Engelbrecht, Rechtsanwalt in Wien, wegen 14.426 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2019, GZ 7 Ra 79/19t-15, in nichtöffentlicher Sitzung Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 2 ASGG, § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Tal Werklexlem AG` — partial — gold is substring of pred: `Tal Werklexlem AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Mag. Thomas Stegmüller`(person)
- `Gerald Fida`(person)
- `Mag. Ingolf Marszalek`(person)
- `MMag. Dr. Susanne Binder-Novak`(person)
- `Tal Werklexlem AG`(organisation)
- `Waizbauerweg 12, 9651 Strajach, Österreich`(address)
- `Dr. Helmut Engelbrecht`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/8ObA71_14w`) (sent_id: `deanon_260716_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Cynthia Schamel, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Werkglanz-Verlag AG, Blattbühel 46, 9073 Klagenfurt, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Werkglanz-Verlag AG` — partial — gold is substring of pred: `Werkglanz-Verlag AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Mag. Andreas Mörk`(person)
- `Mag. Matthias Schachner`(person)
- `Cynthia Schamel`(person)
- `Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft`(organisation)
- `Werkglanz-Verlag AG`(organisation)
- `Blattbühel 46, 9073 Klagenfurt, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, Dr. Thunhart und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Lieselotte Mebesius, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Ahrenhold Druck AG, Brunnbichlweg 19, 3261 Figelsberg, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 22.140,32 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Juni 2019, GZ 2 R 92/19s-21, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Linz vom 12. April 2019, GZ 45 Cg 33/18v-17, nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch I. Das mit Beschluss vom 15. April 2020, AZ 9 Ob 61/19i, bis zur Entscheidung des Gerichtshofs der Europäischen Union über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Partei Ahrenhold Druck AG` — partial — gold is substring of pred: `Ahrenhold Druck AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Mag. Korn`(person)
- `Dr. Thunhart`(person)
- `MMag. Sloboda`(person)
- `Lieselotte Mebesius`(person)
- `Poduschka Partner Anwaltsgesellschaft mbH`(organisation)
- `Ahrenhold Druck AG`(organisation)
- `Brunnbichlweg 19, 3261 Figelsberg, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_123`)


In einer weiteren Entscheidung in Zusammenhang mit Abschalteinrichtungen, der Rechtssache C-100/21,QBgegenMercedes-Benz Group AG, beantwortet der EuGH die an ihn gestellten Vorlagefragen wie folgt: „1. Art 18 Abs 1, Art 26 Abs 1 und Art 46 der Richtlinie 2007/46/EG in Verbindung mit Art 5 Abs 2 VO 715/2007/EG sind dahin auszulegen, dass sie neben allgemeinen Rechtsgütern die Einzelinteressen des individuellen Käufers eines Kraftfahrzeugs gegenüber dessen Hersteller schützen, wenn dieses Fahrzeug mit einer unzulässigen Abschalteinrichtung im Sinne von Art 5 Abs 2 dieser Verordnung ausgestattet ist.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_125`)


In seiner Entscheidungsbegründung rekapituliert der EuGH zunächst, dass ein individueller Käufer, der ein Fahrzeug erwirbt, das zur Serie eines genehmigten Fahrzeugtyps gehört und somit mit einer Übereinstimmungsbescheinigung versehen ist, vernünftiger Weise erwarten kann, dass die VO 715/2007/EG und insbesondere deren Art 5 bei diesem Fahrzeug eingehalten werden (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 81 unter Hinweis auf C-145/20,Porsche Inter Auto und Volkswagen, Rn 54).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_127`)


[34] Konkret leitet der EuGH aus den Bestimmungen über die Übereinstimmungsbescheinigung (Art 18 Abs 1 und Art 26 Abs 1 der Rahmen-RL [RL 2007/46/EG des Europäischen Parlaments und des Rates vom 5. 9. 2007 zur Schaffung eines Rahmens für die Genehmigung von Kraftfahrzeugen und Kraftfahrzeuganhängern sowie von Systemen, Bauteilen und selbstständigen technischen Einheiten für diese Fahrzeuge; künftig: RL 2007/46/EG]) ab, dass die Übereinstimmungsbescheinigung „eine unmittelbare Verbindung zwischen dem Automobilhersteller und dem individuellen Käufer eines Kraftfahrzeugs herstellt, mit der diesem gewährleistet werden soll, dass das Fahrzeug mit den maßgeblichen Rechtsvorschriften der Union übereinstimmt“ (C-100/21,QBgegenMercedes-Benz Group AG, Rn 82).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_147`)


Für diesen Schadenersatzanspruch macht der EuGH grundsätzliche Vorgaben, nämlich in dem Sinn, dass die Mitgliedstaaten in einem solchen Fall einen Schadenersatzanspruch zu Gunsten eines Käufers gegenüber dem Hersteller vorzusehen haben, wenn dem Käufer durch diese Abschalteinrichtung ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_148`)


Dabei handelt es sich um einen im nationalen Recht wurzelnden Schadenersatzanspruch, der am unionsrechtlichen Effektivitätsgrundsatz zu messen ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 93), also eine wirksame, verhältnismäßige und abschreckende Sanktion für den Verstoß darstellen muss (vgl EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 90).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation
- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 66** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_149`)


Im Übrigen richten sich die Modalitäten dieses Schadenersatzanspruchs nach nationalem Recht (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 92), hier also unstrittig nach österreichischem Recht.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_151`)


Eine unionsrechtliche Vorgabe eines Schadenersatzanspruchs ist das Vorliegen eines Schadens: Der EuGH betont, dass dem Käufer eines mit einer unzulässigen Abschalteinrichtung ausgestatteten Fahrzeugs ein Schadenersatzanspruch zusteht, wenn ihm ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_153`)


Als nachteilige Folge – vor der ein Fahrzeugkäufer durch das Unionsrecht geschützt werden soll – sieht der EuGH an, dass durch die Unzulässigkeit der Abschalteinrichtung die Gültigkeit der EG-Typengenehmigung und daran anschließend die der Übereinstimmungsbescheinigung in Frage gestellt werden, was wiederum (unter anderem) zu einer Unsicherheit über die Nutzungsmöglichkeit (Anmeldung, Verkauf oder Inbetriebnahme des Fahrzeugs) und „letztlich“ zu einem Schaden führen kann (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_173`)


Ebenso wenig lässt die Feststellung erkennen, ob der Kläger die Notwendigkeit des Software-Updates und die vom EuGH angesprochene Unsicherheit über die Nutzungsmöglichkeit des Fahrzeugs (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84; vgl zu dieser Unsicherheit auch die mit der Entscheidung des EuGH vom 8.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_260716_TRAIN/9Ob6_24h`) (sent_id: `deanon_260716_TRAIN/9Ob6_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Stiefsohn in der Rechtssache der klagenden Partei Jennifer Franckh, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Fürstentum Liechtenstein, gegen die beklagte Partei DrauGarten AG, Wamprechtsham 54, 4926 Untereselbach, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 2.375 EUR und Feststellung (Streitwert: 4.000 EUR), über die Revision der beklagten Partei gegen das Zwischenurteil des Landesgerichts Wels als Berufungsgericht vom 25. Oktober 2023, GZ 22 R 198/23h-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Vöcklabruck vom 15. Juni 2023, GZ 13 C 630/22f-26, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I.Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei DrauGarten AG` — partial — gold is substring of pred: `DrauGarten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Hargassner`(person)
- `Mag. Korn`(person)
- `Dr. Stiefsohn`(person)
- `Jennifer Franckh`(person)
- `Dr. Alexander Amann LL.M.`(person)
- `DrauGarten AG`(organisation)
- `Wamprechtsham 54, 4926 Untereselbach, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Vöcklabruck`(organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/9ObA134_09k`) (sent_id: `deanon_260716_TRAIN/9ObA134_09k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Hradil und Dr. Hopf als weitere Richter in der Arbeitsrechtssache der klagenden Partei Frederike Geschwind, vertreten durch Dr. Andreas Lintl, Rechtsanwalt in Wien, gegen die beklagte Partei Sudbertri Garten AG, Mauerfeldstraße 26, 8753 Dietersdorf, Österreich, vertreten durch die Winkler Reich-Rohrwig Illedits Rechtsanwälte-Partnerschaft in Wien, wegen Kündigungsanfechtung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht in Arbeits- und Sozialrechtssachen vom 14. Oktober 2009, GZ 10 Ra 108/09i-17, womit der Beschluss des Landesgerichts Krems an der Donau als Arbeits- und Sozialgericht vom 13. August 2009, GZ 7 Cga 42/09b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs der klagenden Partei wird gemäß § 526 Abs 2 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Sudbertri Garten AG` — partial — gold is substring of pred: `Sudbertri Garten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Rohrer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hradil`(person)
- `Dr. Hopf`(person)
- `Frederike Geschwind`(person)
- `Dr. Andreas Lintl`(person)
- `Sudbertri Garten AG`(organisation)
- `Mauerfeldstraße 26, 8753 Dietersdorf, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/9ObA41_14s`) (sent_id: `deanon_260716_TRAIN/9ObA41_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Gerald Fuchs und Peter Schönhofer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Clarissa Bannwarth, vertreten durch Dr. Remo Sacherer, Rechtsanwalt in Wien, gegen die beklagte Partei Garten Bernexdorf AG, Sittestraße 49, 4203 Katzgraben, Österreich, vertreten durch Korn Rechtsanwälte OG in Wien, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Februar 2014, GZ 7 Ra 4/14f-29, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Garten Bernexdorf AG` — partial — gold is substring of pred: `Garten Bernexdorf AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Mag. Gerald Fuchs`(person)
- `Peter Schönhofer`(person)
- `Clarissa Bannwarth`(person)
- `Dr. Remo Sacherer`(person)
- `Garten Bernexdorf AG`(organisation)
- `Sittestraße 49, 4203 Katzgraben, Österreich`(address)
- `Korn Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/9ObA8_20x`) (sent_id: `deanon_260716_TRAIN/9ObA8_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Werner Pletzenauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Dr. Hartmut Sperber, vertreten durch Moser Mutz Rechtsanwälte GesbR in Klagenfurt am Wörthersee, gegen die beklagte Partei HASK Software Betriebe AG, Alter Garten 34, 8490 Hummersdorf, Österreich, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Klagenfurt am Wörthersee, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Dezember 2019, GZ 7 Ra 70/19x-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei HASK Software Betriebe AG` — partial — gold is substring of pred: `HASK Software Betriebe AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Dr. Ingomar Stupar`(person)
- `Mag. Werner`(person)
- `Mag. Dr. Hartmut Sperber`(person)
- `Moser Mutz Rechtsanwälte GesbR`(organisation)
- `HASK Software Betriebe AG`(organisation)
- `Alter Garten 34, 8490 Hummersdorf, Österreich`(address)
- `Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)

</details>

---

## `m.b.H. Entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ed74dfb7`  
**Description:**
Matches limited liability companies ending in m.b.H., often with 'Fa.' prefix.

**Content:**
```
(?<!\w)(?:auf\s+die\s+|von\s+der\s+|der\s+|Firma\s+|Fa\.)?([A-Z][a-zA-Z\s\-]+(?:m\.b\.H\.))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verwaltungsgerichtshof` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7b7ff6a0`  
**Description:**
Matches Verwaltungsgerichtshof and its genitive form Verwaltungsgerichtshofes, capturing only the name.

**Content:**
```
(?<!\w)(Verwaltungsgerichtshof(?:es)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzpolizei` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `56ef1e64`  
**Description:**
Matches Finanzpolizei, capturing only the name.

**Content:**
```
(?<!\w)(?:des\s+)?(Finanzpolizei)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FAÖ Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `22d21e30`  
**Description:**
Matches the abbreviation FAÖ (Finanzamt Österreich) in various contexts.

**Content:**
```
\bFA\u00d6\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Vorbrodt Sanitär` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4bdf9643`  
**Description:**
Matches 'Vorbrodt Sanitär'.

**Content:**
```
\bVorbrodt\s+Sanitär\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Snajdr E-Commerce GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4e32c7fb`  
**Description:**
Matches Snajdr E-Commerce GmbH with strict context anchors, excluding preceding articles.

**Content:**
```
(?<!\w)(?:Fa\.\s+)?Snajdr\s+E‑Commerce\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Glanzder-Automotive GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c834b863`  
**Description:**
Matches Glanzder-Automotive GmbH variants including 'Fa.' prefix, excluding preceding articles.

**Content:**
```
(?<!\w)(?:Fa\.\s+)?Glanzder-Automotive\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Jackobi und Horbank KI GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e4d2df6a`  
**Description:**
Matches Jackobi und Horbank KI GmbH with context anchors, excluding preceding articles.

**Content:**
```
(?<!\w)(?:Fa\.\s+)?Jackobi\s+und\s+Horbank\s+KI\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KAG Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e48833bc`  
**Description:**
Matches the abbreviation KAG in context.

**Content:**
```
\bKAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fa. GmbH Entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4fd3d809`  
**Description:**
Specifically matches company names starting with 'Fa.' to ensure the prefix is captured as part of the entity.

**Content:**
```
(?<!\w)(?:auf\s+die\s+|von\s+der\s+|der\s+|Firma\s+)?(Fa\.[A-Z][a-zA-Z\s\-]+(?:GmbH|G\.mbH|m\.b\.H\.))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ÖGK Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `84f357dc`  
**Description:**
Matches the abbreviation ÖGK (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KPMG Alpen-Treuhand GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `10cbae66`  
**Description:**
Matches KPMG Alpen-Treuhand GmbH variants.

**Content:**
```
(?<!\w)(?:Fa\.\s+)?KPMG\s+Alpen-Treuhand\s+GmbH\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht (BFG) Combined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `064c1891`  
**Description:**
Matches 'Bundesfinanzgericht' followed immediately by '(BFG)' as a single entity.

**Content:**
```
(?<!\w)(Bundesfinanzgericht(?:es)?\s*\(BFG\))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Pensionsversicherungsanstalt` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ba58da3f`  
**Description:**
Matches 'Pensionsversicherungsanstalt' and its variant with '/PVA' suffix, allowing for leading punctuation.

**Content:**
```
(?<!\w)(\.?Pensionsversicherungsanstalt(?:/PVA)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 3500 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Gabriele Griehsel`(person)
- `Dr. Wolfgang Kozak`(person)
- `Roland Soukup`(person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

</details>

---

## `Universität Wien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b691e0ce`  
**Description:**
Matches 'Universität Wien' as an organisation.

**Content:**
```
(?<!\w)(Universität\s+Wien)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BMI Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9f5cf45c`  
**Description:**
Matches the abbreviation BMI (Bundesministerium für Inneres) in various contexts.

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht Genitive` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `310f7e93`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive forms, allowing standard punctuation (commas, periods) and prepositions, but excluding compound location suffixes like 'Außenstelle'.

**Content:**
```
(?<!\w)(Bundesfinanzgericht(?:es|s)?)(?!\w|\s+(?:Außenstelle|Zweigstelle|Standort))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Derdonal-Garten AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e0e7dd99`  
**Description:**
Specifically matches Derdonal-Garten AG to ensure full capture.

**Content:**
```
(?<!\w)(Derdonal-Garten\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Energie Verdorfwald GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9691babe`  
**Description:**
Matches Energie Verdorfwald GmbH specifically.

**Content:**
```
(?<!\w)(Energie\s+Verdorfwald\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schlaich Bau KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bf750965`  
**Description:**
Matches Schlaich Bau KG specifically.

**Content:**
```
(?<!\w)(Schlaich\s+Bau\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `St. Johann Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `02360847`  
**Description:**
Matches St. Johann Steuerberatung GmbH specifically.

**Content:**
```
(?<!\w)(St\.\s+Johann\s+Steuerberatung\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `APP Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `018a4fe0`  
**Description:**
Matches APP Steuerberatung GmbH specifically.

**Content:**
```
(?<!\w)(APP\s+Steuerberatung\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gerichtshof der Europäischen Union` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `433e64b3`  
**Description:**
Matches Gerichtshof der Europäischen Union.

**Content:**
```
(?<!\w)(Gerichtshof\s+der\s+Europäischen\s+Union)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 2438 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_51`)


Auch der Gerichtshof der Europäischen Union wies in diesem Zusammenhang darauf hin, dass der Kausalzusammenhang zwischen dem vom Geschädigten geltend gemachten Schaden und dem (unionsrechtlichen) Vergaberechtsverstoß eine Voraussetzung des Ersatzanspruchs ist (vgl EuGH C-568/08,Combinatie Sijker Infrabouwua, Rn 87;

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_23`)


Das Landgericht Ravensburg (Deutschland) hat dem Gerichtshof der Europäischen Union am 9.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_158`)


Was die gerichtliche Nachprüfbarkeit der Einhaltung dieser Voraussetzungen betrifft, billigt der Gerichtshof der Europäischen Union dem Unionsrechtsgesetzgeber im Rahmen der Ausübung der ihm übertragenen Zuständigkeiten ein weites Ermessen in Bereichen zu, in denen seine Tätigkeit sowohl politische als auch wirtschaftliche oder soziale Entscheidungen verlangt und in denen er komplexe Prüfungen und Beurteilungen vornehmen muss.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_5`)


Der Antrag der Revisionswerberin, der Oberste Gerichtshof möge ein Vorabentscheidungsersuchen an den Gerichtshof der Europäischen Union stellen, wird zurückgewiesen.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Monika Lanz`(person)
- `Wolfgang Cadilek`(person)
- `Hon.-Prof. Dieter Kovacs`(person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte`(organisation)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_133`)


Der Oberste Gerichtshof hat beschlossen, ein Vorabentscheidungsersuchen an den Gerichtshof der Europäischen Union zu stellen.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_141`)


Der Oberste Gerichtshof würde es begrüßen, wenn der Gerichtshof der Europäischen Union über das vorliegende Vorabentscheidungsersuchen und über die Vorlage des Oberlandesgerichts Innsbruck gemeinsam entscheiden würde.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_148`)


3. 2020 legte der Oberste Gerichtshof zu 10 Ob 44/19x dem Gerichtshof der Europäischen Union gemäß Art 267 AEUV folgende Fragen zur Vorabentscheidung vor: 2.1.„1.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

</details>

---

## `Landesgericht Standalone` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c4b03ff7`  
**Description:**
Matches 'Landesgericht' when not followed by a specific location name, as standalone references are common in legal texts.

**Content:**
```
(?<!\w)(Landesgericht)(?!\s+[A-Z][a-z]+)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 3208 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_22`)


1./ Gemäß § 357 Abs 2 erster Satz StPO hat das Landesgericht den Antrag auf Wiederaufnahme des Strafverfahrens dem Gegner des Antragstellers mit der Belehrung zuzustellen, dass er seine Gegenäußerung binnen 14 Tagen überreichen könne.

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__23`)


Seither besteht das Landesgericht als Schöffengericht aus nur einem (Berufs-)Richter und zwei Schöffen (§ 32 Abs 1 dritter Satz StPO).

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_7`)


Die gegen diesen Ausspruch gerichtete Berufung des Privatbeteiligten (ON 23) wies das Oberlandesgericht Graz mit dem nunmehr angefochtenen Beschluss im Wesentlichen mit der Begründung zurück, auch im Verfahren vor dem Landesgericht als Einzelrichter stehe dem Privatbeteiligten die Berufung nur bei vollständiger Verweisung mit seinen Ansprüchen auf den Zivilrechtsweg (trotz Verurteilung) offen, während die Höhe des Zuspruchs nicht bekämpfbar sei (vgl zum kollegialgerichtlichen Verfahren § 283 Abs 4 iVm § 366 Abs 3 StPO).

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgericht Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Graz`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_11`)


Diese Regelung findet zufolge § 489 Abs 1 StPO auch im Verfahren vor dem Landesgericht als Einzelrichter Anwendung.

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_11`)


Rechtliche Beurteilung Das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, steht - wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt - in seinem Punkt A./2./ mit dem Gesetz nicht im Einklang: Gemäß der auch für das Verfahren vor dem Landesgericht als Einzelrichter geltenden (§ 488 Abs 1 StPO) Bestimmung des § 270 Abs 4 StPO hat eine - unter den in dieser Vorschrift genannten, hier vorliegenden Voraussetzungen zulässigerweise - gekürzte Urteilsaus- fertigung die in § 270 Abs 2 StPO angeführten Angaben mit Ausnahme der Entscheidungsgründe, also auch die in § 260 StPO (§ 270 Abs 4 Z 1 StPO) genannten Punkte zu enthalten.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgerichts Korneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Korneuburg`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_4`)


Im Verfahren AZ 7 U 49/08s des Bezirksgerichts Innsbruck verletzt der Vorgang, dass es das Gericht unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Garthoff im Verfahren AZ 23 BE 29/06a des Landesgerichts Innsbruck gemäß § 46 Abs 2 StGB gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich dieses Landesgericht als Vollzugsgericht zu verständigen, § 494a Abs 7 StPO.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innsbruck`(organisation)
- `Andreas Garthoff`(person)
- `Landesgerichts Innsbruck`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_10`)


Da dieser Tatbestand einer notwendigen und der Parteiendisposition entzogenen (1 Nc 24/09h) Delegierung im vorliegenden Fall erfüllt ist, ist ein Landesgericht außerhalb des Sprengels des Oberlandesgerichts Wien als zuständig zu bestimmen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)

</details>

---

## `Nieder Unisyn Manufaktur GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e26b229b`  
**Description:**
Matches the specific entity 'Nieder Unisyn Manufaktur GmbH'.

**Content:**
```
(?<!\w)(Nieder\s+Unisyn\s+Manufaktur\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schniederjahn Software KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6251a465`  
**Description:**
Matches the specific entity 'Schniederjahn Software KG'.

**Content:**
```
(?<!\w)(Schniederjahn\s+Software\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Unverdroß Planung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `16d6cb4f`  
**Description:**
Matches the specific entity 'Unverdroß Planung GmbH'.

**Content:**
```
(?<!\w)(Unverdroß\s+Planung\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg-Stadt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d3d0f7ef`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt' specifically.

**Content:**
```
(?<!\w)(Finanzamt\s+Salzburg-Stadt)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesamt für Soziales und Behindertenwesen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d6163a2a`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its genitive form 'Bundesamtes für Soziales und Behindertenwesen', including the '/BSB' suffix variant.

**Content:**
```
(?<!\w)(Bundesamt(?:es)?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen(?:/BSB)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verwaltungsgericht Wien` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d153afbb`  
**Description:**
Matches 'Verwaltungsgericht Wien' and its genitive form 'Verwaltungsgericht Wien' (no 's' in genitive for this specific compound in this context, or just the name).

**Content:**
```
(?<!\w)(Verwaltungsgericht\s+Wien)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 2440 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_13`)


Da keines der Angebote – also auch nicht jenes der Klägerin – den Anforderungen der Ausschreibung entsprach, widerrief die Beklagte die Ausschreibung, was von der Klägerin vor dem Verwaltungsgericht Wien erfolglos bekämpft wurde.

**False Positives:**

- `Verwaltungsgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_16`)


Das von ihr (neuerlich) angerufene Verwaltungsgericht Wien stellte (in zwei Verfahren, die jeweils unterschiedliche Zeiträume betrafen) rechtskräftig fest, dass diese Vorgehensweise rechtswidrig war.

**False Positives:**

- `Verwaltungsgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `COFAG Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `823fff02`  
**Description:**
Matches the abbreviation COFAG as an organisation entity, but excludes cases where it is part of a compound word (e.g., COFAG-NoAG).

**Content:**
```
(?<!\w)(COFAG)(?![-\w])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BHAG Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1225c510`  
**Description:**
Matches the abbreviation BHAG (Bundesheer- und Heeresabgaben) in various contexts.

**Content:**
```
\bBHAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `technoRent International GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `06953d99`  
**Description:**
Matches the specific entity 'technoRent International GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(technoRent\s+International\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Südb Consynkel KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b7b1078a`  
**Description:**
Matches the specific entity 'Südb Consynkel KG'.

**Content:**
```
(?<!\w)(Südb\s+Consynkel\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Glatzhofer & Matschek mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f708af96`  
**Description:**
Matches the specific entity 'Glatzhofer & Matschek Steuerberatungsgesellschaft mbH'.

**Content:**
```
(?<!\w)(Glatzhofer\s+&\s+Matschek\s+Steuerberatungsgesellschaft\s+mbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag. Manfred Reumiller GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66d69f81`  
**Description:**
Matches the specific entity 'Mag. Manfred Reumiller, Wirtschaftsprüfung und Steuerberatung GmbH & Co KG'.

**Content:**
```
(?<!\w)(Mag\.\s+Manfred\s+Reumiller,\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s*&\s*Co\.\s*KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verwaltungsgerichtshof Genitive` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1fe8a541`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive form 'Verwaltungsgerichtshofs', capturing the full name.

**Content:**
```
(?<!\w)(Verwaltungsgerichtshof(?:es|s)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 2452 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_20`)


Ob die offene „Zeitungsröhre“ als solche überhaupt eine Abgabeeinrichtung iSd § 17 Abs 2 ZustG sein kann (der Verwaltungsgerichtshof verneinte eine solche Eigenschaft etwa bei einem frei zugänglichen „Holzverschlag“; vgl 2011/05/0076), muss nach dem Vorgesagten nicht geprüft werden.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/4Ob23_24x`) (sent_id: `deanon_260716_TRAIN/4Ob23_24x_30`)


Der Verwaltungsgerichtshof definiert „Handel“ als eine auf den Warenaustausch zwischen den einzelnen Wirtschaftsgliedern gerichtete gewerbsmäßige Tätigkeit (83/04/0257;

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/8Ob101_14g`) (sent_id: `deanon_260716_TRAIN/8Ob101_14g_12`)


Hinsichtlich der vom Klagebegehren betroffenen Liegenschaften hat nicht nur die Agrarbehörde über diese Frage bereits entschieden, sondern liegt auch ein letztinstanzliches Erkenntnis des Verwaltungsgerichtshofs vor (VwGH 15.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VwGH`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_163`)


3.2Der österreichische Verwaltungsgerichtshof lässt die Einführung eines neuen Anrechnungs- und Vorrückungssystems nicht genügen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_169`)


Der Verwaltungsgerichtshof gab der Beschwerde des Lehrers statt und sprach aus, dass dem Beschwerdeführer ein Gehalt in der höheren Gehaltsstufe gebühre.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_170`)


Der Verwaltungsgerichtshof korrigierte somit nur den Vorrückungsstichtag nach den zugrunde liegenden neuen Dienstvorschriften, ohne auch den verlängerten Vorrückungszeitraum, der ebenfalls mit den neuen Dienstvorschriften normiert worden war, zu berücksichtigen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_171`)


In seiner Begründung führte der Verwaltungsgerichtshof unter anderem aus, dass weiterhin eine unzulässige Ungleichbehandlung von Zeiten vor bzw nach Vollendung des 18.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_176`)


3.3Aus Anlass dieser Entscheidung des Verwaltungsgerichtshofs hat der Gesetzgeber mit BGBl I 2012/120 eine neue Bestimmung in § 7a des Gehaltsgesetzes 1956 eingefügt, in der auf die Umsetzung der Richtlinie 2000/78/EG Bezug genommen wird.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_180`)


3.4Die Beurteilung des Verwaltungsgerichtshofs ist zumindest nicht zwingend.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_185`)


Der Verwaltungsgerichtshof inkriminiert anscheinend das Ergebnis der gesetzlichen Neuregelung, nach dem sich die Neuermittlung des Vorrückungsstichtags aufgrund der gleichzeitigen Verlängerung des Vorrückungszeitraums nicht auf denEntgeltanspruchdes Beschwerdeführers ausgewirkt hat.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_37`)


3.Eine nähere Auseinandersetzung mit der Frage findet sich auch in der Rechtsprechung des Verwaltungsgerichtshofs.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzamt Steiermark Mitte` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `110ed7aa`  
**Description:**
Matches 'Finanzamt Steiermark Mitte' specifically.

**Content:**
```
(?<!\w)(Finanzamt\s+Steiermark\s+Mitte)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Feldkirch` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `36e74c5d`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Feldkirch'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Feldkirch)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BM für Finanzen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `67788719`  
**Description:**
Matches 'BM für Finanzen' or 'Bundesministeriums für Finanzen' as an organisation.

**Content:**
```
(?<!\w)(Bundesministerium(?:s)?\s+f\u00fcr\s+Finanzen|BM\s+f\u00fcr\s+Finanzen)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Süd Consynkel KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6d28d4fe`  
**Description:**
Matches the specific entity 'Süd Consynkel KG'.

**Content:**
```
(?<!\w)(Süd\s+Consynkel\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinhard Stulik Steuerberatungs GmbH & Co OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `54ba6d5c`  
**Description:**
Matches the specific entity 'Reinhard Stulik Steuerberatungs GmbH & Co OG' including double spaces if present.

**Content:**
```
(?<!\w)(Reinhard\s+Stulik\s+Steuerberatungs\s+GmbH\s*&\s*Co\s+OG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministers für Arbeit, Soziales und Konsumentenschutz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bd020285`  
**Description:**
Matches the full ministry name 'Bundesministers für Arbeit, Soziales und Konsumentenschutz' and its nominative form.

**Content:**
```
(?<!\w)(Bundesministers?\s+f\u00fcr\s+Arbeit,?\s+Soziales\s+und\s+Konsumentenschutz)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SK Telecom` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `974b3bdf`  
**Description:**
Matches 'SK Telecom' and 'SK Telecom Co. Ltd' as an organisation.

**Content:**
```
(?<!\w)(SK\s+Telecom(?:\s+Co\.\s+Ltd)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BDO Assurance` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d14e62dc`  
**Description:**
Matches 'BDO Assurance GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft' as an organisation.

**Content:**
```
(?<!\w)(BDO\s+Assurance\s+GmbH\s+Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wald Zorwaldmon KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `85238484`  
**Description:**
Matches the specific entity 'Wald Zorwaldmon KG' to ensure full capture.

**Content:**
```
(?<!\w)(Wald\s+Zorwaldmon\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Alpen-KI GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c93567dd`  
**Description:**
Matches the specific entity 'Alpen-KI GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(Alpen-KI\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Amtes für Betrugsbekämpfung` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fdd690e3`  
**Description:**
Matches 'Amtes für Betrugsbekämpfung' as an organisation.

**Content:**
```
(?<!\w)(Amtes\s+für\s+Betrugsbekämpfung)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Zollamt` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ecb879a4`  
**Description:**
Matches 'Zollamt' as a standalone organization entity, handling genitive forms and various contexts.

**Content:**
```
(?<!\w)(Zollamt(?:es)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 2796 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_11`)


Nach den Sachverhaltsannahmen des Beschwerdegerichts ist Johann Rothmaler dringend verdächtig, in Am Spitalfeld 2, 9462 St. Peter im Lavanttal, Österreich und anderen Orten I. vorschriftswidrig Suchtgift 1. in einer das 25fache der Grenzmenge (§ 28b SMG) übersteigenden Menge anderen überlassen zu haben, indem er seit 2018 bis Mitte Dezember 2019 an Alexander Schuhardt wöchentlich zumindest ein Kilogramm „Speed“, enthaltend Amphetamin mit einem Reinheitsgehalt von zumindest 70 % weitergab, 2. aus dem Ausland aus- und nach Österreich eingeführt bzw dies versucht zu haben, indem er unbekannte Täter im „Darknet“ dazu bestimmte, 21,57 Gramm [richtig: 25,65 Gramm] Reinsubstanz MDMA sowie 200 Gramm „Speed-Paste“, enthaltend 74 % reines Amphetamin, auf dem Postweg an seine Wohnadresse zu versenden, wobei die zuerst genannte Sendung beim Zollamt Frankfurt/Deutschland sichergestellt wurde, II. am 14. Dezember 2019 im bewussten und gewollten Zusammenwirken mit Alexander Schlossmann Roberto Hampisch 1.

**False Positives:**

- `Zollamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Johann Rothmaler`(person)
- `Am Spitalfeld 2, 9462 St. Peter im Lavanttal, Österreich`(address)
- `Alexander Schuhardt`(person)
- `Alexander Schlossmann`(person)
- `Roberto Hampisch`(person)

</details>

---

## `XY GmbH & Co KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `01b44077`  
**Description:**
Matches the specific entity 'XY- GmbH & Co KG' to ensure full capture.

**Content:**
```
(?<!\w)(XY\-\s*GmbH\s*&\s*Co\.\s*KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFG Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `72c489ec`  
**Description:**
Matches the abbreviation BFG (Bundesfinanzgericht) in various contexts, ensuring it captures the acronym even when followed by prepositions like 'an die' or 'bei', preventing over-capture by GmbH rules.

**Content:**
```
(?<!\w)(?<!-)BFG(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Amt für Betrugsbekämpfung` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b3e76bd8`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' as an organisation. Fixed output template to use $0 for full match.

**Content:**
```
(?<!\w)(Amt\s+f\u00fcr\s+Betrugsbek\u00e4mpfung)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FB + KG Entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3134d83d`  
**Description:**
Matches company names with '+' in the name followed by KG, e.g., 'FB + KG'.

**Content:**
```
(?<![a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])([A-Z][A-Z\s+]+\s+KG)(?![a-zA-Z0-9])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FB + KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `960bf96f`  
**Description:**
Matches the specific abbreviation 'FB + KG' as an organisation.

**Content:**
```
(?<!\w)(FB\s*\+\s*KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frontex` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b28f4fd8`  
**Description:**
Matches the organization 'Frontex' (European Border and Coast Guard Agency).

**Content:**
```
\bFrontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Oststeiermark` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c188b760`  
**Description:**
Matches 'Finanzamt Oststeiermark' and its genitive form 'Finanzamtes Oststeiermark'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Oststeiermark)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hallas & Partner GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e8942a33`  
**Description:**
Specifically matches the full entity 'Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG' to ensure complete capture.

**Content:**
```
(?<!\w)(Hallas\s+&\s+Partner\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s*&\s*Co\s*KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrats der Stadt Wien with Dept` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b83bcdf9`  
**Description:**
Matches 'Magistrat' or 'Magistrats' with 'der Stadt Wien' as a standalone entity, explicitly stopping before department info (including 'MA' abbreviations) to avoid over-matching.

**Content:**
```
(?<!\w)(Magistrat(?:es)?\s+der\s+Stadt\s+Wien)(?!\s*,\s*Magistratsabteilung|\s+MA\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schabetsberger & Partner GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7f94d153`  
**Description:**
Specifically matches the full entity 'Schabetsberger & Partner Steuerberatung und Unternehmensberatung GmbH' to ensure complete capture.

**Content:**
```
(?<!\w)(Schabetsberger\s+&\s+Partner\s+Steuerberatung\s+und\s+Unternehmensberatung\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schaar Wirtschaftstreuhand OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `22cdb255`  
**Description:**
Specifically matches 'Schaar Wirtschaftstreuhand-, Steuerberatungs OG' variants.

**Content:**
```
(?<!\w)(Schaar\s+Wirtschaftstreuhand-?,\s+Steuerberatungs\s+OG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Süd Ostfen Institut AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `34ea9066`  
**Description:**
Specifically matches 'Süd Ostfen Institut AG' to ensure full capture.

**Content:**
```
(?<!\w)(Süd\s+Ostfen\s+Institut\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kailuhn KI AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `946eb39c`  
**Description:**
Specifically matches 'Kailuhn KI AG' to ensure full capture.

**Content:**
```
(?<!\w)(Kailuhn\s+KI\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Zollamt with Location` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d8449959`  
**Description:**
Matches 'Zollamt' or 'Zollamtes' followed by a specific known location name (e.g., 'Zollamt Linz', 'Zollamtes Klagenfurt'). This rule is tightened to only match known locations to prevent false positives from random capitalized words.

**Content:**
```
(?<!\w)(Zollamt(?:es)?)(?:\s+(?:Linz|Wels|Klagenfurt|Salzburg|Innsbruck|Graz|Villach|Bregenz|Eisenstadt|St\.\s*Pölten|Dornbirn|Leoben|Lienz|Amstetten|Baden|Braunau|Eferding|Feldkirchen|Gmunden|Hall|Horn|Kufstein|Lustenau|Neuhaus|Oberwart|Perg|Ried|Schwaz|Steyr|Telfs|Waidhofen|Wien|Wolfsberg|Zell|Zwettl|Lilienfeld|Hollabrunn|Schwechat|Tirol|Gmunden|Spittal|Grieskirchen|Steiermark|Österreich|Klagenfurt\s+St\.\s*Veit\s+Wolfsberg))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Linien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `986eb41c`  
**Description:**
Matches the specific organization 'Wiener Linien'.

**Content:**
```
(?<!\w)(Wiener\s+Linien)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Gemeindebezirk` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fdd6f4b5`  
**Description:**
Matches 'Wiener Gemeindebezirk' as an organisation.

**Content:**
```
(?<!\w)(Wiener\s+Gemeindebezirk)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `APK Pensionskasse AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c5908d00`  
**Description:**
Matches 'APK Pensionskasse AG' and 'APK-Pensionsersicherungs AG' specifically to prevent the generic GmbH rule from capturing only the suffix.

**Content:**
```
(?<!\w)(AP(?:K(?:\-Pensionsersicherungs| Pensionskasse)|S\-Pensionskasse) AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deutschen Rentenversicherung Bund` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4171af37`  
**Description:**
Matches the specific organization 'Deutschen Rentenversicherung Bund' in various cases (nominative, genitive, dative).

**Content:**
```
(?<!\w)(Deutschen\sRentenversicherung\sBund|Deutsche\sRentenversicherung\sBund|Rentenversicherung\sBund)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WGKK Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e5d1b4d`  
**Description:**
Matches the specific acronym WGKK (Wiener Gebietskrankenkasse) as an organisation.

**Content:**
```
(?<!\w)(WGKK)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministerium für Inneres` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `159939f2`  
**Description:**
Matches the specific ministry name 'Bundesministerium für Inneres' and its genitive form, excluding cases where it is immediately followed by '(BMI)'.

**Content:**
```
(?<!\w)(Bundesministerium(?:s)?\s+f\u00fcr\s+Inneres)(?!\s*\(BMI\))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 2814 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_11`)


Diese Kriterien verfehlt der eine unrechtmäßige Bereicherung verneinende Rechtsmittelwerber, indem er die erstgerichtlichen Feststellungen, wonach die Rückerstattung eines Bekleidungsbetrags nur dann vorgesehen war, wenn vom Polizeibeamten eine „vergleichbare“ zivile Regenjacke für seine dienstlichen Aufgaben gekauft wurde (US 7, 14 f), übergeht und den diesbezüglichen Erlass des Bundesministeriums für Inneres eigenständig dahin interpretiert, jeder Beamte hätte einen Rechtsanspruch auf den Bekleidungsbetrag als Gehaltsbestandteil für erhöhten Kleidungsaufwand.

**False Positives:**

- `Bundesministeriums für Inneres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_13`)


Mit der Hypothese, der Erlass des Bundesministeriums für Inneres könne „die aus dem Eigentumsrecht erfließenden Rechte nicht aufheben, sodass es jedem in den Genuss des Bekleidungskostenzuschusses kommenden Beamten freistehen muss, über seine Jacke nach Belieben zu disponieren“, bestreitet der Beschwerdeführer eine Schädigung im Vermögen der Republik Österreich.

**False Positives:**

- `Bundesministeriums für Inneres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Mur Steinstein` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `95b1affd`  
**Description:**
Matches 'Mur Steinstein' specifically as a person/entity, ensuring it is not captured by the GmbH rule or treated as a company.

**Content:**
```
(?<!\w)(Mur\s+Steinstein)(?!\s+GmbH)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wirtschaftsuniversität Wien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e214ad86`  
**Description:**
Matches the specific organization 'Wirtschaftsuniversität Wien'.

**Content:**
```
(?<!\w)Wirtschaftsuniversität\s+Wien(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt für Gebühren` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `344fd92c`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'für Gebühren', 'Verkehrsteuern' or 'Glücksspiel'. Only matches if the full functional description is present.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+f\u00fcr\s+Geb\u00fchren(?:\s+und\s+Verkehrsteuern\s+und\s+Gl\u00fccksspiel)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landespolizeidirektion State` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `db0e697e`  
**Description:**
Matches 'Landespolizeidirektion' followed by a state name ONLY if immediately adjacent (no space) or part of a known compound. If separated by space, it should not be captured here (handled by standalone rule).

**Content:**
```
(?<!\w)(Landespolizeidirektion(?:Wien|Burgenland|K\u00e4rnten|Nieder\u00f6sterreich|Ober\u00f6sterreich|Salzburg|Steiermark|Tirol|Vorarlberg))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzstrafsenat` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b82273a6`  
**Description:**
Matches 'Finanzstrafsenat' followed by location, stopping before 'des' or other prepositions. Does not capture the following genitive phrase.

**Content:**
```
(?<!\w)(Finanzstrafsenat\s+[A-Z][a-zA-Z\s/\d]+)(?!\s+des\s+|\s+[a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landespolizeidirektion Wien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `10f1886e`  
**Description:**
Matches 'Landespolizeidirektion Wien' as a specific organisation entity.

**Content:**
```
(?<!\w)(Landespolizeidirektion\s+Wien)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UniCredit Bank Austria AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e119da8`  
**Description:**
Matches 'UniCredit Bank Austria AG' as a specific organisation entity.

**Content:**
```
(?<!\w)(UniCredit\s+Bank\s+Austria\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reiffenstuel Pflege GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `282d31e1`  
**Description:**
Matches 'Reiffenstuel Pflege GmbH' specifically to ensure full capture.

**Content:**
```
(?<!\w)(Reiffenstuel\s+Pflege\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Garantie - Wirtschaftstreuhand- gesellschaft m.b.H.` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `707e2aa3`  
**Description:**
Matches 'Garantie - Wirtschaftstreuhand- gesellschaft m.b.H.' specifically.

**Content:**
```
(?<!\w)(Garantie\s+-\s+Wirtschaftstreuhand-\s+gesellschaft\s+m\.b\.H\.)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Djuric & Oberger Wth OG Steuerberatungsgesellschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `953a4b5d`  
**Description:**
Matches 'Djuric & Oberger Wth OG Steuerberatungsgesellschaft' specifically.

**Content:**
```
(?<!\w)(Djuric\s+&\s+Oberger\s+Wth\s+OG\s+Steuerberatungsgesellschaft)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `G & W Steuerberatungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `54153fec`  
**Description:**
Matches 'G & W Steuerberatungs GmbH' specifically.

**Content:**
```
(?<!\w)(G\s+&\s+W\s+Steuerberatungs\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien 9/18/19 Klosterneuburg` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1cab0da5`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Wien 9/18/19 Klosterneuburg' specifically to prevent truncation.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Wien\s+9/18/19\s+Klosterneuburg)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Baden Mödling` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a4b9d4c2`  
**Description:**
Matches 'Finanzamtes Baden Mödling' specifically.

**Content:**
```
(?<!\w)(Finanzamtes\s+Baden\s+Mödling)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Wien 4/5/10` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `676c1192`  
**Description:**
Matches 'Finanzamtes Wien 4/5/10' specifically.

**Content:**
```
(?<!\w)(Finanzamtes\s+Wien\s+4/5/10)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Österreich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d5bb90a7`  
**Description:**
Matches 'Finanzamtes Österreich' and 'Finanzamts Österreich' specifically.

**Content:**
```
(?<!\w)(Finanzamtes\s+\u00d6sterreich(?:s)?|Finanzamts\s+\u00d6sterreich)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lexlog Automotive GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `32d75bae`  
**Description:**
Matches 'Lexlog Automotive GmbH' specifically.

**Content:**
```
(?<!\w)(Lexlog\s+Automotive\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Textil Berdon KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f2cfe989`  
**Description:**
Matches 'Textil Berdon KG' specifically.

**Content:**
```
(?<!\w)(Textil\s+Berdon\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BKS Steuerberatungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `901aeca2`  
**Description:**
Matches 'BKS Steuerberatungs GmbH' specifically.

**Content:**
```
(?<!\w)(BKS\s+Steuerberatungs\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verlag Derkel GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2b5f81d4`  
**Description:**
Specifically matches 'Verlag Derkel GmbH' to ensure it is captured even when preceded by articles or context that the generic rule might miss or over-capture.

**Content:**
```
(?<!\w)(Verlag\s+Derkel\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `kaubek & partner GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `96e1683b`  
**Description:**
Matches the specific entity 'kaubek & partner Wirtschaftstreuhand Steuerberatungs- gesellschaft' variants.

**Content:**
```
(?<!\w)(?:kaubek\s+&\s+partner\s+Wirtschaftstreuhand\s+Steuerberatungs\-\s+gesellschaft)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Central Liaison Office` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `78136e56`  
**Description:**
Matches 'Central Liaison Office' and its variations as an organisation entity.

**Content:**
```
(?<!\w)(Central\s+Liaison\s+Office)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Europäische Gerichtshof` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e41fea20`  
**Description:**
Matches 'Europäische Gerichtshof' and its genitive form 'Europäischen Gerichtshofes' as an organisation.

**Content:**
```
(?<!\w)(Europ\u00e4ische\s+Gerichtshof(?:es)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 275 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_151`)


3. Ist Art 3 Abs 6 der Richtlinie 1999/44/EG dahin auszulegen, dass eine Vertragswidrigkeit, die in der Ausstattung eines Fahrzeugs mit einer nach Art 3 Z 10 in Verbindung mit Art 5 Abs 2 VO (EG) 715/2007 unzulässigen Abschalteinrichtung liegt, dann als geringfügig im Sinn der genannten Bestimmung zu qualifizieren ist, wenn der Übernehmer das Fahrzeug in Kenntnis ihres Vorhandenseins und ihrer Wirkungsweise dennoch erworben hätte?“ [24]2.2.Mit Urteil vom 14. 7. 2022, C-145/20,Porsche Inter Auto und Volkswagen, hat der Europäische Gerichtshof die ihm gestellten Fragen wie folgt beantwortet: „1.Art. 2 Abs. 2 Buchst.

**False Positives:**

- `Europäische Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_214`)


I.C.3.7.Der Europäische Gerichtshof hat darüber hinaus klargestellt, dass – ungeachtet des Vorliegens der in Art 5 Abs 2 Satz 2 lit a VO 715/2007/EU normierten Voraussetzungen – eine Abschalteinrichtung, die unter normalen Betriebsbedingungen den überwiegenden Teil des Jahres funktionieren müsste, damit der Motor vor Beschädigung oder Unfall geschützt und der sichere Betrieb des Fahrzeugs gewährleistet ist, nicht unter die Verbotsausnahme des Art 5 Abs 2 Satz 2 lit a VO 715/2007/EU fällt (Urteile C-145/20, Porsche Inter Auto und Volkswagen, Rn 73, 81;

**False Positives:**

- `Europäische Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Fa. GmbH Entities (No Space)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3376eac0`  
**Description:**
Matches company names preceded by 'Fa.' (e.g., 'Fa.Brocke Robotik GmbH') where there is no space between 'Fa.' and the name, capturing the full entity including the prefix. Updated to handle cases where 'Fa.' is immediately followed by the name without space.

**Content:**
```
(?<!\w)Fa\.([A-Z][a-zA-Z\-\.]+(?:\s+[A-Z][a-zA-Z\-\.]+)*(?:\s+&\s*[A-Z][a-zA-Z\-\.]+)*(?:\s+und\s+[A-Z][a-zA-Z\-\.]+)*\s+(?:GmbH|m\.b\.H\.?|AG|KG|GmbH\s*&\s*Co\s*KG|OG|Steuerberatungsgesellschaft\s*mbH|Wirtschaftsprüfungsgesellschaft\s*mbH|Wirtschaftstreuhandgesellschaft\s*mbH|Treuhandgesellschaft\s*mbH|Consulting\s*GmbH|Investment\s*GmbH|Holding\s*GmbH|Service\s*GmbH|Logistik\s*GmbH|Transport\s*GmbH|Immobilien\s*GmbH|Immobilienverwalt\s*GmbH|Immobilienmanagement\s*GmbH|Immobilienfonds\s*GmbH|Immobilienentwicklung\s*GmbH|Immobilienberatung\s*GmbH|Immobilienmakler\s*GmbH|Immobilienvermittlung\s*GmbH|Immobilienverwaltung\s*GmbH))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Analyse Allexwald GmbH` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `853911e7`  
**Description:**
Matches specific entity 'Analyse Allexwald GmbH' and similar patterns where 'Analyse' is part of the name.

**Content:**
```
(?<!\w)(Analyse\s+[A-Z][a-zA-Z\-\.]+\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 3480 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die UAMA Analyse Consulting GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

**False Positives:**

- `Analyse Consulting GmbH` — partial — pred is substring of gold: `UAMA Analyse Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UAMA Analyse Consulting GmbH`(organisation)

</details>

---

## `c Stahl und Anlagenbau GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9ae3b1e8`  
**Description:**
Matches the specific entity 'c Stahl und Anlagenbau GmbH' and its variants including the question mark.

**Content:**
```
(?<!\w)(c\s+Stahl\s+und\s+Anlagenbau\s+GmbH\??)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `D-Stahl und Anlagenbau GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `81b85257`  
**Description:**
Matches the specific entity 'D-Stahl und Anlagenbau GmbH' and its variants.

**Content:**
```
(?<!\w)(D\-Stahl\s+und\s+Anlagenbau\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landespolizeidirektion Standalone` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `215ccbc9`  
**Description:**
Matches 'Landespolizeidirektion' as a standalone entity, even without a following location name.

**Content:**
```
(?<!\w)(Landespolizeidirektion)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 3460 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_22`)


Dass die Pistole im Abschlussbericht der Landespolizeidirektion Niederösterreich einmal als Luftdruckpistole (ON 4 S 11) und einmal als Faustfeuerwaffe (ON 4 S 9) bezeichnet wird, bedurfte keiner Erörterung in den Urteilsgründen (Z 5 zweiter Fall), weil es sich in beiden Fällen jedenfalls um eine (Schuss-)Waffe im Sinn der §§ 2, 3 WaffG handelt. Die Rechtsrüge (Z 10) vermisst Feststellungen „hinsichtlich Merkmalen und Eigenschaften dieser Luftdruckpistole“, unterlässt es aber, vorzubringen, weshalb die Konstatierungen, wonach es sich bei der Waffe um eine Luftdruckpistole, Marke Webley Stinger, 4,5 mm, mit der feste Geschosse verschossen werden, und demnach um keine Spielzeugpistole handelte (US 2, 6), zur rechtlichen Beurteilung nicht ausreichen sollten.

**False Positives:**

- `Landespolizeidirektion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzamts Österreich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `be57329a`  
**Description:**
Matches 'Finanzamtes Österreich' and 'Finanzamts Österreich' specifically.

**Content:**
```
(?<!\w)(Finanzamtes\s+\u00d6sterreich|Finanzamts\s+\u00d6sterreich)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Österreich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d146b0f7`  
**Description:**
Matches 'Finanzamt Österreich' and 'Finanzamtes Österreich' specifically to prevent the generic location rule from capturing it incorrectly.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Österreich)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hans Bühler KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ac274d51`  
**Description:**
Matches the specific entity 'Hans Bühler KG' to ensure full capture.

**Content:**
```
(?<!\w)Hans\s+B\u00fchler\s+KG(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KRW Kärnten Steuerberatungsgesellschaft mbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `415e15e2`  
**Description:**
Matches the specific entity 'KRW Kärnten Steuerberatungsgesellschaft mbH' to ensure full capture.

**Content:**
```
(?<!\w)KRW\s+K\u00e4rnten\s+Steuerberatungsgesellschaft\s+mbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BMF Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8cb7f7e2`  
**Description:**
Matches the abbreviation BMF (Bundesministerium für Finanzen) in various contexts, excluding cases where it is followed by numbers indicating a document number rather than the org.

**Content:**
```
(?<!\w)(?<!-)BMF(?!\w|\s+[A-Z]|\s+\d+|\s+\d{2}\.\d{2}\.\d{4}|\s+\d{2}/\d{2}/\d{4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Billa Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0600f0df`  
**Description:**
Matches 'Billa' as a specific organization entity (supermarket chain), distinguishing it from common nouns.

**Content:**
```
(?<!\w)(Billa)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Gemeindebezirkes` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `15be3bd6`  
**Description:**
Matches 'Wiener Gemeindebezirk' and its genitive form 'Wiener Gemeindebezirkes' as an organisation.

**Content:**
```
(?<!\w)Wiener\s+Gemeindebezirk(?:es)?(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Steuerberatungspartnerschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ea868cd0`  
**Description:**
Matches company names ending in 'Steuerberatungspartnerschaft', capturing the full name including the prefix.

**Content:**
```
(?<!\w)([A-Z][a-zA-Z\s&]+\s+Steuerberatungspartnerschaft)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WestImmobilien GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f54c731d`  
**Description:**
Matches the specific entity 'WestImmobilien GmbH' to ensure it is captured even when the generic rule might miss it due to specific spacing or context.

**Content:**
```
(?<!\w)WestImmobilien\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `OstLextraMedien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `529b33b6`  
**Description:**
Matches the specific entity 'OstLextraMedien' as an organisation.

**Content:**
```
(?<!\w)OstLextraMedien(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat Klagenfurt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6ea9f27b`  
**Description:**
Matches 'Magistrat Klagenfurt' as an organisation.

**Content:**
```
(?<!\w)Magistrat\s+Klagenfurt(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Erste Bank` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `18285c60`  
**Description:**
Matches 'Erste Bank' as an organisation.

**Content:**
```
(?<!\w)Erste\s+Bank(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GKK Wien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3e5e7186`  
**Description:**
Matches 'GKK Wien' as an organisation.

**Content:**
```
(?<!\w)GKK\s+Wien(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GKK Kärnten` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3472e394`  
**Description:**
Matches 'GKK Kärnten' as an organisation.

**Content:**
```
(?<!\w)GKK\s+K\u00e4rnten(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fuchshuber Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8b2db3a0`  
**Description:**
Matches 'Fuchshuber Steuerberatung GmbH' as an organisation.

**Content:**
```
(?<!\w)Fuchshuber\s+Steuerberatung\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `S Projektenwicklung und Beteiligungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `662c293d`  
**Description:**
Matches the specific entity 'S Projektenwicklung und Beteiligungs GmbH' which was missing from the generic GmbH rule.

**Content:**
```
(?<!\w)S\s+Projektenwicklung\s+und\s+Beteiligungs\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Seidlmayer Software GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9640a869`  
**Description:**
Matches the specific entity 'Seidlmayer Software GmbH' to ensure it is captured.

**Content:**
```
(?<!\w)Seidlmayer\s+Software\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt Klagenfurt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `54e43296`  
**Description:**
Matches 'Magistrat der Stadt Klagenfurt' as an organisation.

**Content:**
```
(?<!\w)Magistrat\s+der\s+Stadt\s+Klagenfurt(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gwen Bozdag` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `41774032`  
**Description:**
Matches the specific entity 'Gwen Bozdag' as an organisation.

**Content:**
```
(?<!\w)Gwen\s+Bozdag(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `LG für ZRS Graz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e207f02`  
**Description:**
Matches 'LG für ZRS Graz' as an organisation.

**Content:**
```
(?<!\w)LG\s+f\u00fcr\s+ZRS\s+Graz(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KAPAS Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `13347f79`  
**Description:**
Matches the specific entity 'KAPAS Steuerberatung GmbH'.

**Content:**
```
(?<!\w)KAPAS\s+Steuerberatung\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt für Großbetriebe` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c3304d06`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'für Großbetriebe'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+f\u00fcr\s+Gro\u00dfbetriebe)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Amstetten Melk Scheibbs` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0bf2abe1`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed strictly by 'Amstetten Melk Scheibbs' as a complete location phrase, ensuring no partial matches.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Amstetten\s+Melk\s+Scheibbs)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Neunkirchen Wiener Neustadt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `06b30364`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Neunkirchen Wiener Neustadt'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Neunkirchen\s+Wiener\s*Neustadt)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt End of Sentence` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8da22a2d`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' when it appears at the very end of a sentence or text, ensuring it is captured even if not followed by a location or article.

**Content:**
```
(?<!\w)(?<!das\s)(?<!dem\s)(?<!des\s)(?<!ein\s)(?<!einem\s)(?<!einer\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!vom\s)(?<!am\s)(?<!zu\s)(?<!bei\s)(?<!von\s)(?<!mit\s)(?<!in\s)(?<!auf\s)(?<!an\s)(?<!f\u00fcr\s)(?<!nach\s)(?<!vor\s)(?<!\u00fcber\s)(?<!unter\s)(?<!zwischen\s)(?<!durch\s)(?<!ohne\s)(?<!gegen\s)(?<!neben\s)(?<!hinter\s)(?<!\w)Finanzamt(?:es)?(?=\s*$|\s*\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FH Wiener Neustadt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8a96923f`  
**Description:**
Matches 'FH Wiener Neustadt' as a specific educational organization entity.

**Content:**
```
(?<!\w)(FH\s+Wiener\s+Neustadt)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Quappill & Lechbauer Technik GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `290b509c`  
**Description:**
Matches 'Quappill & Lechbauer Technik' optionally followed by 'GmbH', capturing only the name part as the entity.

**Content:**
```
(?<!\w)(Quappill\s+&\s+Lechbauer\s+Technik)(?:\s+GmbH)?(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ELDA Competence Center` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `619174c6`  
**Description:**
Matches the specific entity 'ELDA Competence Center'.

**Content:**
```
(?<!\w)(ELDA\s+Competence\s+Center)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Quappill & Lechbauer Technik` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `20a935f2`  
**Description:**
Matches the specific entity 'Quappill & Lechbauer Technik' when 'GmbH' is not present or is separated by extra spaces, ensuring the core name is captured.

**Content:**
```
(?<!\w)(Quappill\s+&\s+Lechbauer\s+Technik)(?!\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lieferant-C KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a9c6a040`  
**Description:**
Matches the specific entity 'Lieferant-C KG' to ensure full capture.

**Content:**
```
(?<!\w)(Lieferant-C\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Wien Numbers` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a4233322`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Wien' and any sequence of numbers separated by slashes (e.g., 1/23, 12/13/14), ensuring the full location is captured including any following city name.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Wien\s+\d+(?:/\d+)+(?:\s+[A-Z][a-zA-Z\s-]+)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Versorgungskasse VVaG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b2eea455`  
**Description:**
Matches 'Versorgungskasse Deutscher Unternehmen VVaG' specifically.

**Content:**
```
(?<!\w)(Versorgungskasse\s+Deutscher\s+Unternehmen\s+VVaG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gronmeier Robotik GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b93cb380`  
**Description:**
Matches the specific entity 'Gronmeier Robotik GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(Gronmeier\s+Robotik\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `39dbfe22`  
**Description:**
Matches the specific entity 'Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft' to ensure full capture.

**Content:**
```
(?<!\w)(Dr\.\s+Roland\s+Gabl\s+Rechtsanwalts-\s+Kommandit-Partnerschaft)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Abbreviation with Location` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b5f1363`  
**Description:**
Matches the abbreviation FA (Finanzamt) followed by specific locations, including cases where it is preceded by 'www.' to capture the full URL entity. Uses a lookahead to ensure the location is one of the known patterns. Added functional descriptors like 'für Neurologie'.

**Content:**
```
(?:www\.)?(FA\s+(?:St\.\s*Johann\s+Tamsweg\s+Zell\s+am\s+See|Neunkirchen\s+Wr\.\s*Neustadt|Neunkirchen\s+Wiener\s*Neustadt|Amstetten\s+Melk\s+Scheibbs|Braunau\s+Ried\s+Schärding|Bruck\s+Eisenstadt\s+Oberwart|Kirchdorf\s+Perg\s+Steyr|Kufstein\s+Schwaz|Wien\s+12/13/14\s+Purkersdorf|Wien\s+2/20/21/22|Wien\s+6/7/15|Baden\s+Mödling|Salzburg-Stadt|Graz-Stadt|Klagenfurt-Stadt|Linz-Stadt|Wels-Stadt|Innsbruck-Stadt|Bregenz-Stadt|Eisenstadt-Stadt|St\.\s*Pölten-Stadt|Villach-Stadt|Dornbirn-Stadt|Leoben-Stadt|Lienz-Stadt|Amstetten-Stadt|Baden-Stadt|Braunau-Stadt|Eferding-Stadt|Feldkirchen-Stadt|Gmunden-Stadt|Hall-Stadt|Horn-Stadt|Kufstein-Stadt|Lustenau-Stadt|Neuhaus-Stadt|Oberwart-Stadt|Perg-Stadt|Ried-Stadt|Schwaz-Stadt|Steyr-Stadt|Telfs-Stadt|Waidhofen-Stadt|Wels-Stadt|Wien-Stadt|Wolfsberg-Stadt|Zell-Stadt|Zwettl-Stadt|Lilienfeld\s+St\.\s*Pölten|Salzburg-Land|Graz-Umgebung|Braunau\s+Ried|Bregenz|Waldviertel|Innsbruck|Linz|Feldkirch|Salzburg\s+Stadt|Linz\s+Stadt|Wels\s+Stadt|Klagenfurt\s+Stadt|Graz\s+Stadt|Innsbruck\s+Stadt|Bregenz\s+Stadt|Eisenstadt\s+Stadt|St\.\s*Pölten\s+Stadt|Villach\s+Stadt|Dornbirn\s+Stadt|Leoben\s+Stadt|Lienz\s+Stadt|Amstetten\s+Stadt|Baden\s+Stadt|Braunau\s+Stadt|Eferding\s+Stadt|Feldkirchen\s+Stadt|Gmunden\s+Stadt|Hall\s+Stadt|Horn\s+Stadt|Kufstein\s+Stadt|Lustenau\s+Stadt|Neuhaus\s+Stadt|Oberwart\s+Stadt|Perg\s+Stadt|Ried\s+Stadt|Schwaz\s+Stadt|Steyr\s+Stadt|Telfs\s+Stadt|Waidhofen\s+Stadt|Wels\s+Stadt|Wien\s+Stadt|Wolfsberg\s+Stadt|Zell\s+Stadt|Zwettl\s+Stadt|Lilienfeld\s+St\.\s*Pölten|Hollabrunn|Schwechat\s+Gerasdorf|Tirol\s+Ost|Gmunden\s+Vöcklabruck|Spittal\s+Villach|Grieskirchen\s+Wels|Steiermark\s+Mitte|für\s+Großbetriebe|für\s+Gebühren|Verkehrsteuern|Glücksspiel|Österreich(?:s)?|für\s+Gebühren|Verkehrsteuern|Glücksspiel|Klagenfurt\s+St\.\s*Veit\s+Wolfsberg|für\s+Neurologie\s+und\s+Psychiatrie|für\s+Neurologie|für\s+Psychiatrie))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Graz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `248bb8fe`  
**Description:**
Matches 'Finanzamtes Graz' specifically, including 'Graz-Stadt' and 'Graz-Umgebung' variants, and handling space before 'Stadt' (e.g., 'Graz- Stadt').

**Content:**
```
(?<!\w)Finanzamtes\s+(?:Graz(?:-\s*Stadt|-Umgebung)?|Graz-Stadt|Graz-Umgebung)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Universität Innsbruck` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bdadc9c4`  
**Description:**
Matches 'Universität Innsbruck' as an organisation.

**Content:**
```
(?<!\w)(Universit\u00e4t\s+Innsbruck)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Höllermeier Schaller & Partner Steuerberatung Hallein GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b565f211`  
**Description:**
Matches the specific entity 'Höllermeier Schaller & Partner Steuerberatung Hallein GmbH' including variable whitespace.

**Content:**
```
(?<!\w)(Höllermeier\s+Schaller\s+&\s+Partner\s+Steuerberatung\s+Hallein\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ernst & Young Steuerberatungsgesellschaft m.b.H.` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cd736f7c`  
**Description:**
Matches 'Ernst & Young Steuerberatungsgesellschaft m.b.H.' variants including hyphenation and spacing.

**Content:**
```
(?<!\w)(Ernst\s+&\s+Young\s+Steuerberatungs(?:-\s*)?gesellschaft\s+m\.b\.H\.?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wirtschaftskammer Entities` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c9527b2a`  
**Description:**
Matches 'Wirtschaftskammer' followed by a location or specific identifier (e.g., 'Wirtschaftskammer ABC'), capturing the full entity name.

**Content:**
```
(?<!\w)(Wirtschaftskammer\s+[A-Z][a-zA-Z0-9\s-]+)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `RheinDertriHandel` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a45d62fe`  
**Description:**
Matches the specific entity 'RheinDertriHandel' as an organisation.

**Content:**
```
(?<!\w)(RheinDertriHandel)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dr. Obermayer Rechtsanwalt GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b7fb0990`  
**Description:**
Matches the specific entity 'Dr. Obermayer Rechtsanwalt GmbH' as an organisation.

**Content:**
```
(?<!\w)(Dr\.\s+Obermayer\s+Rechtsanwalt\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Claus & Berthold Rechtsanwaltspartnerschaft KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `57c0f304`  
**Description:**
Matches the specific entity 'Claus & Berthold Rechtsanwaltspartnerschaft KG' as an organisation.

**Content:**
```
(?<!\w)(Claus\s+&\s+Berthold\s+Rechtsanwaltspartnerschaft\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FLAG Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ea948e66`  
**Description:**
Matches the specific acronym FLAG (Arbeitslosenversicherungsgesetz) as an organisation, excluding cases where it is part of a compound word, followed by '1967' (law citation), or preceded by 'iSd', 'Abs.', 'lit.', or '§' (legal citation context). Also excludes cases where FLAG is followed by numbers or slashes indicating a case number. STRICTLY requires context indicating it is an organization or law reference.

**Content:**
```
(?<!\w)(?<!-)FLAG(?!\s+1967)(?!\s*\))(?!\w)(?<!iSd\s)(?<!Abs\.\s)(?<!Abs\s)(?<!lit\.\s)(?<!lit\s)(?<!§\s)(?!\s,)(?!\s§)(?!\s*§)(?!\s*\d)(?!\s*/)(?!\s*\d-)(?!\s*\d\s)(?<!\s)(?!\s)(?<!\s)(?!\s)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KG Standalone` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1c1815c6`  
**Description:**
Matches company names ending in 'KG' or 'GmbH & Co KG'. STRICTLY requires a capitalized name prefix (letters, ampersands, hyphens, spaces) immediately before 'KG'. Excludes trailing non-name characters like 'xxxxx' or 'bzw.'.

**Content:**
```
(?<!\w)(?<!iSd\s)(?<!FLAG\s)(?<!FLAG\n)(?<!FLAG\t)(?<!FLAG\s)(?<!FLAG\b)(?<!Berufsausbildung\s)(?<!Adresse\s)(?<!Anteiles\s)(?<!Kommunalsteuer\s)(?<!Ablichtung\s)(?<!Kontoauszuges\s)(?<!Firmenbuchauszug\s)(?<!Einschreiter\s)(?<!ANTRAG\s)(?<!Abs\.\s)(?<!Abs\s)(?<!Abs\.)(?<!Abs\b)(?<!lit\.\s)(?<!lit\s)(?<!Bf\.\s)(?<!Bf\s)(?<!Bf\.)\s*([A-Z][a-zA-Z0-9\s&.,-]{2,60}\s+(?:GmbH\s*&\s*Co\s*KG|KG))(?!\s*[a-zA-Z]|\s*[0-9]|\s*[.,;:?!])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Höhere Lehranstalt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ebb9858c`  
**Description:**
Matches 'Höhere Lehranstalt' followed by specific educational fields, capturing the full institution name.

**Content:**
```
(?<!\w)(Höhere\s+Lehranstalt\s+für\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht/BFG Compound` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `83bc455c`  
**Description:**
Matches 'Bundesfinanzgericht/BFG' as a single compound entity.

**Content:**
```
(?<!\w)(Bundesfinanzgericht/BFG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hennicke Robotik` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `415bdc54`  
**Description:**
Matches the specific entity 'Hennicke Robotik' which is a company name without a standard suffix like GmbH/AG.

**Content:**
```
(?<!\w)(Hennicke\s+Robotik)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Quoted Company Name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `11a9a186`  
**Description:**
Matches company names enclosed in German quotation marks, but strictly requires the content to contain organizational suffixes or keywords (GmbH, AG, KG, m.b.H., Steuerberatung, Rechtsanwalt, Bank, Versicherung) to avoid matching document titles or case references.

**Content:**
```
(?:„|“)([A-Z][A-Za-z0-9\s&.,-]*?(?:GmbH|AG|KG|m\.b\.H\.|Steuerberatung|Rechtsanwalt|Bank|Versicherung|Partnerschaft|Gesellschaft|Unternehmen|Dienstleistung|Consulting|Ingenieure|Architekten|Notar|Wirtschaftsprüfung)[A-Za-z0-9\s&.,-]*?)(?:„|“)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1077 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/6Ob69_23z`) (sent_id: `deanon_260716_TRAIN/6Ob69_23z_21`)


6. 2019 (bis 13. 1. 2020) von einer namentlich genannten Person „von Kirmayr&Rölfing IT Bildungsinstituts, Moorkamp Bildung GmbH“ (die später vom Erstgericht in Bezug auf den Komplementär als „seine“ bezeichnet wird) dem Beklagten an eine auf die Fahrschule lautende E-Mail-Adresse unter Angabe (jeweils) von „Rechnungsnummer Fa Scheffold Druck GmbH“ (was einer gekürzten Angabe der GmbH entspricht) und einer Kurzbezeichnung des Inhalts (etwa: „Gehälter 06-2019“) übermittelt wurden, sie an die „Firma Fahrschule Till Frohschammer [mit der Adresse des Hauptstandorts] gerichtet waren, wobei die UID-Nummer ab Dezember 2019 geändert wurde.

**False Positives:**

- `Rechnungsnummer Fa Scheffold Druck GmbH` — partial — gold is substring of pred: `Scheffold Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kirmayr&Rölfing IT`(organisation)
- `Moorkamp Bildung GmbH`(organisation)
- `Scheffold Druck GmbH`(organisation)
- `Till Frohschammer`(organisation)

</details>

---

## `Landesgerichtes für ZRS` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `17e0844a`  
**Description:**
Matches 'Landesgerichtes für ZRS' followed by a city name, stopping before prepositions.

**Content:**
```
(?<!\w)(Landesgerichtes\s+f\u00fcr\s+ZRS\s+[A-Z][a-zA-Z]+)(?!\s+(?:zu|zur|zum|als|bei|in|an|auf|mit|von|f\u00fcr|nach|vor|\u00fcber|unter|ohne|gegen|durch|seit|neben|zwischen|hinter|Konkursgericht|Konkurs|GZ|G\.Z\.|eine|gegen|eingereicht|Beschwerde|ein|entrichtet|diesem|zu\s+GZ|zu\s+G\.Z\.|zu\s+Akten|zu\s+Verfahren|zu\s+G\.Z\.\s+vom))(?=[\s.,;:!?]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kraftbachstein-Energie GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `05f88a3d`  
**Description:**
Specifically matches 'Kraftbachstein-Energie GmbH' to ensure it is captured even when the generic rule fails.

**Content:**
```
(?<!\w)(Kraftbachstein-Energie\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schweizerische Ausgleichskasse` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fcd8bc2d`  
**Description:**
Matches the specific organization 'Schweizerische Ausgleichskasse'.

**Content:**
```
(?<!\w)(Schweizerische\s+Ausgleichskasse)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht Standalone` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fcbe171e`  
**Description:**
Matches 'Bezirksgericht' as a standalone organization entity, handling genitive forms and various contexts.

**Content:**
```
(?<!\w)(Bezirksgericht(?:es)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 26 | 0 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 26 | 4000 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

**False Positives:**

- `Bezirksgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshof`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Bezirksgericht` — similar text (different position): `Bezirksgerichts Mödling`
- `Bezirksgericht` — similar text (different position): `Bezirksgerichts Mödling`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Florens Drehkopf, LLB`(person)
- `16. Dezember 1952`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mödling`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_8`)


Sachlich zuständig zur Erteilung der Vollstreckbarerklärung ist kraft Eigenzuständigkeit das Bezirksgericht.

**False Positives:**

- `Bezirksgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_8`)


Das bisher zuständige Bezirksgericht werde daher die Interessen der Minderjährigen besser wahren können, zumal unmittelbare pflegschaftsbehördliche Maßnahmen nicht zu setzen seien.

**False Positives:**

- `Bezirksgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_7`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Kreutzerstraße 7, 4851 Haunolding, Österreich aufhalte (ON 7).

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Vöcklabruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Vöcklabruck`(organisation)
- `Bezirksgericht Villach`(organisation)
- `Kreutzerstraße 7, 4851 Haunolding, Österreich`(address)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_4`)


Anstelle des Bezirksgerichts Kitzbühel wird das Bezirksgericht Mödling als zur Führung des Verlassenschaftsverfahrens zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht` — similar text (different position): `Bezirksgerichts Kitzbühel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Kitzbühel`(organisation)
- `Bezirksgericht Mödling`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_10`)


Im Hinblick auf die angeführten Umstände erscheint die Übertragung der Zuständigkeit an das Bezirksgericht Mödling im Sinne des § 31 Abs 1 JN zweckmäßig und geeignet, eine Verkürzung und Verbilligung des Verfahrens zu bewirken.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mödling`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_16`)


Mit Urteil des Bezirksgerichts Bezirksgericht für Handelssachen Wien vom 21.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_12`)


Ein anderes Verständnis legt – entgegen der vom Berufungsgericht mit Verweis auf eine Literaturstelle (Hinterhofer/Oshidari, System des österreichischen Strafverfahrens Rz 10.89) vertretenen Ansicht – auch die historische Interpretation nicht nahe: Die im Verfahren vor dem Bezirksgericht schon in der Stammfassung der StPO vorgesehene Rechtsmittellegitimation des Privatbeteiligten (zum Nachteil des Angeklagten) wurde von der Rechtsprechung und überwiegend im Schrifttum zur früheren Rechtslage (mit Blick auf § 366 Abs 2 letzter Satz StPO idF vor BGBl 1978/169) dahin ausgelegt, dass dieser Berufung (nur) dann habe ergreifen können, wenn das Erstgericht eine Entschädigung (zumindest teilweise) zugesprochen hatte, nicht jedoch bei vollständiger Verweisung auf den Zivilrechtsweg.

**False Positives:**

- `Bezirksgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/3Nc11_13t`) (sent_id: `deanon_260716_TRAIN/3Nc11_13t_10`)


Für eine Unterlassungsexekution ist gemäß § 18 Z 4 zweiter Fall EO jenes Bezirksgericht zuständig, in dessen Sprengel die erste Exekutionshandlung, nämlich die Zustellung der Exekutionsbewilligung, zu bewirken ist.

**False Positives:**

- `Bezirksgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_9`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

**False Positives:**

- `Bezirksgericht` — similar text (different position): `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und den Hofrat Dr. Steger als weitere Richter in der Pflegschaftssache des mj Aron Margwarth, geboren am 29. März 1957, Vater Klaus Rufer, vertreten durch Prof. Dr. Georg Zanger, Rechtsanwalt in Wien, wegen Obsorge, über den Delegierungsantrag der Mutter Rafaela Erreth, vertreten durch Mag. Britta Schönhart-Loinig, Rechtsanwältin in Wien, den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Pflegschaftssache vom Bezirksgericht Gänserndorf an das Bezirksgericht Villach wird abgewiesen.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Gänserndorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Dr. Grohmann`(person)
- `Dr. Steger`(person)
- `Aron Margwarth`(person)
- `29. März 1957`(date)
- `Klaus Rufer`(person)
- `Prof. Dr. Georg Zanger`(person)
- `Rafaela Erreth`(person)
- `Mag. Britta Schönhart-Loinig`(person)
- `Bezirksgericht Gänserndorf`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_12`)


Seit damals ist das Bezirksgericht Gänserndorf mit diesem mittlerweile hoch eskalierten Obsorgestreit regelmäßig und intensiv befasst, der Prozessstoff umfasst bereits zwei Aktenbände.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Gänserndorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Gänserndorf`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_30`)


Der zukünftige gewöhnliche Aufenthalt des Minderjährigen hänge vom Ausgang des beim Bezirksgericht Gänserndorf anhängigen Verfahrens ab, das seit August 2018 intensiv mit den zugrunde liegenden Umständen befasst sei, bereits Sachverständigengutachten und Stellungnahmen des Jugendamts eingeholt und anlässlich von Tagsatzungen vergleichsweise Einigungen zum Kontaktrecht initiiert habe.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Gänserndorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Gänserndorf`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_36`)


Die Handhabung des pflegschaftsgerichtlichen Schutzes des Kindes sei durch das Bezirksgericht Gänserndorf wirksamer gestaltbar als durch das Bezirksgericht Villach, das die Familie überhaupt noch nicht kenne.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Gänserndorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Gänserndorf`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_39`)


Die Mutter habe nicht die Übertragung der Zuständigkeit nach § 111 JN, sondern die Delegierung der Außerstreitsache nach § 31 Abs 1 JN begehrt, die Entscheidung darüber komme – da es sich um eine Delegierung aus einem Oberlandesgerichtssprengel an den anderen handle – dem Obersten Gerichtshof zu. Das Bezirksgericht Gänserndorf legte die Akten daraufhin dem Obersten Gerichtshof zur Entscheidung über den Delegierungsantrag vor.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Gänserndorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshof`(organisation)
- `Bezirksgericht Gänserndorf`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_58`)


Darüber hinaus hat das Bezirksgericht Gänserndorf bereits für 26.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Gänserndorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Gänserndorf`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_62`)


Der Umstand, dass der Minderjährige derzeit im Sprengel des Bezirksgerichts Villach wohnt und für die Mutter seine Betreuung bei Terminen am Bezirksgericht Villach leichter zu organisieren wäre als beim Bezirksgericht Gänserndorf, reicht daher für eine Bejahung der Zweckmäßigkeit iSd § 31 Abs 1 JN nicht aus.

**False Positives:**

- `Bezirksgericht` — similar text (different position): `Bezirksgerichts Villach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Villach`(organisation)
- `Bezirksgericht Villach`(organisation)
- `Bezirksgericht Gänserndorf`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_4`)


Lieselotte Sedlmair, und 2. Yorick Bergbauer, wegen Erlassung einer einstweiligen Verfügung, infolge der Vorlage des Aktes 1 C 16/12t des Bezirksgerichts Wiener Neustadt zur Entscheidung über den negativen Kompetenzkonflikt mit dem Bezirksgericht Mürzzuschlag nach § 47 JN den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag auf Erlassung der einstweiligen Verfügung ist das Bezirksgericht Wiener Neustadt zuständig.

**False Positives:**

- `Bezirksgericht` — similar text (different position): `Bezirksgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Sedlmair`(person)
- `Yorick Bergbauer`(person)
- `Bezirksgerichts Wiener Neustadt`(organisation)
- `Bezirksgericht Mürzzuschlag`(organisation)
- `Bezirksgericht Wiener Neustadt`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_6`)


Text Begründung: Der Antragsteller stellte mit am 2. 1. 2012 beim Bezirksgericht Mürzzuschlag eingelangtem Schriftsatz den Antrag, mit einstweiliger Verfügung gemäß §§ 382g, 381 Z 2 EO gegen die Antragsgegner diverse Verbote zu erlassen.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Mürzzuschlag`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mürzzuschlag`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_7`)


Das Bezirksgericht Mürzzuschlag erklärte sich mit am selben Tag gefasstem Beschluss gemäß § 387 Abs 4 EO für unzuständig und überwies das Verfahren nach § 44 JN an das nicht offenbar unzuständige Bezirksgericht Wiener Neustadt.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Mürzzuschlag`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mürzzuschlag`(organisation)
- `Bezirksgericht Wiener Neustadt`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_10`)


2. 2012 den Beschluss, die Rechtssache wiederum dem Bezirksgericht Mürzzuschlag (zurück-)zuüberweisen.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Mürzzuschlag`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mürzzuschlag`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/8Ob96_17a`) (sent_id: `deanon_260716_TRAIN/8Ob96_17a_16`)


Das Erstgericht schränkte das Verfahren auf die Fragen der örtlichen und sachlichen Zuständigkeit ein und stellte – soweit Gegenstand des Rechtsmittelverfahrens – fest, der Antrag sei im Verfahren außer Streitsachen zu erledigen und die Rechtssache werde an das nicht offenbar unzuständige Bezirksgericht Fünfhaus überwiesen.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Fünfhaus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Fünfhaus`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/8Ob96_17a`) (sent_id: `deanon_260716_TRAIN/8Ob96_17a_43`)


3.3 Die vom Erstgericht ausgesprochene Überweisung an das Bezirksgericht Fünfhaus wird im Revisionsrekurs nicht inhaltlich bekämpft.

**False Positives:**

- `Bezirksgericht` — partial — pred is substring of gold: `Bezirksgericht Fünfhaus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Fünfhaus`(organisation)

</details>

---

## `Glanzber E-Commerce GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3765a04a`  
**Description:**
Matches the specific entity 'Glanzber E-Commerce GmbH' variants including the em-dash or hyphen.

**Content:**
```
(?<!\w)(Glanzber\s*(?:E-|E\u2011|E\u2013)Commerce\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Vercon-Holz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e44bd9d4`  
**Description:**
Matches the specific entity 'Vercon-Holz' as an organisation.

**Content:**
```
(?<!\w)(Vercon-Holz)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WKO Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0976627b`  
**Description:**
Matches the abbreviation WKO (Wirtschaftskammer Österreich) as an organisation.

**Content:**
```
(?<!\w)(WKO)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Österreich FAÖ Combined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a3ea39c8`  
**Description:**
Matches the combined entity 'Finanzamt Österreich/FAÖ' or 'Finanzamt Österreich FAÖ' as a single organisation entity.

**Content:**
```
(?<!\w)(Finanzamt\s+Österreich(?:\s*/\s*FAÖ|\s+FAÖ))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Österreich/FAÖ Combined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `44cca1c5`  
**Description:**
Matches 'Finanzamt Österreich/FAÖ' or 'Finanzamt Österreich FAÖ' as a single entity.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+\u00d6sterreich(?:/|\s)FA\u00d6)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SUVA Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9d04c399`  
**Description:**
Matches the abbreviation SUVA (Schweizerische Unfallversicherung) as an organisation.

**Content:**
```
(?<!\w)(SUVA)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Paracelsus Medizinische Privatuniversität` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5469cb3e`  
**Description:**
Matches the specific entity 'Paracelsus Medizinische Privatuniversität'.

**Content:**
```
(?<!\w)(Paracelsus\s+Medizinische\s+Privatuniversität)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Universität Salzburg` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d616d7ee`  
**Description:**
Matches the specific entity 'Universität Salzburg'.

**Content:**
```
(?<!\w)(Universität\s+Salzburg)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Yang + Jannowsky Handel GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f7a10ea1`  
**Description:**
Matches the specific entity 'Yang + Jannowsky Handel GmbH'.

**Content:**
```
(?<!\w)(Yang\s+\+\s+Jannowsky\s+Handel\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deloitte Tax Wirtschaftsprüfungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e6f462dc`  
**Description:**
Matches the specific entity 'Deloitte Tax Wirtschaftsprüfungs GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(Deloitte\s+Tax\s+Wirtschaftsprüfungs\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hauer & Partner Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d4b25141`  
**Description:**
Matches the specific entity 'Hauer & Partner Steuerberatung GmbH'.

**Content:**
```
(?<!\w)Hauer\s+&\s+Partner\s+Steuerberatung\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GKA Gao u Keki-Angermann RA GesbR` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `30b47c22`  
**Description:**
Matches the specific entity 'GKA Gao u Keki-Angermann RA GesbR'.

**Content:**
```
(?<!\w)GKA\s+Gao\s+u\s+Keki-Angermann\s+RA\s+GesbR(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `DR. NIKOLAUS Wirtschaftstreuhand GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `383cc39b`  
**Description:**
Matches the specific entity 'DR. NIKOLAUS Wirtschaftstreuhand GmbH - Wirtschaftsprüfungs- und Steuerberatungsgesellschaft'.

**Content:**
```
(?<!\w)DR\.\s+NIKOLAUS\s+Wirtschaftstreuhand\s+GmbH\s*-\s*Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BG&P Binder Grossek & Partner Steuerberatung und Wirtschafts- prüfung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3628afd1`  
**Description:**
Matches the specific entity 'BG&P Binder Grossek & Partner Steuerberatung und Wirtschafts- prüfung GmbH' with variable whitespace.

**Content:**
```
(?<!\w)BG&P\s+Binder\s+Grossek\s+&\s+Partner\s+Steuerberatung\s+und\s+Wirtschafts-?\s+prüfung\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Spittal Villach` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7472bbe0`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Spittal Villach'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Spittal\s+Villach)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Braunau Ried` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1e794f7c`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Braunau Ried' specifically, allowing for optional 'Schärding' but prioritizing the shorter form if the text ends or is followed by a non-location word.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Braunau\s+Ried)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Braunau Ried Schärding` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d332fb93`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Braunau Ried Schärding'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Braunau\s+Ried\s+Sch\u00e4rding)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BDO Austria GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `83cd8d1d`  
**Description:**
Matches the specific entity 'BDO Austria GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft'.

**Content:**
```
(?<!\w)BDO\s+Austria\s+GmbH\s+Wirtschaftspr\u00fcfungs-?\s+und\s+Steuerberatungsgesellschaft(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ernst & Young Steuerberatungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d32f5f41`  
**Description:**
Matches 'Ernst & Young Steuerberatungs GmbH' variants including hyphenation and spacing.

**Content:**
```
(?<!\w)Ernst\s+&\s+Young\s+Steuerberatungs-?\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Krüger/Bauer Rechtsanwälte GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8c0b594a`  
**Description:**
Matches the specific entity 'Krüger/Bauer Rechtsanwälte GmbH'.

**Content:**
```
(?<!\w)Kr\u00fcger/Bauer\s+Rechtsanw\u00e4lte\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AMS Abbreviation` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3c9787c1`  
**Description:**
Matches the abbreviation AMS (Arbeitsmarktservice) as an organisation entity, ensuring it captures the acronym even when followed by 'Österreich' or other context.

**Content:**
```
(?<!\w)(AMS(?:\s+Österreich)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1867 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob222_17v`) (sent_id: `deanon_260716_TRAIN/3Ob222_17v_8`)


Danach meldete er sich beim AMS als arbeitssuchend.

**False Positives:**

- `AMS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `GmbH Missing Space` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b0b6490f`  
**Description:**
Matches company names ending in 'GmbH' or 'm.b.H.' where there is no space between the name and the suffix (e.g., 'XY-SteuerberatungsGmbH').

**Content:**
```
(?<!\w)([A-Z][a-zA-Z0-9\-]+(?:Steuerberatungs?|Rechtsanw?lte|Wirtschaftspr?fungs?|Gesellschaft|Unternehmensberatung|Technik|Robotik|Automotive|E-Commerce|Handel|Logistik|Consulting|Services|Solutions|Software|Hardware|Medien|Immobilien|Bau|Planung|Entwicklung|Produktion|Vertrieb|Marketing|Finanzen|Versicherung|Bank|Kredit|Leasing|Investment|Asset|Management|Consulting|Services|Solutions|Software|Hardware|Medien|Immobilien|Bau|Planung|Entwicklung|Produktion|Vertrieb|Marketing|Finanzen|Versicherung|Bank|Kredit|Leasing|Investment|Asset|Management)[A-Z]?)(GmbH|m\.b\.H\.?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lognexuni-Lebensmittel GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `08a161b0`  
**Description:**
Matches the specific entity 'Lognexuni-Lebensmittel GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(Lognexuni-Lebensmittel\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Zorglanzsyn-Software GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c4ab30fe`  
**Description:**
Matches the specific entity 'Zorglanzsyn-Software GmbH' to ensure full capture.

**Content:**
```
(?<!\w)Zorglanzsyn-Software\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Gänserndorf Mistelbach` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2fdf8059`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Gänserndorf Mistelbach'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+G\u00e4nserndorf\s+Mistelbach)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt St. Johann Tamsweg Zell am See` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1c7c7eb3`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'St. Johann Tamsweg Zell am See'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+St\.\s*Johann\s+Tamsweg\s+Zell\s+am\s+See)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Leoben` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5e2905a0`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Leoben', but only if NOT followed by 'Mürzzuschlag' or 'Bruck' (which are handled by other rules).

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Leoben)(?!\s+M\u00fcrzzuschlag)(?!\s+Bruck)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Logsudglanz-Versand GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1edee156`  
**Description:**
Matches the specific entity 'Logsudglanz-Versand GmbH'.

**Content:**
```
(?<!\w)(Logsudglanz-Versand\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wilsee IT Werke GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ac390104`  
**Description:**
Matches the specific entity 'Wilsee IT Werke GmbH' including a trailing period if present.

**Content:**
```
(?<!\w)(Wilsee\s+IT\s+Werke\s+GmbH\.?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Zachmann & Partner Rechtsanwälte` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `40676549`  
**Description:**
Matches the specific entity 'Zachmann & Partner Rechtsanwälte'.

**Content:**
```
(?<!\w)(Zachmann\s+&\s+Partner\s+Rechtsanwälte)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Steuerberater Metzler & Adelsberger OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ae7331d1`  
**Description:**
Matches the specific entity 'Steuerberater Metzler & Adelsberger OG'.

**Content:**
```
(?<!\w)(Steuerberater\s+Metzler\s+&\s+Adelsberger\s+OG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ARTUS Steuerberatung GmbH & Co KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9eda3336`  
**Description:**
Matches the specific entity 'ARTUS Steuerberatung GmbH & Co KG'.

**Content:**
```
(?<!\w)(ARTUS\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kleiner Eberl Brandstätter Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `01643afe`  
**Description:**
Matches the specific entity 'Kleiner Eberl Brandstätter Steuerberatung GmbH'.

**Content:**
```
(?<!\w)(Kleiner\s+Eberl\s+Brandstätter\s+Steuerberatung\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiech und Gökcek Transport GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `863e75da`  
**Description:**
Matches the specific entity 'Wiech und Gökcek Transport GmbH'.

**Content:**
```
(?<!\w)(Wiech\s+und\s+Gökcek\s+Transport\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WaldHolz OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `437959d4`  
**Description:**
Matches the specific entity 'WaldHolz OG'.

**Content:**
```
(?<!\w)(WaldHolz\s+OG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ikea Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8f025f07`  
**Description:**
Matches 'Ikea' as a specific organization entity.

**Content:**
```
(?<!\w)(Ikea)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Obi Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5877ca3d`  
**Description:**
Matches 'Obi' as a specific organization entity.

**Content:**
```
(?<!\w)(Obi)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Leiner Organization` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `864395dd`  
**Description:**
Matches 'Leiner' as a specific organization entity.

**Content:**
```
(?<!\w)(Leiner)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1568 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/4Ob26_20g`) (sent_id: `deanon_260716_TRAIN/4Ob26_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Xenia Pintar GmbH, Alfred Leiner-Straße 15, 8674 Grubbauer, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Wendling GmbH in Kitzbühel, gegen die beklagte Partei Sudwil-Umwelt GmbH, Pleschberg 7, 9872 Gössering, Österreich, Deutschland, vertreten durch Dr. Dan Katzlinger, Rechtsanwalt in Innsbruck, wegen 70.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Dezember 2019, GZ 10 R 49/19k-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Leiner` — partial — pred is substring of gold: `Alfred Leiner-Straße 15, 8674 Grubbauer, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Vogel`(person)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `MMag. Matzka`(person)
- `Xenia Pintar`(person)
- `Alfred Leiner-Straße 15, 8674 Grubbauer, Österreich`(address)
- `Dr. Wendling GmbH`(organisation)
- `Sudwil-Umwelt GmbH`(organisation)
- `Pleschberg 7, 9872 Gössering, Österreich`(address)
- `Dr. Dan Katzlinger`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

</details>

---

## `Möbelix Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5894ff9d`  
**Description:**
Matches 'Möbelix' as a specific organization entity.

**Content:**
```
(?<!\w)(Möbelix)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `MömaX Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b5188ae2`  
**Description:**
Matches 'MömaX' as a specific organization entity.

**Content:**
```
(?<!\w)(MömaX)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Otto.de Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8a38f541`  
**Description:**
Matches 'Otto.de' as a specific organization entity.

**Content:**
```
(?<!\w)(Otto\.de)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `xxxLutz Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `aa47cc64`  
**Description:**
Matches 'xxxLutz' as a specific organization entity.

**Content:**
```
(?<!\w)(xxxLutz)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Graz-Stadt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3c050989`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Graz-Stadt' specifically.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Graz-Stadt)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Neunkirchen Wr. Neustadt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `88a65b96`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Neunkirchen Wr. Neustadt' specifically.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Neunkirchen\s+Wr\.\s*Neustadt)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Kirchdorf Perg Steyr` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `91708229`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by the specific multi-word location 'Kirchdorf Perg Steyr'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Kirchdorf\s+Perg\s+Steyr)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Gemeindebezirks` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `add0ab5a`  
**Description:**
Matches 'Wiener Gemeindebezirk' and its specific form 'Wiener Gemeindebezirks' (dative/accusative genitive variant).

**Content:**
```
(?<!\w)(Wiener\s+Gemeindebezirk(?:s)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 756 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_212`)


Wiener Gemeindebezirk nicht ohne weiteres gleichwertig ist.

**False Positives:**

- `Wiener Gemeindebezirk` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bundesamt für Soziales und Behindertenwesen Genitive` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ff99acb9`  
**Description:**
Matches 'Bundesamts für Soziales und Behindertenwesen' (genitive) and 'Bundesamt für Soziales und Behindertenwesen' (nominative), including the '/BSB' suffix variant.

**Content:**
```
(?<!\w)(Bundesamts?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen(?:\s*/BSB)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Arbeits- und Sozialgericht Wien` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fef75c99`  
**Description:**
Matches 'Arbeits- und Sozialgericht Wien' as a standalone organization entity, prioritizing the full name over the partial match.

**Content:**
```
(?<!\w)Arbeits-\s+und\s+Sozialgericht\s+Wien(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 5 | 419 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/9Nc4_10b`) (sent_id: `deanon_260716_TRAIN/9Nc4_10b_5`)


2. Der Akt wird an das Arbeits- und Sozialgericht Wien zurückgestellt.  Text Begründung: Der Kläger begehrt mit seiner beim Arbeits- und Sozialgericht Wien eingebrachten Klage restliches Entgelt. Die Beklagte hat das Klagebegehren bestritten und Schadenersatzansprüche eingewendet.

**False Positives:**

- `Arbeits- und Sozialgericht Wien` — no gold match — likely missing annotation
- `Arbeits- und Sozialgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `deanon_260716_TRAIN/9Nc4_10b`) (sent_id: `deanon_260716_TRAIN/9Nc4_10b_14`)


Da sowohl das Arbeits- und Sozialgericht Wien als auch das Landesgericht Eisenstadt im Sprengel des Oberlandesgerichts Wien liegen, ist der Oberste Gerichtshof zur Entscheidung über den Delegierungsantrag nicht zuständig.

**False Positives:**

- `Arbeits- und Sozialgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Eisenstadt`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Oberste Gerichtshof`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/9Ob23_10p`) (sent_id: `deanon_260716_TRAIN/9Ob23_10p_6`)


Vorweg wird darauf hingewiesen, dass die Zustellung der Rekursentscheidung vor der Übermittlung des Aktes an das Arbeits- und Sozialgericht Wien durch das Erstgericht erfolgt ist.

**False Positives:**

- `Arbeits- und Sozialgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/9Ob59_20x`) (sent_id: `deanon_260716_TRAIN/9Ob59_20x_17`)


Weiters begehrt der Kläger die Feststellung der Haftung des Beklagten für die ihm künftig aus der unrichtigen Gutachtenserstellung durch den Beklagten im Verfahren vor dem Arbeits- und Sozialgericht Wien zur AZ 25 Cgs 77/16w entstehenden Schaden.

**False Positives:**

- `Arbeits- und Sozialgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Inn Talwerk Services GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d40eb939`  
**Description:**
Matches the specific entity 'Inn Talwerk Services GmbH' to ensure full capture.

**Content:**
```
(?<!\w)Inn\s+Talwerk\s+Services\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Leybrand&Weinforth Medien GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f83973b8`  
**Description:**
Matches the specific entity 'Leybrand&Weinforth Medien GmbH' to ensure full capture.

**Content:**
```
(?<!\w)Leybrand&Weinforth\s+Medien\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bayer Finanzen OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `05df1c95`  
**Description:**
Matches the specific entity 'Bayer Finanzen OG' to ensure full capture.

**Content:**
```
(?<!\w)Bayer\s+Finanzen\s+OG(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Bruck Eisenstadt Oberwart` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e6be7ba`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by the specific multi-word location 'Bruck Eisenstadt Oberwart'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Bruck\s+Eisenstadt\s+Oberwart)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stadt Wien Double Space` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e9bae3e1`  
**Description:**
Matches 'Stadt  Wien' (with double space) to handle typos in the text.

**Content:**
```
(?<!\w)(Stadt\s{2,}Wien)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Arbeits- und Sozialgericht` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ab31d9ae`  
**Description:**
Matches 'Arbeits- und Sozialgericht' as a standalone organization entity, ensuring it is captured even when preceded by 'als' or other prepositions, and not followed by 'Wien' (which is handled by a specific rule).

**Content:**
```
(?<!\w)(Arbeits-\s+und\s+Sozialgericht)(?!\s+Wien)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 24 | 0 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 24 | 3524 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Ing. Christian Stangl-Brachnik, MA BA`(person)
- `Mag. Claudia Gründel`(person)
- `Mathias Jendl`(person)
- `Dr. Thomas Stampfer`(person)
- `Dr. Christoph Orgler`(person)
- `Dr. Michael Stögerer`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Gabriele Griehsel`(person)
- `Dr. Wolfgang Kozak`(person)
- `Roland Soukup`(person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mag. Dr. Wolfgang Höfle`(person)
- `Ing. Thomas Bauer`(person)
- `Willibald Kollowrat, BEd`(person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH`(organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau`(organisation)
- `Dr. Marie-Luise Safranek`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/18OCg2_24d`) (sent_id: `deanon_260716_TRAIN/18OCg2_24d_5`)


Text Begründung: [1] DerKlägerbegehrt mit seiner beim Landesgericht Klagenfurt als Arbeits- und Sozialgericht eingebrachten Klage, das Erkenntnis des Schiedsgerichts der beklagten Glaubensgemeinschaft vom 18.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Klagenfurt`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/18OCg2_24d`) (sent_id: `deanon_260716_TRAIN/18OCg2_24d_18`)


Rechtliche Beurteilung [6] DasLandesgericht Klagenfurtals Arbeits- und Sozialgericht erklärte sich mit Beschluss vom 21.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA10_12x`) (sent_id: `deanon_260716_TRAIN/8ObA10_12x_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Kuras und Mag. Ziegelbauer sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Manuela Majeranowski als weitere Richter in der Arbeitsrechtssache der klagenden Partei Techn R Laurin Tommke, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Zorlex Verlag Gesellschaft mbH, Poeschlstraße 16, 4904 Hippelsberg, Österreich, vertreten durch Mag. Klaus F. Lughofer LLM, Rechtsanwalt in Linz, wegen Feststellung (Streitwert: 30.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. November 2011, GZ 11 Ra 92/11w-10, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 31. August 2011, GZ 11 Cga 101/11d-5, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Spenling`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Mag. Ziegelbauer`(person)
- `Mag. Dr. Rolf Gleißner`(person)
- `Mag. Manuela Majeranowski`(person)
- `Techn R Laurin Tommke`(person)
- `Hasch & Partner Anwaltsgesellschaft mbH`(organisation)
- `Zorlex Verlag Gesellschaft mbH`(organisation)
- `Poeschlstraße 16, 4904 Hippelsberg, Österreich`(address)
- `Mag. Klaus F. Lughofer LLM`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA1_13z`) (sent_id: `deanon_260716_TRAIN/8ObA1_13z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die fachkundigen Laienrichter Dr. Christoph Kainz und Horst Nurschinger als weitere Richter in der Arbeitsrechtssache der klagenden Partei Heinz Hövermann, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, wider die beklagte Partei Verein Alina Siekmann, vertreten durch Dr. Dieter Neger, Rechtsanwalt in Graz, wegen Entlassungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Oktober 2012, GZ 6 Ra 67/12p-12, mit dem über Berufung der klagenden Partei das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 2. Juli 2012, GZ 20 Cga 23/11v-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Spenling`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Christoph Kainz`(person)
- `Heinz Hövermann`(person)
- `Dr. Gerhard Hiebler`(person)
- `Dr. Gerd Grebenjak`(person)
- `Alina Siekmann`(person)
- `Dr. Dieter Neger`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Leoben`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Monika Lanz`(person)
- `Wolfgang Cadilek`(person)
- `Hon.-Prof. Dieter Kovacs`(person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte`(organisation)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/8ObA72_16w`) (sent_id: `deanon_260716_TRAIN/8ObA72_16w_30`)


Die Beklagte habe es unterlassen, rechtzeitig beim Arbeits- und Sozialgericht einen Antrag gemäß § 433 Abs 1 ZPO (§ 15k Abs 2 MSchG) zu stellen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/8ObA72_16w`) (sent_id: `deanon_260716_TRAIN/8ObA72_16w_89`)


3.4Beim Anspruch auf Teilzeitbeschäftigung nach § 15h MSchG ist das Verfahren zur Durchsetzung in § 15k MSchG geregelt. Kommt binnen vier Wochen ab Bekanntgabe (Meldung) keine (innerbetriebliche) Einigung über Dauer und Lage der Teilzeitbeschäftigung zu Stande, so muss der Dienstgeber binnen weiterer zwei Wochen beim zuständigen Arbeits- und Sozialgericht einen Antrag nach § 433 Abs 1 ZPO (zur gütlichen Einigung durch prätorischen Vergleich) stellen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/8ObS12_19a`) (sent_id: `deanon_260716_TRAIN/8ObS12_19a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Sozialrechtssache der klagenden Partei Miranda Tönnesmann, vertreten durch Dr. Christoph Orgler, Rechtsanwalt in Graz, gegen die beklagte Partei IEF-Service GmbH, Geschäftsstelle Graz, 8020 Graz, Europaplatz 12, vertreten durch die Finanzprokuratur, 1010 Wien, Singerstraße 17–19, wegen 3.159 EUR sA (Insolvenz-Entgelt), über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. September 2019, GZ 6 Rs 33/19y-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 6. Mai 2019, GZ 36 Cgs 47/19h-5, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Mag. Thomas Stegmüller`(person)
- `Gerald Fida`(person)
- `Miranda Tönnesmann`(person)
- `Dr. Christoph Orgler`(person)
- `IEF-Service GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/8ObS8_22t`) (sent_id: `deanon_260716_TRAIN/8ObS8_22t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter (Senat gemäß § 11a Abs 3 Z 2 ASGG) in der Sozialrechtssache der klagenden Partei Dipl. Kff. Saskia Claussner, vertreten durch Dr. Herbert Marschitz und andere Rechtsanwälte in Kufstein, gegen die beklagte Partei IEF-Service GmbH, 6020 Innsbruck, Meraner Straße 1, vertreten durch die Finanzprokuratur in Wien, wegen 34.726 EUR sA (Insolvenzentgelt), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Oktober 2022, GZ 25 Rs 56/22d-34, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Juni 2022, GZ 44 Cgs 43/21m-27, samt dem ihm vorangegangenen Verfahren für nichtig erklärt und die Klage zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Stefula`(person)
- `Dipl. Kff. Saskia Claussner`(person)
- `Dr. Herbert Marschitz`(person)
- `IEF-Service GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/9Nc4_10b`) (sent_id: `deanon_260716_TRAIN/9Nc4_10b_6`)


Sie hat nach § 31 JN die Delegation an das Landesgericht Eisenstadt als Arbeits- und Sozialgericht beantragt.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Eisenstadt`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/9ObA112_19i`) (sent_id: `deanon_260716_TRAIN/9ObA112_19i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter (Senat nach § 11a Abs 3 ASGG) in der Arbeitsrechtssache der klagenden und gefährdeten Partei MMag. Timon Mlejnek, vertreten durch Dr. Robert Palka, Rechtsanwalt in Wien, gegen die beklagte Partei und Gegnerin der gefährdeten Partei Norval Technologien GmbH, Eißlgasse 14, 4841 Haag, Österreich, vertreten durch Mag. Kristina Silberbauer, Rechtsanwältin in Wien, wegen Zulassung zur Arbeitsleistung, hier wegen einstweiliger Verfügung, über den Revisionsrekurs der klagenden und gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht in Arbeits- und Sozialrechtssachen vom 14. August 2019, GZ 9 Ra 71/19f-12, mit dem dem Rekurs der klagenden und gefährdeten Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 25. Juni 2019, GZ 9 Cga 30/19s-8, teilweise Folge gegeben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `MMag. Timon Mlejnek`(person)
- `Dr. Robert Palka`(person)
- `Norval Technologien GmbH`(organisation)
- `Eißlgasse 14, 4841 Haag, Österreich`(address)
- `Mag. Kristina Silberbauer`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/9ObA118_18w`) (sent_id: `deanon_260716_TRAIN/9ObA118_18w_4`)


Gabriele Svirak in der Arbeitsrechtssache der klagenden Partei Gertrude Kovacik, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei Hoch-Handel GmbH, Sollach 7, 6671 Gaicht, Österreich, vertreten durch Dr. Helmut Fetz, Dr. Birgit Fetz ua, Rechtsanwälte in Leoben, wegen 500 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. August 2018, GZ 7 Ra 23/18h-12, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 14. Dezember 2017, GZ 23 Cga 75/17x-7, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der klagenden Partei wird zurückgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gabriele Svirak`(person)
- `Gertrude Kovacik`(person)
- `Dr. Gerhard Hiebler`(person)
- `Dr. Gerd Grebenjak`(person)
- `Hoch-Handel GmbH`(organisation)
- `Sollach 7, 6671 Gaicht, Österreich`(address)
- `Dr. Helmut Fetz`(person)
- `Dr. Birgit Fetz`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Leoben`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/9ObA120_19s`) (sent_id: `deanon_260716_TRAIN/9ObA120_19s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mike Scheinpflug, vertreten durch Mag. Martin Wakolbinger, Rechtsanwalt in Enns, gegen die beklagte Partei EnnsValkelKI GmbH, Eckldorf 4z, 8755 Möschitzgraben, Österreich, vertreten durch Mag. Martin Singer, Rechtsanwalt in Schwaz, wegen 7.434,83 EUR sA, über die Revision der beklagten Partei (Revisionsstreitwert: 2.400 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. August 2019, GZ 11 Ra 45/19w-33, mit dem den Berufungen beider Parteien gegen das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 19. Februar 2019, GZ 9 Cga 79/18i-26, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `KR Mag. Paul Kunsky`(person)
- `Harald Kohlruss`(person)
- `Mike Scheinpflug`(person)
- `Mag. Martin Wakolbinger`(person)
- `EnnsValkelKI GmbH`(organisation)
- `Eckldorf 4z, 8755 Möschitzgraben, Österreich`(address)
- `Mag. Martin Singer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/9ObA131_12y`) (sent_id: `deanon_260716_TRAIN/9ObA131_12y_5`)


Gesamtstreitwert 29.396,19 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei (Revisionsrekursinteresse 12.248,88 EUR) gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht in Arbeits- und Sozialrechtssachen vom 26. September 2012, GZ 6 Ra 69/12g-13, womit der Beschluss des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. August 2012, GZ 32 Cga 78/12g-5, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs der klagenden Partei wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/9ObA134_09k`) (sent_id: `deanon_260716_TRAIN/9ObA134_09k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Hradil und Dr. Hopf als weitere Richter in der Arbeitsrechtssache der klagenden Partei Frederike Geschwind, vertreten durch Dr. Andreas Lintl, Rechtsanwalt in Wien, gegen die beklagte Partei Sudbertri Garten AG, Mauerfeldstraße 26, 8753 Dietersdorf, Österreich, vertreten durch die Winkler Reich-Rohrwig Illedits Rechtsanwälte-Partnerschaft in Wien, wegen Kündigungsanfechtung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht in Arbeits- und Sozialrechtssachen vom 14. Oktober 2009, GZ 10 Ra 108/09i-17, womit der Beschluss des Landesgerichts Krems an der Donau als Arbeits- und Sozialgericht vom 13. August 2009, GZ 7 Cga 42/09b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs der klagenden Partei wird gemäß § 526 Abs 2 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Rohrer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hradil`(person)
- `Dr. Hopf`(person)
- `Frederike Geschwind`(person)
- `Dr. Andreas Lintl`(person)
- `Sudbertri Garten AG`(organisation)
- `Mauerfeldstraße 26, 8753 Dietersdorf, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/9ObA18_25z`) (sent_id: `deanon_260716_TRAIN/9ObA18_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Mag. Ziegelbauer als Vorsitzenden, die Hofräte Dr. Hargassner und Dr. Stiefsohn sowie die fachkundigen Laienrichter Mag. Lena Steiger (aus dem Kreis der Arbeitgeber) und Mag. Maria Buhr (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei KzlR Joshua Ballnuweit, vertreten durch Dr. Michael Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Reins Logistik GmbH, Heinrich-Butz-Gasse 63, 2443 Stotzing, Österreich, vertreten durch Dr. Stephan Rainer und Dr. Michael Rück, Rechtsanwälte in Innsbruck, wegen zuletzt 9.053,78 EUR brutto sA und Feststellung (Gesamtstreitwert: 95.473,55 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Februar 2025, GZ 7 Ra 7/25p-28, mit dem das Urteil des Landesgerichts St. Pölten als Arbeits- und Sozialgericht vom 7. November 2024, GZ 27 Cga 41/24f-22, abgeändert wurde den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Hargassner`(person)
- `Dr. Stiefsohn`(person)
- `Mag. Lena Steiger`(person)
- `Mag. Maria Buhr`(person)
- `KzlR Joshua Ballnuweit`(person)
- `Dr. Michael Leitner`(person)
- `Reins Logistik GmbH`(organisation)
- `Heinrich-Butz-Gasse 63, 2443 Stotzing, Österreich`(address)
- `Dr. Stephan Rainer`(person)
- `Dr. Michael`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/9ObA44_11b`) (sent_id: `deanon_260716_TRAIN/9ObA44_11b_5`)


Dr. Wolfgang List, Rechtsanwalt in Wien, wider die beklagte Partei und Gegnerin der gefährdeten Partei Traude Uszpelkat, vertreten durch Dr. J. Pfurtscheller, Dr. Orgler, Mag. Huber, Rechtsanwälte in Innsbruck, wegen Feststellung des Fortbestands eines Arbeitsverhältnisses, in eventu Anfechtung einer Kündigung nach § 105 ArbVG (Streitwert jeweils 31.000 EUR), in eventu 18.957 EUR sA, hier Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der klagenden und gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Rekursgericht in Arbeits- und Sozialrechtssachen vom 24. Februar 2011, GZ 15 Ra 11/11x-15, mit dem infolge Rekurses der klagenden und gefährdeten Partei der Beschluss des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Dezember 2010, GZ 43 Cga 126/10y-8, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wolfgang List`(person)
- `Traude Uszpelkat`(person)
- `Dr. J. Pfurtscheller`(person)
- `Dr. Orgler`(person)
- `Mag. Huber`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/9ObA4_10v`) (sent_id: `deanon_260716_TRAIN/9ObA4_10v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Dr. Hradil und Hon.-Prof. Dr. Kuras sowie die fachkundigen Laienrichter Mag. Eva Pernt und KR Mag. Michaela Haydter als weitere Richter in der Arbeitsrechtssache der klagenden Partei Bruno Milona, vertreten durch Mag. Stefan Weiskopf, Dr. Rainer Kappacher, Rechtsanwälte in Landeck, wider die beklagte Partei Mathilda Bödiker, vertreten durch Greiter, Pegger, Kofler & Partner, Rechtsanwälte in Innsbruck, sowie den Nebenintervenienten auf Seiten der beklagten Partei Hubert Wegmüller, wegen 65.800 EUR sA und Rechnungslegung (Streitwert 6.000 EUR), über die Revision der beklagten Partei (Revisionsinteresse 1.500 EUR) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. November 2009, GZ 15 Ra 96/09v-40, mit dem infolge Berufung beider Parteien das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 29. April 2009, GZ 44 Cga 33/07z-35, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Rohrer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hradil`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Mag. Eva Pernt`(person)
- `KR Mag. Michaela Haydter`(person)
- `Bruno Milona`(person)
- `Mag. Stefan Weiskopf`(person)
- `Dr. Rainer Kappacher`(person)
- `Mathilda Bödiker`(person)
- `Greiter, Pegger, Kofler & Partner, Rechtsanwälte`(organisation)
- `Hubert Wegmüller`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/9ObA4_13y`) (sent_id: `deanon_260716_TRAIN/9ObA4_13y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Werner Rodlauer und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei OSR Mag.a Amber Mittelhäußer, vertreten durch Dr. Susanne Kuen, Rechtsanwältin in Wien, gegen die beklagte Partei Klaussen Metall GmbH, Urlakenstraße 5W, 3912 Kleingöttfritz, Österreich, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen 125.731,44 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. Oktober 2012, GZ 11 Ra 82/12a-74, mit dem das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 31. Juli 2012, GZ 9 Cga 245/08g-70, aufgehoben und die Rechtssache an das Erstgericht zurückverwiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Mag. Robert Brunner`(person)
- `OSR Mag.a Amber Mittelhäußer`(person)
- `Dr. Susanne Kuen`(person)
- `Klaussen Metall GmbH`(organisation)
- `Urlakenstraße 5W, 3912 Kleingöttfritz, Österreich`(address)
- `Fellner Wratzfeld & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Steyr`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/9ObA82_20d`) (sent_id: `deanon_260716_TRAIN/9ObA82_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisions- und Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber (aus dem Kreis der Arbeitgeber) und Angela Taschek (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Marktgemeinde KommR KommR Piedro Leyendecker, vertreten durch Ehrenhöfer & Häusler Rechtsanwälte GmbH in Wiener Neustadt, gegen die beklagte Partei Milena Leinhaas, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, wegen 28.428,01 EUR sA, über den Rekurs und die außerordentliche Revision der klagenden Partei gegen den Beschluss (I.) und das Urteil (II.) des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 22. Juli 2020, GZ 9 Ra 111/19p-25, mit dem das Urteil des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 17. September 2019, GZ 9 Cga 126/18g-21, aus Anlass der Berufung der beklagten Partei hinsichtlich der Rückforderung einer Zahlung als nichtig aufgehoben und die Klage zurückgewiesen wurde und über Berufung der beklagen Partei hinsichtlich des Anspruchs nach dem OrgHG abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird teilweise Folge gegeben und der angefochtene Beschluss des Berufungsgerichts ersatzlos aufgehoben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Mag. Dr. Bernhard Gruber`(person)
- `KommR KommR Piedro Leyendecker`(person)
- `Ehrenhöfer & Häusler Rechtsanwälte GmbH`(organisation)
- `Milena Leinhaas`(person)
- `Kosch & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Ziegelbauer, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Dr. Johannes Pflug und Mag. Manuela Majeranowski in der Arbeitsrechtssache der klagenden Partei VetR Thorsten Overdieck, vertreten durch Dr. August Lahnsteiner, Rechtsanwalt in Ebensee, gegen die beklagte Partei Niehles + Walburg Recycling GmbH, Dr.-Schueller-Straße 13, 4754 Steingreß, Österreich, vertreten durch Hosp, Hegen Rechtsanwaltspartnerschaft in Salzburg, wegen 1.736,22 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 7. Mai 2015, GZ 11 Ra 36/15s-11, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Wels als Arbeits- und Sozialgericht vom 10. Februar 2015, GZ 10 Cga 83/14h-7, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Ziegelbauer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Dr. Johannes Pflug`(person)
- `Mag. Manuela Majeranowski`(person)
- `VetR Thorsten Overdieck`(person)
- `Dr. August Lahnsteiner`(person)
- `Niehles + Walburg Recycling GmbH`(organisation)
- `Dr.-Schueller-Straße 13, 4754 Steingreß, Österreich`(address)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

</details>

---

## `ZMH Planung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d902d176`  
**Description:**
Matches the specific entity 'ZMH Planung GmbH' to ensure full capture.

**Content:**
```
(?<!\w)ZMH\s+Planung\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Waldwil-Daten GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dbd9bb11`  
**Description:**
Matches the specific entity 'Waldwil-Daten GmbH' to ensure full capture.

**Content:**
```
(?<!\w)Waldwil-Daten\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `CQLA Solar Systeme GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a2b9c67a`  
**Description:**
Matches the specific entity 'CQLA Solar Systeme GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(CQLA\s+Solar\s+Systeme\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gneist Consulting Team Wien Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1267affc`  
**Description:**
Matches the specific entity 'Gneist Consulting Team Wien Steuerberatung GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(Gneist\s+Consulting\s+Team\s+Wien\s+Steuerberatung\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Erlacher & Erlacher-Philadelphy Rechtsanwälte` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dece87fd`  
**Description:**
Matches the specific entity 'Erlacher & Erlacher-Philadelphy Rechtsanwälte' to ensure full capture.

**Content:**
```
(?<!\w)(Erlacher\s+&\s+Erlacher-Philadelphy\s+Rechtsanwälte)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FRONTEX` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `57ccd363`  
**Description:**
Matches the organization 'FRONTEX' (European Border and Coast Guard Agency).

**Content:**
```
(?<!\w)FRONTEX(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3a31fc99`  
**Description:**
Matches 'Raiffeisenbank' followed by a location or branch name, stopping at specific delimiters to prevent over-capture. Updated to handle hyphens and specific branch names like 'Feldkirchen-Goldwörth' and trailing spaces.

**Content:**
```
(?<!\w)Raiffeisenbank\s+[A-Za-z\s-]+(?=[\s,.)]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Oberbank` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f1d4451f`  
**Description:**
Matches 'Oberbank' as an organization entity, handling trailing punctuation or spaces.

**Content:**
```
(?<!\w)Oberbank\s*(?:,|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Steuerberatungsgesellschaft KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1a4bf3eb`  
**Description:**
Matches full law firm names ending in 'Steuerberatungsgesellschaft' or 'Steuerberatungsgesellschaft KG' to capture the full entity name including the suffix.

**Content:**
```
(?<!\w)([A-Z][a-zA-Z\s&-]+(?:\s+Steuerberatungsgesellschaft(?:\s+KG)?))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bärje Pharma GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5d93369f`  
**Description:**
Matches the specific entity 'Bärje Pharma GmbH' to ensure full capture.

**Content:**
```
(?<!\w)Bärje\s+Pharma\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lenfeld Leys Sonderegger Rechtsanwälte` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5fce8375`  
**Description:**
Matches the specific entity 'Lenfeld Leys Sonderegger Rechtsanwälte'.

**Content:**
```
(?<!\w)Lenfeld\s+Leys\s+Sonderegger\s+Rechtsanwälte(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Linz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `24f7874d`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Linz' specifically.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Linz)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BergEnergie GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `36a95cca`  
**Description:**
Matches 'BergEnergie GmbH' specifically to capture this organization.

**Content:**
```
(?<!\w)(BergEnergie\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Könning und Wilmesmaier Bau GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `255cf392`  
**Description:**
Matches the specific entity 'Könning und Wilmesmaier Bau GmbH' to ensure full capture.

**Content:**
```
(?<!\w)Könning\s+und\s+Wilmesmaier\s+Bau\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KMG AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4c077bc4`  
**Description:**
Matches the specific entity 'KMG AG' to ensure full capture.

**Content:**
```
(?<!\w)KMG\s+AG(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Standalone` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9b8d3fea`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' as a standalone organization entity, or followed by a location name that is not explicitly listed in specific rules. Updated to explicitly exclude known multi-word location patterns to prevent partial matches like 'Finanzamtes' in 'Finanzamtes Klagenfurt'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?)(?!\s+(?:St\.\s*Johann\s+Tamsweg\s+Zell\s+am\s+See|Neunkirchen\s+Wr\.\s*Neustadt|Neunkirchen\s+Wiener\s*Neustadt|Amstetten\s+Melk\s+Scheibbs|Braunau\s+Ried\s+Schärding|Bruck\s+Eisenstadt\s+Oberwart|Kirchdorf\s+Perg\s+Steyr|Kufstein\s+Schwaz|Wien\s+12/13/14\s+Purkersdorf|Wien\s+2/20/21/22|Wien\s+6/7/15|Baden\s+Mödling|Salzburg-Stadt|Graz-Stadt|Klagenfurt-Stadt|Linz-Stadt|Wels-Stadt|Innsbruck-Stadt|Bregenz-Stadt|Eisenstadt-Stadt|St\.\s*Pölten-Stadt|Villach-Stadt|Dornbirn-Stadt|Leoben-Stadt|Lienz-Stadt|Amstetten-Stadt|Baden-Stadt|Braunau-Stadt|Eferding-Stadt|Feldkirchen-Stadt|Gmunden-Stadt|Hall-Stadt|Horn-Stadt|Kufstein-Stadt|Lustenau-Stadt|Neuhaus-Stadt|Oberwart-Stadt|Perg-Stadt|Ried-Stadt|Schwaz-Stadt|Steyr-Stadt|Telfs-Stadt|Waidhofen-Stadt|Wels-Stadt|Wien-Stadt|Wolfsberg-Stadt|Zell-Stadt|Zwettl-Stadt|Lilienfeld\s+St\.\s*Pölten|Salzburg-Land|Graz-Umgebung|Bregenz|Waldviertel|Innsbruck|Linz|Feldkirch|Salzburg\s+Stadt|Linz\s+Stadt|Wels\s+Stadt|Klagenfurt\s+Stadt|Graz\s+Stadt|Innsbruck\s+Stadt|Bregenz\s+Stadt|Eisenstadt\s+Stadt|St\.\s*Pölten\s+Stadt|Villach\s+Stadt|Dornbirn\s+Stadt|Leoben\s+Stadt|Lienz\s+Stadt|Amstetten\s+Stadt|Baden\s+Stadt|Braunau\s+Stadt|Eferding\s+Stadt|Feldkirchen\s+Stadt|Gmunden\s+Stadt|Hall\s+Stadt|Horn\s+Stadt|Kufstein\s+Stadt|Lustenau\s+Stadt|Neuhaus\s+Stadt|Oberwart\s+Stadt|Perg\s+Stadt|Ried\s+Stadt|Schwaz\s+Stadt|Steyr\s+Stadt|Telfs\s+Stadt|Waidhofen\s+Stadt|Wels\s+Stadt|Wien\s+Stadt|Wolfsberg\s+Stadt|Zell\s+Stadt|Zwettl\s+Stadt|Lilienfeld|Hollabrunn|Schwechat\s+Gerasdorf|Tirol\s+Ost|Gmunden\s+Vöcklabruck|Spittal\s+Villach|Grieskirchen\s+Wels|Steiermark\s+Mitte|für\s+Großbetriebe|für\s+Gebühren|Verkehrsteuern|Glücksspiel|Österreich(?:s)?|für\s+Gebühren|Verkehrsteuern|Glücksspiel|Klagenfurt\s+St\.\s*Veit\s+Wolfsberg|Landeck\s+Reutte|Judenburg\s+Liezen|Gänserndorf\s+Mistelbach|Klagenfurt|Graz|Linz|Salzburg|Innsbruck|Wien|Bregenz|Eisenstadt|St\.\s*Pölten|Villach|Dornbirn|Leoben|Lienz|Amstetten|Baden|Braunau|Eferding|Feldkirchen|Gmunden|Hall|Horn|Kufstein|Lustenau|Neuhaus|Oberwart|Perg|Ried|Schwaz|Steyr|Telfs|Waidhofen|Wels|Wien|Wolfsberg|Zell|Zwettl|Lilienfeld|Hollabrunn|Schwechat|Tirol|Gmunden|Spittal|Grieskirchen|Steiermark|Gänserndorf|Judenburg|Landeck))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 1772 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_75`)


Der Rückstand beim Finanzamt betrage zum 30. Juni 2005 352.000 EUR, bei der beklagen Partei 157.000 EUR.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_424`)


Der Schuldnerin war allerdings ohnehin ihre geradezu hoffnungslose Finanzsituation bekannt (vgl nur die Schreiben vom 7. Juli 2005, Beil ./E und vom 31. August 2005, Beil ./H, an die Banken zur Erreichung des Ausgleichs mit Hinweis ua auf ein negatives Eigenkapital per 30. Juni 2005 und einen Rückstand beim Finanzamt von 352.000 EUR, also auf eine klare Insolvenzsituation).

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_14`)


Die „Erfolgsprämien“ für die ihr für die Jahre 2009 und 2010 vom Finanzamt zuerkannten Forschungsprämien wurden der Klägerin von der Beklagten gezahlt. DieKlägerinerhob aufgrund der Nichtzahlung ihrer die Erfolgsprämie für das Jahr 2011 betreffenden Rechnung vom 7. 12. 2012 am 1. 12. 2015 Klage auf Zahlung von 65.850,37 EUR samt Zinsen.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_36`)


2012 erfolgte die Gutbuchung der Forschungsprämie 2011 auf dem Abgabenkonto der Beklagten durch das Finanzamt.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_37`)


Eine bescheidmäßige Erledigung erfolgt in solchen Fällen nicht, ein Bescheid wird in diesem Zusammenhang vom Finanzamt nur erlassen, wenn die beantragte Forschungsprämie nicht oder nicht zur Gänze gewährt wird.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_52`)


Im Zuge der Betriebsprüfungen durch das Finanzamt war die Klägerin noch zeitweise unterstützend bis in den Oktober 2014 hinein tätig, danach beendete sie ihre Tätigkeit für die Beklagte.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_54`)


Eine Gutbuchung einer Forschungsprämie für das Jahr 2012 durch das Finanzamt erfolgte bis zum Schluss der mündlichen Verhandlung erster Instanz durch das Finanzamt nicht am Abgabenkonto der Beklagten (unbestritten).

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation
- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 7** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_84`)


Das Erstgericht stützte vorliegend seine negative Feststellung – richtig: rechtliche Beurteilung – nun in erster Linie darauf (Ersturteil Seiten 7 f), dass der Geschäftsführer der Beklagten in Gesprächen mit dem Geschäftsführer der Klägerin stets darauf hingewiesen habe, er sei der Meinung, aufgrund der Zurückforderung der Forschungsprämien durch das Finanzamt nichts zu schulden und deshalb die offene Rechnung nicht bezahlen zu können.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_86`)


Gerade letzteres war hier aber nach der genannten (dislozierten) Feststellung der Fall: Der Geschäftsführer der Beklagten erklärte, wegen der Zurückforderung der Forschungsprämie durch das Finanzamt der Klägerin das in Rechnung gestellte Erfolgshonorar nicht bezahlen zu können.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bachkelber-Bildung` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `058dc9dc`  
**Description:**
Matches the specific entity 'Bachkelber-Bildung' as an organisation.

**Content:**
```
(?<!\w)(Bachkelber-Bildung)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stanley Versand GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `225f7d23`  
**Description:**
Matches 'Stanley Versand GmbH' specifically to ensure full capture.

**Content:**
```
(?<!\w)Stanley\s+Versand\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `A-Klinikum GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0dc4ced9`  
**Description:**
Matches 'A-Klinikum GmbH' and 'A-Privatklinikum GmbH' specifically.

**Content:**
```
(?<!\w)(?:A-Klinikum|A-Privatklinikum)\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Vorarlberg` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8073914d`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Vorarlberg'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Vorarlberg)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien 1/23` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1ddca5ac`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Wien 1/23'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Wien\s+1/23)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AT Tax Advisory & Trustee Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cf0454f1`  
**Description:**
Matches 'AT Tax Advisory & Trustee Steuerberatung GmbH' specifically.

**Content:**
```
(?<!\w)AT\s+Tax\s+Advisory\s+&\s+Trustee\s+Steuerberatung\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SOLIDUS Steuerberatungs- und Wirtschaftstreuhand GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c36d13ce`  
**Description:**
Matches 'SOLIDUS Steuerberatungs- und Wirtschaftstreuhand GmbH' specifically.

**Content:**
```
(?<!\w)SOLIDUS\s+Steuerberatungs-\s+und\s+Wirtschaftstreuhand\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Keuler u. Symmat Chemie` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d4b2499c`  
**Description:**
Matches 'Keuler u. Symmat Chemie' specifically.

**Content:**
```
(?<!\w)Keuler\s+u\.\s+Symmat\s+Chemie(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Johann Sch Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6ceaec19`  
**Description:**
Matches 'Johann Sch' as a specific organization entity, often appearing as 'Firma Johann Sch'.

**Content:**
```
(?<!\w)Johann\s+Sch(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FEGA Services Organization` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7aa28a91`  
**Description:**
Matches 'FEGA Services' as a specific organization entity.

**Content:**
```
(?<!\w)FEGA\s+Services(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `NordRecycling Betriebe AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d2882312`  
**Description:**
Matches 'NordRecycling Betriebe AG' as a specific organization entity.

**Content:**
```
(?<!\w)NordRecycling\s+Betriebe\s+AG(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lemtalheim-Energie AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `075c021b`  
**Description:**
Matches 'Lemtalheim-Energie AG' as a specific organization entity.

**Content:**
```
(?<!\w)Lemtalheim-Energie\s+AG(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Nieder\u00f6sterreich Mitte` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6dff139a`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Nieder\u00f6sterreich Mitte'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Nieder\u00f6sterreich\s+Mitte)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Graf & Partner Steuerberatungs- gesellschaft m.b.H.` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6432d6b8`  
**Description:**
Matches 'Graf & Partner Steuerberatungs- gesellschaft m.b.H.' specifically, handling the hyphenation and spacing.

**Content:**
```
(?<!\w)Graf\s+&\s+Partner\s+Steuerberatungs-\s+gesellschaft\s+m\.b\.H\.(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Graz-Umgebung` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a4e591ca`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Graz-Umgebung'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Graz-Umgebung)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gambi Luftfahrt GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `93426bfa`  
**Description:**
Matches the specific entity 'Gambi Luftfahrt GmbH'.

**Content:**
```
(?<!\w)(Gambi\s+Luftfahrt\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Weber Harrer Rechtsanwälte GmbH & Co KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a110d29d`  
**Description:**
Matches the specific entity 'Weber Harrer Rechtsanwälte GmbH & Co KG' to ensure full capture.

**Content:**
```
(?<!\w)(Weber\s+Harrer\s+Rechtsanwälte\s+GmbH\s+&\s+Co\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `3Partner Steuerberatung OG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f63d53e9`  
**Description:**
Matches the specific entity '3Partner Steuerberatung OG' to ensure full capture.

**Content:**
```
(?<!\w)(3Partner\s+Steuerberatung\s+OG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `B & S Steuer- und Unternehmensberatungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b7b49db4`  
**Description:**
Matches the specific entity 'B & S Steuer- und Unternehmensberatungs GmbH' to ensure full capture.

**Content:**
```
(?<!\w)(B\s+&\s+S\s+Steuer-\s+und\s+Unternehmensberatungs\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Eckhardt Wirtschaftsprüfung u SteuerberatungsgmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0d1eb5c3`  
**Description:**
Matches the specific entity 'Eckhardt Wirtschaftsprüfung u SteuerberatungsgmbH' to ensure full capture.

**Content:**
```
(?<!\w)(Eckhardt\s+Wirtschaftsprüfung\s+u\s+SteuerberatungsgmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dr. Obermoser Wirtschaftstreuhand GmbH, Steuerberatungsgesellschaft` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `39139b38`  
**Description:**
Matches the specific entity 'Dr. Obermoser Wirtschaftstreuhand GmbH, Steuerberatungsgesellschaft' to ensure full capture.

**Content:**
```
(?<!\w)(Dr\.\s+Obermoser\s+Wirtschaftstreuhand\s+GmbH,?\s+Steuerberatungsgesellschaft)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Grieskirchen Wels` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e3754771`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Grieskirchen Wels' specifically, ensuring the full location is captured and preventing partial matches.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Grieskirchen\s+Wels)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `LG Abbreviation Court` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `16fcb9f6`  
**Description:**
Matches the abbreviation 'LG' (Landesgericht) followed by a location or case number context, ensuring it is treated as an organization.

**Content:**
```
(?<!\w)(LG)(?:\s+[A-Z][a-zA-Z\-]+(?:\s+[A-Z][a-zA-Z\-]+)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 3 | 1535 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/4Ob68_14z`) (sent_id: `deanon_260716_TRAIN/4Ob68_14z_21`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `LG Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Innsbruck`(organisation)
- `Oberlandesgericht Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/6Ob182_20p`) (sent_id: `deanon_260716_TRAIN/6Ob182_20p_40`)


Dieser Auffassung hat sich zwischenzeitig bereits zweitinstanzliche Rechtsprechung ausdrücklich (vgl etwa LG Salzburg EFSlg 156.701 [2018], 159.791, 159.792 [2019];

**False Positives:**

- `LG Salzburg EFSlg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob182_20p`) (sent_id: `deanon_260716_TRAIN/6Ob182_20p_41`)


LG Linz EFSlg 156.702 [2018], 159.793 [2019]) und die Entscheidung 9 Ob 57/17y offensichtlich angeschlossen.

**False Positives:**

- `LG Linz EFSlg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bundesfinanzgericht with Location` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `87b3c89f`  
**Description:**
Matches 'Bundesfinanzgericht' followed by location details like 'Außenstelle' or specific addresses, capturing the full entity name but stopping strictly before non-location text.

**Content:**
```
(?<!\w)(Bundesfinanzgericht(?:\s+(?:Außenstelle|Zweigstelle|Standort)\s+[A-Z][a-zA-Z\s-]+))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt Wien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5cd03cb3`  
**Description:**
Matches 'Magistrat' or 'Magistrats' with 'der Stadt Wien' WITHOUT department info. STRICTLY excludes department info (Magistratsabteilung/MA) to prevent over-capture by the higher priority rule.

**Content:**
```
(?<!\w)(Magistrat(?:es)?\s+der\s+Stadt\s+Wien)(?!\s+Magistratsabteilung|\s+MA\s+\d+|\s+Abteilung|\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Innsbruck` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3915ffd2`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Innsbruck', handling genitive forms and ensuring the full location is captured.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Innsbruck)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Bregenz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9cef19f8`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed strictly by 'Bregenz', ensuring the full entity is captured and preventing partial matches.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Bregenz)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kohl-Verlag` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `01dd722c`  
**Description:**
Matches the specific entity 'Kohl-Verlag' as an organisation.

**Content:**
```
(?<!\w)Kohl-Verlag(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Waldviertel` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9191141c`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Waldviertel' specifically.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Waldviertel)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Tirol Ost` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `31d250e0`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Tirol Ost'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Tirol\s+Ost)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Freistadt Rohrbach Urfahr` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a8eb3008`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Freistadt Rohrbach Urfahr'.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Freistadt\s+Rohrbach\s+Urfahr)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg-Land` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `30a8dc9d`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Salzburg-Land' specifically to ensure the hyphenated location is captured fully.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Salzburg-Land)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Abbreviation with Location (Extended)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c0b500a9`  
**Description:**
Matches 'FA' followed by known locations including 'Tirol Ost', 'Freistadt Rohrbach Urfahr', 'Salzburg-Land', and others, ensuring full capture.

**Content:**
```
(?<!\w)(FA\s+(?:Tirol\s+Ost|Freistadt\s+Rohrbach\s+Urfahr|Salzburg-Land|Wien\s+(?:\d+(?:/\d+)*|\d+\s+\d+)|Steiermark\s+Mitte|Braunau\s+Ried|Salzburg\s+Stadt|Salzburg\s+Land|Österreich|Innsbruck|Linz|Graz|Klagenfurt|Villach|Bregenz|Feldkirch|Wels|Linz\s+Stadt|Graz\s+Stadt|Innsbruck\s+Stadt|Bregenz\s+Stadt|Eisenstadt\s+Stadt|St\.\s*P\u00f6lten\s+Stadt|Villach\s+Stadt|Dornbirn\s+Stadt|Leoben\s+Stadt|Lienz\s+Stadt|Amstetten\s+Stadt|Baden\s+Stadt|Braunau\s+Stadt|Eferding\s+Stadt|Feldkirchen\s+Stadt|Gmunden\s+Stadt|Hall\s+Stadt|Horn\s+Stadt|Kufstein\s+Stadt|Lustenau\s+Stadt|Neuhaus\s+Stadt|Oberwart\s+Stadt|Perg\s+Stadt|Ried\s+Stadt|Schwaz\s+Stadt|Steyr\s+Stadt|Telfs\s+Stadt|Waidhofen\s+Stadt|Wels\s+Stadt|Wien\s+Stadt|Wolfsberg\s+Stadt|Zell\s+Stadt|Zwettl\s+Stadt|Lilienfeld\s+St\.\s*P\u00f6lten|Hollabrunn|Schwechat\s+Gerasdorf|Tirol\s+Ost|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Judenburg\s+Liezen|Klagenfurt\s+St\.\s*Veit\s+Wolfsberg|Landeck\s+Reutte|Baden\s+M\u00f6dling|Amstetten\s+Melk\s+Scheibbs|Neunkirchen\s+Wr\.\s*Neustadt|Neunkirchen\s+Wiener\s*Neustadt|St\.\s*Johann\s+Tamsweg\s+Zell\s+am\s+See|Bruck\s+Eisenstadt\s+Oberwart|Kirchdorf\s+Perg\s+Steyr|Kufstein\s+Schwaz|Wien\s+12/13/14\s+Purkersdorf|Wien\s+2/20/21/22|Wien\s+6/7/15|Wien\s+9/18/19\s+Klosterneuburg|Braunau\s+Ried\s+Sch\u00e4rding|Salzburg-Stadt|Graz-Stadt|Klagenfurt-Stadt|Linz-Stadt|Wels-Stadt|Innsbruck-Stadt|Bregenz-Stadt|Eisenstadt-Stadt|St\.\s*P\u00f6lten-Stadt|Villach-Stadt|Dornbirn-Stadt|Leoben-Stadt|Lienz-Stadt|Amstetten-Stadt|Baden-Stadt|Braunau-Stadt|Eferding-Stadt|Feldkirchen-Stadt|Gmunden-Stadt|Hall-Stadt|Horn-Stadt|Kufstein-Stadt|Lustenau-Stadt|Neuhaus-Stadt|Oberwart-Stadt|Perg-Stadt|Ried-Stadt|Schwaz-Stadt|Steyr-Stadt|Telfs-Stadt|Waidhofen-Stadt|Wels-Stadt|Wien-Stadt|Wolfsberg-Stadt|Zell-Stadt|Zwettl-Stadt|Lilienfeld\s+St\.\s*P\u00f6lten|Salzburg-Land|Graz-Umgebung|Bregenz|Waldviertel|Innsbruck|Linz|Feldkirch|Salzburg\s+Stadt|Linz\s+Stadt|Wels\s+Stadt|Klagenfurt\s+Stadt|Graz\s+Stadt|Innsbruck\s+Stadt|Bregenz\s+Stadt|Eisenstadt\s+Stadt|St\.\s*P\u00f6lten\s+Stadt|Villach\s+Stadt|Dornbirn\s+Stadt|Leoben\s+Stadt|Lienz\s+Stadt|Amstetten\s+Stadt|Baden\s+Stadt|Braunau\s+Stadt|Eferding\s+Stadt|Feldkirchen\s+Stadt|Gmunden\s+Stadt|Hall\s+Stadt|Horn\s+Stadt|Kufstein\s+Stadt|Lustenau\s+Stadt|Neuhaus\s+Stadt|Oberwart\s+Stadt|Perg\s+Stadt|Ried\s+Stadt|Schwaz\s+Stadt|Steyr\s+Stadt|Telfs\s+Stadt|Waidhofen\s+Stadt|Wels\s+Stadt|Wien\s+Stadt|Wolfsberg\s+Stadt|Zell\s+Stadt|Zwettl\s+Stadt|Lilienfeld\s+St\.\s*P\u00f6lten|Hollabrunn|Schwechat\s+Gerasdorf|Tirol\s+Ost|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Grieskirchen\s+Wels|Steiermark\s+Mitte|Klagenfurt\s+St\.\s*Veit\s+Wolfsberg|Landeck\s+Reutte|Judenburg\s+Liezen|Purkersdorf))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b22eb1fd`  
**Description:**
Matches the abbreviation FA (Finanzamt) followed by specific known locations, excluding 'Österreich' (handled by specific rules) and preventing over-capture of 'Finanzamtes' genitive forms or compound names.

**Content:**
```
(?<!\w)(FA\s+(?:Wien\s+(?:\d+(?:/\d+)*|\d+\s+\d+)|Steiermark\s+Mitte|Braunau\s+Ried|Salzburg\s+Stadt|Salzburg\s+Land|Innsbruck|Linz|Graz|Klagenfurt|Villach|Bregenz|Dornbirn|Feldkirch|Wels|Linz\s+Stadt|Graz\s+Stadt|Innsbruck\s+Stadt|Bregenz\s+Stadt|Eisenstadt\s+Stadt|St\.\s*P\u00f6lten\s+Stadt|Villach\s+Stadt|Dornbirn\s+Stadt|Leoben\s+Stadt|Lienz\s+Stadt|Amstetten\s+Stadt|Baden\s+Stadt|Braunau\s+Stadt|Eferding\s+Stadt|Feldkirchen\s+Stadt|Gmunden\s+Stadt|Hall\s+Stadt|Horn\s+Stadt|Kufstein\s+Stadt|Lustenau\s+Stadt|Neuhaus\s+Stadt|Oberwart\s+Stadt|Perg\s+Stadt|Ried\s+Stadt|Schwaz\s+Stadt|Steyr\s+Stadt|Telfs\s+Stadt|Waidhofen\s+Stadt|Wels\s+Stadt|Wien\s+Stadt|Wolfsberg\s+Stadt|Zell\s+Stadt|Zwettl\s+Stadt|Lilienfeld\s+St\.\s*P\u00f6lten|Hollabrunn|Schwechat\s+Gerasdorf|Tirol\s+Ost|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Judenburg\s+Liezen|Klagenfurt\s+St\.\s*Veit\s+Wolfsberg|Landeck\s+Reutte|Baden\s+M\u00f6dling|Amstetten\s+Melk\s+Scheibbs|Neunkirchen\s+Wr\.\s*Neustadt|Neunkirchen\s+Wiener\s*Neustadt|St\.\s*Johann\s+Tamsweg\s+Zell\s+am\s+See|Bruck\s+Eisenstadt\s+Oberwart|Kirchdorf\s+Perg\s+Steyr|Kufstein\s+Schwaz|Wien\s+12/13/14\s+Purkersdorf|Wien\s+2/20/21/22|Wien\s+6/7/15|Wien\s+9/18/19\s+Klosterneuburg|Braunau\s+Ried\s+Sch\u00e4rding|Salzburg-Stadt|Graz-Stadt|Klagenfurt-Stadt|Linz-Stadt|Wels-Stadt|Innsbruck-Stadt|Bregenz-Stadt|Eisenstadt-Stadt|St\.\s*P\u00f6lten-Stadt|Villach-Stadt|Dornbirn-Stadt|Leoben-Stadt|Lienz-Stadt|Amstetten-Stadt|Baden-Stadt|Braunau-Stadt|Eferding-Stadt|Feldkirchen-Stadt|Gmunden-Stadt|Hall-Stadt|Horn-Stadt|Kufstein-Stadt|Lustenau-Stadt|Neuhaus-Stadt|Oberwart-Stadt|Perg-Stadt|Ried-Stadt|Schwaz-Stadt|Steyr-Stadt|Telfs-Stadt|Waidhofen-Stadt|Wels-Stadt|Wien-Stadt|Wolfsberg-Stadt|Zell-Stadt|Zwettl-Stadt|Lilienfeld\s+St\.\s*P\u00f6lten|Salzburg-Land|Graz-Umgebung|Bregenz|Waldviertel|Innsbruck|Linz|Feldkirch|Salzburg\s+Stadt|Linz\s+Stadt|Wels\s+Stadt|Klagenfurt\s+Stadt|Graz\s+Stadt|Innsbruck\s+Stadt|Bregenz\s+Stadt|Eisenstadt\s+Stadt|St\.\s*P\u00f6lten\s+Stadt|Villach\s+Stadt|Dornbirn\s+Stadt|Leoben\s+Stadt|Lienz\s+Stadt|Amstetten\s+Stadt|Baden\s+Stadt|Braunau\s+Stadt|Eferding\s+Stadt|Feldkirchen\s+Stadt|Gmunden\s+Stadt|Hall\s+Stadt|Horn\s+Stadt|Kufstein\s+Stadt|Lustenau\s+Stadt|Neuhaus\s+Stadt|Oberwart\s+Stadt|Perg\s+Stadt|Ried\s+Stadt|Schwaz\s+Stadt|Steyr\s+Stadt|Telfs\s+Stadt|Waidhofen\s+Stadt|Wels\s+Stadt|Wien\s+Stadt|Wolfsberg\s+Stadt|Zell\s+Stadt|Zwettl\s+Stadt|Lilienfeld\s+St\.\s*P\u00f6lten|Hollabrunn|Schwechat\s+Gerasdorf|Tirol\s+Ost|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Grieskirchen\s+Wels|Steiermark\s+Mitte|Klagenfurt\s+St\.\s*Veit\s+Wolfsberg|Landeck\s+Reutte|Judenburg\s+Liezen|Purkersdorf))(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag. Thonhauser Steuerberater GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c2d4adbc`  
**Description:**
Matches the specific entity 'Mag. Thonhauser Steuerberater GmbH' to ensure full capture.

**Content:**
```
(?<!\w)Mag\.\s*Thonhauser\s*Steuerberater\s*GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFP Wirtschaftsprüfungs- u STB GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `59f62bc7`  
**Description:**
Matches the specific entity 'BFP Wirtschaftsprüfungs- u STB GmbH' to ensure full capture.

**Content:**
```
(?<!\w)BFP\s*Wirtschaftspr\u00fcfungs-\s*u\s*STB\s*GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ERNST & YOUNG Wirtschaftsprüfungs und Steuerberatungs GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6d60627d`  
**Description:**
Matches the specific entity 'ERNST & YOUNG Wirtschaftsprüfungs und Steuerberatungs GmbH' variants including spacing.

**Content:**
```
(?<!\w)ERNST\s*&\s*YOUNG\s*Wirtschaftspr\u00fcfungs\s+und\s+Steuerberatungs\s*GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4cd39546`  
**Description:**
Matches the specific entity 'smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung GmbH' to ensure full capture.

**Content:**
```
(?<!\w)smc\s*Steirer\s*Mika\s*&\s*Comp\.\s*Wirtschaftspr\u00fcfung\s*Steuerberatung\s*GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien 2/20/21/22` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d24b194b`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Wien 2/20/21/22' specifically.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Wien\s+2/20/21/22)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Enns-Holz Betriebe GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c588b31f`  
**Description:**
Matches 'Enns-Holz Betriebe GmbH' specifically to ensure it is captured in all contexts.

**Content:**
```
(?<!\w)(Enns-Holz\s+Betriebe\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Gemeinderat` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e353d768`  
**Description:**
Matches 'Wiener Gemeinderat' and its genitive form, ensuring it is not a false positive in non-entity contexts by requiring specific context or being at the start of a sentence/phrase.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[)(Wiener\s+Gemeinderat(?:es)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Gemeinderates` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `68caa739`  
**Description:**
Matches 'Wiener Gemeinderat' and its genitive form 'Wiener Gemeinderates' as an organisation.

**Content:**
```
(?<!\w)(Wiener\s+Gemeinderat(?:es)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Diezelmüller Pflege GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `aebb884a`  
**Description:**
Matches 'Diezelmüller Pflege GmbH' and its variant with 'Fa.' prefix to ensure it is captured in all contexts.

**Content:**
```
(?<!\w)(?:Fa\.)?Diezelmüller\s+Pflege\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TalBachvertraSoftware Services GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f15d180d`  
**Description:**
Matches 'TalBachvertraSoftware Services GmbH' to ensure it is captured even when not preceded by 'Firmen'.

**Content:**
```
(?<!\w)TalBachvertraSoftware\s+Services\s+GmbH(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Period-Prefixed GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6d816439`  
**Description:**
Matches company names ending in GmbH that are preceded by a period (e.g., '.Valwerk GmbH'), capturing the full entity including the period.

**Content:**
```
(?<!\w)(\.\s*[A-Z][a-zA-Z0-9\-]+(?:\s+[A-Z][a-zA-Z0-9\-]+)*\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Period-Prefixed KG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `87323524`  
**Description:**
Matches company names ending in KG that are preceded by a period (e.g., '.Mur Verwerkwil KG'), capturing the full entity including the period.

**Content:**
```
(?<!\w)(\.\s*[A-Z][a-zA-Z0-9\s&\-]+\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dreismickenbecker Logistik GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5165b0d3`  
**Description:**
Matches 'Dreismickenbecker Logistik GmbH' specifically to ensure it is captured.

**Content:**
```
(?<!\w)(Dreismickenbecker\s+Logistik\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Freiert Garten GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2a24dfb7`  
**Description:**
Matches 'Freiert Garten GmbH' specifically to ensure it is captured.

**Content:**
```
(?<!\w)(Freiert\s+Garten\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisen Digital Bank` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f9d63b22`  
**Description:**
Matches 'Raiffeisen Digital Bank' specifically to ensure it is captured.

**Content:**
```
(?<!\w)(Raiffeisen\s+Digital\s+Bank)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `de6821fb`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Salzburg' or 'Salzburg-Land' ONLY if NOT followed by 'Stadt' or 'Land' (which are handled by specific rules). Updated to ensure '-Land' is captured if present.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Salzburg(?:-Land)?)(?!\s+(?:Stadt|\w))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lebensmittel Zorder GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1c3ac1f5`  
**Description:**
Matches the specific entity 'Lebensmittel Zorder GmbH' to ensure it is captured.

**Content:**
```
(?<!\w)(Lebensmittel\s+Zorder\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stb. & Partner GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c5f4e2fe`  
**Description:**
Matches 'Stb. & Partner' followed by 'Wirtschaftsprüfungs- und Steuerberatungs GmbH' or similar variants, including cases with 'Fa.' prefix and optional '(KPMG)' suffix.

**Content:**
```
(?<!\w)(?:Fa\.\s+)?(Stb\.\s+&\s+Partner\s+(?:Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungs\s+GmbH|WP-\s+und\s+Stb\.\s+GmbH)(?:\s*\(KPMG\))?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hendlmaier Möbel AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `eb66eb71`  
**Description:**
Matches the specific entity 'Hendlmaier Möbel AG' to ensure it is captured.

**Content:**
```
(?<!\w)(Hendlmaier\s+M\u00f6bel\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mikloweit Bau AG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e2491ec4`  
**Description:**
Matches the specific entity 'Mikloweit Bau AG' to ensure it is captured.

**Content:**
```
(?<!\w)(Mikloweit\s+Bau\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `X GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `06602add`  
**Description:**
Matches 'X GmbH' as a placeholder or specific entity, ensuring it is captured even if it's a generic placeholder.

**Content:**
```
(?<!\w)(X\s+GmbH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Riegerl` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2fe324f3`  
**Description:**
Matches 'Riegerl' as a specific organization entity (likely a firm name in context).

**Content:**
```
(?<!\w)(Riegerl)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verfassungsgerichtshof/Verwaltungsgerichtshof Compound` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4ac9ed6a`  
**Description:**
Matches the compound entity 'Verfassungsgerichtshof/Verwaltungsgerichtshof' as a single organisation.

**Content:**
```
(?<!\w)(Verfassungsgerichtshof(?:es|s)?/Verwaltungsgerichtshof(?:es|s)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt Wien, Magistratsabteilung 67` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `45e12c2d`  
**Description:**
Matches the specific full entity 'Magistrat der Stadt Wien, Magistratsabteilung 67' to ensure the full name including the department is captured as a single entity.

**Content:**
```
(?<!\w)(Magistrat\s+der\s+Stadt\s+Wien,\s+Magistratsabteilung\s+67)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgerichtes Standalone` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ee1d0c9c`  
**Description:**
Matches 'Landesgerichtes' or 'Landesgericht' as a standalone organization entity, even without a following location name.

**Content:**
```
(?<!\w)(Landesgericht(?:es)?)(?!\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 470 | 0 | 470 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 470 | 3995 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgericht Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Landesgericht Linz`(organisation)
- `Hollengk Planung GmbH`(organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich`(address)
- `Huber Berchtold Rechtsanwälte OG`(organisation)
- `Wind Nexheimval GmbH`(organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich`(address)
- `ScherbaumSeebacher Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Linz`(organisation)
- `Landesgericht Korneuburg`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Linz`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_30`)


Zwar ist das Bauvorhaben im Sprengel des Landesgerichts Korneuburg situiert.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Korneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Korneuburg`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Linz`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_10`)


Die Klägerin stützte die Zuständigkeit des von ihr angerufenen Landesgerichts Wr. Neustadt als Handelsgericht auf § 88 Abs 1 und 2 JN.

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_11`)


Für den Fall der örtlichen Unzuständigkeit des angerufenen Gerichts beantragte die Klägerin gemäß § 28 JN die Bestimmung des Landesgerichts Wr. Neustadt als Handelsgericht als für den gegenständlichen Rechtsstreit örtlich zuständiges Gericht.

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgericht Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Landesgericht Linz`(organisation)
- `Steidlen+Ysner Daten GmbH`(organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich`(address)
- `Dr. Roland Kassowitz`(person)
- `Verlag Waldlemder GmbH`(organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich`(address)
- `Prof. Haslinger`(person)
- `Landesgerichts Linz`(organisation)
- `Handelsgericht Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mur Dorftalnex Technologien -GmbH`(organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich`(address)
- `Dr. Peter Lechner`(person)
- `Dr. Hermann Pfurtscheller`(person)
- `Ober Dertri GmbH`(organisation)
- `Hintereggweg 93, 2070 Kleinhöflein, Österreich`(address)
- `Dr. Thomas Girardi`(person)
- `Rudolf Ketelhut`(person)
- `Fiebrichgasse 17, 5120 Seeleiten, Österreich`(address)
- `Dr. Bernhard Hämmerle GmbH`(organisation)
- `Völkertz Energie GmbH`(organisation)
- `Brunnbachweg 19, 4653 Mayersdorf, Österreich`(address)
- `Dr. Franz Pechmann`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Stefula`(person)
- `Schneidergruberweg 37, 5132 Reith, Österreich`(address)
- `Dr. Alois Schneider`(person)
- `Dario von Ebers`(person)
- `Dr. Walter Hausberger`(person)
- `Dr. Katharina Moritz`(person)
- `Dr. Alfred Schmidt`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Rattenberg`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Bartholomäus Junghahn`(person)
- `HR Sophie Elefteriadis`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Juri Gerstl`(person)
- `Mutten 18, 3251 Schauboden, Österreich`(address)
- `Dr. Ralph Trischler`(person)
- `Bundesbeschaffung GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Leander Lindlahr`(person)
- `Yussuf Prussog`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Ziegelbauer`(person)
- `Cedric Annamüller`(person)
- `8. März`(date)
- `16. Mai 1964`(date)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Wels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Ludmilla von Amelunxen`(person)
- `Dr. Bernhard Birek`(person)
- `Svetlana Leinhäuser`(person)
- `Dr. Thomas Brückl`(person)
- `Mag. Christian Breit`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Ziegelbauer`(person)
- `Mag. Kevin Maassen`(person)
- `Dr. Clemens Lintschinger`(person)
- `Hon.-Prof. Friedhelm Adde`(person)
- `Mag. Dr. Georg Backhausen`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Wels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Anita Schetzel`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Wels`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Steger`(person)
- `Dr. Annerl`(person)
- `Dr. Wallner-Friedl`(person)
- `Ralph Prusseit`(person)
- `Mag. Franz Eckl`(person)
- `Akbayrak Metall GmbH`(organisation)
- `Schroateck 57, 4710 Niederweng, Österreich`(address)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)
- `Bezirksgerichts Zwettl`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Annabelle Thurnher`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `DDr.in Cornelia Rinaldo`(person)
- `Dr. Sven Rudolf Thorstensen`(person)
- `Conmon-Verlag Limited`(organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich`(address)
- `Brandl Talos Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Malik Schoch`(person)
- `7. November`(date)
- `7. Juli 2025`(date)
- `10. Juli`(date)
- `Alan Schindlmair`(person)
- `7. August`(date)
- `Mag. Florian Kucera`(person)
- `Mag. Timon Schönswetter`(person)
- `Doschek Rechtsanwalts GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Döbling`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns-Umwelt`(organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich`(address)
- `Ing. Lara Markart`(person)
- `Radel Stampf Supper Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_10`)


2008 erfolgte die Eintragung beim Firmenbuch des Landesgerichts Eisenstadt mit einer Niederlassung in Angyalföldstraße 52, 4193 Hayrl, Österreich.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Eisenstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Eisenstadt`(organisation)
- `Angyalföldstraße 52, 4193 Hayrl, Österreich`(address)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lars Ballogh`(person)
- `Mag. Anton Bohmert`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Alver GmbH`(organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich`(address)
- `Dr. Michael Schneditz-Bolfras`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Brigitte Martz`(person)
- `16. November 1978`(date)
- `Dr. Gustav Thöning`(person)
- `Pieler & Pieler & Partner KG`(organisation)
- `Dr. Madeleine Musialik`(person)
- `Kosch & Partner Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)
- `Bezirksgerichts Wiener Neustadt`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_6`)


11. 2008, GZ 38 Nc 13/08i-2, den Ablehnungsantrag des Mag. Herwig Berkenbrink in dessen Rekurs gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 13.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Herwig Berkenbrink`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Jaden Meyerjohann`(person)
- `3. Juli 2020`(date)
- `Leroy Jungschmidt`(person)
- `28. Mai 1965`(date)
- `Clemens Theocharakis`(person)
- `25. März 1999`(date)
- `Emanuela Janischefsky`(person)
- `Bezirkshauptmannschaft Feldkirch`(organisation)
- `Ashley Biesert`(person)
- `Mag. Hans-Christian Obernberger`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Feldkirch`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Korneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Karsten Alberter`(person)
- `2. April 2010`(date)
- `Helmut Dreilich`(person)
- `Landesgerichts Korneuburg`(organisation)
- `Bezirksgerichts Schwechat`(organisation)
- `Lena Amini`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Maja Dolleschell`(person)
- `14. August`(date)
- `Bezirkshauptmannschaft Melk`(organisation)
- `Landesgerichts St. Pölten`(organisation)
- `Bezirksgerichts Melk`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Mag. Johannes Bügler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Dr. Wallner-Friedl`(person)
- `Karim Mielewczik`(person)
- `Dr. Sandro Gädecken`(person)
- `Ing. Dr. Stefan Krall`(person)
- `Dr. Oliver Kühnl`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Seekirchen`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Maja Pirkmayr`(person)
- `Dr. Georg Gorton`(person)
- `DDr. Birgit Gorton`(person)
- `Ing. Emanuel Puff`(person)
- `Dr. Gottfried Kassin`(person)
- `Landesgerichts Klagenfurt`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Dr. Annerl`(person)
- `Meinrad Bruhnsen`(person)
- `30. Januar`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `DI Dr. Bodo Kaczynski`(person)
- `25. Juli 1975`(date)
- `Mag. Werner Thurner`(person)
- `Wolfgang Lombardini`(person)
- `4. Dezember 2022`(date)
- `Livia Löblein`(person)
- `11. Januar 1966`(date)
- `Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Graz-Ost`(organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Felix Cornils`(person)
- `Tramposch & Partner, Rechtsanwälte KG`(organisation)
- `Mag.a Constanze Rizzo`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Emma Mittelstaedt`(person)
- `21. Mai 2025`(date)
- `Milena Roesche`(person)
- `25. Juni 1957`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Othmar Mertl`(person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG`(organisation)
- `Malik Fridt`(person)
- `Krist Bubits Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_9`)


Im Rahmen seiner Äußerung zu diesem Unterhaltserhöhungsantrag lehnte der Antragsgegner jeweils alle Richter des Bezirksgerichts Josefstadt und des diesem übergeordneten Landesgerichts für Zivilrechtssachen Wien ab.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Josefstadt`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_12`)


Da mehrere Senate des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht an dem genannten Verhalten beteiligt gewesen seien, sei auch das gesamte Landesgericht für Zivilrechtssachen Wien als befangen anzusehen, über den nunmehr geltend gemachten Unterhaltsanspruch zu entscheiden.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgericht Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Josefstadt`(organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mikolaj Eleftheriadou`(person)
- `Helge Schuchmann`(person)
- `Isabel Rahnfeld`(person)
- `PhD Daniel Coutand`(person)
- `Mag. Dirk Hükelheim`(person)
- `Mag. Roland Marko`(person)
- `Dr. Francisco Rumpf`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Dr. Weber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Agatha von der Heide`(person)
- `MMag. Dr. Sebastian Pribas`(person)
- `Mag. Benedikt Walch`(person)
- `Alva Sengül`(person)
- `Selina Birkmeir`(person)
- `Harald Ladwig, LLM`(person)
- `In der Klaus 72, 4785 Bach, Österreich`(address)
- `Mag. German Bertsch`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Feldkirch`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Ing. Christian Stangl-Brachnik, MA BA`(person)
- `Mag. Claudia Gründel`(person)
- `Mathias Jendl`(person)
- `Dr. Thomas Stampfer`(person)
- `Dr. Christoph Orgler`(person)
- `Dr. Michael Stögerer`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_12`)


Mit Beschluss des Landesgerichts für Strafsachen Graz vom 18.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_14`)


Mit Urteil des Landesgerichts für Strafsachen Graz vom 14. 12. 2016, 222 Hv 68/16m, wurde er gemäß § 21 Abs 1 StGB in eine Anstalt für geistig abnorme Rechtsbrecher eingewiesen, wo er seit 20.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Gabriele Griehsel`(person)
- `Dr. Wolfgang Kozak`(person)
- `Roland Soukup`(person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mag. Dr. Wolfgang Höfle`(person)
- `Ing. Thomas Bauer`(person)
- `Willibald Kollowrat, BEd`(person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH`(organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau`(organisation)
- `Dr. Marie-Luise Safranek`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Zehetner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Oshidari`(person)
- `Dr. Parapatits`(person)
- `Bernhard Buddäus`(person)
- `Norbert Wehrhahn`(person)
- `Landesgerichts Salzburg`(organisation)
- `Mag. Höpler`(person)
- `Mag. Rienmüller`(person)

**Example 48** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Zehetner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Sommer`(person)
- `Richard Lindt`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wurde die von Richard Lilienfein erhobene Nichtigkeitsbeschwerde gegen das Urteil des Landesgerichts Salzburg vom 17. Juni 2011, GZ 40 Hv 147/10g-538, als unzulässig zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Richard Lilienfein`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_8`)


Die von Richard Leissner gegen das ihn freisprechende Urteil des Einzelrichters des Landesgerichts Salzburg vom 17. Juni 2011 ausdrücklich an den Obersten Gerichtshof gerichtete Nichtigkeitsbeschwerde wurde vom Erstgericht zutreffend gemäß § 285a Z 1 StPO als unzulässig zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Richard Leissner`(person)
- `Landesgerichts Salzburg`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Zehetner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Oshidari`(person)
- `Mag. Kurzthaler`(person)
- `Andreas Schiessl`(person)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Mag. Fürnkranz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oberressl`(person)
- `Mag. Rathgeb`(person)
- `Daniel Kur`(person)
- `Landesgerichts Innsbruck`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oberressl`(person)
- `Mag. Wieser`(person)
- `Gerald Winand`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Korneuburg`(organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Gerald Wandscheer`(person)
- `Landesgerichts Korneuburg`(organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`
- `Landesgericht` — similar text (different position): `Landesgerichts für Strafsachen Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Herwig Bäseke`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)
- `OGH`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)
- `Mag. Herwig Berto`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Herwig Bleuler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_9`)


Dieses Verfahren hat unter anderem auch als mit Strafe bedrohte Handlungen iSd § 107 Abs 1 und 2 erster Fall StGB subsumierte Anlasstaten zum Nachteil der genannten Richter des Obersten Gerichtshofs zum Gegenstand (US 7, 10 des erwähnten Urteils des Landesgerichts für Strafsachen Wien).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Brenner`(person)
- `Oliver Pekarek`(person)
- `Landesgerichts Krems an der Donau`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `OGH`(organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Dr. Oshidari`(person)
- `Gerhard Bukowska`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)
- `OGH`(organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und Hofrätin des Obersten Gerichtshofs Mag. Michel sind von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Gerhard Boesl betreffend das Verfahren AZ 16 Hv20/14x des Landesgerichts für Strafsachen Wien ausgeschlossen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)
- `Gerhard Boesl`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_6`)


Gründe:  Rechtliche Beurteilung Der Oberste Gerichtshof hat zu AZ 11 Os 5/15t über die gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, ergriffene Nichtigkeitsbeschwerde und Berufung des Angeklagten Gerhard Bugnenings zu entscheiden.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Gerhard Bugnenings`(person)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_14`)


Senat des Obersten Gerichtshofs - unter dem Aspekt der §§ 281 Abs 1 Z 5a, 362 StPO - auch der Tatverdacht hinsichtlich eines Tatzeitraums („August 2008 bis längstens 14. Dezember 2008“ - vgl Urteil des Landesgerichts für Strafsachen Wien vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, US 2) zu prüfen, auf den sich auch das Oberlandesgericht Wien in Entscheidungen bezog, die unter Mitwirkung der Angehörigen des Anzeigers getroffen wurden (vgl insb BS 32 f in AZ 19 Bs 465/12i).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgericht Wien`(organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Herwig Bernts`(person)
- `Landesgerichts Linz`(organisation)
- `OGH`(organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Brenner`(person)
- `Dr. Setz-Hummel`(person)
- `Ahmed Koehnen`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `OGH`(organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_7`)


Mit dem erwähnten Beschluss vom 25. November 2019 hatte das Oberlandesgericht Wien einer Beschwerde des Ahmed Kocks gegen einen Beschluss des Landesgerichts für Strafsachen Wien auf Ablehnung eines Antrags des Genannten auf Wiederaufnahme des Verfahrens AZ 606 Hv 1/11m jenes Gerichts nicht Folge gegeben.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgericht Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Ahmed Kocks`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Mann`(person)
- `Dr. Brenner`(person)
- `Mag. Rögner`(person)
- `Thomas Michenfelder`(person)
- `Landesgerichts Krems an der Donau`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Gföller`(person)
- `Dr. Zeh-Gindl`(person)

**Example 67** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


Dieser Beschluss wird aufgehoben und es wird in der Sache selbst erkannt, dass der Senatspräsident des Oberlandesgerichts Wien Dr. Krenn sowie die Richterinnen des Oberlandesgerichts Wien Mag. Edwards und Mag. Sanda von der Entscheidung über die Berufung des Angeklagten gegen das Urteil des Landesgerichts Krems an der Donau vom 8. August 2018, GZ 38 Hv 40/18z-100, nicht ausgeschlossen sind.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Krenn`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Edwards`(person)
- `Mag. Sanda`(person)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_6`)


Text Gründe: Soweit für die Behandlung der Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Bedeutung wurde Thomas Maksym mit Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB (I./) sowie der Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB (II./) und des Betrugs nach § 146 StGB (III./) schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Aus Anlass der (allein aufrechterhaltenen) Berufung des Angeklagten wegen des Ausspruchs über die Strafe (ON 86) hob der zuständige 21.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Maksym`(person)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_10`)


Im zweiten Rechtsgang sprach die Einzelrichterin des Landesgerichts Krems an der Donau Thomas Muthardt mit Urteil vom 8. August 2018 (ON 100) neuerlich anklagekonform schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Krems an der Donau`(organisation)
- `Thomas Muthardt`(person)

**Example 70** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_13`)


Dazu führte er aus, dass die genannten Richter das Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) in amtswegiger Wahrnehmung des Nichtigkeitsgrundes des § 281 Abs 1 Z 9 lit a [der Sache nach Z 10] StPO „großteils aufgehoben“ und „dabei“ „die Tatfrage mit Hinweis auf die Strafbarkeit des angelasteten Verhaltens indizierende Verfahrensergebnisse mit voller Kognitionsbefugnis [beurteilt] und […] beweiswürdigend Stellung bezogen“ hätten.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Krems an der Donau`(organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fruhmann`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Gebhard Sayin`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_4`)


Text Gründe: Mit der angefochtenen Entscheidung wies das Oberlandesgericht Wien die Beschwerde des Gebhard Senkfeil gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 25. September 2012, GZ 130 Bl 65/12s-10, mit welchem der Antrag des Beschwerdeführers auf Fortführung des Verfahrens AZ 20 UT 91/12p der Staatsanwaltschaft Wien gegen unbekannte Täter wegen § 302 Abs 1 StGB zurückgewiesen worden war, als unzulässig zurück (§ 196 Abs 1 StPO).

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgericht Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Gebhard Senkfeil`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__4`)


Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt verletzen 1./ die Durchführung der Hauptverhandlung und Urteilsfällung am 26. September 2018 in Abwesenheit des Angeklagten § 427 Abs 1 StPO, 2./ die Verlesung des die Vernehmung des Zeugen Alexander Struttmann beinhaltenden Teils des Hauptverhandlungsprotokolls vom 28. Februar 2018 (ON 9) in der Hauptverhandlung am 26. September 2018 § 252 Abs 1 StPO iVm § 447 StPO, 3./ der unter einem mit dem Urteil vom 26. September 2018 (ON 25) gefasste Beschluss auf Widerruf der Nenad Pohlmann mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht § 494a Abs 3 StPO und 4./ das Urteil vom 26. September 2018 (ON 25) § 31 Abs 1 StGB.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Leopoldstadt`(organisation)
- `Alexander Struttmann`(person)
- `Nenad Pohlmann`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__7`)


Ferner beantragte die Staatsanwaltschaft, die Nenad Pleßing mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährte bedingte Strafnachsicht (vgl ON 2 S 32) zu widerrufen, und wies darauf hin, dass der Widerruf der mit Urteil des genannten Gerichts vom 19. September 2017, AZ 44 Hv 88/17g, gewährten bedingten Strafnachsicht dem zuständigen Gerichtshof vorzubehalten sei.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nenad Pleßing`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__14`)


Eine Bedachtnahme auf das Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, (unjournalisiert im Akt einliegend nach ON 27; vgl ON 22 Punkt 2./) gemäß § 31 StGB, erfolgte nicht.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__15`)


Zugleich fasste es den Beschluss auf Widerruf (§ 494a Abs 1 Z 4 StPO) der Nenad Plettener mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht einer Freiheitsstrafe, ohne zuvor diesen Akt oder zumindest eine Abschrift des Urteils beigeschafft zu haben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nenad Plettener`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__16`)


In Ansehung der dem Angeklagten mit Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, gewährten bedingten Strafnachsicht erging ein auf § 494a Abs 2 letzter Satz StPO gestützter Vorbehaltsbeschluss.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__18`)


Über die rechtzeitige Beschwerde der Staatsanwaltschaft gegen den Beschluss auf Widerruf bedingter Strafnachsicht (ON 28) wurde noch nicht entschieden (AZ 131 Bl 94/18x des Landesgerichts für Strafsachen Wien).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__28`)


Der Strafantrag vom 28. November 2017, aus dem der Antrag der Staatsanwaltschaft auf Widerruf der bedingten Strafnachsicht zu AZ 162 Hv 117/14k des Landesgerichts für Strafsachen Wien ersichtlich ist (ON 4), wurde dem Angeklagten durch Zustellung zur Kenntnis gebracht.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__32`)


Die unterbliebene Bedachtnahme auf das aktenkundige Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, verletzt daher mit Blick auf den Zeitpunkt der dem Abwesenheitsurteil zugrunde liegenden Tat (3. Februar 2017) § 31 Abs 1 StGB.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_3`)


Kopf Der Oberste Gerichtshof hat am 15. März 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ettel als Schriftführerin in der Maßnahmenvollzugssache des Andreas Wegele, AZ 181 BE 143/17y des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 9. Jänner 2018, AZ 131 Bs 370/17z, und seinen Antrag auf Bewilligung der Verfahrenshilfe nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Dr. Oshidari`(person)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Brenner`(person)
- `Mag. Ettel`(person)
- `Andreas Wegele`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_5`)


Text Gründe: Mit dem angefochtenen Beschluss vom 9. Jänner 2018, AZ 131 Bs 370/17z, gab das Oberlandesgericht Wien als Rechtsmittelgericht der Beschwerde des Andreas Wackerow gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 20. November 2017, GZ 181 BE 143/17y-16, mit dem die bedingte Entlassung aus einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 2 StGB abgelehnt worden war, nicht Folge.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgericht Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Andreas Wackerow`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__9`)


Unter einem erging der Beschluss, gemäß § 494a Abs 1 Z 2 StPO vom Widerruf der zum AZ 36 Hv 118/05p des Landesgerichts Innsbruck und zum AZ 3 U 350/06d des Bezirksgerichts Kufstein jeweils gewährten bedingten Strafnachsicht abzusehen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Kufstein`(organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


Kopf Der Oberste Gerichtshof hat am 12. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Ruckendorfer als Schriftführerin in der Strafsache gegen Thomas Leutz wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 13. September 2018, GZ 35 Hv 46/18m-130, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Brenner`(person)
- `Dr. Setz-Hummel`(person)
- `Mag. Ruckendorfer`(person)
- `Thomas Leutz`(person)
- `Landesgerichts Innsbruck`(organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, im Ausspruch über den Verfall aufgehoben, soweit er sich auf einen 35.353,95 Euro übersteigenden Betrag bezieht, und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck verwiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Innsbruck`(organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_26`)


In Stattgebung der Nichtigkeitsbeschwerde des Angeklagten war daher das angefochtene Urteil wie im Spruch ersichtlich aufzuheben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck (§ 445 Abs 2 StPO;

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Innsbruck`(organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Holzweber`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Dr. Schwab`(person)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Mag. Bayer`(person)
- `Dr. Ernst`(person)
- `Nepomuk Lieschke`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Brenner`(person)
- `Dr. Setz-Hummel`(person)
- `Mag. Hauer`(person)
- `Viktor Marschmeyer`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Dr. Stefan Toepfl`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Müller`(person)
- `Maximilian Gompertz`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_3`)


Kopf Der Oberste Gerichtshof hat am 5. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Brenner als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Kaltenbrunner als Schriftführerin in der Strafsache gegen Johannes Barkhof wegen des Vergehens der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB und weiterer strafbarer Handlungen, AZ 51 Hv 32/13i des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen den Beschluss des genannten Gerichts vom 4. Mai 2014, GZ 51 Hv 32/13i-35, und weitere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, und der Verteidigerin Mag. Reisinger zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Brenner`(person)
- `Mag. Kaltenbrunner`(person)
- `Johannes Barkhof`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Dr. Eisenmenger`(person)
- `Mag. Reisinger`(person)

**Example 92** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_4`)


Im Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch, verletzt die Unterlassung der nachstehend angeführten Zustellungen an den gesetzlichen Vertreter des jugendlichen Beschuldigten Johannes Büffel das Gesetz, und zwar 1./ des Antrags der Staatsanwaltschaft vom 12. März 2014 auf Wiederaufnahme des Strafverfahrens (ON 29) zur Gegenäußerung binnen 14 Tagen in § 38 Abs 1 JGG iVm § 357 Abs 2 erster Satz StPO; 2./ des Beschlusses vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens (ON 35) in § 38 Abs 3 erster Satz JGG iVm § 86 Abs 2 StPO iVm § 87 Abs 1 StPO.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Johannes Büffel`(person)

**Example 93** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_6`)


Text Gründe: In der Jugendstrafsache AZ 51 Hv 32/13i des Landesgerichts Feldkirch legte die Staatsanwaltschaft Feldkirch mit Strafantrag vom 18. April 2013, AZ 9 St 82/13f, dem am 23. August 1996 geborenen Angeklagten Johannes Bednorz als Vergehen der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB (I./) sowie der Nötigung nach den §§ 15 Abs 1, 105 Abs 1 StGB (II./, III./1./), der gefährlichen Drohung nach § 107 Abs 1 StGB (III./2./) und der Sachbeschädigung nach § 125 StGB (III./3./) qualifiziertes Verhalten zum Nachteil der Sabrina Hemmersdorfer zur Last (ON 3).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Johannes Bednorz`(person)
- `Sabrina Hemmersdorfer`(person)

**Example 94** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_7`)


Mit gekürzt ausgefertigtem Urteil der Einzelrichterin in Jugendstrafsachen des Landesgerichts Feldkirch vom 5. Juni 2013 wurde der jugendliche Angeklagte mehrerer Vergehen schuldig erkannt, jedoch von der Anklage (I./), er habe in Heinrich-Prosl-Gasse 6, 2034 Großharras, Österreich im Zeitraum von März 2012 bis Ende Februar 2013 gegen Sabrina Höllerl eine längere Zeit hindurch fortgesetzt Gewalt ausgeübt, indem er sie mehr als zehnmal mit Fäusten gegen den Bauch und gegen das Gesicht geschlagen habe, wodurch diese teilweise Prellungen und Schürfwunden erlitten habe, mangels Schuldbeweises gemäß § 259 Z 3 StPO freigesprochen (ON 14).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Heinrich-Prosl-Gasse 6, 2034 Großharras, Österreich`(address)
- `Sabrina Höllerl`(person)

**Example 95** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_8`)


Aus Anlass des ihre polizeilichen Angaben abschwächenden und zum oben angeführten Freispruch führenden Aussageverhaltens der Zeugin Sabrina Härtel in der Hauptverhandlung vom 5. Juni 2013 (ON 13 S 5 ff) erhob die Staatsanwaltschaft Feldkirch am 20. Juni 2013 zu AZ 9 St 131/13m in der Jugendstrafsache AZ 20 Hv 68/13f des Landesgerichts Feldkirch Strafantrag (ON 4 des zuletzt bezeichneten Aktes) gegen die Genannte wegen des Verdachts der am 8. März 2013 und am 15. März 2013 in Franz Schuster-Straße 8, 8212 Kleinpesendorf, Österreich im Ermittlungsverfahren gegen Johannes Breenkötter begangenen Vergehen der falschen Beweisaussage nach § 288 Abs 1 und Abs 4 StGB (I./) sowie der Verleumdung nach § 297 Abs 1 zweiter Fall StGB (II./).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sabrina Härtel`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Franz Schuster-Straße 8, 8212 Kleinpesendorf, Österreich`(address)
- `Johannes Breenkötter`(person)

**Example 96** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_9`)


Nachdem die Angeklagte Sabrina Heckel in der Hauptverhandlung am 24. Juli 2013 angegeben hatte, als Zeugin nicht vor der Polizei, sondern in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Butze falsch ausgesagt zu haben, gab die Staatsanwaltschaft noch in dieser Hauptverhandlung eine Alternativanklage zu Protokoll, der zufolge sie als Zeugin in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Bulthaup vor dem Landesgericht Feldkirch die Vergehen der falschen Beweisaussage nach § 288 Abs 1 StGB (III./) und der Begünstigung nach § 299 Abs 1 StGB (IV./) begangen habe (ON 10 S 3 f des Aktes AZ 51 Hv 46/13y des Landesgerichts Feldkirch).

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgericht Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sabrina Heckel`(person)
- `Johannes Butze`(person)
- `Johannes Bulthaup`(person)
- `Landesgericht Feldkirch`(organisation)
- `Landesgerichts Feldkirch`(organisation)

**Example 97** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_10`)


Mit gekürzt ausgefertigtem Urteil des Landesgerichts Feldkirch vom 2. September 2013, GZ 20 Hv 68/13f-13, wurde Sabrina Harrazin im Sinne dieser Alternativanklage schuldig erkannt.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Sabrina Harrazin`(person)

**Example 98** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_11`)


Hierauf beantragte die Staatsanwaltschaft Feldkirch in dem Johannes Bergknecht betreffenden Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch am 12. März 2014 gemäß § 355 StPO iVm § 352 Abs 1 Z 1 StPO die Wiederaufnahme des Strafverfahrens im Umfang des am 5. Juni 2013 ergangenen Freispruchs des Angeklagten Johannes Bertrang, weil dieser durch die falsche Beweisaussage der Zeugin Sabrina Holzschuher herbeigeführt worden sei (ON 29).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Johannes Bergknecht`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Johannes Bertrang`(person)
- `Sabrina Holzschuher`(person)

**Example 99** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_13`)


Mit Beschluss des Einzelrichters des Landesgerichts Feldkirch vom 4. Mai 2014, GZ 51 Hv 32/13i-35, wurde in Stattgebung des Antrags der Staatsanwaltschaft das Strafverfahren gegen Johannes Braentel wegen § 107b Abs 1 und Abs 2 StGB gemäß § 355 StPO im Umfang des rechtskräftigen Freispruchs wiederaufgenommen und das Urteil des Landesgerichts Feldkirch vom 5. Juni 2013 (ON 14) umfänglich des Freispruchs aufgehoben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgerichts Feldkirch`
- `Landesgericht` — similar text (different position): `Landesgerichts Feldkirch`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Johannes Braentel`(person)
- `Landesgerichts Feldkirch`(organisation)

</details>

---

## `BFH Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a2ba4517`  
**Description:**
Matches the abbreviation BFH (Bundesfinanzhof) in various contexts, including citation contexts like 'BFH 27.10.2011', excluding cases where it is part of a compound word or followed by citation markers like 'in BStBl' or numbers that are not dates.

**Content:**
```
(?<!\w)(?<!-)BFH(?!\w|\-|\s+in\s+BStBl|\s+\d{2}/\d{2}/\d{4}|\s+\d{2}\.\d{2}\.\d{4}|\s+\d{2}\.\d{2}\.\d{2})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Bruck Leoben Mürzzuschlag` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f603fc4c`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed strictly by 'Bruck Leoben Mürzzuschlag'. This rule is now strictly enforced to only match the full location phrase, preventing partial matches like 'Finanzamtes' alone.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Bruck\s+Leoben\s+M\u00fcrzzuschlag)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Judenburg Liezen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `16ca3e86`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed strictly by 'Judenburg Liezen'. This rule is now strictly enforced to only match the full location phrase, preventing partial matches like 'Finanzamtes' alone.

**Content:**
```
(?<!\w)(Finanzamt(?:es)?\s+Judenburg\s+Liezen)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stadt Wien` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c6449a2a`  
**Description:**
Matches 'Stadt Wien' as an organization entity, but strictly excludes cases where it is preceded by 'Magistrat' (which is handled by a higher priority rule).

**Content:**
```
(?<!\w)(?<!Magistrat\s)(Stadt\s+Wien)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 32 | 0 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 32 | 3965 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Marlene Friss`(person)
- `WestTelekom GmbH`(organisation)
- `Rehwald 11, 4723 Fronberg, Österreich`(address)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Basil Biewer anhängig.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)
- `Basil Biewer`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Dr. Annerl`(person)
- `Meinrad Bruhnsen`(person)
- `30. Januar`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_6`)


Mit einstweiliger Verfügung des Bezirksgerichts Innere Stadt Wien vom 28. April 2022 wurde der Vater verpflichtet, dem Kind einen vorläufigen monatlichen Unterhaltsbeitrag in Höhe von 38 EUR zu leisten (ON 2).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mikolaj Eleftheriadou`(person)
- `Helge Schuchmann`(person)
- `Isabel Rahnfeld`(person)
- `PhD Daniel Coutand`(person)
- `Mag. Dirk Hükelheim`(person)
- `Mag. Roland Marko`(person)
- `Dr. Francisco Rumpf`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Mann`(person)
- `Mag. Anscheringer`(person)
- `Natascha von Bohr`(person)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Bezirksgerichts Linz`(organisation)
- `Bezirksgericht Linz`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_5`)


Das Bezirksgericht Linz überwies die Sache dem Bezirksgericht Innere Stadt Wien mit der Begründung örtlicher Unzuständigkeit (vgl ON 1 S 3: „erste Taten in Wien“).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Linz`(organisation)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`
- `Stadt Wien` — similar text (different position): `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Dr. Schöll`(person)
- `Robert Ultsch`(person)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Mag. Schneider`(person)

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__6`)


2. Der Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) verletzt §§ 270 Abs 3, 271 Abs 7 StPO iVm §§ 447, 458 zweiter Satz StPO.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__7`)


Text Gründe: Mit Urteil des Bezirksgerichts Innere Stadt Wien (ON 19) wurde Robert Ulrici jeweils eines Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB schuldig erkannt und hiefür zu einer bedingt nachgesehenen Freiheitsstrafe verurteilt. Nach Verkündung des Urteils und erteilter Rechtsmittelbelehrung erklärte der – nicht durch einen Verteidiger vertretene (vgl § 57 Abs 2 dritter Satz StPO;Fabrizy, StPO13§ 57 Rz 10) – Angeklagte zunächst, auf Rechtsmittel zu verzichten (ON 18 S 5).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Robert Ulrici`(person)

**Example 12** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__10`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__13`)


Mit Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30) wurden sowohl das Protokoll über die Hauptverhandlung (ON 18) als auch die Urteilsurschrift (ON 19) in Ansehung des „Verhandlungsdatum[s]“ von „23. 11. 2018“ auf „27. 11. 2018“ berichtigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__14`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrem Antrag auf außerordentliche Wiederaufnahme des Verfahrens zutreffend darlegt, bestehen gegen die Richtigkeit der dem Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), zugrunde gelegten Tatsache, das erstinstanzliche Urteil sei am 23. November 2018 verkündet worden, erhebliche Bedenken: Die Verfügung des Bezirksgerichts Innere Stadt Wien vom 1. November 2018 auf Ladung des Angeklagten zur Hauptverhandlung am 27. November 2018 (ON 1 [unjournalisiert] S 6), das auf der letzten Seite der Urteilsurschrift angeführte Urteilsdatum „27. November 2018“ (ON 19 S 5), die im Verfahrensakt enthaltene (unjournalisierte) Äußerung der Staatsanwaltschaft Wien vom 15. November 2019, AZ 126 BAZ 822/11s, sowie der Berichtigungsbeschluss vom 4. Dezember 2019 (ON 30) legen qualifiziert nahe, dass das Urteil am27. November 2018verkündet wurde.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__18`)


Ebenso zutreffend führt die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde aus, dass der Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30) in zweierlei Hinsicht das Gesetz verletzt: Die Ausfertigung der Urteilsurschrift mit unrichtigem Datum bewirkt ein – nicht die im § 260 Abs 1 Z 1 bis Z 3 und Abs 2 StPO erwähnten Punkte betreffendes – Formgebrechen, das (hier) der Richter des Bezirksgerichts allenfalls nach Anhörung der Beteiligten zu berichtigen hat (§ 270 Abs 3 erster Satz StPO iVm §§ 447, 458 zweiter Satz StPO;

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/1Ob61_18d`) (sent_id: `deanon_260716_TRAIN/1Ob61_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Johanna Moehrlin, vertreten durch Dr. Georg Kahlig und Mag. Gerhard Stauder, Rechtsanwälte in Wien, gegen die beklagte Partei DI Camilla Willoweit, vertreten durch Dr. Reinhard Schäfer, Rechtsanwalt in Wien, wegen Unterhalts, über die „außerordentliche“ Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 1. März 2018, GZ 45 R 517/17p-75, mit dem das Urteil des Bezirksgerichts Innere Stadt Wien vom 19. September 2017, GZ 4 C 50/14g-68, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Das Erstgericht sprach der Klägerin rückständigen nachehelichen Unterhalt in Höhe von 24.081,48 EUR sA zu. Das Berufungsgericht gab der Berufung des Beklagten nicht Folge und bestätigte dieses Urteil.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Johanna Moehrlin`(person)
- `Dr. Georg Kahlig`(person)
- `Mag. Gerhard Stauder`(person)
- `DI Camilla Willoweit`(person)
- `Dr. Reinhard Schäfer`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_5`)


Ihre Ehe wurde mit Urteil des Bezirksgerichts Innere Stadt Wien vom 24.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_4`)


Silvana Roellgen, MBA KG und 2. Dr. Nancy Achatzy, vertreten durch die erstklagende Partei, wider die beklagte Partei Dr. Theodora Jungverdorben, vertreten durch BMA Brandstätter Rechtsanwälte GmbH in Wien, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. April 2014, GZ 46 R 135/13p-43, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Jänner 2013, GZ 75 C 17/11x-37, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Silvana Roellgen, MBA`(person)
- `Dr. Nancy Achatzy`(person)
- `Dr. Theodora Jungverdorben`(person)
- `BMA Brandstätter Rechtsanwälte GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Moritz Absmeier, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei DENU Immobilien GmbH, Gürtel 12, 5145 Schmalzhofen, Österreich, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Dr. Moritz Absmeier`(person)
- `Dr. Martin Neuwirth`(person)
- `Dr. Alexander Neurauter`(person)
- `DENU Immobilien GmbH`(organisation)
- `Gürtel 12, 5145 Schmalzhofen, Österreich`(address)
- `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_6`)


Für die Bewilligung und die Vollziehung der beabsichtigten Exekution gegen die Zweitbeklagte auf Urteilsveröffentlichung wird das Bezirksgericht Innere Stadt Wien als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_9`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_19`)


Die Ordinationsvoraussetzungen gemäß § 28 Abs 1 Z 2 JN sind daher erfüllt. Dem Ordinationsantrag ist somit stattzugeben und zweckmäßigerweise das Bezirksgericht Innere Stadt Wien als zuständiges Gericht zu bestimmen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/5Ob106_20d`) (sent_id: `deanon_260716_TRAIN/5Ob106_20d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Pflegschaftssache der mj Mathilda Dirichs, und Gregor Frysch, beide vorläufig in Obsorge der Mutter Melissa Noßmann, vertreten durch Mag. Wolfgang Doppelhofer, Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs des Vaters Olaf Fleischhaker, vertreten durch Dr. Marco Nademleinsky, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. April 2020, GZ 42 R 466/19v-138, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 14. Oktober 2019, GZ 79 Ps 97/16d-121, bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Steger`(person)
- `Mathilda Dirichs`(person)
- `Gregor Frysch`(person)
- `Melissa Noßmann`(person)
- `Mag. Wolfgang Doppelhofer`(person)
- `Olaf Fleischhaker`(person)
- `Dr. Marco Nademleinsky`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/5Ob152_12g`) (sent_id: `deanon_260716_TRAIN/5Ob152_12g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofrätinnen Dr. Hurch und Dr. Lovrek sowie die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der Pflegschaftssache der minderjährigen Volker Staybl, geboren am 8. März 1994, wegen Obsorge, über den Revisionsrekurs der Mutter Ing. Adriana Kravchenko, vertreten durch Mag. Klaus Kabelka, Rechtsanwalt in Wien, über den Revisionsrekurs der Mutter gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 23. Mai 2012, GZ 42 R 195/12f-96, mit dem infolge Rekurses der Mutter der Beschluss des Bezirksgerichts Innere Stadt Wien vom 15. März 2012, GZ 59 Ps 21/10x-90, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Danzl`(person)
- `Dr. Hurch`(person)
- `Dr. Lovrek`(person)
- `Dr. Höllwerth`(person)
- `Mag. Wurzer`(person)
- `Volker Staybl`(person)
- `8. März 1994`(date)
- `Ing. Adriana Kravchenko`(person)
- `Mag. Klaus Kabelka`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/6Ob182_20p`) (sent_id: `deanon_260716_TRAIN/6Ob182_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des Minderjährigen ÖkR Techn R Mag.a Helge Cigan, geboren am 13. Dezember 2007, 3. September 1976, vertreten durch das Land Wien (Stadt Wien Kinder- und Jugendhilfe Rechtsvertretung Bezirk 22, 1220 Wien, Simone-de-Beauvoir-Platz 6) als Kinder- und Jugendhilfeträger, über den Revisionsrekurs des Vaters Quentin Martschinke, vertreten durch Anwaltssocietät Sattlegger Dorninger Steiner & Partner in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 25. Juni 2020, GZ 43 R 237/20a-31, mit dem der Beschluss des Bezirksgerichts Donaustadt vom 21. April 2020, GZ 1 P 135/18y-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wirdzurückgewiesen.

**False Positives:**

- `Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `ÖkR Techn R Mag.a Helge Cigan`(person)
- `13. Dezember`(date)
- `3. September 1976`(date)
- `Quentin Martschinke`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/7Ob138_16v`) (sent_id: `deanon_260716_TRAIN/7Ob138_16v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Höllwerth als Vorsitzenden und durch die Hofräte Mag. Wurzer, Mag. Malesich, Dr. Hofer-Zeni-Rennhofer und Dr. Singer als weitere Richter in der Rechtssache der gefährdeten Partei Theobald Schomäker, vertreten durch Suppan & Spiegl Rechtsanwälte GmbH in Wien, gegen den Gegner der gefährdeten Partei Berthold Hömann, vertreten durch Dr. Paul Luiki, Rechtsanwalt in Wien, dieser vertreten durch Dr. Romana Zeh-Gindl, Rechtsanwältin in Wien, wegen Erlassung einer einstweiligen Verfügung, infolge des außerordentlichen Revisionsrekurses des Gegners der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 30. Mai 2016, GZ 46 R 177/16v-26, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 19. Jänner 2016, GZ 26 C 1563/15w-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Rekursgericht zur Ergänzung seiner Entscheidung durch den Ausspruch über den Wert seines Entscheidungsgegenstands übermittelt.  Text Begründung: Das Erstgericht erließ die nach § 382g EO beantragte einstweilige Verfügung zur Sicherung der auf §§ 16, 1328a ABGB und § 1330 ABGB gestützten Unterlassungsansprüche.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Höllwerth`(person)
- `Mag. Wurzer`(person)
- `Mag. Malesich`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Singer`(person)
- `Theobald Schomäker`(person)
- `Suppan & Spiegl Rechtsanwälte GmbH`(organisation)
- `Berthold Hömann`(person)
- `Dr. Paul Luiki`(person)
- `Dr. Romana Zeh-Gindl`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/7Ob180_16w`) (sent_id: `deanon_260716_TRAIN/7Ob180_16w_4`)


Dr. Anabel Heimboeckel, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dominik Westerberger, vertreten durch Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, wegen Ehescheidung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juni 2016, GZ 42 R 130/16b-33, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Dezember 2015, GZ 3 C 9/14w-27, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anabel Heimboeckel`(person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `Dominik Westerberger`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/8Ob163_09t`) (sent_id: `deanon_260716_TRAIN/8Ob163_09t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner und die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Pflegschaftssache der mj OMedR Roderich Pruvot, geboren am 9. Februar 1955, und der mj Konrad Michailidis, geboren am 29. September 2000, beide wohnhaft bei ihrer Mutter Ing. KzlR Tatjana Pumpmeyer, über den außerordentlichen Revisionsrekurs des Vaters Vitus Welfle, geboren am 9. Dezember 2009, vertreten durch Mag. Theresia Brunhölzl, Rechtsanwältin in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 7. Juli 2009, GZ 42 R 210/09g-S-93, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 23. März 2009, GZ 88 P 65/08v-81b, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Brenn`(person)
- `OMedR Roderich Pruvot`(person)
- `9. Februar 1955`(date)
- `Konrad Michailidis`(person)
- `29. September 2000`(date)
- `Ing. KzlR Tatjana Pumpmeyer`(person)
- `Vitus Welfle`(person)
- `9. Dezember 2009`(date)
- `Mag. Theresia Brunhölzl`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/8Ob163_09t`) (sent_id: `deanon_260716_TRAIN/8Ob163_09t_5`)


Mit Beschluss des Bezirksgerichts Innere Stadt Wien vom 16. Mai 2006, GZ 9 C 58/06z-20, wurde die Ehe der Eltern einvernehmlich geschieden.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/8Ob163_09t`) (sent_id: `deanon_260716_TRAIN/8Ob163_09t_9`)


Mit einstweiliger Verfügung des Bezirksgerichts Innere Stadt Wien vom 8. Juni 2009 (ON S-91), also nach der Entscheidung des Erstgerichts, wurde dem Vater der Aufenthalt an näher bezeichneten Orten im Nahbereich der Mutter sowie der Kinder sowie das Zusammentreffen und die Kontaktaufnahme mit diesen untersagt, nachdem er anlässlich eines zufälligen Zusammentreffens am 13. Mai 2009 in Anwesenheit der Kinder die Mutter beschimpfte und bedrohte und deren neuen Ehegatten, der sie beschützen wollte, durch Würgen und einen Faustschlag ins Gesicht verletzte.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

</details>

---

## `OECD` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `491c7ed9`  
**Description:**
Matches the organization 'OECD' (Organisation for Economic Co-operation and Development), including in citation contexts like 'OECD-MA'.

**Content:**
```
\bOECD\b
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

