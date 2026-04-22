# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-22T10:39:11.091627

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
| Test documents | 56 |
| Train sentences | 2327 |
| Validation sentences | 218 |
| Test sentences | 6566 |
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
| Accuracy (exact match) | 91.1% |
| True Positives | 540 |
| False Positives | 414 |
| Micro Precision | 56.6% |
| Micro Recall | 59.0% |
| Micro F1 | 57.8% |
| Macro F1 | 57.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Specific Entity: KQPC Versand GMBH` | 4.3% | 100.0% | 2.2% | 20 | 20 | 0 |
| `Specific Entity: Event Sudkraftlex GMBH` | 4.3% | 100.0% | 2.2% | 20 | 20 | 0 |
| `Specific Entity: Sudver Handel Services GMBH` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Specific Entity: Glanznorost Institut GMBH` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Specific Entity: ÖGK` | 8.4% | 100.0% | 4.4% | 40 | 40 | 0 |
| `Specific Entity: Landespolizeidirektion Wien` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Specific Entity: Wirtschaftsuniversität Wien` | 1.7% | 100.0% | 0.9% | 8 | 8 | 0 |
| `Specific Entity: FAÖ` | 4.3% | 100.0% | 2.2% | 20 | 20 | 0 |
| `Specific Entity: Deloitte Tax Wirtschaftsprüfungs GmbH` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Specific Entity: Universität Wien` | 3.9% | 100.0% | 2.0% | 18 | 18 | 0 |
| `Specific Entity: Finanzamt Consolidated` | 1.7% | 100.0% | 0.9% | 8 | 8 | 0 |
| `Specific Entity: Mag. Ghesla Steuerberater GmbH` | 0.4% | 100.0% | 0.2% | 2 | 2 | 0 |
| `Specific Entity: Bundesministerium` | 0.9% | 100.0% | 0.4% | 4 | 4 | 0 |
| `German Tax Authority Consolidated` | 3.4% | 100.0% | 1.7% | 16 | 16 | 0 |
| `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)` | 9.8% | 75.0% | 5.2% | 64 | 48 | 16 |
| `Specific Entity: BMF` | 0.9% | 66.7% | 0.4% | 6 | 4 | 2 |
| `Specific Entity: Verwaltungsgerichtshof` | 21.6% | 50.0% | 13.8% | 252 | 126 | 126 |
| `Specific Entity: Verfassungsgerichtshof` | 0.9% | 50.0% | 0.4% | 8 | 4 | 4 |
| `Specific Entity: Magistrat der Stadt Wien` | 2.1% | 50.0% | 1.1% | 20 | 10 | 10 |
| `Specific Entity: VfGH` | 1.1% | 50.0% | 0.5% | 10 | 5 | 5 |
| `Specific Entity: Bundesfinanzgericht` | 27.4% | 49.7% | 18.9% | 348 | 173 | 175 |
| `Specific Entity: VwGH` | 21.4% | 41.8% | 14.4% | 316 | 132 | 184 |
| `Specific Entity: Pensionsversicherungsanstalt` | 0.4% | 25.0% | 0.2% | 8 | 2 | 6 |
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
| `Specific Entity: Missing Known Organizations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Buhrfeindt Lebensmittel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Finanzen Tradonnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Wiederspan Beratung GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Mur Alver OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hinklein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Tritri-IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Dongartcon-Landwirtschaft GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Monlogtri-Analyse GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Botho Mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Blazickova & Hepprich Energie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Berend Energie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bankhaus Denzel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Cervenka&Neunübel Telekom AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Specific Entity: AMS` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundesamt für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Landespolizeidirketion Tirol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Musikhochschule Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Konservatorium der Stadt Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Wiener Philharmoniker` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: ÖBUG Law Firm` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Österreichische Gesellschaft für Europapolitik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: INET Internet Service GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: UFS` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `Specific Entity: INET System Informations GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: UFS/BFG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: How to spend it Verlag GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BKS Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: FH Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Karl-Franzens- Universität Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Fachhochschule Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: UnterRecycling Services GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: London Film Academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundeskanzleramtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: PVA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Specific Entity: Garanta VersicherungsAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: The International Sivananda Yoga Vedanta Centre` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: DA Deutsche Allgemeine Versicherung AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Geschenkartikel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: AVED cosmetic` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Yoga Vidya GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hamburger Fern-Hochschule` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Johannes Kepler Universität Linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: WU Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Universität St. Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Immobilienbüro Mandl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Magistrat der Stadt Klagenfurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Berwaldkel-Möbel AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Amt für Betrugsbekämpfung` | 0.0% | 0.0% | 0.0% | 14 | 0 | 14 |
| `Specific Entity: FAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: LG für ZRS Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Schule für allgemeine Gesundheits- und Krankenpflege` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BM für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Kriminalpolizei in Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: EASO` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BMI` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Flughafen München` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: OECD` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `General Court Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Eckhardt SteuerberatungsgmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: HLF Krems/Donau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Höhere Lehranstalt für Tourismus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Paugger Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Landesregierung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: King's School` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: The King's School Worcester` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: University of Bristol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: England` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Grazer Treuhand Steuerberatung GmbH & Partner KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Rhein Normonkel Manufaktur GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Merkur Treuhand Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Schabetsberger Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: UFS Salzburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Merkur Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Steuerberater Metzler & Adelsberger OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: B-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: A-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Hausverwaltung-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bezirkshauptmannschaft Bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: ÖBB` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: SeneCura Variations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: LG Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bezirksgericht Silz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Raiffeisenbank Stallhofen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Mittel Unisyn GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Ober Lemostnor AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Vennes Recycling AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: InnMarine GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Lenfeld/Leys/Sonderegger Rechtsanwälte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Universität Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Unter Donunisee AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Raiffeisenbank Karnische Rion Bankstelle St.Stefan` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: X GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bärs & Walterscheidt Handel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `General Organisation Pattern: Name + Beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Sozialversicherung Variations` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Specific Entity: FA Wien Variations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Retail Chains` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BFG, Außenstelle Linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundesfinanzgericht, Außenstelle Linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BFG (Außenstelle Linz)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: R GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundesamtes für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Specific Entity: ÖGK`

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

## `Specific Entity: KQPC Versand GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches 'KQPC Versand GMBH' specifically.

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

## `Specific Entity: Event Sudkraftlex GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches 'Event Sudkraftlex GMBH' specifically.

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

## `Specific Entity: FAÖ`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAÖ' (Finanzamt Österreich) as an organization.

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

## `Specific Entity: Universität Wien`

**F1:** 0.039 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Universität Wien' specifically.

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

## `German Tax Authority Consolidated`

