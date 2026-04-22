# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-22T10:40:24.631239

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-22/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2327 |
| Validation documents | 218 |
| Test documents | 56 |
| Train sentences | 2327 |
| Validation sentences | 218 |
| Test sentences | 6566 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 20 |
| Refinement iterations | 10 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | False |
| Enable Prune | False |
| Critic Interval | 0 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 15 |
| Refine per batch | 1 |
| Manually annotated examples | 1304 |
| First batch with manual data | 68 |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 90.9% |
| True Positives | 587 |
| False Positives | 423 |
| Micro Precision | 58.1% |
| Micro Recall | 64.1% |
| Micro F1 | 61.0% |
| Macro F1 | 61.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Event Sudkraftlex GMBH` | 4.3% | 100.0% | 2.2% | 20 | 20 | 0 |
| `KQPC Versand GMBH` | 4.3% | 100.0% | 2.2% | 20 | 20 | 0 |
| `Sudver Handel Services GMBH` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Glanznorost Institut GMBH` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `FA Specific Locations` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Mag. Ghesla Steuerberater GmbH Specific` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `FA St. Johann Tamsweg Zell am See Specific` | 0.9% | 100.0% | 0.4% | 4 | 4 | 0 |
| `ÖGK` | 8.4% | 100.0% | 4.4% | 40 | 40 | 0 |
| `Finanzamts Genitive Locations` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Magistrat Wien MA 67` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Wirtschaftsuniversität Wien` | 1.7% | 100.0% | 0.9% | 8 | 8 | 0 |
| `Bundesministeriums für Finanzen Genitive` | 0.9% | 100.0% | 0.4% | 4 | 4 | 0 |
| `FAÖ Acronym` | 4.3% | 100.0% | 2.2% | 20 | 20 | 0 |
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Magistrat der Stadt Wien, MA 67` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | 0.9% | 100.0% | 0.4% | 4 | 4 | 0 |
| `Universität Wien` | 3.9% | 100.0% | 2.0% | 18 | 18 | 0 |
| `Finanzamtes Wien 1/23 Specific` | 0.9% | 100.0% | 0.4% | 4 | 4 | 0 |
| `Bundesministerium General` | 0.9% | 100.0% | 0.4% | 4 | 4 | 0 |
| `Landespolizeidirektion Wien` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Finanzamt Österreich` | 5.5% | 100.0% | 2.8% | 26 | 26 | 0 |
| `Finanzamtes Österreich` | 6.3% | 100.0% | 3.3% | 30 | 30 | 0 |
| `Universität General` | 3.9% | 100.0% | 2.0% | 18 | 18 | 0 |
| `SUVA Acronym` | 9.8% | 75.0% | 5.2% | 64 | 48 | 16 |
| `BMF Specific` | 0.9% | 66.7% | 0.4% | 6 | 4 | 2 |
| `Magistrat der Stadt Wien, Magistratsabteilung 6` | 0.9% | 66.7% | 0.4% | 6 | 4 | 2 |
| `Verfassungsgerichtshof` | 0.9% | 50.0% | 0.4% | 8 | 4 | 4 |
| `Magistrat der Stadt Wien Genitive Plural` | 0.9% | 50.0% | 0.4% | 8 | 4 | 4 |
| `VfGH Acronym` | 0.2% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Bundesfinanzgericht Full` | 23.3% | 50.0% | 15.2% | 278 | 139 | 139 |
| `Verwaltungsgerichtshof Specific` | 21.6% | 50.0% | 13.8% | 252 | 126 | 126 |
| `Magistrat der Stadt Wien` | 2.1% | 45.5% | 1.1% | 22 | 10 | 12 |
| `Magistratsabteilung 67` | 0.9% | 40.0% | 0.4% | 10 | 4 | 6 |
| `BFG Acronym` | 3.1% | 35.7% | 1.6% | 42 | 15 | 27 |
| `Finanzamt General Location` | 0.4% | 33.3% | 0.2% | 6 | 2 | 4 |
| `Pensionsversicherungsanstalt` | 0.4% | 25.0% | 0.2% | 8 | 2 | 6 |
| `FA General Location` | 0.4% | 25.0% | 0.2% | 8 | 2 | 6 |
| `VwGH Acronym` | 3.3% | 25.0% | 1.7% | 64 | 16 | 48 |
| `Pastl+Bächle Handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht Zell am See` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Klusner&Päffgen Bildung GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Englert Möbel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hülsebusch + Breithaupt Versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Logal Gruppe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Enns Werkal GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Süd Nortri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Trafenfen Automotive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mur Ververzor Betriebe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kornfelder Recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Füchsl Touristik GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mägerlein Logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Roelfsen Versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lubomir Merschmeyer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Houdek Maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schmeltz Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dorfcon-Verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lexdon IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Wien 1/23 Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Naaß Elektro GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bersud Möbel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unter Heimdorf GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Buhrfeindt Lebensmittel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mur Alver OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tritri-IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gözcü Getränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dongartcon-Landwirtschaft GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Monlogtri-Analyse GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Traun Aluni Institut GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Specific Locations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Berend Energie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Blazickova & Hepprich Energie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Botho Mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unter Gartglanz GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzen Tradonnex GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Obernöder+Küsbert Touristik GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Talost GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `DonauRecycling GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `XJOV Cloud Dienstleistungen GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `MittelHeizung Werke AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Traun-Digital KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Klosterneuburg Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Amstetten Melk Scheibbs Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien 8/16/17 Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Wien 8/16/17 Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gernot Hirschkorn Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerischen Unfallversicherungsanstalt (SUVA)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UnterRecycling Services GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamt für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirketion Tirol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Musikhochschule Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Konservatorium der Stadt Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Philharmoniker` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Arbeitsmarktservice (AMS)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Wien 2/20/21/22 Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Landeck Reutte Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Oststeiermark Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Linz Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Judenburg Liezen Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Salzburg-Stadt Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Landeck Reutte Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Judenburg Liezen Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ÖBUG Full Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Österreichische Gesellschaft für Europapolitik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TPA STB Wien GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `INET Internet Service GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS Acronym` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `INET System Informations GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS/BFG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `How to spend it Verlag GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Karl-Franzens- Universität Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BKS Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fachhochschule Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFH Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `London Film Academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundeskanzleramtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PVA Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SVS/SVB Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien Ambulatorium Landstraße` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherungsanstalt der Bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherung der Bauern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `PSD Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Psychiatrie Otto Wagner Spital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht BFG Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Saxinger Chalupsky & Partner Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Imre & Schaffer Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Vorarlberg Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Klagenfurt St. Veit Wolfsberg Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Bruck Eisenstadt Oberwart Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Landeck Reutte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Garanta VersicherungsAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sivananda Yoga Centre` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `DA Deutsche Allgemeine Versicherung AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Geschenkartikel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AVED cosmetic` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Yoga Vidya GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hamburger Fern-Hochschule` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wirtschaftsuniversität Wien Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Johannes Kepler Universität Linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Johannes Kepler Universität Linz Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `JKU Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Universität St. Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tschurtschenthaler Walder Fister Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Immobilienbüro Mandl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt Klagenfurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Berwaldkel-Möbel AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Amts für Betrugsbekämpfung Genitive` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `FAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LG Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht Silz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LG für ZRS Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Justiz Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anwälte Mandl & Mitterbauer GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schule Gesundheitspflege Grillenreith` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GesundheitspflegeSchule LKH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Graz-Stadt Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hinklein Organisation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KG Companies Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bankhaus Denzel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Cervenka&Neunübel Telekom AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Europäische Grenzschutzagentur Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kriminalpolizei in Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `EASO` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMI` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Flughafen München` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OECD` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `Arbeits- und Sozialgericht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Eckhardt SteuerberatungsgmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Amts für Betrugsbekämpfung` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `Bundesministers für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrates der Stadt Wien, Magistratsabteilung 67` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Höhere Lehranstalt für Tourismus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HLF Krems/Donau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verfassungsgerichtshof Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Paugger Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `King's School` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `The King's School Worcester` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University of Bristol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `England` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `King's School Worcester` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Grazer Treuhand Steuerberatung GmbH & Partner KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Kirchdorf Perg Steyr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Kirchdorf Perg Steyr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamts Graz-Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamts Graz- Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Rhein Normonkel Manufaktur GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Merkur Treuhand Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Österreich (DST12)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schabetsberger Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Merkur Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS Salzburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Merkur Treuhand Steuerberatung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgericht Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiederspan Beratung GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Retail Giants Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steuerberater Metzler & Adelsberger OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Braunau Ried Schärding` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `B-GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `A-GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hausverwaltung-GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirkshauptmannschaft Bludenz Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Braunau Ried Schärding Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ÖBB Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SeneCura General` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Krankenpflegevereins Bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mittel Unisyn GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ober Lemostnor AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vennes Recycling AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bärs & Walterscheidt Handel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `InnMarine GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Universität Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lenfeld/Leys/Sonderegger Rechtsanwälte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Neunkirchen Wr. Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamtes Hollabrunn Korneuburg Tulln Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unter Donunisee AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministerin für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `X GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BDO Austria GmbH WP- u. StBges.` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFG Außenstelle Linz Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `R GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `X-GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AG General Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KG General Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Rechtsanwaltskanzlei Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherung Pattern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Partnerschaft Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirksgericht General Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht General Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `ÖGK`

**F1:** 0.084 | **Precision:** 1.000 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Matches the acronym 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.044 | 0.084 | 40 | 40 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 873 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Finanzamtes Österreich`

**F1:** 0.063 | **Precision:** 1.000 | **Recall:** 0.033  

**Format:** `regex`  
**Description:**
Matches the genitive form 'Finanzamtes Österreich'.

**Content:**
```
\bFinanzamtes\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.033 | 0.063 | 30 | 30 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 30 | 0 | 824 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

</details>

---

## `Finanzamt Österreich`

**F1:** 0.055 | **Precision:** 1.000 | **Recall:** 0.028  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' specifically to ensure it is captured.

**Content:**
```
\bFinanzamt\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.028 | 0.055 | 26 | 26 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 0 | 780 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_12`)


In der Bescheidbeschwerde wurde im Wesentlichen vorgebracht, dass die Unterlagen zum  Einkommen 2021 und 2022 per Fax und per Einschreiben an das Finanzamt Österreich in Wien  zugesandt worden wären.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_15`)


Mit Beschwerdevorentscheidung vom 08.10.2024 wurde die gegenständliche  Bescheidbeschwerde als unbegründet abgewiesen und zur Begründung angeführt:  „Der Antrag wird damit begründet, dass sämtliche Unterlagen an das Finanzamt Österreich  zugesandt wurden und man unrechtmäßig den Betrag gepfändet hat.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `Event Sudkraftlex GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Event Sudkraftlex GMBH'.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 20 | 20 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 754 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `KQPC Versand GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the specific entity 'KQPC Versand GMBH'.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 20 | 20 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 758 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

## `FAÖ Acronym`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAÖ' (Finanzamt Österreich) as an organisation.

**Content:**
```
\bFAÖ\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 20 | 20 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 723 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_11`)


Mit dem angefochtenen Bescheid vom 7. September 2023 wies das Finanzamt Österreich (im  Weiteren FAÖ) den Antrag als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_29`)


Mit Ergänzungsersuchen vom 17. November 2023 hielt das FAÖ dem BF vor, dass eine bloß  abstrakte Strafdrohung eine Wiedereinsetzung nicht rechtfertige, sondern ein konkreter  Rechtsnachteil eingetreten sein müsse.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_31`)


In seiner Vorhaltsbeantwortung vom 21. November 2023 brachte der BF vor, dass die  Rechtsansicht des FAÖ verfehlt sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

</details>

---

## `Universität Wien`

**F1:** 0.039 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Universität Wien'.

**Content:**
```
\bUniversität\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.020 | 0.039 | 18 | 18 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 833 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `Universität General`

**F1:** 0.039 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Universität' followed by a location or name, excluding common labels like 'Name', 'Art', 'Typ'.

**Content:**
```
\bUniversität\s+(?!(?:Name|Art|Typ|Bezeichnung|Anzahl|Beginn|Ende|Wohnort|Land|Landes|Stadt|Gemeinde)\b)(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*|in\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.020 | 0.039 | 18 | 18 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 833 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `Wirtschaftsuniversität Wien`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'Wirtschaftsuniversität Wien', 'WU Wien', and the standalone abbreviation 'WU' in university contexts.

**Content:**
```
\b(?:Wirtschaftsuniversität\s+Wien|WU\s+Wien|(?<!\w)WU(?!\s+Linz|\s*\())\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.017 | 8 | 8 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 842 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_47`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_74`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_135`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

</details>

---

## `SUVA Acronym`

**F1:** 0.098 | **Precision:** 0.750 | **Recall:** 0.052  

**Format:** `regex`  
**Description:**
Matches the acronym 'SUVA' as a standalone organization name.

**Content:**
```
\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.750 | 0.052 | 0.098 | 64 | 48 | 16 | 12 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 48 | 16 | 528 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_11`)


Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_12`)


Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_13`)


3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_14`)


4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_18`)


5.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer mit Beschwerde und – nach Ergehen abweisender Beschwer- devorentscheidungen – mit Vorlageantrag wandte.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_8`)


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

**False Positives:**

- `SUVA` — type mismatch (gold: `SUVA`)
- `SUVA` — type mismatch (gold: `SUVA`)

> partial: 2  |  missing annotation: 0

**Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

**False Positives:**

- `SUVA` — type mismatch (gold: `SUVA`)

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_44`)


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

**False Positives:**

- `SUVA` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_58`)


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizeri- schen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Bundesfinanzgericht Full`

**F1:** 0.233 | **Precision:** 0.500 | **Recall:** 0.152  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its optional suffixes (Außenstelle Linz, (BFG)), but excludes the genitive suffix 'es' or 's' from the extracted text.

**Content:**
```
\bBundesfinanzgericht\b(?:\s*,\s*Außenstelle\s+Linz)?(?:\s*\(\s*BFG\s*(?:\s*\d+\.\s*\d+\.\s*\d+|\s*RV/\d+[^)]*)?\s*\))?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.152 | 0.233 | 278 | 139 | 139 | 0 | 139 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 139 | 139 | 777 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_210`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_226`)


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_227`)


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_236`)


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_210`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_226`)


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_227`)


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `USA` (country)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_236`)


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Verwaltungsgerichtshof Specific`

**F1:** 0.216 | **Precision:** 0.500 | **Recall:** 0.138  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs', including the optional acronym '(VwGH)'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?(?:\s*\(\s*VwGH\s*\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.138 | 0.216 | 252 | 126 | 126 | 0 | 126 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 126 | 126 | 788 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

</details>

---

## `VwGH Acronym`

**F1:** 0.033 | **Precision:** 0.250 | **Recall:** 0.017  

**Format:** `regex`  
**Description:**
Matches the acronym 'VwGH' (Verwaltungsgerichtshof) as a standalone organization, excluding cases where it is followed by dates (citations).

**Content:**
```
\bVwGH\b(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.250 | 0.017 | 0.033 | 64 | 16 | 48 | 1 | 47 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 48 | 881 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_125`)


Die Rechtsfolgen im beschwerdegegenständlichen Fall ergeben sich unmittelbar aus den  anzuwendenden, vom Wortlaut her eindeutigen gesetzlichen Bestimmungen und wurde im  Übrigen der ständigen Rechtsprechung des VwGH gefolgt.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_248`)


Zu alldem ist auf die Rechtsprechung des VwGH zu verweisen, wonach eine freie Auflösbarkeit  des Vertrags nur dann vorliegt, wenn eine Kündigung auch die tatsächliche Befreiung von den  Leistungsverpflichtungen für die Zeit nach der Vertragsauflösung bewirkt (vgl VwGH  16.10.2014, 2011/16/0169;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_14`)


Neben den vom VwGH  behandelten einfachgesetzlichen Rechtsfragen macht die Bf weiters geltend, die  Kürzungsbestimmungen des § 2 Abs 2 Z 3a StabAbgG auf die Liquiditätsreserve in den  zweistufigen Sektoren nicht anzuwenden, stelle einen unsachlichen Systembruch, eine  unsachliche Differenzierung zwischen Einlagensicherung und Liquiditätsverbund, eine  sachwidrige Besteuerung gedeckter Einlagen, eine Benachteiligung gegenüber Kreditinstituten,  die keinem Liquiditätsverbund angehören müssen, sowie eine gleichheitswidrige  Differenzierung innerhalb der dezentralen Sektoren dar.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_19`)


Für 2024 wurde in der Stabilitätsabgabeerklärung 2024 die Liquiditätsreserve im Hinblick  auf die Entscheidung des VwGH vom 20.11.2024, Ro 2024/13/0019 nicht abgezogen und  erfolgte demnach eine erklärungsgemäße Festsetzung der Stabilitätsabgabe 2024 mit €  2.614,77.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_291`)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_294`)


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_291`)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_294`)


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `BFG Acronym`

**F1:** 0.031 | **Precision:** 0.357 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches 'BFG' acronym as an organisation, excluding cases where it is part of a hyphenated compound or a citation (followed by dates/numbers).

**Content:**
```
\bBFG\b(?!-)(?!\s*\d+\.\s*\d+\.\s*\d+)(?!\s*RV/)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.357 | 0.016 | 0.031 | 42 | 15 | 27 | 1 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 15 | 27 | 887 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_101`)


Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_103`)


Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_135`)


Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_147`)


Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_148`)


Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_101`)


Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_103`)


Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_135`)


Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_147`)


Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_148`)


Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Amts für Betrugsbekämpfung Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amts für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmts?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 676 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_3`)


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_10`)


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

</details>

---

## `Amts für Betrugsbekämpfung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amts für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung' with flexible whitespace.

**Content:**
```
\bAmts?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 676 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_3`)


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_10`)


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

</details>

---

## `Magistrat der Stadt Wien`

**F1:** 0.021 | **Precision:** 0.455 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Magistrat/Magistrats/Magistrates der Stadt Wien' without the MA 67 suffix, covering genitive forms.

**Content:**
```
\bMagistrat(?:s|es)?\s+der\s+Stadt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.455 | 0.011 | 0.021 | 22 | 10 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 12 | 772 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred ⊂ gold: `Magistrats der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred ⊂ gold: `Magistrats der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

</details>

---

## `UFS Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat).

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 434 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_30`)


Der Zeitpunkt, an dem die Daten in den elektronischen Verfügungsbereich des Empfängers  gelangt sind, ist bei FinanzOnline der Zeitpunkt der Einbringung der Daten in die Databox, zu  der der Empfänger Zugang hat (UFS 22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_41`)


UFS  22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_55`)


Wird zu einem späteren Zeitpunkt festgestellt, dass Beiträge nicht oder in geringerer Höhe zu  leisten gewesen wären, ändert dies nichts an ihrem ursprünglichen Charakter (UFS 15.4.2013,  RV/0220-W/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149731.1`) (sent_id: `findok-manually-annotated_TRAIN/149731.1_30`)


Der Zeitpunkt, an dem die Daten in den elektronischen Verfügungsbereich des Empfängers  gelangt sind, ist bei FinanzOnline der Zeitpunkt der Einbringung der Daten in die Databox, zu  der der Empfänger Zugang hat (UFS 22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149731.1`) (sent_id: `findok-manually-annotated_TRAIN/149731.1_41`)


UFS  22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Pensionsversicherungsanstalt`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt'.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.250 | 0.002 | 0.004 | 8 | 2 | 6 | 2 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 6 | 676 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_24`)


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

**False Positives:**

- `Pensionsversicherungsanstalt` — partial — pred ⊂ gold: `Pensionsversicherungsanstalt Wien`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_57`)


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_58`)


Auf den aktenkundigen Lohnzettel der Pensionsversicherungsanstalt sowie den im Akt  aufliegenden Kontrollmitteilungen wird verwiesen.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_24`)


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

**False Positives:**

- `Pensionsversicherungsanstalt` — partial — pred ⊂ gold: `Pensionsversicherungsanstalt Wien`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_57`)


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

</details>

---

## `FA General Location`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by a location, excluding known multi-word entities. Refined to be more robust.

**Content:**
```
\bFA\s+(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*|\d+\.\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b(?!(?:\s+1/23|\s+8/16/17|\s+2/20/21/22|\s+Klosterneuburg|\s+Landeck\s+Reutte|\s+Judenburg\s+Liezen|\s+Oststeiermark|\s+Linz|\s+St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|\s+Vorarlberg|\s+Graz\-Stadt|\s+Kirchdorf\s+Perg\s+Steyr|\s+Braunau\s+Ried\s+Sch\u00e4rding|\s+Hollabrunn\s+Korneuburg\s+Tulln|\s+Salzburg\-Stadt|\s+Innsbruck|\s+Bruck\s+Eisenstadt\s+Oberwart|\s+Freistadt\s+Rohrbach\s+Urfahr|\s+Tirol\s+Ost|\s+Deutschlandsberg\s+Leibnitz\s+Voitsberg|\s+Purkersdorf|\s+Nieder\u00f6sterreich\s+Mitte|\s+Baden\s+M\u00f6dling|\s+Waldviertel|\s+\u00d6sterreich))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.250 | 0.002 | 0.004 | 8 | 2 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 6 | 914 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_50`)


Aufgrund der  Anrechnung von Prüfungen (FA Abweisungsbescheid 61675550) verkürzt sich die Wartezeit auf  ein Semester und beginnt ab März 2023 zu laufen und dauert bis September 2023.

**False Positives:**

- `FA Abweisungsbescheid` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

**False Positives:**

- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`
- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`

> partial: 2  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Bruemmer` (person)
- `Konstanze Bertling` (person)
- `Pabstbergstraße 45, 9135 Unterort, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `88-575/7122` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

**False Positives:**

- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`
- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`

> partial: 2  |  missing annotation: 0

**Gold Entities:**
- `Univ.-Prof.in Jacqueline Bruemmer` (person)
- `Konstanze Bertling` (person)
- `Pabstbergstraße 45, 9135 Unterort, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `88-575/7122` (tax_number)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_50`)


Aufgrund der  Anrechnung von Prüfungen (FA Abweisungsbescheid 61675550) verkürzt sich die Wartezeit auf  ein Semester und beginnt ab März 2023 zu laufen und dauert bis September 2023.

