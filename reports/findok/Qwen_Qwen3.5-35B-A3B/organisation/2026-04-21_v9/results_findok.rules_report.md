# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-22T10:25:20.238740

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
| Test documents | 10 |
| Train sentences | 2327 |
| Validation sentences | 218 |
| Test sentences | 892 |
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
| Accuracy (exact match) | 90.6% |
| True Positives | 55 |
| False Positives | 59 |
| Micro Precision | 48.2% |
| Micro Recall | 47.4% |
| Micro F1 | 47.8% |
| Macro F1 | 47.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Specific Entity: Landespolizeidirektion Wien` | 3.4% | 100.0% | 1.7% | 2 | 2 | 0 |
| `Specific Entity: Finanzamt Consolidated` | 3.4% | 100.0% | 1.7% | 2 | 2 | 0 |
| `German Tax Authority Consolidated` | 3.4% | 100.0% | 1.7% | 2 | 2 | 0 |
| `Specific Entity: Magistrat der Stadt Wien` | 12.3% | 57.1% | 6.9% | 14 | 8 | 6 |
| `Specific Entity: Verwaltungsgerichtshof` | 20.5% | 50.0% | 12.9% | 30 | 15 | 15 |
| `Specific Entity: Verfassungsgerichtshof` | 1.7% | 50.0% | 0.9% | 2 | 1 | 1 |
| `Specific Entity: VfGH` | 1.7% | 50.0% | 0.9% | 2 | 1 | 1 |
| `Specific Entity: Bundesfinanzgericht` | 29.3% | 50.0% | 20.7% | 48 | 24 | 24 |
| `Specific Entity: VwGH` | 23.1% | 45.0% | 15.5% | 40 | 18 | 22 |
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
| `Specific Entity: KQPC Versand GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Event Sudkraftlex GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Sudver Handel Services GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Glanznorost Institut GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Specific Entity: BMF` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: ÖGK` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Specific Entity: UFS` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Specific Entity: Sozialversicherungsanstalt der Bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Pensionsversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
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
| `Specific Entity: Wirtschaftsuniversität Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Johannes Kepler Universität Linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: WU Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Universität St. Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Immobilienbüro Mandl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Magistrat der Stadt Klagenfurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Berwaldkel-Möbel AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Amt für Betrugsbekämpfung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: FAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: FAÖ` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Deloitte Tax Wirtschaftsprüfungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: LG für ZRS Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Schule für allgemeine Gesundheits- und Krankenpflege` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BM für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Kriminalpolizei in Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: EASO` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: BMI` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Flughafen München` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: OECD` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `General Court Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Eckhardt SteuerberatungsgmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: HLF Krems/Donau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Höhere Lehranstalt für Tourismus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Universität Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Specific Entity: Mag. Ghesla Steuerberater GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: X GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bärs & Walterscheidt Handel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `General Organisation Pattern: Name + Beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Bundesministerium` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity: Sozialversicherung Variations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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

## `Specific Entity: Magistrat der Stadt Wien`

**F1:** 0.123 | **Precision:** 0.571 | **Recall:** 0.069  

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
| 0.571 | 0.069 | 0.123 | 14 | 8 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 6 | 60 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

</details>

---

## `Specific Entity: Bundesfinanzgericht`

**F1:** 0.293 | **Precision:** 0.500 | **Recall:** 0.207  

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
| 0.500 | 0.207 | 0.293 | 48 | 24 | 24 | 0 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 24 | 24 | 92 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Marion Bomarius  in der Beschwerdesache Norbert Ribarczik,  Zufahrt Felbermayr 68, 9241 Neudorf, Österreich, vertreten durch Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft,  Museumstraße 31a, 4020 Linz, über die Beschwerde vom 3. Jänner 2024 gegen den  Einkommensteuerbescheid des Finanzamtes Österreich vom 23. November 2023 betreffend  Berichtigung gem. § 293b BAO zu Bescheid vom 21.11.2023 Steuernummer 71-595/2950  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_29`)