**F1:** 0.034 | **Precision:** 1.000 | **Recall:** 0.017  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' or 'FA' followed by known specific location patterns, excluding 'Österreich' as a standalone location.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Spittal\s+Villach|Graz-Stadt|Graz-\s+Stadt|Linz|Kirchdorf\s+Perg\s+Steyr|Wien\s+\d+(?:/\d+)*|Steiermark\s+Mitte|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Gmunden\s+V\u00f6cklabruck|Purkersdorf|Landeck\s+Reutte|Braunau\s+Ried\s+Sch\u00e4rding|Waldviertel|Salzburg-Stadt|Salzburg-Land|Oststeiermark|Innsbruck|Amstetten\s+Melk\s+Scheibbs|Nieder\u00f6sterreich\s+Mitte|Klosterneuburg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Baden\s+M\u00f6dling|Freistadt\s+Rohrbach\s+Urfahr|Judenburg\s+Liezen|Grieskirchen\s+Wels|Tirol\s+Ost|Neunkirchen\s+Wr\.?\s+Neustadt|Hollabrunn\s+Korneuburg\s+Tulln|Neunkirchen\s+(?:Wr\.?\s+|Wiener\s+)Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.017 | 0.034 | 16 | 16 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 0 | 900 |

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

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker,  Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend  Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

</details>

---

## `Specific Entity: Wirtschaftsuniversität Wien`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'Wirtschaftsuniversität Wien' and its abbreviation 'WU Wien', including the optional '(WU)' suffix.

**Content:**
```
\b(?:Wirtschaftsuniversit\u00e4t\s+Wien(?:\s*\(\s*WU\s*\))?|WU\s+Wien)\b
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

## `Specific Entity: Finanzamt Consolidated`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' or 'FA' followed by known location patterns, simplified and consolidated.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Spittal\s+Villach|Graz-Stadt|Linz|Kirchdorf\s+Perg\s+Steyr|Wien\s+\d+/\d+(?:/\d+)*\s+Klosterneuburg|Steiermark\s+Mitte|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Gmunden\s+V\u00f6cklabruck|Purkersdorf|Landeck\s+Reutte|Braunau\s+Ried\s+Sch\u00e4rding|Waldviertel|Salzburg-Stadt|Salzburg-Land|Oststeiermark|Innsbruck|Amstetten\s+Melk\s+Scheibbs|Nieder\u00f6sterreich\s+Mitte|Klosterneuburg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Baden\s+M\u00f6dling|Freistadt\s+Rohrbach\s+Urfahr|Judenburg\s+Liezen|Grieskirchen\s+Wels|Tirol\s+Ost|Oststeiermark|Neunkirchen\s+Wr\.?\s+Neustadt|Hollabrunn\s+Korneuburg\s+Tulln|Wien\s+\d+/\d+/\d+/\d+/\d+\s+Schwechat\s+Gerasdorf|Hollabrunn\s+Korneuburg\s+Tulln|Neunkirchen\s+(?:Wr\.?\s+|Wiener\s+)Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.017 | 8 | 8 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 908 |

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

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

</details>

---

## `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)`

**F1:** 0.098 | **Precision:** 0.750 | **Recall:** 0.052  

**Format:** `regex`  
**Description:**
Matches the full name 'Schweizerischen Unfallversicherungsanstalt (SUVA)' and the abbreviation 'SUVA' as a standalone organization. Prioritizes the full name match.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)\b|\bSUVA\b
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

## `Specific Entity: Verwaltungsgerichtshof`

**F1:** 0.216 | **Precision:** 0.500 | **Recall:** 0.138  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
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

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Specific Entity: VwGH`

**F1:** 0.214 | **Precision:** 0.418 | **Recall:** 0.144  

**Format:** `regex`  
**Description:**
Matches 'VwGH' standalone or as part of 'Verwaltungsgerichtshof (VwGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verwaltungsgerichtshof(?:es)?(?:\s*\(\s*VwGH\s*\))?|VwGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.418 | 0.144 | 0.214 | 316 | 132 | 184 | 11 | 173 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 132 | 184 | 782 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

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

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: Bundesfinanzgericht`

**F1:** 0.274 | **Precision:** 0.497 | **Recall:** 0.189  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive form 'Bundesfinanzgerichts', including with location suffixes or in genitive contexts.

**Content:**
```
\bBundesfinanzgericht(?:es)?(?:\s*\(\s*BFG\s*\)|,\s+Au\u00dfenstelle|\s+Innsbruck|\s+Linz|\s+Salzburg|\s+Wien|\s+des)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.497 | 0.189 | 0.274 | 348 | 173 | 175 | 1 | 174 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 173 | 175 | 743 |

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

## `Specific Entity: Amt für Betrugsbekämpfung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmt(?:es)?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 | 2 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 14 | 676 |

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
- `Amtes für Betrugsbekämpfung` — partial — pred ⊂ gold: `Amtes für Betrugsbekämpfung als Finanzstrafbehörde`

> partial: 1  |  missing annotation: 1

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

## `Specific Entity: Magistrat der Stadt Wien`

**F1:** 0.021 | **Precision:** 0.500 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien', 'Magistrates der Stadt Wien', and variations including 'MA 67' or 'Magistratsabteilung 67'.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s+(?:MA\s+\d+|Magistratsabteilung\s+\d+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.011 | 0.021 | 20 | 10 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 10 | 772 |

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

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


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

</details>

---

## `Specific Entity: UFS`

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

## `Specific Entity: Pensionsversicherungsanstalt`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt' specifically.

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

## `Specific Entity: VfGH`

**F1:** 0.011 | **Precision:** 0.500 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'VfGH' standalone or as part of 'Verfassungsgerichtshof (VfGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verfassungsgerichtshof(?:es)?(?:\s*\(\s*VfGH\s*\))?|VfGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.005 | 0.011 | 10 | 5 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 5 | 753 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) (sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


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

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

**False Positives:**

- `VfGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: Verfassungsgerichtshof`

**F1:** 0.009 | **Precision:** 0.500 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofes'.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
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

## `Specific Entity: BMF`

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Specific Entity: Bundesfinanzgericht`

**F1:** 0.274 | **Precision:** 0.497 | **Recall:** 0.189  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive form 'Bundesfinanzgerichts', including with location suffixes or in genitive contexts.

**Content:**
```
\bBundesfinanzgericht(?:es)?(?:\s*\(\s*BFG\s*\)|,\s+Au\u00dfenstelle|\s+Innsbruck|\s+Linz|\s+Salzburg|\s+Wien|\s+des)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.497 | 0.189 | 0.274 | 348 | 173 | 175 | 1 | 174 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 173 | 175 | 743 |

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

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_41`)


Daher stelle ich den Antrag auf Entscheidung über die Beschwerde (Vorlageantrag) durch das  Bundesfinanzgericht, ob als Grundlage der Berechnung der Wartezeit bis zur Wiedergewährung  der Familienbeihilfe nur jene Semester des Vorstudiums heranzuziehen sind, für die  Familienbeihilfe bezogen wurde oder alle Semester des Vorstudiums zugrunde zu legen sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_107`)


Im Erkenntnis vom BFG 15.05.2014, RV/7100395/2014 führte das Bundesfinanzgericht  auszugsweise aus:  „In § 2 Abs. 1 lit. b FLAG 1967 wird ausdrücklich darauf verwiesen, dass bei einem  Studienwechsel die in § 17 StudFG angeführten Regelungen auch für den Anspruch auf  9 von 11 Seite 10 von 11

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_114`)


Erwähnt sei auch, dass der von der Bf. zitierte Punkt 02.01.21.14 der Durchführungsrichtlinien  zum Familienlastenausgleichsgesetz 1967 - an die das Bundesfinanzgericht allerdings nicht  gebunden ist - nicht die Wartezeit, sondern die Voraussetzungen für einen schädlichen  Studienwechsel betrifft.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_124`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_15`)


Mit Schriftsatz vom 28. Mai 2019 beantragte der Bf die Entscheidung durch das  Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG, Niederau 25, 6731 Bühl, Österreich  tätig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_33`)


