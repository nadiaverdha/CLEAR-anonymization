# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-21T23:37:09.081590

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-21_v9/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2327 |
| Validation documents | 218 |
| Test documents | 108 |
| Train sentences | 2327 |
| Validation sentences | 218 |
| Test sentences | 12077 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
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
| Accuracy (exact match) | 90.2% |
| True Positives | 1243 |
| False Positives | 1051 |
| Micro Precision | 54.2% |
| Micro Recall | 71.3% |
| Micro F1 | 61.6% |
| Macro F1 | 61.6% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Specific Entity: KQPC Versand GMBH` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `Specific Entity: Event Sudkraftlex GMBH` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `Specific Entity: Sudver Handel Services GMBH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: Glanznorost Institut GMBH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: Missing Known Organizations` | 15.3% | 100.0% | 8.3% | 144 | 144 | 0 |
| `Specific Entity: Wiederspan Beratung GMBH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Mur Alver OG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Tritri-IT` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Bankhaus Denzel` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Specific Entity: Cervenka&Neunübel Telekom AG` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: ÖGK` | 4.5% | 100.0% | 2.3% | 40 | 40 | 0 |
| `Specific Entity: Bundesamt für Soziales und Behindertenwesen` | 1.5% | 100.0% | 0.7% | 13 | 13 | 0 |
| `Specific Entity: Landespolizeidirketion Tirol` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Musikhochschule Wien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Konservatorium der Stadt Wien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Wiener Philharmoniker` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: INET Internet Service GmbH` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Specific Entity: INET System Informations GmbH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: UFS/BFG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: How to spend it Verlag GmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Landespolizeidirektion Wien` | 0.9% | 100.0% | 0.5% | 8 | 8 | 0 |
| `Specific Entity: Garanta VersicherungsAG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: The International Sivananda Yoga Vedanta Centre` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: DA Deutsche Allgemeine Versicherung AG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Geschenkartikel GmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: AVED cosmetic` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Yoga Vidya GmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Hamburger Fern-Hochschule` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Universität St. Gallen` | 0.8% | 100.0% | 0.4% | 7 | 7 | 0 |
| `Specific Entity: Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Immobilienbüro Mandl` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Magistrat der Stadt Klagenfurt` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: Berwaldkel-Möbel AG` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Specific Entity: FAG` | 2.6% | 100.0% | 1.3% | 23 | 23 | 0 |
| `Specific Entity: FAÖ` | 4.6% | 100.0% | 2.4% | 41 | 41 | 0 |
| `Specific Entity: Deloitte Tax Wirtschaftsprüfungs GmbH` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `Specific Entity: Schule für allgemeine Gesundheits- und Krankenpflege` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Specific Entity: BM für Inneres` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: Kriminalpolizei in Österreich` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: EASO` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: BMI` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Specific Entity: Flughafen München` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Specific Entity: Eckhardt SteuerberatungsgmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: HLF Krems/Donau` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Höhere Lehranstalt für Tourismus` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: Universität Wien` | 2.0% | 100.0% | 1.0% | 18 | 18 | 0 |
| `Specific Entity: Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: The King's School Worcester` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: University of Bristol` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Specific Entity: England` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: Grazer Treuhand Steuerberatung GmbH & Partner KG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Rhein Normonkel Manufaktur GMBH` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `Specific Entity: Merkur Treuhand Steuerberatung GmbH` | 1.1% | 100.0% | 0.6% | 10 | 10 | 0 |
| `Specific Entity: Schabetsberger Steuerberatung GmbH` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Specific Entity: UFS Salzburg` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Merkur Steuerberatung GmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Steuerberater Metzler & Adelsberger OG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Bezirkshauptmannschaft Bludenz` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `Specific Entity: ÖBB` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: InnMarine GMBH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Lenfeld/Leys/Sonderegger Rechtsanwälte` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Universität Innsbruck` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific Entity: Raiffeisenbank Karnische Rion Bankstelle St.Stefan` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `Specific Entity: Mag. Ghesla Steuerberater GmbH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: X GmbH` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `Specific Entity: Retail Chains` | 0.9% | 100.0% | 0.5% | 8 | 8 | 0 |
| `Specific Entity: R GmbH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific Entity: Bundesamtes für Soziales und Behindertenwesen` | 1.5% | 100.0% | 0.7% | 13 | 13 | 0 |
| `Specific Entity: FA Wien Variations` | 2.3% | 95.2% | 1.1% | 21 | 20 | 1 |
| `Specific Entity: Finanzamt Consolidated` | 2.9% | 92.9% | 1.5% | 28 | 26 | 2 |
| `Specific Entity: SeneCura Variations` | 1.1% | 90.9% | 0.6% | 11 | 10 | 1 |
| `Specific Entity: Wirtschaftsuniversität Wien` | 2.9% | 89.7% | 1.5% | 29 | 26 | 3 |
| `German Tax Authority Consolidated` | 7.4% | 89.3% | 3.8% | 75 | 67 | 8 |
| `Specific Entity: Bundesministerium` | 1.1% | 83.3% | 0.6% | 12 | 10 | 2 |
| `Specific Entity: Johannes Kepler Universität Linz` | 2.5% | 75.9% | 1.3% | 29 | 22 | 7 |
| `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)` | 5.3% | 75.0% | 2.8% | 64 | 48 | 16 |
| `General Court Names` | 0.3% | 75.0% | 0.2% | 4 | 3 | 1 |
| `Specific Entity: PVA` | 0.6% | 71.4% | 0.3% | 7 | 5 | 2 |
| `Specific Entity: AMS` | 0.2% | 66.7% | 0.1% | 3 | 2 | 1 |
| `Specific Entity: BMF` | 0.8% | 58.3% | 0.4% | 12 | 7 | 5 |
| `Specific Entity: Magistrat der Stadt Wien` | 2.6% | 54.8% | 1.3% | 42 | 23 | 19 |
| `Specific Entity: Frontex` | 1.1% | 52.6% | 0.6% | 19 | 10 | 9 |
| `Specific Entity: Bundesfinanzgericht` | 24.3% | 43.4% | 16.9% | 680 | 295 | 385 |
| `Specific Entity: Verwaltungsgerichtshof` | 18.6% | 42.3% | 11.9% | 492 | 208 | 284 |
| `Specific Entity: King's School` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `Specific Entity: VwGH` | 17.6% | 30.5% | 12.3% | 705 | 215 | 490 |
| `Specific Entity: Verfassungsgerichtshof` | 0.7% | 27.3% | 0.3% | 22 | 6 | 16 |
| `Specific Entity: OECD` | 0.1% | 20.0% | 0.1% | 5 | 1 | 4 |
| `Specific Entity: VfGH` | 0.9% | 18.2% | 0.5% | 44 | 8 | 36 |
| `Specific Entity: UFS` | 0.6% | 17.2% | 0.3% | 29 | 5 | 24 |
| `Specific Entity: WU Acronym` | 0.3% | 15.8% | 0.2% | 19 | 3 | 16 |
| `Specific Entity: Pensionsversicherungsanstalt` | 0.2% | 15.4% | 0.1% | 13 | 2 | 11 |
| `Specific Entity: Amt für Betrugsbekämpfung` | 0.1% | 6.7% | 0.1% | 15 | 1 | 14 |
| `Specific Entity: Bahrdt Digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Wildorftra KI GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bruckmonwil Digital GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Niederösterreichische Vorsorgekasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Raiffeisenbank Mittleres Mostviertel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hempel Heizung GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Süd Nortri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hülsebusch + Breithaupt Versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Enns Werkal GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Logal Gruppe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Trafenfen Automotive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Mur Ververzor Betriebe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Naaß Elektro GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Lexkel Vertrieb KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Kornfelder Recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Füchsl Touristik GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Buhrfeindt Lebensmittel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Finanzen Tradonnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hinklein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Dongartcon-Landwirtschaft GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Monlogtri-Analyse GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Botho Mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Blazickova & Hepprich Energie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Berend Energie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Raiffeisenbank Hippach-Hart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Raiffeisenbank genburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Raiffeisenkasse Retz-Pulkautal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Obernöder+Küsbert Touristik GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Energie Synlexder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Aicher & Partner Steuerberater OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: MittelHeizung Werke AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Traun-Digital KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Mertznich Bau GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Gernot Hirschkorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: ÖBUG Law Firm` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Österreichische Gesellschaft für Europapolitik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BKS Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: FH Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Karl-Franzens- Universität Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Fachhochschule Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: UnterRecycling Services GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: London Film Academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundeskanzleramtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: SVS/SVB` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: PSD Wien Ambulatorium Landstraße` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Sozialversicherungsanstalt der Bauern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Specific Entity: PSD Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Psychiatrie Otto Wagner Spital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundesfinanzgericht (BFG)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Saxinger Chalupsky & Partner Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Imre & Schaffer Rechtsanwälte OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Talwerk Logistik Holding GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bersud Möbel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Unter Heimdorf GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: LG für ZRS Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Paugger Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Landesregierung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: B-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: A-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hausverwaltung-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: LG Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bezirksgericht Silz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Raiffeisenbank Stallhofen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Mittel Unisyn GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Ober Lemostnor AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Vennes Recycling AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Unter Donunisee AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bärs & Walterscheidt Handel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `General Organisation Pattern: Name + Beratung` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Specific Entity: Sozialversicherung Variations` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Specific Entity: BFG, Außenstelle Linz` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Specific Entity: Bundesfinanzgericht, Außenstelle Linz` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Specific Entity: BFG (Außenstelle Linz)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Specific Entity: Missing Known Organizations`

**F1:** 0.153 | **Precision:** 1.000 | **Recall:** 0.083  

**Format:** `regex`  
**Description:**
Matches specific organization names found in training data and failures, including BDO Austria, LeitnerLeitner, Lubomir Merschmeyer, and Betriebsprüfung GmbH.

**Content:**
```
\b(?:Schmeltz\s+Luftfahrt|Dorfcon\-Verlag|Houdek\s+Maschinenbau|Lexdon\s+IT|Roelfsen\s+Versicherung|FA\s+Wien\s+1/23|G\u00f6zc\u00fc\s+Getr\u00e4nke|Lubomir\s+Merschmeyer|BDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.|LeitnerLeitner\s+GmbH\s+Wirtschaftspr\u00fcfer\s+und\s+Steuerberater|Betriebspr\u00fcfung\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.083 | 0.153 | 144 | 144 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 144 | 0 | 1403 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |
| `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` | `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)


Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_17`)


Der Sachverhalt ergibt sich bisherigen Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der Houdek Maschinenbau, Str.Nr.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_18`)


95-002/7970, BV 24:  Das Unternehmen Houdek Maschinenbau  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_21`)


Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.


Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)


Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.


Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Lexdon IT` | `Lexdon IT` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_24`)


zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die Roelfsen Versicherung  durch Übertragung des  gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und  Übernahmsvertrages taxativ angeführten Positionen) erfolgt.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_27`)


Im Wirtschaftsjahr 2007 ist gemäß der beim FA Wien 1/23  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84  Tankstellen erzielt worden.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_28`)


In den Jahren 2011 bis 2013 fand eine Außenprüfung gemäß § 147 BAO durch die  Großbetriebsprüfung (Außenstelle Linz) über die Jahre 2007 und 2008 bei der Houdek Maschinenbau  statt.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lexdon IT` | `Lexdon IT` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_31`)


Der Lexdon IT  als weiterem partiellen  Gesamtrechtsnachfolger wurde ein Körperschaftsteuerbescheid 2007 zugestellt, der einen  Ergebnisanteil von Null mangels Übergang von verlustverursachenden Vermögen auswies.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_32`)


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_33`)


Begründend führte das Finanzamt zusammenfassend aus,  dass die Houdek Maschinenbau  aufgrund der Rechtsform eine nach unternehmensrechtlichen  Vorschriften zur Rechnungslegung verpflichtete Körperschaft im Sinne des § 7 Abs. 3 KStG 1988  3 von 39 Seite 4 von 39

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_45`)


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_49`)


Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %


Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `Specific Entity: FAÖ`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAÖ' (Finanzamt Österreich) as an organization.

**Content:**
```
\bFAÖ\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.024 | 0.046 | 41 | 41 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 41 | 0 | 1514 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_11`)


Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_12`)


Mit Beschwerdevorentscheidungen vom 17.7.2025 wies das FAÖ die Beschwerden sowohl  gegen den Umsatzsteuerbescheid 2022 vom 5.11.2024, als auch jene das Jahr 2023 betreffend  vom 26.5.2025, als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_13`)


Die Bf. richtete daraufhin am 13.8.2025 einen Vorlageantrag an das FAÖ, dies verbunden mit  dem Antrag auf Durchführung einer mündlichen Verhandlung und Entscheidung durch den  Senat.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_14`)


Inhaltlich monierte die Bf. insbesondere, dass rücksichtlich der Bestimmung des § 59  BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde, nämlich dem FAÖ  anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_16`)


Das Verwaltungsgericht forderte sowohl das FAÖ als auch das FAG am 21.10.2025 auf, die  bezughabenden Akten vorzulegen und umfassend zum Vorbringen der Bf. Stellung zu nehmen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_18`)


Das FAÖ gab am selben Tag bekannt, sich der Stellungnahme des FAG  vollinhaltlich anzuschließen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_30`)


Mit Schreiben vom 11.7.2025 wurde die Bf. darüber in Kenntnis gesetzt, dass die  Steuernummer auf das FAÖ übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_31`)


Mit Beschwerdevorentscheidungen je vom 17.7.2025 wies nunmehr das FAÖ die Beschwerden  gegen die Umsatzsteuerbescheide 2022 und 2023 als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_32`)


Die Bf. richtete daraufhin am 13.8.2025 einen Vorlageantrag an das FAÖ, dies verbunden mit  dem Antrag auf Durchführung einer mündlichen Verhandlung und Entscheidung durch den  Senat.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_34`)


Inhaltlich monierte die Bf. -  soweit für die vorerst maßgebliche Rechtsfrage von Relevanz -, dass rücksichtlich der  Bestimmung des § 59 BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde,  nämlich dem FAÖ anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_36`)


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAÖ` | `FAÖ` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_38`)


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAÖ` | `FAÖ` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_45`)


unstrittig ist weiters, dass – nach Erlassung von Beschwerdevorentscheidungen –  am 13.8.2025 ein Vorlageantrag der Bf. beim FAÖ einlangte.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_51`)


Fraglich ist, wie der  Übergang der Zuständigkeit vom FAG an das FAÖ – wie aus der Mitteilung vom 11.7.2025  entnommen werden kann – auf die anhängigen Beschwerdeverfahren wirkt.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_53`)


Daraus folgt sohin, dass zwar die  Zuständigkeit vom FAG auf das FAÖ übergegangen sein mag, das FAG bleibt aber weiterhin für  jene Beschwerdeverfahren zuständig, die bis zum Übergang dieser Zuständigkeit bei ihr  anhängig gemacht wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_55`)


die Änderung der  Zuständigkeit erfolgte jedoch erst zeitlich später, sodass nicht das FAÖ, sondern richtigerweise  das FAG zur Erlassung der Beschwerdevorentscheidungen zuständig gewesen wäre.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_56`)


Nur der Ordnung halber wird an dieser Stelle noch angemerkt, dass aufgrund der nach außen  in Erscheinung tretenden Umstände (ausdrückliche Nennung des FAÖ im Briefkopf, deren  Telefonnummer für das Kundenservice, deren Bankverbindung) es auch offensichtlich ist,  welches Finanzamt die Beschwerdevorentscheidungen erlassen hat und kann hier etwa nicht  mit einem einfachen Schreibfehler iSd § 293 BAO argumentiert werden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

</details>

---

## `Specific Entity: ÖGK`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the acronym 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1700 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist in der vorliegenden Beschwerdesache, ob zu Recht Einkünfte in Höhe von EUR  620,43 von der Österreichischen Gesundheitskasse (im Folgenden: ÖGK) im  Einkommensteuerbescheid 2023 des Beschwerdeführers (im Folgenden: Bf.) berücksichtigt  wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_6`)


Darin  wurden auch Einkünfte von der ÖGK in Höhe von EUR 620,43 berücksichtigt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_15`)


Im Jahr 2023 erhielt der Bf. von der ÖGK eine Erstattung von insgesamt EUR 723,84 an  Beiträgen zur Sozialversicherung (davon entfielen auf die Krankenversicherung EUR 163,53, auf  die Arbeitslosenversicherung EUR 126,77 und auf die Pensionsversicherung EUR 433,54).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_16`)


Diese  Erstattung hatte ihre Wurzel im Jahr 2022, da in diesem Jahr Beiträge über die  Höchstbeitragsgrundlage hinaus an die ÖGK entrichtet wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_17`)


In einem Schreiben der ÖGK  vom 12.5.2023 wurde der Bf. über die Rückerstattung der Beiträge informiert und darauf  aufmerksam gemacht, dass die rückerstatteten Sozialversicherungsbeiträge steuerpflichtig  sind.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_18`)


Am 20.2.2024 wurde dem Finanzamt von der ÖGK ein Lohnzettel für den Bf. und das Jahr 2023  übermittelt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_20`)


Im Einkommensteuerbescheid 2023 des Bf. kamen bei den Einkünften aus nichtselbständiger  Arbeit auch die von der ÖGK rückerstatteten Sozialversicherungsbeiträge in Höhe von EUR  620,43 zum Ansatz.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_23`)


Darüber hinaus enthält das  Schreiben der ÖGK vom 12.5.2023 eine Aufstellung der für die Berechnung relevanten  Versicherungsverhältnisse 2022 und ergibt sich die Sachverhaltsfeststellung auch daraus.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_27`)


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_32`)


Dieses Schreiben der ÖGK über die Erstattung von Beiträgen in Höhe von EUR 723,84 ist im  finanzbehördlichen Abgabeninformationssystem (JVP) hinterlegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_35`)


Aufgrund dieses Schreibens der ÖGK an den Bf. ist für das Bundesfinanzgericht die Grundlage  für den im Jahr 2024 übermittelten Lohnzettel an das Finanzamt (auch dieser ist in der JVP  ersichtlich) und die Berücksichtigung des Betrages von EUR 620,43 im  Einkommensteuerbescheid 2023 des Bf. geklärt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Specific Entity: FAG`

**F1:** 0.026 | **Precision:** 1.000 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAG' (Finanzamt für Großbetriebe) as an organization.

**Content:**
```
\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.013 | 0.026 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 1027 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_5`)


Das FAG erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides  2022 vom 8.9.2023 und verband diese mit dem ebenfalls vom selben Tag datierenden  Sachbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_7`)


Am 5.11.2024 hob das FAG den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § 299 BAO auf und erließ einen neuen Jahresbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_8`)


Weiters hob das FAG am  26.5.2025 den Umsatzsteuerbescheid des Jahres 2023 gemäß § 299 BAO auf und verband  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_10`)


Dagegen wurde von der Bf. am 16.6.2025 Beschwerde, eingebracht beim FAG, erhoben.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_11`)


Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_14`)


Inhaltlich monierte die Bf. insbesondere, dass rücksichtlich der Bestimmung des § 59  BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde, nämlich dem FAÖ  anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_16`)


Das Verwaltungsgericht forderte sowohl das FAÖ als auch das FAG am 21.10.2025 auf, die  bezughabenden Akten vorzulegen und umfassend zum Vorbringen der Bf. Stellung zu nehmen.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_17`)


Daraufhin teilte das FAG am 22.10.2025 mit, dass es den Einwand, wonach die  Beschwerdevorentscheidungen vom 17.7.2025 von der unzuständigen Behörde erlassen  worden seien, teile.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_18`)


Das FAÖ gab am selben Tag bekannt, sich der Stellungnahme des FAG  vollinhaltlich anzuschließen.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_27`)


Alle genannten Bescheide wurden  vom FAG als damals für die Bf. zuständige Behörde erlassen;

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_28`)


die Beschwerden wurden allesamt  beim FAG eingebracht.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_34`)


Inhaltlich monierte die Bf. -  soweit für die vorerst maßgebliche Rechtsfrage von Relevanz -, dass rücksichtlich der  Bestimmung des § 59 BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde,  nämlich dem FAÖ anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_36`)


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |
| `FAG` | `FAG` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_38`)


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |
| `FAG` | `FAG` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_51`)


Fraglich ist, wie der  Übergang der Zuständigkeit vom FAG an das FAÖ – wie aus der Mitteilung vom 11.7.2025  entnommen werden kann – auf die anhängigen Beschwerdeverfahren wirkt.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_53`)


Daraus folgt sohin, dass zwar die  Zuständigkeit vom FAG auf das FAÖ übergegangen sein mag, das FAG bleibt aber weiterhin für  jene Beschwerdeverfahren zuständig, die bis zum Übergang dieser Zuständigkeit bei ihr  anhängig gemacht wurden.


Daraus folgt sohin, dass zwar die  Zuständigkeit vom FAG auf das FAÖ übergegangen sein mag, das FAG bleibt aber weiterhin für  jene Beschwerdeverfahren zuständig, die bis zum Übergang dieser Zuständigkeit bei ihr  anhängig gemacht wurden.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |
| `FAG` | `FAG` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_54`)


Wie aus dem elektronischen Akt unzweifelhaft hervorgeht, waren  die Beschwerden ab dem 5.11.2024 bzw. 26.5.2025 beim FAG anhängig;

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_55`)


die Änderung der  Zuständigkeit erfolgte jedoch erst zeitlich später, sodass nicht das FAÖ, sondern richtigerweise  das FAG zur Erlassung der Beschwerdevorentscheidungen zuständig gewesen wäre.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_61`)


Es wird somit nun das FAG die  Beschwerdevorentscheidungen zu erlassen haben.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

</details>

---

## `Specific Entity: KQPC Versand GMBH`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'KQPC Versand GMBH' specifically.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

## `Specific Entity: Event Sudkraftlex GMBH`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Event Sudkraftlex GMBH' specifically.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1579 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `Specific Entity: X GmbH`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'X GmbH' and 'X-GmbH' specifically to cover both space and hyphen variants found in training data, including variable whitespace.

**Content:**
```
\bX[-\s]+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1451 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_113`)


Streitfrage wie folgt „Strittig ist, ob für Zwecke der Anwendung des § 35 UmgrStG den  abgespaltenen Tankstellen (Teilbetrieben) zurechnende Verluste 2007 von EUR -882.676,16  vorrangig mit Gewinnen 2007 von der X GmbH verbliebenen Tankstellen (Teilbetrieben) in  Höhe von EUR 1.183.053,01 verrechnet werden (so die Mitbeteiligte) oder ob dies nicht der  Fall ist (so das Finanzamt).

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_114`)


In Streit steht also letztlich, weicher Teil des Jahresverlustes 2007  der X GmbH in Anbetracht des § 35 UmgrStG von der X GmbH in den auf das Jahr 2007  folgenden Jahren als Verlustvortrag iSd § 8 Abs. 4 Z 2 KStG 1988 geltend gemacht werden  kann".


In Streit steht also letztlich, weicher Teil des Jahresverlustes 2007  der X GmbH in Anbetracht des § 35 UmgrStG von der X GmbH in den auf das Jahr 2007  folgenden Jahren als Verlustvortrag iSd § 8 Abs. 4 Z 2 KStG 1988 geltend gemacht werden  kann".

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_121`)


Für den Revisionsfall folge daraus: Die X GmbH habe - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen sei.


Für den Revisionsfall folge daraus: Die X GmbH habe - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen sei.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_123`)


Entscheidend sei allerdings, dass im Veranlagungsjahr 2007 die Spaltung noch nicht erfolgt sei  und der gesamte Verlust des Veranlagungsjahres 2007 von 3,632.188,29 EUR durch die X  GmbH erzielt worden sei.

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_124`)


Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39


Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_126`)


Mit dem Spruch des Erkenntnisses werde nämlich nicht  normativ über die Höhe der Verlustvorträge, die vor dem Hintergrund des § 35 UmgrStG der X  GmbH verbleiben, abgesprochen.

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_265`)


In Rz 24  der Entscheidung hält der VwGH ausdrücklich fest, dass „für die Berechnung der  Körperschaftsteuer der X GmbH für das Jahr 2007 im Rahmen der  Körperschaftsteuerveranlagung zur Ermittlung des steuerpflichtigen Einkommens ein  innerbetrieblicher Verlustausgleich vorzunehmen ist [...].

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_268`)


Übersehen werden dabei insbesondere die Ausführungen des VwGH in Rz 25: „Eine andere  Frage ist es, von wem dieser Jahresverlust - in Anbetracht der zum Ablauf des 31. Dezember  2007 vorgenommenen Spaltung des X-GmbH - in den Folgejahren [Herv d Verf] als  Verlustvortrag iSd § 8 Abs 4 KStG 1988 geltend gemacht werden kann."

| Predicted | Gold |
|---|---|
| `X-GmbH` | `X-GmbH` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_430`)


Der VwGH  führte mit Erkenntnis vom 13.9.2018 (VwGH 13.9.2018, Ro 2016/15/0010) aus: „28 Für den  Revisionsfall folgt daraus: Die X GmbH hat - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen ist.


Der VwGH  führte mit Erkenntnis vom 13.9.2018 (VwGH 13.9.2018, Ro 2016/15/0010) aus: „28 Für den  Revisionsfall folgt daraus: Die X GmbH hat - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen ist.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_432`)


29 Entscheidend ist allerdings, dass im Veranlagungsjahr 2007 die Spaltung noch nicht erfolgt  ist und der gesamte Verlust des Veranlagungsjahres 2007 von 3.632.188,29 EUR durch die X  GmbH erzielt worden ist.

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_433`)


30 Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH  der Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels  objektbezogener Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen  Erkenntnis des Bundesfinanzgerichts dargestellten Höhe zusteht, erweist sich der Spruch des  angefochtenen Erkenntnisses nicht als rechtswidrig.


30 Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH  der Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels  objektbezogener Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen  Erkenntnis des Bundesfinanzgerichts dargestellten Höhe zusteht, erweist sich der Spruch des  angefochtenen Erkenntnisses nicht als rechtswidrig.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_434`)


Mit dem Spruch des Erkenntnisses wird  nämlich nicht normativ über die Höhe der Verlustvorträge, die vor dem Hintergrund des § 35  UmgrStG der X GmbH verbleiben, abgesprochen.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_28`)


bis 31.12.2023 Einkünfte aus nichtselbständiger Arbeit von der  X GmbH in Adr AG.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_33`)


Die Entfernung zwischen der Adresse des Arbeitgebers X GmbH in Adr AG und der  österreichischen Wohnadresse Bf-Adr Ö beträgt weniger als 20 Kilometer.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_42`)


Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG und der österreichischen Wohnadresse Bf-Adr Ö und der Zeitdauer der Benutzung  eines Massenbeförderungsmittels gründen sich auf eine vom Bundesfinanzgericht  durchgeführte Berechnung mit dem von Bundesministerium für Finanzen im Internet zur  Verfügung gestellten Pendlerrechner.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

</details>

---

## `Specific Entity: Universität Wien`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches 'Universität Wien' specifically.

**Content:**
```
\bUniversität\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.010 | 0.020 | 18 | 18 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 1658 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `Specific Entity: Bundesamt für Soziales und Behindertenwesen`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its genitive form 'Bundesamts für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamts?\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.015 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 1111 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_38`)


In § 35 Abs. 2 EStG 1988 hat der Gesetzgeber bindend festgelegt, dass die Tatsache der  Behinderung und das Ausmaß der Minderung der Erwerbsfähigkeit (Grad der Behinderung)  durch eine amtliche Bescheinigung der für diese Feststellung zuständigen Stelle - hier das  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice) – nachzuweisen ist.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_49`)


– In allen übrigen Fällen sowie bei Zusammentreffen von   Behinderungen verschiedener Art das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_56`)


Die zuständige Stelle ist im  gegenständlichen Fall das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_59`)


Die Bescheinigung des Bundesamts für Soziales  und Behindertenwesen (Sozialministeriumservice) als gesetzlich ausdrücklich geforderter  Nachweis kann durch die Vorlage von zB haus- oder fachärztlichen Bestätigungen,  Privatgutachten oder Arztbriefen anlässlich eines stationären Krankenhausaufenthaltes nicht  ersetzt werden.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales  und Behindertenwesen` | `Bundesamts für Soziales  und Behindertenwesen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_78`)