**False Positives:**

- `FA Abweisungsbescheid` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Pastl+Bächle Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Pastl+Bächle Handel' which was missing from the rules.

**Content:**
```
\bPastl\+Bächle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht Zell am See`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirksgericht Zell am See'.

**Content:**
```
\bBezirksgericht\s+Zell\s+am\s+See\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Klusner&Päffgen Bildung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Klusner&Päffgen Bildung GMBH' which was missing and causing total misses.

**Content:**
```
\bKlusner&Päffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Englert Möbel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Englert Möbel' including cases where it is followed by a hyphenated suffix (e.g., 'Englert Möbel -Konzernes').

**Content:**
```
\b(Englert\s+Möbel)(?:\s*-\w+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank' followed by specific location patterns, extended to capture full multi-word locations like 'Karnische Rion Bankstelle St.Stefan'.

**Content:**
```
\bRaiffeisenbank\s+(?:Hippach-Hart|genburg|Stallhofen|[A-Z][a-zA-Z\-\s]+?)(?=\s*(?:als|an|der|des|die|den|dem|bei|von|mit|f\u00fcr|zur|in|auf|\u00fcber|unter|nach|vor|durch|gegen|ohne|um|bis|seit|statt|trotz|w\u00e4hrend|wegen|laut|neben|au\u00dfer|au\u00dferhalb|innerhalb|entlang|gegen\u00fcber|KG|GmbH|GMBH|AG|&|Co|\s+[a-z]|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Hülsebusch + Breithaupt Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hülsebusch + Breithaupt Versicherung' including cases where it is followed by 'GmbH & Co KG'.

**Content:**
```
\bHülsebusch\s+\+\s+Breithaupt\s+Versicherung(?:\s+GmbH\s+&\s+Co\s+KG)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Logal Gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Logal Gruppe'.

**Content:**
```
\bLogal\s+Gruppe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Enns Werkal GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Enns Werkal GMBH'.

**Content:**
```
\bEnns\s+Werkal\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Süd Nortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Süd Nortri'.

**Content:**
```
\bSüd\s+Nortri\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Trafenfen Automotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Trafenfen Automotive'.

**Content:**
```
\bTrafenfen\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Bundesfinanzgericht Full`

**F1:** 0.233 | **Precision:** 0.500 | **Recall:** 0.152  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its optional suffixes (Außenstelle Linz, (BFG)), but excludes the genitive suffix 'es' or 's' from the extracted text.

**Content:**
```
\bBundesfinanzgericht\b(?:\s*,\s*Außenstelle\s+Linz)?(?:\s*\(\s*BFG\s*(?:\s*\d+\.\s*\d+\.\s*\d+|\s*RV/\d+[^)]*)?\s*\))?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.152 | 0.233 | 278 | 139 | 139 | 0 | 139 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 139 | 139 | 777 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_210`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_226`)


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_227`)


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_236`)


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_251`)


Dass diese Zustellung zu Unrecht erfolgt sei, wurde  nicht behauptet und konnte auch durch das Bundesfinanzgericht nicht erkannt werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_279`)


Das  Bundesfinanzgericht hat grundsätzlich auf Grund der zum Zeitpunkt ihrer Entscheidung  gegebenen Sach- und Rechtslage zu entscheiden (vgl. VwGH 24.3.2009, 2006/13/0149).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_288`)


Die Angaben des Bf.  versetzen das Bundesfinanzgericht nicht in die Lage, abschließend eine persönliche Unbilligkeit  feststellen zu können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_41`)


Daher stelle ich den Antrag auf Entscheidung über die Beschwerde (Vorlageantrag) durch das  Bundesfinanzgericht, ob als Grundlage der Berechnung der Wartezeit bis zur Wiedergewährung  der Familienbeihilfe nur jene Semester des Vorstudiums heranzuziehen sind, für die  Familienbeihilfe bezogen wurde oder alle Semester des Vorstudiums zugrunde zu legen sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_107`)


Im Erkenntnis vom BFG 15.05.2014, RV/7100395/2014 führte das Bundesfinanzgericht  auszugsweise aus:  „In § 2 Abs. 1 lit. b FLAG 1967 wird ausdrücklich darauf verwiesen, dass bei einem  Studienwechsel die in § 17 StudFG angeführten Regelungen auch für den Anspruch auf  9 von 11 Seite 10 von 11

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_114`)


Erwähnt sei auch, dass der von der Bf. zitierte Punkt 02.01.21.14 der Durchführungsrichtlinien  zum Familienlastenausgleichsgesetz 1967 - an die das Bundesfinanzgericht allerdings nicht  gebunden ist - nicht die Wartezeit, sondern die Voraussetzungen für einen schädlichen  Studienwechsel betrifft.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_15`)


Mit Schriftsatz vom 28. Mai 2019 beantragte der Bf die Entscheidung durch das  Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG, Niederau 25, 6731 Bühl, Österreich  tätig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_33`)


Beweiswürdigung  Der entscheidungswesentliche Sachverhalt ergibt sich aus dem dem Bundesfinanzgericht  elektronisch vorgelegten Akt, insbesondere aus den vom Bf eingebrachten Schriftsätzen und  den erlassenen Bescheiden, und ist unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_12`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf hat am 4.1.2024 einen Betrag von 3.141 Euro auf sein Abgabenkonto eingezahlt, ohne  den Betrag mit einer Zweckwidmung zu versehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_27`)


Das Bundesfinanzgericht geht davon aus, dass der Bescheid  jedenfalls noch im Jänner 2018 erlassen wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 24** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker,  Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend  Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 25** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht (BFG)` | `Bundesfinanzgericht (BFG)` |

**Example 26** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 27** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_35`)


Betreffend Einkommensteuerbescheide 2010 und 2011:  Mit als Vorlageantrag zu wertendem Schreiben vom 28.09.2015 beantragte die Bf die Vorlage  der Beschwerden für die Jahre 2010 bis 2011 an das Bundesfinanzgericht zur Entscheidung.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_37`)


Mit Vorlagebericht vom 19.03.2019 wurden die Beschwerden dem Bundesfinanzgericht  übermittelt und beantragte die Behörde weiterhin die Abweisung der Beschwerde als  unbegründet.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_38`)


Mit 07.03.2022, somit bereits nach Vorlage der Beschwerde an das Bundesfinanzgericht, erließ  die belangte Behörde einen Berichtigungsbescheid gem. § 293 BAO zur  Beschwerdevorentscheidung vom 28.08.2015 für das Jahr 2011.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 30** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_41`)


Mit 14.08.2025 übermittelte das Bundesfinanzgericht der belangten Behörde einen Vorhalt zur  Aufklärung der Frage, weshalb (entgegen den Bestimmungen des § 300 BAO) mit 07.03.2022  zur Beschwerdevorentscheidung vom 28.08.2015 durch die belangte Behörde ein  Berichtigungsbescheid nach § 293 BAO erlassen worden war, obwohl die Beschwerde bereits  beim Bundesfinanzgericht anhängig war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 31** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Durch den oben angeführten (aufgrund der Korrektur der Lohnzettel) durch die belangte  Behörde erlassenen Berichtigungsbescheid nach § 293 BAO vom 07.03.2022 wurde dem  Begehren der Bf für das Jahr 2011 vollinhaltlich entsprochen, aufgrund der  Entscheidungssperre des § 300 BAO war der Bescheid jedoch als absolut nichtig zu werten und  somit die Beschwerdesache weiterhin als unerledigt anzusehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 32** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_52`)


Die Zuständigkeit in  gegenständlichem Beschwerdefall liegt daher weiterhin beim Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 33** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_79`)


Aufgrund der beim Dienstgeber der Bf  durchgeführten GPLA den gegenständlichen Beschwerdezeitraum betreffend, werden die  Werte vom Bundesfinanzgericht als unstrittig angenommen und werden diese auch seitens der  belangten Behörde in der Vorhaltsbeantwortung vom 26.08.2025 als korrekt angesehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_80`)


Die obigen Sachverhaltsdarstellungen werden daher gem. § 167 Abs 2 BAO vom  Bundesfinanzgericht als erwiesen angenommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 35** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_86`)


Da diese Ausnahmevoraussetzungen in gegenständlichem Fall nicht gegeben sind, ist der durch  die belangte Behörde erlassene Bescheid absolut nichtig und liegt die Zuständigkeit in  gegenständlichem Beschwerdeverfahren weiterhin beim Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 36** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_100`)


Aufgrund des Verfahrensganges und insbesondere der Ausführungen der belangen Behörde im  Schreiben zur Vorhaltsbeantwortung vom 26.08.2025 geht das Bundesfinanzgericht nunmehr  davon aus, dass es unstrittig ist, dass die Grundregel des Art 15 Abs 1 und das damit  zusammenhängende Arbeitsortprinzip in gegenständlichem Fall zutreffend ist und Art 15 Abs 2  DBA nicht anzuwenden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 37** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_106`)


Im vorliegenden Fall handelt es sich um keine Rechtfrage von grundsätzlicher Bedeutung, da  das Bundesfinanzgericht in rechtlicher Hinsicht der in der Entscheidung dargestellten Judikatur  des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 38** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 39** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_36`)


Die Bescheidbeschwerde wurde am 14.4.2025 dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 40** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_37`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 41** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_96`)


Im gegenständlichen Fall orientiert sich das Bundesfinanzgericht an der zitierten ständigen  Judikatur des Verwaltungsgerichtshofes, sodass keine Rechtsfrage von grundsätzlicher  Bedeutung zu klären war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 42** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 43** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_13`)


Die daraufhin an die Beschwerdeführerin als „Bescheid gemäß § 201 Bundesabgabenordnung  über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1 Gebührengesetz 1957“ bzw „Bescheid  über die Festsetzung von Gebührenerhöhungen gemäß § 9 GebG 1957“ betreffend die Jahre  2010 bis 2012 übermittelten Schriftstücke, jeweils datiert mit 18.7.2014, wurden vom  Bundesfinanzgericht mit Beschluss vom 28.8.2018, RV/7104136/2015, aufgrund eines  erheblichen Zustellmangels als rechtlich nicht existent gewordene Erledigungen qualifiziert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 44** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_19`)


Mit Eingabe vom 27.4.2020 beantragte die Beschwerdeführerin die Vorlage an das  Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 45** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_21`)


Im Zuge der am 20.4.2021 am Bundesfinanzgericht abgehaltenen mündlichen Verhandlung  erfolgte mit den Vertretern der Beschwerdeführerin und der belangten Behörde die Erörterung  der Sach- und Rechtsfragen und weiteres Vorbringen wurde zur Niederschrift genommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 46** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_46`)


Das Bundesfinanzgericht hat erwogen  1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 47** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_194`)


Dem wird vom Bundesfinanzgericht wiederum entgegengehalten, dass die Zweifelsregel nach  § 915 ABGB im gegenständlichen Fall gar nicht zur Anwendung gelangen kann, da der der  betreffenden Klausel zugrundeliegende Parteiwille nämlich bereits im Weg der einfachen  Vertragsauslegung nach § 914 ABGB klar feststellbar ist: Ohne Zustimmung der  Beschwerdeführerin als Leasinggeberin soll der Leasingnehmer innerhalb der vereinbarten  Kalkulationsbasisdauer den Vertrag nicht aus freiem Willen beenden können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 48** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_203`)


Dem hält das Bundesfinanzgericht zunächst entgegen, dass der Beschwerdeführerin als  Leasinggeberin ohnehin kein ordentliches Kündigungsrecht zukommt (siehe dazu die unten  getroffene Beurteilung).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 49** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_243`)


Dem von der Beschwerdeführerin vorgenommenen Verweis auf die Entscheidung des OGH  vom 16.1.2003, 2 Ob 311/02b, nach der sich ergebe, dass, wenn die ordentliche Kündigung  nicht erwähnt werde, dennoch auf die ordentliche Kündigung nicht verzichtet worden sei, und  das Recht zur ordentlichen Kündigung daher bestehen bleibe, tritt das Bundesfinanzgericht  damit entgegen, dass im Sachverhalt des zitierten OGH-Urteils offenbar überhaupt keine  Regelungen zur ordentlichen Kündigung getroffen wurden;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_210`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_226`)


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_227`)


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `USA` (country)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_236`)


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_251`)


Dass diese Zustellung zu Unrecht erfolgt sei, wurde  nicht behauptet und konnte auch durch das Bundesfinanzgericht nicht erkannt werden.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_279`)


Das  Bundesfinanzgericht hat grundsätzlich auf Grund der zum Zeitpunkt ihrer Entscheidung  gegebenen Sach- und Rechtslage zu entscheiden (vgl. VwGH 24.3.2009, 2006/13/0149).

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_288`)


Die Angaben des Bf.  versetzen das Bundesfinanzgericht nicht in die Lage, abschließend eine persönliche Unbilligkeit  feststellen zu können.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_27`)


Das Bundesfinanzgericht geht davon aus, dass der Bescheid  jedenfalls noch im Jänner 2018 erlassen wurde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `80-738/9953` (tax_number)

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_24`)


Mit Eingabe vom 21. Mai 2024 beantragte der Bf. innerhalb verlängerter Frist die Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht sowie die Durchführung einer  mündlichen Verhandlung.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_26`)


Am 13. Juni 2024 legte die belangte Behörde die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_31`)


Am 1. Oktober 2025 fand die beantragte mündliche Verhandlung vor dem Bundesfinanzgericht  statt, in der insbesondere das Vorliegen bzw. Nichtvorliegen von triftigen medizinischen  Gründen diskutiert wurde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_36`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. bezieht im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_63`)


Das Bundesfinanzgericht kommt aus den nachstehenden Gründen im Rahmen der freien  Beweiswürdigung zum Ergebnis, dass die nach der höchstgerichtlichen Rechtsprechung  geforderten triftigen medizinischen Gründe nicht vorliegen:  Zunächst steht unstrittig fest, dass in keinem öffentlichen Krankenhaus eine Terminanfrage  betreffend die Bandscheibenoperation der Ehefrau des Bf. gestellt wurde (vgl. Protokoll zur  Verhandlung vom 1. Oktober 2025 sowie Befundberichte vom 6. und 8. Oktober 2025).

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_102`)


das Bundesfinanzgericht ist vielmehr an diesen Schuldspruch gebunden (VwGH 29.6.1999,  98/14/0177;

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_183`)


Gemäß § 161 Abs. 1 FinStrG hat das Bundesfinanzgericht, sofern die Beschwerde nicht gemäß  § 156 mit Beschluss zurückzuweisen ist, grundsätzlich in der Sache selbst mit Erkenntnis zu  entscheiden.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Univ.-Prof.in Jacqueline Bruemmer` (person)
- `Konstanze Bertling` (person)
- `Pabstbergstraße 45, 9135 Unterort, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `88-575/7122` (tax_number)

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_15`)


Mit Schriftsatz vom 28. Mai 2019 beantragte der Bf die Entscheidung durch das  Bundesfinanzgericht.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG, Niederau 25, 6731 Bühl, Österreich  tätig.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Nexkelkel AG` (organisation)
- `Niederau 25, 6731 Bühl, Österreich` (address)

**Example 23** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_33`)


Beweiswürdigung  Der entscheidungswesentliche Sachverhalt ergibt sich aus dem dem Bundesfinanzgericht  elektronisch vorgelegten Akt, insbesondere aus den vom Bf eingebrachten Schriftsätzen und  den erlassenen Bescheiden, und ist unstrittig.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 24** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker,  Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend  Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Dr. Zacharias Lüdike` (person)
- `Felix Stukenbröker` (person)
- `Lenzenkreuzweg 29, 9232 Frög, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)
- `23-124/1598` (tax_number)

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

**False Positives:**

- `Bundesfinanzgericht (BFG)` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `FAÖ` (organisation)

**Example 26** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache HR KzlR Stephanie Ganssloser, Schwemmgasse 16, 8992 Fischerndorf, Österreich, betreffend Beschwerde vom 8. April 2025 gegen  den Bescheid des Finanzamtes Österreich vom 10. März 2025 betreffend Säumniszuschlag  10.03.2025 zur Steuernummer 16-527/7844  beschlossen:   Die Beschwerde vom 8. April 2025 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag. Markus Knechtl LL.M.` (person)
- `HR KzlR Stephanie Ganssloser` (person)
- `Schwemmgasse 16, 8992 Fischerndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `16-527/7844` (tax_number)

**Example 27** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_15`)


Mit Beschluss vom 26.8.2025 wies das Bundesfinanzgericht die Beschwerdeführerin darauf hin,  dass einerseits die angekündigte Begründung zur Beschwerde nie nachgereicht wurde und dass  andererseits bei der Festsetzung von Säumniszuschlägen kein Ermessen zu üben sei (VwGH  26.3.2025, Ra 2025/13/0016).

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 28** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Pawel Heldt  in der Beschwerdesache  Samir Krahnepuhl, Webersberg 40, 7331 Kalkgruben, Österreich, über die Beschwerde vom 18. September 2023 gegen den  Bescheid des Finanzamtes Österreich vom 7. September 2023 betreffend Abweisung des  Antrags auf Wiedereinsetzung in den vorigen Stand vom 5. August 2023, Steuernummer  88-903/5443, zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Dr. Pawel Heldt` (person)
- `Samir Krahnepuhl` (person)
- `Webersberg 40, 7331 Kalkgruben, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-903/5443` (tax_number)

**Example 29** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_51`)


Das FAÖ legte die Beschwerde am 4. März 2024 dem Bundesfinanzgericht vor und beantragte  die Abweisung der Beschwerde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `FAÖ` (organisation)

**Example 30** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Bundesministerium für Finanzen` (organisation)

**Example 31** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_90`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der BF war als Intermediär verpflichtet, bis zum 27. Juli 2023 eine Meldung nach dem EU-MPfG  abzugeben.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 32** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag. Johann Fischerlehner` (person)
- `Veronika Ogrissek` (person)
- `Weißeneggerberg 160, 3631 Kienings, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `48-541/5488` (tax_number)

**Example 33** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_36`)


Die Bescheidbeschwerde wurde am 14.4.2025 dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 34** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_37`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 35** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_96`)


Im gegenständlichen Fall orientiert sich das Bundesfinanzgericht an der zitierten ständigen  Judikatur des Verwaltungsgerichtshofes, sodass keine Rechtsfrage von grundsätzlicher  Bedeutung zu klären war.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 36** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Wilma Kewer, Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich, über die Beschwerde vom 17. August 2025  gegen den Bescheid des Finanzamtes Österreich vom 04. August 2025 betreffend die  Verzinsung der Rückerstattung gem. § 16 COFAG-NoAG (Steuernummer 45-588/1819 ) zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag. Patrick Brandstetter` (person)
- `Wilma Kewer` (person)
- `Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `45-588/1819` (tax_number)

**Example 37** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_9`)


Diese Beschwerde wurde vom Finanzamt mit dem Vermerk, dass sich das  Beschwerdevorbringen ausschließlich auf das Prinzip der Rechtsstaatlichkeit beziehe, ohne  Erlassung einer Beschwerdevorentscheidung gem. § 262 Abs. 3 BAO direkt dem  Bundesfinanzgericht vorgelegt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 38** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_10`)


Im Zuge eines Vorhalteverfahrens durch das Bundesfinanzgericht legte die Beschwerdeführerin  den Schriftverkehr mit der COFAG bzgl.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `COFAG` (organisation)

**Example 39** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_52`)


In Anbetracht dieser Ausführungen zeigt sich, dass die verfassungsrechtlichen Bedenken der  Beschwerdeführerin vom Bundesfinanzgericht nicht geteilt werden und musste daher der  Beschwerde der Erfolg versagt bleiben.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 40** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Arielle Billmaier  in der Beschwerdesache Elena Dämel,  Römerstraße-Palfen 44E, 9431 Thürn, Österreich, betreffend Beschwerde vom 10. Juli 2025 gegen den Bescheid des Finanzamtes  Österreich vom 3. Juni 2025 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2024,  Steuernummer 70-316/9622  beschlossen:  I.Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag.a Arielle Billmaier` (person)
- `Elena Dämel` (person)
- `Römerstraße-Palfen 44E, 9431 Thürn, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `70-316/9622` (tax_number)

**Example 41** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_15`)


Mit Bericht vom 17.09.2025 legte die belangte Behörde die oa Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Beschwerde als verspätet  zurückzuweisen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 42** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_20`)


Zu diesem, dem Bf am 14. Oktober 2025 (Beginn der Abholfrist) gem. § 17 Zustellgesetz  zugestellten Schreiben, langte bis dato keine Stellungnahme beim Bundesfinanzgericht ein.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 43** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_21`)


B. Beweiswürdigung:  Der streitwesentliche Sachverhalt ergibt sich für das Bundesfinanzgericht aus der vorliegenden  Aktenlage, insbesondere aus den oben angeführten Unterlagen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 44** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_23`)


Das Bundesfinanzgericht hat keinen Zweifel  an der Richtigkeit dieser Daten.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 45** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Dr. Wolfgang Pavlik` (person)
- `Desiree Häfke` (person)
- `Weinrebengasse 209, 4282 Hinterhütten, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 46** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Universität Wien` (organisation)

**Example 47** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Dr. Wiebke Peperkorn in der  Beschwerdesache Sophie Zekalla, Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich, über die Beschwerde vom 29. April 2024 gegen  den Bescheid des Finanzamtes Österreich vom 24. April 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 71-479/6461  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag. Dr. Wiebke Peperkorn` (person)
- `Sophie Zekalla` (person)
- `Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `71-479/6461` (tax_number)

**Example 48** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_10`)


Dagegen brachte der Bf. am 8.10.2024 den Antrag auf Entscheidung über die Beschwerde  (Vorlageantrag) durch das Bundesfinanzgericht ein.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 49** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_11`)