Beweiswürdigung  Der entscheidungswesentliche Sachverhalt ergibt sich aus dem dem Bundesfinanzgericht  elektronisch vorgelegten Akt, insbesondere aus den vom Bf eingebrachten Schriftsätzen und  den erlassenen Bescheiden, und ist unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 24** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_12`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf hat am 4.1.2024 einen Betrag von 3.141 Euro auf sein Abgabenkonto eingezahlt, ohne  den Betrag mit einer Zweckwidmung zu versehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 25** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_28`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 26** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 27** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_27`)


Das Bundesfinanzgericht geht davon aus, dass der Bescheid  jedenfalls noch im Jänner 2018 erlassen wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker,  Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend  Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 30** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 31** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 32** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_35`)


Betreffend Einkommensteuerbescheide 2010 und 2011:  Mit als Vorlageantrag zu wertendem Schreiben vom 28.09.2015 beantragte die Bf die Vorlage  der Beschwerden für die Jahre 2010 bis 2011 an das Bundesfinanzgericht zur Entscheidung.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 33** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_37`)


Mit Vorlagebericht vom 19.03.2019 wurden die Beschwerden dem Bundesfinanzgericht  übermittelt und beantragte die Behörde weiterhin die Abweisung der Beschwerde als  unbegründet.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_38`)


Mit 07.03.2022, somit bereits nach Vorlage der Beschwerde an das Bundesfinanzgericht, erließ  die belangte Behörde einen Berichtigungsbescheid gem. § 293 BAO zur  Beschwerdevorentscheidung vom 28.08.2015 für das Jahr 2011.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 35** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_40`)


Mit 01.07.2025 wurde die Beschwerde der nunmehr zuständigen Gerichtsabteilung des  Bundesfinanzgerichtes aufgrund einer Verfügung des Geschäftsverteilungsausschusses iZm der  Pensionierung der zuständigen Richterin zugeteilt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 36** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_41`)


Mit 14.08.2025 übermittelte das Bundesfinanzgericht der belangten Behörde einen Vorhalt zur  Aufklärung der Frage, weshalb (entgegen den Bestimmungen des § 300 BAO) mit 07.03.2022  zur Beschwerdevorentscheidung vom 28.08.2015 durch die belangte Behörde ein  Berichtigungsbescheid nach § 293 BAO erlassen worden war, obwohl die Beschwerde bereits  beim Bundesfinanzgericht anhängig war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 37** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Durch den oben angeführten (aufgrund der Korrektur der Lohnzettel) durch die belangte  Behörde erlassenen Berichtigungsbescheid nach § 293 BAO vom 07.03.2022 wurde dem  Begehren der Bf für das Jahr 2011 vollinhaltlich entsprochen, aufgrund der  Entscheidungssperre des § 300 BAO war der Bescheid jedoch als absolut nichtig zu werten und  somit die Beschwerdesache weiterhin als unerledigt anzusehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 38** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_52`)


Die Zuständigkeit in  gegenständlichem Beschwerdefall liegt daher weiterhin beim Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 39** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_65`)


Dies wird von der  belangten Behörde ebenfalls nicht bestritten und wird daher seitens des  Bundesfinanzgerichtes als gegeben angenommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 40** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_79`)


Aufgrund der beim Dienstgeber der Bf  durchgeführten GPLA den gegenständlichen Beschwerdezeitraum betreffend, werden die  Werte vom Bundesfinanzgericht als unstrittig angenommen und werden diese auch seitens der  belangten Behörde in der Vorhaltsbeantwortung vom 26.08.2025 als korrekt angesehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 41** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_80`)


Die obigen Sachverhaltsdarstellungen werden daher gem. § 167 Abs 2 BAO vom  Bundesfinanzgericht als erwiesen angenommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 42** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_83`)


(Eine Stornierung der  entsprechenden Guthabensbuchung erfolgt mit 27./28.11.2025 durch die belangte Behörde  aufgrund des Vorhaltes des Bundesfinanzgerichtes vom 26.11.2025.)   § 300 BAO sieht jedoch vor, dass ab Vorlage der Beschwerde die Abgabenbehörden beim  Verwaltungsgericht mit Bescheidbeschwerde angefochtene Bescheide und allfällige  Beschwerdevorentscheidungen bei sonstiger Nichtigkeit weder abändern noch aufheben  können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 43** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_86`)


Da diese Ausnahmevoraussetzungen in gegenständlichem Fall nicht gegeben sind, ist der durch  die belangte Behörde erlassene Bescheid absolut nichtig und liegt die Zuständigkeit in  gegenständlichem Beschwerdeverfahren weiterhin beim Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 44** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_100`)


Aufgrund des Verfahrensganges und insbesondere der Ausführungen der belangen Behörde im  Schreiben zur Vorhaltsbeantwortung vom 26.08.2025 geht das Bundesfinanzgericht nunmehr  davon aus, dass es unstrittig ist, dass die Grundregel des Art 15 Abs 1 und das damit  zusammenhängende Arbeitsortprinzip in gegenständlichem Fall zutreffend ist und Art 15 Abs 2  DBA nicht anzuwenden ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 45** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_105`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 46** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_106`)


Im vorliegenden Fall handelt es sich um keine Rechtfrage von grundsätzlicher Bedeutung, da  das Bundesfinanzgericht in rechtlicher Hinsicht der in der Entscheidung dargestellten Judikatur  des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 47** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 48** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_10`)


Der beschwerdeführenden Partei wurde gemäß § 85 Abs. 2 iVm § 2a BAO mit Beschluss des  Bundesfinanzgerichtes vom 5.5.2025 aufgetragen, den Mangel der fehlenden Unterschrift  binnen einer Woche ab Zustellung des Beschlusses nachzuholen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 49** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_36`)


Die Bescheidbeschwerde wurde am 14.4.2025 dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

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

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

**False Positives:**

- `Bundesfinanzgericht` — partial — pred ⊂ gold: `Bundesfinanzgericht (BFG)`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Bundesfinanzgericht (BFG)` (organisation)
- `FAÖ` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)


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

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_27`)


Das Bundesfinanzgericht geht davon aus, dass der Bescheid  jedenfalls noch im Jänner 2018 erlassen wurde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_1`)


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

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_24`)


Mit Eingabe vom 21. Mai 2024 beantragte der Bf. innerhalb verlängerter Frist die Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht sowie die Durchführung einer  mündlichen Verhandlung.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_26`)