Diese  Feststellung ob, ab wann und in welchem Ausmaß eine Behinderung vorliegt, obliegt nur dem  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_18`)


2. Beweiswürdigung  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist dem Finanzamt Österreich vom Bundesamt für Soziales und  Behindertenwesen mit einer Bescheinigung aufgrund eines ärztlichen  Sachverständigengutachtens nachzuweisen (§ 8 Abs. 6 FLAG).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_19`)


Sowohl die Abgabenbehörde als  auch das Bundesfinanzgericht sind an die im Sachverständigengutachten des Bundesamts für  Soziales und Behindertenwesen getroffenen Feststellungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamts für  Soziales und Behindertenwesen` | `Bundesamts für  Soziales und Behindertenwesen` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_20`)


Gutachten des  Bundesamts für Soziales und Behindertenwesen dürfen lediglich auf Schlüssigkeit,  Vollständigkeit und im Fall mehrerer Gutachten auf Widerspruchsfreiheit überprüft werden (zB  VwGH 9.9.2017, 2013/16/0049).

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_21`)


Die Behinderung der Bf seit Juli 1999 ergibt sich ebenso wie deren Ausmaß von 30% aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_22`)


Da sich dieses Gutachten auf sämtliche zum  Zeitpunkt der Gutachtenserstellung vorliegenden Befunde stützt, ist es, was die Frage des  Zeitpunkts des Eintritts der Behinderung und deren Ausmaß anbelangt, das aus Sicht des  Bundesfinanzgerichts glaubwürdigste, weil vollständigste, der insgesamt drei Gutachten des  Bundesamts für Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_26`)


Die Behinderung im Ausmaß von 50% seit Mai 2012 ergibt sich ebenfalls aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_38`)


Die drei Sachverständigengutachten des Bundesamts für Soziales und Behindertenwesen  widersprechen sich bezüglich der Frage, ob die Bf dauerhaft erwerbsunfähig ist.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_47`)


Gutachtens vom 2. Juli 2021 und der damit im Zusammenhang stehenden chefärztlichen  Stellungnahme vom 6. Juli 2021 kann das Bundesfinanzgericht daher dem Schluss der beiden  Gutachten des Bundesamts für Soziales und Behindertenwesen vom 14. Februar 2024 und vom  5. Dezember 2024, die Bf sei (erst) seit Juli 2021 dauerhaft erwerbsunfähig, nicht folgen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

</details>

---

## `Specific Entity: Bundesamtes für Soziales und Behindertenwesen`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Bundesamtes für Soziales und Behindertenwesen' (genitive) and 'Bundesamt für Soziales und Behindertenwesen' (nominative).

**Content:**
```
\bBundesamts?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.015 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 1111 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_38`)


In § 35 Abs. 2 EStG 1988 hat der Gesetzgeber bindend festgelegt, dass die Tatsache der  Behinderung und das Ausmaß der Minderung der Erwerbsfähigkeit (Grad der Behinderung)  durch eine amtliche Bescheinigung der für diese Feststellung zuständigen Stelle - hier das  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice) – nachzuweisen ist.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_49`)


– In allen übrigen Fällen sowie bei Zusammentreffen von   Behinderungen verschiedener Art das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_56`)


Die zuständige Stelle ist im  gegenständlichen Fall das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_59`)


Die Bescheinigung des Bundesamts für Soziales  und Behindertenwesen (Sozialministeriumservice) als gesetzlich ausdrücklich geforderter  Nachweis kann durch die Vorlage von zB haus- oder fachärztlichen Bestätigungen,  Privatgutachten oder Arztbriefen anlässlich eines stationären Krankenhausaufenthaltes nicht  ersetzt werden.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales  und Behindertenwesen` | `Bundesamts für Soziales  und Behindertenwesen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_78`)


Diese  Feststellung ob, ab wann und in welchem Ausmaß eine Behinderung vorliegt, obliegt nur dem  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_18`)


2. Beweiswürdigung  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist dem Finanzamt Österreich vom Bundesamt für Soziales und  Behindertenwesen mit einer Bescheinigung aufgrund eines ärztlichen  Sachverständigengutachtens nachzuweisen (§ 8 Abs. 6 FLAG).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_19`)


Sowohl die Abgabenbehörde als  auch das Bundesfinanzgericht sind an die im Sachverständigengutachten des Bundesamts für  Soziales und Behindertenwesen getroffenen Feststellungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamts für  Soziales und Behindertenwesen` | `Bundesamts für  Soziales und Behindertenwesen` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_20`)


Gutachten des  Bundesamts für Soziales und Behindertenwesen dürfen lediglich auf Schlüssigkeit,  Vollständigkeit und im Fall mehrerer Gutachten auf Widerspruchsfreiheit überprüft werden (zB  VwGH 9.9.2017, 2013/16/0049).

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_21`)


Die Behinderung der Bf seit Juli 1999 ergibt sich ebenso wie deren Ausmaß von 30% aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_22`)


Da sich dieses Gutachten auf sämtliche zum  Zeitpunkt der Gutachtenserstellung vorliegenden Befunde stützt, ist es, was die Frage des  Zeitpunkts des Eintritts der Behinderung und deren Ausmaß anbelangt, das aus Sicht des  Bundesfinanzgerichts glaubwürdigste, weil vollständigste, der insgesamt drei Gutachten des  Bundesamts für Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_26`)


Die Behinderung im Ausmaß von 50% seit Mai 2012 ergibt sich ebenfalls aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_38`)


Die drei Sachverständigengutachten des Bundesamts für Soziales und Behindertenwesen  widersprechen sich bezüglich der Frage, ob die Bf dauerhaft erwerbsunfähig ist.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_47`)


Gutachtens vom 2. Juli 2021 und der damit im Zusammenhang stehenden chefärztlichen  Stellungnahme vom 6. Juli 2021 kann das Bundesfinanzgericht daher dem Schluss der beiden  Gutachten des Bundesamts für Soziales und Behindertenwesen vom 14. Februar 2024 und vom  5. Dezember 2024, die Bf sei (erst) seit Juli 2021 dauerhaft erwerbsunfähig, nicht folgen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Specific Entity: VwGH`

**F1:** 0.176 | **Precision:** 0.305 | **Recall:** 0.123  

**Format:** `regex`  
**Description:**
Matches 'VwGH' standalone or as part of 'Verwaltungsgerichtshof (VwGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verwaltungsgerichtshof(?:es)?(?:\s*\(\s*VwGH\s*\))?|VwGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.305 | 0.123 | 0.176 | 705 | 215 | 490 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 215 | 490 | 1526 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)

**False Positives:**


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_291`)

**False Positives:**


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_294`)

**False Positives:**


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_291`)

**False Positives:**


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_294`)

**False Positives:**


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof  nach Art. 133 Abs. 4 B-VG nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_69`)

**False Positives:**


III. Zulässigkeit einer Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an  den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  4 von 5 Seite 5 von 5

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_71`)

**False Positives:**


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_73`)

**False Positives:**


Die ordentliche  Revision an den Verwaltungsgerichtshof ist demzufolge nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Bundesfinanzgericht`

**F1:** 0.243 | **Precision:** 0.434 | **Recall:** 0.169  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive form 'Bundesfinanzgerichts', including with location suffixes or in genitive contexts.

**Content:**
```
\bBundesfinanzgericht(?:es)?(?:\s*\(\s*BFG\s*\)|,\s+Au\u00dfenstelle|\s+Innsbruck|\s+Linz|\s+Salzburg|\s+Wien|\s+des)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.434 | 0.169 | 0.243 | 680 | 295 | 385 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 295 | 385 | 1448 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_210`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_226`)


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_227`)


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_236`)


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_251`)


Dass diese Zustellung zu Unrecht erfolgt sei, wurde  nicht behauptet und konnte auch durch das Bundesfinanzgericht nicht erkannt werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_279`)


Das  Bundesfinanzgericht hat grundsätzlich auf Grund der zum Zeitpunkt ihrer Entscheidung  gegebenen Sach- und Rechtslage zu entscheiden (vgl. VwGH 24.3.2009, 2006/13/0149).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_288`)


Die Angaben des Bf.  versetzen das Bundesfinanzgericht nicht in die Lage, abschließend eine persönliche Unbilligkeit  feststellen zu können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_210`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_226`)

**False Positives:**


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_227`)

**False Positives:**


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `USA` (country)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_236`)

**False Positives:**


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_251`)

**False Positives:**


Dass diese Zustellung zu Unrecht erfolgt sei, wurde  nicht behauptet und konnte auch durch das Bundesfinanzgericht nicht erkannt werden.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_279`)

**False Positives:**


Das  Bundesfinanzgericht hat grundsätzlich auf Grund der zum Zeitpunkt ihrer Entscheidung  gegebenen Sach- und Rechtslage zu entscheiden (vgl. VwGH 24.3.2009, 2006/13/0149).

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_288`)

**False Positives:**


Die Angaben des Bf.  versetzen das Bundesfinanzgericht nicht in die Lage, abschließend eine persönliche Unbilligkeit  feststellen zu können.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Niklas Bußjann  in der Beschwerdesache ÖkR ÖkR Jonas Sternekicker,  Mühlbach 2, 4851 Fischhamering, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 15. Mai 2025  zu Steuernummer 98-117/5180  ausgefertigten Bescheid betreffend Einkommensteuer für  das Jahr 2024 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Priv.-Doz. Niklas Bußjann` (person)
- `ÖkR ÖkR Jonas Sternekicker` (person)
- `Mühlbach 2, 4851 Fischhamering, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `98-117/5180` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_43`)

**False Positives:**


8. Die belangte Behörde hat die Bescheidbeschwerde mit Bericht vom 23. September 2025  dem Bundesfinanzgericht zur Entscheidung vorgelegt.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Verwaltungsgerichtshof`

**F1:** 0.186 | **Precision:** 0.423 | **Recall:** 0.119  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.119 | 0.186 | 492 | 208 | 284 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 208 | 284 | 1533 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_118`)


Der Verwaltungsgerichtshof hat zum schädlichen und unschädlichen Studienwechsel folgende  Judikatur entwickelt:  Ein Studienwechsel iSd § 17 StudFG liegt vor, wenn der/die Studierende das von ihm/ihr  begonnene und bisher betriebene, aber noch nicht abgeschlossene Studium nicht mehr  fortsetzt und an dessen Stelle ein anderes unter den Geltungsbereich des StudFG fallendes  Studium beginnt (VwGH 26.05.2011, 2011/16/0060).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_146`)


Entgegen der Rechtsansicht des Bf, dass der erste tatsächliche Studienwechsel zum Studium  der biotechnischen Verfahren erfolgt ist, gilt auch der Rückwechsel vom Bachelorstudium  Wirtschaftsrecht auf das Studium Rechtswissenschaften nach der zitierten Judikatur des  Verwaltungsgerichtshofes (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_163`)


Subjektive  Momente, wie Verschulden an der (ursprünglichen oder weiteren) Auszahlung der  Familienleistungen, Gutgläubigkeit des Empfangs der Familienbeihilfe und des  Kinderabsetzbetrags oder die Verwendung der Familienbeihilfe und des Kinderabsetzbetrags,  sind nach ständiger Rechtsprechung des Verwaltungsgerichtshofes für die Verpflichtung zur  Rückerstattung unrechtmäßiger Beihilfenbezüge unerheblich.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof  nach Art. 133 Abs. 4 B-VG nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_69`)

**False Positives:**


III. Zulässigkeit einer Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an  den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  4 von 5 Seite 5 von 5

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_71`)

**False Positives:**


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_73`)

**False Positives:**


Die ordentliche  Revision an den Verwaltungsgerichtshof ist demzufolge nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_74`)

**False Positives:**


Zur außerordentlichen  Revision an den Verwaltungsgerichtshof siehe nachstehende Rechtsbelehrung.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: VfGH`

**F1:** 0.009 | **Precision:** 0.182 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'VfGH' standalone or as part of 'Verfassungsgerichtshof (VfGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verfassungsgerichtshof(?:es)?(?:\s*\(\s*VfGH\s*\))?|VfGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.182 | 0.005 | 0.009 | 44 | 8 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 36 | 1575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `Verfassungsgerichtshof` (organisation)


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_157`)

**False Positives:**


Der VfGH hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_159`)

**False Positives:**


Dem genannten VfGH-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung aus dem Jahr 1984 gab die zuständige FLD der Berufung einer  Gesellschafterin gegen die einheitliche und gesonderte Gewinnfeststellung in der Form statt,  dass die im Erstbescheid bei der Gesellschafterin zur Gänze als Gewinnanteil behandelte  Ablösezahlung mit 2/3 zu aktivieren und auf 6 Jahre verteilt abzuschreiben war.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_162`)

**False Positives:**


Der VfGH bejahte die Anwendbarkeit des Vorfragentatbestandes.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_172`)

**False Positives:**


Der Verfassungsgerichtshof ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein  derartiger Fall, nämlich wenn eine Entscheidung derselben Behörde für einen früheren  Steuerzeitraum, die sich in der rechtlichen Würdigung des Sachverhaltes direkt auf einen  (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt, in gleicher Weise behandelt  werden muss, wie der Fall der Vorfrage;

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_293`)

**False Positives:**


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_295`)

**False Positives:**


Im der  zitierten Entscheidung des Verfassungsgerichtshofes zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher Aktivierung eine beantragte Wiederaufnahme für die Folgejahre  zwecks Berücksichtigung der AfA vorzunehmen ist.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_301`)

**False Positives:**


Erst der Verfassungsgerichtshof kam zu dem  Ergebnis, dass in diesem Fall ein Wiederaufnahmegrund vorliege bzw eine Wiederaufnahme zu  verfügen sei, um ein gleichheitskonformes Ergebnis zu erreichen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_313`)

**False Positives:**


- Weiters wurde vom Verfassungsgerichtshof aufgezeigt, dass eine Nichtwiederaufnahme im  Hinblick auf die Jahre 1975 und 1976 auch dem Grundsatz von Treu und Glauben  widersprechen würde, da sich die Abgabepflichtigen auf die ursprüngliche rechtliche  Beurteilung der Behörde verlassen haben.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_316`)

**False Positives:**


Im Ergebnis zeigt sich, dass eine Erweiterung der Regelung des § 303 BAO auch vom  Verfassungsgerichtshof nur in bestimmten Ausnahmefällen angedacht ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_328`)

**False Positives:**


Dazu ergänzend wird seitens des Finanzamtes zu den Beschwerdeausführungen wie folgt  Stellung genommen:   Wie bereits in der händischen Begründung der Wiederaufnahme vom 29.01.2019 ausgeführt,  kam der VfGH in seiner Entscheidung B 783/89 vom 6.12.1990 zum Schluss, dass auch eine  Wiederaufnahme des Verfahrens in verfassungsgemäßer Interpretation möglich ist und eine  Vorfrage deshalb auch nicht nur "klassisch" zu verstehen ist.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_329`)

**False Positives:**


D.h. durch die Entscheidung des  VfGH wurden die Wiederaufnahmegründe in ihrem Anwendungsbereich de facto erweitert (so  auch Ritz, 6.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_367`)

**False Positives:**


Lt. Ansicht des Finanzamtes liegt damit auch hier  eine weite Auslegung der Wiederaufnahmebestimmung im Sinn der Rechtsprechung des VfGH  vor (verfassungskonforme Interpretation des § 303 Abs. 1 lit c BAO).

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_383`)

**False Positives:**


Die Wiederaufnahme wurde laut Begründung des angefochtenen Bescheides auf die  verfassungskonforme Auslegung des § 303 Abs. 1 lit c BAO - Wiederaufnahmsgrund laut  Erkenntnis des VfGH vom 6.12.1990, B 783/89 (siehe dazu bei Ritz, BAO, 6.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_385`)

**False Positives:**


Die Parallelität zum vom Verfassungsgerichtshof entschiedenen Fall ergibt  sich daraus, dass nach dem gegenüber der Beschwerdeführerin ergangenen und in Rechtskraft  erwachsenen Bescheid vom 7.3.2016 gegenüber (auch) der Beschwerdeführerin eine anders  lautende Gerichtsentscheidung ergangen ist, nach welcher der Bescheid vom 7.3.2016 so nicht  ergehen hätte dürfen, da die vom BFG gelöste, vom Finanzamt aufgrund der Bindungswirkung  dem Bescheid zugrunde gelegte Rechtsfrage, nachträglich höchstgerichtlich anders beurteilt  bzw. entschieden wurde.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_454`)

**False Positives:**


Dazu hat der VfGH in seinem Erkenntnis vom 6.12.1990, B 783/89  klargestellt, dass als Vorfragetatbestand bei der Wiederaufnahme des Verfahrens auch ein  neuer Bescheid derselben Abgabenbehörde in einem anderen Verfahren in Betracht kommen  kann (siehe Ritz, BAO 5, § 303, Tz 41;

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_457`)

**False Positives:**


In diesem Erkenntnis des VfGH war die Frage zu lösen, ob die nachträgliche Änderung der  behördlichen Auffassung zur Frage der Aktivierung oder Nichtaktivierung eines Aufwandes für  ein bestimmtes Veranlagungsjahr zur Wiederaufnahme nachfolgender - bereits rechtskräftiger  - Veranlagungsjahre, in denen der selbe Aufwand (im Hinblick auf seine Aktivierung)  Auswirkungen zeitigte, führen kann.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_458`)

**False Positives:**


Der VfGH hat zugestanden, dass die rechtliche Beurteilung  eines Sachverhaltes für ein früheres Steuerjahr keine Vorfrage im technischen Sinn darstellt  und dass nach der Judikatur des VwGH die Änderung der rechtlichen Qualifikation eines  Sachverhaltes keine Tatsache iSd § 303 Abs 1 lit. b BAO darstellt.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: UFS`

**F1:** 0.006 | **Precision:** 0.172 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat).

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.172 | 0.003 | 0.006 | 29 | 5 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 24 | 1478 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)


85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_141`)


19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)   29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)   16.12.2013 Vorlage an BFG (damals noch UFS)   17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  07.03.2016 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010   07.03.2016 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 (Erhöhung des  Verlustvortrages infolge BFG-Erkenntnis RV/5101064/2013)

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_64`)

**False Positives:**


UFS 27.11.2007, RV/0087-L/07).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_78`)

**False Positives:**


UFS 18.2.2010, RV/0098-L/06;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_82`)

**False Positives:**


BFG 9.1.2019, RV/3100898/2018),   die Höhe des durch die verspätete Einreichung der Abgabenerklärung erzielten  finanziellen Vorteils (vgl UFS 21.10.2003, RV/0234-G/02, FJ 2004, 77;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_86`)

**False Positives:**


BMF, AÖF 2006/128, Abschn 5; UFS 24.8.2009, RV/0430-L/04;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_93`)

**False Positives:**


UFS 27.11.2007, RV/0087-L/07;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_26`)

**False Positives:**


Von einer Liebhabereitätigkeit kann ja wohl nur dann gesprochen werden, wenn jemand,  dessen Hauptberuf sich von seinem Hobby, dem er aus besonderer Neigung nachgeht (siehe  UFS 27.11.2003, RV/0509-L/02), unterscheidet, und dieses Hobby zu steuerlich unbeachtlichen  Gesamtverlusten führt.

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_30`)

**False Positives:**


Der Zeitpunkt, an dem die Daten in den elektronischen Verfügungsbereich des Empfängers  gelangt sind, ist bei FinanzOnline der Zeitpunkt der Einbringung der Daten in die Databox, zu  der der Empfänger Zugang hat (UFS 22.7.2013, RV/0002-F/13;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_41`)

**False Positives:**


UFS  22.7.2013, RV/0002-F/13;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) ( sent_id: `findok-manually-annotated_TRAIN/148648.1_62`)

**False Positives:**


Ein Zimmer bei den Eltern ist nicht als Haushalt anzusehen  (UFS 4.12.08, RV/0662-L/07).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_55`)

**False Positives:**


Wird zu einem späteren Zeitpunkt festgestellt, dass Beiträge nicht oder in geringerer Höhe zu  leisten gewesen wären, ändert dies nichts an ihrem ursprünglichen Charakter (UFS 15.4.2013,  RV/0220-W/13;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)

**False Positives:**


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

FP: `UFS` (organisation)

**✅ Gold Entities:**
- `WU` (organisation)
- `JKU` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)

**False Positives:**


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)

**False Positives:**


UFS 19.10.2010, RV/0180-L/10).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)

**False Positives:**


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)

**False Positives:**


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

FP: `UFS` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_164`)

**False Positives:**


vgl. auch UFS  16.02.2007, RV/0189-G/06).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)

**False Positives:**


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

FP: `UFS` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Magistrat der Stadt Wien`

**F1:** 0.026 | **Precision:** 0.548 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien', 'Magistrates der Stadt Wien', and variations including 'MA 67' or 'Magistratsabteilung 67'.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s+(?:MA\s+\d+|Magistratsabteilung\s+\d+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.548 | 0.013 | 0.026 | 42 | 23 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 19 | 1584 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Emanuela Deider, Astätt 60, 4682 Wilding, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 26. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 29. August 2025, Zahl: MA67/MA-GZ/2025 zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_15`)


Wegen Verletzung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 verhängte der Magistrat der Stadt Wien über den Bf. eine Geldstrafe in  Höhe € 75,00 (Ersatzfreiheitsstrafe 17 Stunden).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_30`)


Die vom Magistrat der Stadt Wien verhängte Geldstrafe sei im Hinblick auf die  Strafzumessungsgründe und den bis zu € 365,00 reichenden Strafsatz, den Unrechtsgehalt der  Tat und das Verschulden, selbst bei ungünstigen wirtschaftlichen Verhältnissen, durchaus  angemessen und keineswegs zu hoch.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_35`)


Über die Beschwerde wurde erwogen:  Der Bf. hat in seiner Beschwerde gegen das Straferkenntnis des Magistrates der Stadt Wien  vom 29. August 2025, Zahl: MA67/MA-GZ/2025, lediglich die Höhe der verhängten Geldstrafe  bekämpft und die angelastete Verwaltungsübertretung nicht in Abrede gestellt, sodass der  Schuldspruch des Straferkenntnisses in Rechtskraft erwachsen ist.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_110`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Diego Strzeletzki` (person)
- `Zwerggasse 116, 8961 Steg, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_8`)

**False Positives:**


Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte die Firma Firma, AdrFirma, als  Zulassungsbesitzerin des in Rede stehenden Fahrzeuges mit Schreiben vom 17. Juni 2025, GZ.  MA67/GZ/2025, zur Lenkerauskunft gemäß § 2 Wiener Parkometergesetz 2006 binnen einer  Frist von zwei Wochen ab Zustellung des Schreibens auf (Lenkererhebung).

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Emanuela Deider, Astätt 60, 4682 Wilding, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 26. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 29. August 2025, Zahl: MA67/MA-GZ/2025 zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

FP: `Magistrates der Stadt  Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Karoline Windsteig` (person)
- `Emanuela Deider` (person)
- `Astätt 60, 4682 Wilding, Österreich` (address)
- `Wien` (city)
- `Wien` (city)
- `Wien` (city)
- `Wien` (city)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_13`)

**False Positives:**


In der Folge lastete der Magistrat der Stadt Wien, MA 67, nach durchgeführter Lenkererhebung  (Erteilung der Lenkerauskunft durch Zulassungsbesitzerin per E-Mail am 10. Juli 2025) mit  Strafverfügung vom 11. Juli 2025, zugestellt am 17. Juli 2025, GZ MA67/MA-GZ/2025, dem  Beschwerdeführer (kurz Bf.) an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen W-Kennz. (A) am 07. Mai 2025 um 11:59 Uhr in der gebührenpflichtigen  Kurzparkzone in 1050 Wien, Bacherplatz gegenüber 14, abgestellt, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `1050 Wien, Bacherplatz` (address)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Felix Grenzheuser  über die Beschwerde des PhD Ing. Theobald Reuschel,  Schloss Straße 184, 3371 Köchling, Österreich  vom 24. April 2025 gegen die Vollstreckungsverfügung des Magistrates der  Stadt Wien, Magistratsabteilung 6, vom 31. März 2025, Zahl: MA67/GZ/2024 in  Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl.

FP: `Magistrates der  Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Felix Grenzheuser` (person)
- `PhD Ing. Theobald Reuschel` (person)
- `Schloss Straße 184, 3371 Köchling, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_5`)

**False Positives:**


I. Verfahrensgang  Mit Strafverfügung vom 03. Jänner 2025, zugestellt am 14. Februar 2025, GZ. MA67/GZ/2024  lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Beschwerdeführer (kurz Bf.)  an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen GU-405 NY  (A) am 06. November 2024 um 12:21 Uhr in der gebührenpflichtigen Kurzparkzone in 1020  Wien, Rustenschacherallee vor Baum 1009 abgestellt, ohne für seine Kennzeichnung mit einem  für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `GU-405 NY` (vehicle_license)
- `1020  Wien, Rustenschacherallee` (address)

</details>

---

## `Specific Entity: WU Acronym`

**F1:** 0.003 | **Precision:** 0.158 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the standalone acronym 'WU' for Wirtschaftsuniversität Wien.

**Content:**
```
\bWU\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.158 | 0.002 | 0.003 | 19 | 3 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 16 | 638 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_41`)


Siehe Internetseite JKU und WU  Karriereaussichten!

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)

**False Positives:**


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)

**False Positives:**


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)

**False Positives:**


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_29`)

**False Positives:**


Die von der belangten Behörde angeforderten Angaben der WU Wien wurden mit diesem  Schreiben jedoch nicht vorgelegt.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)

**False Positives:**


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `Linz` (city)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)

**False Positives:**


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)

**False Positives:**


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler  Universität Linz` (organisation)
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)

**False Positives:**


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_54`)

**False Positives:**


Aufgrund des Arbeitsauftrages wurde dann ermittelt und es stellte sich ein Studienwechsel mit  WS 19/20 heraus, vom Studium UJ033 561 Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der WU Wien auf UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der JKU Linz.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_61`)

**False Positives:**


Weiters wurde jedoch von  den abgelegten 42 ECTS an der WU Wien, nur 24 ECTS an der JKU Linz angerechnet.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_65`)

**False Positives:**


Im gegenständlichen Fall  wurde das erste Studium an der WU Wien nach 4 Semester gewechselt, also nach dem jeweils  dritten inskribierten Semester und daher liegt ein schädlicher Studienwechsel vor.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_73`)

**False Positives:**


Von den an der WU Wien absolvierten  Lehrveranstaltungen mit 42 ECTS-Punkten wurden 24 ECTS-Punkte an der JKU Linz  angerechnet.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_98`)

**False Positives:**


Die belangte Behörde bringt vor, dass von den abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der JKU Linz angerechnet wurden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `Specific Entity: Verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 0.273 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofes'.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.273 | 0.003 | 0.007 | 22 | 6 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 16 | 1577 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149708.1`) ( sent_id: `findok-manually-annotated_TRAIN/149708.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149379.1`) ( sent_id: `findok-manually-annotated_TRAIN/149379.1_65`)


Eine Einschränkung finden diese Überlegungen insoweit, als nach der Rechtsprechung des  Verfassungsgerichtshofes (vgl VfGH 05.03.1979, B 175/76), welcher sich der  Verwaltungsgerichtshof (vgl VwGH 13.02.1991, 90/13/0161;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_172`)

**False Positives:**


Der Verfassungsgerichtshof ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein  derartiger Fall, nämlich wenn eine Entscheidung derselben Behörde für einen früheren  Steuerzeitraum, die sich in der rechtlichen Würdigung des Sachverhaltes direkt auf einen  (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt, in gleicher Weise behandelt  werden muss, wie der Fall der Vorfrage;

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_293`)

**False Positives:**


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_295`)

**False Positives:**


Im der  zitierten Entscheidung des Verfassungsgerichtshofes zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher Aktivierung eine beantragte Wiederaufnahme für die Folgejahre  zwecks Berücksichtigung der AfA vorzunehmen ist.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_301`)