Mit Schreiben vom 21.3.2024 beantragte der Vertreter des Bf gemäß § 264 BAO die Vorlage  und die Entscheidung durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer hat den Wohnsitz in Österreich.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_59`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsfeststellungen  gemäß § 167 BAO als erwiesen annehmen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Fürniß  in der Beschwerdesache PhD OMedR Ada Segert,  Gschlößlgasse 2, 5542 Flachau, Österreich, vertreten durch Vertreter, Adresse Vertreter, über die Säumnisbeschwerde der  beschwerdeführenden Partei vom 4. September 2025 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2023, Steuernummer xx-xxx/xxxx, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag.a Delia Fürniß` (person)
- `PhD OMedR Ada Segert` (person)
- `Gschlößlgasse 2, 5542 Flachau, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_4`)


Die gegenständliche Säumnisbeschwerde, welche ebenfalls von der steuerlichen Vertreterin  eingebracht wurde, langte beim Bundesfinanzgericht am 4. September 2025 ein.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_6`)


Das Finanzamt übersendete dem Bundesfinanzgericht am 17. Oktober 2025 den am  12. Dezember 2024 durch das Finanzamt Österreich erlassen Bescheid gemäß § 84 Abs. 1 BAO  betreffend die Ablehnung der steuerlichen Vertreterin sowie die Verständigung des Bf. über  die Ablehnung seiner steuerlichen Vertreterin mit selben Datum.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Finanzamt Österreich` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Univ.-Prof.in Eva Rauber` (person)
- `Henken` (organisation)
- `Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich` (address)
- `Finanzamt Schwechat Gerasdorf` (organisation)
- `69-427/7795` (tax_number)

</details>

---

## `Specific Entity: Verwaltungsgerichtshof`

**F1:** 0.205 | **Precision:** 0.500 | **Recall:** 0.129  

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
| 0.500 | 0.129 | 0.205 | 30 | 15 | 15 | 0 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 15 | 15 | 98 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_95`)


Im vorliegenden Fall ergeben sich die Rechtsfolgen unmittelbar aus dem Gesetz und der  einschlägigen Judikatur des Verwaltungsgerichtshofes, diese schlichte Rechtsanwendung  berührt keine Rechtsfrage von grundsätzlicher Bedeutung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz nicht  zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_23`)


Nach ständiger Judikatur des Verwaltungsgerichtshofes sind Ereignisse im Sinne des § 295a  BAO sachverhaltsändernde tatsächliche oder rechtliche Vorgänge, von denen sich - aus den die  steuerlich relevanten Tatbestände regelnden Abgabenvorschriften - eine abgabenrechtliche  Wirkung für bereits entstandene Abgabenansprüche ergibt (VwGH 1.9.2015, Ra 2015/15/0035  mwN).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_94`)


Die Unkenntnis ua. von straßenpolizeilichen Bestimmungen oder Parkgebührenvorschriften  stellt zufolge der Judikatur des Verwaltungsgerichtshofes zu § 5 Abs. 2 VStG 1991 keinen  entschuldigenden Rechtsirrtum dar, da von einem Kfz-Lenker verlangt werden kann und ihm  auch zumutbar ist, dass er sich hierzu ausreichend informiert (VwGH 4.8.2005, 2005/17/0056,  VwGH 26.2.2015, 2012/11/0243).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: VwGH`

**F1:** 0.231 | **Precision:** 0.450 | **Recall:** 0.155  

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
| 0.450 | 0.155 | 0.231 | 40 | 18 | 22 | 1 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 22 | 95 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_95`)


Im vorliegenden Fall ergeben sich die Rechtsfolgen unmittelbar aus dem Gesetz und der  einschlägigen Judikatur des Verwaltungsgerichtshofes, diese schlichte Rechtsanwendung  berührt keine Rechtsfrage von grundsätzlicher Bedeutung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_14`)


Wie der VwGH in seiner Entscheidung vom 15. Jänner 2008, 2007/15/0232 ausführt, ist die  Ablehnung eines unbefugten Vertreters diesem gegenüber bescheidmäßig zu verfügen.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_19`)