Am 13. Juni 2024 legte die belangte Behörde die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_31`)


Am 1. Oktober 2025 fand die beantragte mündliche Verhandlung vor dem Bundesfinanzgericht  statt, in der insbesondere das Vorliegen bzw. Nichtvorliegen von triftigen medizinischen  Gründen diskutiert wurde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_36`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. bezieht im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_63`)


Das Bundesfinanzgericht kommt aus den nachstehenden Gründen im Rahmen der freien  Beweiswürdigung zum Ergebnis, dass die nach der höchstgerichtlichen Rechtsprechung  geforderten triftigen medizinischen Gründe nicht vorliegen:  Zunächst steht unstrittig fest, dass in keinem öffentlichen Krankenhaus eine Terminanfrage  betreffend die Bandscheibenoperation der Ehefrau des Bf. gestellt wurde (vgl. Protokoll zur  Verhandlung vom 1. Oktober 2025 sowie Befundberichte vom 6. und 8. Oktober 2025).

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  1.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Finanzstrafsenat Wien 2` (organisation)

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_102`)


das Bundesfinanzgericht ist vielmehr an diesen Schuldspruch gebunden (VwGH 29.6.1999,  98/14/0177;

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 23** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_183`)


Gemäß § 161 Abs. 1 FinStrG hat das Bundesfinanzgericht, sofern die Beschwerde nicht gemäß  § 156 mit Beschluss zurückzuweisen ist, grundsätzlich in der Sache selbst mit Erkenntnis zu  entscheiden.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 24** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


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

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_15`)


Mit Schriftsatz vom 28. Mai 2019 beantragte der Bf die Entscheidung durch das  Bundesfinanzgericht.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 26** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG, Niederau 25, 6731 Bühl, Österreich  tätig.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Nexkelkel AG` (organisation)
- `Niederau 25, 6731 Bühl, Österreich` (address)

**Example 27** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_33`)


Beweiswürdigung  Der entscheidungswesentliche Sachverhalt ergibt sich aus dem dem Bundesfinanzgericht  elektronisch vorgelegten Akt, insbesondere aus den vom Bf eingebrachten Schriftsätzen und  den erlassenen Bescheiden, und ist unstrittig.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 28** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 29** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_1`)


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

**Example 30** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `FAÖ` (organisation)

**Example 31** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 32** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_1`)


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

**Example 33** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_15`)


Mit Beschluss vom 26.8.2025 wies das Bundesfinanzgericht die Beschwerdeführerin darauf hin,  dass einerseits die angekündigte Begründung zur Beschwerde nie nachgereicht wurde und dass  andererseits bei der Festsetzung von Säumniszuschlägen kein Ermessen zu üben sei (VwGH  26.3.2025, Ra 2025/13/0016).

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 34** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_23`)


Zur Unzulässigkeit einer Revision   Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 35** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_1`)


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

**Example 36** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_51`)


Das FAÖ legte die Beschwerde am 4. März 2024 dem Bundesfinanzgericht vor und beantragte  die Abweisung der Beschwerde.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `FAÖ` (organisation)

**Example 37** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_68`)


Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Bundesministerium für Finanzen` (organisation)

**Example 38** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_90`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der BF war als Intermediär verpflichtet, bis zum 27. Juli 2023 eine Meldung nach dem EU-MPfG  abzugeben.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 39** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_128`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 40** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_1`)


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

**Example 41** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_10`)


Der beschwerdeführenden Partei wurde gemäß § 85 Abs. 2 iVm § 2a BAO mit Beschluss des  Bundesfinanzgerichtes vom 5.5.2025 aufgetragen, den Mangel der fehlenden Unterschrift  binnen einer Woche ab Zustellung des Beschlusses nachzuholen.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 42** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_36`)


Die Bescheidbeschwerde wurde am 14.4.2025 dem Bundesfinanzgericht zur Entscheidung  vorgelegt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 43** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_37`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 44** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_95`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 45** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149404.1_96`)


Im gegenständlichen Fall orientiert sich das Bundesfinanzgericht an der zitierten ständigen  Judikatur des Verwaltungsgerichtshofes, sodass keine Rechtsfrage von grundsätzlicher  Bedeutung zu klären war.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 46** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_1`)


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

**Example 47** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_9`)


Diese Beschwerde wurde vom Finanzamt mit dem Vermerk, dass sich das  Beschwerdevorbringen ausschließlich auf das Prinzip der Rechtsstaatlichkeit beziehe, ohne  Erlassung einer Beschwerdevorentscheidung gem. § 262 Abs. 3 BAO direkt dem  Bundesfinanzgericht vorgelegt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 48** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_10`)


Im Zuge eines Vorhalteverfahrens durch das Bundesfinanzgericht legte die Beschwerdeführerin  den Schriftverkehr mit der COFAG bzgl.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `COFAG` (organisation)

**Example 49** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_52`)


In Anbetracht dieser Ausführungen zeigt sich, dass die verfassungsrechtlichen Bedenken der  Beschwerdeführerin vom Bundesfinanzgericht nicht geteilt werden und musste daher der  Beschwerde der Erfolg versagt bleiben.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: Verwaltungsgerichtshof`

**F1:** 0.216 | **Precision:** 0.500 | **Recall:** 0.138  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
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

## `Specific Entity: VwGH`

**F1:** 0.214 | **Precision:** 0.418 | **Recall:** 0.144  

**Format:** `regex`  
**Description:**
Matches 'VwGH' standalone or as part of 'Verwaltungsgerichtshof (VwGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verwaltungsgerichtshof(?:es)?(?:\s*\(\s*VwGH\s*\))?|VwGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.418 | 0.144 | 0.214 | 316 | 132 | 184 | 11 | 173 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 132 | 184 | 782 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_118`)


Der Verwaltungsgerichtshof hat zum schädlichen und unschädlichen Studienwechsel folgende  Judikatur entwickelt:  Ein Studienwechsel iSd § 17 StudFG liegt vor, wenn der/die Studierende das von ihm/ihr  begonnene und bisher betriebene, aber noch nicht abgeschlossene Studium nicht mehr  fortsetzt und an dessen Stelle ein anderes unter den Geltungsbereich des StudFG fallendes  Studium beginnt (VwGH 26.05.2011, 2011/16/0060).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_146`)


Entgegen der Rechtsansicht des Bf, dass der erste tatsächliche Studienwechsel zum Studium  der biotechnischen Verfahren erfolgt ist, gilt auch der Rückwechsel vom Bachelorstudium  Wirtschaftsrecht auf das Studium Rechtswissenschaften nach der zitierten Judikatur des  Verwaltungsgerichtshofes (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_163`)


Subjektive  Momente, wie Verschulden an der (ursprünglichen oder weiteren) Auszahlung der  Familienleistungen, Gutgläubigkeit des Empfangs der Familienbeihilfe und des  Kinderabsetzbetrags oder die Verwendung der Familienbeihilfe und des Kinderabsetzbetrags,  sind nach ständiger Rechtsprechung des Verwaltungsgerichtshofes für die Verpflichtung zur  Rückerstattung unrechtmäßiger Beihilfenbezüge unerheblich.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_2`)


Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_124`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_125`)


Die Rechtsfolgen im beschwerdegegenständlichen Fall ergeben sich unmittelbar aus den  anzuwendenden, vom Wortlaut her eindeutigen gesetzlichen Bestimmungen und wurde im  Übrigen der ständigen Rechtsprechung des VwGH gefolgt.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_45`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes besteht keine Entscheidungspflicht  betreffend Anregung einer Wiederaufnahme des Verfahrens (VwGH 22.5.2014, 2011/15/0064,  VwGH 20.2.2019, Ro 2016/13/0011).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_63`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (vgl. VwGH 16.10.2016, Ra  2014/15/0058) ist bei einem Antrag auf Wiederaufnahme des Verfahrens das  Neuhervorkommen von Tatsachen aus Sicht des Antragstellers zu beurteilen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_70`)