**False Positives:**


Erst der Verfassungsgerichtshof kam zu dem  Ergebnis, dass in diesem Fall ein Wiederaufnahmegrund vorliege bzw eine Wiederaufnahme zu  verfügen sei, um ein gleichheitskonformes Ergebnis zu erreichen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_313`)

**False Positives:**


- Weiters wurde vom Verfassungsgerichtshof aufgezeigt, dass eine Nichtwiederaufnahme im  Hinblick auf die Jahre 1975 und 1976 auch dem Grundsatz von Treu und Glauben  widersprechen würde, da sich die Abgabepflichtigen auf die ursprüngliche rechtliche  Beurteilung der Behörde verlassen haben.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_316`)

**False Positives:**


Im Ergebnis zeigt sich, dass eine Erweiterung der Regelung des § 303 BAO auch vom  Verfassungsgerichtshof nur in bestimmten Ausnahmefällen angedacht ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_385`)

**False Positives:**


Die Parallelität zum vom Verfassungsgerichtshof entschiedenen Fall ergibt  sich daraus, dass nach dem gegenüber der Beschwerdeführerin ergangenen und in Rechtskraft  erwachsenen Bescheid vom 7.3.2016 gegenüber (auch) der Beschwerdeführerin eine anders  lautende Gerichtsentscheidung ergangen ist, nach welcher der Bescheid vom 7.3.2016 so nicht  ergehen hätte dürfen, da die vom BFG gelöste, vom Finanzamt aufgrund der Bindungswirkung  dem Bescheid zugrunde gelegte Rechtsfrage, nachträglich höchstgerichtlich anders beurteilt  bzw. entschieden wurde.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_51`)

**False Positives:**


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_50`)

**False Positives:**


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**
- `COFAG` (organisation)

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_53`)

**False Positives:**


Wenn sich die Bf. dadurch benachteiligt fühlt, dass der Prüfungstermin ohne ihre  Einflussmöglichkeit bereits für Mai 2022 angesetzt wurde, ist ihr Folgendes entgegenzuhalten:  Der Verfassungsgerichtshof hat wiederholt zum Ausdruck gebracht, dass der rechtspolitische  Gestaltungsspielraum des Gesetzgebers bei staatlichen Beihilfen, selbst wenn sie hoheitlich  gewährt werden (zur Familienbeihilfe vgl.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_65`)

**False Positives:**


Eine Verfassungswidrigkeit, die es gebieten würde, die Norm zunächst bis zu einer  Entscheidung des Verfassungsgerichtshofes unangewendet zu lassen, kann das  Bundesfinanzgericht nicht erkennen.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_33`)

**False Positives:**


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)`

**F1:** 0.053 | **Precision:** 0.750 | **Recall:** 0.028  

**Format:** `regex`  
**Description:**
Matches the full name 'Schweizerischen Unfallversicherungsanstalt (SUVA)' and the abbreviation 'SUVA' as a standalone organization. Prioritizes the full name match.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)\b|\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.028 | 0.053 | 64 | 48 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 48 | 16 | 937 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_11`)


Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_12`)


Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_13`)


3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_14`)


4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_18`)


5.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer mit Beschwerde und – nach Ergehen abweisender Beschwer- devorentscheidungen – mit Vorlageantrag wandte.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_19`)


6.  Mit am 11. Februar 2022 elektronisch eingereichtem Anbringen gab die steuerliche Vertre- tung unter Anschluss einer E-Mail des Steueramtes des Kantons Luzern, wonach die Schweiz  nach Art. 19 DBA-Schweiz das Recht habe, die von der SUVA (öffentlich-rechtlich) ausbezahlte  Rente zu besteuern, bekannt, dass sein Antrag auf Rückerstattung der Schweizer Quellensteuer  in der Schweiz abgewiesen worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_21`)


von der SUVA bezogenen Rente wie auch die Abzugsfähigkeit der von der Schweiz einbehal- tenen Quellensteuer und gab der Beschwerde gegen den Einkommensteuerbescheid 2015 ge- samthaft gesehen im Umfang der Beschwerdevorentscheidung (Höhe der Schweizer Invaliden- renten, Nichtberücksichtigung einer Pensionskassenleistung) teilweise Folge.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_22`)


Die einzig die  Frage der Steuerpflicht der von der SUVA ausbezahlten Invalidenrente betreffenden Beschwer- den gegen den Einkommensteuerbescheid 2016 und die Einkommensteuervorauszahlungsbe- scheide 2017 sowie 2018 und Folgejahre wurden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_34`)


Es werde dazu auf die Verfügung der  SUVA vom 8. Jänner 2024 sowie auf die Untersuchungsberichte des Kantonsspitals St. Gallen  und weitere ärztliche Untersuchungsberichte verwiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_35`)


Die Unterlagen, welche großteils an  die SUVA gerichtet seien, dürften dabei auch die Grundlage für die Einschätzung der festge- stellten Invalidität darstellen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_39`)


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_45`)


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_50`)


Dem- nach wurde die Minderung der Erwerbsfähigkeit im Hinblick auf die im Einzelnen angeführten  unfallkausalen Diagnosen und Verletzungsfolgen sowie die Beurteilung des Integritätsschadens  nach Gutachten der SUVA mit ärztlicher Abschlussuntersuchung am 22. Juli 2013 mit 30 % be- wertet.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_60`)


Betreffend das Jahr 2015 wurde von der SUVA Quellensteuer in Höhe von 5.623,80 CHF einbe- halten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_8`)

**False Positives:**


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)

**False Positives:**


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)

**False Positives:**


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_44`)

**False Positives:**


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_58`)

**False Positives:**


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_63`)

**False Positives:**


Rechtliche Beurteilung  2.1. SUVA-Invalidenrente  Gemäß § 3 Abs. 1 Z 4 lit. c EStG 1988 sind Geldleistungen aus einer gesetzlichen Unfallversor- gung sowie dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen ge- setzlichen Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspricht,  steuerbefreit.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Amt für Betrugsbekämpfung`

**F1:** 0.001 | **Precision:** 0.067 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmt(?:es)?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.067 | 0.001 | 0.001 | 15 | 1 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 14 | 1263 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_22`)


Die belangte Behörde verweigere die Buchung der UVAs und NOVA- Meldungen mit dem Hinweis, dass man auf eine Aussage des Amtes für Betrugsbekämpfung  (ABB) warte.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_2`)

**False Positives:**


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_3`)

**False Positives:**


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_10`)

**False Positives:**


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)

**False Positives:**


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amt für Betrugsbekämpfung` (organisation)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_89`)

**False Positives:**


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_140`)

**False Positives:**


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Zollamt Österreich` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_2`)

**False Positives:**


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_3`)

**False Positives:**


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_10`)

**False Positives:**


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)

**False Positives:**


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amt für Betrugsbekämpfung` (organisation)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_89`)

**False Positives:**


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_140`)

**False Positives:**


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Zollamt Österreich` (organisation)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Specific Entity: Bahrdt Digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bahrdt Digital' specifically, handling context like 'Fa. Bahrdt Digital'.

**Content:**
```
(?:Fa\.?\s+)?Bahrdt\s+Digital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Wildorftra KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wildorftra KI GMBH' specifically.

**Content:**
```
\bWildorftra\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bruckmonwil Digital GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bruckmonwil Digital GMBH' specifically.

**Content:**
```
\bBruckmonwil\s+Digital\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Niederösterreichische Vorsorgekasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Niederösterreichische Vorsorgekasse' specifically.

**Content:**
```
\bNiederösterreichische\s+Vorsorgekasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Raiffeisenbank Mittleres Mostviertel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Mittleres Mostviertel' specifically.

**Content:**
```
\bRaiffeisenbank\s+Mittleres\s+Mostviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Hempel Heizung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hempel Heizung GMBH' specifically.

**Content:**
```
\bHempel\s+Heizung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Süd Nortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Süd Nortri' specifically to prevent 'Co' or other fragments from being matched as organizations.

**Content:**
```
\bSüd\s+Nortri\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Hülsebusch + Breithaupt Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hülsebusch + Breithaupt Versicherung' specifically to ensure the full name is captured before 'GmbH & Co KG'.

**Content:**
```
\bHülsebusch\s+\+\s+Breithaupt\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Enns Werkal GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Enns Werkal GMBH' specifically to ensure correct extraction in legal contexts.

**Content:**
```
\bEnns\s+Werkal\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Logal Gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Logal Gruppe' specifically.

**Content:**
```
\bLogal\s+Gruppe\b
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

<details>
<summary>📋 All Rules</summary>

## `Specific Entity: Bundesfinanzgericht`

**F1:** 0.243 | **Precision:** 0.434 | **Recall:** 0.169  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive form 'Bundesfinanzgerichts', including with location suffixes or in genitive contexts.

**Content:**
```
\bBundesfinanzgericht(?:es)?(?:\s*\(\s*BFG\s*\)|,\s+Au\u00dfenstelle|\s+Innsbruck|\s+Linz|\s+Salzburg|\s+Wien|\s+des)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.434 | 0.169 | 0.243 | 680 | 295 | 385 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 295 | 385 | 1448 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_210`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_226`)


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_227`)


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_236`)


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_251`)


Dass diese Zustellung zu Unrecht erfolgt sei, wurde  nicht behauptet und konnte auch durch das Bundesfinanzgericht nicht erkannt werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_279`)


Das  Bundesfinanzgericht hat grundsätzlich auf Grund der zum Zeitpunkt ihrer Entscheidung  gegebenen Sach- und Rechtslage zu entscheiden (vgl. VwGH 24.3.2009, 2006/13/0149).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_288`)


Die Angaben des Bf.  versetzen das Bundesfinanzgericht nicht in die Lage, abschließend eine persönliche Unbilligkeit  feststellen zu können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_210`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_226`)

**False Positives:**


Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_227`)

**False Positives:**


Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `USA` (country)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_236`)

**False Positives:**


Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_251`)

**False Positives:**


Dass diese Zustellung zu Unrecht erfolgt sei, wurde  nicht behauptet und konnte auch durch das Bundesfinanzgericht nicht erkannt werden.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_279`)

**False Positives:**


Das  Bundesfinanzgericht hat grundsätzlich auf Grund der zum Zeitpunkt ihrer Entscheidung  gegebenen Sach- und Rechtslage zu entscheiden (vgl. VwGH 24.3.2009, 2006/13/0149).

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_288`)

**False Positives:**


Die Angaben des Bf.  versetzen das Bundesfinanzgericht nicht in die Lage, abschließend eine persönliche Unbilligkeit  feststellen zu können.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Niklas Bußjann  in der Beschwerdesache ÖkR ÖkR Jonas Sternekicker,  Mühlbach 2, 4851 Fischhamering, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 15. Mai 2025  zu Steuernummer 98-117/5180  ausgefertigten Bescheid betreffend Einkommensteuer für  das Jahr 2024 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Priv.-Doz. Niklas Bußjann` (person)
- `ÖkR ÖkR Jonas Sternekicker` (person)
- `Mühlbach 2, 4851 Fischhamering, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `98-117/5180` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_43`)

**False Positives:**


8. Die belangte Behörde hat die Bescheidbeschwerde mit Bericht vom 23. September 2025  dem Bundesfinanzgericht zur Entscheidung vorgelegt.

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Verwaltungsgerichtshof`

**F1:** 0.186 | **Precision:** 0.423 | **Recall:** 0.119  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.119 | 0.186 | 492 | 208 | 284 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 208 | 284 | 1533 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_118`)


Der Verwaltungsgerichtshof hat zum schädlichen und unschädlichen Studienwechsel folgende  Judikatur entwickelt:  Ein Studienwechsel iSd § 17 StudFG liegt vor, wenn der/die Studierende das von ihm/ihr  begonnene und bisher betriebene, aber noch nicht abgeschlossene Studium nicht mehr  fortsetzt und an dessen Stelle ein anderes unter den Geltungsbereich des StudFG fallendes  Studium beginnt (VwGH 26.05.2011, 2011/16/0060).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_146`)


Entgegen der Rechtsansicht des Bf, dass der erste tatsächliche Studienwechsel zum Studium  der biotechnischen Verfahren erfolgt ist, gilt auch der Rückwechsel vom Bachelorstudium  Wirtschaftsrecht auf das Studium Rechtswissenschaften nach der zitierten Judikatur des  Verwaltungsgerichtshofes (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_163`)


Subjektive  Momente, wie Verschulden an der (ursprünglichen oder weiteren) Auszahlung der  Familienleistungen, Gutgläubigkeit des Empfangs der Familienbeihilfe und des  Kinderabsetzbetrags oder die Verwendung der Familienbeihilfe und des Kinderabsetzbetrags,  sind nach ständiger Rechtsprechung des Verwaltungsgerichtshofes für die Verpflichtung zur  Rückerstattung unrechtmäßiger Beihilfenbezüge unerheblich.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof  nach Art. 133 Abs. 4 B-VG nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_69`)

**False Positives:**


III. Zulässigkeit einer Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an  den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  4 von 5 Seite 5 von 5

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_71`)

**False Positives:**


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_73`)

**False Positives:**


Die ordentliche  Revision an den Verwaltungsgerichtshof ist demzufolge nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_74`)

**False Positives:**


Zur außerordentlichen  Revision an den Verwaltungsgerichtshof siehe nachstehende Rechtsbelehrung.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: VwGH`

**F1:** 0.176 | **Precision:** 0.305 | **Recall:** 0.123  

**Format:** `regex`  
**Description:**
Matches 'VwGH' standalone or as part of 'Verwaltungsgerichtshof (VwGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verwaltungsgerichtshof(?:es)?(?:\s*\(\s*VwGH\s*\))?|VwGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.305 | 0.123 | 0.176 | 705 | 215 | 490 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 215 | 490 | 1526 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)

**False Positives:**


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_291`)

**False Positives:**


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_294`)

**False Positives:**


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_291`)

**False Positives:**


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_294`)

**False Positives:**


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof  nach Art. 133 Abs. 4 B-VG nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_69`)

**False Positives:**


III. Zulässigkeit einer Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an  den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  4 von 5 Seite 5 von 5

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_71`)

**False Positives:**


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_73`)

**False Positives:**


Die ordentliche  Revision an den Verwaltungsgerichtshof ist demzufolge nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Missing Known Organizations`

**F1:** 0.153 | **Precision:** 1.000 | **Recall:** 0.083  

**Format:** `regex`  
**Description:**
Matches specific organization names found in training data and failures, including BDO Austria, LeitnerLeitner, Lubomir Merschmeyer, and Betriebsprüfung GmbH.

**Content:**
```
\b(?:Schmeltz\s+Luftfahrt|Dorfcon\-Verlag|Houdek\s+Maschinenbau|Lexdon\s+IT|Roelfsen\s+Versicherung|FA\s+Wien\s+1/23|G\u00f6zc\u00fc\s+Getr\u00e4nke|Lubomir\s+Merschmeyer|BDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.|LeitnerLeitner\s+GmbH\s+Wirtschaftspr\u00fcfer\s+und\s+Steuerberater|Betriebspr\u00fcfung\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.083 | 0.153 | 144 | 144 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 144 | 0 | 1403 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |
| `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` | `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)


Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_17`)


Der Sachverhalt ergibt sich bisherigen Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der Houdek Maschinenbau, Str.Nr.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_18`)


95-002/7970, BV 24:  Das Unternehmen Houdek Maschinenbau  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_21`)


Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.


Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)


Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.


Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Lexdon IT` | `Lexdon IT` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_24`)


zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die Roelfsen Versicherung  durch Übertragung des  gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und  Übernahmsvertrages taxativ angeführten Positionen) erfolgt.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_27`)


Im Wirtschaftsjahr 2007 ist gemäß der beim FA Wien 1/23  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84  Tankstellen erzielt worden.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_28`)


In den Jahren 2011 bis 2013 fand eine Außenprüfung gemäß § 147 BAO durch die  Großbetriebsprüfung (Außenstelle Linz) über die Jahre 2007 und 2008 bei der Houdek Maschinenbau  statt.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lexdon IT` | `Lexdon IT` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_31`)


Der Lexdon IT  als weiterem partiellen  Gesamtrechtsnachfolger wurde ein Körperschaftsteuerbescheid 2007 zugestellt, der einen  Ergebnisanteil von Null mangels Übergang von verlustverursachenden Vermögen auswies.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_32`)


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_33`)


Begründend führte das Finanzamt zusammenfassend aus,  dass die Houdek Maschinenbau  aufgrund der Rechtsform eine nach unternehmensrechtlichen  Vorschriften zur Rechnungslegung verpflichtete Körperschaft im Sinne des § 7 Abs. 3 KStG 1988  3 von 39 Seite 4 von 39

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_45`)


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_49`)


Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %


Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `German Tax Authority Consolidated`

**F1:** 0.074 | **Precision:** 0.893 | **Recall:** 0.038  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' or 'FA' followed by known specific location patterns, excluding 'Österreich' as a standalone location.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Spittal\s+Villach|Graz-Stadt|Graz-\s+Stadt|Linz|Kirchdorf\s+Perg\s+Steyr|Wien\s+\d+(?:/\d+)*|Steiermark\s+Mitte|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Gmunden\s+V\u00f6cklabruck|Purkersdorf|Landeck\s+Reutte|Braunau\s+Ried\s+Sch\u00e4rding|Waldviertel|Salzburg-Stadt|Salzburg-Land|Oststeiermark|Innsbruck|Amstetten\s+Melk\s+Scheibbs|Nieder\u00f6sterreich\s+Mitte|Klosterneuburg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Baden\s+M\u00f6dling|Freistadt\s+Rohrbach\s+Urfahr|Judenburg\s+Liezen|Grieskirchen\s+Wels|Tirol\s+Ost|Neunkirchen\s+Wr\.?\s+Neustadt|Hollabrunn\s+Korneuburg\s+Tulln|Neunkirchen\s+(?:Wr\.?\s+|Wiener\s+)Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.893 | 0.038 | 0.074 | 75 | 67 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 67 | 8 | 1676 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Innsbruck` | `Finanzamtes  Innsbruck` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker,  Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend  Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_3`)


über die Beschwerden vom 29. März 2019 gegen den Bescheid des Finanzamt Wien 1/23  vom 29. Jänner  2019 betreffend Wiederaufnahme § 303 BAO /  KSt 2010 Steuernummer 85-900/3590  zu  Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_27`)


Im Wirtschaftsjahr 2007 ist gemäß der beim FA Wien 1/23  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84  Tankstellen erzielt worden.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_75`)


Das BFG hat der Beschwerde stattgegeben (Entscheidung vom 27.01.2016, GZ  RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des FA Wien 1/23  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung (als partiellen Gesamtrechtsnachfolger der Houdek Maschinenbau)  abgeändert.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_102`)


Unmittelbar nachfolgend hat das BFG die Amtsrevision des Finanzamt Wien 1/23 (samt Veranlagungsakten  sowie Auszügen aus dem Arbeitsbogen der Betriebsprüfung) dem VwGH unter der Zahl Ro  2016/15/0010 zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_111`)


Mittels VwGH-Entscheidung vom 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die  Amtsrevision des Finanzamt Wien 1/23  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_129`)


Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim  Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Wien 1/23  am 07.03.2016 das  Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO  wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da  11 von 39 Seite 12 von 39

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_135`)


Begründend  wurde deshalb durch das Finanzamt Wien 1/23  im Sachbescheid Feststellungsbescheid Gruppenmitglied  2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ  RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Roelfsen Versicherung  als RNF der  Houdek Maschinenbau  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR  1.047.673,40 ergibt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_137`)


Die BFG- Entscheidung RV/5101064/2013 vom 27.01.2016 für das Jahr 2007 (Rechtsvorgänger) wurde  seitens des Finanzamt Wien 1/23  mittels Amtsrevision bekämpft.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_142`)


Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der  Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des  Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann,  wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum  Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_150`)


Die Wiederaufnahme des Verfahrens wird seitens des Finanzamt Wien 1/23  auf den Vorfragetatbestand  gern.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_197`)


Gemäß § 282  BAO war das Finanzamt Wien 1/23  verpflichtet, die Rechtsanschauung des BFG unverzüglich mit den ihr zu  Gebote stehenden rechtlichen Mitteln umzusetzen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_204`)


Damit hat das FA Wien 1/23  in seinem Bescheid vom 07.03.2016 die Vorfrage gemäß der  Rechtsanschauung in der BFG-Entscheidung beurteilt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

</details>

---

## `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)`

**F1:** 0.053 | **Precision:** 0.750 | **Recall:** 0.028  

**Format:** `regex`  
**Description:**
Matches the full name 'Schweizerischen Unfallversicherungsanstalt (SUVA)' and the abbreviation 'SUVA' as a standalone organization. Prioritizes the full name match.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)\b|\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.028 | 0.053 | 64 | 48 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 48 | 16 | 937 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_11`)


Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_12`)


Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_13`)


3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_14`)


4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_18`)


5.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer mit Beschwerde und – nach Ergehen abweisender Beschwer- devorentscheidungen – mit Vorlageantrag wandte.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_19`)


6.  Mit am 11. Februar 2022 elektronisch eingereichtem Anbringen gab die steuerliche Vertre- tung unter Anschluss einer E-Mail des Steueramtes des Kantons Luzern, wonach die Schweiz  nach Art. 19 DBA-Schweiz das Recht habe, die von der SUVA (öffentlich-rechtlich) ausbezahlte  Rente zu besteuern, bekannt, dass sein Antrag auf Rückerstattung der Schweizer Quellensteuer  in der Schweiz abgewiesen worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_21`)


von der SUVA bezogenen Rente wie auch die Abzugsfähigkeit der von der Schweiz einbehal- tenen Quellensteuer und gab der Beschwerde gegen den Einkommensteuerbescheid 2015 ge- samthaft gesehen im Umfang der Beschwerdevorentscheidung (Höhe der Schweizer Invaliden- renten, Nichtberücksichtigung einer Pensionskassenleistung) teilweise Folge.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_22`)


Die einzig die  Frage der Steuerpflicht der von der SUVA ausbezahlten Invalidenrente betreffenden Beschwer- den gegen den Einkommensteuerbescheid 2016 und die Einkommensteuervorauszahlungsbe- scheide 2017 sowie 2018 und Folgejahre wurden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_34`)


Es werde dazu auf die Verfügung der  SUVA vom 8. Jänner 2024 sowie auf die Untersuchungsberichte des Kantonsspitals St. Gallen  und weitere ärztliche Untersuchungsberichte verwiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_35`)


Die Unterlagen, welche großteils an  die SUVA gerichtet seien, dürften dabei auch die Grundlage für die Einschätzung der festge- stellten Invalidität darstellen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_39`)


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_45`)


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_50`)


Dem- nach wurde die Minderung der Erwerbsfähigkeit im Hinblick auf die im Einzelnen angeführten  unfallkausalen Diagnosen und Verletzungsfolgen sowie die Beurteilung des Integritätsschadens  nach Gutachten der SUVA mit ärztlicher Abschlussuntersuchung am 22. Juli 2013 mit 30 % be- wertet.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_60`)


Betreffend das Jahr 2015 wurde von der SUVA Quellensteuer in Höhe von 5.623,80 CHF einbe- halten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_8`)

**False Positives:**


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)

**False Positives:**


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)

**False Positives:**


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_44`)

**False Positives:**


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_58`)

**False Positives:**


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_63`)

**False Positives:**


Rechtliche Beurteilung  2.1. SUVA-Invalidenrente  Gemäß § 3 Abs. 1 Z 4 lit. c EStG 1988 sind Geldleistungen aus einer gesetzlichen Unfallversor- gung sowie dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen ge- setzlichen Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspricht,  steuerbefreit.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: FAÖ`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAÖ' (Finanzamt Österreich) as an organization.

**Content:**
```
\bFAÖ\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.024 | 0.046 | 41 | 41 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 41 | 0 | 1514 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_11`)


Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_12`)


Mit Beschwerdevorentscheidungen vom 17.7.2025 wies das FAÖ die Beschwerden sowohl  gegen den Umsatzsteuerbescheid 2022 vom 5.11.2024, als auch jene das Jahr 2023 betreffend  vom 26.5.2025, als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_13`)


Die Bf. richtete daraufhin am 13.8.2025 einen Vorlageantrag an das FAÖ, dies verbunden mit  dem Antrag auf Durchführung einer mündlichen Verhandlung und Entscheidung durch den  Senat.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_14`)


Inhaltlich monierte die Bf. insbesondere, dass rücksichtlich der Bestimmung des § 59  BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde, nämlich dem FAÖ  anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_16`)


Das Verwaltungsgericht forderte sowohl das FAÖ als auch das FAG am 21.10.2025 auf, die  bezughabenden Akten vorzulegen und umfassend zum Vorbringen der Bf. Stellung zu nehmen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_18`)


Das FAÖ gab am selben Tag bekannt, sich der Stellungnahme des FAG  vollinhaltlich anzuschließen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_30`)


Mit Schreiben vom 11.7.2025 wurde die Bf. darüber in Kenntnis gesetzt, dass die  Steuernummer auf das FAÖ übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_31`)


Mit Beschwerdevorentscheidungen je vom 17.7.2025 wies nunmehr das FAÖ die Beschwerden  gegen die Umsatzsteuerbescheide 2022 und 2023 als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_32`)


Die Bf. richtete daraufhin am 13.8.2025 einen Vorlageantrag an das FAÖ, dies verbunden mit  dem Antrag auf Durchführung einer mündlichen Verhandlung und Entscheidung durch den  Senat.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_34`)


Inhaltlich monierte die Bf. -  soweit für die vorerst maßgebliche Rechtsfrage von Relevanz -, dass rücksichtlich der  Bestimmung des § 59 BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde,  nämlich dem FAÖ anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_36`)


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAÖ` | `FAÖ` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_38`)


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAÖ` | `FAÖ` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_45`)


unstrittig ist weiters, dass – nach Erlassung von Beschwerdevorentscheidungen –  am 13.8.2025 ein Vorlageantrag der Bf. beim FAÖ einlangte.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_51`)


Fraglich ist, wie der  Übergang der Zuständigkeit vom FAG an das FAÖ – wie aus der Mitteilung vom 11.7.2025  entnommen werden kann – auf die anhängigen Beschwerdeverfahren wirkt.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_53`)


Daraus folgt sohin, dass zwar die  Zuständigkeit vom FAG auf das FAÖ übergegangen sein mag, das FAG bleibt aber weiterhin für  jene Beschwerdeverfahren zuständig, die bis zum Übergang dieser Zuständigkeit bei ihr  anhängig gemacht wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_55`)


die Änderung der  Zuständigkeit erfolgte jedoch erst zeitlich später, sodass nicht das FAÖ, sondern richtigerweise  das FAG zur Erlassung der Beschwerdevorentscheidungen zuständig gewesen wäre.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_56`)


Nur der Ordnung halber wird an dieser Stelle noch angemerkt, dass aufgrund der nach außen  in Erscheinung tretenden Umstände (ausdrückliche Nennung des FAÖ im Briefkopf, deren  Telefonnummer für das Kundenservice, deren Bankverbindung) es auch offensichtlich ist,  welches Finanzamt die Beschwerdevorentscheidungen erlassen hat und kann hier etwa nicht  mit einem einfachen Schreibfehler iSd § 293 BAO argumentiert werden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

</details>

---

## `Specific Entity: ÖGK`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the acronym 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1700 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist in der vorliegenden Beschwerdesache, ob zu Recht Einkünfte in Höhe von EUR  620,43 von der Österreichischen Gesundheitskasse (im Folgenden: ÖGK) im  Einkommensteuerbescheid 2023 des Beschwerdeführers (im Folgenden: Bf.) berücksichtigt  wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_6`)


Darin  wurden auch Einkünfte von der ÖGK in Höhe von EUR 620,43 berücksichtigt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_15`)


Im Jahr 2023 erhielt der Bf. von der ÖGK eine Erstattung von insgesamt EUR 723,84 an  Beiträgen zur Sozialversicherung (davon entfielen auf die Krankenversicherung EUR 163,53, auf  die Arbeitslosenversicherung EUR 126,77 und auf die Pensionsversicherung EUR 433,54).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_16`)