(vgl. auch VwGH 19. Oktober 2016, Ro 2014/15/0004)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_20`)


In seinem Erkenntnis vom 21. März 2019, Ra 2019/22/0004 hat der VwGH ausgeführt, dass das  verwaltungsgerichtliche Verfahren einerseits und das behördliche Verfahren andererseits eine  Einheit darstellen (vgl. auch VwGH 25. September 2018, Ra 2018/21/0069, Rn. 12f).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

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

## `Specific Entity: Pensionsversicherungsanstalt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 | 2 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 111 |

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

**F1:** 0.293 | **Precision:** 0.500 | **Recall:** 0.207  

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
| 0.500 | 0.207 | 0.293 | 48 | 24 | 24 | 0 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 24 | 24 | 92 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Marion Bomarius  in der Beschwerdesache Norbert Ribarczik,  Zufahrt Felbermayr 68, 9241 Neudorf, Österreich, vertreten durch Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft,  Museumstraße 31a, 4020 Linz, über die Beschwerde vom 3. Jänner 2024 gegen den  Einkommensteuerbescheid des Finanzamtes Österreich vom 23. November 2023 betreffend  Berichtigung gem. § 293b BAO zu Bescheid vom 21.11.2023 Steuernummer 71-595/2950  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_29`)


Mit Schreiben vom 21.3.2024 beantragte der Vertreter des Bf gemäß § 264 BAO die Vorlage  und die Entscheidung durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer hat den Wohnsitz in Österreich.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_59`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsfeststellungen  gemäß § 167 BAO als erwiesen annehmen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Reinhold Moellenkamp, Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_91`)


…“  5. Der eingebrachte Vorlageantrag vom 01.04.2020 wurde vom Finanzamt dem  Bundesfinanzgericht am 22.04.2020 zur Entscheidung vorgelegt (Vorlagebericht des  Finanzamtes vom 22.04.2020).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_93`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf. ist Schweizer Staatsbürgerin, hatte im Streitjahr 2019 in der Schweiz in ihrem  Elternhaus in Ort1 (CH)-Adr1 gemeinsam mit ihrer Mutter einen Wohnsitz und war im Jahr  2019 in der Schweiz als Lehrerin beschäftigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_131`)


Darüber hinaus gelangt das Bundesfinanzgericht aber auch zur Auffassung, dass sich in den die  NoVA und KfzSt betreffenden festsetzenden Zeiträumen (Juli bis Oktober 2019) die gegebenen  (Lebens-)Umstände der Bf. noch nicht derart verdichtet hatten, dass hinsichtlich des  Wohnsitzes in Ort1 (Ö) von einem Hauptwohnsitz der Bf. auszugehen wäre.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_139`)


Daraus ergibt sich für das Bundesfinanzgericht, dass die Bf. im Zeitpunkt der  erstmaligen Einbringung des gegenständlichen Kfz nach Österreich bzw. in den Zeiträumen, für  welche die NoVA (07/2019) und KfzSt (08 bis 10/2019) festgesetzt wurden, in Ort1 (Ö) (noch)  keinen Hauptwohnsitz hatte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Fürniß  in der Beschwerdesache PhD OMedR Ada Segert,  Gschlößlgasse 2, 5542 Flachau, Österreich, vertreten durch Vertreter, Adresse Vertreter, über die Säumnisbeschwerde der  beschwerdeführenden Partei vom 4. September 2025 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2023, Steuernummer xx-xxx/xxxx, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_4`)


Die gegenständliche Säumnisbeschwerde, welche ebenfalls von der steuerlichen Vertreterin  eingebracht wurde, langte beim Bundesfinanzgericht am 4. September 2025 ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_6`)


Das Finanzamt übersendete dem Bundesfinanzgericht am 17. Oktober 2025 den am  12. Dezember 2024 durch das Finanzamt Österreich erlassen Bescheid gemäß § 84 Abs. 1 BAO  betreffend die Ablehnung der steuerlichen Vertreterin sowie die Verständigung des Bf. über  die Ablehnung seiner steuerlichen Vertreterin mit selben Datum.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_55`)


Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 18. Juni 2025).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_74`)