Das Erkenntnis folgt der zitierten Rechtsprechung des Verwaltungsgerichtshofes und liegt  damit keine Rechtsfrage grundsätzlicher Bedeutung vor.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_28`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_73`)


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 24** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_4`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 25** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 26** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_3`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 27** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_105`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_106`)


Im vorliegenden Fall handelt es sich um keine Rechtfrage von grundsätzlicher Bedeutung, da  das Bundesfinanzgericht in rechtlicher Hinsicht der in der Entscheidung dargestellten Judikatur  des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 29** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_3`)


III. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 30** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_92`)


Laut Rechtsprechung des Verwaltungsgerichtshofes wird das  Rechtsschutzinteresse des Abgabepflichtigen dadurch nicht verletzt, weil gegen den Bescheid  betreffend Pfändung sowohl das Beschwerderecht als auch die Revision an den  Verwaltungsgerichtshof offensteht (VwGH 23.11.1994, 94/13/0246).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 31** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_95`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 32** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_96`)


Im gegenständlichen Fall orientiert sich das Bundesfinanzgericht an der zitierten ständigen  Judikatur des Verwaltungsgerichtshofes, sodass keine Rechtsfrage von grundsätzlicher  Bedeutung zu klären war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 33** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_4`)


II. Die Revision an den Verwaltungsgerichtshof ist gemäß Art 133 Abs 4 B-VG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 34** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_248`)


Zu alldem ist auf die Rechtsprechung des VwGH zu verweisen, wonach eine freie Auflösbarkeit  des Vertrags nur dann vorliegt, wenn eine Kündigung auch die tatsächliche Befreiung von den  Leistungsverpflichtungen für die Zeit nach der Vertragsauflösung bewirkt (vgl VwGH  16.10.2014, 2011/16/0169;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 35** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_324`)


Zu Spruchpunkt II. (Unzulässigkeit der Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

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

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_291`)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_294`)


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_291`)


Das Hauptgewicht der Behauptungs- und Beweislast liegt beim Nachsichtswerber (vgl. etwa  VwGH 20. November 2019, Ra 2018/15/0014 und VwGH 7. Juli 2011, 2008/15/0010).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) (sent_id: `findok-manually-annotated_TRAIN/149808.1_294`)


Für eine  Ermessenentscheidung bleibt daher kein Raum (vgl. VwGH 27. Juni 2013, 2013/15/0173).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_38`)


Für die Wirksamkeit einer Prozesserklärung ist das Erklärte maßgebend, nicht das Gewollte (vgl  zB VwGH vom 28.2.2008, 2006/16/0129).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_39`)


Das Erklärte ist allerdings der Auslegung zugänglich  (vgl. zB VwGH vom 29.7.2010, 2009/15/0152).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_41`)


hierbei kommt es  darauf an, wie die Erklärung unter Berücksichtigung der konkreten gesetzlichen Regelung, des  Verfahrenszweckes und der der Behörde vorliegenden Aktenlage objektiv verstanden werden  muss (zB VwGH vom 20.3.2014, 2010/15/0195, VwGH 30.1.2015, Ra 2014/17/0025)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_42`)


Ist der Inhalt eines Anbringens eindeutig, ist eine davon abweichende, nach außen auch  andeutungsweise nicht zum Ausdruck kommende Absicht des Einschreiters nicht maßgeblich  (vgl. zB VwGH vom 24.6.2009, 2007/15/0041)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_6`)


Gemäß Art. 133 Abs. 4 B-VG ist gegen dieses Erkenntnis eine ordentliche Revision an den  Verwaltungsgerichtshof durch die vor dem Bundesfinanzgericht belangte Behörde nicht  zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_73`)


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_107`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 23** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 24** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_14`)


3. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 25** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_97`)


Über die Beschwerde wurde erwogen:  Teilrechtskraft:  Laut ständiger Rechtsprechung des Verwaltungsgerichtshofes ist im Bereich des  Finanzstrafrechtes Teilrechtskraft hinsichtlich des Ausspruches von Schuld einerseits und Strafe  andererseits rechtlich möglich (vgl. VwGH 8.2.2007, 2006/15/0293).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 26** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_188`)


Zur subjektiven Tatseite ist zunächst auf die Rechtsprechung des Verwaltungsgerichtshofes zu  verweisen, wonach Vorsatz eine zielgerichtete subjektive Einstellung des Täters bedeutet, auf  deren Vorhandensein oder Nichtvorhandensein nur nach seinem nach außen in Erscheinung  tretenden Verhalten unter Würdigung aller sonstigen Sachverhaltselemente geschlossen  werden kann (VwGH 29.3.2007, 2006/16/0062).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 27** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_272`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 28** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 29** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_38`)


Für die Wirksamkeit einer Prozesserklärung ist das Erklärte maßgebend, nicht das Gewollte (vgl  zB VwGH vom 28.2.2008, 2006/16/0129).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 30** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_39`)


Das Erklärte ist allerdings der Auslegung zugänglich  (vgl. zB VwGH vom 29.7.2010, 2009/15/0152).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 31** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_41`)


hierbei kommt es  darauf an, wie die Erklärung unter Berücksichtigung der konkreten gesetzlichen Regelung, des  Verfahrenszweckes und der der Behörde vorliegenden Aktenlage objektiv verstanden werden  muss (zB VwGH vom 20.3.2014, 2010/15/0195, VwGH 30.1.2015, Ra 2014/17/0025)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 32** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_42`)


Ist der Inhalt eines Anbringens eindeutig, ist eine davon abweichende, nach außen auch  andeutungsweise nicht zum Ausdruck kommende Absicht des Einschreiters nicht maßgeblich  (vgl. zB VwGH vom 24.6.2009, 2007/15/0041)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 33** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_45`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes besteht keine Entscheidungspflicht  betreffend Anregung einer Wiederaufnahme des Verfahrens (VwGH 22.5.2014, 2011/15/0064,  VwGH 20.2.2019, Ro 2016/13/0011).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 34** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_63`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (vgl. VwGH 16.10.2016, Ra  2014/15/0058) ist bei einem Antrag auf Wiederaufnahme des Verfahrens das  Neuhervorkommen von Tatsachen aus Sicht des Antragstellers zu beurteilen.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 35** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 36** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_70`)


Das Erkenntnis folgt der zitierten Rechtsprechung des Verwaltungsgerichtshofes und liegt  damit keine Rechtsfrage grundsätzlicher Bedeutung vor.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 37** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_4`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 38** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 39** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_3`)


Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 40** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149322.1_23`)


Zur Unzulässigkeit einer Revision   Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 41** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_180`)