Diese  Erstattung hatte ihre Wurzel im Jahr 2022, da in diesem Jahr Beiträge über die  Höchstbeitragsgrundlage hinaus an die ÖGK entrichtet wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_17`)


In einem Schreiben der ÖGK  vom 12.5.2023 wurde der Bf. über die Rückerstattung der Beiträge informiert und darauf  aufmerksam gemacht, dass die rückerstatteten Sozialversicherungsbeiträge steuerpflichtig  sind.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_18`)


Am 20.2.2024 wurde dem Finanzamt von der ÖGK ein Lohnzettel für den Bf. und das Jahr 2023  übermittelt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_20`)


Im Einkommensteuerbescheid 2023 des Bf. kamen bei den Einkünften aus nichtselbständiger  Arbeit auch die von der ÖGK rückerstatteten Sozialversicherungsbeiträge in Höhe von EUR  620,43 zum Ansatz.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_23`)


Darüber hinaus enthält das  Schreiben der ÖGK vom 12.5.2023 eine Aufstellung der für die Berechnung relevanten  Versicherungsverhältnisse 2022 und ergibt sich die Sachverhaltsfeststellung auch daraus.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_27`)


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_32`)


Dieses Schreiben der ÖGK über die Erstattung von Beiträgen in Höhe von EUR 723,84 ist im  finanzbehördlichen Abgabeninformationssystem (JVP) hinterlegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_35`)


Aufgrund dieses Schreibens der ÖGK an den Bf. ist für das Bundesfinanzgericht die Grundlage  für den im Jahr 2024 übermittelten Lohnzettel an das Finanzamt (auch dieser ist in der JVP  ersichtlich) und die Berücksichtigung des Betrages von EUR 620,43 im  Einkommensteuerbescheid 2023 des Bf. geklärt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Specific Entity: Finanzamt Consolidated`

**F1:** 0.029 | **Precision:** 0.929 | **Recall:** 0.015  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' or 'FA' followed by known location patterns, simplified and consolidated.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Spittal\s+Villach|Graz-Stadt|Linz|Kirchdorf\s+Perg\s+Steyr|Wien\s+\d+/\d+(?:/\d+)*\s+Klosterneuburg|Steiermark\s+Mitte|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Gmunden\s+V\u00f6cklabruck|Purkersdorf|Landeck\s+Reutte|Braunau\s+Ried\s+Sch\u00e4rding|Waldviertel|Salzburg-Stadt|Salzburg-Land|Oststeiermark|Innsbruck|Amstetten\s+Melk\s+Scheibbs|Nieder\u00f6sterreich\s+Mitte|Klosterneuburg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Baden\s+M\u00f6dling|Freistadt\s+Rohrbach\s+Urfahr|Judenburg\s+Liezen|Grieskirchen\s+Wels|Tirol\s+Ost|Oststeiermark|Neunkirchen\s+Wr\.?\s+Neustadt|Hollabrunn\s+Korneuburg\s+Tulln|Wien\s+\d+/\d+/\d+/\d+/\d+\s+Schwechat\s+Gerasdorf|Hollabrunn\s+Korneuburg\s+Tulln|Neunkirchen\s+(?:Wr\.?\s+|Wiener\s+)Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.929 | 0.015 | 0.029 | 28 | 26 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 2 | 1717 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Innsbruck` | `Finanzamtes  Innsbruck` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Corvin Diebald, Pitzelstätten 4, 2490 Ebenfurth, Österreich, vertreten durch Dr. Ronald Rödler, Lagerstraße 5/1/20, 2460  Bruck/Leitha über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 11. September 2019  betreffend Aussetzung gemäß § 212a BAO zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Neunkirchen Wr. Neustadt` | `Finanzamtes  Neunkirchen Wr. Neustadt` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Ferdinand Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt  Österreich) vom 31. Oktober 2017 betreffend Festsetzung eines Verspätungszuschlages  betreffend Einkommensteuer 2015 und 2016 und Umsatzsteuer 2015 und 2016,  Steuernummer 86-167/7419  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde des Marion Voits, Kasparekgasse 1, 4981 Fraham, Österreich, vom 19. Oktober 2022 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 10. Oktober 2022 betreffend Pfändung einer Geldforderung 2022 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Braunau Ried Schärding` | `Finanzamt Braunau Ried Schärding` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_40`)


Am 11.11.2022  ging der gepfändete Betrag in Höhe von EUR 4.681,64 am Konto des FA Braunau Ried Schärding  ein und ist am  Abgabenkonto des Beschwerdeführers verbucht.

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Alois Ahl  in der Beschwerdesache Romana van Straaten, MBA,  Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich, vertreten durch Dr. Anna Schlosser-Péter, Kurrentgasse 6/3, 1010  Wien, über die Beschwerden vom 23. März 2015 gegen die Bescheide des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich) vom 17. März 2015  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer  38-795/8528, zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf` | `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/138410.1`) ( sent_id: `findok-manually-annotated_TRAIN/138410.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Prof.in Klara Dolejsch, vertreten durch die Prof.in Tamara Simanek, über die Beschwerde vom 2.  November 2020 gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr  zuständig: Finanzamt Österreich) vom 9. September 2020 betreffend Abweisung des Antrags  auf Wiedereinsetzung in den vorigen Stand gemäß § 308 BAO zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149316.1`) ( sent_id: `findok-manually-annotated_TRAIN/149316.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Siegbert Höweltewes  in der Beschwerdesache Xenia Lukoszek,  Nußbaumallee 23, 9556 Sörg, Österreich, über die Beschwerde vom 22. Dezember 2017 gegen die Bescheide des  Finanzamt Innsbruck  vom 5. Dezember 2017 betreffend Festsetzung der   Normverbrauchsabgabe für April 2014 (4.338,82 €) und Kraftfahrzeugsteuer für die  Zeiträume 4 - 12/2014 (608,26 €) und 1 - 9/2015 (684,29 €) sowie    Normverbrauchsabgabe für September 2015 (11.193,28 €) und Kraftfahrzeugsteuer für  die Zeiträume 10 - 12/2015 (574,60 €), 1 - 12/2016 (2.298,38) und 1 - 9/2017 (1.723,79  €)   Normverbrauchsabgabe für Oktober 2017 (20.414,12 €) und Kraftfahrzeugsteuer für die  Zeiträume 10 - 12/2017 (240 €), 1 - 12/2018 (960 €) und 1 - 8/2019 (640 €),  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Innsbruck` | `Finanzamt Innsbruck` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149892.1`) ( sent_id: `findok-manually-annotated_TRAIN/149892.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Louisa Kastan  in der Beschwerdesache des  Annette Lieschka, Würzberg 6, 3073 Mayerhöfen, Österreich, über die Beschwerde 25. September 2025 gegen die Bescheide  gemäß §§ 15 und 16 COFAG-NoAG des Finanzamt Klosterneuburg  6. August 2025 betreffend Rückerstattung  zum Fördervertrag Vorschuss auf den Fixkostenzuschuss 800.000 iRd Ausfallsbonus 01/2021,  Rückerstattung zum Fördervertrag Vorschuss auf den Fixkostenzuschuss 800.000 iRd  Ausfallsbonus 12/2020, Rückerstattung zum Fördervertrag Ausfallsbonus III 12/2021,  Rückerstattung zum Fördervertrag Ausfallsbonus III 11/2021, Rückerstattung zum  Fördervertrag Ausfallsbonus II 09/2021, Rückerstattung zum Fördervertrag Ausfallsbonus II  08/2021, Rückerstattung zum Fördervertrag Ausfallsbonus II 07/2021, Rückerstattung zum  Fördervertrag Ausfallsbonus 06/2021, Rückerstattung zum Fördervertrag Ausfallsbonus  05/2021, Rückerstattung zum Fördervertrag Ausfallsbonus 04/2021, Rückerstattung zum  Fördervertrag Ausfallsbonus 01/2021, Rückerstattung zum Fördervertrag Ausfallsbonus  12/2020, Rückerstattung zum Fördervertrag Ausfallsbonus 11/2020 und Verzinsung der  Rückerstattung, allesamt zu Steuernummer 65-634/0503, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Klosterneuburg` | `Finanzamt Klosterneuburg` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Elmar Neimayer  in der Beschwerdesache Viola Siebenhühner, LLB,  Jokischberg 11, 3571 Maiersch, Österreich, über die Beschwerde vom 14. Dezember 2010 gegen die jeweils am   8. Oktober 2010 ausgefertigten Bescheide des Finanzamtes Landeck Reutte betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2006 bis 2008 (Steuernummer 063/3127 )zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Landeck Reutte` | `Finanzamtes Landeck Reutte` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_78`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt    Vorausgegangenes Verfahren:  Am 4. Februar 2020 hatte das Finanzamt Waldviertel folgenden Bescheid an die Bf. erlassen:   Abweisungsbescheid   Ihr Antrag vom 16.9.2019 auf Familienbeihilfe wird abgewiesen für:   5 von 10 Seite 6 von 10

| Predicted | Gold |
|---|---|
| `Finanzamt Waldviertel` | `Finanzamt Waldviertel` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_88`)


Schreiben der steuerlichen Vertretung der Bf. vom 14. Juni 2021:   Mit Abweisungsbescheid vom 04.02.2020 des FA Waldviertel wurde Familienbeihilfe für die  das Kind … (Nachname die Bf.) (VNR … 05 00) für den Zeitraum September 2019 bis Februar  2020 (ist der Zeitpunkt der Erlassung des Bescheides) abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_90`)

**False Positives:**


Für den Zeitraum März 2020 bis April 2021 (14 Monate) liegt noch keine Entscheidung des  Finanzamtes Waldviertel über die Gewährung von Familienbeihilfe vor.

FP: `Finanzamtes Waldviertel` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Wirtschaftsuniversität Wien`

**F1:** 0.029 | **Precision:** 0.897 | **Recall:** 0.015  

**Format:** `regex`  
**Description:**
Matches 'Wirtschaftsuniversität Wien' and its abbreviation 'WU Wien', including the optional '(WU)' suffix.

**Content:**
```
\b(?:Wirtschaftsuniversit\u00e4t\s+Wien(?:\s*\(\s*WU\s*\))?|WU\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.897 | 0.015 | 0.029 | 29 | 26 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 3 | 1649 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_47`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_74`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_135`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_47`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_74`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_135`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `WU  Wien` | `WU  Wien` |

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_29`)


Die von der belangten Behörde angeforderten Angaben der WU Wien wurden mit diesem  Schreiben jedoch nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `WU  Wien` | `WU  Wien` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_54`)


Aufgrund des Arbeitsauftrages wurde dann ermittelt und es stellte sich ein Studienwechsel mit  WS 19/20 heraus, vom Studium UJ033 561 Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der WU Wien auf UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der JKU Linz.

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `Wirtschaftsuniversität Wien` (organisation)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `WU Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

</details>

---

## `Specific Entity: FAG`

**F1:** 0.026 | **Precision:** 1.000 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAG' (Finanzamt für Großbetriebe) as an organization.

**Content:**
```
\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.013 | 0.026 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 1027 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_5`)


Das FAG erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides  2022 vom 8.9.2023 und verband diese mit dem ebenfalls vom selben Tag datierenden  Sachbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_7`)


Am 5.11.2024 hob das FAG den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § 299 BAO auf und erließ einen neuen Jahresbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_8`)


Weiters hob das FAG am  26.5.2025 den Umsatzsteuerbescheid des Jahres 2023 gemäß § 299 BAO auf und verband  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_10`)


Dagegen wurde von der Bf. am 16.6.2025 Beschwerde, eingebracht beim FAG, erhoben.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_11`)


Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_14`)


Inhaltlich monierte die Bf. insbesondere, dass rücksichtlich der Bestimmung des § 59  BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde, nämlich dem FAÖ  anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_16`)


Das Verwaltungsgericht forderte sowohl das FAÖ als auch das FAG am 21.10.2025 auf, die  bezughabenden Akten vorzulegen und umfassend zum Vorbringen der Bf. Stellung zu nehmen.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_17`)


Daraufhin teilte das FAG am 22.10.2025 mit, dass es den Einwand, wonach die  Beschwerdevorentscheidungen vom 17.7.2025 von der unzuständigen Behörde erlassen  worden seien, teile.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_18`)


Das FAÖ gab am selben Tag bekannt, sich der Stellungnahme des FAG  vollinhaltlich anzuschließen.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_27`)


Alle genannten Bescheide wurden  vom FAG als damals für die Bf. zuständige Behörde erlassen;

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_28`)


die Beschwerden wurden allesamt  beim FAG eingebracht.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_34`)


Inhaltlich monierte die Bf. -  soweit für die vorerst maßgebliche Rechtsfrage von Relevanz -, dass rücksichtlich der  Bestimmung des § 59 BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde,  nämlich dem FAÖ anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_36`)


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.


Sowohl das FAG als auch das FAÖ teilten in der Folge die Rechtsansicht der Bf., wonach die  Beschwerdevorentscheidungen vom 17.7.2025 nicht vom FAÖ, sondern vom FAG hätten  erlassen werden müssen.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |
| `FAG` | `FAG` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_38`)


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).


Im Übrigen ist er – auch was die  Frage der Zuständigkeiten zwischen dem FAG und dem FAÖ anlangt – unstrittig (vgl. dazu  insbesondere die Schreiben des FAG und des FAÖ vom 22.10.2025).

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |
| `FAG` | `FAG` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_51`)


Fraglich ist, wie der  Übergang der Zuständigkeit vom FAG an das FAÖ – wie aus der Mitteilung vom 11.7.2025  entnommen werden kann – auf die anhängigen Beschwerdeverfahren wirkt.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_53`)


Daraus folgt sohin, dass zwar die  Zuständigkeit vom FAG auf das FAÖ übergegangen sein mag, das FAG bleibt aber weiterhin für  jene Beschwerdeverfahren zuständig, die bis zum Übergang dieser Zuständigkeit bei ihr  anhängig gemacht wurden.


Daraus folgt sohin, dass zwar die  Zuständigkeit vom FAG auf das FAÖ übergegangen sein mag, das FAG bleibt aber weiterhin für  jene Beschwerdeverfahren zuständig, die bis zum Übergang dieser Zuständigkeit bei ihr  anhängig gemacht wurden.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |
| `FAG` | `FAG` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_54`)


Wie aus dem elektronischen Akt unzweifelhaft hervorgeht, waren  die Beschwerden ab dem 5.11.2024 bzw. 26.5.2025 beim FAG anhängig;

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_55`)


die Änderung der  Zuständigkeit erfolgte jedoch erst zeitlich später, sodass nicht das FAÖ, sondern richtigerweise  das FAG zur Erlassung der Beschwerdevorentscheidungen zuständig gewesen wäre.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_61`)


Es wird somit nun das FAG die  Beschwerdevorentscheidungen zu erlassen haben.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

</details>

---

## `Specific Entity: Magistrat der Stadt Wien`

**F1:** 0.026 | **Precision:** 0.548 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien', 'Magistrates der Stadt Wien', and variations including 'MA 67' or 'Magistratsabteilung 67'.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s+(?:MA\s+\d+|Magistratsabteilung\s+\d+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.548 | 0.013 | 0.026 | 42 | 23 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 19 | 1584 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Emanuela Deider, Astätt 60, 4682 Wilding, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 26. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 29. August 2025, Zahl: MA67/MA-GZ/2025 zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_15`)


Wegen Verletzung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 verhängte der Magistrat der Stadt Wien über den Bf. eine Geldstrafe in  Höhe € 75,00 (Ersatzfreiheitsstrafe 17 Stunden).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_30`)


Die vom Magistrat der Stadt Wien verhängte Geldstrafe sei im Hinblick auf die  Strafzumessungsgründe und den bis zu € 365,00 reichenden Strafsatz, den Unrechtsgehalt der  Tat und das Verschulden, selbst bei ungünstigen wirtschaftlichen Verhältnissen, durchaus  angemessen und keineswegs zu hoch.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_35`)


Über die Beschwerde wurde erwogen:  Der Bf. hat in seiner Beschwerde gegen das Straferkenntnis des Magistrates der Stadt Wien  vom 29. August 2025, Zahl: MA67/MA-GZ/2025, lediglich die Höhe der verhängten Geldstrafe  bekämpft und die angelastete Verwaltungsübertretung nicht in Abrede gestellt, sodass der  Schuldspruch des Straferkenntnisses in Rechtskraft erwachsen ist.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_110`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Diego Strzeletzki` (person)
- `Zwerggasse 116, 8961 Steg, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_8`)

**False Positives:**


Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte die Firma Firma, AdrFirma, als  Zulassungsbesitzerin des in Rede stehenden Fahrzeuges mit Schreiben vom 17. Juni 2025, GZ.  MA67/GZ/2025, zur Lenkerauskunft gemäß § 2 Wiener Parkometergesetz 2006 binnen einer  Frist von zwei Wochen ab Zustellung des Schreibens auf (Lenkererhebung).

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Emanuela Deider, Astätt 60, 4682 Wilding, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 26. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 29. August 2025, Zahl: MA67/MA-GZ/2025 zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

FP: `Magistrates der Stadt  Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Karoline Windsteig` (person)
- `Emanuela Deider` (person)
- `Astätt 60, 4682 Wilding, Österreich` (address)
- `Wien` (city)
- `Wien` (city)
- `Wien` (city)
- `Wien` (city)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_13`)

**False Positives:**


In der Folge lastete der Magistrat der Stadt Wien, MA 67, nach durchgeführter Lenkererhebung  (Erteilung der Lenkerauskunft durch Zulassungsbesitzerin per E-Mail am 10. Juli 2025) mit  Strafverfügung vom 11. Juli 2025, zugestellt am 17. Juli 2025, GZ MA67/MA-GZ/2025, dem  Beschwerdeführer (kurz Bf.) an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen W-Kennz. (A) am 07. Mai 2025 um 11:59 Uhr in der gebührenpflichtigen  Kurzparkzone in 1050 Wien, Bacherplatz gegenüber 14, abgestellt, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `1050 Wien, Bacherplatz` (address)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Felix Grenzheuser  über die Beschwerde des PhD Ing. Theobald Reuschel,  Schloss Straße 184, 3371 Köchling, Österreich  vom 24. April 2025 gegen die Vollstreckungsverfügung des Magistrates der  Stadt Wien, Magistratsabteilung 6, vom 31. März 2025, Zahl: MA67/GZ/2024 in  Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl.

FP: `Magistrates der  Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Felix Grenzheuser` (person)
- `PhD Ing. Theobald Reuschel` (person)
- `Schloss Straße 184, 3371 Köchling, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_5`)

**False Positives:**


I. Verfahrensgang  Mit Strafverfügung vom 03. Jänner 2025, zugestellt am 14. Februar 2025, GZ. MA67/GZ/2024  lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Beschwerdeführer (kurz Bf.)  an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen GU-405 NY  (A) am 06. November 2024 um 12:21 Uhr in der gebührenpflichtigen Kurzparkzone in 1020  Wien, Rustenschacherallee vor Baum 1009 abgestellt, ohne für seine Kennzeichnung mit einem  für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `GU-405 NY` (vehicle_license)
- `1020  Wien, Rustenschacherallee` (address)

</details>

---

## `Specific Entity: Johannes Kepler Universität Linz`

**F1:** 0.025 | **Precision:** 0.759 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches 'Johannes Kepler Universität Linz' and its abbreviation 'JKU Linz' or 'JKU', including the optional '(JKU)' suffix.

**Content:**
```
\b(?:Johannes\s+Kepler\s+Universit\u00e4t\s+Linz(?:\s*\(\s*JKU\s*\))?|JKU\s+Linz|JKU)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.759 | 0.013 | 0.025 | 29 | 22 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 22 | 7 | 621 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |
| `JKU Linz` | `JKU Linz` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)


 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_41`)


Siehe Internetseite JKU und WU  Karriereaussichten!

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `Johannes Kepler  Universität Linz` | `Johannes Kepler  Universität Linz` |
| `JKU` | `JKU` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_54`)


Aufgrund des Arbeitsauftrages wurde dann ermittelt und es stellte sich ein Studienwechsel mit  WS 19/20 heraus, vom Studium UJ033 561 Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der WU Wien auf UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der JKU Linz.

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_60`)


Im Dezember 2021 langte dann noch eine Bestätigung der JKU  Linz ein, die die beiden Studien „grundsätzlich gleichwertig“ ansah.

| Predicted | Gold |
|---|---|
| `JKU  Linz` | `JKU  Linz` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_61`)


Weiters wurde jedoch von  den abgelegten 42 ECTS an der WU Wien, nur 24 ECTS an der JKU Linz angerechnet.

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_73`)


Von den an der WU Wien absolvierten  Lehrveranstaltungen mit 42 ECTS-Punkten wurden 24 ECTS-Punkte an der JKU Linz  angerechnet.

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_74`)


Weiters absolvierte die Tochter der Bf. an der JKU Linz Lehrveranstaltungen mit  31 ECTS-Punkten (ohne Berücksichtigung von Anrechnungen).

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `Johannes Kepler Universität Linz` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `Johannes Kepler Universität Linz` (organisation)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_97`)

**False Positives:**


JKU-Curriculum § 5 Abs. 3; Datum der Abfrage: Approbationsdatum dieser  Entscheidung).

FP: `JKU` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_98`)

**False Positives:**


Die belangte Behörde bringt vor, dass von den abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der JKU Linz angerechnet wurden.

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `Specific Entity: KQPC Versand GMBH`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'KQPC Versand GMBH' specifically.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

## `Specific Entity: Event Sudkraftlex GMBH`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Event Sudkraftlex GMBH' specifically.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1579 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `Specific Entity: X GmbH`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'X GmbH' and 'X-GmbH' specifically to cover both space and hyphen variants found in training data, including variable whitespace.

**Content:**
```
\bX[-\s]+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1451 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_113`)


Streitfrage wie folgt „Strittig ist, ob für Zwecke der Anwendung des § 35 UmgrStG den  abgespaltenen Tankstellen (Teilbetrieben) zurechnende Verluste 2007 von EUR -882.676,16  vorrangig mit Gewinnen 2007 von der X GmbH verbliebenen Tankstellen (Teilbetrieben) in  Höhe von EUR 1.183.053,01 verrechnet werden (so die Mitbeteiligte) oder ob dies nicht der  Fall ist (so das Finanzamt).

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_114`)


In Streit steht also letztlich, weicher Teil des Jahresverlustes 2007  der X GmbH in Anbetracht des § 35 UmgrStG von der X GmbH in den auf das Jahr 2007  folgenden Jahren als Verlustvortrag iSd § 8 Abs. 4 Z 2 KStG 1988 geltend gemacht werden  kann".


In Streit steht also letztlich, weicher Teil des Jahresverlustes 2007  der X GmbH in Anbetracht des § 35 UmgrStG von der X GmbH in den auf das Jahr 2007  folgenden Jahren als Verlustvortrag iSd § 8 Abs. 4 Z 2 KStG 1988 geltend gemacht werden  kann".

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_121`)


Für den Revisionsfall folge daraus: Die X GmbH habe - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen sei.


Für den Revisionsfall folge daraus: Die X GmbH habe - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen sei.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_123`)


Entscheidend sei allerdings, dass im Veranlagungsjahr 2007 die Spaltung noch nicht erfolgt sei  und der gesamte Verlust des Veranlagungsjahres 2007 von 3,632.188,29 EUR durch die X  GmbH erzielt worden sei.

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_124`)


Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39


Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_126`)


Mit dem Spruch des Erkenntnisses werde nämlich nicht  normativ über die Höhe der Verlustvorträge, die vor dem Hintergrund des § 35 UmgrStG der X  GmbH verbleiben, abgesprochen.

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_265`)


In Rz 24  der Entscheidung hält der VwGH ausdrücklich fest, dass „für die Berechnung der  Körperschaftsteuer der X GmbH für das Jahr 2007 im Rahmen der  Körperschaftsteuerveranlagung zur Ermittlung des steuerpflichtigen Einkommens ein  innerbetrieblicher Verlustausgleich vorzunehmen ist [...].

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_268`)


Übersehen werden dabei insbesondere die Ausführungen des VwGH in Rz 25: „Eine andere  Frage ist es, von wem dieser Jahresverlust - in Anbetracht der zum Ablauf des 31. Dezember  2007 vorgenommenen Spaltung des X-GmbH - in den Folgejahren [Herv d Verf] als  Verlustvortrag iSd § 8 Abs 4 KStG 1988 geltend gemacht werden kann."

| Predicted | Gold |
|---|---|
| `X-GmbH` | `X-GmbH` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_430`)


Der VwGH  führte mit Erkenntnis vom 13.9.2018 (VwGH 13.9.2018, Ro 2016/15/0010) aus: „28 Für den  Revisionsfall folgt daraus: Die X GmbH hat - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen ist.


Der VwGH  führte mit Erkenntnis vom 13.9.2018 (VwGH 13.9.2018, Ro 2016/15/0010) aus: „28 Für den  Revisionsfall folgt daraus: Die X GmbH hat - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen ist.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_432`)


29 Entscheidend ist allerdings, dass im Veranlagungsjahr 2007 die Spaltung noch nicht erfolgt  ist und der gesamte Verlust des Veranlagungsjahres 2007 von 3.632.188,29 EUR durch die X  GmbH erzielt worden ist.

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_433`)


30 Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH  der Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels  objektbezogener Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen  Erkenntnis des Bundesfinanzgerichts dargestellten Höhe zusteht, erweist sich der Spruch des  angefochtenen Erkenntnisses nicht als rechtswidrig.


30 Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH  der Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels  objektbezogener Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen  Erkenntnis des Bundesfinanzgerichts dargestellten Höhe zusteht, erweist sich der Spruch des  angefochtenen Erkenntnisses nicht als rechtswidrig.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_434`)


Mit dem Spruch des Erkenntnisses wird  nämlich nicht normativ über die Höhe der Verlustvorträge, die vor dem Hintergrund des § 35  UmgrStG der X GmbH verbleiben, abgesprochen.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_28`)


bis 31.12.2023 Einkünfte aus nichtselbständiger Arbeit von der  X GmbH in Adr AG.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_33`)


Die Entfernung zwischen der Adresse des Arbeitgebers X GmbH in Adr AG und der  österreichischen Wohnadresse Bf-Adr Ö beträgt weniger als 20 Kilometer.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_42`)


Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG und der österreichischen Wohnadresse Bf-Adr Ö und der Zeitdauer der Benutzung  eines Massenbeförderungsmittels gründen sich auf eine vom Bundesfinanzgericht  durchgeführte Berechnung mit dem von Bundesministerium für Finanzen im Internet zur  Verfügung gestellten Pendlerrechner.

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

</details>

---

## `Specific Entity: FA Wien Variations`

**F1:** 0.023 | **Precision:** 0.952 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'FA Wien' followed by various number patterns (e.g., 1/23, 2/20/21/22, etc.) to capture abbreviated tax authority forms.

**Content:**
```
\bFA\s+Wien\s+\d+(?:/\d+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.952 | 0.011 | 0.023 | 21 | 20 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 1 | 1500 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_27`)


Im Wirtschaftsjahr 2007 ist gemäß der beim FA Wien 1/23  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84  Tankstellen erzielt worden.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_75`)


Das BFG hat der Beschwerde stattgegeben (Entscheidung vom 27.01.2016, GZ  RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des FA Wien 1/23  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung (als partiellen Gesamtrechtsnachfolger der Houdek Maschinenbau)  abgeändert.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_129`)


Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim  Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Wien 1/23  am 07.03.2016 das  Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO  wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da  11 von 39 Seite 12 von 39

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_142`)


Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der  Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des  Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann,  wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum  Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_204`)


Damit hat das FA Wien 1/23  in seinem Bescheid vom 07.03.2016 die Vorfrage gemäß der  Rechtsanschauung in der BFG-Entscheidung beurteilt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_205`)


(Das FA Wien 1/23  war zu diesem Zeitpunkt  gern.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_251`)