Am 9.10.2024 wurde die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorgelegt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Verwaltungsgerichtshof Specific`

**F1:** 0.216 | **Precision:** 0.500 | **Recall:** 0.138  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs', including the optional acronym '(VwGH)'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?(?:\s*\(\s*VwGH\s*\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.138 | 0.216 | 252 | 126 | 126 | 0 | 126 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 126 | 126 | 788 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_118`)


Der Verwaltungsgerichtshof hat zum schädlichen und unschädlichen Studienwechsel folgende  Judikatur entwickelt:  Ein Studienwechsel iSd § 17 StudFG liegt vor, wenn der/die Studierende das von ihm/ihr  begonnene und bisher betriebene, aber noch nicht abgeschlossene Studium nicht mehr  fortsetzt und an dessen Stelle ein anderes unter den Geltungsbereich des StudFG fallendes  Studium beginnt (VwGH 26.05.2011, 2011/16/0060).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_146`)


Entgegen der Rechtsansicht des Bf, dass der erste tatsächliche Studienwechsel zum Studium  der biotechnischen Verfahren erfolgt ist, gilt auch der Rückwechsel vom Bachelorstudium  Wirtschaftsrecht auf das Studium Rechtswissenschaften nach der zitierten Judikatur des  Verwaltungsgerichtshofes (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_163`)


Subjektive  Momente, wie Verschulden an der (ursprünglichen oder weiteren) Auszahlung der  Familienleistungen, Gutgläubigkeit des Empfangs der Familienbeihilfe und des  Kinderabsetzbetrags oder die Verwendung der Familienbeihilfe und des Kinderabsetzbetrags,  sind nach ständiger Rechtsprechung des Verwaltungsgerichtshofes für die Verpflichtung zur  Rückerstattung unrechtmäßiger Beihilfenbezüge unerheblich.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_124`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_45`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes besteht keine Entscheidungspflicht  betreffend Anregung einer Wiederaufnahme des Verfahrens (VwGH 22.5.2014, 2011/15/0064,  VwGH 20.2.2019, Ro 2016/13/0011).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_63`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (vgl. VwGH 16.10.2016, Ra  2014/15/0058) ist bei einem Antrag auf Wiederaufnahme des Verfahrens das  Neuhervorkommen von Tatsachen aus Sicht des Antragstellers zu beurteilen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_70`)


Das Erkenntnis folgt der zitierten Rechtsprechung des Verwaltungsgerichtshofes und liegt  damit keine Rechtsfrage grundsätzlicher Bedeutung vor.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_28`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_73`)


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_4`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 24** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_3`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 25** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_105`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 26** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_106`)


Im vorliegenden Fall handelt es sich um keine Rechtfrage von grundsätzlicher Bedeutung, da  das Bundesfinanzgericht in rechtlicher Hinsicht der in der Entscheidung dargestellten Judikatur  des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 27** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_3`)


III. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_92`)


Laut Rechtsprechung des Verwaltungsgerichtshofes wird das  Rechtsschutzinteresse des Abgabepflichtigen dadurch nicht verletzt, weil gegen den Bescheid  betreffend Pfändung sowohl das Beschwerderecht als auch die Revision an den  Verwaltungsgerichtshof offensteht (VwGH 23.11.1994, 94/13/0246).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 29** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_95`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 30** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_96`)


Im gegenständlichen Fall orientiert sich das Bundesfinanzgericht an der zitierten ständigen  Judikatur des Verwaltungsgerichtshofes, sodass keine Rechtsfrage von grundsätzlicher  Bedeutung zu klären war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 31** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_4`)


II. Die Revision an den Verwaltungsgerichtshof ist gemäß Art 133 Abs 4 B-VG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 32** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_180`)


Zur gebührenrechtlich maßgeblichen Vertragsdauer  Nach ständiger Judikatur des Verwaltungsgerichtshofs ist für die Frage, ob gebührenrechtlich  ein Vertrag von bestimmter oder unbestimmter Dauer vorliegt, nicht die von den Parteien  gewählte Bezeichnung des Vertrags, sondern der gesamte Vertragsinhalt maßgebend (vgl etwa  VwGH 16.10.2014, 2011/16/0169;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 33** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_263`)


Das von der  Beschwerdeführerin angeführte Erkenntnis des Verwaltungsgerichtshofs vom 2.7.1981,  15/0701/80, vermag somit ihren Standpunkt nicht zu unterstützen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 34** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_324`)


Zu Spruchpunkt II. (Unzulässigkeit der Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 35** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_325`)


Die Lösung der gegenständlich aufgeworfenen Rechtsfragen gründet sich auf der  Rechtsprechung des Verwaltungsgerichtshofs.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 36** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_47`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes ist Voraussetzung für die  Zurückweisung eines Rechtsmittels als verspätet allein die Versäumung der Rechtsmittelfrist  und nicht auch ein Verschulden der Partei an der Verspätung (vgl. VwGH 22.09.1989,  89/11/0184, VwGH 11.07.1988, 88/10/0113).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 37** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_50`)


Da eine nicht rechtzeitig eingebrachte Beschwerde mit Beschluss zurückzuweisen ist, war es  dem Bundesfinanzgericht – in Entsprechung der Judikatur des Verwaltungsgerichtshofes (vgl  VwGH 09.09.2015, Ra 2015/03/0032, VwGH 18.12.2014, Ra 2014/07/0002, 0003) - verwehrt,  auf das Vorbringen des Bf., wonach er das Fahrzeug unter Einhaltung sämtlicher gesetzlicher  Bestimmungen gelenkt und sich ordnungsgemäß verhalten habe, einzugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 38** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_53`)


Zur Unzulässigkeit einer Revision  Gemäß Art. 133 Abs. 4 B-VG iVm Art. 133 Abs. 9 B-VG und § 25a Abs. 1 VwGG ist gegen einen  die Angelegenheit abschließenden Beschluss des Bundesfinanzgerichtes die Revision zulässig,  wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 39** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_7`)


3. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 40** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_23`)


8.  Der dagegen erhobenen Revision gab der Verwaltungsgerichtshof mit Erkenntnis vom  19. Dezember 2024, Ro 2023/15/0003, Folge und hob das Erkenntnis des Bundesfinanzge- richtes auf, weil das Bundesfinanzgericht es bei grundsätzlicher Vergleichbarkeit der Systeme  in Verkennung der Rechtslage unterlassen habe, die aus dem Ausland bezogene Geldleistung  jener gegenüber zu stellen, die beim konkret gegebenen Sachverhalt aus einer inländischen  gesetzlichen Unfallversorgung zu gewähren gewesen wäre.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 41** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_24`)


9.  Mit Vorhalt vom 28. Jänner 2025 ersuchte das Bundesfinanzgericht das Finanzamt unter  Verweis auf die Ausführungen des Verwaltungsgerichtshofes, zu ermitteln, ob und allenfalls  in welcher Höhe der Beschwerdeführer bei der gegebenen Sachlage einen Anspruch auf Ver- sehrtenrente nach § 203 ASVG hätte, wenn er im Inland versichert gewesen wäre und ob ihm  nach österreichischem Recht eine Schwerversehrtenrente zustünde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 42** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_64`)


Mit Erkenntnis vom 19. Dezember 2024, Ro 2023/15/0003, hob der Verwaltungsgerichtshof  das die Gleichartigkeit der von der SUVA ausbezahlten Invalidenrente und Geldleistungen aus  der gesetzlichen inländischen Unfallversorgung verneinende Erkenntnis des Bundesfinanzge- richtes vom 30. September 2022, RV/1100086/2019, wegen inhaltlicher Rechtswidrigkeit auf.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 43** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_65`)


Begründend führte der Verwaltungsgerichtshof dazu auszugsweise Folgendes aus:  „Gemäß § 203 Abs. 1 ASVG gebührt eine Versehrtenrente, wenn die Erwerbsfähigkeit des Ver- sehrten durch die Folgen eines Arbeitsunfalles oder eine Berufskrankheit über drei Monate nach  dem Eintritt des Versicherungsfalles hinaus um mindestens 20 % vermindert ist;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 44** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_73`)


Die Revision bringt zur Gleichartigkeit der von der SUVA ausbezahlten Schweizer Invalidenrente  Folgendes vor:   […]  Der Verwaltungsgerichtshof stimmt den Ausführungen der Revision zu, dass eine Gleichartig- keit der Leistungen iSd § 3 Abs. 1 Z 4 lit. c EStG 1988 keine völlige Identität in deren gesetzlicher  Ausgestaltung voraussetzt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 45** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_74`)


Wie der Verwaltungsgerichtshof bereits mehrfach ausgesprochen hat, besteht das Wesens- merkmal der österreichischen Versehrtenrente aus der gesetzlichen Unfallversorgung (Pflicht- versicherung) darin, dass sie bei Eintritt des versicherten Risikos dem Ausgleich des durch die  unfallbedingte Erwerbsminderung eintretenden Schadens dienen soll.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 46** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_78`)


Wie der Verwaltungsgerichtshof bereits in seinem Erkenntnis vom 28. Juni 2012, 2009/15/0069,  ausgesprochen hat, ist zur Prüfung der Gleichartigkeit der ausländischen Leistung iSd § 3 Abs. 1  Z 4 lit. c EStG 1988 die aus dem Ausland bezogene Geldleistung jener gegenüber zu stellen, die  beim konkret gegebenen Sachverhalt aus einer inländischen gesetzlichen Unfallversorgung zu  gewähren gewesen wäre.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 47** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_85`)


Im Sinne der Ausführungen des Verwaltungsgerichtshofes im  Erkenntnis vom 19. Dezember 2024, Ro 2023/15/0003, handelt es sich dabei um jene Leistung,  die beim konkret gegebenen Sachverhalt aus einer inländischen gesetzlichen Unfallversorgung  zu gewähren gewesen wäre und war die schweizerische Invalidenrente daher in diesem Um- fang steuerfrei zu belassen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 48** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_123`)


2.4. Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 49** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_124`)


Die im Beschwerdefall strittige Frage, ob es sich bei einer infolge eines Arbeitsunfalles von der  Schweizerischen Unfallversicherungsanstalt (SUVA) ausbezahlten Invalidenrente um eine mit  einer Geldleistung aus der inländischen gesetzlichen Unfallversorgung gleichartige ausländi- sche Leistung im Sinne des § 3 Abs. 1 Z 4 lit. c EStG 1988 handelt, ist durch das Erkenntnis des  Verwaltungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, geklärt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_73`)


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_107`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_14`)


3. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_97`)


Über die Beschwerde wurde erwogen:  Teilrechtskraft:  Laut ständiger Rechtsprechung des Verwaltungsgerichtshofes ist im Bereich des  Finanzstrafrechtes Teilrechtskraft hinsichtlich des Ausspruches von Schuld einerseits und Strafe  andererseits rechtlich möglich (vgl. VwGH 8.2.2007, 2006/15/0293).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_188`)


Zur subjektiven Tatseite ist zunächst auf die Rechtsprechung des Verwaltungsgerichtshofes zu  verweisen, wonach Vorsatz eine zielgerichtete subjektive Einstellung des Täters bedeutet, auf  deren Vorhandensein oder Nichtvorhandensein nur nach seinem nach außen in Erscheinung  tretenden Verhalten unter Würdigung aller sonstigen Sachverhaltselemente geschlossen  werden kann (VwGH 29.3.2007, 2006/16/0062).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_272`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_45`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes besteht keine Entscheidungspflicht  betreffend Anregung einer Wiederaufnahme des Verfahrens (VwGH 22.5.2014, 2011/15/0064,  VwGH 20.2.2019, Ro 2016/13/0011).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_63`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (vgl. VwGH 16.10.2016, Ra  2014/15/0058) ist bei einem Antrag auf Wiederaufnahme des Verfahrens das  Neuhervorkommen von Tatsachen aus Sicht des Antragstellers zu beurteilen.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_70`)


Das Erkenntnis folgt der zitierten Rechtsprechung des Verwaltungsgerichtshofes und liegt  damit keine Rechtsfrage grundsätzlicher Bedeutung vor.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_4`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 23** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 24** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_3`)


Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_23`)


Zur Unzulässigkeit einer Revision   Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 26** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_3`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof  nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 27** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_124`)


Da die versäumte Handlung im beschwerdegegenständlichen Fall nicht spätestens gleichzeitig  mit dem Antrag auf Wiedereinsetzung nachgeholt wurde, ist dieser Antrag im Einklang mit der  Rechtsprechung des Verwaltungsgerichtshofs zurückzuweisen.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 28** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_128`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 29** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_3`)


III. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht  zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 30** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_92`)


Laut Rechtsprechung des Verwaltungsgerichtshofes wird das  Rechtsschutzinteresse des Abgabepflichtigen dadurch nicht verletzt, weil gegen den Bescheid  betreffend Pfändung sowohl das Beschwerderecht als auch die Revision an den  Verwaltungsgerichtshof offensteht (VwGH 23.11.1994, 94/13/0246).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 31** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_95`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 32** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_96`)


Im gegenständlichen Fall orientiert sich das Bundesfinanzgericht an der zitierten ständigen  Judikatur des Verwaltungsgerichtshofes, sodass keine Rechtsfrage von grundsätzlicher  Bedeutung zu klären war.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 33** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 34** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_53`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 35** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_2`)


II.Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 36** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_63`)


Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 37** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 38** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_118`)


Der Verwaltungsgerichtshof hat zum schädlichen und unschädlichen Studienwechsel folgende  Judikatur entwickelt:  Ein Studienwechsel iSd § 17 StudFG liegt vor, wenn der/die Studierende das von ihm/ihr  begonnene und bisher betriebene, aber noch nicht abgeschlossene Studium nicht mehr  fortsetzt und an dessen Stelle ein anderes unter den Geltungsbereich des StudFG fallendes  Studium beginnt (VwGH 26.05.2011, 2011/16/0060).

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 39** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_146`)


Entgegen der Rechtsansicht des Bf, dass der erste tatsächliche Studienwechsel zum Studium  der biotechnischen Verfahren erfolgt ist, gilt auch der Rückwechsel vom Bachelorstudium  Wirtschaftsrecht auf das Studium Rechtswissenschaften nach der zitierten Judikatur des  Verwaltungsgerichtshofes (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 40** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_163`)


Subjektive  Momente, wie Verschulden an der (ursprünglichen oder weiteren) Auszahlung der  Familienleistungen, Gutgläubigkeit des Empfangs der Familienbeihilfe und des  Kinderabsetzbetrags oder die Verwendung der Familienbeihilfe und des Kinderabsetzbetrags,  sind nach ständiger Rechtsprechung des Verwaltungsgerichtshofes für die Verpflichtung zur  Rückerstattung unrechtmäßiger Beihilfenbezüge unerheblich.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 41** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 42** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 43** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_69`)


Zu Spruchpunkt II. (Unzulässigkeit der Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 44** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_47`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes ist Voraussetzung für die  Zurückweisung eines Rechtsmittels als verspätet allein die Versäumung der Rechtsmittelfrist  und nicht auch ein Verschulden der Partei an der Verspätung (vgl. VwGH 22.09.1989,  89/11/0184, VwGH 11.07.1988, 88/10/0113).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 45** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_50`)


Da eine nicht rechtzeitig eingebrachte Beschwerde mit Beschluss zurückzuweisen ist, war es  dem Bundesfinanzgericht – in Entsprechung der Judikatur des Verwaltungsgerichtshofes (vgl  VwGH 09.09.2015, Ra 2015/03/0032, VwGH 18.12.2014, Ra 2014/07/0002, 0003) - verwehrt,  auf das Vorbringen des Bf., wonach er das Fahrzeug unter Einhaltung sämtlicher gesetzlicher  Bestimmungen gelenkt und sich ordnungsgemäß verhalten habe, einzugehen.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 46** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_53`)


Zur Unzulässigkeit einer Revision  Gemäß Art. 133 Abs. 4 B-VG iVm Art. 133 Abs. 9 B-VG und § 25a Abs. 1 VwGG ist gegen einen  die Angelegenheit abschließenden Beschluss des Bundesfinanzgerichtes die Revision zulässig,  wenn sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 47** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 48** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_241`)


Bei Reitställen zählen der Rechtsprechung des  Verwaltungsgerichtshofs zufolge Anzahl und Umfang der Wirtschaftsgüter und die Qualität der  Betätigung.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 49** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_258`)


Unter einem absehbaren Zeitraum zur Erzielung  eines wirtschaftlichen Gesamterfolges wird nach der Rechtsprechung des  Verwaltungsgerichtshofs eine Zeitspanne verstanden, die zum getätigten Mitteleinsatz bei  Betrachtung der Umstände des konkreten Falles in einer nach der Verkehrsauffassung  vernünftigen, üblichen Relation steht (VwGH 03.07.1996, 93/13/0171 (übliche  Rentabilitätsdauer des geleisteten Mitteleinsatzes).

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `SUVA Acronym`

**F1:** 0.098 | **Precision:** 0.750 | **Recall:** 0.052  

**Format:** `regex`  
**Description:**
Matches the acronym 'SUVA' as a standalone organization name.

**Content:**
```
\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.750 | 0.052 | 0.098 | 64 | 48 | 16 | 12 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 48 | 16 | 528 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_11`)


Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_12`)


Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_13`)


3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_14`)


4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_18`)


5.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer mit Beschwerde und – nach Ergehen abweisender Beschwer- devorentscheidungen – mit Vorlageantrag wandte.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_19`)


6.  Mit am 11. Februar 2022 elektronisch eingereichtem Anbringen gab die steuerliche Vertre- tung unter Anschluss einer E-Mail des Steueramtes des Kantons Luzern, wonach die Schweiz  nach Art. 19 DBA-Schweiz das Recht habe, die von der SUVA (öffentlich-rechtlich) ausbezahlte  Rente zu besteuern, bekannt, dass sein Antrag auf Rückerstattung der Schweizer Quellensteuer  in der Schweiz abgewiesen worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_21`)


von der SUVA bezogenen Rente wie auch die Abzugsfähigkeit der von der Schweiz einbehal- tenen Quellensteuer und gab der Beschwerde gegen den Einkommensteuerbescheid 2015 ge- samthaft gesehen im Umfang der Beschwerdevorentscheidung (Höhe der Schweizer Invaliden- renten, Nichtberücksichtigung einer Pensionskassenleistung) teilweise Folge.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_22`)


Die einzig die  Frage der Steuerpflicht der von der SUVA ausbezahlten Invalidenrente betreffenden Beschwer- den gegen den Einkommensteuerbescheid 2016 und die Einkommensteuervorauszahlungsbe- scheide 2017 sowie 2018 und Folgejahre wurden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_34`)


Es werde dazu auf die Verfügung der  SUVA vom 8. Jänner 2024 sowie auf die Untersuchungsberichte des Kantonsspitals St. Gallen  und weitere ärztliche Untersuchungsberichte verwiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_35`)


Die Unterlagen, welche großteils an  die SUVA gerichtet seien, dürften dabei auch die Grundlage für die Einschätzung der festge- stellten Invalidität darstellen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_39`)


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_45`)


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_50`)


Dem- nach wurde die Minderung der Erwerbsfähigkeit im Hinblick auf die im Einzelnen angeführten  unfallkausalen Diagnosen und Verletzungsfolgen sowie die Beurteilung des Integritätsschadens  nach Gutachten der SUVA mit ärztlicher Abschlussuntersuchung am 22. Juli 2013 mit 30 % be- wertet.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_60`)


Betreffend das Jahr 2015 wurde von der SUVA Quellensteuer in Höhe von 5.623,80 CHF einbe- halten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_64`)


Mit Erkenntnis vom 19. Dezember 2024, Ro 2023/15/0003, hob der Verwaltungsgerichtshof  das die Gleichartigkeit der von der SUVA ausbezahlten Invalidenrente und Geldleistungen aus  der gesetzlichen inländischen Unfallversorgung verneinende Erkenntnis des Bundesfinanzge- richtes vom 30. September 2022, RV/1100086/2019, wegen inhaltlicher Rechtswidrigkeit auf.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_73`)


Die Revision bringt zur Gleichartigkeit der von der SUVA ausbezahlten Schweizer Invalidenrente  Folgendes vor:   […]  Der Verwaltungsgerichtshof stimmt den Ausführungen der Revision zu, dass eine Gleichartig- keit der Leistungen iSd § 3 Abs. 1 Z 4 lit. c EStG 1988 keine völlige Identität in deren gesetzlicher  Ausgestaltung voraussetzt.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_107`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_115`)


Das Finanzamt hat die Einkommensteuervorauszahlungen für die Jahre 2017 sowie 2018 und  Folgejahren mit Bescheiden vom 4. Juli 2017 bzw. vom 27. November 2017 gemäß § 45 Abs. 4  EStG 1988 mit 24.000,00 € (2017) bzw. 22.391,00 € (2018) festgesetzt, wobei die von der SUVA  bezogene Invalidenrente jeweils als zur Gänze steuerpflichtig berücksichtigt wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_118`)


Wie oben dargelegt, wurde die von der SUVA bezogene Invalidenrente zu Unrecht zur Gänze  der Besteuerung unterzogen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_121`)


Gesamthaft gesehen war den Beschwerden gegen die Einkommensteuerbescheide 2015 und  2016 somit (hinsichtlich des Jahres 2015 über den Umfang der Beschwerdevorentscheidung  hinaus) insoweit teilweise Folge zu geben, als die von der SUVA bezogene Invalidenrente im  oben genannten Ausmaß steuerfrei zu belassen war.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_11`)


Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 23** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_12`)


Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 24** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_13`)


3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_14`)


4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 26** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_18`)


5.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer mit Beschwerde und – nach Ergehen abweisender Beschwer- devorentscheidungen – mit Vorlageantrag wandte.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 27** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_19`)


6.  Mit am 11. Februar 2022 elektronisch eingereichtem Anbringen gab die steuerliche Vertre- tung unter Anschluss einer E-Mail des Steueramtes des Kantons Luzern, wonach die Schweiz  nach Art. 19 DBA-Schweiz das Recht habe, die von der SUVA (öffentlich-rechtlich) ausbezahlte  Rente zu besteuern, bekannt, dass sein Antrag auf Rückerstattung der Schweizer Quellensteuer  in der Schweiz abgewiesen worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 28** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_21`)