Zur gebührenrechtlich maßgeblichen Vertragsdauer  Nach ständiger Judikatur des Verwaltungsgerichtshofs ist für die Frage, ob gebührenrechtlich  ein Vertrag von bestimmter oder unbestimmter Dauer vorliegt, nicht die von den Parteien  gewählte Bezeichnung des Vertrags, sondern der gesamte Vertragsinhalt maßgebend (vgl etwa  VwGH 16.10.2014, 2011/16/0169;

**False Positives:**

- `Verwaltungsgerichtshof` — partial — pred ⊂ gold: `Verwaltungsgerichtshofs`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Verwaltungsgerichtshofs` (organisation)

**Example 42** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_263`)


Das von der  Beschwerdeführerin angeführte Erkenntnis des Verwaltungsgerichtshofs vom 2.7.1981,  15/0701/80, vermag somit ihren Standpunkt nicht zu unterstützen.

**False Positives:**

- `Verwaltungsgerichtshof` — partial — pred ⊂ gold: `Verwaltungsgerichtshofs`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Verwaltungsgerichtshofs` (organisation)

**Example 43** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_264`)


Vielmehr ist diesbezüglich auf das VwGH-Erkenntnis vom 24.3.1994, 93/16/0133, zu verweisen,  wonach, sofern dem Mieter ein jederzeitiges Kündigungsrecht zusteht, dieser jedoch im Fall  der Kündigung dem Vermieter eine „Pönale“ im Ausmaß des Mietzinses für eine festgelegte  Dauer zu entrichten hat, dem Vermieter jedenfalls das Mietentgelt für eine Bestanddauer von  dieser festgelegten Dauer gesichert ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 44** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_302`)


Maßgebend für die Festsetzung der Gebühren ist im  Sinne des § 17 Abs 1 GebG vielmehr der Inhalt der über das Rechtsgeschäft errichteten  Urkunde und damit das im konkreten Fall tatsächlich Vereinbarte (vgl VwGH 22.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 45** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_325`)


Die Lösung der gegenständlich aufgeworfenen Rechtsfragen gründet sich auf der  Rechtsprechung des Verwaltungsgerichtshofs.

**False Positives:**

- `Verwaltungsgerichtshof` — partial — pred ⊂ gold: `Verwaltungsgerichtshofs`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Verwaltungsgerichtshofs` (organisation)

**Example 46** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_11`)


Der Amtsrevision folgend hat der VwGH das Erkenntnis des Bundesfinanzgerichtes aufgehoben  (VwGH 20.11.2024, Ro 2024/13/0019).

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Bundesfinanzgerichtes` (organisation)

**Example 47** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_39`)


Die gegenständliche Rechtsfrage ist durch das VwGH-Erkenntnis Ro 2024/13/0019 vom  20.11.2024 geklärt.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 48** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_3`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof  nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 49** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_124`)


Da die versäumte Handlung im beschwerdegegenständlichen Fall nicht spätestens gleichzeitig  mit dem Antrag auf Wiedereinsetzung nachgeholt wurde, ist dieser Antrag im Einklang mit der  Rechtsprechung des Verwaltungsgerichtshofs zurückzuweisen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)`

**F1:** 0.098 | **Precision:** 0.750 | **Recall:** 0.052  

**Format:** `regex`  
**Description:**
Matches the full name 'Schweizerischen Unfallversicherungsanstalt (SUVA)' and the abbreviation 'SUVA' as a standalone organization. Prioritizes the full name match.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)\b|\bSUVA\b
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

## `Specific Entity: ÖGK`

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

## `Specific Entity: KQPC Versand GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches 'KQPC Versand GMBH' specifically.

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

## `Specific Entity: Event Sudkraftlex GMBH`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches 'Event Sudkraftlex GMBH' specifically.

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

## `Specific Entity: FAÖ`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAÖ' (Finanzamt Österreich) as an organization.

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

## `Specific Entity: Universität Wien`

**F1:** 0.039 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Universität Wien' specifically.

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

## `German Tax Authority Consolidated`

**F1:** 0.034 | **Precision:** 1.000 | **Recall:** 0.017  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' or 'FA' followed by known specific location patterns, excluding 'Österreich' as a standalone location.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Spittal\s+Villach|Graz-Stadt|Graz-\s+Stadt|Linz|Kirchdorf\s+Perg\s+Steyr|Wien\s+\d+(?:/\d+)*|Steiermark\s+Mitte|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Gmunden\s+V\u00f6cklabruck|Purkersdorf|Landeck\s+Reutte|Braunau\s+Ried\s+Sch\u00e4rding|Waldviertel|Salzburg-Stadt|Salzburg-Land|Oststeiermark|Innsbruck|Amstetten\s+Melk\s+Scheibbs|Nieder\u00f6sterreich\s+Mitte|Klosterneuburg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Baden\s+M\u00f6dling|Freistadt\s+Rohrbach\s+Urfahr|Judenburg\s+Liezen|Grieskirchen\s+Wels|Tirol\s+Ost|Neunkirchen\s+Wr\.?\s+Neustadt|Hollabrunn\s+Korneuburg\s+Tulln|Neunkirchen\s+(?:Wr\.?\s+|Wiener\s+)Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.017 | 0.034 | 16 | 16 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 0 | 900 |

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

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) (sent_id: `findok-manually-annotated_TRAIN/149809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker,  Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend  Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Zacharias Lüdike  in der Beschwerdesache Felix Stukenbröker,  Lenzenkreuzweg 29, 9232 Frög, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  14. Jänner 2016 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 10. Dezember 2015 betreffend  Haftungsbescheid / Sonstige 2015 Steuernummer 23-124/1598  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_15`)


Nach den im Zuge einer Vorprüfung für die Jahre 2007 bis 2010 und den  Umsatzsteuernachschauzeitraum 2011 und 2012 getroffenen Feststellungen des damals  zuständigen Finanzamt Wien 6/7/15 sei das Vermietungsobjekt keine Einkunftsquelle.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 6/7/15` | `Finanzamt Wien 6/7/15` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_15`)


Nach den im Zuge einer Vorprüfung für die Jahre 2007 bis 2010 und den  Umsatzsteuernachschauzeitraum 2011 und 2012 getroffenen Feststellungen des damals  zuständigen Finanzamt Wien 6/7/15 sei das Vermietungsobjekt keine Einkunftsquelle.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 6/7/15` | `Finanzamt Wien 6/7/15` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

</details>

---

## `Specific Entity: Magistrat der Stadt Wien`

**F1:** 0.021 | **Precision:** 0.500 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien', 'Magistrates der Stadt Wien', and variations including 'MA 67' or 'Magistratsabteilung 67'.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s+(?:MA\s+\d+|Magistratsabteilung\s+\d+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.011 | 0.021 | 20 | 10 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 10 | 772 |

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

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


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

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


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

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

## `Specific Entity: Wirtschaftsuniversität Wien`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'Wirtschaftsuniversität Wien' and its abbreviation 'WU Wien', including the optional '(WU)' suffix.

**Content:**
```
\b(?:Wirtschaftsuniversit\u00e4t\s+Wien(?:\s*\(\s*WU\s*\))?|WU\s+Wien)\b
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