Diesen  Ausführungen des Finanzamtes ist aus folgenden Gründen entgegenzutreten:   2.1 Nichtvorliegen einer Vorfrage im Sinne des § 303 Abs 1 lit c BAO iVm § 116 BAO   Es liegt schon keine Vorfrage iSd § 116 BAO vor, da das FA Wien 1/23  für die hier  entscheidungserheblichen Fragestellungen sachlich zuständige Behörde ist.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_261`)


2.2 Unzulässige Vermengung der Begründungselemente der VwGH-Entscheidung durch das  FA Wien 1/23  In ihren Ausführungen hinsichtlich der Begründung der Wiederaufnahme nimmt das Finanzamt  immer wieder auf die Entscheidung des Verwaltungsgerichtshofes im Beschwerdeverfahren  22 von 39 Seite 23 von 39

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_267`)


Die vom FA Wien 1/23  in weiterer Folge zitierten Ausführungen (Rz 30 VwGH-Entscheidung)  betreffen Ausführungen des VwGH zu - nicht verfahrensgegenständlichen - Folgejahren.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_281`)


Schon aus diesem  Grund kann sich das FA Wien 1/23  für die gegenständliche Wiederaufnahme nicht auf eine  Entscheidung des VwGH, in welcher nur über die Höhe des Verlustes abgesprochen worden ist,  stützen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_332`)


In verfassungskonformer Interpretation  liegt lt.   Ansicht des FA Wien 1/23  eine Vorfrage gem. § 303 Abs. 1 lit c. BAO vor.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_346`)


Sowohl  die Großbetriebsprüfung, das FA Wien 1/23, die nunmehrige Beschwerdeführerin (die im Übrigen  selbst lediglich für das Jahr 2007 das freie Wahlrecht und die Verlustzuteilung geklärt haben  wollte und daher für das Jahr 2010 "nur" die Streitfrage der Angemessenheit der PKW- Aufwendungen im Verfahren RV/5100056/2014 vor dem BFG vorbrachte) und natürlich auch  der BFG-Richter gingen übereinstimmend in der Vergangenheit davon aus, dass die Streitfrage,   ob ein freies Wahlrecht iZm dem innerbetrieblichen Verlustausgleich vorliegt oder nicht, eine  Streitfrage des Jahres 2007 ist.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_353`)


Das Erkenntnis des BFG wurde zwar  sofort durch das FA Wien 1/23  mittels Amtsrevision bekämpft, war jedoch jedenfalls gem. § 282  BAO durch das Finanzamt umzusetzen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_372`)


Im Übrigen entspricht dieser Verlustvortrag wieder jenem Betrag, wie er vor der erfolgten  Anpassung an das Erkenntnis des BFG, seitens des FA Wien 1/23  im Rahmen der BVE vom  19.11.2013 festgesetzt worden ist und wogegen - wie bereits erwähnt weder in der  Beschwerde noch im Vorlageantrag - die Rechtsunrichtigkeit eingewandt wurde.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_388`)


Aus diesem Grunde wurden auch seitens des FA Wien 1/23  in weiterer Folge im Jahr  2017 und 2018 Unterbrechungshandlungen für das Jahr 2010 gesetzt, um die  Rechtsproblematik der Verjährung für das Jahr 2010 hintanzuhalten.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_408`)


Somit war es  dem FA Wien 1/23  im Jahr 2016 verwehrt - ungeachtet der eingebrachten Amtsrevision -, den  33 von 39 Seite 34 von 39

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_410`)


Antrag des Finanzamtes:   Das FA Wien 1/23  hält seine Rechtsmeinung weiterhin aufrecht, dass ein Anwendungsfall des §  303 Abs. 1 lit c BAO in verfassungskonformer Interpretation vorliegt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

</details>

---

## `Specific Entity: Universität Wien`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches 'Universität Wien' specifically.

**Content:**
```
\bUniversität\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.010 | 0.020 | 18 | 18 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 1658 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_4`)


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_46`)


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_10`)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_27`)


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_116`)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `Specific Entity: Bundesamt für Soziales und Behindertenwesen`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its genitive form 'Bundesamts für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamts?\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.015 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 1111 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_38`)


In § 35 Abs. 2 EStG 1988 hat der Gesetzgeber bindend festgelegt, dass die Tatsache der  Behinderung und das Ausmaß der Minderung der Erwerbsfähigkeit (Grad der Behinderung)  durch eine amtliche Bescheinigung der für diese Feststellung zuständigen Stelle - hier das  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice) – nachzuweisen ist.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_49`)


– In allen übrigen Fällen sowie bei Zusammentreffen von   Behinderungen verschiedener Art das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_56`)


Die zuständige Stelle ist im  gegenständlichen Fall das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_59`)


Die Bescheinigung des Bundesamts für Soziales  und Behindertenwesen (Sozialministeriumservice) als gesetzlich ausdrücklich geforderter  Nachweis kann durch die Vorlage von zB haus- oder fachärztlichen Bestätigungen,  Privatgutachten oder Arztbriefen anlässlich eines stationären Krankenhausaufenthaltes nicht  ersetzt werden.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales  und Behindertenwesen` | `Bundesamts für Soziales  und Behindertenwesen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_78`)


Diese  Feststellung ob, ab wann und in welchem Ausmaß eine Behinderung vorliegt, obliegt nur dem  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_18`)


2. Beweiswürdigung  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist dem Finanzamt Österreich vom Bundesamt für Soziales und  Behindertenwesen mit einer Bescheinigung aufgrund eines ärztlichen  Sachverständigengutachtens nachzuweisen (§ 8 Abs. 6 FLAG).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_19`)


Sowohl die Abgabenbehörde als  auch das Bundesfinanzgericht sind an die im Sachverständigengutachten des Bundesamts für  Soziales und Behindertenwesen getroffenen Feststellungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamts für  Soziales und Behindertenwesen` | `Bundesamts für  Soziales und Behindertenwesen` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_20`)


Gutachten des  Bundesamts für Soziales und Behindertenwesen dürfen lediglich auf Schlüssigkeit,  Vollständigkeit und im Fall mehrerer Gutachten auf Widerspruchsfreiheit überprüft werden (zB  VwGH 9.9.2017, 2013/16/0049).

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_21`)


Die Behinderung der Bf seit Juli 1999 ergibt sich ebenso wie deren Ausmaß von 30% aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_22`)


Da sich dieses Gutachten auf sämtliche zum  Zeitpunkt der Gutachtenserstellung vorliegenden Befunde stützt, ist es, was die Frage des  Zeitpunkts des Eintritts der Behinderung und deren Ausmaß anbelangt, das aus Sicht des  Bundesfinanzgerichts glaubwürdigste, weil vollständigste, der insgesamt drei Gutachten des  Bundesamts für Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_26`)


Die Behinderung im Ausmaß von 50% seit Mai 2012 ergibt sich ebenfalls aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_38`)


Die drei Sachverständigengutachten des Bundesamts für Soziales und Behindertenwesen  widersprechen sich bezüglich der Frage, ob die Bf dauerhaft erwerbsunfähig ist.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_47`)


Gutachtens vom 2. Juli 2021 und der damit im Zusammenhang stehenden chefärztlichen  Stellungnahme vom 6. Juli 2021 kann das Bundesfinanzgericht daher dem Schluss der beiden  Gutachten des Bundesamts für Soziales und Behindertenwesen vom 14. Februar 2024 und vom  5. Dezember 2024, die Bf sei (erst) seit Juli 2021 dauerhaft erwerbsunfähig, nicht folgen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

</details>

---

## `Specific Entity: Bundesamtes für Soziales und Behindertenwesen`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Bundesamtes für Soziales und Behindertenwesen' (genitive) and 'Bundesamt für Soziales und Behindertenwesen' (nominative).

**Content:**
```
\bBundesamts?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.015 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 1111 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_38`)


In § 35 Abs. 2 EStG 1988 hat der Gesetzgeber bindend festgelegt, dass die Tatsache der  Behinderung und das Ausmaß der Minderung der Erwerbsfähigkeit (Grad der Behinderung)  durch eine amtliche Bescheinigung der für diese Feststellung zuständigen Stelle - hier das  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice) – nachzuweisen ist.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_49`)


– In allen übrigen Fällen sowie bei Zusammentreffen von   Behinderungen verschiedener Art das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_56`)


Die zuständige Stelle ist im  gegenständlichen Fall das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_59`)


Die Bescheinigung des Bundesamts für Soziales  und Behindertenwesen (Sozialministeriumservice) als gesetzlich ausdrücklich geforderter  Nachweis kann durch die Vorlage von zB haus- oder fachärztlichen Bestätigungen,  Privatgutachten oder Arztbriefen anlässlich eines stationären Krankenhausaufenthaltes nicht  ersetzt werden.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales  und Behindertenwesen` | `Bundesamts für Soziales  und Behindertenwesen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_78`)


Diese  Feststellung ob, ab wann und in welchem Ausmaß eine Behinderung vorliegt, obliegt nur dem  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_18`)


2. Beweiswürdigung  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist dem Finanzamt Österreich vom Bundesamt für Soziales und  Behindertenwesen mit einer Bescheinigung aufgrund eines ärztlichen  Sachverständigengutachtens nachzuweisen (§ 8 Abs. 6 FLAG).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_19`)


Sowohl die Abgabenbehörde als  auch das Bundesfinanzgericht sind an die im Sachverständigengutachten des Bundesamts für  Soziales und Behindertenwesen getroffenen Feststellungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamts für  Soziales und Behindertenwesen` | `Bundesamts für  Soziales und Behindertenwesen` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_20`)


Gutachten des  Bundesamts für Soziales und Behindertenwesen dürfen lediglich auf Schlüssigkeit,  Vollständigkeit und im Fall mehrerer Gutachten auf Widerspruchsfreiheit überprüft werden (zB  VwGH 9.9.2017, 2013/16/0049).

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_21`)


Die Behinderung der Bf seit Juli 1999 ergibt sich ebenso wie deren Ausmaß von 30% aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_22`)


Da sich dieses Gutachten auf sämtliche zum  Zeitpunkt der Gutachtenserstellung vorliegenden Befunde stützt, ist es, was die Frage des  Zeitpunkts des Eintritts der Behinderung und deren Ausmaß anbelangt, das aus Sicht des  Bundesfinanzgerichts glaubwürdigste, weil vollständigste, der insgesamt drei Gutachten des  Bundesamts für Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_26`)


Die Behinderung im Ausmaß von 50% seit Mai 2012 ergibt sich ebenfalls aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_38`)


Die drei Sachverständigengutachten des Bundesamts für Soziales und Behindertenwesen  widersprechen sich bezüglich der Frage, ob die Bf dauerhaft erwerbsunfähig ist.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_47`)


Gutachtens vom 2. Juli 2021 und der damit im Zusammenhang stehenden chefärztlichen  Stellungnahme vom 6. Juli 2021 kann das Bundesfinanzgericht daher dem Schluss der beiden  Gutachten des Bundesamts für Soziales und Behindertenwesen vom 14. Februar 2024 und vom  5. Dezember 2024, die Bf sei (erst) seit Juli 2021 dauerhaft erwerbsunfähig, nicht folgen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

</details>

---

## `Specific Entity: Merkur Treuhand Steuerberatung GmbH`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'Merkur Treuhand Steuerberatung GmbH' specifically, allowing for variable whitespace including newlines.

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 0 | 25 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Hartwig Boehler  in der Beschwerdesache DDr.in Josepha de Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch Merkur Treuhand Steuerberatung GmbH, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom 16. Mai 2024 gegen den Bescheid des Finanzamtes  Österreich vom 13. Mai 2024 betreffend Abrechnung gem. § 216 BAO Steuernummer  01-186/7053  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und festgestellt, dass die  Umbuchung des per 3.4.2024 auf dem Abgabenkonto der Beschwerdeführerin bestehenden  Guthabens i.H.v. € 166.146,40 auf Finanzverwahrnisse unrichtig war.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_43`)


B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.


B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_44`)


Weiters wurde  der Merkur Treuhand Steuerberatung GmbH darin die Vollmacht „zum Empfang von  Schriftstücken, insbesondere der Abgabenbehörden, welche nunmehr ausschließlich dem  Bevollmächtigten zuzustellen sind“ erteilt und mitgeteilt, dass durch die vorliegende Vollmacht  „noch etwa beim Finanzamt erliegende vorhergehende Vollmachten außer Kraft gesetzt“  werden.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_45`)


Im (Begleit-) Schreiben vom 13.3.2024 führt die Merkur Treuhand Steuerberatung  GmbH aus, dass die Vollmacht als „Spezialvollmacht für das laufende Verfahren betreffend  Umsatzsteuer und NOVA sowie das Finanzstrafverfahren“ erteilt wurde.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung  GmbH` | `Merkur Treuhand Steuerberatung  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)


Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_63`)


Die Feststellungen zum Sicherstellungsauftrag vom 20.3.2024 und zum Pfändungsbescheid  vom 3.4.2024 gründen sich auf eine Einsichtnahme in den Akt RV/702183/2024 des  Bundesfinanzgerichtes (dort bekämpft die Beschwerdeführerin den Pfändungsbescheid vom  3.4.2024), insbesondere auf den Zustellnachweis (Rückschein) zum Sicherstellungsauftrag vom  20.3.2024 und zum Pfändungsbescheid vom 3.4.2024, worin ein Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der Schabetsberger Steuerberatung GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, sowie auf das Schreiben der  Merkur Treuhand Steuerberatung GmbH vom 13.3.2024 und die damit übermittelte Vollmacht  vom 11.3.2024.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_107`)


Im vorliegenden Fall bestellte die Beschwerdeführerin am 11.3.2024 die Merkur Treuhand  Steuerberatung GmbH zum Zustellbevollmächtigten.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand  Steuerberatung GmbH` | `Merkur Treuhand  Steuerberatung GmbH` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_110`)


Anzumerken ist, dass die Vollmacht zugunsten der Merkur  Treuhand Steuerberatung GmbH entgegen den Ausführungen im Schreiben vom 13.3.2024 alle  steuerlichen Angelegenheiten umfasst und daher nicht auf das laufende Verfahren betreffend  Umsatzsteuer und NOVA sowie das Finanzstrafverfahren eingeschränkt ist.

| Predicted | Gold |
|---|---|
| `Merkur  Treuhand Steuerberatung GmbH` | `Merkur  Treuhand Steuerberatung GmbH` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_121`)


Die hier geschehene Übermittlung der eingescannten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail der Schabetsberger  Steuerberatung GmbH vom 16.4.2024 an die Merkur Treuhand Steuerberatung GmbH konnte  daher keine Heilung der unwirksamen Zustellung bewirken.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

</details>

---

## `Specific Entity: SeneCura Variations`

**F1:** 0.011 | **Precision:** 0.909 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'SeneCura', 'SENECURA', 'Senecura' and their full names with flexible spacing (e.g., 'Laurentius  Park').

**Content:**
```
\b(?:SENECURA|SeneCura|Senecura)(?:\s+(?:Laurentius\s+Park(?:\s+Bludenz)?|Laurentius\s+Park\s+Bludenz))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.909 | 0.006 | 0.011 | 11 | 10 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 1 | 1314 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_11`)


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |
| `SENECURA` | `SENECURA` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_12`)


Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_36`)


Darin wurden weitere Nachweise und Unterlagen zu den Krankheitskosten für  die Mutter der Bf angefordert (Vereinbarung über die Kostentragung mit dem Pflegeheim,  Rechtsgrundlage für die Übernahme der Zahlungen für diverse Lebenshaltungskosten,  Nachweise über tatsächliche Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst SENECURA, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, etc).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_50`)


Anschließend brachte die belangte Behörde ergänzend vor, dass sie die Richtigkeit des Inhaltes  der Rechnung vom 25.04.2016 (es wurden 4 weitere Rechnungen/Bestätigungen der SeneCura  im Rahmen des Ermittlungsverfahrens von der Bf bzw von deren Vertreter vorgelegt) in der  Höhe von 985,34 Euro bezweifle und ihr diese nicht gänzlich richtig erscheine, da hier  Kostenteile des Kostenträgers nicht abgerechnet, sondern zugerechnet wurden.

| Predicted | Gold |
|---|---|
| `SeneCura` | `SeneCura` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_61`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Mutter der Bf war in den streitgegenständlichen Jahren im Pflegeheim SeneCura Laurentius  Park Bludenz (beginnend ab 28.01.2016) untergebracht.

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius  Park Bludenz` | `SeneCura Laurentius  Park Bludenz` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_68`)


Die Bf lebte in Wien, die Mutter der Bf war in Bludenz im Pflegeheim SeneCura Laurentius Park  untergebracht.

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius Park` | `SeneCura Laurentius Park` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_69`)


Damit ihre Mutter nicht vereinsamte, übernahm die Bf die Kosten für eine  Besuchshilfe (Mobiler Hilfsdienst Senecura), welcher bereits aber auch in den Jahren, bevor die  Mutter der Bf ins Pflegeheim kam, regelmäßig gebucht war.

| Predicted | Gold |
|---|---|
| `Senecura` | `Senecura` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_77`)


Für das Jahr 2016 wurden von der Bf zusätzlich Pflege(heim)kosten iHv 3.259,47 Euro von  ihrem Konto an SeneCura überwiesen.

| Predicted | Gold |
|---|---|
| `SeneCura` | `SeneCura` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_80`)


2. Beweiswürdigung  Der Sachverhalt ist grundsätzlich unstrittig und ergibt sich als solcher aus dem Akt,  insbesondere den angeführten Aktenteilen wie den Bestätigungen der PVA, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.

| Predicted | Gold |
|---|---|
| `SeneCura  Laurentius Park Bludenz` | `SeneCura  Laurentius Park Bludenz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_13`)

**False Positives:**


Dazu wurden von der Bf Bestätigungen der PVA, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten für Nervenheilkunde vorgelegt.

FP: `SeneCura` (organisation)

**✅ Gold Entities:**
- `PVA` (organisation)
- `SeneCura Laurentius-Park Bludenz` (organisation)

</details>

---

## `Specific Entity: Bundesministerium`

**F1:** 0.011 | **Precision:** 0.833 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium' and 'Bundesministerin' with optional genitive form and common department suffixes.

**Content:**
```
\bBundes(?:minister(?:ium|iums)?|in(?:\s+f\u00fcr)?)\s+f\u00fcr\s+(?:Finanzen|Inneres|Justiz|Arbeit,\s+Soziales\s+und\s+Konsumentenschutz|Bildung,\s+Kunst\s+und\s+Kultur)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.833 | 0.006 | 0.011 | 12 | 10 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 2 | 1318 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1_43`)


Nach Auskunft des Bundesministeriums für Finanzen in gleichgelagerten Fällen ist der im  Signaturblock angegebene Tag im Allgemeinen jener Tag, an welchem der Bescheid in die  Databox eingebracht wurde, weil diese Einbringung in der Regel innerhalb einer Stunde ab  Erstellung der Amtssignatur erfolgt.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_42`)


Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG und der österreichischen Wohnadresse Bf-Adr Ö und der Zeitdauer der Benutzung  eines Massenbeförderungsmittels gründen sich auf eine vom Bundesfinanzgericht  durchgeführte Berechnung mit dem von Bundesministerium für Finanzen im Internet zur  Verfügung gestellten Pendlerrechner.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_91`)


Gemäß § 3 Abs 1 Pendlerverordnung ist für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist, für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_92`)


Das Bundesfinanzgericht führte im Zuge seiner Entscheidungsfindung eine Berechnung mit  dem vom Bundesministerium für Finanzen im Internet zur Verfügung gestellten  Pendlerrechner durch.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated_TRAIN/149473.1_105`)


Die Feststellungen zum Login-Versuch,  zur Sperre und zu den beiden Rücksetzungsverfahren gründen sich auf das Vorbringen des BF,  die aus dem elektronischen Akt des FAÖ abrufbaren Informationen sowie auf im Amtshilfeweg  vom Bundesministerium für Finanzen erteilte Auskünfte.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_87`)


Dass die  Liegenschaft vor dem 31.12.2019 an den Käufer übergeben wurde hat die Bf. einerseits selbst  in ihrer Erklärung an Eides statt vom 19.07.2022 ausgeführt und deckt sich andererseits mit  den Eintragungen im Zentralen Melderegister des Bundesministeriums für Inneres (demnach  wurde der verfahrensgegenständliche Hauptwohnsitz am 19.12.2019 abgemeldet).

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Inneres` | `Bundesministeriums für Inneres` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_72`)


Die Differenz iHv 2.114,80 €  entspricht dem mit dem Kurzzeiteinsatz zusammenhängenden, im Lohnzettel des  Bundesministerium für Inneres ausgewiesenen Reisekostenersatz, welcher zuvor iSd § 47 EStG  durch Abzug vom Arbeitslohn versteuert wurde.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Inneres` | `Bundesministerium für Inneres` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_73`)

**False Positives:**


Der Bundesminister für Finanzen wird ermächtigt, Kriterien zur Festlegung der Entfernung  und der Zumutbarkeit der Benützung eines Massenverkehrsmittels mit Verordnung festzulegen.

FP: `Bundesminister für Finanzen` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) ( sent_id: `findok-manually-annotated_TRAIN/148648.1_103`)

**False Positives:**


Der Bundesminister für Finanzen wird ermächtigt, Kriterien zur Festlegung der  Entfernung und der Zumutbarkeit der Benützung eines Massenverkehrsmittels mit  Verordnung festzulegen.

FP: `Bundesminister für Finanzen` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Frontex`

**F1:** 0.011 | **Precision:** 0.526 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'Frontex' and 'Europäische Grenzschutzagentur Frontex' (and genitive 'Europäischen') as organizations.

**Content:**
```
\b(?:Europäischen?\s+Grenzschutzagentur\s+Frontex|Frontex)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.526 | 0.006 | 0.011 | 19 | 10 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 9 | 239 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_6`)


Über Aufforderung der belangten Behörde gliederte der Bf. die Reisekosten wie folgt auf:  Einsätze für die Grenzschutzagentur Frontex: versteuerte Taggelder  Einsatz im Jahr 2018 als Frontex-Beamter in  Sardinien (I) vom 04.06.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_43`)


Zur Reisezulage:  Im Kalenderjahr 2019 war ich einmal für die Organisation "Europäische Grenzschutzagentur  Frontex" in Trapani auf der Insel Silzilien (I) tätig.

| Predicted | Gold |
|---|---|
| `Europäische Grenzschutzagentur  Frontex` | `Europäische Grenzschutzagentur  Frontex` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_46`)


Für die Tätigkeit  bei der "Europäischen Grenzschutzagentur Frontex" wird eine Reisezulage in der Höhe von 98,--  Euro täglich gewährt.

| Predicted | Gold |
|---|---|
| `Europäischen Grenzschutzagentur Frontex` | `Europäischen Grenzschutzagentur Frontex` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_62`)


Werbungskosten die in Zusammenhang mit Frontex, EASO, ... Einsätzen stehen, dürfen daher in  solchen Fällen nicht berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_74`)


Da mit den von der  Besteuerung ausgenommenen Taggelder in Zusammenhang mit dem Kurzzeiteinsatz für  Frontex auch die laut Reisekosten-Beilage gesondert beantragten Kilometer-/ und Taggeld iHv  355,15 € abgerechnet wurden steht eine weitere pauschalierte Vergütung nicht zu, daher  wurden mit Beschwerdevorentscheidung vom 13.12.2021 alle in Zusammenhang mit dem  Frontex-Einsatz stehenden weiteren Werbungskosten nicht berücksichtigt.“

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_76`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer (Bf.) ist Polizist und wurde gemäß § 39a BDG in der Zeit 26. Februar 2025  an Frontex entsendet und war im Auslandseinsatz in Sizilien.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)


Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_119`)


Der Bf. wurde gemäß § 39a BDG an Frontex für die Zeit vom 26. Februar 2025  entsendet und war  für Frontex im Ausland tätig;


Der Bf. wurde gemäß § 39a BDG an Frontex für die Zeit vom 26. Februar 2025  entsendet und war  für Frontex im Ausland tätig;

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |
| `Frontex` | `Frontex` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_136`)


Frontex unterscheidet bei den „Reimbursement Rules“ (Rückerstattungsvereinbarungen):  https://etendering.ted.europa.eu/document/document-file-download.html?docFileId=69347 )  zwischen Taggeldern und Reisekostenersätzen.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_6`)

**False Positives:**


Über Aufforderung der belangten Behörde gliederte der Bf. die Reisekosten wie folgt auf:  Einsätze für die Grenzschutzagentur Frontex: versteuerte Taggelder  Einsatz im Jahr 2018 als Frontex-Beamter in  Sardinien (I) vom 04.06.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Frontex` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_10`)

**False Positives:**


Einsatz im Jahr 2019 als Frontex-Beamter in  Sizilien (I) vom 16.07.

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_25`)

**False Positives:**


Frontex-Einsatz: Anreise  zumFlugh.

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_28`)

**False Positives:**


Frontex-Einsatz in Sizilien  (Trapani) 31 x Frühstück a'  5,85   181,35  181,35  18.08.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Trapani` (city)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_63`)

**False Positives:**


Somit wurden von den beantragten 485,15€ alle in  Zusammenhang mit dem Frontex-Einsatz stehenden Werbungskosten nicht berücksichtigt  (485,15€ - 355,15€).

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_65`)

**False Positives:**


Werbungskosten berücksichtigt werden, da auch diese Kosten im Zusammenhang mit dem  Frontex-Einsatz stehen.“

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_67`)

**False Positives:**


Die Kürzung der Reisekosten um die Aufwendungen iZm dem Frontex-Einsatz seien nicht  gerechtfertigt, da diese Dienstreisen ausschließlich im Rahmen der Tätigkeit bei der  Kriminalpolizei in Österreich getätigt worden seien.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Kriminalpolizei in Österreich` (organisation)

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_74`)

**False Positives:**


Da mit den von der  Besteuerung ausgenommenen Taggelder in Zusammenhang mit dem Kurzzeiteinsatz für  Frontex auch die laut Reisekosten-Beilage gesondert beantragten Kilometer-/ und Taggeld iHv  355,15 € abgerechnet wurden steht eine weitere pauschalierte Vergütung nicht zu, daher  wurden mit Beschwerdevorentscheidung vom 13.12.2021 alle in Zusammenhang mit dem  Frontex-Einsatz stehenden weiteren Werbungskosten nicht berücksichtigt.“

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Frontex` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)

**False Positives:**


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Flughafen München` (organisation)
- `BMI` (organisation)

</details>

---

## `Specific Entity: Landespolizeidirektion Wien`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirektion Wien' specifically.

**Content:**
```
\bLandespolizeidirektion\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.009 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 1125 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_7`)


Entscheidungsgründe  Verfahrensgang:  Das Abstellen des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A)  wurde von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien  (A118) am 18. April 2025 um 11:07 Uhr in 1120 Wien, Meidlinger Hauptstraße 67,  beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_19`)


In dem Schreiben vom 18. August 2025 wurde zum Ergebnis der Beweisaufnahme angeführt:  „Aus der Organstrafverfügung, welche von einem Organ des Parkraumüberwachungsorgans  der Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung gelegt wurde,  ergibt sich, dass das Fahrzeug der Marke Marke mit dem behördlichen Kennzeichen 123 am  18.04.2025 um 11:07 Uhr in 1120 Wien, Meidlinger Hauptstraße 67, in einer  gebührenpflichtigen Kurzparkzone abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_7`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug, mit dem behördlichen Kennzeichen W-Kennz. (A) wurde vom  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 07. Mai 2025  um 11:59 Uhr in der gebührenpflichtigen Kurzparkzone in 1050 Wien, Bacherplatz gegenüber  14, beanstandet, da es zur Beanstandungszeit ohne gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Specific Entity: Retail Chains`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches common retail organization names: Ikea, Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz, Quelle.at.

**Content:**
```
\b(?:Ikea|Obi|Leiner|M\u00f6belix|M\u00f6maX|Otto\.de|xxxLutz|Quelle\.at)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.009 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 1562 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |
| `Obi` | `Obi` |
| `Leiner` | `Leiner` |
| `Möbelix` | `Möbelix` |
| `MömaX` | `MömaX` |
| `Otto.de` | `Otto.de` |
| `xxxLutz` | `xxxLutz` |
| `Quelle.at` | `Quelle.at` |