Das Bundesfinanzgericht geht daher in freier Beweiswürdigung nach § 45 Abs. 2 AVG davon  aus, dass der Bf.das gegenständliche Fahrzeug am 28. Februar 2025 um 14:19 Uhr in 1230  Wien, Altmannsdorfer Straße nächst ONr. 164, nicht im Rahmen einer Paketzustellung,  sondern zum Einkauf im Supermarkt, am angeführten Ort ohne Entrichtung der  Parkometerabgabe abgestellt hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_109`)


Das Bundesfinanzgericht erachtet die von der belangten Behörde unter Beachtung der  Strafzumessungsgründe bei einem bis zu 365,00 Euro reichenden Strafrahmen mit 75,00 Euro  verhängte Geldstrafe und die für den Fall der Uneinbringlichkeit mit 17 Stunden festgesetzte  Ersatzfreiheitsstrafe als schuld- und tatangemessen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_121`)


Gemäß § 25 Abs. 2 BFGG hat das Bundesfinanzgericht, soweit dies nicht in der BAO, im ZollR- DG oder im FinStrG geregelt ist, in seiner Entscheidung zu bestimmen, welche  Abgabenbehörde oder Finanzstrafbehörde die Entscheidung zu vollstrecken hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_14`)


Die Beschwerdeführerin beantragte  am 16.9.2025 die Vorlage ihrer Beschwerde an das Bundesfinanzgericht und führte aus, es  seien 181 Tage bis zum 30.6. und sie habe mehr als das halbe Jahr allein mit ihren Kindern im  Haushalt gelebt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_15`)


Das Finanzamt legte die Beschwerde am 16.10.2025 dem Bundesfinanzgericht  vor und beantragte, sie abzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1.1. Zu Spruchpunkt I. (Abweisung)  § 295a BAO lautet: „(1)

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Fürniß  in der Beschwerdesache PhD OMedR Ada Segert,  Gschlößlgasse 2, 5542 Flachau, Österreich, vertreten durch Vertreter, Adresse Vertreter, über die Säumnisbeschwerde der  beschwerdeführenden Partei vom 4. September 2025 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2023, Steuernummer xx-xxx/xxxx, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag.a Delia Fürniß` (person)
- `PhD OMedR Ada Segert` (person)
- `Gschlößlgasse 2, 5542 Flachau, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_4`)


Die gegenständliche Säumnisbeschwerde, welche ebenfalls von der steuerlichen Vertreterin  eingebracht wurde, langte beim Bundesfinanzgericht am 4. September 2025 ein.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_6`)


Das Finanzamt übersendete dem Bundesfinanzgericht am 17. Oktober 2025 den am  12. Dezember 2024 durch das Finanzamt Österreich erlassen Bescheid gemäß § 84 Abs. 1 BAO  betreffend die Ablehnung der steuerlichen Vertreterin sowie die Verständigung des Bf. über  die Ablehnung seiner steuerlichen Vertreterin mit selben Datum.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Finanzamt Österreich` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Univ.-Prof.in Eva Rauber` (person)
- `Henken` (organisation)
- `Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich` (address)
- `Finanzamt Schwechat Gerasdorf` (organisation)
- `69-427/7795` (tax_number)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_14`)


Die Beschwerdeführerin beantragte  am 16.9.2025 die Vorlage ihrer Beschwerde an das Bundesfinanzgericht und führte aus, es  seien 181 Tage bis zum 30.6. und sie habe mehr als das halbe Jahr allein mit ihren Kindern im  Haushalt gelebt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_15`)


Das Finanzamt legte die Beschwerde am 16.10.2025 dem Bundesfinanzgericht  vor und beantragte, sie abzuweisen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1.1. Zu Spruchpunkt I. (Abweisung)  § 295a BAO lautet: „(1)

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag. Irene Kohler` (person)
- `Jean Broderius` (person)
- `Weinwartshof 30, 8151 Södingberg, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_55`)


Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 18. Juni 2025).

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_74`)