## `Specific Entity: Finanzamt Consolidated`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' or 'FA' followed by known location patterns, simplified and consolidated.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Spittal\s+Villach|Graz-Stadt|Linz|Kirchdorf\s+Perg\s+Steyr|Wien\s+\d+/\d+(?:/\d+)*\s+Klosterneuburg|Steiermark\s+Mitte|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Gmunden\s+V\u00f6cklabruck|Purkersdorf|Landeck\s+Reutte|Braunau\s+Ried\s+Sch\u00e4rding|Waldviertel|Salzburg-Stadt|Salzburg-Land|Oststeiermark|Innsbruck|Amstetten\s+Melk\s+Scheibbs|Nieder\u00f6sterreich\s+Mitte|Klosterneuburg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Baden\s+M\u00f6dling|Freistadt\s+Rohrbach\s+Urfahr|Judenburg\s+Liezen|Grieskirchen\s+Wels|Tirol\s+Ost|Oststeiermark|Neunkirchen\s+Wr\.?\s+Neustadt|Hollabrunn\s+Korneuburg\s+Tulln|Wien\s+\d+/\d+/\d+/\d+/\d+\s+Schwechat\s+Gerasdorf|Hollabrunn\s+Korneuburg\s+Tulln|Neunkirchen\s+(?:Wr\.?\s+|Wiener\s+)Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.017 | 8 | 8 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 908 |

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

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

</details>

---

## `Specific Entity: VfGH`

**F1:** 0.011 | **Precision:** 0.500 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'VfGH' standalone or as part of 'Verfassungsgerichtshof (VfGH)', but NOT when followed by a date/citation pattern to avoid false positives in legal citations.

**Content:**
```
\b(?:Verfassungsgerichtshof(?:es)?(?:\s*\(\s*VfGH\s*\))?|VfGH)(?!\s*\d+\.\s*\d+\.\s*\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.500 | 0.005 | 0.011 | 10 | 5 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 5 | 753 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) (sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


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

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

**False Positives:**

- `VfGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: Bundesministerium`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium' and 'Bundesministerin' with optional genitive form and common department suffixes.

**Content:**
```
\bBundes(?:minister(?:ium|iums)?|in(?:\s+f\u00fcr)?)\s+f\u00fcr\s+(?:Finanzen|Inneres|Justiz|Arbeit,\s+Soziales\s+und\s+Konsumentenschutz|Bildung,\s+Kunst\s+und\s+Kultur)\b
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

## `Specific Entity: BMF`

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

## `Specific Entity: Verfassungsgerichtshof`

**F1:** 0.009 | **Precision:** 0.500 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofes'.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
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

## `Specific Entity: Sudver Handel Services GMBH`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Sudver Handel Services GMBH' specifically.

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

## `Specific Entity: Glanznorost Institut GMBH`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Glanznorost Institut GMBH' specifically.

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

## `Specific Entity: Landespolizeidirektion Wien`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirektion Wien' specifically.