</details>

---

## `Specific Entity: VfGH`

**F1:** 0.009 | **Precision:** 0.182 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'VfGH' standalone or as part of 'Verfassungsgerichtshof (VfGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verfassungsgerichtshof(?:es)?(?:\s*\(\s*VfGH\s*\))?|VfGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.182 | 0.005 | 0.009 | 44 | 8 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 36 | 1575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `Verfassungsgerichtshof` (organisation)


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_157`)

**False Positives:**


Der VfGH hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_159`)

**False Positives:**


Dem genannten VfGH-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung aus dem Jahr 1984 gab die zuständige FLD der Berufung einer  Gesellschafterin gegen die einheitliche und gesonderte Gewinnfeststellung in der Form statt,  dass die im Erstbescheid bei der Gesellschafterin zur Gänze als Gewinnanteil behandelte  Ablösezahlung mit 2/3 zu aktivieren und auf 6 Jahre verteilt abzuschreiben war.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_162`)

**False Positives:**


Der VfGH bejahte die Anwendbarkeit des Vorfragentatbestandes.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_172`)

**False Positives:**


Der Verfassungsgerichtshof ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein  derartiger Fall, nämlich wenn eine Entscheidung derselben Behörde für einen früheren  Steuerzeitraum, die sich in der rechtlichen Würdigung des Sachverhaltes direkt auf einen  (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt, in gleicher Weise behandelt  werden muss, wie der Fall der Vorfrage;

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_293`)

**False Positives:**


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_295`)

**False Positives:**


Im der  zitierten Entscheidung des Verfassungsgerichtshofes zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher Aktivierung eine beantragte Wiederaufnahme für die Folgejahre  zwecks Berücksichtigung der AfA vorzunehmen ist.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_301`)

**False Positives:**


Erst der Verfassungsgerichtshof kam zu dem  Ergebnis, dass in diesem Fall ein Wiederaufnahmegrund vorliege bzw eine Wiederaufnahme zu  verfügen sei, um ein gleichheitskonformes Ergebnis zu erreichen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_313`)

**False Positives:**


- Weiters wurde vom Verfassungsgerichtshof aufgezeigt, dass eine Nichtwiederaufnahme im  Hinblick auf die Jahre 1975 und 1976 auch dem Grundsatz von Treu und Glauben  widersprechen würde, da sich die Abgabepflichtigen auf die ursprüngliche rechtliche  Beurteilung der Behörde verlassen haben.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_316`)

**False Positives:**


Im Ergebnis zeigt sich, dass eine Erweiterung der Regelung des § 303 BAO auch vom  Verfassungsgerichtshof nur in bestimmten Ausnahmefällen angedacht ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_328`)

**False Positives:**


Dazu ergänzend wird seitens des Finanzamtes zu den Beschwerdeausführungen wie folgt  Stellung genommen:   Wie bereits in der händischen Begründung der Wiederaufnahme vom 29.01.2019 ausgeführt,  kam der VfGH in seiner Entscheidung B 783/89 vom 6.12.1990 zum Schluss, dass auch eine  Wiederaufnahme des Verfahrens in verfassungsgemäßer Interpretation möglich ist und eine  Vorfrage deshalb auch nicht nur "klassisch" zu verstehen ist.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_329`)

**False Positives:**


D.h. durch die Entscheidung des  VfGH wurden die Wiederaufnahmegründe in ihrem Anwendungsbereich de facto erweitert (so  auch Ritz, 6.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_367`)

**False Positives:**


Lt. Ansicht des Finanzamtes liegt damit auch hier  eine weite Auslegung der Wiederaufnahmebestimmung im Sinn der Rechtsprechung des VfGH  vor (verfassungskonforme Interpretation des § 303 Abs. 1 lit c BAO).

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_383`)

**False Positives:**


Die Wiederaufnahme wurde laut Begründung des angefochtenen Bescheides auf die  verfassungskonforme Auslegung des § 303 Abs. 1 lit c BAO - Wiederaufnahmsgrund laut  Erkenntnis des VfGH vom 6.12.1990, B 783/89 (siehe dazu bei Ritz, BAO, 6.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_385`)

**False Positives:**


Die Parallelität zum vom Verfassungsgerichtshof entschiedenen Fall ergibt  sich daraus, dass nach dem gegenüber der Beschwerdeführerin ergangenen und in Rechtskraft  erwachsenen Bescheid vom 7.3.2016 gegenüber (auch) der Beschwerdeführerin eine anders  lautende Gerichtsentscheidung ergangen ist, nach welcher der Bescheid vom 7.3.2016 so nicht  ergehen hätte dürfen, da die vom BFG gelöste, vom Finanzamt aufgrund der Bindungswirkung  dem Bescheid zugrunde gelegte Rechtsfrage, nachträglich höchstgerichtlich anders beurteilt  bzw. entschieden wurde.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_454`)

**False Positives:**


Dazu hat der VfGH in seinem Erkenntnis vom 6.12.1990, B 783/89  klargestellt, dass als Vorfragetatbestand bei der Wiederaufnahme des Verfahrens auch ein  neuer Bescheid derselben Abgabenbehörde in einem anderen Verfahren in Betracht kommen  kann (siehe Ritz, BAO 5, § 303, Tz 41;

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_457`)

**False Positives:**


In diesem Erkenntnis des VfGH war die Frage zu lösen, ob die nachträgliche Änderung der  behördlichen Auffassung zur Frage der Aktivierung oder Nichtaktivierung eines Aufwandes für  ein bestimmtes Veranlagungsjahr zur Wiederaufnahme nachfolgender - bereits rechtskräftiger  - Veranlagungsjahre, in denen der selbe Aufwand (im Hinblick auf seine Aktivierung)  Auswirkungen zeitigte, führen kann.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_458`)

**False Positives:**


Der VfGH hat zugestanden, dass die rechtliche Beurteilung  eines Sachverhaltes für ein früheres Steuerjahr keine Vorfrage im technischen Sinn darstellt  und dass nach der Judikatur des VwGH die Änderung der rechtlichen Qualifikation eines  Sachverhaltes keine Tatsache iSd § 303 Abs 1 lit. b BAO darstellt.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Universität St. Gallen`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Universität St. Gallen' and 'Universität in St. Gallen' with flexible spacing, covering variations like 'Universität  in St. Gallen'.

**Content:**
```
\bUniversität\s+(?:in\s+)?St\.\s+Gallen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 250 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_24`)


Das Finanzamt erließ eine abweisende Beschwerdevorentscheidung, dies mit folgender  Begründung:   Ihr Sohn P…, geboren am … .2000 studiert seit dem Wintersemester 2020/21 an der Universität  in St. Gallen in der Schweiz, das Studium wird ernsthaft und zielstrebig betrieben.

| Predicted | Gold |
|---|---|
| `Universität  in St. Gallen` | `Universität  in St. Gallen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_45`)


Der Vorlageantrag wurde erhoben wie folgt:   Hinsichtlich der Begründung meines Begehrens und der beantragten Änderungen verweise ich  auf meine Beschwerde vom 29.7.2023 und auf die Stellungnahme vom 13.10.2023 bzw.  möchte diese ergänzen wie folgt:   Mein Sohn P… (geb. … .00) hat von 2020 bis 2023 erfolgreich an der Universität St. Gallen  studiert.

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_50`)


Insbesondere im Studium hatte sich die Corona-Pandemie für Studierende der Universität St.  Gallen zu Gunsten der Ortsunabhängigkeit der Studierenden ausgewirkt.

| Predicted | Gold |
|---|---|
| `Universität St.  Gallen` | `Universität St.  Gallen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_53`)


Außerdem besteht  an der Universität St. Gallen (unabhängig der Pandemie Situation) keine Anwesenheitspflicht.

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_68`)


Der Sohn P… ist seit dem Herbstsemester 2020 für  das Studium der Betriebswirtschaftslehre an der Universität St. Gallen (HSG) in der Schweiz  inskribiert.

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_83`)


Entsprechende Lehrveranstaltungen fanden wöchentlich statt, wie aus der  Prüfungsordnung der Universität St. Gallen für das Studium der Betriebswirtschaftslehre  hervorgeht und deren Besuch und positive Benotung waren jedenfalls Voraussetzung für den  weiteren Studienerfolg.

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_91`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der im Jahr 2000 geborene Sohn der in Wien wohnhaften Bf. studierte seit dem  Wintersemester 2020/21 an der Universität in St. Gallen in der Schweiz, somit im gesamten  Rückforderungszeitraum;

| Predicted | Gold |
|---|---|
| `Universität in St. Gallen` | `Universität in St. Gallen` |

</details>

---

## `Specific Entity: BMF`

**F1:** 0.008 | **Precision:** 0.583 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the acronym 'BMF' (Bundesministerium für Finanzen).

**Content:**
```
\bBMF\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.583 | 0.004 | 0.008 | 12 | 7 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 5 | 1673 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_24`)


Abrufbar auf der  Website des BMF unter Formulare) kann auch für ausländische Arbeitgeber  ausgefüllt werden.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_101`)


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_65`)


Mangels gesetzlicher Vorgaben, aufgrund der diesbezüglichen  VwGH-Rechtsprechung und nach Ansicht des BMF sei es dem Steuerpflichtigen freigestellt, in  welcher Reihenfolge er den innerbetrieblichen Verlustausgleich vornehme, dh. wie er die  positiven Ergebnisse einzelner Teilbetriebe mit den negativen Ergebnissen anderer Teilbetriebe  saldiere, sodass der Steuerpflichtige die für ihn günstigste Form des Verlustausgleichs wählen  könne.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_8`)


Mit  Eingaben vom 8. und 9. August 2023 ergänzte der BF den Antrag dahingehend, dass die  Meldung tatsächlich zunächst noch nicht erfolgt, sondern nur in FOn gespeichert worden sei,  da ein auf Seiten des BMF liegendes technisches Problem die Einbringung verhindere.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_101`)


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated_TRAIN/149473.1_8`)


Mit  Eingaben vom 8. und 9. August 2023 ergänzte der BF den Antrag dahingehend, dass die  Meldung tatsächlich zunächst noch nicht erfolgt, sondern nur in FOn gespeichert worden sei,  da ein auf Seiten des BMF liegendes technisches Problem die Einbringung verhindere.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_129`)


Aufgrund der zwischenzeitlichen Änderungen der Feststellungen betragen die Einkünfte aus  Gewerbebetrieb nunmehr wie folgt (alle Beträge in Euro):  Einkommensteuer 2001:   Gesamte Beteiligungen 2001 laut Online-Abfrage in den Zentralen Anwendungen des BMF : -  138.509 öS = 10.065,84 €  Beteiligung INET II (***): € - 10.065,84 (aufgrund des rechtskräftigem BFG-Erkenntnisses  RV/7102483/2013 vom 27.5.2022 bzw. BP-Bericht vom 29.22.2010 (ABNr.: 121095/09) zur  St.nr.

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_101`)

**False Positives:**


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

FP: `BMF` (organisation)

**✅ Gold Entities:**
- `BMF` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_86`)

**False Positives:**


BMF, AÖF 2006/128, Abschn 5; UFS 24.8.2009, RV/0430-L/04;

FP: `BMF` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_98`)

**False Positives:**


BFG  9.1.2019, RV/3100898/2018),   die persönlichen, insbesondere die wirtschaftlichen Verhältnisse des  Abgabepflichtigen (BMF, AÖF 2006/128, Abschn 4; BFG 14.8.2017,  RV/7102275/2017).

FP: `BMF` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_100`)

**False Positives:**


BMF, AÖF 2006/128, Abschn 4).

FP: `BMF` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_101`)

**False Positives:**


Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).

FP: `BMF` (organisation)

**✅ Gold Entities:**
- `BMF` (organisation)

</details>

---

## `Specific Entity: INET Internet Service GmbH`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the specific organization 'INET Internet Service GmbH'.

**Content:**
```
\bINET\s+Internet\s+Service\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 111 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_6`)


Entscheidungsgründe  Laut den Feststellungsbescheiden des Finanzamts Neunkirchen Wiener Neustadt vom  9.11.2011 für die Jahre 2001 bis 2003 und Nichtfeststellungsbescheid für das Jahr 2004  betreffend INET Internet Service GmbH und Mitges.

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_13`)


Mit den gegenständlich angefochtenen Einkommensteuerbescheiden für die Jahre 2001 bis  2003 vom 21.12.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (FA 07) die  Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter Berücksichtigung der  Grundlagenbescheide vom 9.11.2011 betreffend Mitunternehmerschaft (atypisch stillen  Beteiligung) an der INET Internet Service GmbH und Mitges., St.nr.: ***, (Beteiligung in den  Streitjahren) fest.

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_31`)


Der Bf. war unstrittig in den Streitjahren an der INET Internet Service GmbH und Mitges.

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_75`)


Im Zuge von Wiederholungsprüfungen gem. § 99 FinStrG u.a. bei der INET Internet Service  GmbH und Mitges.

| Predicted | Gold |
|---|---|
| `INET Internet Service  GmbH` | `INET Internet Service  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_83`)


Im Jahr 2008 wurde am 30.1.2008 ein Bescheid gemäß § 293b BAO betreffend das  Feststellungsverfahren der INET Internet Service GmbH und atypisch Stille erlassen, mit  welchem die Feststellungsbescheide für 2001 und 2002, beide vom 22.3.2006, abgeändert  wurden.

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_91`)


Im Jahr 2010 wurden am 29.10.2010 nach Wiederaufnahme geänderte Festellungsbescheide  für 2001 bis 2004 betreffend INET Internet Service GmbH und Mitges.

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

</details>

---

## `Specific Entity: Schule für allgemeine Gesundheits- und Krankenpflege`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the specific school name variations including 'Schule für allgemeine Gesundheits- und Krankenpflege Grillenreith', 'Schule für allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith', 'Schule für allgemeine Gesundheits- und Krankenpflege in Grillenreith', and 'Gesundheits- und Krankenpflege-Schule am LKH Grillenreith'.

**Content:**
```
\b(?:Schule\s+für\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+(?:am\s+LKH\s+|in\s+)?Grillenreith|Gesundheits\-\s+und\s+Krankenpflege\-Schule\s+am\s+LKH\s+Grillenreith)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 789 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

| Predicted | Gold |
|---|---|
| `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` | `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

| Predicted | Gold |
|---|---|
| `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` | `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

| Predicted | Gold |
|---|---|
| `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` | `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_26`)


Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_29`)


Die Tochter der BF absolvierte in der Zeit vom 01.10.2016 bis 04.10.2017 die Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith.

| Predicted | Gold |
|---|---|
| `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith` | `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith` |

</details>

---

## `Specific Entity: Flughafen München`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Flughafen München' specifically.

**Content:**
```
\bFlughafen\s+München\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 231 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_83`)


Der Bf. macht Werbungskosten geltend, die im Zusammenhang mit dem Auslandseinsatz  stehen und zwar Frühstückskosten iHv € 181,35, sowie An- und Rückreisekosten zum Flughafen  München iHv € 173,80.

| Predicted | Gold |
|---|---|
| `Flughafen  München` | `Flughafen  München` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)


Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_127`)


II. Zu den Frühstücks- und Reisekosten:  In Streit steht die Rechtsfrage, ob pauschale Frühstückskosten sowie die An- und  Rückreisekosten zum Flughafen München als Werbungskosten im Zusammenhang mit der  Auslandstätigkeit des Bw., für die er eine steuerfreie Auslandszulage iSd § 21 Gehaltsgesetz  erhalten hat, zu berücksichtigen sind.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_139`)


Die Kosten für die Fahrt  zwischen Wohnort und Flughafen München, die der Bf. mit dem eigenen PKW zurückgelegt  hat, wurden nicht ersetzt.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_141`)


Der Beschwerde war daher teilweise Folge zu geben und die An- und Rückreisekosten zum  Flughafen München in Höhe von € 173,80 zum Abzug zuzulassen.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

</details>

---

## `Specific Entity: University of Bristol`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'University of Bristol'.

**Content:**
```
\bUniversity\s+of\s+Bristol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 663 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_26`)


Die Tochter studiert an der University of Bristol bis voraussichtlich Juli 2023.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_66`)


Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_67`)


2…7 is studying for a Chemistry (BSc) full time at the University of Bristol.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

| Predicted | Gold |
|---|---|
| `University of  Bristol` | `University of  Bristol` |

</details>

---

## `Specific Entity: Schabetsberger Steuerberatung GmbH`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Schabetsberger Steuerberatung GmbH' specifically.

**Content:**
```
\bSchabetsberger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 20 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_51`)


Beide Bescheide (der an das  Finanzamt Österreich adressierte Pfändungsescheid vom 3.4.2024 ergänzt um die Anmerkung  „Ausfertigung für den Abgabenschuldner“) wurden der Beschwerdeführerin am 5.4.2024 zu  Handen der Schabetsberger Steuerberatung GmbH, Fischerstiege 9, 1010 Wien, zugestellt.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)


Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_63`)


Die Feststellungen zum Sicherstellungsauftrag vom 20.3.2024 und zum Pfändungsbescheid  vom 3.4.2024 gründen sich auf eine Einsichtnahme in den Akt RV/702183/2024 des  Bundesfinanzgerichtes (dort bekämpft die Beschwerdeführerin den Pfändungsbescheid vom  3.4.2024), insbesondere auf den Zustellnachweis (Rückschein) zum Sicherstellungsauftrag vom  20.3.2024 und zum Pfändungsbescheid vom 3.4.2024, worin ein Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der Schabetsberger Steuerberatung GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, sowie auf das Schreiben der  Merkur Treuhand Steuerberatung GmbH vom 13.3.2024 und die damit übermittelte Vollmacht  vom 11.3.2024.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_108`)


Gleichzeitig wurden alle bis dahin beim  Finanzamt erliegenden Vollmachten (daher auch eine allfällige Zustellvollmacht der  Schabetsberger Steuerberatung GmbH) aufgelöst.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_114`)


Die Zustellung an die Schabetsberger  Steuerberatung GmbH war unwirksam.

| Predicted | Gold |
|---|---|
| `Schabetsberger  Steuerberatung GmbH` | `Schabetsberger  Steuerberatung GmbH` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_121`)


Die hier geschehene Übermittlung der eingescannten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail der Schabetsberger  Steuerberatung GmbH vom 16.4.2024 an die Merkur Treuhand Steuerberatung GmbH konnte  daher keine Heilung der unwirksamen Zustellung bewirken.

| Predicted | Gold |
|---|---|
| `Schabetsberger  Steuerberatung GmbH` | `Schabetsberger  Steuerberatung GmbH` |

</details>

---

## `Specific Entity: Verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 0.273 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofes'.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.273 | 0.003 | 0.007 | 22 | 6 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 16 | 1577 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149708.1`) ( sent_id: `findok-manually-annotated_TRAIN/149708.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149379.1`) ( sent_id: `findok-manually-annotated_TRAIN/149379.1_65`)


Eine Einschränkung finden diese Überlegungen insoweit, als nach der Rechtsprechung des  Verfassungsgerichtshofes (vgl VfGH 05.03.1979, B 175/76), welcher sich der  Verwaltungsgerichtshof (vgl VwGH 13.02.1991, 90/13/0161;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_172`)

**False Positives:**


Der Verfassungsgerichtshof ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein  derartiger Fall, nämlich wenn eine Entscheidung derselben Behörde für einen früheren  Steuerzeitraum, die sich in der rechtlichen Würdigung des Sachverhaltes direkt auf einen  (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt, in gleicher Weise behandelt  werden muss, wie der Fall der Vorfrage;

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_293`)

**False Positives:**


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_295`)

**False Positives:**


Im der  zitierten Entscheidung des Verfassungsgerichtshofes zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher Aktivierung eine beantragte Wiederaufnahme für die Folgejahre  zwecks Berücksichtigung der AfA vorzunehmen ist.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_301`)

**False Positives:**


Erst der Verfassungsgerichtshof kam zu dem  Ergebnis, dass in diesem Fall ein Wiederaufnahmegrund vorliege bzw eine Wiederaufnahme zu  verfügen sei, um ein gleichheitskonformes Ergebnis zu erreichen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_313`)

**False Positives:**


- Weiters wurde vom Verfassungsgerichtshof aufgezeigt, dass eine Nichtwiederaufnahme im  Hinblick auf die Jahre 1975 und 1976 auch dem Grundsatz von Treu und Glauben  widersprechen würde, da sich die Abgabepflichtigen auf die ursprüngliche rechtliche  Beurteilung der Behörde verlassen haben.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_316`)

**False Positives:**


Im Ergebnis zeigt sich, dass eine Erweiterung der Regelung des § 303 BAO auch vom  Verfassungsgerichtshof nur in bestimmten Ausnahmefällen angedacht ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_385`)

**False Positives:**


Die Parallelität zum vom Verfassungsgerichtshof entschiedenen Fall ergibt  sich daraus, dass nach dem gegenüber der Beschwerdeführerin ergangenen und in Rechtskraft  erwachsenen Bescheid vom 7.3.2016 gegenüber (auch) der Beschwerdeführerin eine anders  lautende Gerichtsentscheidung ergangen ist, nach welcher der Bescheid vom 7.3.2016 so nicht  ergehen hätte dürfen, da die vom BFG gelöste, vom Finanzamt aufgrund der Bindungswirkung  dem Bescheid zugrunde gelegte Rechtsfrage, nachträglich höchstgerichtlich anders beurteilt  bzw. entschieden wurde.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_51`)

**False Positives:**


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_50`)

**False Positives:**


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**
- `COFAG` (organisation)

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_53`)

**False Positives:**


Wenn sich die Bf. dadurch benachteiligt fühlt, dass der Prüfungstermin ohne ihre  Einflussmöglichkeit bereits für Mai 2022 angesetzt wurde, ist ihr Folgendes entgegenzuhalten:  Der Verfassungsgerichtshof hat wiederholt zum Ausdruck gebracht, dass der rechtspolitische  Gestaltungsspielraum des Gesetzgebers bei staatlichen Beihilfen, selbst wenn sie hoheitlich  gewährt werden (zur Familienbeihilfe vgl.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_65`)

**False Positives:**


Eine Verfassungswidrigkeit, die es gebieten würde, die Norm zunächst bis zu einer  Entscheidung des Verfassungsgerichtshofes unangewendet zu lassen, kann das  Bundesfinanzgericht nicht erkennen.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_33`)

**False Positives:**


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Rhein Normonkel Manufaktur GMBH`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Rhein Normonkel Manufaktur GMBH' specifically to ensure the full name is captured and not truncated by the general GMBH pattern.

**Content:**
```
\bRhein\s+Normonkel\s+Manufaktur\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 431 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_32`)


Der ehemalige Arbeitgeber unseres Klienten, die Firma Rhein Normonkel Manufaktur GMBH, hat ihren Sitz in  4331  Wien, Elmbachweg (siehe aktenkundigen Lohnzettel).

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_69`)


II. Über die Beschwerde wurde erwogen:  1. Festgestellter Sachverhalt:  Der Bf war im Streitjahr für die in Wien ansässige Rhein Normonkel Manufaktur GMBH, einem Marktführer im  institutionellen Hygienebereich, als Außendienstmitarbeiter (Vertreter) nichtselbständig tätig.

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_70`)


Im Rahmen dieses Dienstverhältnisses wurde dem Bf von der Rhein Normonkel Manufaktur GMBH  ein Dienstwagen  der Marke Skoda Octavia zur Verfügung gestellt, welchen der Bf auch für Privatfahrten nutzte.

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_71`)


Die Rhein Normonkel Manufaktur GMBH  setzte in der laufenden Lohnverrechnung den vollen Pkw-Sachbezug iHv  332,06 Euro monatlich an.

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_72`)


Auch in den von der Rhein Normonkel Manufaktur GMBH  an das Finanzamt  übermittelten Lohnzettel, der den im Einkommensteuerbescheid 2014 vom 20.5.2015  ausgewiesenen Einkünften aus nichtselbständiger Arbeit zugrunde liegt, hat der volle Pkw- Sachbezug Eingang gefunden.

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

</details>

---

## `Specific Entity: Raiffeisenbank Karnische Rion Bankstelle St.Stefan`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Karnische Rion Bankstelle St.Stefan' specifically, handling the multi-word bank name.

**Content:**
```
\bRaiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 991 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_13`)


Die belangte Behörde forderte den Beschwerdeführer mit Schreiben vom 08.11.2022 auf,  Nachweise zu erbringen, die belegen, dass dieser nicht Kontoinhaber des Kontos mit der  AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  sei.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_36`)


Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis  zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der  Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_39`)


Der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  wurde der Bescheid vom 10.10.2022 zugestellt und aufgetragen, die  gepfändeten Forderungen nicht mehr an den Abgabenschuldiger auszuzahlen.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_41`)


Der Beschwerdeführer ist Kontoinhaber des Kontos mit der AT78 2024 1897 7421 2903  bei der  Raiffeisenbank Karnische Rion  Bankstelle St.Stefan.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_45`)


Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend  Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

</details>

---

## `Specific Entity: PVA`

**F1:** 0.006 | **Precision:** 0.714 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the acronym 'PVA' (Präventionsversicherung) as an organization.

**Content:**
```
\bPVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.714 | 0.003 | 0.006 | 7 | 5 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 2 | 1321 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_10`)


In ihrer Beantwortung vom 27.11.2019 gab die Bf an, dass die nicht vom Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der PVA einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) erhalten würde.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_13`)


Dazu wurden von der Bf Bestätigungen der PVA, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten für Nervenheilkunde vorgelegt.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_63`)


Davon wurde ein Selbstbetrag von der PVA direkt  an den Kostenträger zur teilweisen Deckung der Verpflegungskosten iHv 1.086,53 Euro  überwiesen.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_64`)


Der Restbetrag (lt Verständigung über die Leistungshöhe zum 01.01.2017 der PVA  war dies ein Betrag von ca 200,00 bis 230,00 Euro) verblieb bei der Mutter der Bf als  „Taschengeld“.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_80`)


2. Beweiswürdigung  Der Sachverhalt ist grundsätzlich unstrittig und ergibt sich als solcher aus dem Akt,  insbesondere den angeführten Aktenteilen wie den Bestätigungen der PVA, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_11`)

**False Positives:**


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)
- `SENECURA` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_12`)

**False Positives:**


Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)

</details>

---

## `Specific Entity: UFS`

**F1:** 0.006 | **Precision:** 0.172 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat).

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.172 | 0.003 | 0.006 | 29 | 5 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 24 | 1478 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)


85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_141`)


19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)   29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)   16.12.2013 Vorlage an BFG (damals noch UFS)   17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  07.03.2016 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010   07.03.2016 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 (Erhöhung des  Verlustvortrages infolge BFG-Erkenntnis RV/5101064/2013)

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_64`)

**False Positives:**


UFS 27.11.2007, RV/0087-L/07).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_78`)

**False Positives:**


UFS 18.2.2010, RV/0098-L/06;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_82`)

**False Positives:**


BFG 9.1.2019, RV/3100898/2018),   die Höhe des durch die verspätete Einreichung der Abgabenerklärung erzielten  finanziellen Vorteils (vgl UFS 21.10.2003, RV/0234-G/02, FJ 2004, 77;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_86`)

**False Positives:**


BMF, AÖF 2006/128, Abschn 5; UFS 24.8.2009, RV/0430-L/04;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_93`)

**False Positives:**


UFS 27.11.2007, RV/0087-L/07;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_26`)

**False Positives:**


Von einer Liebhabereitätigkeit kann ja wohl nur dann gesprochen werden, wenn jemand,  dessen Hauptberuf sich von seinem Hobby, dem er aus besonderer Neigung nachgeht (siehe  UFS 27.11.2003, RV/0509-L/02), unterscheidet, und dieses Hobby zu steuerlich unbeachtlichen  Gesamtverlusten führt.

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_30`)

**False Positives:**


Der Zeitpunkt, an dem die Daten in den elektronischen Verfügungsbereich des Empfängers  gelangt sind, ist bei FinanzOnline der Zeitpunkt der Einbringung der Daten in die Databox, zu  der der Empfänger Zugang hat (UFS 22.7.2013, RV/0002-F/13;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149731.1_41`)