Das Bundesfinanzgericht geht daher in freier Beweiswürdigung nach § 45 Abs. 2 AVG davon  aus, dass der Bf.das gegenständliche Fahrzeug am 28. Februar 2025 um 14:19 Uhr in 1230  Wien, Altmannsdorfer Straße nächst ONr. 164, nicht im Rahmen einer Paketzustellung,  sondern zum Einkauf im Supermarkt, am angeführten Ort ohne Entrichtung der  Parkometerabgabe abgestellt hat.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `1230  Wien, Altmannsdorfer Straße` (address)

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_109`)


Das Bundesfinanzgericht erachtet die von der belangten Behörde unter Beachtung der  Strafzumessungsgründe bei einem bis zu 365,00 Euro reichenden Strafrahmen mit 75,00 Euro  verhängte Geldstrafe und die für den Fall der Uneinbringlichkeit mit 17 Stunden festgesetzte  Ersatzfreiheitsstrafe als schuld- und tatangemessen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_121`)


Gemäß § 25 Abs. 2 BFGG hat das Bundesfinanzgericht, soweit dies nicht in der BAO, im ZollR- DG oder im FinStrG geregelt ist, in seiner Entscheidung zu bestimmen, welche  Abgabenbehörde oder Finanzstrafbehörde die Entscheidung zu vollstrecken hat.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Marion Bomarius  in der Beschwerdesache Norbert Ribarczik,  Zufahrt Felbermayr 68, 9241 Neudorf, Österreich, vertreten durch Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft,  Museumstraße 31a, 4020 Linz, über die Beschwerde vom 3. Jänner 2024 gegen den  Einkommensteuerbescheid des Finanzamtes Österreich vom 23. November 2023 betreffend  Berichtigung gem. § 293b BAO zu Bescheid vom 21.11.2023 Steuernummer 71-595/2950  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Dr.in Univ.-Prof.in Marion Bomarius` (person)
- `Norbert Ribarczik` (person)
- `Zufahrt Felbermayr 68, 9241 Neudorf, Österreich` (address)
- `Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft` (organisation)
- `Museumstraße 31a, 4020 Linz` (address)
- `Finanzamtes Österreich` (organisation)
- `71-595/2950` (tax_number)

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_29`)


Mit Schreiben vom 21.3.2024 beantragte der Vertreter des Bf gemäß § 264 BAO die Vorlage  und die Entscheidung durch das Bundesfinanzgericht.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer hat den Wohnsitz in Österreich.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Österreich` (country)

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_59`)


Vor diesem Hintergrund durfte das Bundesfinanzgericht die obigen Sachverhaltsfeststellungen  gemäß § 167 BAO als erwiesen annehmen.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Reinhold Moellenkamp, Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Mag. Josef Ungericht` (person)
- `Reinhold Moellenkamp` (person)
- `Höllererweg 4, 2852 Maltern, Österreich` (address)
- `Achammer & Mennel Rechtsanwälte OG` (organisation)
- `Schloßgraben 10, 6800 Feldkirch` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_91`)


…“  5. Der eingebrachte Vorlageantrag vom 01.04.2020 wurde vom Finanzamt dem  Bundesfinanzgericht am 22.04.2020 zur Entscheidung vorgelegt (Vorlagebericht des  Finanzamtes vom 22.04.2020).

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_93`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf. ist Schweizer Staatsbürgerin, hatte im Streitjahr 2019 in der Schweiz in ihrem  Elternhaus in Ort1 (CH)-Adr1 gemeinsam mit ihrer Mutter einen Wohnsitz und war im Jahr  2019 in der Schweiz als Lehrerin beschäftigt.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Schweiz` (country)
- `Schweiz` (country)

**Example 21** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_131`)


Darüber hinaus gelangt das Bundesfinanzgericht aber auch zur Auffassung, dass sich in den die  NoVA und KfzSt betreffenden festsetzenden Zeiträumen (Juli bis Oktober 2019) die gegebenen  (Lebens-)Umstände der Bf. noch nicht derart verdichtet hatten, dass hinsichtlich des  Wohnsitzes in Ort1 (Ö) von einem Hauptwohnsitz der Bf. auszugehen wäre.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 22** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_139`)


Daraus ergibt sich für das Bundesfinanzgericht, dass die Bf. im Zeitpunkt der  erstmaligen Einbringung des gegenständlichen Kfz nach Österreich bzw. in den Zeiträumen, für  welche die NoVA (07/2019) und KfzSt (08 bis 10/2019) festgesetzt wurden, in Ort1 (Ö) (noch)  keinen Hauptwohnsitz hatte.