von der SUVA bezogenen Rente wie auch die Abzugsfähigkeit der von der Schweiz einbehal- tenen Quellensteuer und gab der Beschwerde gegen den Einkommensteuerbescheid 2015 ge- samthaft gesehen im Umfang der Beschwerdevorentscheidung (Höhe der Schweizer Invaliden- renten, Nichtberücksichtigung einer Pensionskassenleistung) teilweise Folge.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 29** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_22`)


Die einzig die  Frage der Steuerpflicht der von der SUVA ausbezahlten Invalidenrente betreffenden Beschwer- den gegen den Einkommensteuerbescheid 2016 und die Einkommensteuervorauszahlungsbe- scheide 2017 sowie 2018 und Folgejahre wurden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 30** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 31** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 32** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_34`)


Es werde dazu auf die Verfügung der  SUVA vom 8. Jänner 2024 sowie auf die Untersuchungsberichte des Kantonsspitals St. Gallen  und weitere ärztliche Untersuchungsberichte verwiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 33** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_35`)


Die Unterlagen, welche großteils an  die SUVA gerichtet seien, dürften dabei auch die Grundlage für die Einschätzung der festge- stellten Invalidität darstellen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 34** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_39`)


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 35** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_45`)


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 36** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_50`)


Dem- nach wurde die Minderung der Erwerbsfähigkeit im Hinblick auf die im Einzelnen angeführten  unfallkausalen Diagnosen und Verletzungsfolgen sowie die Beurteilung des Integritätsschadens  nach Gutachten der SUVA mit ärztlicher Abschlussuntersuchung am 22. Juli 2013 mit 30 % be- wertet.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 37** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_60`)


Betreffend das Jahr 2015 wurde von der SUVA Quellensteuer in Höhe von 5.623,80 CHF einbe- halten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 38** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_64`)


Mit Erkenntnis vom 19. Dezember 2024, Ro 2023/15/0003, hob der Verwaltungsgerichtshof  das die Gleichartigkeit der von der SUVA ausbezahlten Invalidenrente und Geldleistungen aus  der gesetzlichen inländischen Unfallversorgung verneinende Erkenntnis des Bundesfinanzge- richtes vom 30. September 2022, RV/1100086/2019, wegen inhaltlicher Rechtswidrigkeit auf.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 39** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_73`)


Die Revision bringt zur Gleichartigkeit der von der SUVA ausbezahlten Schweizer Invalidenrente  Folgendes vor:   […]  Der Verwaltungsgerichtshof stimmt den Ausführungen der Revision zu, dass eine Gleichartig- keit der Leistungen iSd § 3 Abs. 1 Z 4 lit. c EStG 1988 keine völlige Identität in deren gesetzlicher  Ausgestaltung voraussetzt.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 40** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_107`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 41** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_115`)


Das Finanzamt hat die Einkommensteuervorauszahlungen für die Jahre 2017 sowie 2018 und  Folgejahren mit Bescheiden vom 4. Juli 2017 bzw. vom 27. November 2017 gemäß § 45 Abs. 4  EStG 1988 mit 24.000,00 € (2017) bzw. 22.391,00 € (2018) festgesetzt, wobei die von der SUVA  bezogene Invalidenrente jeweils als zur Gänze steuerpflichtig berücksichtigt wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 42** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_118`)


Wie oben dargelegt, wurde die von der SUVA bezogene Invalidenrente zu Unrecht zur Gänze  der Besteuerung unterzogen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 43** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_121`)


Gesamthaft gesehen war den Beschwerden gegen die Einkommensteuerbescheide 2015 und  2016 somit (hinsichtlich des Jahres 2015 über den Umfang der Beschwerdevorentscheidung  hinaus) insoweit teilweise Folge zu geben, als die von der SUVA bezogene Invalidenrente im  oben genannten Ausmaß steuerfrei zu belassen war.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_8`)


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

**False Positives:**

- `SUVA` — type mismatch (gold: `SUVA`)
- `SUVA` — type mismatch (gold: `SUVA`)

> partial: 2  |  missing annotation: 0

**Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

**False Positives:**

- `SUVA` — type mismatch (gold: `SUVA`)

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_44`)


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

**False Positives:**

- `SUVA` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_58`)


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizeri- schen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_63`)


Rechtliche Beurteilung  2.1. SUVA-Invalidenrente  Gemäß § 3 Abs. 1 Z 4 lit. c EStG 1988 sind Geldleistungen aus einer gesetzlichen Unfallversor- gung sowie dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen ge- setzlichen Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspricht,  steuerbefreit.

**False Positives:**

- `SUVA` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_124`)


Die im Beschwerdefall strittige Frage, ob es sich bei einer infolge eines Arbeitsunfalles von der  Schweizerischen Unfallversicherungsanstalt (SUVA) ausbezahlten Invalidenrente um eine mit  einer Geldleistung aus der inländischen gesetzlichen Unfallversorgung gleichartige ausländi- sche Leistung im Sinne des § 3 Abs. 1 Z 4 lit. c EStG 1988 handelt, ist durch das Erkenntnis des  Verwaltungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, geklärt.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_8`)


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

**False Positives:**

- `SUVA` — type mismatch (gold: `SUVA`)
- `SUVA` — type mismatch (gold: `SUVA`)

> partial: 2  |  missing annotation: 0

**Gold Entities:**
- `SUVA` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

**False Positives:**

- `SUVA` — type mismatch (gold: `SUVA`)

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `SUVA` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_44`)


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

**False Positives:**

- `SUVA` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_58`)


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizeri- schen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_63`)


Rechtliche Beurteilung  2.1. SUVA-Invalidenrente  Gemäß § 3 Abs. 1 Z 4 lit. c EStG 1988 sind Geldleistungen aus einer gesetzlichen Unfallversor- gung sowie dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen ge- setzlichen Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspricht,  steuerbefreit.

**False Positives:**

- `SUVA` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_124`)


Die im Beschwerdefall strittige Frage, ob es sich bei einer infolge eines Arbeitsunfalles von der  Schweizerischen Unfallversicherungsanstalt (SUVA) ausbezahlten Invalidenrente um eine mit  einer Geldleistung aus der inländischen gesetzlichen Unfallversorgung gleichartige ausländi- sche Leistung im Sinne des § 3 Abs. 1 Z 4 lit. c EStG 1988 handelt, ist durch das Erkenntnis des  Verwaltungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, geklärt.

**False Positives:**

- `SUVA` — partial — pred ⊂ gold: `Schweizerischen Unfallversicherungsanstalt (SUVA)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

</details>

---

## `ÖGK`

**F1:** 0.084 | **Precision:** 1.000 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Matches the acronym 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.044 | 0.084 | 40 | 40 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 873 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist in der vorliegenden Beschwerdesache, ob zu Recht Einkünfte in Höhe von EUR  620,43 von der Österreichischen Gesundheitskasse (im Folgenden: ÖGK) im  Einkommensteuerbescheid 2023 des Beschwerdeführers (im Folgenden: Bf.) berücksichtigt  wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_6`)


Darin  wurden auch Einkünfte von der ÖGK in Höhe von EUR 620,43 berücksichtigt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_15`)


Im Jahr 2023 erhielt der Bf. von der ÖGK eine Erstattung von insgesamt EUR 723,84 an  Beiträgen zur Sozialversicherung (davon entfielen auf die Krankenversicherung EUR 163,53, auf  die Arbeitslosenversicherung EUR 126,77 und auf die Pensionsversicherung EUR 433,54).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_16`)


Diese  Erstattung hatte ihre Wurzel im Jahr 2022, da in diesem Jahr Beiträge über die  Höchstbeitragsgrundlage hinaus an die ÖGK entrichtet wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_17`)


In einem Schreiben der ÖGK  vom 12.5.2023 wurde der Bf. über die Rückerstattung der Beiträge informiert und darauf  aufmerksam gemacht, dass die rückerstatteten Sozialversicherungsbeiträge steuerpflichtig  sind.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_18`)


Am 20.2.2024 wurde dem Finanzamt von der ÖGK ein Lohnzettel für den Bf. und das Jahr 2023  übermittelt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_20`)


Im Einkommensteuerbescheid 2023 des Bf. kamen bei den Einkünften aus nichtselbständiger  Arbeit auch die von der ÖGK rückerstatteten Sozialversicherungsbeiträge in Höhe von EUR  620,43 zum Ansatz.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_23`)


Darüber hinaus enthält das  Schreiben der ÖGK vom 12.5.2023 eine Aufstellung der für die Berechnung relevanten  Versicherungsverhältnisse 2022 und ergibt sich die Sachverhaltsfeststellung auch daraus.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_27`)


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_32`)


Dieses Schreiben der ÖGK über die Erstattung von Beiträgen in Höhe von EUR 723,84 ist im  finanzbehördlichen Abgabeninformationssystem (JVP) hinterlegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_35`)


Aufgrund dieses Schreibens der ÖGK an den Bf. ist für das Bundesfinanzgericht die Grundlage  für den im Jahr 2024 übermittelten Lohnzettel an das Finanzamt (auch dieser ist in der JVP  ersichtlich) und die Berücksichtigung des Betrages von EUR 620,43 im  Einkommensteuerbescheid 2023 des Bf. geklärt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_36`)


Die im Einkommensteuerbescheid 2023  ersichtlichen Einkünfte in dieser Höhe betreffen somit nicht allfällige Krankenstände im Jahr  2023, sondern es handelt sich vielmehr um einen Rückerstattungsbetrag der ÖGK an den Bf.  aufgrund zu viel bezahlter Beiträge zur Kranken-, Arbeitslosen- und Pensionsversicherung im  Jahr 2022.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_37`)


Aus dem Schreiben der ÖGK geht zudem eindeutig hervor, dass die  Sozialversicherungsbeiträge im Jahr 2022 aufgrund der in diesem Jahr bestandenen  Dienstverhältnisse bei den Firmen Gogel Daten GMBH  und im Folgenden bei der Klein-Vorholt KI GMBH  einbehalten und geleistet wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_58`)


Dabei besteht jedoch kein Zweifel, dass die im Jahr 2022 geleisteten  Beträge als Pflichtbeiträge zur Sozialversicherung von den Dienstgebern des Bf. einbehalten  und an die ÖGK abgeführt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 24** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist in der vorliegenden Beschwerdesache, ob zu Recht Einkünfte in Höhe von EUR  620,43 von der Österreichischen Gesundheitskasse (im Folgenden: ÖGK) im  Einkommensteuerbescheid 2023 des Beschwerdeführers (im Folgenden: Bf.) berücksichtigt  wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 25** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_6`)


Darin  wurden auch Einkünfte von der ÖGK in Höhe von EUR 620,43 berücksichtigt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 26** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_15`)


Im Jahr 2023 erhielt der Bf. von der ÖGK eine Erstattung von insgesamt EUR 723,84 an  Beiträgen zur Sozialversicherung (davon entfielen auf die Krankenversicherung EUR 163,53, auf  die Arbeitslosenversicherung EUR 126,77 und auf die Pensionsversicherung EUR 433,54).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 27** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_16`)


Diese  Erstattung hatte ihre Wurzel im Jahr 2022, da in diesem Jahr Beiträge über die  Höchstbeitragsgrundlage hinaus an die ÖGK entrichtet wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_17`)


In einem Schreiben der ÖGK  vom 12.5.2023 wurde der Bf. über die Rückerstattung der Beiträge informiert und darauf  aufmerksam gemacht, dass die rückerstatteten Sozialversicherungsbeiträge steuerpflichtig  sind.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 29** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_18`)


Am 20.2.2024 wurde dem Finanzamt von der ÖGK ein Lohnzettel für den Bf. und das Jahr 2023  übermittelt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 30** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_20`)


Im Einkommensteuerbescheid 2023 des Bf. kamen bei den Einkünften aus nichtselbständiger  Arbeit auch die von der ÖGK rückerstatteten Sozialversicherungsbeiträge in Höhe von EUR  620,43 zum Ansatz.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 31** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_23`)


Darüber hinaus enthält das  Schreiben der ÖGK vom 12.5.2023 eine Aufstellung der für die Berechnung relevanten  Versicherungsverhältnisse 2022 und ergibt sich die Sachverhaltsfeststellung auch daraus.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 32** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_27`)


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 33** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_32`)


Dieses Schreiben der ÖGK über die Erstattung von Beiträgen in Höhe von EUR 723,84 ist im  finanzbehördlichen Abgabeninformationssystem (JVP) hinterlegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 34** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_35`)


Aufgrund dieses Schreibens der ÖGK an den Bf. ist für das Bundesfinanzgericht die Grundlage  für den im Jahr 2024 übermittelten Lohnzettel an das Finanzamt (auch dieser ist in der JVP  ersichtlich) und die Berücksichtigung des Betrages von EUR 620,43 im  Einkommensteuerbescheid 2023 des Bf. geklärt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 35** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_36`)


Die im Einkommensteuerbescheid 2023  ersichtlichen Einkünfte in dieser Höhe betreffen somit nicht allfällige Krankenstände im Jahr  2023, sondern es handelt sich vielmehr um einen Rückerstattungsbetrag der ÖGK an den Bf.  aufgrund zu viel bezahlter Beiträge zur Kranken-, Arbeitslosen- und Pensionsversicherung im  Jahr 2022.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 36** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_37`)


Aus dem Schreiben der ÖGK geht zudem eindeutig hervor, dass die  Sozialversicherungsbeiträge im Jahr 2022 aufgrund der in diesem Jahr bestandenen  Dienstverhältnisse bei den Firmen Gogel Daten GMBH  und im Folgenden bei der Klein-Vorholt KI GMBH  einbehalten und geleistet wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 37** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_58`)


Dabei besteht jedoch kein Zweifel, dass die im Jahr 2022 geleisteten  Beträge als Pflichtbeiträge zur Sozialversicherung von den Dienstgebern des Bf. einbehalten  und an die ÖGK abgeführt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Finanzamtes Österreich`

**F1:** 0.063 | **Precision:** 1.000 | **Recall:** 0.033  

**Format:** `regex`  
**Description:**
Matches the genitive form 'Finanzamtes Österreich'.

**Content:**
```
\bFinanzamtes\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.033 | 0.063 | 30 | 30 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 30 | 0 | 824 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache HR KzlR Stephanie Ganssloser, Schwemmgasse 16, 8992 Fischerndorf, Österreich, betreffend Beschwerde vom 8. April 2025 gegen  den Bescheid des Finanzamtes Österreich vom 10. März 2025 betreffend Säumniszuschlag  10.03.2025 zur Steuernummer 16-527/7844  beschlossen:   Die Beschwerde vom 8. April 2025 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_4`)


Begründung  Mit Bescheid des Finanzamtes Österreich vom 10. März 2025 wurden erste Säumniszuschläge  hinsichtlich   -) Lohnsteuer 1/2025,  -) Dienstgeberbeitrag 1/2025  -) Umsatzsteuer 2022,   -) Umsatzsteuer 12/2024,  -) KESt 12/2018,   -) KESt 12/2019,   -) KESt 12/2021 und   -) KESt 12/2022   in Höhe von € 6.644,77 festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Pawel Heldt  in der Beschwerdesache  Samir Krahnepuhl, Webersberg 40, 7331 Kalkgruben, Österreich, über die Beschwerde vom 18. September 2023 gegen den  Bescheid des Finanzamtes Österreich vom 7. September 2023 betreffend Abweisung des  Antrags auf Wiedereinsetzung in den vorigen Stand vom 5. August 2023, Steuernummer  88-903/5443, zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149301.1`) (sent_id: `findok-manually-annotated_TRAIN/149301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Annalena Spatzier, Bahnhof Krottenbachstraße 4, 3130 Unterwinden, Österreich, über die Beschwerde vom 21. März 2024 gegen  den Bescheid des Finanzamtes Österreich vom 22. Februar 2024 betreffend Einkommensteuer  2018, Steuernummer 78-848/2763, zu Recht erkannt:   I. Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Wilma Kewer, Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich, über die Beschwerde vom 17. August 2025  gegen den Bescheid des Finanzamtes Österreich vom 04. August 2025 betreffend die  Verzinsung der Rückerstattung gem. § 16 COFAG-NoAG (Steuernummer 45-588/1819 ) zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Arielle Billmaier  in der Beschwerdesache Elena Dämel,  Römerstraße-Palfen 44E, 9431 Thürn, Österreich, betreffend Beschwerde vom 10. Juli 2025 gegen den Bescheid des Finanzamtes  Österreich vom 3. Juni 2025 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2024,  Steuernummer 70-316/9622  beschlossen:  I.Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Dr. Wiebke Peperkorn in der  Beschwerdesache Sophie Zekalla, Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich, über die Beschwerde vom 29. April 2024 gegen  den Bescheid des Finanzamtes Österreich vom 24. April 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 71-479/6461  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hedwig Kaszemeikat  in der Beschwerdesache  Erna Kaireit, Haibach im Mühlkreis, vertreten durch Peter Weinmar, Neudeggergasse 5 Tür 22, 1080  Wien, über die Beschwerde vom 11. Dezember 2019 gegen die Bescheide des Finanzamtes  Österreich vom 15. März 2019 betreffend Feststellung der Einkünfte § 188 BAO 2011 bis 2017  und betreffend Umsatzsteuer 2013 bis 2017 zu Steuernummer 91-046/2147  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hedwig Kaszemeikat  in der Beschwerdesache  Erna Kaireit, Haibach im Mühlkreis, vertreten durch Peter Weinmar, Neudeggergasse 5 Tür 22, 1080  Wien, über die Beschwerde vom 11. Dezember 2019 gegen die Bescheide des Finanzamtes  Österreich vom 15. März 2019 betreffend Feststellung der Einkünfte § 188 BAO 2011 bis 2017  und betreffend Umsatzsteuer 2013 bis 2017 zu Steuernummer 91-046/2147  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149301.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Annalena Spatzier, Bahnhof Krottenbachstraße 4, 3130 Unterwinden, Österreich, über die Beschwerde vom 21. März 2024 gegen  den Bescheid des Finanzamtes Österreich vom 22. Februar 2024 betreffend Einkommensteuer  2018, Steuernummer 78-848/2763, zu Recht erkannt:   I. Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) (sent_id: `findok-manually-annotated_TRAIN/149863.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Wilma Kewer, Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich, über die Beschwerde vom 17. August 2025  gegen den Bescheid des Finanzamtes Österreich vom 04. August 2025 betreffend die  Verzinsung der Rückerstattung gem. § 16 COFAG-NoAG (Steuernummer 45-588/1819 ) zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Marion Bomarius  in der Beschwerdesache Norbert Ribarczik,  Zufahrt Felbermayr 68, 9241 Neudorf, Österreich, vertreten durch Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft,  Museumstraße 31a, 4020 Linz, über die Beschwerde vom 3. Jänner 2024 gegen den  Einkommensteuerbescheid des Finanzamtes Österreich vom 23. November 2023 betreffend  Berichtigung gem. § 293b BAO zu Bescheid vom 21.11.2023 Steuernummer 71-595/2950  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Pawel Heldt  in der Beschwerdesache  Samir Krahnepuhl, Webersberg 40, 7331 Kalkgruben, Österreich, über die Beschwerde vom 18. September 2023 gegen den  Bescheid des Finanzamtes Österreich vom 7. September 2023 betreffend Abweisung des  Antrags auf Wiedereinsetzung in den vorigen Stand vom 5. August 2023, Steuernummer  88-903/5443, zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/149731.1`) (sent_id: `findok-manually-annotated_TRAIN/149731.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Arielle Billmaier  in der Beschwerdesache Elena Dämel,  Römerstraße-Palfen 44E, 9431 Thürn, Österreich, betreffend Beschwerde vom 10. Juli 2025 gegen den Bescheid des Finanzamtes  Österreich vom 3. Juni 2025 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2024,  Steuernummer 70-316/9622  beschlossen:  I.Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149497.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 26** (doc_id: `findok-manually-annotated_TRAIN/149322.1`) (sent_id: `findok-manually-annotated_TRAIN/149322.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache HR KzlR Stephanie Ganssloser, Schwemmgasse 16, 8992 Fischerndorf, Österreich, betreffend Beschwerde vom 8. April 2025 gegen  den Bescheid des Finanzamtes Österreich vom 10. März 2025 betreffend Säumniszuschlag  10.03.2025 zur Steuernummer 16-527/7844  beschlossen:   Die Beschwerde vom 8. April 2025 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 27** (doc_id: `findok-manually-annotated_TRAIN/149322.1`) (sent_id: `findok-manually-annotated_TRAIN/149322.1_4`)


Begründung  Mit Bescheid des Finanzamtes Österreich vom 10. März 2025 wurden erste Säumniszuschläge  hinsichtlich   -) Lohnsteuer 1/2025,  -) Dienstgeberbeitrag 1/2025  -) Umsatzsteuer 2022,   -) Umsatzsteuer 12/2024,  -) KESt 12/2018,   -) KESt 12/2019,   -) KESt 12/2021 und   -) KESt 12/2022   in Höhe von € 6.644,77 festgesetzt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Dr. Wiebke Peperkorn in der  Beschwerdesache Sophie Zekalla, Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich, über die Beschwerde vom 29. April 2024 gegen  den Bescheid des Finanzamtes Österreich vom 24. April 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 71-479/6461  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 29** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Marion Bomarius  in der Beschwerdesache Norbert Ribarczik,  Zufahrt Felbermayr 68, 9241 Neudorf, Österreich, vertreten durch Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft,  Museumstraße 31a, 4020 Linz, über die Beschwerde vom 3. Jänner 2024 gegen den  Einkommensteuerbescheid des Finanzamtes Österreich vom 23. November 2023 betreffend  Berichtigung gem. § 293b BAO zu Bescheid vom 21.11.2023 Steuernummer 71-595/2950  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

</details>

---

## `Finanzamt Österreich`

**F1:** 0.055 | **Precision:** 1.000 | **Recall:** 0.028  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' specifically to ensure it is captured.

**Content:**
```
\bFinanzamt\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.028 | 0.055 | 26 | 26 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 0 | 780 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_12`)


In der Bescheidbeschwerde wurde im Wesentlichen vorgebracht, dass die Unterlagen zum  Einkommen 2021 und 2022 per Fax und per Einschreiben an das Finanzamt Österreich in Wien  zugesandt worden wären.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_15`)


Mit Beschwerdevorentscheidung vom 08.10.2024 wurde die gegenständliche  Bescheidbeschwerde als unbegründet abgewiesen und zur Begründung angeführt:  „Der Antrag wird damit begründet, dass sämtliche Unterlagen an das Finanzamt Österreich  zugesandt wurden und man unrechtmäßig den Betrag gepfändet hat.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Ronald Leinberger, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 6. Dezember 2019 gegen die  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr  zuständig: Finanzamt Österreich) vom 31. Oktober 2019 betreffend Gebühren 2010 bis 2012 zu  Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_11`)


Mit dem angefochtenen Bescheid vom 7. September 2023 wies das Finanzamt Österreich (im  Weiteren FAÖ) den Antrag als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_12`)