**False Positives:**


UFS  22.7.2013, RV/0002-F/13;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) ( sent_id: `findok-manually-annotated_TRAIN/148648.1_62`)

**False Positives:**


Ein Zimmer bei den Eltern ist nicht als Haushalt anzusehen  (UFS 4.12.08, RV/0662-L/07).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_55`)

**False Positives:**


Wird zu einem späteren Zeitpunkt festgestellt, dass Beiträge nicht oder in geringerer Höhe zu  leisten gewesen wären, ändert dies nichts an ihrem ursprünglichen Charakter (UFS 15.4.2013,  RV/0220-W/13;

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)

**False Positives:**


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

FP: `UFS` (organisation)

**✅ Gold Entities:**
- `WU` (organisation)
- `JKU` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)

**False Positives:**


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)

**False Positives:**


UFS 19.10.2010, RV/0180-L/10).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)

**False Positives:**


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)

**False Positives:**


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

FP: `UFS` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_164`)

**False Positives:**


vgl. auch UFS  16.02.2007, RV/0189-G/06).

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)

**False Positives:**


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

FP: `UFS` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Bankhaus Denzel`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Bankhaus Denzel' specifically.

**Content:**
```
\bBankhaus\s+Denzel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 877 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_11`)


für Wohnraumschaffung, das Pendlerpauschale und die Kosten für doppelte Haushaltsführung  und Familienheimfahrten näher zu erläutern und zu belegen, übermittelte der  Beschwerdeführer eine Reihe von Urkunden, darunter ein Kreditantrag an die Bankhaus Denzel  vom 7.9.2000, einen Kfz-Zulassungsschein und eine Auflistung der Fahrten vom  Familienwohnsitz in Ungarn nach Wien und zurück sowie der Fahrten von seinem Quartier in  Wien zum jeweiligen Arbeitsort und zurück.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_50`)


Zu den  Kosten der Wohnraumschaffung bzw. -sanierung legte er nochmals die bereits übermittelten  Kreditunterlagen aus dem Jahr 2000 sowie ein Schreiben der Bankhaus Denzel  vom 26.3.2015 vor,  worin ihm mitgeteilt wird, dass auf dem Kreditkonto ein Saldo i.H.v. € 23.904,50 (inkl. Zinsen  sowie Anwalts- und Gerichtskosten) unberichtigt aushaftet und er aufgefordert wird, die  monatlichen Einzahlungen i.H.v. € 200,00 ab sofort auf dieses Kreditkonto vorzunehmen.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_73`)


Im Jahr 2000 nahm der Beschwerdeführer einen Kredit über ATS 300.000,00 bei der  Bankhaus Denzel  zum Zwecke eines Hausbaues in Ungarn auf.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_90`)


Die Feststellungen zum Kredit ergeben sich aus den vom Beschwerdeführer vorgelegten  Unterlagen, nämlich dem Kreditantrag vom 7.9.2000, der Selbstauskunft vom 31.8.2001 und  dem Schreiben der Bankhaus Denzel  vom 26.3.2015.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

</details>

---

## `Specific Entity: Berwaldkel-Möbel AG`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Berwaldkel-Möbel AG' specifically.

**Content:**
```
\bBerwaldkel-Möbel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 717 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_5`)


Das Pendlerpauschale war bereits vom Arbeitgeber Berwaldkel-Möbel AG  berücksichtigt worden, hatte  aber dort wegen der Geringfügigkeit der Einkünfte bei der Berechnung der Lohnsteuer keine  Auswirkung.

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_7`)


Es wurden daher auch im Einkommensteuerbescheid 2016 vom 27.02.2017 bei der  Berechnung des Einkommens und der Einkommensteuer die bereits um das Pendlerpauschale  in Höhe von 1.476,00 € gekürzten Einkünfte bei der Fa. Berwaldkel-Möbel AG  in Ansatz gebracht.

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_16`)


Beigelegt war eine Bestätigung der Firma Berwaldkel-Möbel AG  vom 09.03.2021, wonach die Beschwerdeführerin das Pendlerpauschale beantragt hätte, es  aber von der Firma nicht berücksichtigt habe werden können, da das Einkommen nicht  lohnsteuerpflichtig sei.

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_27`)


Gleichzeitig wurde in Punkt 2) des Ergänzungsersuchens ausführlich dargestellt, dass das  Pendlerpauschale in den Einkommensteuerbescheiden 2016, 2017 und 2018 dadurch  Berücksichtigung gefunden habe, dass die vom Arbeitgeber Berwaldkel-Möbel AG  übermittelten Einkünfte  schon um das Pendlerpauschale gekürzt worden waren.

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

</details>

---

## `Specific Entity: BMI`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the acronym 'BMI' (Bundesministerium für Inneres) as an organization.

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 237 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_66`)


Mit Schriftsatz vom 07. Jänner 2022 stellte der Bf. einen Vorlageantrag in welchem er  zusätzlich zu dem Vorbringen in der Beschwerde noch angibt, dass eine weitere Möglichkeit für  die steuerfreie Berücksichtigung der € 2.114,80 ein berichtigter Lohnzettel des BMI wäre.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)


Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_93`)


Dem Erkenntnis des  Verwaltungsgerichtshofes vom 4. November 2020, Ra 2020/16/0039-6, liegt die  Grundausbildungsverordnung-Exekutivdienst BMI des Bundesministers für Inneres, BGBl. II  vom 12. Juni 2017, zu Grunde.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

</details>

---

## `Specific Entity: Deloitte Tax Wirtschaftsprüfungs GmbH`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Deloitte Tax Wirtschaftsprüfungs GmbH' specifically, handling variable whitespace.

**Content:**
```
\bDeloitte\s+Tax\s+Wirtschaftsprüfungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1356 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_2`)


Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Fabienne Jostl, Aufschließungsweg Löx Gründe Tschierweg 3, 9862 Vorderkrems, Österreich  vertreten durch Deloitte Tax Wirtschaftsprüfungs  GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerden gegen die Bescheide des  Finanzamtes Österreich vom 5.11.2024 und 26.5.2025 betreffend Umsatzsteuer 2022 und 2023  zu Recht erkannt (Steuernummer 81-450/8995):   I. Die Beschwerdevorentscheidungen des Finanzamtes Österreich vom 17.7.2025, mit  welchen über die Beschwerden gegen die Bescheide des Finanzamtes für Großbetriebe  vom 5.11.2024 (USt 2022) und 26.5.2025 (USt 2023) abgesprochen wurde, werden  wegen Unzuständigkeit der bescheiderlassenden Behörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs  GmbH` | `Deloitte Tax Wirtschaftsprüfungs  GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

</details>

---

## `Specific Entity: Bezirkshauptmannschaft Bludenz`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Bezirkshauptmannschaft Bludenz' specifically.

**Content:**
```
\bBezirkshauptmannschaft\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1323 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_10`)


In ihrer Beantwortung vom 27.11.2019 gab die Bf an, dass die nicht vom Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der PVA einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) erhalten würde.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_24`)


werden und die Heimkosten würden von der Bezirkshauptmannschaft Bludenz getragen.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_67`)


Jener Kostenteil der Pflegeheimkosten der Mutter der Bf, welcher nicht  selbst getragen werden konnte, wurde von der Bezirkshauptmannschaft Bludenz getragen.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

</details>

---

## `General Court Names`

**F1:** 0.003 | **Precision:** 0.750 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches common German court names with location suffixes, simplified pattern.

**Content:**
```
\b(?:Arbeits-\s+und\s+Sozialgericht|Bezirksgericht|Landesgericht|Oberlandesgericht|Bundesgerichtshof|Arbeitsgericht|Finanzgericht|Sozialgericht|Verwaltungsgericht)\s+[A-Z][a-zA-Z\u00C0-\u00FF]+(?:\s+[A-Z][a-zA-Z\u00C0-\u00FF]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.002 | 0.003 | 4 | 3 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 1 | 1106 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_49`)


Die Bf hat  nämlich ein für das Arbeits- und Sozialgericht Wien erstelltes berufskundliches  Sachverständigengutachten vom 29. März 2013 vorgelegt, das eine Erwerbsunfähigkeit der Bf  zum Zeitpunkt der Gutachtenserstellung verneint.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Purkersdorf` | `Bezirksgericht Purkersdorf` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_15`)


Die Verfügungen mit den Zahlen   MA67/GZ/2024 vom 31.03.2025 und   MA67/GZ-2/2024 vom 02.04.2025  jedoch sind nicht berechtigt, daher erhebe ich hiermit das Rechtsmittel der Beschwerde an das  Verwaltungsgericht Wien.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_6`)

**False Positives:**


Gegen den Pfändungsbescheid brachte der Beschwerdeführer am 18.10.2022 Beschwerde ein,  und führte begründend aus, das Bezirksgericht Favoriten habe am TT.06.2022 eine  offenkundige Zahlungsunfähigkeit beschlossen und veröffentlicht.

FP: `Bezirksgericht Favoriten` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: WU Acronym`

**F1:** 0.003 | **Precision:** 0.158 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the standalone acronym 'WU' for Wirtschaftsuniversität Wien.

**Content:**
```
\bWU\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.158 | 0.002 | 0.003 | 19 | 3 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 16 | 638 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_41`)


Siehe Internetseite JKU und WU  Karriereaussichten!

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)

**False Positives:**


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)

**False Positives:**


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)

**False Positives:**


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_29`)

**False Positives:**


Die von der belangten Behörde angeforderten Angaben der WU Wien wurden mit diesem  Schreiben jedoch nicht vorgelegt.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)

**False Positives:**


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `Linz` (city)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)

**False Positives:**


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)

**False Positives:**


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler  Universität Linz` (organisation)
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)

**False Positives:**


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_54`)

**False Positives:**


Aufgrund des Arbeitsauftrages wurde dann ermittelt und es stellte sich ein Studienwechsel mit  WS 19/20 heraus, vom Studium UJ033 561 Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der WU Wien auf UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der JKU Linz.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_61`)

**False Positives:**


Weiters wurde jedoch von  den abgelegten 42 ECTS an der WU Wien, nur 24 ECTS an der JKU Linz angerechnet.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_65`)

**False Positives:**


Im gegenständlichen Fall  wurde das erste Studium an der WU Wien nach 4 Semester gewechselt, also nach dem jeweils  dritten inskribierten Semester und daher liegt ein schädlicher Studienwechsel vor.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_73`)

**False Positives:**


Von den an der WU Wien absolvierten  Lehrveranstaltungen mit 42 ECTS-Punkten wurden 24 ECTS-Punkte an der JKU Linz  angerechnet.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_98`)

**False Positives:**


Die belangte Behörde bringt vor, dass von den abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der JKU Linz angerechnet wurden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `Specific Entity: Sudver Handel Services GMBH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Sudver Handel Services GMBH' specifically.

**Content:**
```
\bSudver\s+Handel\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

</details>

---

## `Specific Entity: Glanznorost Institut GMBH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Glanznorost Institut GMBH' specifically.

**Content:**
```
\bGlanznorost\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

</details>

---

## `Specific Entity: Cervenka&Neunübel Telekom AG`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Cervenka&Neunübel Telekom AG' specifically.

**Content:**
```
\bCervenka&Neunübel\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 877 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_56`)


Der Beschwerdeführer war seit 21.4.1992 und auch noch in den streitgegenständlichen Jahren  als Monteur bei der Cervenka&Neunübel Telekom AG, unselbstständig erwerbstätig.

| Predicted | Gold |
|---|---|
| `Cervenka&Neunübel Telekom AG` | `Cervenka&Neunübel Telekom AG` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_80`)


Die  Feststellungen zur beruflichen Tätigkeit des Beschwerdeführers, zu den konkreten Einsatzorten  und zu den von seinem Arbeitgeber geleisteten Kostenersätzen gründen sich auf das Schreiben  der Cervenka&Neunübel Telekom AG  vom 9.6.2016 sowie die mit diesem Schreiben übermittelten Beilagen  („Dienstnehmerkalender“ und „Baustellenbesetzung“).

| Predicted | Gold |
|---|---|
| `Cervenka&Neunübel Telekom AG` | `Cervenka&Neunübel Telekom AG` |

</details>

---

## `Specific Entity: INET System Informations GmbH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'INET System Informations GmbH' specifically, handling potential double spaces found in training data.

**Content:**
```
\bINET\s+(?:System\s+)?Informations\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 105 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_84`)


Weiters wurde am 9. Dezember 2008 im Rahmen der Ermittlungen zu den  Feststellungsbescheiden 2000 bis 2007 zur Geltendmachung des Angabenanspruchs ein  Ergänzungsersuchen des Finanzamts Neunkirchen Wiener Neustadt an INET System  Informations GmbH und Mitges.

| Predicted | Gold |
|---|---|
| `INET System  Informations GmbH` | `INET System  Informations GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_87`)


Im Jahr 2009 wurde am 9.10.2009 der Prüfungsauftrag betreffend die INET System  Informations GmbH und Mitges.

| Predicted | Gold |
|---|---|
| `INET System  Informations GmbH` | `INET System  Informations GmbH` |

</details>

---

## `Specific Entity: Magistrat der Stadt Klagenfurt`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Klagenfurt' and its genitive form 'Magistrats der Stadt Klagenfurt'.

**Content:**
```
\bMagistrat(?:s)?\s+der\s+Stadt\s+Klagenfurt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 270 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_69`)


Mit selbem Datum wurde das Magistrat der Stadt Klagenfurt  ersucht, den Bauakt die strittige Liegenschaft betreffend vorzulegen, welchem Ersuchen am  19.03.2024 nachgekommen wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Klagenfurt` | `Magistrat der Stadt Klagenfurt` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_89`)


Der Kauf im Jahr 1983 geht aus dem im Bauakt  des Magistrats der Stadt Klagenfurt, GZXX, enthaltenen Grundbuchsauszug vom 26.4.1990 und  dem Historischen Grundbuchsauszug diese Liegenschaft betreffend hervor.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Klagenfurt` | `Magistrats der Stadt Klagenfurt` |

</details>

---

## `Specific Entity: BM für Inneres`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'BM für Inneres' specifically.

**Content:**
```
\bBM\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 245 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_45`)


Auf den Lohnzettel des BM für Inneres wird verwiesen.

| Predicted | Gold |
|---|---|
| `BM für Inneres` | `BM für Inneres` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_51`)


Der Betrag, welcher vom BM für Inneres als Bezüge gem. § 26 EStG ausbezahlt wird, betrifft  den Kfz-Aufwand, die Miete der Wohnung und sonstigen Reisekosten, wie etwa Fahrkarten  usw., jedoch keine Tagesgelder.

| Predicted | Gold |
|---|---|
| `BM für Inneres` | `BM für Inneres` |

</details>

---

## `Specific Entity: Kriminalpolizei in Österreich`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Kriminalpolizei in Österreich' specifically.

**Content:**
```
\bKriminalpolizei\s+in\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_55`)


Die Kürzung betrifft wahrscheinlich die Dienstreisen im Zuge meiner  Tätigkeit bei der Kriminalpolizei in Österreich.

| Predicted | Gold |
|---|---|
| `Kriminalpolizei in Österreich` | `Kriminalpolizei in Österreich` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_67`)


Die Kürzung der Reisekosten um die Aufwendungen iZm dem Frontex-Einsatz seien nicht  gerechtfertigt, da diese Dienstreisen ausschließlich im Rahmen der Tätigkeit bei der  Kriminalpolizei in Österreich getätigt worden seien.

| Predicted | Gold |
|---|---|
| `Kriminalpolizei in Österreich` | `Kriminalpolizei in Österreich` |

</details>

---

## `Specific Entity: Höhere Lehranstalt für Tourismus`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the full name 'Höhere Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit' and its genitive form 'Höheren Lehranstalt...'.

**Content:**
```
\b(?:H\u00f6here|H\u00f6heren)\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin bezog für die Tochter T., geb. 2003, wegen Schulbesuch (Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit in Krems) bis Juni 2022  Familienbeihilfe.

| Predicted | Gold |
|---|---|
| `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` | `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_34`)


Sachverhalt:  T. legte am 30.05.2022 die Reifeprüfung an der Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit ab und machte danach keine weitere Ausbildung.

| Predicted | Gold |
|---|---|
| `Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit` | `Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit` |

</details>

---

## `Specific Entity: The King's School Worcester`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'The King's School Worcester' and 'The King´s School Worcester'.

**Content:**
```
\bThe\s+King['´]s\s+School\s+Worcester\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 665 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_41`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

| Predicted | Gold |
|---|---|
| `The King´s School Worcester` | `The King´s School Worcester` |
| `The King's  School Worcester` | `The King's  School Worcester` |

</details>

---

## `Specific Entity: England`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'England' as an organization in this context (e.g., 'in England').

**Content:**
```
\bEngland\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 669 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

| Predicted | Gold |
|---|---|
| `England` | `England` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

| Predicted | Gold |
|---|---|
| `England` | `England` |

</details>

---

## `Specific Entity: ÖBB`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the acronym 'ÖBB' (Österreichische Bundesbahnen) as an organization.

**Content:**
```
\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1315 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_40`)


Weiters wurde auch eine Aufstellung der Kosten,  welche die Tochter zusätzlich noch übernommen hatte (Fahrkarten ÖBB für Besuche,  Betriebskosten der Wohnung in Bludenz, Depotgeld für das Pflegeheim, etc), beigelegt.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_76`)


Belege für die geltend gemachten Besuchskosten wie für die Jahreskarten der ÖBB sowie der  einzelnen Bahn- oder Bustickets bzw Taxirechnungen wurden nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

</details>

---

## `Specific Entity: Mag. Ghesla Steuerberater GmbH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Mag. Ghesla Steuerberater GmbH' specifically as found in training data.

**Content:**
```
\bMag\.\s+Ghesla\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 988 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

</details>

---

## `Specific Entity: R GmbH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the placeholder organization 'R GmbH' found in training data and failures, handling variable whitespace.

**Content:**
```
\bR[-\s]+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1466 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_121`)


Für den Revisionsfall folge daraus: Die X GmbH habe - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen sei.

| Predicted | Gold |
|---|---|
| `R GmbH` | `R GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_430`)


Der VwGH  führte mit Erkenntnis vom 13.9.2018 (VwGH 13.9.2018, Ro 2016/15/0010) aus: „28 Für den  Revisionsfall folgt daraus: Die X GmbH hat - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen ist.

| Predicted | Gold |
|---|---|
| `R GmbH` | `R GmbH` |

</details>

---

## `Specific Entity: AMS`

**F1:** 0.002 | **Precision:** 0.667 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'AMS Österreich', 'Arbeitsmarktservice (AMS)', and the standalone acronym 'AMS' with correct priority to avoid partial matches.

**Content:**
```
\b(?:AMS\s+Österreich|Arbeitsmarktservice\s*\(\s*AMS\s*\)|(?<!\w)AMS(?!\s+Österreich|\s*\(\s*AMS))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.001 | 0.002 | 3 | 2 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 1 | 1299 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer vom AMS Österreich der Abgabenbehörde übermittelten korrigierten  Mitteilung nahm die Behörde das Verfahren betreffend Einkommensteuer 2019 gemäß § 303  Abs. 1 BAO wieder auf und erließ unter Berücksichtigung der nunmehr korrigierten  Arbeitslosengeldzahlung iHv 1.228,50 Euro für das Jahr 2019 einen neuen  Einkommensteuerbescheid 2019.

| Predicted | Gold |
|---|---|
| `AMS Österreich` | `AMS Österreich` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_27`)


Ebenso sei ihm aufgrund dieser Behinderung eine Umschulung von einem Art Beruf auf neuer  Beruf vom AMS finanziert worden.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_11`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. erhielt für das Jahr 2019 folgende Zahlungen vom Arbeitsmarktservice (AMS):  Am 18.03.2019 308,35 Euro für den Zeitraum 14.01.

FP: `AMS` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Arbeitsmarktservice (AMS)` (organisation)

</details>

---

## `Specific Entity: Pensionsversicherungsanstalt`

**F1:** 0.002 | **Precision:** 0.154 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt' specifically.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.154 | 0.001 | 0.002 | 13 | 2 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 11 | 1264 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_41`)

**False Positives:**


Denn beide eine dauerhafte Erwerbsunfähigkeit bejahenden Gutachten beziehen sich  hinsichtlich der Frage des Eintritts der dauerhaften Erwerbsunfähigkeit auf ein von der Bf  vorgelegtes, von der Pensionsversicherungsanstalt in Auftrag gegebenes Gutachten vom 2. Juli  2021: Dieses stellt fest, dass der Bf „aufgrund der reduzierten psychomotorischen  Belastbarkeit und der geringen Stresstoleranz mit mehrfach gescheiterten Arbeitsversuchen  […] keine Tätigkeiten zumutbar [sind]“.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_42`)

**False Positives:**


Eine sich auf das genannte Gutachten der  Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme vom 6. Juli 2021 hält  fest, dass „das Gesamtleistungskalkül […] für Tätigkeiten auf dem allgemeinen Arbeitsmarkt  vorübergehend mehr als 6 Monate nicht aus[reicht] ab Antragstellung 29.06.2021“.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_45`)

**False Positives:**


Da das für die Pensionsversicherungsanstalt erstellte Gutachten festhält,  dass die Bf „seit ca. 2006 mit Unterbrechung bei Jugend am Werk“ tätig ist, geht die sich auf  das Gutachten der Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme  davon aus, dass die Bf seit 2006 originär invalid (iSd § 255 Abs. 7 ASVG) ist.

FP: `Pensionsversicherungsanstalt` (organisation)


Da das für die Pensionsversicherungsanstalt erstellte Gutachten festhält,  dass die Bf „seit ca. 2006 mit Unterbrechung bei Jugend am Werk“ tätig ist, geht die sich auf  das Gutachten der Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme  davon aus, dass die Bf seit 2006 originär invalid (iSd § 255 Abs. 7 ASVG) ist.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_46`)

**False Positives:**


Vor dem  Hintergrund der Ausführungen des von der Pensionsversicherungsanstalt in Auftrag gegebenen  3 von 6 Seite 4 von 6

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_24`)

**False Positives:**


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_57`)

**False Positives:**


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_58`)

**False Positives:**


Auf den aktenkundigen Lohnzettel der Pensionsversicherungsanstalt sowie den im Akt  aufliegenden Kontrollmitteilungen wird verwiesen.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_24`)

**False Positives:**


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_57`)

**False Positives:**


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_58`)

**False Positives:**


Auf den aktenkundigen Lohnzettel der Pensionsversicherungsanstalt sowie den im Akt  aufliegenden Kontrollmitteilungen wird verwiesen.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific Entity: Wiederspan Beratung GMBH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Wiederspan Beratung GMBH' specifically.

**Content:**
```
\bWiederspan\s+Beratung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1571 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_25`)


Unter Punkt „Küche“ wurde zunächst ausgeführt, dass zwei Rechnungen der „Wiederspan Beratung GMBH“  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Wiederspan Beratung GMBH` | `Wiederspan Beratung GMBH` |

</details>

---

## `Specific Entity: Mur Alver OG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Mur Alver OG' specifically.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1570 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_26`)


keine Leistungsbeschreibung enthalte und nicht der Bf als Empfänger aufscheine und eine  Rechnung der „Mur Alver OG“ Leuchten aus dem Luxussegment anführe.

| Predicted | Gold |
|---|---|
| `Mur Alver OG` | `Mur Alver OG` |

</details>

---

## `Specific Entity: Tritri-IT`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Tritri-IT' specifically, handling cases where it is followed by a hyphenated suffix like '-Konzernes'.

**Content:**
```
\bTritri-IT(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1392 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_348`)


(Der Vollständigkeit halber  wird angemerkt, dass damals alle Beschwerden des Tritri-IT -Konzernes durch denselben  Richter beim BFG entschieden wurden).

| Predicted | Gold |
|---|---|
| `Tritri-IT` | `Tritri-IT` |

</details>

---

## `Specific Entity: Landespolizeidirketion Tirol`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirketion Tirol' specifically, handling the typo 'direktion' found in training data.

**Content:**
```
\bLandespolizeidirketion\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 424 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149316.1`) ( sent_id: `findok-manually-annotated_TRAIN/149316.1_6`)


Mit Verständigungen gem. § 82 Abs. 9 KFG 1967 wurde durch die Landespolizeidirketion  Tirol an die Finanzpolizei mitgeteilt, dass im Zuge von Kontrollen festgestellt werden konnte,  dass die Beschwerdeführerin gemeinsam mit ihrem Ehemann und ebenso deren gemeinsame  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Landespolizeidirketion  Tirol` | `Landespolizeidirketion  Tirol` |

</details>

---

## `Specific Entity: Musikhochschule Wien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Musikhochschule Wien' specifically.

**Content:**
```
\bMusikhochschule\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1160 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

| Predicted | Gold |
|---|---|
| `Musikhochschule Wien` | `Musikhochschule Wien` |

</details>

---

## `Specific Entity: Konservatorium der Stadt Wien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Konservatorium der Stadt Wien' specifically.

**Content:**
```
\bKonservatorium\s+der\s+Stadt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1160 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

| Predicted | Gold |
|---|---|
| `Konservatorium  der Stadt Wien` | `Konservatorium  der Stadt Wien` |

</details>

---

## `Specific Entity: Wiener Philharmoniker`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Wiener Philharmoniker' specifically.

**Content:**
```
\bWiener\s+Philharmoniker\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1147 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_153`)


An der in diesen beiden Erkenntnis zum Ausdruck gebrachten Rechtsansicht hat der  Verwaltungsgerichtshof in seinem einen Berufsmusiker und Mitglied der Wiener  Philharmoniker betreffenden, Erkenntnis vom 21. September 2005, 2001/13/0241,  festgehalten und sie vertieft.

| Predicted | Gold |
|---|---|
| `Wiener  Philharmoniker` | `Wiener  Philharmoniker` |

</details>

---

## `Specific Entity: UFS/BFG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the combined acronym 'UFS/BFG' as a single organization entity.

**Content:**
```
\bUFS/BFG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 102 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_94`)


Obwohl sich im  weiteren Verfahren (beim UFS/BFG) herausstellte, dass dies sogenannte „Nichtbescheide“  waren, ist die Erlassung dieser Schriftstücke nach Rechtsansicht des BFG trotzdem als nach  außen gerichtete Amtshandlung zu werten.

| Predicted | Gold |
|---|---|
| `UFS/BFG` | `UFS/BFG` |

</details>

---

## `Specific Entity: How to spend it Verlag GmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'How to spend it Verlag GmbH' specifically, handling the English phrase within the German legal context.

**Content:**
```
\bHow\s+to\s+spend\s+it\s+Verlag\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 100 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_134`)


*** „How to spend it Verlag GmbH u. Mitges.“: € 613,72  Beteiligung INET II: € -2.235,63 (aufgrund des rechtskräftigem BFG-Erkenntnisses  RV/7102483/2013 vom 27.5.2022 bzw. BP-Bericht vom 29.22.2010 (ABNr.: 121095/09) zur  St.nr.

| Predicted | Gold |
|---|---|
| `How to spend it Verlag GmbH` | `How to spend it Verlag GmbH` |

</details>

---

## `Specific Entity: Garanta VersicherungsAG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Garanta VersicherungsAG' specifically.

**Content:**
```
\bGaranta\s+VersicherungsAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 211 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_56`)


Dem Vorlageantrag beigelegt wurden eine Versicherungsbestätigung zur Mobilitätsgarantie  der Garanta VersicherungsAG (undatiert) für den Zeitraum 26.08.2011 bis 25.08.2012 für die  Beschwerdeführerin, eine Wartungsliste vom 26.08.2011 für das Auto der Beschwerdeführerin  und eine englische Bestätigung des The International Sivananda Yoga Vedanta Centre in  Canada vom 24.05.2003, in der die Beschwerdeführerin als Teacher of Yoga bezeichnet wird.