**False Positives:**

- `Bundesfinanzgericht` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**
- `Österreich` (country)

**Example 23** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: VwGH`

**F1:** 0.231 | **Precision:** 0.450 | **Recall:** 0.155  

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
| 0.450 | 0.155 | 0.231 | 40 | 18 | 22 | 1 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 22 | 95 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_95`)


Im vorliegenden Fall ergeben sich die Rechtsfolgen unmittelbar aus dem Gesetz und der  einschlägigen Judikatur des Verwaltungsgerichtshofes, diese schlichte Rechtsanwendung  berührt keine Rechtsfrage von grundsätzlicher Bedeutung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_144`)


Im gegenständlichen Fall wurde von der Rechtsprechung des Verwaltungsgerichtshofes nicht  abgewichen bzw. ergeben sich die Rechtsfolgen unmittelbar und eindeutig aus den  gesetzlichen Bestimmungen, weshalb eine Revision nicht zuzulassen war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

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

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_29`)


Der angefochtene Bescheid steht im Einklang mit der geltenden Rechtslage, welche durch die  oben zitierte einschlägige Judikatur des VwGH fundiert bzw. gesichert ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_94`)


Die Unkenntnis ua. von straßenpolizeilichen Bestimmungen oder Parkgebührenvorschriften  stellt zufolge der Judikatur des Verwaltungsgerichtshofes zu § 5 Abs. 2 VStG 1991 keinen  entschuldigenden Rechtsirrtum dar, da von einem Kfz-Lenker verlangt werden kann und ihm  auch zumutbar ist, dass er sich hierzu ausreichend informiert (VwGH 4.8.2005, 2005/17/0056,  VwGH 26.2.2015, 2012/11/0243).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_124`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_23`)


Nach ständiger Judikatur des Verwaltungsgerichtshofes sind Ereignisse im Sinne des § 295a  BAO sachverhaltsändernde tatsächliche oder rechtliche Vorgänge, von denen sich - aus den die  steuerlich relevanten Tatbestände regelnden Abgabenvorschriften - eine abgabenrechtliche  Wirkung für bereits entstandene Abgabenansprüche ergibt (VwGH 1.9.2015, Ra 2015/15/0035  mwN).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_14`)


Wie der VwGH in seiner Entscheidung vom 15. Jänner 2008, 2007/15/0232 ausführt, ist die  Ablehnung eines unbefugten Vertreters diesem gegenüber bescheidmäßig zu verfügen.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_19`)


(vgl. auch VwGH 19. Oktober 2016, Ro 2014/15/0004)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_20`)


In seinem Erkenntnis vom 21. März 2019, Ra 2019/22/0004 hat der VwGH ausgeführt, dass das  verwaltungsgerichtliche Verfahren einerseits und das behördliche Verfahren andererseits eine  Einheit darstellen (vgl. auch VwGH 25. September 2018, Ra 2018/21/0069, Rn. 12f).

**False Positives:**

- `VwGH` — no gold match — missing annotation
- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_29`)


Der angefochtene Bescheid steht im Einklang mit der geltenden Rechtslage, welche durch die  oben zitierte einschlägige Judikatur des VwGH fundiert bzw. gesichert ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_19`)


(vgl. auch VwGH 19. Oktober 2016, Ro 2014/15/0004)

**False Positives:**

- `VwGH` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_20`)


In seinem Erkenntnis vom 21. März 2019, Ra 2019/22/0004 hat der VwGH ausgeführt, dass das  verwaltungsgerichtliche Verfahren einerseits und das behördliche Verfahren andererseits eine  Einheit darstellen (vgl. auch VwGH 25. September 2018, Ra 2018/21/0069, Rn. 12f).

**False Positives:**

- `VwGH` — type mismatch (gold: `VwGH`)

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `VwGH` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz nicht  zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_23`)