In der Bescheidbeschwerde wurde im Wesentlichen vorgebracht, dass die Unterlagen zum  Einkommen 2021 und 2022 per Fax und per Einschreiben an das Finanzamt Österreich in Wien  zugesandt worden wären.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_15`)


Mit Beschwerdevorentscheidung vom 08.10.2024 wurde die gegenständliche  Bescheidbeschwerde als unbegründet abgewiesen und zur Begründung angeführt:  „Der Antrag wird damit begründet, dass sämtliche Unterlagen an das Finanzamt Österreich  zugesandt wurden und man unrechtmäßig den Betrag gepfändet hat.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_22`)


Mit Bescheid vom 01. August 2025 setzte das Finanzamt Österreich gem. § 13ff COFAG-NoAG  den Rückerstattungsanspruch hinsichtlich des noch ausstehenden Betrags an rückzuzahlender  Förderung aus dem Fördervertrag betreffend Fixkostenzuschuss 800.000 in Höhe von EUR  12.566,57 fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) (sent_id: `findok-manually-annotated_TRAIN/149863.1_22`)


Mit Bescheid vom 01. August 2025 setzte das Finanzamt Österreich gem. § 13ff COFAG-NoAG  den Rückerstattungsanspruch hinsichtlich des noch ausstehenden Betrags an rückzuzahlender  Förderung aus dem Fördervertrag betreffend Fixkostenzuschuss 800.000 in Höhe von EUR  12.566,57 fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Fürniß  in der Beschwerdesache PhD OMedR Ada Segert,  Gschlößlgasse 2, 5542 Flachau, Österreich, vertreten durch Vertreter, Adresse Vertreter, über die Säumnisbeschwerde der  beschwerdeführenden Partei vom 4. September 2025 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2023, Steuernummer xx-xxx/xxxx, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_6`)


Das Finanzamt übersendete dem Bundesfinanzgericht am 17. Oktober 2025 den am  12. Dezember 2024 durch das Finanzamt Österreich erlassen Bescheid gemäß § 84 Abs. 1 BAO  betreffend die Ablehnung der steuerlichen Vertreterin sowie die Verständigung des Bf. über  die Ablehnung seiner steuerlichen Vertreterin mit selben Datum.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Fürniß  in der Beschwerdesache PhD OMedR Ada Segert,  Gschlößlgasse 2, 5542 Flachau, Österreich, vertreten durch Vertreter, Adresse Vertreter, über die Säumnisbeschwerde der  beschwerdeführenden Partei vom 4. September 2025 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2023, Steuernummer xx-xxx/xxxx, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_6`)


Das Finanzamt übersendete dem Bundesfinanzgericht am 17. Oktober 2025 den am  12. Dezember 2024 durch das Finanzamt Österreich erlassen Bescheid gemäß § 84 Abs. 1 BAO  betreffend die Ablehnung der steuerlichen Vertreterin sowie die Verständigung des Bf. über  die Ablehnung seiner steuerlichen Vertreterin mit selben Datum.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_11`)


Mit dem angefochtenen Bescheid vom 7. September 2023 wies das Finanzamt Österreich (im  Weiteren FAÖ) den Antrag als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Ronald Leinberger, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 6. Dezember 2019 gegen die  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr  zuständig: Finanzamt Österreich) vom 31. Oktober 2019 betreffend Gebühren 2010 bis 2012 zu  Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `Event Sudkraftlex GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Event Sudkraftlex GMBH'.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 20 | 20 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 754 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `KQPC Versand GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the specific entity 'KQPC Versand GMBH'.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 20 | 20 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 758 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

## `FAÖ Acronym`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAÖ' (Finanzamt Österreich) as an organisation.

**Content:**
```
\bFAÖ\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 20 | 20 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 723 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_11`)


Mit dem angefochtenen Bescheid vom 7. September 2023 wies das Finanzamt Österreich (im  Weiteren FAÖ) den Antrag als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_29`)


Mit Ergänzungsersuchen vom 17. November 2023 hielt das FAÖ dem BF vor, dass eine bloß  abstrakte Strafdrohung eine Wiedereinsetzung nicht rechtfertige, sondern ein konkreter  Rechtsnachteil eingetreten sein müsse.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_31`)


In seiner Vorhaltsbeantwortung vom 21. November 2023 brachte der BF vor, dass die  Rechtsansicht des FAÖ verfehlt sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_35`)


Mit Beschwerdevorentscheidung vom 5. Februar 2024 wies das FAÖ die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_45`)


Insofern habe das FAÖ aktenwidrig entschieden, weil es den Umstand,  dass der BF mit der Sperre nicht gerechnet habe, als glaubhaft feststellte.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_51`)


Das FAÖ legte die Beschwerde am 4. März 2024 dem Bundesfinanzgericht vor und beantragte  die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_85`)


Das FAÖ betonte, dass sehr wohl ein erhöhter Sorgfaltsmaßstab anzusetzen sei, weil für die  Rolle eines Intermediär ein hohes steuerliches Wissen erforderlich sei und daher davon  ausgegangen werden könne, dass diese Rolle nur von Steuerberatern ausgeübt wird.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_126`)


Da das FAÖ den Antrag mit dem  angefochtenen Bescheid abgewiesen hat, ist dessen Spruch dahingehend zu ändern, dass der  Antrag zurückgewiesen wird.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_11`)


Mit dem angefochtenen Bescheid vom 7. September 2023 wies das Finanzamt Österreich (im  Weiteren FAÖ) den Antrag als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_29`)


Mit Ergänzungsersuchen vom 17. November 2023 hielt das FAÖ dem BF vor, dass eine bloß  abstrakte Strafdrohung eine Wiedereinsetzung nicht rechtfertige, sondern ein konkreter  Rechtsnachteil eingetreten sein müsse.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_31`)


In seiner Vorhaltsbeantwortung vom 21. November 2023 brachte der BF vor, dass die  Rechtsansicht des FAÖ verfehlt sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_35`)


Mit Beschwerdevorentscheidung vom 5. Februar 2024 wies das FAÖ die Beschwerde als  unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_45`)


Insofern habe das FAÖ aktenwidrig entschieden, weil es den Umstand,  dass der BF mit der Sperre nicht gerechnet habe, als glaubhaft feststellte.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_51`)


Das FAÖ legte die Beschwerde am 4. März 2024 dem Bundesfinanzgericht vor und beantragte  die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_85`)


Das FAÖ betonte, dass sehr wohl ein erhöhter Sorgfaltsmaßstab anzusetzen sei, weil für die  Rolle eines Intermediär ein hohes steuerliches Wissen erforderlich sei und daher davon  ausgegangen werden könne, dass diese Rolle nur von Steuerberatern ausgeübt wird.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_126`)


Da das FAÖ den Antrag mit dem  angefochtenen Bescheid abgewiesen hat, ist dessen Spruch dahingehend zu ändern, dass der  Antrag zurückgewiesen wird.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

</details>

---

## `Universität Wien`

**F1:** 0.039 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Universität Wien'.

**Content:**
```
\bUniversität\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.020 | 0.039 | 18 | 18 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 833 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `Universität General`

**F1:** 0.039 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Universität' followed by a location or name, excluding common labels like 'Name', 'Art', 'Typ'.

**Content:**
```
\bUniversität\s+(?!(?:Name|Art|Typ|Bezeichnung|Anzahl|Beginn|Ende|Wohnort|Land|Landes|Stadt|Gemeinde)\b)(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*|in\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.020 | 0.039 | 18 | 18 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 833 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `VwGH Acronym`

**F1:** 0.033 | **Precision:** 0.250 | **Recall:** 0.017  

**Format:** `regex`  
**Description:**
Matches the acronym 'VwGH' (Verwaltungsgerichtshof) as a standalone organization, excluding cases where it is followed by dates (citations).

**Content:**
```
\bVwGH\b(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.250 | 0.017 | 0.033 | 64 | 16 | 48 | 1 | 47 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 48 | 881 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_125`)


Die Rechtsfolgen im beschwerdegegenständlichen Fall ergeben sich unmittelbar aus den  anzuwendenden, vom Wortlaut her eindeutigen gesetzlichen Bestimmungen und wurde im  Übrigen der ständigen Rechtsprechung des VwGH gefolgt.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_248`)


Zu alldem ist auf die Rechtsprechung des VwGH zu verweisen, wonach eine freie Auflösbarkeit  des Vertrags nur dann vorliegt, wenn eine Kündigung auch die tatsächliche Befreiung von den  Leistungsverpflichtungen für die Zeit nach der Vertragsauflösung bewirkt (vgl VwGH  16.10.2014, 2011/16/0169;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_14`)


Neben den vom VwGH  behandelten einfachgesetzlichen Rechtsfragen macht die Bf weiters geltend, die  Kürzungsbestimmungen des § 2 Abs 2 Z 3a StabAbgG auf die Liquiditätsreserve in den  zweistufigen Sektoren nicht anzuwenden, stelle einen unsachlichen Systembruch, eine  unsachliche Differenzierung zwischen Einlagensicherung und Liquiditätsverbund, eine  sachwidrige Besteuerung gedeckter Einlagen, eine Benachteiligung gegenüber Kreditinstituten,  die keinem Liquiditätsverbund angehören müssen, sowie eine gleichheitswidrige  Differenzierung innerhalb der dezentralen Sektoren dar.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_19`)


Für 2024 wurde in der Stabilitätsabgabeerklärung 2024 die Liquiditätsreserve im Hinblick  auf die Entscheidung des VwGH vom 20.11.2024, Ro 2024/13/0019 nicht abgezogen und  erfolgte demnach eine erklärungsgemäße Festsetzung der Stabilitätsabgabe 2024 mit €  2.614,77.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_28`)


Zur Anwendbarkeit des § 2 Abs 2 Z 3a StabAbgG auf die vorliegende Fallkonstellation hat  der VwGH in seinem Erkenntnis vom 20.11.2024, Ro 2024/13/0019, ausgesprochen:  Da eine Verminderung nur in jenem Ausmaß zulässig ist, als Forderungen an das  Zentralinstitut (oder ein anderes Kreditinstitut) bestehen, kann die Verminderung der  Bemessungsgrundlage nach dieser Ziffer nur im Fall eines mehrstufigen Bankenverbundes  eintreten, weil nur in diesem Fall sowohl Verpflichtungen gegenüber einem Kreditinstitut  (aus der Erfüllung eines Liquiditätserfordernisses), anderseits aber auch Forderungen an  das Zentralinstitut bestehen können.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_123`)


Dabei zitierte die Behörde eine Rechtsprechung des  VwGH, aus welcher sich ableiten ließe, dass bei einem Reitbetrieb und Betrieb eines Schlosses  eine Tätigkeit mit Liebhabereivermutung dann vorliegen würde, wenn in 14 Jahren nur geringe  Einnahmen erzielt worden sind und die Aufwendungen erst frühestens nach 28 Jahren  ausgeglichen werden können (VwGH 27.08.1998, 96/13/0041).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_14`)


Wie der VwGH in seiner Entscheidung vom 15. Jänner 2008, 2007/15/0232 ausführt, ist die  Ablehnung eines unbefugten Vertreters diesem gegenüber bescheidmäßig zu verfügen.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_20`)


In seinem Erkenntnis vom 21. März 2019, Ra 2019/22/0004 hat der VwGH ausgeführt, dass das  verwaltungsgerichtliche Verfahren einerseits und das behördliche Verfahren andererseits eine  Einheit darstellen (vgl. auch VwGH 25. September 2018, Ra 2018/21/0069, Rn. 12f).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_29`)


Der angefochtene Bescheid steht im Einklang mit der geltenden Rechtslage, welche durch die  oben zitierte einschlägige Judikatur des VwGH fundiert bzw. gesichert ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_129`)


Im gegenständlichen Verfahren waren keine Rechtsfragen zu lösen, zu denen es noch an  Rechtsprechung des VwGH fehlt, bzw. diese uneinheitlich ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_130`)


Die Entscheidung weicht auch  nicht von der in der Begründung zitierten Rechtsprechung des VwGH ab.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_131`)


Hinsichtlich der Konsequenzen einer verspäteten Nachholung der versäumten Handlung gibt es  bereits eine Rechtsprechung des VwGH, von der in diesem Erkenntnis auch nicht abgewichen  wird.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_71`)


Im Übrigen folgt das Erkenntnis der oben zitierten Rechtsprechung des VwGH zur Rückzahlung  von Pflichtbeiträgen.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_291`)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_294`)


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_291`)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_294`)


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_38`)


Für die Wirksamkeit einer Prozesserklärung ist das Erklärte maßgebend, nicht das Gewollte (vgl  zB VwGH vom 28.2.2008, 2006/16/0129).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_39`)


Das Erklärte ist allerdings der Auslegung zugänglich  (vgl. zB VwGH vom 29.7.2010, 2009/15/0152).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_41`)


hierbei kommt es  darauf an, wie die Erklärung unter Berücksichtigung der konkreten gesetzlichen Regelung, des  Verfahrenszweckes und der der Behörde vorliegenden Aktenlage objektiv verstanden werden  muss (zB VwGH vom 20.3.2014, 2010/15/0195, VwGH 30.1.2015, Ra 2014/17/0025)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_42`)


Ist der Inhalt eines Anbringens eindeutig, ist eine davon abweichende, nach außen auch  andeutungsweise nicht zum Ausdruck kommende Absicht des Einschreiters nicht maßgeblich  (vgl. zB VwGH vom 24.6.2009, 2007/15/0041)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_38`)


Für die Wirksamkeit einer Prozesserklärung ist das Erklärte maßgebend, nicht das Gewollte (vgl  zB VwGH vom 28.2.2008, 2006/16/0129).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_39`)


Das Erklärte ist allerdings der Auslegung zugänglich  (vgl. zB VwGH vom 29.7.2010, 2009/15/0152).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_41`)


hierbei kommt es  darauf an, wie die Erklärung unter Berücksichtigung der konkreten gesetzlichen Regelung, des  Verfahrenszweckes und der der Behörde vorliegenden Aktenlage objektiv verstanden werden  muss (zB VwGH vom 20.3.2014, 2010/15/0195, VwGH 30.1.2015, Ra 2014/17/0025)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_42`)


Ist der Inhalt eines Anbringens eindeutig, ist eine davon abweichende, nach außen auch  andeutungsweise nicht zum Ausdruck kommende Absicht des Einschreiters nicht maßgeblich  (vgl. zB VwGH vom 24.6.2009, 2007/15/0041)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_264`)


Vielmehr ist diesbezüglich auf das VwGH-Erkenntnis vom 24.3.1994, 93/16/0133, zu verweisen,  wonach, sofern dem Mieter ein jederzeitiges Kündigungsrecht zusteht, dieser jedoch im Fall  der Kündigung dem Vermieter eine „Pönale“ im Ausmaß des Mietzinses für eine festgelegte  Dauer zu entrichten hat, dem Vermieter jedenfalls das Mietentgelt für eine Bestanddauer von  dieser festgelegten Dauer gesichert ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_302`)


Maßgebend für die Festsetzung der Gebühren ist im  Sinne des § 17 Abs 1 GebG vielmehr der Inhalt der über das Rechtsgeschäft errichteten  Urkunde und damit das im konkreten Fall tatsächlich Vereinbarte (vgl VwGH 22.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_11`)


Der Amtsrevision folgend hat der VwGH das Erkenntnis des Bundesfinanzgerichtes aufgehoben  (VwGH 20.11.2024, Ro 2024/13/0019).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Bundesfinanzgerichtes` (organisation)

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_39`)


Die gegenständliche Rechtsfrage ist durch das VwGH-Erkenntnis Ro 2024/13/0019 vom  20.11.2024 geklärt.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_129`)


Im gegenständlichen Verfahren waren keine Rechtsfragen zu lösen, zu denen es noch an  Rechtsprechung des VwGH fehlt, bzw. diese uneinheitlich ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_130`)


Die Entscheidung weicht auch  nicht von der in der Begründung zitierten Rechtsprechung des VwGH ab.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_131`)


Hinsichtlich der Konsequenzen einer verspäteten Nachholung der versäumten Handlung gibt es  bereits eine Rechtsprechung des VwGH, von der in diesem Erkenntnis auch nicht abgewichen  wird.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_48`)


Nach der Rechtsprechung des VwGH schafft die Bestimmung des § 25 Abs. 1 Z 3 lit. d EStG  1988 nur eine Fiktion in Bezug auf die Zuordnung rückgezahlter Pflichtbeiträge zu den  nichtselbständigen Einkünften auf der Einnahmenseite.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 23** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_71`)


Im Übrigen folgt das Erkenntnis der oben zitierten Rechtsprechung des VwGH zur Rückzahlung  von Pflichtbeiträgen.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 24** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_93`)


Nicht ein  tatsächlich erwirtschafteter Gesamterfolg, sondern die objektive Eignung der Tätigkeit zur  Erwirtschaftung eines solchen, subsidiär das nach außen in Erscheinung tretende Streben der  Tätigkeit nach einem solchen Erfolg hat demnach als Tatbestandsvoraussetzung des Vorliegens  von Einkünften zu gelten (VwGH 93/13/0171 vom 03.07.1996)“  Sowohl anlässlich der „Vorprüfung“ betreffend die Jahre 2007 bis 2010 (Nachschau 2011 und  2012) als auch die nunmehrige Außenprüfung betreffend die Umsatzsteuer für die Jahre 2013  bis 2017 und Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2011 bis 2017 hätte  die Bf mehrmals auf diese Sachverhalte hingewiesen und diese offen gelegt (vgl VwGH  03.07.1996, 93/13/0171).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_96`)


Es geht nicht an, dass der Fiskus positive Ergebnisse  einer von ihrem Zuschnitt durchaus erwerbswirtschaftlichen Tätigkeit abschöpft, da, dafür  maßgebliche außer Acht lässt, nur weil es zu einer Zeit gemacht wurde, zu der ein  Gesamtüberschuss (noch) nicht abzusehen war“ (vgl VwGH B301/94 vom 07.03.1995).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 26** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_123`)


Dabei zitierte die Behörde eine Rechtsprechung des  VwGH, aus welcher sich ableiten ließe, dass bei einem Reitbetrieb und Betrieb eines Schlosses  eine Tätigkeit mit Liebhabereivermutung dann vorliegen würde, wenn in 14 Jahren nur geringe  Einnahmen erzielt worden sind und die Aufwendungen erst frühestens nach 28 Jahren  ausgeglichen werden können (VwGH 27.08.1998, 96/13/0041).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 27** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_125`)


Die Rechtsfolgen im beschwerdegegenständlichen Fall ergeben sich unmittelbar aus den  anzuwendenden, vom Wortlaut her eindeutigen gesetzlichen Bestimmungen und wurde im  Übrigen der ständigen Rechtsprechung des VwGH gefolgt.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_93`)


Nicht ein  tatsächlich erwirtschafteter Gesamterfolg, sondern die objektive Eignung der Tätigkeit zur  Erwirtschaftung eines solchen, subsidiär das nach außen in Erscheinung tretende Streben der  Tätigkeit nach einem solchen Erfolg hat demnach als Tatbestandsvoraussetzung des Vorliegens  von Einkünften zu gelten (VwGH 93/13/0171 vom 03.07.1996)“  Sowohl anlässlich der „Vorprüfung“ betreffend die Jahre 2007 bis 2010 (Nachschau 2011 und  2012) als auch die nunmehrige Außenprüfung betreffend die Umsatzsteuer für die Jahre 2013  bis 2017 und Feststellung von Einkünften gemäß § 188 BAO für die Jahre 2011 bis 2017 hätte  die Bf mehrmals auf diese Sachverhalte hingewiesen und diese offen gelegt (vgl VwGH  03.07.1996, 93/13/0171).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 29** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_96`)


Es geht nicht an, dass der Fiskus positive Ergebnisse  einer von ihrem Zuschnitt durchaus erwerbswirtschaftlichen Tätigkeit abschöpft, da, dafür  maßgebliche außer Acht lässt, nur weil es zu einer Zeit gemacht wurde, zu der ein  Gesamtüberschuss (noch) nicht abzusehen war“ (vgl VwGH B301/94 vom 07.03.1995).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 30** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_14`)


Wie der VwGH in seiner Entscheidung vom 15. Jänner 2008, 2007/15/0232 ausführt, ist die  Ablehnung eines unbefugten Vertreters diesem gegenüber bescheidmäßig zu verfügen.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 31** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_19`)


(vgl. auch VwGH 19. Oktober 2016, Ro 2014/15/0004)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 32** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_20`)


In seinem Erkenntnis vom 21. März 2019, Ra 2019/22/0004 hat der VwGH ausgeführt, dass das  verwaltungsgerichtliche Verfahren einerseits und das behördliche Verfahren andererseits eine  Einheit darstellen (vgl. auch VwGH 25. September 2018, Ra 2018/21/0069, Rn. 12f).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 33** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_29`)


Der angefochtene Bescheid steht im Einklang mit der geltenden Rechtslage, welche durch die  oben zitierte einschlägige Judikatur des VwGH fundiert bzw. gesichert ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 34** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_19`)