| Predicted | Gold |
|---|---|
| `Garanta VersicherungsAG` | `Garanta VersicherungsAG` |

</details>

---

## `Specific Entity: The International Sivananda Yoga Vedanta Centre`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'The International Sivananda Yoga Vedanta Centre' specifically.

**Content:**
```
\bThe\s+International\s+Sivananda\s+Yoga\s+Vedanta\s+Centre\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 211 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_56`)


Dem Vorlageantrag beigelegt wurden eine Versicherungsbestätigung zur Mobilitätsgarantie  der Garanta VersicherungsAG (undatiert) für den Zeitraum 26.08.2011 bis 25.08.2012 für die  Beschwerdeführerin, eine Wartungsliste vom 26.08.2011 für das Auto der Beschwerdeführerin  und eine englische Bestätigung des The International Sivananda Yoga Vedanta Centre in  Canada vom 24.05.2003, in der die Beschwerdeführerin als Teacher of Yoga bezeichnet wird.

| Predicted | Gold |
|---|---|
| `The International Sivananda Yoga Vedanta Centre` | `The International Sivananda Yoga Vedanta Centre` |

</details>

---

## `Specific Entity: DA Deutsche Allgemeine Versicherung AG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'DA Deutsche Allgemeine Versicherung AG' specifically.

**Content:**
```
\bDA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 202 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_113`)


Bis August 2006 hatte die  Beschwerdeführerin einen Audi A 3 (siehe Vorschreibung der Kraftfahrversicherung durch die  DA Deutsche Allgemeine Versicherung AG vom Jänner 2006).

| Predicted | Gold |
|---|---|
| `DA Deutsche Allgemeine Versicherung AG` | `DA Deutsche Allgemeine Versicherung AG` |

</details>

---

## `Specific Entity: Geschenkartikel GmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Geschenkartikel GmbH' specifically.

**Content:**
```
\bGeschenkartikel\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 200 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_211`)


Der Beschwerdeführerin wurde mit Vorhalt vom 13.11.2019 mitgeteilt, dass die dem BFG  vorliegenden Belegkopien nur teilweise lesbar sind und ein Nachweis an Aufwendungen für  Arbeitsmittel (ohne Massageliege) iHv € 1.213,81 vorliegt (Rechnung Geschenkartikel GmbH €  92,73;

| Predicted | Gold |
|---|---|
| `Geschenkartikel GmbH` | `Geschenkartikel GmbH` |

</details>

---

## `Specific Entity: AVED cosmetic`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'AVED cosmetic' specifically.

**Content:**
```
\bAVED\s+cosmetic\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 196 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_223`)


Trotz Aufforderung des Finanzamtes zur Vorlage des Zahlungsnachweises und nochmaligen  Vorhalt durch das Bundesfinanzgericht wurde ein Zahlungsnachweis der Kosten der Firma  AVED cosmetic iHv € 975,48 nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `AVED cosmetic` | `AVED cosmetic` |

</details>

---

## `Specific Entity: Yoga Vidya GmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Yoga Vidya GmbH' specifically.

**Content:**
```
\bYoga\s+Vidya\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 194 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_230`)


Bei den Einzelanwendungen handelt es sich laut der vorgelegten Abrechnung vom 19.10.2006  von der Yoga Vidya GmbH um jeweils eine Anwendung Abhyanga, Garshan, kleine Abhyanga,  Shiro- und Mukabhyanga, Jambeera Pindas Sveda, Upanasveda mit Lepa und Padabhyanga.

| Predicted | Gold |
|---|---|
| `Yoga Vidya GmbH` | `Yoga Vidya GmbH` |

</details>

---

## `Specific Entity: Hamburger Fern-Hochschule`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Hamburger Fern-Hochschule' specifically.

**Content:**
```
\bHamburger\s+Fern-Hochschule\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 633 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_16`)


 Studienerfolgsnachweis der Hamburger Fern-Hochschule betreffend den Studiengang  Betriebswirtschaft für HAK-Absolventen betreffend im Jahr 2021 absolvierte Prüfungen  vom 02.08.2021  3.

| Predicted | Gold |
|---|---|
| `Hamburger Fern-Hochschule` | `Hamburger Fern-Hochschule` |

</details>

---

## `Specific Entity: Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific law firm name 'Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH'.

**Content:**
```
\bTschurtschenthaler,\s*Walder,\s*Fister\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 276 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_2`)


Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Mag. Janosch Moehrle, Bakk. rer. nat., Neue Frauengasse 2, 3180 Hintereben, Österreich  vertreten durch Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH, Dr. Arthur Lemisch Platz 7, 9020 Klagenfurt, über die Beschwerde  vom 3. Juni 2022 gegen den Bescheid des Finanzamtes Österreich vom 4. Mai 2022 betreffend  Einkommensteuer 2020 (Steuernummer 71-848/5765) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH` | `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH` |

</details>

---

## `Specific Entity: Immobilienbüro Mandl`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Immobilienbüro Mandl' specifically.

**Content:**
```
\bImmobilienbüro\s+Mandl\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 273 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_58`)


Darüber hinaus seien die  vorliegenden Pläne keine amtlichen Pläne, sondern vom Immobilienbüro Mandl erstellte.

| Predicted | Gold |
|---|---|
| `Immobilienbüro Mandl` | `Immobilienbüro Mandl` |

</details>

---

## `Specific Entity: EASO`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the acronym 'EASO' (European Asylum Support Office) as an organization.

**Content:**
```
\bEASO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_62`)


Werbungskosten die in Zusammenhang mit Frontex, EASO, ... Einsätzen stehen, dürfen daher in  solchen Fällen nicht berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `EASO` | `EASO` |

</details>

---

## `Specific Entity: Eckhardt SteuerberatungsgmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Eckhardt SteuerberatungsgmbH' specifically as found in training data.

**Content:**
```
\bEckhardt\s+SteuerberatungsgmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 544 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149708.1`) ( sent_id: `findok-manually-annotated_TRAIN/149708.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht fasst durch die Richterin Mag. Lisa Fries in der Revisionssache  Donald Kurun, Röcklbrunnstraße 21, 5222 Valentinhaft, Österreich, vertreten durch Eckhardt SteuerberatungsgmbH, Hauptstraße 58,  7033 Pöttsching, über den Antrag der Revisionswerberin der Revision vom 13. November 2025  gegen das Erkenntnis des Bundesfinanzgerichtes vom 29. September 2025, RV/7103756/2024,  betreffend Abweisung einer Nachsicht, die aufschiebende Wirkung zuzuerkennen, den  Beschluss:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Eckhardt SteuerberatungsgmbH` | `Eckhardt SteuerberatungsgmbH` |

</details>

---

## `Specific Entity: HLF Krems/Donau`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'HLF Krems/Donau' for the higher technical school.

**Content:**
```
\bHLF\s+Krems/Donau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_28`)


Die Bf. bringt im Vorlageantrag, eingelangt beim Finanzamt am 23.03.2023, vor, dass ihre  Tochter T. am 30.05.2022 an der HLF Krems/Donau maturiert habe und damit in die alte  2 von 6 Seite 3 von 6

| Predicted | Gold |
|---|---|
| `HLF Krems/Donau` | `HLF Krems/Donau` |

</details>

---

## `Specific Entity: Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG', handling variable whitespace.

**Content:**
```
\bHallas\s+&\s+Partner\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1214 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Ferdinand Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt  Österreich) vom 31. Oktober 2017 betreffend Festsetzung eines Verspätungszuschlages  betreffend Einkommensteuer 2015 und 2016 und Umsatzsteuer 2015 und 2016,  Steuernummer 86-167/7419  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` | `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` |

</details>

---

## `Specific Entity: Grazer Treuhand Steuerberatung GmbH & Partner KG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Grazer Treuhand Steuerberatung GmbH & Partner KG' specifically.

**Content:**
```
\bGrazer\s+Treuhand\s+Steuerberatung\s+GmbH\s+&\s+Partner\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 438 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Maximilian Karrer  in der Beschwerdesache VetR Tosca Buecher,  Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich, vertreten durch Grazer Treuhand Steuerberatung GmbH & Partner KG,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 gegen den Bescheid des  Finanzamts Graz-Stadt vom 12.10.2016 betreffend Abweisung des Antrages gemäß § 299 BAO  vom 9.7.2015 auf Aufhebung des Einkommensteuerbescheides 2014 des Finanzamts Graz- Stadt vom 20.5.2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Grazer Treuhand Steuerberatung GmbH & Partner KG` | `Grazer Treuhand Steuerberatung GmbH & Partner KG` |

</details>

---

## `Specific Entity: UFS Salzburg`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'UFS Salzburg' specifically to prevent splitting into 'UFS' and 'Salzburg'.

**Content:**
```
\bUFS\s+Salzburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 16 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_98`)


Gegenteiliges ergibt sich auch nicht aus der von der  belangten Behörde in diesem Zusammenhang ins Treffen geführten Entscheidung des UFS  Salzburg vom 20.8.2013, RV/0389-S/13 (dort hatte der Berufungswerber die Verbuchung einer  von ihm auf Grund einer noch anhängigen VwGH-Beschwerde erwarteten Gutschrift, also  tatsächlich die Verbuchung einer zukünftigen Gutschrift beantragt).

| Predicted | Gold |
|---|---|
| `UFS  Salzburg` | `UFS  Salzburg` |

</details>

---

## `Specific Entity: Merkur Steuerberatung GmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Merkur Steuerberatung GmbH' specifically to cover the shorter variant not covered by the 'Treuhand' rule.

**Content:**
```
\bMerkur\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 12 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_113`)


Der Sicherstellungsauftrag vom 20.3.2024 und der Pfändungsbescheid  (Zahlungsverbot) vom 3.4.2024 hätten daher der Beschwerdeführerin z.Hd. der Merkur  Steuerberatung GmbH zugestellt werden müssen.

| Predicted | Gold |
|---|---|
| `Merkur  Steuerberatung GmbH` | `Merkur  Steuerberatung GmbH` |

</details>

---

## `Specific Entity: Steuerberater Metzler & Adelsberger OG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Steuerberater Metzler & Adelsberger OG' specifically as found in training data.

**Content:**
```
\bSteuerberater\s+Metzler\s+&\s+Adelsberger\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1574 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Steuerberater Metzler & Adelsberger OG` | `Steuerberater Metzler & Adelsberger OG` |

</details>

---

## `Specific Entity: InnMarine GMBH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'InnMarine GMBH' specifically.

**Content:**
```
\bInnMarine\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1224 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid von 3. Oktober 2018 wurde der Beschwerdeführer gemäß § 9a BAO für die  aushaftenden Abgabenschulden der InnMarine GMBH (Primärschuldnerin) im Ausmaß von  € 99.885,72 in Anspruch genommen.

| Predicted | Gold |
|---|---|
| `InnMarine GMBH` | `InnMarine GMBH` |

</details>

---

## `Specific Entity: Lenfeld/Leys/Sonderegger Rechtsanwälte`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Lenfeld/Leys/Sonderegger Rechtsanwälte' specifically, handling the slash-separated names.

**Content:**
```
\bLenfeld/Leys/Sonderegger\s+Rechtsanwälte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 65 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ashley Ditges  in der Beschwerdesache Willibald Urbanowicz,  Caritasstraße 286, 3920 Heinreichs, Österreich, vertreten durch Lenfeld/Leys/Sonderegger Rechtsanwälte, Malserstraße 19,  6500 Landeck, über die Beschwerde vom 14. Dezember 2023 gegen den Bescheid des  Finanzamtes Österreich vom 14. November 2023 betreffend Rückforderung von  Familienbeihilfe und Kinderabsetzbeträgen für die Monate Oktober 2021 bis Jänner 2022,  Steuernummer 83-447/1877,  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lenfeld/Leys/Sonderegger Rechtsanwälte` | `Lenfeld/Leys/Sonderegger Rechtsanwälte` |

</details>

---

## `Specific Entity: Universität Innsbruck`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Universität Innsbruck' specifically.

**Content:**
```
\bUniversität\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 63 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1_29`)


Nach dem Studienblatt der Universität Innsbruck inskribierte der Sohn im Wintersemester  2019/20 im Diplomstudium Rechtswissenschaften.

| Predicted | Gold |
|---|---|
| `Universität Innsbruck` | `Universität Innsbruck` |

</details>

---

## `Specific Entity: King's School`

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'King's School Worcester' specifically, handling context like 'King's School Worcester, Großbritannien'.

**Content:**
```
\bKing['\u00b4]s\s+School\s+Worcester\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 666 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_71`)


Diese Feststellung beruht auf folgenden Umständen:  Maximiliane Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der King's School Worcester,  Großbritannien.

| Predicted | Gold |
|---|---|
| `King's School Worcester` | `King's School Worcester` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_41`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

FP: `King´s School Worcester` (organisation)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

FP: `King's  School Worcester` (organisation)

**✅ Gold Entities:**
- `The King´s School Worcester` (organisation)
- `Maximiliane Sakschewsky, MA` (person)
- `The King's  School Worcester` (organisation)

</details>

---

## `Specific Entity: OECD`

**F1:** 0.001 | **Precision:** 0.200 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the acronym 'OECD' (Organisation for Economic Co-operation and Development) as an organization.

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.200 | 0.001 | 0.001 | 5 | 1 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 4 | 939 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_94`)


Die Zentralstelle kann den Beamten mit seiner Zustimmung  1. zu Ausbildungszwecken oder als Nationalen Experten zu einer Einrichtung, die im Rahmen  der europäischen Integration oder der OECD tätig ist, oder  2.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_107`)

**False Positives:**


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_107`)

**False Positives:**


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

</details>

---

## `Specific Entity: Amt für Betrugsbekämpfung`

**F1:** 0.001 | **Precision:** 0.067 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmt(?:es)?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.067 | 0.001 | 0.001 | 15 | 1 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 14 | 1263 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_22`)


Die belangte Behörde verweigere die Buchung der UVAs und NOVA- Meldungen mit dem Hinweis, dass man auf eine Aussage des Amtes für Betrugsbekämpfung  (ABB) warte.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_2`)

**False Positives:**


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_3`)

**False Positives:**


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_10`)

**False Positives:**


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)

**False Positives:**


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amt für Betrugsbekämpfung` (organisation)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_89`)

**False Positives:**


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_140`)

**False Positives:**


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Zollamt Österreich` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_2`)

**False Positives:**


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_3`)

**False Positives:**


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_10`)

**False Positives:**


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)

**False Positives:**


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amt für Betrugsbekämpfung` (organisation)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_89`)

**False Positives:**


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_140`)

**False Positives:**


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Zollamt Österreich` (organisation)

</details>

---

## `Specific Entity: Bahrdt Digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bahrdt Digital' specifically, handling context like 'Fa. Bahrdt Digital'.

**Content:**
```
(?:Fa\.?\s+)?Bahrdt\s+Digital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Wildorftra KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wildorftra KI GMBH' specifically.

**Content:**
```
\bWildorftra\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bruckmonwil Digital GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bruckmonwil Digital GMBH' specifically.

**Content:**
```
\bBruckmonwil\s+Digital\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Niederösterreichische Vorsorgekasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Niederösterreichische Vorsorgekasse' specifically.

**Content:**
```
\bNiederösterreichische\s+Vorsorgekasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Raiffeisenbank Mittleres Mostviertel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Mittleres Mostviertel' specifically.

**Content:**
```
\bRaiffeisenbank\s+Mittleres\s+Mostviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Hempel Heizung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hempel Heizung GMBH' specifically.

**Content:**
```
\bHempel\s+Heizung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Süd Nortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Süd Nortri' specifically to prevent 'Co' or other fragments from being matched as organizations.

**Content:**
```
\bSüd\s+Nortri\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Hülsebusch + Breithaupt Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hülsebusch + Breithaupt Versicherung' specifically to ensure the full name is captured before 'GmbH & Co KG'.

**Content:**
```
\bHülsebusch\s+\+\s+Breithaupt\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Enns Werkal GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Enns Werkal GMBH' specifically to ensure correct extraction in legal contexts.

**Content:**
```
\bEnns\s+Werkal\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Logal Gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Logal Gruppe' specifically.

**Content:**
```
\bLogal\s+Gruppe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Trafenfen Automotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Trafenfen Automotive' specifically to prevent partial matching.

**Content:**
```
\bTrafenfen\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Mur Ververzor Betriebe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mur Ververzor Betriebe' specifically.

**Content:**
```
\bMur\s+Ververzor\s+Betriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Naaß Elektro GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Naaß Elektro GMBH' specifically.

**Content:**
```
\bNaaß\s+Elektro\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Lexkel Vertrieb KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lexkel Vertrieb KG' specifically, including with a trailing period.

**Content:**
```
\bLexkel\s+Vertrieb\s+KG(?:\.)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Kornfelder Recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kornfelder Recycling' specifically.

**Content:**
```
\bKornfelder\s+Recycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Füchsl Touristik GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Füchsl Touristik GMBH' specifically.

**Content:**
```
\bFüchsl\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Buhrfeindt Lebensmittel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Buhrfeindt Lebensmittel GMBH' specifically.

**Content:**
```
\bBuhrfeindt\s+Lebensmittel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Finanzen Tradonnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzen Tradonnex' specifically.

**Content:**
```
\bFinanzen\s+Tradonnex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Hinklein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hinklein' specifically as an organization in legal contexts.

**Content:**
```
\bHinklein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Norconheim' specifically as an organization.

**Content:**
```
\bNorconheim\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Dongartcon-Landwirtschaft GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Dongartcon-Landwirtschaft GMBH' specifically to prevent partial matching by the general rule.

**Content:**
```
\bDongartcon\-Landwirtschaft\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Monlogtri-Analyse GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Monlogtri-Analyse GMBH' specifically to prevent partial matching by the general rule.

**Content:**
```
\bMonlogtri\-Analyse\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Botho Mikloweit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Botho Mikloweit' specifically as an organization (sole proprietorship context).

**Content:**
```
\bBotho\s+Mikloweit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Blazickova & Hepprich Energie AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Blazickova & Hepprich Energie AG' specifically to prevent partial matching.

**Content:**
```
\bBlazickova\s+&\s+Hepprich\s+Energie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Berend Energie AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Berend Energie AG' specifically to prevent partial matching.

**Content:**
```
\bBerend\s+Energie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Raiffeisenbank Hippach-Hart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Hippach-Hart' specifically.

**Content:**
```
\bRaiffeisenbank\s+Hippach-Hart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Raiffeisenbank genburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank genburg' specifically.

**Content:**
```
\bRaiffeisenbank\s+genburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Raiffeisenkasse Retz-Pulkautal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenkasse Retz-Pulkautal' specifically.

**Content:**
```
\bRaiffeisenkasse\s+Retz-Pulkautal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Obernöder+Küsbert Touristik GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Obernöder+Küsbert Touristik GMBH' specifically.

**Content:**
```
\bObernöder\+Küsbert\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Energie Synlexder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Energie Synlexder' specifically.

**Content:**
```
\bEnergie\s+Synlexder\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Aicher & Partner Steuerberater OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Aicher & Partner Steuerberater OG' specifically.

**Content:**
```
\bAicher\s+&\s+Partner\s+Steuerberater\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: MittelHeizung Werke AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'MittelHeizung Werke AG' specifically to handle the CamelCase and specific entity name found in training data.

**Content:**
```
\bMittelHeizung\s+Werke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Traun-Digital KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Traun-Digital KG' specifically, handling the hyphenated name and KG suffix.

**Content:**
```
\bTraun-Digital\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Mertznich Bau GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mertznich Bau GMBH' specifically as found in training data.

**Content:**
```
\bMertznich\s+Bau\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Gernot Hirschkorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gernot Hirschkorn' specifically as an organisation (sole proprietorship context).

**Content:**
```
\bGernot\s+Hirschkorn\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: ÖBUG Law Firm`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm name with quoted acronym, title, and long suffix, handling variable whitespace around the hyphen.

**Content:**
```
\b"\u00d6BUG"\s+DR\.\s+NIKOLAUS\s+Wirtschaftstreuhand\s+GmbH\s*-\s*Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Österreichische Gesellschaft für Europapolitik`

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

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: BM für Finanzen`

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

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: BKS Steuerberatung GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BKS Steuerberatung GmbH & Co KG' specifically to handle the complex suffix.

**Content:**
```
\bBKS\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: FH Kärnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FH Kärnten' specifically.

**Content:**
```
\bFH\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Karl-Franzens- Universität Graz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Karl-Franzens- Universität Graz' specifically, handling the hyphen and space.

**Content:**
```
\bKarl-Franzens-\s+Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Fachhochschule Kärnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fachhochschule Kärnten' specifically.

**Content:**
```
\bFachhochschule\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH' specifically, allowing for variable whitespace.

**Content:**
```
\bHuber\s+\s*Swoboda\s+\s*Oswald\s+\s*Aixberger\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: UnterRecycling Services GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'UnterRecycling Services GMBH' specifically to ensure exact capture without 'Firma' prefix.

**Content:**
```
\bUnterRecycling\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: London Film Academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and the typo 'London Film Acadamy'.

**Content:**
```
\bLondon\s+Film\s+Acad[ae]my\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bundeskanzleramtes`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramtes' (genitive form) and 'Bundeskanzleramt' (nominative).

**Content:**
```
\bBundeskanzleramt(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: SVS/SVB`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the combined acronym 'SVS/SVB' (Sozialversicherung der Selbständigen / Sozialversicherung der Bauern) as an organization.

**Content:**
```
\bSVS/SVB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: PSD Wien Ambulatorium Landstraße`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'PSD Wien Ambulatorium Landstraße'. Priority increased to 11 to ensure it matches before the shorter 'PSD Wien' rule.

**Content:**
```
\bPSD\s+Wien\s+Ambulatorium\s+Landstraße\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Sozialversicherungsanstalt der Bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherungsanstalt der Bauern' and 'Sozialversicherung der Bauern' (with or without 'anstalt').

**Content:**
```
\bSozialversicherung(?:sanstalt)?\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 695 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_200`)

**False Positives:**


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated_TRAIN/149834.1_200`)

**False Positives:**


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

</details>

---

## `Specific Entity: PSD Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'PSD Wien' specifically.

**Content:**
```
\bPSD\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Psychiatrie Otto Wagner Spital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Psychiatrie Otto Wagner Spital' and its truncated form 'Psychiatrie Otto Wagner Spital-'.

**Content:**
```
\bPsychiatrie\s+Otto\s+Wagner\s+Spital(?:-)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bundesfinanzgericht (BFG)`

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

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Saxinger Chalupsky & Partner Rechtsanwälte GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm name 'Saxinger Chalupsky & Partner Rechtsanwälte GmbH'.

**Content:**
```
\bSaxinger\s+Chalupsky\s+&\s+Partner\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Imre & Schaffer Rechtsanwälte OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm name 'Imre & Schaffer Rechtsanwälte OG'.

**Content:**
```
\bImre\s+&\s+Schaffer\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Talwerk Logistik Holding GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name 'Talwerk Logistik Holding GMBH' to prevent partial matching by general rules.

**Content:**
```
\bTalwerk\s+Logistik\s+Holding\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bersud Möbel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bersud Möbel GMBH' specifically to prevent partial matching.

**Content:**
```
\bBersud\s+M\u00f6bel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Unter Heimdorf GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Unter Heimdorf GMBH' specifically to prevent partial matching.

**Content:**
```
\bUnter\s+Heimdorf\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: LG für ZRS Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LG für ZRS Wien' specifically, handling the abbreviation and preposition structure found in legal texts.

**Content:**
```
\bLG\s+für\s+ZRS\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Paugger Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Paugger Steuerberatung GmbH' specifically.

**Content:**
```
\bPaugger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Landesregierung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Landesregierung' followed by state names.

**Content:**
```
\bLandesregierung\s+(?:Nieder\u00f6sterreich|Ober\u00f6sterreich|Steiermark|K\u00e4rnten|Salzburg|Tirol|Vorarlberg|Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: B-GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'B-GmbH' specifically as found in training data.

**Content:**
```
\bB-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: A-GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'A-GmbH' specifically as found in training data.

**Content:**
```
\bA-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Hausverwaltung-GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hausverwaltung-GmbH' specifically.

**Content:**
```
\bHausverwaltung-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: LG Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LG Innsbruck' specifically, as the general court rule does not cover 'LG' abbreviations.

**Content:**
```
\bLG\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bezirksgericht Silz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht Silz' specifically to ensure consistent extraction and priority over general patterns.

**Content:**
```
\bBezirksgericht\s+Silz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Raiffeisenbank Stallhofen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Stallhofen' specifically.

**Content:**
```
\bRaiffeisenbank\s+Stallhofen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Mittel Unisyn GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mittel Unisyn GMBH' specifically.

**Content:**
```
\bMittel\s+Unisyn\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Ober Lemostnor AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Ober Lemostnor AG' specifically.

**Content:**
```
\bOber\s+Lemostnor\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Vennes Recycling AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Vennes Recycling AG' specifically.

**Content:**
```
\bVennes\s+Recycling\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Unter Donunisee AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Unter Donunisee AG' specifically to capture this employer entity.

**Content:**
```
\bUnter\s+Donunisee\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bärs & Walterscheidt Handel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bärs & Walterscheidt Handel GMBH' specifically as found in training data.

**Content:**
```
\bBärs\s+&\s+Walterscheidt\s+Handel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `General Organisation Pattern: Name + Beratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Beratung', capturing the full name including 'Beratung'. Tightened to require a preceding proper noun pattern.

**Content:**
```
\b([A-Z][a-zA-Z\u00C0-\u00FF]+(?:\s+[A-Z][a-zA-Z\u00C0-\u00FF]+)*)\s+Beratung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1572 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_25`)

**False Positives:**


Unter Punkt „Küche“ wurde zunächst ausgeführt, dass zwei Rechnungen der „Wiederspan Beratung GMBH“  2 von 7 Seite 3 von 7

FP: `Wiederspan Beratung` (organisation)

**✅ Gold Entities:**
- `Wiederspan Beratung GMBH` (organisation)

</details>

---

## `Specific Entity: Sozialversicherung Variations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherung' and 'Sozialversicherungsanstalt' with 'der Bauern' or 'der Selbständigen' variations.

**Content:**
```
\bSozialversicherung(?:sanstalt)?\s+(?:der\s+Bauern|der\s+Selbst\u00e4ndigen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 695 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_200`)

**False Positives:**


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated_TRAIN/149834.1_200`)

**False Positives:**


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

</details>

---

## `Specific Entity: BFG, Außenstelle Linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BFG, Außenstelle Linz' to prevent splitting into 'BFG' and 'Außenstelle Linz'.

**Content:**
```
\bBFG,\s+Außenstelle\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1483 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)

**False Positives:**


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

FP: `BFG, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)
- `UFS` (organisation)

</details>

---

## `Specific Entity: Bundesfinanzgericht, Außenstelle Linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht, Außenstelle Linz' and its genitive form 'Bundesfinanzgerichts, Außenstelle Linz'.

**Content:**
```
\bBundesfinanzgericht(?:s)?,\s+Außenstelle\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 1476 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)

**False Positives:**


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

FP: `Bundesfinanzgerichts, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)

**False Positives:**


85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.

FP: `Bundesfinanzgerichts, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `85-900/3590` (tax_number)
- `Roelfsen Versicherung` (organisation)
- `UFS` (organisation)
- `Houdek Maschinenbau` (organisation)

</details>

---

## `Specific Entity: BFG (Außenstelle Linz)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BFG (Außenstelle Linz)' specifically to capture the acronym with location in parentheses.

**Content:**
```
\bBFG\s*\(\s*Außenstelle\s+Linz\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bundesministers für Arbeit, Soziales und Konsumentenschutz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz' (genitive) and 'Bundesminister für Arbeit, Soziales und Konsumentenschutz' (nominative).

**Content:**
```
\bBundes(?:minister(?:s)?|in(?:\s+f\u00fcr)?)\s+f\u00fcr\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
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