Nach ständiger Judikatur des Verwaltungsgerichtshofes sind Ereignisse im Sinne des § 295a  BAO sachverhaltsändernde tatsächliche oder rechtliche Vorgänge, von denen sich - aus den die  steuerlich relevanten Tatbestände regelnden Abgabenvorschriften - eine abgabenrechtliche  Wirkung für bereits entstandene Abgabenansprüche ergibt (VwGH 1.9.2015, Ra 2015/15/0035  mwN).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_94`)


Die Unkenntnis ua. von straßenpolizeilichen Bestimmungen oder Parkgebührenvorschriften  stellt zufolge der Judikatur des Verwaltungsgerichtshofes zu § 5 Abs. 2 VStG 1991 keinen  entschuldigenden Rechtsirrtum dar, da von einem Kfz-Lenker verlangt werden kann und ihm  auch zumutbar ist, dass er sich hierzu ausreichend informiert (VwGH 4.8.2005, 2005/17/0056,  VwGH 26.2.2015, 2012/11/0243).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_124`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_95`)


Im vorliegenden Fall ergeben sich die Rechtsfolgen unmittelbar aus dem Gesetz und der  einschlägigen Judikatur des Verwaltungsgerichtshofes, diese schlichte Rechtsanwendung  berührt keine Rechtsfrage von grundsätzlicher Bedeutung.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_144`)


Im gegenständlichen Fall wurde von der Rechtsprechung des Verwaltungsgerichtshofes nicht  abgewichen bzw. ergeben sich die Rechtsfolgen unmittelbar und eindeutig aus den  gesetzlichen Bestimmungen, weshalb eine Revision nicht zuzulassen war.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: Verwaltungsgerichtshof`

**F1:** 0.205 | **Precision:** 0.500 | **Recall:** 0.129  

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
| 0.500 | 0.129 | 0.205 | 30 | 15 | 15 | 0 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 15 | 15 | 98 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_95`)


Im vorliegenden Fall ergeben sich die Rechtsfolgen unmittelbar aus dem Gesetz und der  einschlägigen Judikatur des Verwaltungsgerichtshofes, diese schlichte Rechtsanwendung  berührt keine Rechtsfrage von grundsätzlicher Bedeutung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_144`)


Im gegenständlichen Fall wurde von der Rechtsprechung des Verwaltungsgerichtshofes nicht  abgewichen bzw. ergeben sich die Rechtsfolgen unmittelbar und eindeutig aus den  gesetzlichen Bestimmungen, weshalb eine Revision nicht zuzulassen war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_94`)


Die Unkenntnis ua. von straßenpolizeilichen Bestimmungen oder Parkgebührenvorschriften  stellt zufolge der Judikatur des Verwaltungsgerichtshofes zu § 5 Abs. 2 VStG 1991 keinen  entschuldigenden Rechtsirrtum dar, da von einem Kfz-Lenker verlangt werden kann und ihm  auch zumutbar ist, dass er sich hierzu ausreichend informiert (VwGH 4.8.2005, 2005/17/0056,  VwGH 26.2.2015, 2012/11/0243).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_124`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz nicht  zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_23`)


Nach ständiger Judikatur des Verwaltungsgerichtshofes sind Ereignisse im Sinne des § 295a  BAO sachverhaltsändernde tatsächliche oder rechtliche Vorgänge, von denen sich - aus den die  steuerlich relevanten Tatbestände regelnden Abgabenvorschriften - eine abgabenrechtliche  Wirkung für bereits entstandene Abgabenansprüche ergibt (VwGH 1.9.2015, Ra 2015/15/0035  mwN).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_2`)


Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149687.1_28`)


Zur Unzulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die ordentliche Revision zulässig, wenn  sie von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt,  insbesondere weil der Beschluss von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den  Verwaltungsgerichtshof nach Art. 133 Abs. 4 Bundes-Verfassungsgesetz nicht  zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149456.1_23`)


Nach ständiger Judikatur des Verwaltungsgerichtshofes sind Ereignisse im Sinne des § 295a  BAO sachverhaltsändernde tatsächliche oder rechtliche Vorgänge, von denen sich - aus den die  steuerlich relevanten Tatbestände regelnden Abgabenvorschriften - eine abgabenrechtliche  Wirkung für bereits entstandene Abgabenansprüche ergibt (VwGH 1.9.2015, Ra 2015/15/0035  mwN).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_94`)