(vgl. auch VwGH 19. Oktober 2016, Ro 2014/15/0004)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 35** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_20`)


In seinem Erkenntnis vom 21. März 2019, Ra 2019/22/0004 hat der VwGH ausgeführt, dass das  verwaltungsgerichtliche Verfahren einerseits und das behördliche Verfahren andererseits eine  Einheit darstellen (vgl. auch VwGH 25. September 2018, Ra 2018/21/0069, Rn. 12f).

**False Positives:**

- `VwGH` — type mismatch (gold: `VwGH`)

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `VwGH` (organisation)

**Example 36** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_11`)


Der Amtsrevision folgend hat der VwGH das Erkenntnis des Bundesfinanzgerichtes aufgehoben  (VwGH 20.11.2024, Ro 2024/13/0019).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 37** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_14`)


Neben den vom VwGH  behandelten einfachgesetzlichen Rechtsfragen macht die Bf weiters geltend, die  Kürzungsbestimmungen des § 2 Abs 2 Z 3a StabAbgG auf die Liquiditätsreserve in den  zweistufigen Sektoren nicht anzuwenden, stelle einen unsachlichen Systembruch, eine  unsachliche Differenzierung zwischen Einlagensicherung und Liquiditätsverbund, eine  sachwidrige Besteuerung gedeckter Einlagen, eine Benachteiligung gegenüber Kreditinstituten,  die keinem Liquiditätsverbund angehören müssen, sowie eine gleichheitswidrige  Differenzierung innerhalb der dezentralen Sektoren dar.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 38** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_19`)


Für 2024 wurde in der Stabilitätsabgabeerklärung 2024 die Liquiditätsreserve im Hinblick  auf die Entscheidung des VwGH vom 20.11.2024, Ro 2024/13/0019 nicht abgezogen und  erfolgte demnach eine erklärungsgemäße Festsetzung der Stabilitätsabgabe 2024 mit €  2.614,77.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 39** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_28`)


Zur Anwendbarkeit des § 2 Abs 2 Z 3a StabAbgG auf die vorliegende Fallkonstellation hat  der VwGH in seinem Erkenntnis vom 20.11.2024, Ro 2024/13/0019, ausgesprochen:  Da eine Verminderung nur in jenem Ausmaß zulässig ist, als Forderungen an das  Zentralinstitut (oder ein anderes Kreditinstitut) bestehen, kann die Verminderung der  Bemessungsgrundlage nach dieser Ziffer nur im Fall eines mehrstufigen Bankenverbundes  eintreten, weil nur in diesem Fall sowohl Verpflichtungen gegenüber einem Kreditinstitut  (aus der Erfüllung eines Liquiditätserfordernisses), anderseits aber auch Forderungen an  das Zentralinstitut bestehen können.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 40** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_39`)


Die gegenständliche Rechtsfrage ist durch das VwGH-Erkenntnis Ro 2024/13/0019 vom  20.11.2024 geklärt.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 41** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1_248`)


Zu alldem ist auf die Rechtsprechung des VwGH zu verweisen, wonach eine freie Auflösbarkeit  des Vertrags nur dann vorliegt, wenn eine Kündigung auch die tatsächliche Befreiung von den  Leistungsverpflichtungen für die Zeit nach der Vertragsauflösung bewirkt (vgl VwGH  16.10.2014, 2011/16/0169;

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 42** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1_264`)


Vielmehr ist diesbezüglich auf das VwGH-Erkenntnis vom 24.3.1994, 93/16/0133, zu verweisen,  wonach, sofern dem Mieter ein jederzeitiges Kündigungsrecht zusteht, dieser jedoch im Fall  der Kündigung dem Vermieter eine „Pönale“ im Ausmaß des Mietzinses für eine festgelegte  Dauer zu entrichten hat, dem Vermieter jedenfalls das Mietentgelt für eine Bestanddauer von  dieser festgelegten Dauer gesichert ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 43** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1_302`)


Maßgebend für die Festsetzung der Gebühren ist im  Sinne des § 17 Abs 1 GebG vielmehr der Inhalt der über das Rechtsgeschäft errichteten  Urkunde und damit das im konkreten Fall tatsächlich Vereinbarte (vgl VwGH 22.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 44** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_48`)


Nach der Rechtsprechung des VwGH schafft die Bestimmung des § 25 Abs. 1 Z 3 lit. d EStG  1988 nur eine Fiktion in Bezug auf die Zuordnung rückgezahlter Pflichtbeiträge zu den  nichtselbständigen Einkünften auf der Einnahmenseite.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `BFG Acronym`

**F1:** 0.031 | **Precision:** 0.357 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches 'BFG' acronym as an organisation, excluding cases where it is part of a hyphenated compound or a citation (followed by dates/numbers).

**Content:**
```
\bBFG\b(?!-)(?!\s*\d+\.\s*\d+\.\s*\d+)(?!\s*RV/)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.357 | 0.016 | 0.031 | 42 | 15 | 27 | 1 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 15 | 27 | 887 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_101`)


Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_103`)


Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_135`)


Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_147`)


Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_148`)


Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_258`)


Auf die weiterführenden Ausführungen des Vertreters des Bf. im Beschwerdeverfahren, die  sich mit der (Un)Zulässigkeit der Festsetzung einer Abzugssteuer befassen, ist nach Sicht des  BFG bei dieser Sachlage nicht einzugehen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_23`)


Im Zuge dieses ET wurde nach eingehender Besprechung der Sach- und Rechtslage  (Abgleichung der Saldenbestände auf dem Abgabenkonto unter Berücksichtigung der  Anrechnung verschiedenster saldowirksamer Verbuchungen) und nach einer durch das BFG  angeregten Sitzungsunterbrechung zur Abklärung des nunmehr haftungsrelevanten Betrages  2 von 3 Seite 3 von 3

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_24`)


durch die steuerliche Vertretung des Bf. das Beschwerdebegehren dahingehend eingeschränkt,  dass das BFG aussprechen möge, dass der Bf. lediglich für einen Betrag von 3.500,- € zur  Haftung herangezogen werde.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_26`)


Das BFG sieht keine Veranlassung, von dem, von den Parteien ermittelten und außer Streit  gestellten, nunmehrigen Haftungsbetrag abzugehen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_75`)


Dass dies bei der gegen- ständlichen gesetzlichen Schweizer Versicherungsleistung aufgrund ihrer Berechnungsmethode  (und dem Abstellen auf nuanciert stärker konkrete statt abstrakte Vergleichsmuster) nicht der  Fall gewesen wäre, ergibt sich aus den Ausführungen des BFG nicht.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_76`)


Vielmehr räumt das BFG  in seinem Erkenntnis selbst ein, dass im Revisionsfall „hinsichtlich des Versicherungsumfanges  6 von 11 Seite 7 von 11

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_82`)


In Verkennung der Rechtslage hat es das BFG unterlassen, eine solche Gegenüberstellung vor- zunehmen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_86`)


Wenn die belangte Behörde daher im vorliegenden Fall zur Ermittlung des maßgeblichen  (Durchschnitts-)Steuersatzes auch die deutschen Pensionseinkünfte herangezogen hat, so  geschah dies im Einklang mit der nationalen und internationalen (Verfassungs-)Rechtslage (BFG  vom 30.3.2021, RV/7100571/2021).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149731.1`) (sent_id: `findok-manually-annotated_TRAIN/149731.1_16`)


Mit Schreiben vom 8. Oktober 2025 bat das BFG um schriftliche Stellungnahme bis 29. Oktober  2025 und hielt dem Bf. nach Zitierung des § 245 Abs. 1 BAO auszugsweise vor:  „Im gegenständlichen Fall wurde der bekämpfte Bescheid Ihnen mittels FinanzOnline  elektronisch am Dienstag, den 03.06.2025, (per DataBox) rechtswirksam zugestellt;

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_72`)


Nach Ansicht des BFG gibt es keinen Grund, den schlüssigen und nachvollziehbaren Angaben  des Parkraumüberwachungsorganes, welche in der Anzeige festgehalten wurden, nicht zu  folgen, zumal nicht ersichtlich ist, weshalb dieser wahrheitswidrige Angaben hätte machen  sollen und sich darüber hinaus aus dem Akt kein Anhaltspunkt dafür ergibt, dass der  Meldungsleger den Bf. durch seine Angaben wahrheitswidrig belasten hätte wollen (vgl. VwGH  02.03.1994, 93/03/0203, 93/03/0276).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_101`)


Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_103`)


Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_135`)


Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_147`)


Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_148`)


Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_258`)


Auf die weiterführenden Ausführungen des Vertreters des Bf. im Beschwerdeverfahren, die  sich mit der (Un)Zulässigkeit der Festsetzung einer Abzugssteuer befassen, ist nach Sicht des  BFG bei dieser Sachlage nicht einzugehen.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_165`)


VwGH 28.10.2009,  2008/15/0329; vgl. auch BFG vom 01.03.2023, RV/2100884/2022).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_106`)


Bei der Berechnung kommt es nicht darauf an, ob und für wie lange in den vorhergehenden  Semestern tatsächlich Familienbeihilfe bezogen wurde (vgl. BFG vom 18.01.2023,  RV/7102766/2021 unter Verweis auf Lenneis/Wanke, FLAG2, § 2 Rz 107).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

**False Positives:**

- `BFG` — partial — pred ⊂ gold: `Bundesfinanzgericht (BFG)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht (BFG)` (organisation)
- `FAÖ` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_103`)


BFG vom 15.01.2019, RV/7300007/2018).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_258`)


BFG  vom 27.09.2021, RV/7300044/2019).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `FAÖ` (organisation)

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_23`)


Im Zuge dieses ET wurde nach eingehender Besprechung der Sach- und Rechtslage  (Abgleichung der Saldenbestände auf dem Abgabenkonto unter Berücksichtigung der  Anrechnung verschiedenster saldowirksamer Verbuchungen) und nach einer durch das BFG  angeregten Sitzungsunterbrechung zur Abklärung des nunmehr haftungsrelevanten Betrages  2 von 3 Seite 3 von 3

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_24`)


durch die steuerliche Vertretung des Bf. das Beschwerdebegehren dahingehend eingeschränkt,  dass das BFG aussprechen möge, dass der Bf. lediglich für einen Betrag von 3.500,- € zur  Haftung herangezogen werde.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_26`)


Das BFG sieht keine Veranlassung, von dem, von den Parteien ermittelten und außer Streit  gestellten, nunmehrigen Haftungsbetrag abzugehen.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_16`)


Mit Schreiben vom 8. Oktober 2025 bat das BFG um schriftliche Stellungnahme bis 29. Oktober  2025 und hielt dem Bf. nach Zitierung des § 245 Abs. 1 BAO auszugsweise vor:  „Im gegenständlichen Fall wurde der bekämpfte Bescheid Ihnen mittels FinanzOnline  elektronisch am Dienstag, den 03.06.2025, (per DataBox) rechtswirksam zugestellt;

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_165`)


VwGH 28.10.2009,  2008/15/0329; vgl. auch BFG vom 01.03.2023, RV/2100884/2022).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_103`)


BFG vom 15.01.2019, RV/7300007/2018).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_258`)


BFG  vom 27.09.2021, RV/7300044/2019).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_106`)


Bei der Berechnung kommt es nicht darauf an, ob und für wie lange in den vorhergehenden  Semestern tatsächlich Familienbeihilfe bezogen wurde (vgl. BFG vom 18.01.2023,  RV/7102766/2021 unter Verweis auf Lenneis/Wanke, FLAG2, § 2 Rz 107).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_75`)


Dass dies bei der gegen- ständlichen gesetzlichen Schweizer Versicherungsleistung aufgrund ihrer Berechnungsmethode  (und dem Abstellen auf nuanciert stärker konkrete statt abstrakte Vergleichsmuster) nicht der  Fall gewesen wäre, ergibt sich aus den Ausführungen des BFG nicht.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Schweizer` (country)

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_76`)


Vielmehr räumt das BFG  in seinem Erkenntnis selbst ein, dass im Revisionsfall „hinsichtlich des Versicherungsumfanges  6 von 11 Seite 7 von 11

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_82`)


In Verkennung der Rechtslage hat es das BFG unterlassen, eine solche Gegenüberstellung vor- zunehmen.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Magistrat der Stadt Wien` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 24** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_72`)


Nach Ansicht des BFG gibt es keinen Grund, den schlüssigen und nachvollziehbaren Angaben  des Parkraumüberwachungsorganes, welche in der Anzeige festgehalten wurden, nicht zu  folgen, zumal nicht ersichtlich ist, weshalb dieser wahrheitswidrige Angaben hätte machen  sollen und sich darüber hinaus aus dem Akt kein Anhaltspunkt dafür ergibt, dass der  Meldungsleger den Bf. durch seine Angaben wahrheitswidrig belasten hätte wollen (vgl. VwGH  02.03.1994, 93/03/0203, 93/03/0276).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Magistrat der Stadt Wien` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 26** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_86`)


Wenn die belangte Behörde daher im vorliegenden Fall zur Ermittlung des maßgeblichen  (Durchschnitts-)Steuersatzes auch die deutschen Pensionseinkünfte herangezogen hat, so  geschah dies im Einklang mit der nationalen und internationalen (Verfassungs-)Rechtslage (BFG  vom 30.3.2021, RV/7100571/2021).

**False Positives:**

- `BFG` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Magistrat der Stadt Wien`

**F1:** 0.021 | **Precision:** 0.455 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Magistrat/Magistrats/Magistrates der Stadt Wien' without the MA 67 suffix, covering genitive forms.

**Content:**
```
\bMagistrat(?:s|es)?\s+der\s+Stadt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.455 | 0.011 | 0.021 | 22 | 10 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 12 | 772 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred ⊂ gold: `Magistrats der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred ⊂ gold: `Magistrats der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, MA 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Irene Kohler` (person)
- `Jean Broderius` (person)
- `Weinwartshof 30, 8151 Södingberg, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, MA 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Mag. Irene Kohler` (person)
- `Jean Broderius` (person)
- `Weinwartshof 30, 8151 Södingberg, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

## `Wirtschaftsuniversität Wien`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'Wirtschaftsuniversität Wien', 'WU Wien', and the standalone abbreviation 'WU' in university contexts.

**Content:**
```
\b(?:Wirtschaftsuniversität\s+Wien|WU\s+Wien|(?<!\w)WU(?!\s+Linz|\s*\())\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.017 | 8 | 8 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 842 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_47`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_74`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_135`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_47`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_74`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_135`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

</details>

---

## `FA St. Johann Tamsweg Zell am See Specific`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA St. Johann Tamsweg Zell am See' to prevent partial matching.

**Content:**
```
\bFA\s+St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.009 | 4 | 4 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 802 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

</details>

---

## `Bundesministeriums für Finanzen Genitive`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Finanzen' and its base form 'Bundesministerium für Finanzen'.

**Content:**
```
\bBundesministerium(?:s)?\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.009 | 4 | 4 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 489 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

</details>

---

## `Magistrat der Stadt Wien, Magistratsabteilung 67`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Magistrat/Magistrats/Magistrates der Stadt Wien, Magistratsabteilung 67' covering all forms.

**Content:**
```
\bMagistrat(?:s|es)?\s+der\s+Stadt\s+Wien,\s+Magistratsabteilung\s+67\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.009 | 4 | 4 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 129 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien, Magistratsabteilung 67` | `Magistrat der  Stadt Wien, Magistratsabteilung 67` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien, Magistratsabteilung 67` | `Magistrat der  Stadt Wien, Magistratsabteilung 67` |

</details>

---

## `Finanzamtes Wien 1/23 Specific`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the specific genitive entity 'Finanzamtes Wien 1/23' which was missing.

**Content:**
```
\bFinanzamtes\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.009 | 4 | 4 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 731 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

</details>

---

## `Bundesministerium General`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium' and its genitive form 'Bundesministeriums' followed by 'für' and a department, covering common departments not explicitly listed in specific rules.

**Content:**
```
\bBundesministerium(?:s)?\s+f\u00fcr\s+(?:Finanzen|Inneres|Justiz|Arbeit,\s+Soziales\s+und\s+Konsumentenschutz|Bildung,\s+Kunst\s+und\s+Kultur|Land-\s+und\s+Forstwirtschaft|Verkehr,\s+Innovation\s+und\s+Technologie|Soziales,\s+Gesundheit,\s+Pflege\s+und\s+Konsumentenschutz|Europ\u00e4isches\s+und\s+Internationales|Wirtschaft|Digitalisierung\s+und\s+Wirtschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.009 | 4 | 4 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 489 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

</details>

---

## `BMF Specific`

**F1:** 0.009 | **Precision:** 0.667 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the acronym 'BMF' (Bundesministerium für Finanzen).

**Content:**
```
\bBMF\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.667 | 0.004 | 0.009 | 6 | 4 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 2 | 811 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_101`)


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_8`)


Mit  Eingaben vom 8. und 9. August 2023 ergänzte der BF den Antrag dahingehend, dass die  Meldung tatsächlich zunächst noch nicht erfolgt, sondern nur in FOn gespeichert worden sei,  da ein auf Seiten des BMF liegendes technisches Problem die Einbringung verhindere.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_101`)


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_8`)


Mit  Eingaben vom 8. und 9. August 2023 ergänzte der BF den Antrag dahingehend, dass die  Meldung tatsächlich zunächst noch nicht erfolgt, sondern nur in FOn gespeichert worden sei,  da ein auf Seiten des BMF liegendes technisches Problem die Einbringung verhindere.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_101`)


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

**False Positives:**

- `BMF` — type mismatch (gold: `BMF`)

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `BMF` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_101`)


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

**False Positives:**

- `BMF` — type mismatch (gold: `BMF`)

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `BMF` (organisation)

</details>

---

## `Magistrat der Stadt Wien, Magistratsabteilung 6`

**F1:** 0.009 | **Precision:** 0.667 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Magistrat/Magistrates der Stadt Wien, Magistratsabteilung 6' covering nominative, genitive, and plural genitive forms.

**Content:**
```
\bMagistrat(?:s|es)?\s+der\s+Stadt\s+Wien,\s+Magistratsabteilung\s+6\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.667 | 0.004 | 0.009 | 6 | 4 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 2 | 778 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 6` | `Magistrates der Stadt Wien, Magistratsabteilung 6` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien, Magistratsabteilung 6` | `Magistrats der Stadt Wien, Magistratsabteilung 6` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 6` | `Magistrates der Stadt Wien, Magistratsabteilung 6` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien, Magistratsabteilung 6` | `Magistrats der Stadt Wien, Magistratsabteilung 6` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Magistrates der Stadt Wien, Magistratsabteilung 6` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Magistrates der Stadt Wien, Magistratsabteilung 6` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

</details>

---

## `Verfassungsgerichtshof`

**F1:** 0.009 | **Precision:** 0.500 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Verfassungsgerichtshof'.

**Content:**
```
\bVerfassungsgerichtshof\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.004 | 0.009 | 8 | 4 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 4 | 754 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) (sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `COFAG` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Magistrat der Stadt Wien Genitive Plural`

**F1:** 0.009 | **Precision:** 0.500 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Magistrates der Stadt Wien' (plural genitive) and its variants with MA 67 or Magistratsabteilung 67.

**Content:**
```
\bMagistrates\s+der\s+Stadt\s+Wien(?:,\s+(?:MA\s+67|Magistratsabteilung\s+67))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.004 | 0.009 | 8 | 4 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 4 | 778 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Magistrates der Stadt Wien` — partial — pred ⊂ gold: `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

</details>

---

## `Magistratsabteilung 67`

**F1:** 0.009 | **Precision:** 0.400 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Magistratsabteilung 67' as a standalone entity, covering cases where the 'Magistrat der Stadt Wien' prefix is omitted.

**Content:**
```
\bMagistratsabteilung\s+67\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.400 | 0.004 | 0.009 | 10 | 4 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 6 | 587 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_9`)


Mit Schreiben der Magistratsabteilung 67 vom 28. April 2025 (Lenkererhebung) wurde die  Firma Firma als Zulassungsbesitzerin des in Rede stehenden mehrspurigen Kraftfahrzeuges  aufgefordert, binnen zwei Wochen nach Zustellung Auskunft darüber zu erteilen, wem das  genannte Kraftfahrzeug zum Beanstandungszeitpunkt überlassen wurde.

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_55`)


Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 18. Juni 2025).

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_9`)


Mit Schreiben der Magistratsabteilung 67 vom 28. April 2025 (Lenkererhebung) wurde die  Firma Firma als Zulassungsbesitzerin des in Rede stehenden mehrspurigen Kraftfahrzeuges  aufgefordert, binnen zwei Wochen nach Zustellung Auskunft darüber zu erteilen, wem das  genannte Kraftfahrzeug zum Beanstandungszeitpunkt überlassen wurde.

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_55`)


Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 18. Juni 2025).

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) (sent_id: `findok-manually-annotated_TRAIN/149661.1_20`)


Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 8. Oktober 2025).

**False Positives:**

- `Magistratsabteilung 67` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_20`)


Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 8. Oktober 2025).

**False Positives:**

- `Magistratsabteilung 67` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistratsabteilung 67` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistratsabteilung 67` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistratsabteilung 67` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistratsabteilung 67` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

## `Sudver Handel Services GMBH`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sudver Handel Services GMBH'.

**Content:**
```
\bSudver\s+Handel\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 760 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

</details>

---

## `Glanznorost Institut GMBH`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Glanznorost Institut GMBH'.

**Content:**
```
\bGlanznorost\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 760 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

</details>

---

## `FA Specific Locations`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by specific known tax office locations including Waldviertel.

**Content:**
```
\bFA\s+(?:Purkersdorf|Nieder\u00f6sterreich\s+Mitte|Baden\s+M\u00f6dling|Innsbruck|Bruck\s+Eisenstadt\s+Oberwart|Freistadt\s+Rohrbach\s+Urfahr|Tirol\s+Ost|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Wien\s+1/23|Waldviertel)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 914 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