**Content:**
```
\bLandespolizeidirektion\s+Wien\b
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

## `Specific Entity: Deloitte Tax Wirtschaftsprüfungs GmbH`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Deloitte Tax Wirtschaftsprüfungs GmbH' specifically, handling variable whitespace.

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

## `Specific Entity: Mag. Ghesla Steuerberater GmbH`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Mag. Ghesla Steuerberater GmbH' specifically as found in training data.

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

## `Specific Entity: Pensionsversicherungsanstalt`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt' specifically.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Missing Known Organizations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific organization names found in training data and failures, including BDO Austria, LeitnerLeitner, Lubomir Merschmeyer, and Betriebsprüfung GmbH.

**Content:**
```
\b(?:Schmeltz\s+Luftfahrt|Dorfcon\-Verlag|Houdek\s+Maschinenbau|Lexdon\s+IT|Roelfsen\s+Versicherung|FA\s+Wien\s+1/23|G\u00f6zc\u00fc\s+Getr\u00e4nke|Lubomir\s+Merschmeyer|BDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.|LeitnerLeitner\s+GmbH\s+Wirtschaftspr\u00fcfer\s+und\s+Steuerberater|Betriebspr\u00fcfung\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Wiederspan Beratung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wiederspan Beratung GMBH' specifically.

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

## `Specific Entity: Mur Alver OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mur Alver OG' specifically.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Tritri-IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Tritri-IT' specifically, handling cases where it is followed by a hyphenated suffix like '-Konzernes'.

**Content:**
```
\bTritri-IT(?![a-zA-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bankhaus Denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bankhaus Denzel' specifically.

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

## `Specific Entity: Cervenka&Neunübel Telekom AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Cervenka&Neunübel Telekom AG' specifically.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: AMS`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'AMS Österreich', 'Arbeitsmarktservice (AMS)', and the standalone acronym 'AMS' with correct priority to avoid partial matches.

**Content:**
```
\b(?:AMS\s+Österreich|Arbeitsmarktservice\s*\(\s*AMS\s*\)|(?<!\w)AMS(?!\s+Österreich|\s*\(\s*AMS))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bundesamt für Soziales und Behindertenwesen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its genitive form 'Bundesamts für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamts?\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Landespolizeidirketion Tirol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirketion Tirol' specifically, handling the typo 'direktion' found in training data.

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

## `Specific Entity: Musikhochschule Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Musikhochschule Wien' specifically.

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

## `Specific Entity: Konservatorium der Stadt Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Konservatorium der Stadt Wien' specifically.

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

## `Specific Entity: Wiener Philharmoniker`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wiener Philharmoniker' specifically.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: INET Internet Service GmbH`

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

## `Specific Entity: UFS`

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

## `Specific Entity: INET System Informations GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'INET System Informations GmbH' specifically, handling potential double spaces found in training data.

**Content:**
```
\bINET\s+(?:System\s+)?Informations\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: UFS/BFG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the combined acronym 'UFS/BFG' as a single organization entity.

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

## `Specific Entity: How to spend it Verlag GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'How to spend it Verlag GmbH' specifically, handling the English phrase within the German legal context.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: PVA`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'PVA' (Präventionsversicherung) as an organization.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Garanta VersicherungsAG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Garanta VersicherungsAG' specifically.

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

## `Specific Entity: The International Sivananda Yoga Vedanta Centre`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'The International Sivananda Yoga Vedanta Centre' specifically.

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

## `Specific Entity: DA Deutsche Allgemeine Versicherung AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DA Deutsche Allgemeine Versicherung AG' specifically.

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

## `Specific Entity: Geschenkartikel GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Geschenkartikel GmbH' specifically.

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

## `Specific Entity: AVED cosmetic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'AVED cosmetic' specifically.

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

## `Specific Entity: Yoga Vidya GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Yoga Vidya GmbH' specifically.

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

## `Specific Entity: Hamburger Fern-Hochschule`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hamburger Fern-Hochschule' specifically.

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

## `Specific Entity: Johannes Kepler Universität Linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Johannes Kepler Universität Linz' and its abbreviation 'JKU Linz' or 'JKU', including the optional '(JKU)' suffix.

**Content:**
```
\b(?:Johannes\s+Kepler\s+Universit\u00e4t\s+Linz(?:\s*\(\s*JKU\s*\))?|JKU\s+Linz|JKU)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: WU Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the standalone acronym 'WU' for Wirtschaftsuniversität Wien.

**Content:**
```
\bWU\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Universität St. Gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Universität St. Gallen' and 'Universität in St. Gallen' with flexible spacing, covering variations like 'Universität  in St. Gallen'.

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

## `Specific Entity: Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm name 'Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH'.

**Content:**
```
\bTschurtschenthaler,\s*Walder,\s*Fister\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Immobilienbüro Mandl`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Immobilienbüro Mandl' specifically.

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

## `Specific Entity: Magistrat der Stadt Klagenfurt`

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

## `Specific Entity: Berwaldkel-Möbel AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Berwaldkel-Möbel AG' specifically.

**Content:**
```
\bBerwaldkel-Möbel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Amt für Betrugsbekämpfung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmt(?:es)?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 | 2 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 14 | 676 |

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
- `Amtes für Betrugsbekämpfung` — partial — pred ⊂ gold: `Amtes für Betrugsbekämpfung als Finanzstrafbehörde`

> partial: 1  |  missing annotation: 1

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
- `Amtes für Betrugsbekämpfung` — partial — pred ⊂ gold: `Amtes für Betrugsbekämpfung als Finanzstrafbehörde`

> partial: 1  |  missing annotation: 1

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

## `Specific Entity: FAG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAG' (Finanzamt für Großbetriebe) as an organization.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Schule für allgemeine Gesundheits- und Krankenpflege`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific school name variations including 'Schule für allgemeine Gesundheits- und Krankenpflege Grillenreith', 'Schule für allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith', 'Schule für allgemeine Gesundheits- und Krankenpflege in Grillenreith', and 'Gesundheits- und Krankenpflege-Schule am LKH Grillenreith'.

**Content:**
```
\b(?:Schule\s+für\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+(?:am\s+LKH\s+|in\s+)?Grillenreith|Gesundheits\-\s+und\s+Krankenpflege\-Schule\s+am\s+LKH\s+Grillenreith)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Frontex' and 'Europäische Grenzschutzagentur Frontex' (and genitive 'Europäischen') as organizations.

**Content:**
```
\b(?:Europäischen?\s+Grenzschutzagentur\s+Frontex|Frontex)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: BM für Inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BM für Inneres' specifically.

**Content:**
```
\bBM\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Kriminalpolizei in Österreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kriminalpolizei in Österreich' specifically.

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

## `Specific Entity: EASO`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'EASO' (European Asylum Support Office) as an organization.

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

## `Specific Entity: BMI`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'BMI' (Bundesministerium für Inneres) as an organization.

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

## `Specific Entity: Flughafen München`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Flughafen München' specifically.

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

## `Specific Entity: OECD`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'OECD' (Organisation for Economic Co-operation and Development) as an organization.

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

## `General Court Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches common German court names with location suffixes, simplified pattern.

**Content:**
```
\b(?:Arbeits-\s+und\s+Sozialgericht|Bezirksgericht|Landesgericht|Oberlandesgericht|Bundesgerichtshof|Arbeitsgericht|Finanzgericht|Sozialgericht|Verwaltungsgericht)\s+[A-Z][a-zA-Z\u00C0-\u00FF]+(?:\s+[A-Z][a-zA-Z\u00C0-\u00FF]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Eckhardt SteuerberatungsgmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Eckhardt SteuerberatungsgmbH' specifically as found in training data.

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

## `Specific Entity: HLF Krems/Donau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'HLF Krems/Donau' for the higher technical school.

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

## `Specific Entity: Höhere Lehranstalt für Tourismus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name 'Höhere Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit' and its genitive form 'Höheren Lehranstalt...'.

**Content:**
```
\b(?:H\u00f6here|H\u00f6heren)\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG', handling variable whitespace.

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

## `Specific Entity: King's School`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'King's School Worcester' specifically, handling context like 'King's School Worcester, Großbritannien'.

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

## `Specific Entity: The King's School Worcester`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'The King's School Worcester' and 'The King´s School Worcester'.

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

## `Specific Entity: University of Bristol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'University of Bristol'.

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

## `Specific Entity: England`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'England' as an organization in this context (e.g., 'in England').

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

## `Specific Entity: Grazer Treuhand Steuerberatung GmbH & Partner KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Grazer Treuhand Steuerberatung GmbH & Partner KG' specifically.

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

## `Specific Entity: Rhein Normonkel Manufaktur GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Rhein Normonkel Manufaktur GMBH' specifically to ensure the full name is captured and not truncated by the general GMBH pattern.

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

## `Specific Entity: Merkur Treuhand Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Merkur Treuhand Steuerberatung GmbH' specifically, allowing for variable whitespace including newlines.

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

## `Specific Entity: Schabetsberger Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schabetsberger Steuerberatung GmbH' specifically.

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

## `Specific Entity: UFS Salzburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'UFS Salzburg' specifically to prevent splitting into 'UFS' and 'Salzburg'.

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

## `Specific Entity: Merkur Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Merkur Steuerberatung GmbH' specifically to cover the shorter variant not covered by the 'Treuhand' rule.

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

## `Specific Entity: Steuerberater Metzler & Adelsberger OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Steuerberater Metzler & Adelsberger OG' specifically as found in training data.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bezirkshauptmannschaft Bludenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirkshauptmannschaft Bludenz' specifically.

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

## `Specific Entity: ÖBB`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'ÖBB' (Österreichische Bundesbahnen) as an organization.

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

## `Specific Entity: SeneCura Variations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SeneCura', 'SENECURA', 'Senecura' and their full names with flexible spacing (e.g., 'Laurentius  Park').

**Content:**
```
\b(?:SENECURA|SeneCura|Senecura)(?:\s+(?:Laurentius\s+Park(?:\s+Bludenz)?|Laurentius\s+Park\s+Bludenz))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: InnMarine GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'InnMarine GMBH' specifically.

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

## `Specific Entity: Lenfeld/Leys/Sonderegger Rechtsanwälte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lenfeld/Leys/Sonderegger Rechtsanwälte' specifically, handling the slash-separated names.

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

## `Specific Entity: Universität Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Universität Innsbruck' specifically.

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Raiffeisenbank Karnische Rion Bankstelle St.Stefan`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Karnische Rion Bankstelle St.Stefan' specifically, handling the multi-word bank name.

**Content:**
```
\bRaiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: X GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'X GmbH' and 'X-GmbH' specifically to cover both space and hyphen variants found in training data, including variable whitespace.

**Content:**
```
\bX[-\s]+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

## `Specific Entity: FA Wien Variations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Wien' followed by various number patterns (e.g., 1/23, 2/20/21/22, etc.) to capture abbreviated tax authority forms.

**Content:**
```
\bFA\s+Wien\s+\d+(?:/\d+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Retail Chains`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches common retail organization names: Ikea, Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz, Quelle.at.

**Content:**
```
\b(?:Ikea|Obi|Leiner|M\u00f6belix|M\u00f6maX|Otto\.de|xxxLutz|Quelle\.at)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: R GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the placeholder organization 'R GmbH' found in training data and failures, handling variable whitespace.

**Content:**
```
\bR[-\s]+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

| Precision | Recall | F1 | Total Predicted | TP | FP | FP partial | FP missing annotation |
|---|---|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Bundesamtes für Soziales und Behindertenwesen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesamtes für Soziales und Behindertenwesen' (genitive) and 'Bundesamt für Soziales und Behindertenwesen' (nominative).

**Content:**
```
\bBundesamts?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
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