Die Unkenntnis ua. von straßenpolizeilichen Bestimmungen oder Parkgebührenvorschriften  stellt zufolge der Judikatur des Verwaltungsgerichtshofes zu § 5 Abs. 2 VStG 1991 keinen  entschuldigenden Rechtsirrtum dar, da von einem Kfz-Lenker verlangt werden kann und ihm  auch zumutbar ist, dass er sich hierzu ausreichend informiert (VwGH 4.8.2005, 2005/17/0056,  VwGH 26.2.2015, 2012/11/0243).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_124`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_94`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_95`)


Im vorliegenden Fall ergeben sich die Rechtsfolgen unmittelbar aus dem Gesetz und der  einschlägigen Judikatur des Verwaltungsgerichtshofes, diese schlichte Rechtsanwendung  berührt keine Rechtsfrage von grundsätzlicher Bedeutung.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_3`)


Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_143`)


3. Zulässigkeit der Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation
- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 2

**Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_144`)


Im gegenständlichen Fall wurde von der Rechtsprechung des Verwaltungsgerichtshofes nicht  abgewichen bzw. ergeben sich die Rechtsfolgen unmittelbar und eindeutig aus den  gesetzlichen Bestimmungen, weshalb eine Revision nicht zuzulassen war.

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: Magistrat der Stadt Wien`

**F1:** 0.123 | **Precision:** 0.571 | **Recall:** 0.069  

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
| 0.571 | 0.069 | 0.123 | 14 | 8 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 6 | 60 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_122`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) (sent_id: `findok-manually-annotated_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_11`)


In der Folge lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Bf. mit  Strafverfügung vom 5. Mai 2025, GZ. MA67/GZ/2025, an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) Wien am 28. Februar 2025 um 14:19  Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer Straße nächst ONr.  164 Nebenfahrbahn abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred ⊂ gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `1230 Wien, Altmannsdorfer Straße` (address)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_23`)


Mit Straferkenntnis vom 2. Juni 2025, GZ. MA67/GZ/2025, wurde der Bf. vom Magistrat der  Stadt Wien, Magistratsabteilung 67, wegen der bereits näher bezeichneten  Verwaltungsübertretung für schuldig befunden und wegen Verletzung der Rechtsvorschriften  des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006 eine Geldstrafe von 75,00 Euro verhängt und es wurden für den Fall der  Uneinbringlichkeit 17 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred ⊂ gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> partial: 1  |  missing annotation: 0

**Gold Entities:**
- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

## `Specific Entity: Landespolizeidirektion Wien`

**F1:** 0.034 | **Precision:** 1.000 | **Recall:** 0.017  

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
| 1.000 | 0.017 | 0.034 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 62 |

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

## `Specific Entity: Finanzamt Consolidated`

**F1:** 0.034 | **Precision:** 1.000 | **Recall:** 0.017  

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
| 1.000 | 0.017 | 0.034 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 38 |

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
| 1.000 | 0.017 | 0.034 | 2 | 2 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 38 |

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

## `Specific Entity: Verfassungsgerichtshof`

**F1:** 0.017 | **Precision:** 0.500 | **Recall:** 0.009  

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
| 0.500 | 0.009 | 0.017 | 2 | 1 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 103 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

> partial: 0  |  missing annotation: 1

**Gold Entities:**

</details>

---

## `Specific Entity: VfGH`

**F1:** 0.017 | **Precision:** 0.500 | **Recall:** 0.009  

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
| 0.500 | 0.009 | 0.017 | 2 | 1 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 103 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) (sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — missing annotation

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

## `Specific Entity: KQPC Versand GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Event Sudkraftlex GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Sudver Handel Services GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Glanznorost Institut GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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

## `Specific Entity: BMF`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Schweizerische Unfallversicherungsanstalt (SUVA)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: ÖGK`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Pensionsversicherungsanstalt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 | 2 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 111 |

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

## `Specific Entity: Wirtschaftsuniversität Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

## `Specific Entity: FAÖ`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

</details>

---

## `Specific Entity: Deloitte Tax Wirtschaftsprüfungs GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

## `Specific Entity: Universität Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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

## `Specific Entity: Mag. Ghesla Steuerberater GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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

## `Specific Entity: Bundesministerium`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 | 0 | 0 |

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