</details>

---

## `Mag. Ghesla Steuerberater GmbH Specific`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mag. Ghesla Steuerberater GmbH'.

**Content:**
```
\bMag\.\s+Ghesla\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 579 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

</details>

---

## `Finanzamts Genitive Locations`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamts' (genitive) followed by specific known locations.

**Content:**
```
\bFinanzamts\s+(?:Neunkirchen\s+(?:Wr\.\s+Neustadt|Wiener\s+Neustadt)|Wien\s+9/18/19\s+Klosterneuburg|Österreich|Amstetten\s+Melk\s+Scheibbs|Landeck\s+Reutte|Judenburg\s+Liezen|Salzburg-Stadt|Purkersdorf|Niederösterreich\s+Mitte|Baden\s+Mödling|Innsbruck|Bruck\s+Eisenstadt\s+Oberwart|Freistadt\s+Rohrbach\s+Urfahr|Tirol\s+Ost|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Oststeiermark|Linz|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 669 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

| Predicted | Gold |
|---|---|
| `Finanzamts Österreich` | `Finanzamts Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

| Predicted | Gold |
|---|---|
| `Finanzamts Österreich` | `Finanzamts Österreich` |

</details>

---

## `Magistrat Wien MA 67`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien, MA 67' specifically.

**Content:**
```
\bMagistrat\s+der\s+Stadt\s+Wien,\s+MA\s+67\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 137 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |

</details>

---

## `Deloitte Tax Wirtschaftsprüfungs GmbH`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Deloitte Tax Wirtschaftsprüfungs GmbH' allowing for variable whitespace (e.g., double spaces).

**Content:**
```
\bDeloitte\s+Tax\s+Wirtschaftsprüfungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 733 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

</details>

---

## `Magistrat der Stadt Wien, MA 67`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Magistrat/Magistrats/Magistrates der Stadt Wien, MA 67' covering nominative, genitive, and plural genitive forms.

**Content:**
```
\bMagistrat(?:s|es)?\s+der\s+Stadt\s+Wien,\s+MA\s+67\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 137 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |

</details>

---

## `Landespolizeidirektion Wien`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirektion Wien' and the typo 'Landespolizeidirketion Wien'.

**Content:**
```
\bLandespolizeidirektion\s+Wien\b|\bLandespolizeidirketion\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 133 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Finanzamt General Location`

**F1:** 0.004 | **Precision:** 0.333 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by a location, excluding known multi-word entities. Refined to be more robust.

**Content:**
```
\bFinanzamt\s+(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*|\d+\.\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b(?!(?:\s+1/23|\s+8/16/17|\s+2/20/21/22|\s+Klosterneuburg|\s+Landeck\s+Reutte|\s+Judenburg\s+Liezen|\s+Oststeiermark|\s+Linz|\s+St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|\s+Vorarlberg|\s+Graz\-Stadt|\s+Kirchdorf\s+Perg\s+Steyr|\s+Braunau\s+Ried\s+Sch\u00e4rding|\s+Hollabrunn\s+Korneuburg\s+Tulln|\s+Salzburg\-Stadt|\s+Innsbruck|\s+Bruck\s+Eisenstadt\s+Oberwart|\s+Freistadt\s+Rohrbach\s+Urfahr|\s+Tirol\s+Ost|\s+Deutschlandsberg\s+Leibnitz\s+Voitsberg|\s+Purkersdorf|\s+Nieder\u00f6sterreich\s+Mitte|\s+Baden\s+M\u00f6dling|\s+Waldviertel|\s+\u00d6sterreich))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.333 | 0.002 | 0.004 | 6 | 2 | 4 | 2 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 4 | 783 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_18`)


Zu Spruchpunkt I. (Gegenstandloserklärung)  Gemäß § 205 Abs 3 BAO kann der Abgabepflichtige dem Finanzamt Anzahlungen auf  Einkommensteuer bekanntgeben.

**False Positives:**

- `Finanzamt Anzahlungen` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_15`)


Nach den im Zuge einer Vorprüfung für die Jahre 2007 bis 2010 und den  Umsatzsteuernachschauzeitraum 2011 und 2012 getroffenen Feststellungen des damals  zuständigen Finanzamt Wien 6/7/15 sei das Vermietungsobjekt keine Einkunftsquelle.

**False Positives:**

- `Finanzamt Wien` — partial — pred ⊂ gold: `Finanzamt Wien 6/7/15`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Finanzamt Wien 6/7/15` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_15`)


Nach den im Zuge einer Vorprüfung für die Jahre 2007 bis 2010 und den  Umsatzsteuernachschauzeitraum 2011 und 2012 getroffenen Feststellungen des damals  zuständigen Finanzamt Wien 6/7/15 sei das Vermietungsobjekt keine Einkunftsquelle.

**False Positives:**

- `Finanzamt Wien` — partial — pred ⊂ gold: `Finanzamt Wien 6/7/15`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Finanzamt Wien 6/7/15` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149497.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149497.1_18`)


Zu Spruchpunkt I. (Gegenstandloserklärung)  Gemäß § 205 Abs 3 BAO kann der Abgabepflichtige dem Finanzamt Anzahlungen auf  Einkommensteuer bekanntgeben.

**False Positives:**

- `Finanzamt Anzahlungen` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Pensionsversicherungsanstalt`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt'.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.250 | 0.002 | 0.004 | 8 | 2 | 6 | 2 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 6 | 676 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_24`)


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

**False Positives:**

- `Pensionsversicherungsanstalt` — partial — pred ⊂ gold: `Pensionsversicherungsanstalt Wien`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_57`)


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_58`)


Auf den aktenkundigen Lohnzettel der Pensionsversicherungsanstalt sowie den im Akt  aufliegenden Kontrollmitteilungen wird verwiesen.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_24`)


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

**False Positives:**

- `Pensionsversicherungsanstalt` — partial — pred ⊂ gold: `Pensionsversicherungsanstalt Wien`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_57`)


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_58`)


Auf den aktenkundigen Lohnzettel der Pensionsversicherungsanstalt sowie den im Akt  aufliegenden Kontrollmitteilungen wird verwiesen.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `FA General Location`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by a location, excluding known multi-word entities. Refined to be more robust.

**Content:**
```
\bFA\s+(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*|\d+\.\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b(?!(?:\s+1/23|\s+8/16/17|\s+2/20/21/22|\s+Klosterneuburg|\s+Landeck\s+Reutte|\s+Judenburg\s+Liezen|\s+Oststeiermark|\s+Linz|\s+St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|\s+Vorarlberg|\s+Graz\-Stadt|\s+Kirchdorf\s+Perg\s+Steyr|\s+Braunau\s+Ried\s+Sch\u00e4rding|\s+Hollabrunn\s+Korneuburg\s+Tulln|\s+Salzburg\-Stadt|\s+Innsbruck|\s+Bruck\s+Eisenstadt\s+Oberwart|\s+Freistadt\s+Rohrbach\s+Urfahr|\s+Tirol\s+Ost|\s+Deutschlandsberg\s+Leibnitz\s+Voitsberg|\s+Purkersdorf|\s+Nieder\u00f6sterreich\s+Mitte|\s+Baden\s+M\u00f6dling|\s+Waldviertel|\s+\u00d6sterreich))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.250 | 0.002 | 0.004 | 8 | 2 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 6 | 914 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_50`)


Aufgrund der  Anrechnung von Prüfungen (FA Abweisungsbescheid 61675550) verkürzt sich die Wartezeit auf  ein Semester und beginnt ab März 2023 zu laufen und dauert bis September 2023.

**False Positives:**

- `FA Abweisungsbescheid` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

**False Positives:**

- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`
- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`

> partial: 2  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Bruemmer` (person)
- `Konstanze Bertling` (person)
- `Pabstbergstraße 45, 9135 Unterort, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `88-575/7122` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

**False Positives:**

- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`
- `FA St` — partial — pred ⊂ gold: `FA St. Johann Tamsweg Zell am See`

> partial: 2  |  missing annotation: 0

**Gold Entities:**
- `Univ.-Prof.in Jacqueline Bruemmer` (person)
- `Konstanze Bertling` (person)
- `Pabstbergstraße 45, 9135 Unterort, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `88-575/7122` (tax_number)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_50`)


Aufgrund der  Anrechnung von Prüfungen (FA Abweisungsbescheid 61675550) verkürzt sich die Wartezeit auf  ein Semester und beginnt ab März 2023 zu laufen und dauert bis September 2023.

**False Positives:**

- `FA Abweisungsbescheid` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `VfGH Acronym`

**F1:** 0.002 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the acronym 'VfGH' (Verfassungsgerichtshof) as a standalone organization, excluding cases where it is followed by dates (citations).

**Content:**
```
\bVfGH\b(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.002 | 2 | 1 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 509 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

**False Positives:**

- `VfGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Pastl+Bächle Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Pastl+Bächle Handel' which was missing from the rules.

**Content:**
```
\bPastl\+Bächle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht Zell am See`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirksgericht Zell am See'.

**Content:**
```
\bBezirksgericht\s+Zell\s+am\s+See\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Klusner&Päffgen Bildung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Klusner&Päffgen Bildung GMBH' which was missing and causing total misses.

**Content:**
```
\bKlusner&Päffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Englert Möbel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Englert Möbel' including cases where it is followed by a hyphenated suffix (e.g., 'Englert Möbel -Konzernes').

**Content:**
```
\b(Englert\s+Möbel)(?:\s*-\w+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank' followed by specific location patterns, extended to capture full multi-word locations like 'Karnische Rion Bankstelle St.Stefan'.

**Content:**
```
\bRaiffeisenbank\s+(?:Hippach-Hart|genburg|Stallhofen|[A-Z][a-zA-Z\-\s]+?)(?=\s*(?:als|an|der|des|die|den|dem|bei|von|mit|f\u00fcr|zur|in|auf|\u00fcber|unter|nach|vor|durch|gegen|ohne|um|bis|seit|statt|trotz|w\u00e4hrend|wegen|laut|neben|au\u00dfer|au\u00dferhalb|innerhalb|entlang|gegen\u00fcber|KG|GmbH|GMBH|AG|&|Co|\s+[a-z]|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Hülsebusch + Breithaupt Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hülsebusch + Breithaupt Versicherung' including cases where it is followed by 'GmbH & Co KG'.

**Content:**
```
\bHülsebusch\s+\+\s+Breithaupt\s+Versicherung(?:\s+GmbH\s+&\s+Co\s+KG)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Logal Gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Logal Gruppe'.

**Content:**
```
\bLogal\s+Gruppe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Enns Werkal GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Enns Werkal GMBH'.

**Content:**
```
\bEnns\s+Werkal\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Süd Nortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Süd Nortri'.

**Content:**
```
\bSüd\s+Nortri\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Trafenfen Automotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Trafenfen Automotive'.

**Content:**
```
\bTrafenfen\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Mur Ververzor Betriebe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mur Ververzor Betriebe'.

**Content:**
```
\bMur\s+Ververzor\s+Betriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Kornfelder Recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Kornfelder Recycling'.

**Content:**
```
\bKornfelder\s+Recycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Füchsl Touristik GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Füchsl Touristik GMBH'.

**Content:**
```
\bFüchsl\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Mägerlein Logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mägerlein Logistik'.

**Content:**
```
\bMägerlein\s+Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Roelfsen Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Roelfsen Versicherung'.

**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Lubomir Merschmeyer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lubomir Merschmeyer'.

**Content:**
```
\bLubomir\s+Merschmeyer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Houdek Maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Houdek Maschinenbau'.

**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Schmeltz Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Schmeltz Luftfahrt'.

**Content:**
```
\bSchmeltz\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Dorfcon-Verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Dorfcon-Verlag'.

**Content:**
```
\bDorfcon\-Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Lexdon IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lexdon IT'.

**Content:**
```
\bLexdon\s+IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Wien 1/23 Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Wien 1/23' to ensure the full numeric code is captured, fixing the partial match issue.

**Content:**
```
\bFA\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Naaß Elektro GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Naaß Elektro GMBH'.

**Content:**
```
\bNaaß\s+Elektro\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bersud Möbel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bersud Möbel GMBH'.

**Content:**
```
\bBersud\s+Möbel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Unter Heimdorf GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Unter Heimdorf GMBH'.

**Content:**
```
\bUnter\s+Heimdorf\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Buhrfeindt Lebensmittel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Buhrfeindt Lebensmittel GMBH'.

**Content:**
```
\bBuhrfeindt\s+Lebensmittel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Mur Alver OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mur Alver OG'.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Tritri-IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Tritri-IT' including cases where it is followed by a hyphenated suffix (e.g., 'Tritri-IT -Konzernes').

**Content:**
```
\b(Tritri-IT)(?:\s*-\w+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Gözcü Getränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Gözcü Getränke' which was missing from the rules.

**Content:**
```
\bGözcü\s+Getränke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Dongartcon-Landwirtschaft GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Dongartcon-Landwirtschaft GMBH'.

**Content:**
```
\bDongartcon\-Landwirtschaft\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Monlogtri-Analyse GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Monlogtri-Analyse GMBH'.

**Content:**
```
\bMonlogtri\-Analyse\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Traun Aluni Institut GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Traun Aluni Institut GMBH'.

**Content:**
```
\bTraun\s+Aluni\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Specific Locations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by specific known tax office locations including Waldviertel.

**Content:**
```
\bFinanzamt\s+(?:Purkersdorf|Nieder\u00f6sterreich\s+Mitte|Baden\s+M\u00f6dling|Innsbruck|Bruck\s+Eisenstadt\s+Oberwart|Freistadt\s+Rohrbach\s+Urfahr|Wien\s+1/23|Klosterneuburg|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Waldviertel)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Berend Energie AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Berend Energie AG'.

**Content:**
```
\bBerend\s+Energie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Blazickova & Hepprich Energie AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Blazickova & Hepprich Energie AG'.

**Content:**
```
\bBlazickova\s+&\s+Hepprich\s+Energie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Botho Mikloweit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Botho Mikloweit'.

**Content:**
```
\bBotho\s+Mikloweit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Unter Gartglanz GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Unter Gartglanz GMBH'.

**Content:**
```
\bUnter\s+Gartglanz\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzen Tradonnex GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzen Tradonnex GmbH' which was missing.

**Content:**
```
\bFinanzen\s+Tradonnex\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Obernöder+Küsbert Touristik GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Obernöder+Küsbert Touristik GMBH'.

**Content:**
```
\bObernöder\+Küsbert\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Talost GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Talost GMBH'.

**Content:**
```
\bTalost\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `DonauRecycling GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'DonauRecycling GMBH'.

**Content:**
```
\bDonauRecycling\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `XJOV Cloud Dienstleistungen GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'XJOV Cloud Dienstleistungen GMBH'.

**Content:**
```
\bXJOV\s+Cloud\s+Dienstleistungen\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `MittelHeizung Werke AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'MittelHeizung Werke AG' which was missing from the rules.

**Content:**
```
\bMittelHeizung\s+Werke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Traun-Digital KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Traun-Digital KG' to prevent partial matching by the generic KG rule.

**Content:**
```
\bTraun-Digital\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Klosterneuburg Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Klosterneuburg' specifically to ensure it is captured.

**Content:**
```
\bFA\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Amstetten Melk Scheibbs Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Amstetten Melk Scheibbs' specifically.

**Content:**
```
\bFinanzamt\s+Amstetten\s+Melk\s+Scheibbs\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien 8/16/17 Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Wien 8/16/17' specifically.

**Content:**
```
\bFinanzamt\s+Wien\s+8/16/17\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Wien 8/16/17 Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Wien 8/16/17' specifically.

**Content:**
```
\bFA\s+Wien\s+8/16/17\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Gernot Hirschkorn Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gernot Hirschkorn' as an organisation in legal contexts.

**Content:**
```
\bGernot\s+Hirschkorn\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Schweizerischen Unfallversicherungsanstalt (SUVA)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name of the Swiss accident insurance institution including the acronym in parentheses, ensuring it takes precedence over the acronym rule.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `UnterRecycling Services GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'UnterRecycling Services GMBH' which was missing from the rules.

**Content:**
```
\bUnterRecycling\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `AMS`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'AMS' only when not followed by 'Österreich' or part of 'Arbeitsmarktservice (AMS)'.

**Content:**
```
\bAMS\b(?!\s+Österreich)(?!\s*\(\s*\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bundesamt für Soziales und Behindertenwesen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its genitive forms 'Bundesamtes' and 'Bundesamts'.

**Content:**
```
\bBundesamte?s?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Landespolizeidirketion Tirol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Landespolizeidirketion Tirol' (including the typo 'dirketion' as seen in training data).

**Content:**
```
\bLandespolizeidirketion\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Wien 9/18/19 Klosterneuburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific genitive entity 'Finanzamtes Wien 9/18/19 Klosterneuburg'.

**Content:**
```
\bFinanzamtes\s+Wien\s+9/18/19\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Musikhochschule Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Musikhochschule Wien'.

**Content:**
```
\bMusikhochschule\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Konservatorium der Stadt Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Konservatorium der Stadt Wien'.

**Content:**
```
\bKonservatorium\s+der\s+Stadt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Wiener Philharmoniker`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wiener Philharmoniker'.

**Content:**
```
\bWiener\s+Philharmoniker\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `AMS Österreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'AMS Österreich' specifically to prevent the generic 'AMS' rule from matching just the acronym.

**Content:**
```
\bAMS\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Arbeitsmarktservice (AMS)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Arbeitsmarktservice (AMS)' specifically.

**Content:**
```
\bArbeitsmarktservice\s*\(\s*AMS\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Wien 2/20/21/22 Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Wien 2/20/21/22' which was missing.

**Content:**
```
\bFA\s+Wien\s+2/20/21/22\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Landeck Reutte Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Landeck Reutte' which was missing.

**Content:**
```
\bFA\s+Landeck\s+Reutte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Oststeiermark Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Oststeiermark'.

**Content:**
```
\bFA\s+Oststeiermark\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Linz Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Linz'.

**Content:**
```
\bFA\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Judenburg Liezen Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Judenburg Liezen' which was missing.

**Content:**
```
\bFA\s+Judenburg\s+Liezen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg-Stadt Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Salzburg-Stadt'.

**Content:**
```
\bFinanzamt\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Landeck Reutte Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Landeck Reutte'.

**Content:**
```
\bFinanzamt\s+Landeck\s+Reutte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Judenburg Liezen Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Judenburg Liezen'.

**Content:**
```
\bFinanzamt\s+Judenburg\s+Liezen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `ÖBUG Full Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full complex entity 'ÖBUG' DR. NIKOLAUS Wirtschaftstreuhand GmbH - Wirtschaftsprüfungs- und Steuerberatungsgesellschaft' with flexible whitespace.

**Content:**
```
\b"\u00d6BUG"\s+DR\.\s+NIKOLAUS\s+Wirtschaftstreuhand\s+GmbH\s*-\s*Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Österreichische Gesellschaft für Europapolitik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Österreichische Gesellschaft für Europapolitik'.

**Content:**
```
\bÖsterreichische\s+Gesellschaft\s+für\s+Europapolitik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `BM für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'BM für Finanzen'.

**Content:**
```
\bBM\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `TPA STB Wien GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'TPA STB Wien GmbH'.

**Content:**
```
\bTPA\s+STB\s+Wien\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `INET Internet Service GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'INET Internet Service GmbH'.

**Content:**
```
\bINET\s+Internet\s+Service\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `UFS Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat).

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 434 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_30`)


Der Zeitpunkt, an dem die Daten in den elektronischen Verfügungsbereich des Empfängers  gelangt sind, ist bei FinanzOnline der Zeitpunkt der Einbringung der Daten in die Databox, zu  der der Empfänger Zugang hat (UFS 22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_41`)


UFS  22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_55`)


Wird zu einem späteren Zeitpunkt festgestellt, dass Beiträge nicht oder in geringerer Höhe zu  leisten gewesen wären, ändert dies nichts an ihrem ursprünglichen Charakter (UFS 15.4.2013,  RV/0220-W/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149731.1`) (sent_id: `findok-manually-annotated_TRAIN/149731.1_30`)


Der Zeitpunkt, an dem die Daten in den elektronischen Verfügungsbereich des Empfängers  gelangt sind, ist bei FinanzOnline der Zeitpunkt der Einbringung der Daten in die Databox, zu  der der Empfänger Zugang hat (UFS 22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149731.1`) (sent_id: `findok-manually-annotated_TRAIN/149731.1_41`)


UFS  22.7.2013, RV/0002-F/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_55`)


Wird zu einem späteren Zeitpunkt festgestellt, dass Beiträge nicht oder in geringerer Höhe zu  leisten gewesen wären, ändert dies nichts an ihrem ursprünglichen Charakter (UFS 15.4.2013,  RV/0220-W/13;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `INET System Informations GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'INET System Informations GmbH' including cases with double spaces.

**Content:**
```
\bINET\s+System\s+Informations\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `UFS/BFG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the combined entity 'UFS/BFG' to prevent splitting into 'UFS' and 'BFG'.

**Content:**
```
\bUFS/BFG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `How to spend it Verlag GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'How to spend it Verlag GmbH'.

**Content:**
```
\bHow\s+to\s+spend\s+it\s+Verlag\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FH Kärnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FH Kärnten'.

**Content:**
```
\bFH\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Karl-Franzens- Universität Graz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Karl-Franzens- Universität Graz'.

**Content:**
```
\bKarl-Franzens-\s+Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `BKS Steuerberatung GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BKS Steuerberatung GmbH & Co KG'.

**Content:**
```
\bBKS\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Fachhochschule Kärnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Fachhochschule Kärnten'.

**Content:**
```
\bFachhochschule\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `BFH Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'BFH' (Bundesfinanzgericht) as an organisation.

**Content:**
```
\bBFH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH' including cases with double spaces.

**Content:**
```
\bHuber\s+Swoboda\s+Oswald\s+Aixberger\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `London Film Academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and its common typo 'Acadamy', handling double spaces.

**Content:**
```
\bLondon\s+Film\s+Acad(\s+)?(a|e)m(y|y)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bundeskanzleramtes`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the genitive form 'Bundeskanzleramtes'.

**Content:**
```
\bBundeskanzleramtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `PVA Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'PVA' (Pflegeversicherung) as an organisation.

**Content:**
```
\bPVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `SVS/SVB Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the combined acronym 'SVS/SVB' (Sozialversicherung der Selbständigen / Sozialversicherung der Bauern) as an organisation.

**Content:**
```
\bSVS/SVB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `PSD Wien Ambulatorium Landstraße`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'PSD Wien Ambulatorium Landstraße' with high priority to prevent partial matching by the generic 'PSD Wien' rule.

**Content:**
```
\bPSD\s+Wien\s+Ambulatorium\s+Landstraße\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Sozialversicherungsanstalt der Bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherungsanstalt der Bauern' and its genitive form 'Sozialversicherungsanstalt der Bauern' (no change in genitive for this specific entity in common usage, but handles the full name).

**Content:**
```
\bSozialversicherungsanstalt\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Sozialversicherung der Bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherung der Bauern' and its genitive form 'Sozialversicherung der Bauern'.

**Content:**
```
\bSozialversicherung\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 354 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_200`)


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

**False Positives:**

- `Sozialversicherung der Bauern` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `WKO` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_200`)


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

**False Positives:**

- `Sozialversicherung der Bauern` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `WKO` (organisation)

</details>

---

## `PSD Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'PSD Wien'.

**Content:**
```
\bPSD\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Psychiatrie Otto Wagner Spital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Psychiatrie Otto Wagner Spital' including the hyphenated suffix seen in training data.

**Content:**
```
\bPsychiatrie\s+Otto\s+Wagner\s+Spital(?:-)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name of the ministry, handling the genitive 'Bundesministers' and the specific list of departments.

**Content:**
```
\bBundesministers?\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht BFG Full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht (BFG)' as a single entity to prevent splitting.

**Content:**
```
\bBundesfinanzgericht\s*\(\s*BFG\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Saxinger Chalupsky & Partner Rechtsanwälte GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm 'Saxinger Chalupsky & Partner Rechtsanwälte GmbH'.

**Content:**
```
\bSaxinger\s+Chalupsky\s+&\s+Partner\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Imre & Schaffer Rechtsanwälte OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm 'Imre & Schaffer Rechtsanwälte OG'.

**Content:**
```
\bImre\s+&\s+Schaffer\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Vorarlberg Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Vorarlberg'.

**Content:**
```
\bFA\s+Vorarlberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Klagenfurt St. Veit Wolfsberg Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Klagenfurt St. Veit Wolfsberg'.

**Content:**
```
\bFinanzamt\s+Klagenfurt\s+St\.\s+Veit\s+Wolfsberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Bruck Eisenstadt Oberwart Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Bruck Eisenstadt Oberwart'.

**Content:**
```
\bFinanzamt\s+Bruck\s+Eisenstadt\s+Oberwart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Landeck Reutte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the genitive form 'Finanzamtes Landeck Reutte'.

**Content:**
```
\bFinanzamtes\s+Landeck\s+Reutte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Garanta VersicherungsAG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Garanta VersicherungsAG'.

**Content:**
```
\bGaranta\s+VersicherungsAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Sivananda Yoga Centre`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'The International Sivananda Yoga Vedanta Centre'.

**Content:**
```
\bThe\s+International\s+Sivananda\s+Yoga\s+Vedanta\s+Centre\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `DA Deutsche Allgemeine Versicherung AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'DA Deutsche Allgemeine Versicherung AG'.

**Content:**
```
\bDA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Geschenkartikel GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Geschenkartikel GmbH'.

**Content:**
```
\bGeschenkartikel\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `AVED cosmetic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'AVED cosmetic' which was missing.

**Content:**
```
\bAVED\s+cosmetic\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Yoga Vidya GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Yoga Vidya GmbH'.

**Content:**
```
\bYoga\s+Vidya\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Hamburger Fern-Hochschule`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hamburger Fern-Hochschule'.

**Content:**
```
\bHamburger\s+Fern-Hochschule\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Wirtschaftsuniversität Wien Full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name with abbreviation in parentheses: 'Wirtschaftsuniversität Wien (WU Wien)'.

**Content:**
```
\bWirtschaftsuniversität\s+Wien\s*\(\s*WU\s+Wien\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Johannes Kepler Universität Linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Johannes Kepler Universität Linz' and its abbreviation 'JKU Linz'.

**Content:**
```
\b(?:Johannes\s+Kepler\s+Universität\s+Linz|JKU\s+Linz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Johannes Kepler Universität Linz Full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name with abbreviation in parentheses: 'Johannes Kepler Universität Linz (JKU Linz)'.

**Content:**
```
\bJohannes\s+Kepler\s+Universität\s+Linz\s*\(\s*JKU\s+Linz\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `JKU Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the standalone abbreviation 'JKU' only when not followed by 'Linz' or '(', to avoid partial matches of 'JKU Linz' or 'JKU (JKU)'.

**Content:**
```
\bJKU\b(?!\s+Linz|\s*\()
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Universität St. Gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Universität St. Gallen' and 'Universität in St. Gallen', handling variable whitespace.

**Content:**
```
\bUniversität\s+(?:in\s+)?St\.\s+Gallen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Tschurtschenthaler Walder Fister Rechtsanwälte GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH' handling variable whitespace.

**Content:**
```
\bTschurtschenthaler,\s+Walder,\s+\s*Fister\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Immobilienbüro Mandl`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Immobilienbüro Mandl'.

**Content:**
```
\bImmobilienbüro\s+Mandl\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt Klagenfurt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Klagenfurt' and its genitive form 'Magistrats der Stadt Klagenfurt'.

**Content:**
```
\bMagistrat(?:s)?\s+der\s+Stadt\s+Klagenfurt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Inneres' (genitive) and 'Bundesministerium für Inneres' (nominative).

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Berwaldkel-Möbel AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Berwaldkel-Möbel AG'.

**Content:**
```
\bBerwaldkel\-Möbel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Amts für Betrugsbekämpfung Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amts für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmts?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 676 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_3`)


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_10`)


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_140`)


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Zollamt Österreich` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_3`)


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_10`)


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_140`)


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Zollamt Österreich` (organisation)

</details>

---

## `FAG Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAG' (Finanzamt für Großbetriebe) as an organisation.

**Content:**
```
\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `LG Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LG Innsbruck' (Landesgericht Innsbruck acronym).

**Content:**
```
\bLG\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Landesgericht Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Landesgericht Innsbruck'.

**Content:**
```
\bLandesgericht\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht Silz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht Silz' specifically to ensure the location is captured.

**Content:**
```
\bBezirksgericht\s+Silz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `LG für ZRS Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'LG für ZRS Wien' (Landesgericht für Zivilrechtssachen Wien).

**Content:**
```
\bLG\s+für\s+ZRS\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Justiz Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Justiz' (genitive) and 'Bundesministerium für Justiz' (nominative).

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Justiz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Anwälte Mandl & Mitterbauer GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Anwälte Mandl & Mitterbauer GmbH' which was missing from the rules.

**Content:**
```
\bAnwälte\s+Mandl\s+&\s+Mitterbauer\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Schule Gesundheitspflege Grillenreith`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the complex entity 'Schule für allgemeine Gesundheits- und Krankenpflege' with variations for location ('am LKH', 'in') and variable whitespace.

**Content:**
```
\bSchule\s+für\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+(?:am\s+LKH\s+Grillenreith|in\s+Grillenreith|Grillenreith)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `GesundheitspflegeSchule LKH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the alternative phrasing 'Gesundheits- und Krankenpflege-Schule am LKH Grillenreith'.

**Content:**
```
\bGesundheits\-\s+und\s+Krankenpflege\-Schule\s+am\s+LKH\s+Grillenreith\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Graz-Stadt Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Graz-Stadt' which might be missed by general FA rules due to the hyphenated location.

**Content:**
```
\bFA\s+Graz\-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Hinklein Organisation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hinklein' as an organization name in legal contexts (party names), but only if followed by a specific context or at the start of a sentence.

**Content:**
```
\bHinklein\b(?=\s+(?:als|und|mit|von|bei|in|auf|an|zu|für|nach|vor|durch|gegen|ohne|bis|seit|statt|trotz|während|wegen|laut|neben|außer|außerhalb|innerhalb|entlang|gegenüber|KG|GmbH|GMBH|AG|&|Co|\s+[a-z]|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `KG Companies Refined`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'KG', excluding 'Co KG' as a standalone match, ensuring a proper name precedes it and stopping before punctuation.

**Content:**
```
\b([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+)*\s+KG)\b(?!\s*&\s*Co)(?![\s]*[.,;:])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bankhaus Denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bankhaus Denzel' which was missing and causing total misses.

**Content:**
```
\bBankhaus\s+Denzel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Cervenka&Neunübel Telekom AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Cervenka&Neunübel Telekom AG' to prevent partial matching by generic AG rules.

**Content:**
```
\bCervenka&Neunübel\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific genitive entity 'Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf' which was missing.

**Content:**
```
\bFinanzamtes\s+Wien\s+3/6/7/11/15\s+Schwechat\s+Gerasdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Frontex'.

**Content:**
```
\bFrontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Europäische Grenzschutzagentur Frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Europäische Grenzschutzagentur Frontex' and its genitive form 'Europäischen Grenzschutzagentur Frontex'.

**Content:**
```
\bEuropäischen?\s+Grenzschutzagentur\s+Frontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `BM für Inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'BM für Inneres'.

**Content:**
```
\bBM\s+für\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH & Co KG' with flexible whitespace.

**Content:**
```
\bTAXCOACH\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Kriminalpolizei in Österreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Kriminalpolizei in Österreich'.

**Content:**
```
\bKriminalpolizei\s+in\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `EASO`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'EASO' (European Asylum Support Office).

**Content:**
```
\bEASO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `BMI`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'BMI' (Bundesministerium für Inneres).

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Flughafen München`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Flughafen München'.

**Content:**
```
\bFlughafen\s+München\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `OECD`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'OECD' (Organisation for Economic Co-operation and Development).

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 4 | 531 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_107`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

**False Positives:**

- `OECD` — no gold match — missing annotation
- `OECD` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_107`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

**False Positives:**

- `OECD` — no gold match — missing annotation
- `OECD` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

</details>

---

## `Arbeits- und Sozialgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Arbeits- und Sozialgericht' with optional 'Wien' suffix and variable whitespace.

**Content:**
```
\bArbeits\-\s+und\s+Sozialgericht(?:\s+Wien)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Eckhardt SteuerberatungsgmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Eckhardt SteuerberatungsgmbH'.

**Content:**
```
\bEckhardt\s+SteuerberatungsgmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Amts für Betrugsbekämpfung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amts für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung' with flexible whitespace.

**Content:**
```
\bAmts?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 676 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_3`)


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_10`)


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_140`)


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Zollamt Österreich` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_3`)


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_10`)


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_140`)


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

**False Positives:**

- `Amt für  Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Zollamt Österreich` (organisation)

</details>

---

## `Bundesministers für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Finanzen' and its base form 'Bundesminister für Finanzen'.

**Content:**
```
\bBundesministers?\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Magistrates der Stadt Wien, Magistratsabteilung 67`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full entity 'Magistrates der Stadt Wien, Magistratsabteilung 67' as a single unit.

**Content:**
```
\bMagistrates\s+der\s+Stadt\s+Wien,\s+Magistratsabteilung\s+67\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Höhere Lehranstalt für Tourismus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific school entity 'Höhere Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit' and its genitive form 'Höheren Lehranstalt...'.

**Content:**
```
\b(Höhere|Höheren)\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `HLF Krems/Donau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific abbreviation 'HLF Krems/Donau'.

**Content:**
```
\bHLF\s+Krems/Donau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Verfassungsgerichtshof Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the genitive form 'Verfassungsgerichtshofes' which was missing.

**Content:**
```
\bVerfassungsgerichtshofes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Paugger Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Paugger Steuerberatung GmbH' to prevent partial matching.

**Content:**
```
\bPaugger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG', handling variable whitespace.

**Content:**
```
\bHallas\s+&\s+Partner\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `King's School`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'King's School' and variations with different apostrophes (e.g., King´s).

**Content:**
```
\bKing['´]s\s+School\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `The King's School Worcester`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'The King's School Worcester' and variations with different apostrophes.

**Content:**
```
\bThe\s+King['´]s\s+School\s+Worcester\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `University of Bristol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'University of Bristol'.

**Content:**
```
\bUniversity\s+of\s+Bristol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `England`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'England' as an organization in legal contexts (e.g., jurisdiction).

**Content:**
```
\bEngland\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `King's School Worcester`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full entity 'King's School Worcester' to prevent partial matching by the generic 'King's School' rule.

**Content:**
```
\bKing['\u00b4]s\s+School\s+Worcester\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Grazer Treuhand Steuerberatung GmbH & Partner KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Grazer Treuhand Steuerberatung GmbH & Partner KG' to prevent partial matching by the generic GmbH rule.

**Content:**
```
\bGrazer\s+Treuhand\s+Steuerberatung\s+GmbH\s+&\s+Partner\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Kirchdorf Perg Steyr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Kirchdorf Perg Steyr' to ensure the full location is captured.

**Content:**
```
\bFA\s+Kirchdorf\s+Perg\s+Steyr\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Kirchdorf Perg Steyr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Kirchdorf Perg Steyr' to ensure the full location is captured.

**Content:**
```
\bFinanzamt\s+Kirchdorf\s+Perg\s+Steyr\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamts Graz-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamts Graz-Stadt' (genitive).

**Content:**
```
\bFinanzamts\s+Graz\-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamts Graz- Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamts Graz- Stadt' (genitive with space).

**Content:**
```
\bFinanzamts\s+Graz\-\s+Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Rhein Normonkel Manufaktur GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Rhein Normonkel Manufaktur GMBH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bRhein\s+Normonkel\s+Manufaktur\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Merkur Treuhand Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Merkur Treuhand Steuerberatung GmbH' including variants with double spaces.

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Österreich (DST12)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich (DST12)' specifically to capture the full entity including the acronym.

**Content:**
```
\bFinanzamt\s+Österreich\s*\(\s*DST12\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Schabetsberger Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schabetsberger Steuerberatung GmbH' including variants with double spaces.

**Content:**
```
\bSchabetsberger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Merkur Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Merkur Steuerberatung GmbH' including variants with double spaces.

**Content:**
```
\bMerkur\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `UFS Salzburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'UFS Salzburg'.

**Content:**
```
\bUFS\s+Salzburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Merkur Treuhand Steuerberatung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Merkur Treuhand Steuerberatung' (without GmbH) including variants with double spaces.

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Verwaltungsgericht Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgericht Wien' specifically.

**Content:**
```
\bVerwaltungsgericht\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Wiederspan Beratung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wiederspan Beratung GMBH'.

**Content:**
```
\bWiederspan\s+Beratung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Retail Giants Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific retail entities: Ikea, Obi, Leiner, Möbelix, MömaX.

**Content:**
```
\b(?:Ikea|Obi|Leiner|Möbelix|MömaX)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Steuerberater Metzler & Adelsberger OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Steuerberater Metzler & Adelsberger OG' to prevent partial matching by generic OG rules.

**Content:**
```
\bSteuerberater\s+Metzler\s+&\s+Adelsberger\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Braunau Ried Schärding`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific multi-word entity 'FA Braunau Ried Schärding' with high priority to prevent truncation.

**Content:**
```
\bFA\s+Braunau\s+Ried\s+Sch\u00e4rding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the genitive form 'Finanzamtes Innsbruck'.

**Content:**
```
\bFinanzamtes\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `B-GmbH Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'B-GmbH' which was missing and causing total misses.

**Content:**
```
\bB-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `A-GmbH Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'A-GmbH' which was missing and causing total misses.

**Content:**
```
\bA-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Hausverwaltung-GmbH Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hausverwaltung-GmbH' which was missing and causing total misses.

**Content:**
```
\bHausverwaltung-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bezirkshauptmannschaft Bludenz Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirkshauptmannschaft Bludenz' which was missing and causing total misses.

**Content:**
```
\bBezirkshauptmannschaft\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Braunau Ried Schärding Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Braunau Ried Schärding' with high priority.

**Content:**
```
\bFinanzamt\s+Braunau\s+Ried\s+Sch\u00e4rding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `ÖBB Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Austrian Federal Railways acronym 'ÖBB'.

**Content:**
```
\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `SeneCura General`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SeneCura' and its variations including the full location 'Laurentius Park Bludenz'.

**Content:**
```
\b(?:SENECURA|SeneCura|Senecura)(?:\s+(?:Laurentius\s+Park\s+Bludenz|Laurentius-Park\s+Bludenz|Laurentius\s+Park|Laurentius-Park))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Krankenpflegevereins Bludenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Krankenpflegevereins Bludenz' which was missing from the rules.

**Content:**
```
\bKrankenpflegevereins\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Mittel Unisyn GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mittel Unisyn GMBH' which was missing.

**Content:**
```
\bMittel\s+Unisyn\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Ober Lemostnor AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Ober Lemostnor AG' which was missing.

**Content:**
```
\bOber\s+Lemostnor\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Vennes Recycling AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Vennes Recycling AG' which was missing.

**Content:**
```
\bVennes\s+Recycling\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bärs & Walterscheidt Handel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bärs & Walterscheidt Handel GMBH' which was missing.

**Content:**
```
\bBärs\s+&\s+Walterscheidt\s+Handel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `InnMarine GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'InnMarine GMBH'.

**Content:**
```
\bInnMarine\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Universität Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Universität Innsbruck'.

**Content:**
```
\bUniversität\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Lenfeld/Leys/Sonderegger Rechtsanwälte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm 'Lenfeld/Leys/Sonderegger Rechtsanwälte'.

**Content:**
```
\bLenfeld/Leys/Sonderegger\s+Rechtsanwälte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Neunkirchen Wr. Neustadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific genitive entity 'Finanzamtes Neunkirchen Wr. Neustadt' with flexible whitespace.

**Content:**
```
\bFinanzamtes\s+(?:Neunkirchen\s+Wr\.\s+Neustadt|Neunkirchen\s+Wiener\s+Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Finanzamtes Hollabrunn Korneuburg Tulln Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific genitive entity 'Finanzamtes Hollabrunn Korneuburg Tulln' which was missing in the failure case.

**Content:**
```
\bFinanzamtes\s+Hollabrunn\s+Korneuburg\s+Tulln\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Unter Donunisee AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Unter Donunisee AG' with high priority to ensure it is captured correctly even if preceded by common nouns.

**Content:**
```
\bUnter\s+Donunisee\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bundesministerin für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerin für Finanzen' and its genitive form 'Bundesministersin für Finanzen' (or 'Bundesministers' if typo).

**Content:**
```
\bBundesministers?in\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `X GmbH Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'X GmbH' which appears in training data and was missing from specific rules.

**Content:**
```
\bX\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `BDO Austria GmbH WP- u. StBges.`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BDO Austria GmbH WP- u. StBges.' which was missing from the rules.

**Content:**
```
\bBDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater' which was missing from the rules.

**Content:**
```
\bLeitnerLeitner\s+GmbH\s+Wirtschaftsprüfer\s+und\s+Steuerberater\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `BFG Außenstelle Linz Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BFG, Außenstelle Linz' to ensure the full location is captured as a single organization, preventing splitting by the generic BFG rule.

**Content:**
```
\bBFG,\s+Außenstelle\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `R GmbH Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'R GmbH' which was missing from the rules.

**Content:**
```
\bR\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `X-GmbH Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'X-GmbH' which was missing and causing total misses in the failure case.

**Content:**
```
\bX-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `AG General Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches generic company names ending in AG, with stricter context checks to avoid matching common nouns. Requires at least two words before AG or a specific structure.

**Content:**
```
\b(?<!Firma\s)(?!\sFirma)(?<!Arbeitgeber\s)(?!\sArbeitgeber)(?<!Gesellschaft\s)(?!\sGesellschaft)(?<!Firmen\s)(?!\sFirmen)(?<!Unternehmen\s)(?!\sUnternehmen)(?<!Adr\s)(?!\sAdr)([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\s+AG)\b(?!\s*&\s*Co)(?![\s]*[.,;:])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `KG General Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in KG, with strict context checks. Excludes 'Co KG' as a standalone match and ensures a proper name precedes it.

**Content:**
```
\b([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+)*\s+KG)\b(?!\s*&\s*Co)(?![\s]*[.,;:])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `FA Österreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Österreich' specifically to ensure it is captured.

**Content:**
```
\bFA\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Rechtsanwaltskanzlei Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches law firms ending in 'Rechtsanwaltskanzlei' or 'Rechtsanwälte' with optional 'GmbH' or 'OG'. Requires at least two words before the suffix to avoid matching 'Partner Rechtsanwälte' as a standalone entity.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+\s+(?:Rechtsanwaltskanzlei|Rechtsanwälte)(?:\s+(?:GmbH|GMBH|OG|Partnerschaft))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Sozialversicherung Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherung' followed by 'der' and a group (e.g., 'der Bauern', 'der Selbständigen').

**Content:**
```
\bSozialversicherung\s+der\s+(?:Bauern|Selbständigen|Landwirte)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 354 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_200`)


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

**False Positives:**

- `Sozialversicherung der Bauern` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `WKO` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_200`)


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

**False Positives:**

- `Sozialversicherung der Bauern` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `WKO` (organisation)

</details>

---

## `Partnerschaft Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organizations ending in 'Partnerschaft' (e.g., 'Partnerschaft M. Müller').

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\s+Partnerschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht General Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht' followed by a location name to capture unseen district courts.

**Content:**
```
\bBezirksgericht\s+(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*|\d+\.\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Landesgericht General Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Landesgericht' followed by a location name to capture unseen state courts.

**Content:**
```
\bLandesgericht\s+(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*|\d+\.\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

</details>

---

