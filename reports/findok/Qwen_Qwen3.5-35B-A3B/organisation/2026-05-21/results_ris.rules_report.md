# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-21T20:45:02.685776

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-21/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 400 |
| Validation documents | 101 |
| Test documents | 476 |
| Train sentences | 1171 |
| Validation sentences | 213 |
| Test sentences | 23285 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 10 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 100 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Best Batch Idx | -1 |
| Best Batch F1 | 0.0 |
| Best Rules Serialized | [] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.0% |
| True Positives | 16 |
| False Positives | 293 |
| False Negatives | 329 |
| Total Gold Entities | 345 |
| Micro Precision | 5.2% |
| Micro Recall | 4.6% |
| Micro F1 | 4.9% |
| Macro F1 | 4.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `General GMBH Company` | 0.6% | 100.0% | 0.3% | 1 | 1 | 0 |
| `General AG Company` | 6.0% | 21.8% | 3.5% | 55 | 12 | 43 |
| `LG abbreviation` | 0.6% | 16.7% | 0.3% | 6 | 1 | 5 |
| `Bezirksgericht` | 0.8% | 1.6% | 0.6% | 126 | 2 | 124 |
| `Greiner-Mai Event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `NordDaten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Technik Ostbachal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vossbein Lebensmittel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Paweltschik Telekom GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nexgartuni Finanzen Planung GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AlpenSicherheit GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Reinemut Smoch Handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Salzburg-Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TalVerverwerkGarten GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Henken` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Süd-Landwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Grönemeier` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Milan Händlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Annemie Bott` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Krolitzki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Manfredo Herrschmann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company StadtEnergie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Laskowsky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company TraunChemie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Butkus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Englert` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Keldonbach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sanitär Talder GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Roelfsen Versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lubomir Merschmeyer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Houdek Maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schmeltz Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dorfcon-Verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lexdon IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stadt Logglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gözcü Getränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hörup Gastronomie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dammke KI GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TraunChemie GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tritri-IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien 1/23` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Wien 1/23` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Naaß Elektro GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bersud Möbel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unter Heimdorf GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WXE Textil GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kornfelder Recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `DGCV E-Commerce GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UGQQ Verlag OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fatima Finkenbein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wien Waldnor KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Botho Mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kraftver-Gastronomie GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gartgart Dienstleistungen GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gogel Daten GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Klein-Vorholt KI GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenkasse Retz-Pulkautal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nord Kellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Nexdorf-Metall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Oppert Elektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Zimmerhackel Bau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Vahrenkamp Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Gorius und Ziegann Event GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Raiffeisenbank Rion Vöcklabruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Basdas Pharma AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Depp Versand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SüdEvent AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Obernöder+Küsbert Touristik GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Talost GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt with location` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `FA abbreviation with location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Inn-Recycling Institut GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `EnnsBildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Olivier u. Bartha Recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `West-Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Chen Setzekorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Istvan Gerart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Berwaldkel-Möbel AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht` | 0.0% | 0.0% | 0.0% | 87 | 0 | 87 |
| `Raiffeisen Rionalbank Hall in Tirol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `General KG Company` | 0.0% | 0.0% | 0.0% | 33 | 0 | 33 |
| `SüdVersand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank Wels Süd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TraunLuftfahrt Solutions` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mittel-Logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fensudlog GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Psomadakis Touristik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `General AG Company`

**F1:** 0.060 | **Precision:** 0.218 | **Recall:** 0.035  

**Format:** `regex`  
**Rule ID:** `847d2566`  
**Description:**
Matches companies ending in AG, excluding 'Firma' prefix.

**Content:**
```
(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&]*(?:\s+[A-Z][a-zA-Z0-9+&]*)*\s+AG)(?=\s|$|\)|\]|\"|\'|,|\.|;)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.218 | 0.035 | 0.060 | 55 | 12 | 43 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 43 | 331 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_115`)


3. Klausel 5: „2. Änderungen Z 2. (1) Änderungen dieser zwischen dem Kunden und dem Kreditinstitut vereinbarten Bedingungen gelten nach Ablauf von zwei Monaten ab Zugang der Mitteilung der angebotenen Änderungen an den Kunden als vereinbart, sofern bis dahin kein schriftlicher Widerspruch des Kunden bei der DFA Planung AG einlangt.

| Predicted | Gold |
|---|---|
| `DFA Planung AG` | `DFA Planung AG` |

**Example 2** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

| Predicted | Gold |
|---|---|
| `Landwerlin&Plumke Versand AG` | `Landwerlin&Plumke Versand AG` |

**Example 3** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Bachseewald Heizung AG` | `Bachseewald Heizung AG` |

**Missed by this rule (FN):**

- `Dr. Nadja Köpers` (person)
- `Laahen 3, 3240 Pölla, Österreich` (address)
- `Jakubus` (person)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich` (address)
- `Janis` (person)

**Example 4** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_9`)


Die Besetzungsrüge (Z 1) zeigt zwar keine Tatsachengrundlage für die reklamierte Ausgeschlossenheit des Vorsitzenden des Disziplinarrats wegen Befangenheit (§ 43 Abs 1 Z 3 StPO iVm § 77 Abs 3 DSt) auf, weil aufgrund der Mitteilung des Genannten vom 5. Dezember 2014, wonach er keine Veranlassung sehe, seine „rechtsgeschäftlichen Kontakte“ dem Disziplinarbeschuldigten gegenüber offenzulegen, entgegen dem rein spekulativen Berufungsstandpunkt nicht „anzunehmen ist, dass ein berufsbedingtes Naheverhältnis“ des Vorsitzenden des Disziplinarrats zur Traun Lemalnor AG (Prozessgegnerin der vom Disziplinarbeschuldigten vertretenen Mandanten)“ besteht (vgl RIS-Justiz RS0125768, RS0097054).

| Predicted | Gold |
|---|---|
| `Traun Lemalnor AG` | `Traun Lemalnor AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Duchscherer Digital AG` — partial — pred is substring of gold: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Partei TalAlvalRobotik AG` — partial — gold is substring of pred: `TalAlvalRobotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei CESW Technik Services AG` — partial — gold is substring of pred: `CESW Technik Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `CESW Technik Services AG`(organisation)
- `Mike Zachariä`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 4** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Bezirksgericht`

**F1:** 0.008 | **Precision:** 0.016 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `f3e2904e`  
**Description:**
Matches district courts like 'Bezirksgericht Neunkirchen'.

**Content:**
```
\bBezirksgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.006 | 0.008 | 126 | 2 | 124 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 124 | 343 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_7`)


Nach dem Klagsvorbringen sei er am 19. 8. 2009 im Strandbad Bezirksgericht Silz beim Verlassen des Wassers von einem ca zwei Fäuste großen Stein ins Gesicht getroffen worden, der vom damals sechsjährigen Beklagten geworfen worden sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 1** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_18`)


Verwiesen werde auf einen Akt der Staatsanwaltschaft Bezirksgericht Wels, in welchem gegen den Schädiger Vorerhebungen geführt, jedoch mangels Deliktsfähigkeit eingestellt worden seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wels` | `Bezirksgericht Wels` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Bezirksgericht Judenburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

</details>

---

## `Landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c413d0ce`  
**Description:**
Matches district courts like 'Landesgericht Innsbruck'.

**Content:**
```
\bLandesgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 87 | 0 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 87 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Verfahrenshilfesache der Antragstellerin Florenzia Elefterakis, gegen den Antragsgegner Univ.-Prof. Dr. Leander Rossetti, wegen Bewilligung der Verfahrenshilfe, über den Antrag der Antragstellerin auf Delegierung der Rechtssache an das Landesgericht Korneuburg den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Rechtssache an das Landesgericht Korneuburg wird abgewiesen.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation
- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Florenzia Elefterakis`(person)
- `Dr. Leander Rossetti`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_4`)


Text Begründung: Die Antragstellerin richtete an das Landesgericht Linz einen Antrag auf Bewilligung der Verfahrenshilfe, weil sie gegen einen gerichtlichen Sachverständigen wegen eines in einem Pflegegeldprozess unrichtig erstatteten Gutachtens eine Schadenersatzklage auf Zahlung entgangenen Pflegegeldes und von Schmerzengeld erheben wolle.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_5`)


Das Landesgericht Linz leitete ein Verbesserungsverfahren ein.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_6`)


Die Antragstellerin beantwortete den schriftlichen Verbesserungsauftrag und beantragte die Delegierung des Verfahrens an das Landesgericht Korneuburg mit der Begründung, dass sie wegen ihrer körperlichen Behinderungen der Einladung der Richterin des Landesgerichts Linz, sie wegen offener Fragen bei Gericht aufzusuchen, nicht folgen könne.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_8`)


Das Landesgericht Linz äußerte sich zu diesem Antrag dahin, eine Delegierung könnte zweckmäßig sein, erscheine doch eine persönliche (ergänzende) Befragung der Antragstellerin zum Verfahrenshilfeantrag sinnvoll.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `General KG Company`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `251b6b11`  
**Description:**
Matches companies ending in KG, excluding 'Co KG' false positives and 'Firma' prefix.

**Content:**
```
(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&]*(?:\s+[A-Z][a-zA-Z0-9+&]*)*\s+KG)(?=\s|$|\)|\]|\"|\'|,|\.|;)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 33 | 0 | 33 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 33 | 318 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Energie Conwald GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob28_17s`) (sent_id: `deanon_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Jaroslaw Mlynarik, geboren am 1. Juli 2009, wegen Kontaktrechts des Vaters Dr. Eckard Tschernig, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Bettina Makswietat, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Partner KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jaroslaw Mlynarik`(person)
- `1. Juli 2009`(date)
- `Dr. Eckard Tschernig`(person)
- `Dr. Bettina Makswietat`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Contra GmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `LG abbreviation`

**F1:** 0.006 | **Precision:** 0.167 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `e5b7265e`  
**Description:**
Matches 'LG' followed by city names, e.g., 'LG Innsbruck'.

**Content:**
```
\bLG\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.003 | 0.006 | 6 | 1 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 5 | 294 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `LG Wels` | `LG Wels` |

**Missed by this rule (FN):**

- `FN912691n` (business_register_number)
- `Landesgericht Klagenfurt` (organisation)
- `Holtschmidt Versicherung GmbH` (organisation)
- `Lohneis Pflege gesellschaft mbH` (organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `LG Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob68_14z`) (sent_id: `deanon_TRAIN/4Ob68_14z_22`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `LG Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_40`)


Dieser Auffassung hat sich zwischenzeitig bereits zweitinstanzliche Rechtsprechung ausdrücklich (vgl etwa LG Salzburg EFSlg 156.701 [2018], 159.791, 159.792 [2019];

**False Positives:**

- `LG Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_41`)


LG Linz EFSlg 156.702 [2018], 159.793 [2019]) und die Entscheidung 9 Ob 57/17y offensichtlich angeschlossen.

**False Positives:**

- `LG Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Ob127_14y`) (sent_id: `deanon_TRAIN/7Ob127_14y_64`)


2.1 In Deutschland setzt der Versicherungsfall „Schneedruck“ voraus, dass die versicherte Sache durch die Wirkung des Gewichts von Schnee oder Eismassen beschädigt wird (LG Meiningen r & s 2009, 69;

**False Positives:**

- `LG Meiningen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Greiner-Mai Event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `297fcc00`  
**Description:**
Matches the specific entity 'Greiner-Mai Event'.

**Content:**
```
\bGreiner-Mai\s+Event\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `NordDaten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1edc6ba7`  
**Description:**
Matches the specific entity 'NordDaten'.

**Content:**
```
\bNordDaten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Technik Ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `687bd956`  
**Description:**
Matches the specific entity 'Technik Ostbachal'.

**Content:**
```
\bTechnik\s+Ostbachal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Vossbein Lebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `606c3ff4`  
**Description:**
Matches the specific entity 'Vossbein Lebensmittel'.

**Content:**
```
\bVossbein\s+Lebensmittel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Paweltschik Telekom GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b15a7862`  
**Description:**
Matches the specific entity 'Paweltschik Telekom GMBH'.

**Content:**
```
\bPaweltschik\s+Telekom\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Nexgartuni Finanzen Planung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bcd7be36`  
**Description:**
Matches the specific entity 'Nexgartuni Finanzen Planung GMBH'.

**Content:**
```
\bNexgartuni\s+Finanzen\s+Planung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AlpenSicherheit GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5f0c9201`  
**Description:**
Matches the specific entity 'AlpenSicherheit GMBH'.

**Content:**
```
\bAlpenSicherheit\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinemut Smoch Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `470fcb8c`  
**Description:**
Matches the specific entity 'Reinemut + Smoch Handel' found in multiple failures.

**Content:**
```
Reinemut\s*\+\s*Smoch\s*Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7c422cd1`  
**Description:**
Matches 'FA Salzburg-Stadt' and 'Finanzamt Salzburg-Stadt' including the www. prefix.

**Content:**
```
(?:www\.)?FA\s*Salzburg\-Stadt|Finanzamt\s*Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TalVerverwerkGarten GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `92ef9b5e`  
**Description:**
Matches the specific entity 'TalVerverwerkGarten GMBH' including the ellipsis variant.

**Content:**
```
\bTalVerverwerkGarten\s+GMBH(?:\u2026)?\b
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

## `General AG Company`

**F1:** 0.060 | **Precision:** 0.218 | **Recall:** 0.035  

**Format:** `regex`  
**Rule ID:** `847d2566`  
**Description:**
Matches companies ending in AG, excluding 'Firma' prefix.

**Content:**
```
(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&]*(?:\s+[A-Z][a-zA-Z0-9+&]*)*\s+AG)(?=\s|$|\)|\]|\"|\'|,|\.|;)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.218 | 0.035 | 0.060 | 55 | 12 | 43 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 43 | 331 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_115`)


3. Klausel 5: „2. Änderungen Z 2. (1) Änderungen dieser zwischen dem Kunden und dem Kreditinstitut vereinbarten Bedingungen gelten nach Ablauf von zwei Monaten ab Zugang der Mitteilung der angebotenen Änderungen an den Kunden als vereinbart, sofern bis dahin kein schriftlicher Widerspruch des Kunden bei der DFA Planung AG einlangt.

| Predicted | Gold |
|---|---|
| `DFA Planung AG` | `DFA Planung AG` |

**Example 2** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

| Predicted | Gold |
|---|---|
| `Landwerlin&Plumke Versand AG` | `Landwerlin&Plumke Versand AG` |

**Example 3** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Bachseewald Heizung AG` | `Bachseewald Heizung AG` |

**Missed by this rule (FN):**

- `Dr. Nadja Köpers` (person)
- `Laahen 3, 3240 Pölla, Österreich` (address)
- `Jakubus` (person)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich` (address)
- `Janis` (person)

**Example 4** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_9`)


Die Besetzungsrüge (Z 1) zeigt zwar keine Tatsachengrundlage für die reklamierte Ausgeschlossenheit des Vorsitzenden des Disziplinarrats wegen Befangenheit (§ 43 Abs 1 Z 3 StPO iVm § 77 Abs 3 DSt) auf, weil aufgrund der Mitteilung des Genannten vom 5. Dezember 2014, wonach er keine Veranlassung sehe, seine „rechtsgeschäftlichen Kontakte“ dem Disziplinarbeschuldigten gegenüber offenzulegen, entgegen dem rein spekulativen Berufungsstandpunkt nicht „anzunehmen ist, dass ein berufsbedingtes Naheverhältnis“ des Vorsitzenden des Disziplinarrats zur Traun Lemalnor AG (Prozessgegnerin der vom Disziplinarbeschuldigten vertretenen Mandanten)“ besteht (vgl RIS-Justiz RS0125768, RS0097054).

| Predicted | Gold |
|---|---|
| `Traun Lemalnor AG` | `Traun Lemalnor AG` |

**Example 5** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_12`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

| Predicted | Gold |
|---|---|
| `Daten Unizorstein AG` | `Daten Unizorstein AG` |

**Example 6** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 7** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Analyse Kelunizor AG` | `Analyse Kelunizor AG` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `LGR Medien GmbH` (organisation)
- `OVX Finanzen` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `TraunBau AG` | `TraunBau AG` |

**Missed by this rule (FN):**

- `Ing. KzlR MedR Brunhild Syndikus` (person)
- `Böhnstedt+Bittlmeier Verlag GmbH` (organisation)
- `Wien Traalmon Betriebe` (organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich` (address)

**Example 10** (doc_id: `deanon_TRAIN/8Ob35_23i`) (sent_id: `deanon_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Pflege Deruni, und 2. Marchesi+Kusnezow Transport AG, Grabenseeweg 48, 8272 Ebersdorf, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Valerie Wilczenski, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Marchesi+Kusnezow Transport AG` | `Marchesi+Kusnezow Transport AG` |

**Missed by this rule (FN):**

- `Pflege Deruni` (organisation)
- `Grabenseeweg 48, 8272 Ebersdorf, Österreich` (address)
- `DI Valerie Wilczenski` (person)

**Example 11** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_7`)


Er brachte vor, über seine depotführende Bank in Graz mehrfach Aktien der Daten Monfen AG mit Sitz in Deutschland gekauft zu haben (und zwar, wie aus den von ihm vorgelegten Beilagen ersichtlich, „loco Düsseldorf“).

| Predicted | Gold |
|---|---|
| `Daten Monfen AG` | `Daten Monfen AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Duchscherer Digital AG` — partial — pred is substring of gold: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Partei TalAlvalRobotik AG` — partial — gold is substring of pred: `TalAlvalRobotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei CESW Technik Services AG` — partial — gold is substring of pred: `CESW Technik Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `CESW Technik Services AG`(organisation)
- `Mike Zachariä`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 4** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 5** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Donsteinlex AG` — partial — gold is substring of pred: `Donsteinlex AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 6** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_54`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei OMedR Eleonore Wunderling, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG, Amanda Deutschlender, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Claeser Forschung AG` — partial — pred is substring of gold: `Fildhaut & Claeser Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Eleonore Wunderling`(person)
- `Fildhaut & Claeser Forschung AG`(organisation)
- `Amanda Deutschlender`(person)

**Example 9** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_6`)


Glöckler Daten AG, Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

**False Positives:**

- `Daten AG` — partial — pred is substring of gold: `Glöckler Daten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Glöckler Daten AG`(organisation)
- `Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich`(address)

**Example 10** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Partei Ofczarczik Planung AG` — partial — gold is substring of pred: `Ofczarczik Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 11** (doc_id: `deanon_TRAIN/3Ob215_19t`) (sent_id: `deanon_TRAIN/3Ob215_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Bartholomäus Kurth, vertreten durch die Torggler Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Traberval AG, Vera Lindenstruth, vertreten durch Dr. Manfred Angerer ua, Rechtsanwälte in Klagenfurt am Wörthersee, wegen 300.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 5 R 68/19p-19, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Traberval AG` — partial — gold is substring of pred: `Traberval AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bartholomäus Kurth`(person)
- `Traberval AG`(organisation)
- `Vera Lindenstruth`(person)

**Example 12** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Partei WienDigital Planung AG` — partial — gold is substring of pred: `WienDigital Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 13** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Bachkelwerk Pflege AG` — partial — gold is substring of pred: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 14** (doc_id: `deanon_TRAIN/4Ob19_10p`) (sent_id: `deanon_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Traun-Sanitär gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei NWJ KI Dienstleistungen AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei NWJ KI Dienstleistungen AG` — partial — gold is substring of pred: `NWJ KI Dienstleistungen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Sanitär gesellschaft mbH`(organisation)
- `NWJ KI Dienstleistungen AG`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Lebensmittel Glanzconuni AG` — partial — gold is substring of pred: `Lebensmittel Glanzconuni AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lebensmittel Glanzconuni AG`(organisation)
- `Immanuel Gspan`(person)
- `Fridolin Braunhold`(person)
- `Mag. Frauke Steinweg`(person)
- `DonauLexlogbruckPlanung GmbH`(organisation)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/5Ob102_24x`) (sent_id: `deanon_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei OSR Wolfram Dag, MA, wider die beklagte Partei MLUD Pharma Planung AG, Leila Wildvang, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei MLUD Pharma Planung AG` — partial — gold is substring of pred: `MLUD Pharma Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Wolfram Dag, MA`(person)
- `MLUD Pharma Planung AG`(organisation)
- `Leila Wildvang`(person)

**Example 17** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Kuebler Daten Versicherungs AG` — positional overlap with gold: `Mozar und Kuebler Daten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

**Example 18** (doc_id: `deanon_TRAIN/6Ob231_24z`) (sent_id: `deanon_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Egon Jurguttis, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei UnterFinanzen AG, Silvius Haagmans, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Partei UnterFinanzen AG` — partial — gold is substring of pred: `UnterFinanzen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Egon Jurguttis`(person)
- `UnterFinanzen AG`(organisation)
- `Silvius Haagmans`(person)

**Example 19** (doc_id: `deanon_TRAIN/6Ob36_20t`) (sent_id: `deanon_TRAIN/6Ob36_20t_140`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Frank Mahrhold, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei PKLA Textil Bank Verwilnex Betriebe AG, Valerie Kallweidt, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

**False Positives:**

- `Partei PKLA Textil Bank Verwilnex Betriebe AG` — partial — gold is substring of pred: `PKLA Textil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Frank Mahrhold`(person)
- `PKLA Textil`(organisation)
- `Verwilnex Betriebe AG`(organisation)
- `Valerie Kallweidt`(person)

**Example 21** (doc_id: `deanon_TRAIN/7Nc6_13m`) (sent_id: `deanon_TRAIN/7Nc6_13m_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Norbert Overdick, vertreten durch Dr. Clemens Gärner, Rechtsanwalt in Wien, gegen die beklagte Partei Daten Lexunilog AG, Marlon Jerabeck, vertreten durch Dr. Helmut Engelbrecht und andere Rechtsanwälte in Wien, wegen 4.868,07 EUR sA und Feststellung, über die Befangenheitsanzeige des Hofrats des Obersten Gerichtshofs Dr. Richard Hargassner im Verfahren 9 ObA 29/13z den Beschluss gefasst:  Spruch Der Hofrat des Obersten Gerichtshofs Dr. Richard Hargassner ist ausgeschlossen.

**False Positives:**

- `Partei Daten Lexunilog AG` — partial — gold is substring of pred: `Daten Lexunilog AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Norbert Overdick`(person)
- `Daten Lexunilog AG`(organisation)
- `Marlon Jerabeck`(person)

**Example 22** (doc_id: `deanon_TRAIN/7Ob162_20d`) (sent_id: `deanon_TRAIN/7Ob162_20d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei DDr.in Gisela Loy, vertreten durch Mag. Marco und Mag. Amelie Kunczicky, Rechtsanwälte in Mayrhofen, gegen die beklagte Partei Helferich & Zeitler Marine AG, Jessica Seebald, vertreten durch Mag. Thomas Anker und DI Mag. Nikolaus Gratl, Rechtsanwäte in Innsbruck, wegen Urkundeneinsicht, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Juni 2020, GZ 4 R 55/20z-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Zeitler Marine AG` — partial — pred is substring of gold: `Helferich & Zeitler Marine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr.in Gisela Loy`(person)
- `Helferich & Zeitler Marine AG`(organisation)
- `Jessica Seebald`(person)

**Example 23** (doc_id: `deanon_TRAIN/7Ob165_23z`) (sent_id: `deanon_TRAIN/7Ob165_23z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und die Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Mag. Norbert Faulwasser, vertreten durch Mag. Alexandra Schwarz, Rechtsanwältin in Wien, gegen die beklagte Partei AlpenMaschinenbau AG, Sibylle von Wachtendonk, vertreten durch Dr. Günter Niebauer, Rechtsanwalt in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2023, GZ 3 R 74/23h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei AlpenMaschinenbau AG` — partial — gold is substring of pred: `AlpenMaschinenbau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Norbert Faulwasser`(person)
- `AlpenMaschinenbau AG`(organisation)
- `Sibylle von Wachtendonk`(person)

**Example 24** (doc_id: `deanon_TRAIN/7Ob55_25a`) (sent_id: `deanon_TRAIN/7Ob55_25a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Laurin Tieltges, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Guender Medien AG, Lothar Sax, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 6.090 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 13. Dezember 2024, GZ 2 R 125/24g-42, mit dem das Urteil des Bezirksgerichts Innsbruck vom 28. Mai 2024, GZ 26 C 450/20h-37, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Guender Medien AG` — partial — gold is substring of pred: `Guender Medien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Laurin Tieltges`(person)
- `Guender Medien AG`(organisation)
- `Lothar Sax`(person)

**Example 25** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_4`)


Cynthia Martchenko AG, Schmidhuberstraße 73, 4792 Landertsberg, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2. Reisch + Weißert Getränke AG und 3.

**False Positives:**

- `Cynthia Martchenko AG` — partial — gold is substring of pred: `Cynthia Martchenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cynthia Martchenko`(person)
- `Schmidhuberstraße 73, 4792 Landertsberg, Österreich`(address)
- `Reisch + Weißert Getränke AG`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/7Ob92_19h`) (sent_id: `deanon_TRAIN/7Ob92_19h_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Tosca Janetscheck, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Domingo + Sinner Robotik AG Liliana Böbe, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Sinner Robotik AG` — partial — pred is substring of gold: `Domingo + Sinner Robotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tosca Janetscheck`(person)
- `Domingo + Sinner Robotik AG`(organisation)
- `Liliana Böbe`(person)

**Example 27** (doc_id: `deanon_TRAIN/7Ob94_20d`) (sent_id: `deanon_TRAIN/7Ob94_20d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Bernhard Siegloch, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Aspleiter Forschung AG, Chen Karime, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Aspleiter Forschung AG` — partial — gold is substring of pred: `Aspleiter Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Bernhard Siegloch`(person)
- `Aspleiter Forschung AG`(organisation)
- `Chen Karime`(person)

**Example 28** (doc_id: `deanon_TRAIN/7Ob97_18t`) (sent_id: `deanon_TRAIN/7Ob97_18t_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Leila Werntz, vertreten durch Dr. Peter Gregorich, Rechtsanwalt in Wien, gegen die beklagte Partei Valber Solar AG, Alexander Lukoszek, vertreten durch Dr. Matthias Bacher, Rechtsanwalt in Wien, wegen 1.057.200 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 160/17g-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Valber Solar AG` — partial — gold is substring of pred: `Valber Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Leila Werntz`(person)
- `Valber Solar AG`(organisation)
- `Alexander Lukoszek`(person)

**Example 29** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei, Guggeis Automotive Bank InnBildung Betriebe AG, Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich, vertreten durch Dr. Mag. Günther Riess, Mag. Christine Schneider, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Doris Froemmel, vertreten durch Czernich Hofstädter Guggenberger & Partner, Rechtsanwälte in Innsbruck, wegen 2.278.895,88 EUR sA, über die Rekurse beider Parteien gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Oktober 2010, GZ 4 R 168/10b-76, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Feldkirch vom 20. Mai 2010, GZ 6 Cg 71/08s-71, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch 1.

**False Positives:**

- `Guggeis Automotive Bank InnBildung Betriebe AG` — partial — gold is substring of pred: `Guggeis Automotive`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Guggeis Automotive`(organisation)
- `InnBildung Betriebe AG`(organisation)
- `Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich`(address)
- `Doris Froemmel`(person)

**Example 30** (doc_id: `deanon_TRAIN/8Ob121_22k`) (sent_id: `deanon_TRAIN/8Ob121_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG, Theophil Bings, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ÖkR Christoph Adamske Privatstiftung,*, vertreten durch Dr. Felix Michael Klement, Rechtsanwalt in Wien, wegen 1.500.000 USD sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien vom 28. April 2022, GZ 2 R 133/21z-42, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Soldmann Heizung AG` — partial — pred is substring of gold: `Roettgermann + Soldmann Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roettgermann + Soldmann Heizung AG`(organisation)
- `Theophil Bings`(person)
- `ÖkR Christoph Adamske`(person)

**Example 31** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_8`)


Er wirft der Beklagten vor, ihre Pflichten als Wirtschaftsprüferin der Steinsdörfer Elektro AG verletzt zu haben.

**False Positives:**

- `Elektro AG` — partial — pred is substring of gold: `Steinsdörfer Elektro AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steinsdörfer Elektro AG`(organisation)

**Example 32** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_9`)


Hätte sie pflichtgemäß gehandelt und den von ihr geprüften Jahresabschlüssen den Bestätigungsvermerk versagt, hätte er die Aktien nicht gekauft und damit – wegen der kurz nach seinen Käufen von der Nieder-Analyse Solutions AG beantragten Insolvenzeröffnung – keinen Schaden erlitten.

**False Positives:**

- `Solutions AG` — partial — pred is substring of gold: `Nieder-Analyse Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder-Analyse Solutions AG`(organisation)

**Example 33** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_13`)


Die West Heimwaldstein Solutions AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die West Heimwaldstein Solutions AG` — partial — gold is substring of pred: `West Heimwaldstein Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Heimwaldstein Solutions AG`(organisation)

**Example 34** (doc_id: `deanon_TRAIN/8ObA10_21k`) (sent_id: `deanon_TRAIN/8ObA10_21k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner (aus dem Kreis der Arbeitgeber) und Wolfgang Jelinek (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Thebuss + Großekemper Bildung AG, Univ.-Prof.in Anna Helffer, vertreten durch Dr. Raimund Gehart, Rechtsanwalt in Wien, gegen die beklagte Partei Paulina Strnadl, vertreten durch Dr. Franz Josef Hofer Rechtsanwalt GmbH in Friesach, wegen 5.625,88 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. Dezember 2020, GZ 6 Ra 69/20v-19, mit dem das Urteil des Landesgerichts Klagenfurt als Arbeits- und Sozialgericht vom 15. Mai 2020, GZ 35 Cga 90/19x-11, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Bildung AG` — partial — pred is substring of gold: `Thebuss + Großekemper Bildung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thebuss + Großekemper Bildung AG`(organisation)
- `Univ.-Prof.in Anna Helffer`(person)
- `Paulina Strnadl`(person)

**Example 35** (doc_id: `deanon_TRAIN/8ObA18_17f`) (sent_id: `deanon_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei Cassandra Hennel, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei SeeTextil AG, Othmar Dempewolf, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei SeeTextil AG` — partial — gold is substring of pred: `SeeTextil AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cassandra Hennel`(person)
- `SeeTextil AG`(organisation)
- `Othmar Dempewolf`(person)

**Example 36** (doc_id: `deanon_TRAIN/8ObA59_23v`) (sent_id: `deanon_TRAIN/8ObA59_23v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter und die fachkundigen Laienrichter OAR Prof. Franz Neuhauser (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Benjamin Saeltzer, vertreten durch Dr. Charlotte Böhm, Rechtsanwältin in Wien, gegen die beklagte Partei WaldGlanzdorflogIT Institut AG, Techn R Roswitha Voitl, vertreten durch die Lansky, Ganzger, Goeth, Frankl & Partner Rechtsanwälte GmbH in Wien, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 21. Juni 2023, GZ 10 Ra 47/23i-120, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei WaldGlanzdorflogIT Institut AG` — partial — gold is substring of pred: `WaldGlanzdorflogIT Institut AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benjamin Saeltzer`(person)
- `WaldGlanzdorflogIT Institut AG`(organisation)
- `Techn R Roswitha Voitl`(person)

**Example 37** (doc_id: `deanon_TRAIN/8ObA69_19h`) (sent_id: `deanon_TRAIN/8ObA69_19h_4`)


Dr. Susanne Binder-Novak, Rechtsanwältin in St. Pölten, gegen die beklagte Partei Heizung Trimonwald AG, Ashley Hoeksma, vertreten durch Dr. Helmut Engelbrecht, Rechtsanwalt in Wien, wegen 14.426 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2019, GZ 7 Ra 79/19t-15, in nichtöffentlicher Sitzung Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 2 ASGG, § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Heizung Trimonwald AG` — partial — gold is substring of pred: `Heizung Trimonwald AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Trimonwald AG`(organisation)
- `Ashley Hoeksma`(person)

**Example 38** (doc_id: `deanon_TRAIN/9Ob10_21t`) (sent_id: `deanon_TRAIN/9Ob10_21t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte Dr. Fichtenau, Hon.-Prof. Dr. Dehn, Dr. Hargassner, und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Schnake Robotik gmbh, Jeanne Großkopf, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Volkmar Kapelner GmbH, Reinberg-Litschau 11, 9343 Aich, Österreich, vertreten durch Advokatur Dr. Herbert Schöpf, LL.M., Rechtsanwalt-GmbH in Innsbruck, sowie die Nebenintervenientin auf Seiten der beklagten Partei EKFS Landwirtschaft AG & Co KG, Burgstallerstraße 10, 4892 Röth, Österreich, vertreten durch Hämmerle & Hübner Rechtsanwälte OG in Innsbruck, wegen 115.062,53 EUR sA, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 104.999,62 EUR sA) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Jänner 2021, GZ 3 R 76/20f-144, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei EKFS Landwirtschaft AG` — partial — gold is substring of pred: `EKFS Landwirtschaft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schnake Robotik gmbh`(organisation)
- `Jeanne Großkopf`(person)
- `Volkmar Kapelner`(person)
- `Reinberg-Litschau 11, 9343 Aich, Österreich`(address)
- `EKFS Landwirtschaft AG`(organisation)
- `Burgstallerstraße 10, 4892 Röth, Österreich`(address)

**Example 39** (doc_id: `deanon_TRAIN/9Ob45_10y`) (sent_id: `deanon_TRAIN/9Ob45_10y_4`)


Carla Blaessing, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Perg, gegen die beklagte Partei TraunMaschinenbau AG, Vivian Lammerschmidt, wegen 11.040,07 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Handelsgerichts Wien als Rekursgericht vom 31. Mai 2010, GZ 1 R 130/10d-5, mit dem der Beschluss des Bezirksgerichts für Handelssachen Wien vom 18. März 2010, GZ 14 C 385/10k-2, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Partei TraunMaschinenbau AG` — partial — gold is substring of pred: `TraunMaschinenbau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunMaschinenbau AG`(organisation)
- `Vivian Lammerschmidt`(person)

**Example 40** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_111`)


Bei der gebotenen objektiven Betrachtung läge in der Mitwirkung der VW AG an der Verbesserung der Beklagten grundsätzlich noch kein ausreichender Grund für die Unzumutbarkeit des primären Gewährleistungsbehelfs, allerdings habe der Kläger auch negative Auswirkungen des für seinen Fahrzeugtyp entwickelten Software-Updates behauptet.

**False Positives:**

- `VW AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/9Ob6_24h`) (sent_id: `deanon_TRAIN/9Ob6_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Stiefsohn in der Rechtssache der klagenden Partei Isaak Feyereis, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Fürstentum Liechtenstein, gegen die beklagte Partei Mur Monsteinsee Technologien AG, Floriane Mavrou, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 2.375 EUR und Feststellung (Streitwert: 4.000 EUR), über die Revision der beklagten Partei gegen das Zwischenurteil des Landesgerichts Wels als Berufungsgericht vom 25. Oktober 2023, GZ 22 R 198/23h-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Vöcklabruck vom 15. Juni 2023, GZ 13 C 630/22f-26, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I.Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Mur Monsteinsee Technologien AG` — partial — gold is substring of pred: `Mur Monsteinsee Technologien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isaak Feyereis`(person)
- `Mur Monsteinsee Technologien AG`(organisation)
- `Floriane Mavrou`(person)

**Example 42** (doc_id: `deanon_TRAIN/9ObA134_09k`) (sent_id: `deanon_TRAIN/9ObA134_09k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Hradil und Dr. Hopf als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dipl.-Ing. Ursula Weeverink, vertreten durch Dr. Andreas Lintl, Rechtsanwalt in Wien, gegen die beklagte Partei Thenert Analyse AG, Stanley Helmli, vertreten durch die Winkler Reich-Rohrwig Illedits Rechtsanwälte-Partnerschaft in Wien, wegen Kündigungsanfechtung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht in Arbeits- und Sozialrechtssachen vom 14. Oktober 2009, GZ 10 Ra 108/09i-17, womit der Beschluss des Landesgerichts Krems an der Donau als Arbeits- und Sozialgericht vom 13. August 2009, GZ 7 Cga 42/09b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs der klagenden Partei wird gemäß § 526 Abs 2 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Thenert Analyse AG` — partial — gold is substring of pred: `Thenert Analyse AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Ursula Weeverink`(person)
- `Thenert Analyse AG`(organisation)
- `Stanley Helmli`(person)

</details>

---

## `Bezirksgericht`

**F1:** 0.008 | **Precision:** 0.016 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `f3e2904e`  
**Description:**
Matches district courts like 'Bezirksgericht Neunkirchen'.

**Content:**
```
\bBezirksgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.006 | 0.008 | 126 | 2 | 124 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 124 | 343 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_7`)


Nach dem Klagsvorbringen sei er am 19. 8. 2009 im Strandbad Bezirksgericht Silz beim Verlassen des Wassers von einem ca zwei Fäuste großen Stein ins Gesicht getroffen worden, der vom damals sechsjährigen Beklagten geworfen worden sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 1** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_18`)


Verwiesen werde auf einen Akt der Staatsanwaltschaft Bezirksgericht Wels, in welchem gegen den Schädiger Vorerhebungen geführt, jedoch mangels Deliktsfähigkeit eingestellt worden seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wels` | `Bezirksgericht Wels` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Bezirksgericht Judenburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_4`)


Kfm. Raul Bialleck Plc, pA Ernestine Enger, Deutschland, wegen 1.624 EUR sA über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernestine Enger`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_7`)


[2] Das von der Klägerin angerufene Bezirksgericht Schwechat wies die Klage mit rechtskräftigem Beschluss vom 19. Jänner 2022 mangels internationaler Zuständigkeit zurück.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_36`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel;

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Delia Truepschuch, geboren am 1. Februar 2026, und Aloisa Eckmaier, geboren am 28. Februar 1976, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation
- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Delia Truepschuch`(person)
- `1. Februar 2026`(date)
- `Aloisa Eckmaier`(person)
- `28. Februar 1976`(date)

**Example 10** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

**False Positives:**

- `Bezirksgericht Feldkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `ÖkR Priv.-Doz. Sven Egerth`(person)
- `3. Mai`(date)

**Example 15** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_5`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation
- `Bezirksgericht Braunau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 16** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_6`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_9`)


Die klagende Partei beantragt die Delegierung des Verfahrens vom Bezirksgericht Graz-West an das Bezirksgericht Fünfhaus.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_11`)


Das Bezirksgericht Graz-West spricht sich für die Delegierung aus.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Zarin Steevens, geboren 26. Mai 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Dorothea Akkaya, und des Antragsgegners Mirko Hamidi, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation
- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Zarin Steevens`(person)
- `26. Mai`(date)
- `Dorothea Akkaya`(person)
- `Mirko Hamidi`(person)

**Example 20** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_8`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Raumberg 325, 2301 Schönau an der Donau, Österreich aufhalte (ON 7).

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Raumberg 325, 2301 Schönau an der Donau, Österreich`(address)

**Example 21** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_10`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_14`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_16`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_18`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_21`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation
- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation
- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 26** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_22`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_23`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/10Ob2_10g`) (sent_id: `deanon_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Dagobert Borghart anhängig.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dagobert Borghart`(person)

**Example 29** (doc_id: `deanon_TRAIN/10Ob4_17m`) (sent_id: `deanon_TRAIN/10Ob4_17m_8`)


Am 20. 9. 2016 beantragte die Antragstellerin beim Bezirksgericht Josefstadt die Erhöhung der monatlichen Unterhaltszahlung auf 440 EUR ab 1. 9. 2016.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_6`)


Aus Anlass einer vom Bezirksgericht Linz am 17. Dezember 2015 ausgesprochenen Verurteilung, AZ 17 U 185/14t, wurde die Probezeit der bedingten Entlassung auf fünf Jahre verlängert (vgl ON 58 S 7 der Hv-Akten).

**False Positives:**

- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_9`)


Hinsichtlich des Vollzugs der verhängten Freiheitsstrafe und des widerrufenen Strafrests bewilligte das Bezirksgericht Steyr (als erkennendes Gericht im Sinn des § 7 StVG [vglJerabek, WK-StPO § 494a Rz 15]) mit Beschluss vom 27. April 2016 dem Verurteilten einen Strafaufschub gemäß § 6 Abs 1 Z 2 lit a StVG bis zum 1. Mai 2017 (ON 11 der U-Akten).

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_10`)


Mit am 10. Februar 2017 beim Bezirksgericht Steyr eingelangtem Schreiben ersuchte der Verurteilte den „Haftaufschub 5 U 42/16w-17 der im Mai 2017 ausläuft, in eine bedingte Haftstrafe umzuändern“, wobei er zusammengefasst vorbrachte, dass er seit August 2016 als Küchenhilfe tätig sei, seinen Zahlungsverpflichtungen nachkomme und nun die Möglichkeit einer stationären Drogenentzugsbehandlung wahrnehmen möchte (ON 18 der U-Akten).

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_12`)


Mit Note vom 17. Februar 2017 teilte das Landesgericht St. Pölten dem Bezirksgericht Steyr mit, „dass derAntrag offensichtlich auf nachträgliche Milderung der mit Urteil des BG Steyr vom 11.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_15`)


Das Bezirksgericht Steyr übermittelte daraufhin die Akten dem Obersten Gerichtshof zur Entscheidung über einen Zuständigkeitskonflikt (ON 23 der U-Akten): Nach Ansicht des vorlegenden Gerichts sei das Bezirksgericht Steyr zwar zur Entscheidung über den Antrag auf nachträgliche Strafmilderung hinsichtlich der mit Urteil des Bezirksgerichts Steyr vom 11. April 2016 verhängten unbedingten Freiheitsstrafe zuständig;

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation
- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 36** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_18`)


Daraufhin übermittelte das Bezirksgericht Steyr die Akten dem Landesgericht St. Pölten mit dem Ersuchen um Äußerung zur Zuständigkeitsfrage im Sinn der Ausführungen des Obersten Gerichtshofs.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_21`)


2012 verhängte Strafmaß von sechzehn Monaten Freiheitsstrafe herabsetzen möge, sondern darauf, dass das Bezirksgericht Steyr seine urteilsmäßige Entscheidung vom 11.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_27`)


Daher kommt – entgegen der Ansicht des Landesgerichts St. Pölten – im Rahmen des § 31a StGB eine nachträgliche Änderung des vom Bezirksgericht Steyr (gemeinsam mit dem Urteil) gefassten Beschlusses auf Widerruf der zu AZ 38 BE 50/13x des Landesgerichts Steyr gewährten bedingten Entlassung nicht in Betracht.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/12Os132_12x`) (sent_id: `deanon_TRAIN/12Os132_12x_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in seinem Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Bezirksgericht Innsbruck verwiesen.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/12Os132_12x`) (sent_id: `deanon_TRAIN/12Os132_12x_7`)


Nach einer gescheiterten staatsanwaltschaftlichen Diversion wurde das in der Folge vom Bezirksgericht Innsbruck zu AZ 8 U 408/09v geführte Verfahren mit Beschluss vom 19. Mai 2010 (ON 28) gemäß §§ 35 Abs 1 iVm 37 SMG unter Bestimmung einer Probezeit von zwei Jahren vorläufig eingestellt.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/12Os132_12x`) (sent_id: `deanon_TRAIN/12Os132_12x_8`)


Mangels Einlangens von Bestätigungen über den Beginn und den anschließenden Verlauf aufgetragener klinisch-psychologischer Beratung und Betreuung sowie einer ärztlichen Entzugs- und Substitutionsbehandlung und weil der Angeklagte sich der Kontrolluntersuchung nach dem SMG entzog (ON 35), was solcherart auch einer weiteren diversionellen Erledigung entgegensteht, setzte das Bezirksgericht Innsbruck das Strafverfahren mit Beschluss vom 29. Oktober 2010 gemäß § 38 Abs 1 Z 2 SMG fort (ON 37).

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Pentzold des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Bezirksgericht Leopoldstadt Nenad Pentzold` — partial — gold is substring of pred: `Pentzold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pentzold`(person)

**Example 45** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__7`)


Das angefochtene Urteil, das im Übrigen unberührt bleibt, wird im Ausspruch über die Verbandsgeldbuße aufgehoben und die Sache in diesem Umfang wird zu neuer Verhandlung und Entscheidung an das Bezirksgericht Spittal an der Drau verwiesen.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__11`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_3`)


Kopf Der Oberste Gerichtshof hat am 23. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Melounek als Schriftführerin in der Strafsache gegen Fabiano Pflichtbeil wegen Vergehen der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB in dem zu AZ 3 U 21/17x des Bezirksgerichts Lienz und zu AZ 5 U 52/17h des Bezirksgerichts Wiener Neustadt geführten Kompetenzkonflikt nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Wiener Neustadt zu führen.

**False Positives:**

- `Bezirksgericht Wiener Neustadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pflichtbeil`(person)

**Example 48** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_4`)


Gründe:  Rechtliche Beurteilung Mit am 24. Februar 2015 beim Bezirksgericht Lienz eingebrachtem Strafantrag (ON 13) legte die Staatsanwaltschaft Innsbruck Fabiano Pierskala zur Last, er habe seine im Familienrecht begründete Unterhaltspflicht gegenüber Leonardo Mehltreter in den Zeiträumen 1. bis 31. März 2015, 1. bis 30. Juni 2015 und 1. August 2015 bis 3. November 2016 gröblich verletzt, und erachtete durch dieses Verhalten „das“ (richtig: mehrere) Vergehen der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB verwirklicht.

**False Positives:**

- `Bezirksgericht Lienz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_5`)


Das Bezirksgericht Lienz überwies die Sache wegen örtlicher Unzuständigkeit dem Bezirksgericht Wiener Neustadt (§ 38 erster Satz StPO).

**False Positives:**

- `Bezirksgericht Lienz` — no gold match — likely missing annotation
- `Bezirksgericht Wiener Neustadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 50** (doc_id: `deanon_TRAIN/15Ns82_10t`) (sent_id: `deanon_TRAIN/15Ns82_10t_3`)


Kopf Der Oberste Gerichtshof hat am 19. Jänner 2011 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Jahn als Schriftführerin in den Strafsachen gegen Christoph Cihlarz wegen des Vergehens der Körperverletzung nach § 83 Abs 1 StGB, AZ 9 U 55/10p des Bezirksgerichts Hartberg, und AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya über den Kompetenzkonflikt betreffend die Durchführung des zu AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya anhängigen Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Für die Durchführung des Strafverfahrens gegen Christoph Cöllner wegen § 83 Abs 1 StGB, AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya, ist das Bezirksgericht Hartberg zuständig.

**False Positives:**

- `Bezirksgericht Hartberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Cihlarz`(person)

**Example 51** (doc_id: `deanon_TRAIN/15Ns82_10t`) (sent_id: `deanon_TRAIN/15Ns82_10t_7`)


Nach Abtretung an das Bezirksgericht Hartberg zur Verbindung mit dem zuvor genannten Verfahren wurde dieses Verfahren vom Bezirksgericht Hartberg an das Bezirksgericht Laa an der Thaya mit dem Bemerken rückabgetreten, dass „eine Einbeziehung auf Grund der angebotenen Diversion nicht möglich“ sei, worauf das Bezirksgericht Laa an der Thaya die Akten zur Entscheidung gemäß § 38 dritter Satz StPO vorlegte.

**False Positives:**

- `Bezirksgericht Hartberg` — no gold match — likely missing annotation
- `Bezirksgericht Hartberg` — no gold match — likely missing annotation
- `Bezirksgericht Laa` — no gold match — likely missing annotation
- `Bezirksgericht Laa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Example 52** (doc_id: `deanon_TRAIN/15Ns82_10t`) (sent_id: `deanon_TRAIN/15Ns82_10t_12`)


Das Bezirksgericht Hartberg, in dessen Zuständigkeit die frühere Straftat (15. Mai 2010) fällt, ist daher nach § 37 Abs 3 iVm § 37 Abs 2 zweiter Satz StPO für die Durchführung des (demnach zu verbindenden) Strafverfahrens AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya zuständig.

**False Positives:**

- `Bezirksgericht Hartberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/15Os97_10v`) (sent_id: `deanon_TRAIN/15Os97_10v_14`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, verletzt der Vorgang, dass es das Bezirksgericht Innsbruck unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Graeupner im Verfahren AZ 23 BE29/06a des Landesgerichts Innsbruck gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich das Vollzugsgericht in Kenntnis zu setzen, § 494a Abs 7 StPO, wonach das erkennende Gericht all jene Gerichte unverzüglich zu verständigen hat, deren Vorentscheidungen von einer Entscheidung nach § 494a Abs 1 und 6 StPO betroffen sind.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Graeupner`(person)

**Example 54** (doc_id: `deanon_TRAIN/15Os97_10v`) (sent_id: `deanon_TRAIN/15Os97_10v_17`)


Das Bezirksgericht Innsbruck hätte daher sogleich nach Fassung seines Probezeitverlängerungsbeschlusses - und nicht erst im Zuge der Endverfügung vom 31. März 2010 - das Vollzugsgericht davon in Kenntnis setzen müssen.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)

**Example 56** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_7`)


Sie beantragt beim Obersten Gerichtshof gemäß § 28 JN unter Anschluss der einzubringenden Klage die Ordination des Bezirksgerichts für Handelssachen Wien als örtlich zuständiges Gericht, auch wenn aufgrund des Abflugorts das Bezirksgericht Schwechat naheliegend erschiene, das aber in Fluggastsachen überlastet sei.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_10`)


2. Der Oberste Gerichtshof hat bereits in anderen gleichgelagerten Fällen der Durchsetzung von Ansprüchen nach der EU-Fluggastrechte-VO gegen das auch hier beklagte Flugunternehmen mit Sitz in Hirschmühle 31, 8221 Hofing, Österreich (Serbien) die Ordination bewilligt und das Bezirksgericht Schwechat, in dessen Sprengel der Abflughafen liegt, als zuständiges Gericht bestimmt (6 Nc 1/19b = ZVR 2019/114, 259 [zustMayr];

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hirschmühle 31, 8221 Hofing, Österreich`(address)

**Example 58** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_6`)


Mit der am 20. 8. 2012 beim Bezirksgericht Bezirksgericht Hallein eingebrachten Klage begehrte der Minderjährige von einem in Deutschland wohnhaften minderjährigen Beklagten Schadenersatz von 3.850 EUR sA und die Feststellung seiner Haftung für sämtliche aus dessen Steinwurf resultierenden Spät- und Dauerfolgen.

**False Positives:**

- `Bezirksgericht Bezirksgericht Hallein` — partial — gold is substring of pred: `Bezirksgericht Hallein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hallein`(organisation)

**Example 59** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_69`)


8. 2012 beim gemäß Art 5 Nr 3 EuGVVO zuständigen Bezirksgericht Bezirksgericht Weiz (Gericht des Ortes, an dem das schädigende Ereignis eingetreten ist) im Elektronischen Rechtsverkehr eingebracht.

**False Positives:**

- `Bezirksgericht Bezirksgericht Weiz` — partial — gold is substring of pred: `Bezirksgericht Weiz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Weiz`(organisation)

**Example 60** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Bezirksgericht Amstetten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 61** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. Musger als weitere Richter in der Rechtssache der klagenden Partei Glanzbruckkraft-Recycling -Aktiengesellschaft, Steindläcker 26, 4183 Obertraberg, Österreich, vertreten durch THUM WEINREICH SCHWARZ CHYBA REITER Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Verband der Versicherungsunternehmen Österreichs, Schwarzenbergplatz 7, 1030 Wien, vertreten durch Mag. Georg E. Thalhammer, Rechtsanwalt in Wien, wegen 11.550 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Innere Stadt Wien das Bezirksgericht Kitzbühel bestimmt.

**False Positives:**

- `Bezirksgericht Kitzb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Glanzbruckkraft-Recycling`(organisation)
- `Steindläcker 26, 4183 Obertraberg, Österreich`(address)

**Example 62** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_4`)


Text Begründung: Die klagende Partei begehrt in ihrer beim Bezirksgericht Innere Stadt Wien am allgemeinen Gerichtsstand der beklagten Partei eingebrachten Klage Schadenersatz nach einem Verkehrsunfall auf der B 178 im Ortsgebiet von Going am Wilden Kaiser.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_7`)


Nachdem die beklagte Partei das Klagebegehren dem Grunde und der Höhe nach bestritten hatte, beantragte die klagende Partei die Delegierung der Rechtssache an das Bezirksgericht Kitzbühel, in dessen Sprengel sich der Unfall ereignet habe.

**False Positives:**

- `Bezirksgericht Kitzb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_11`)


Das Bezirksgericht Innere Stadt Wien hält die Delegierung für zweckmäßig.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/2Ob162_23x`) (sent_id: `deanon_TRAIN/2Ob162_23x_8`)


Text Begründung: [1] Beim Bezirksgericht St. Johann im Pongau ist zu AZ 455 A 78/22f das Verlassenschaftsverfahren nach dem 2022 verstorbenen Erblasser anhängig.

**False Positives:**

- `Bezirksgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)

**Example 67** (doc_id: `deanon_TRAIN/3Nc32_19i`) (sent_id: `deanon_TRAIN/3Nc32_19i_5`)


Das Bezirksgericht Telfs legte den Akt unmittelbar (dh ohne jede sonstige Erledigung) von Amts wegen dem Obersten Gerichtshof zwecks Entscheidung über eine Ordination nach § 28 JN vor.

**False Positives:**

- `Bezirksgericht Telfs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/3Nc32_19i`) (sent_id: `deanon_TRAIN/3Nc32_19i_8`)


Da das angerufene Bezirksgericht Telfs bislang noch nicht negativ über seine Zuständigkeit entschieden hat, kommt eine Ordination nach § 28 JN nicht in Betracht.

**False Positives:**

- `Bezirksgericht Telfs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

**Example 70** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_30`)


Als örtlich zuständiges Exekutionsgericht für die beabsichtigte Rechteexekution ist das Bezirksgericht Salzburg zu bestimmen, weil die Logcon-Möbel.at GmbH als Registrierungsstelle der von der beabsichtigten Exekutionsführung betroffenen Domain der Verpflichteten im Sprengel dieses Gerichts ihren Sitz hat.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Logcon-Möbel.at`(organisation)

**Example 71** (doc_id: `deanon_TRAIN/3Ob203_11s`) (sent_id: `deanon_TRAIN/3Ob203_11s_9`)


Am selben Tag langte eine von den Antragstellern selbst verfasste Berufung per Fax beim Bezirksgericht Saalfelden ein.

**False Positives:**

- `Bezirksgericht Saalfelden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_5`)


Für die Bewilligung und die Vollziehung der beabsichtigten Exekution gegen die Zweitbeklagte auf Urteilsveröffentlichung wird das Bezirksgericht Innere Stadt Wien als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_8`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_19`)


Dem Ordinationsantrag ist somit stattzugeben und zweckmäßigerweise das Bezirksgericht Innere Stadt Wien als zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_14`)


Mit dem vorliegendenOrdinationsantragbegehren die Kläger, für die Rechtssache das Bezirksgericht Imst als örtlich zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Imst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_15`)


Sie gestehen zu, dass das angerufene Bezirksgericht Imst nicht zufolge § 83 Abs 1 JN zuständig sei, weil der Bestandgegenstand nicht im Sprengel dieses Bezirksgerichts, sondern im Fürstentum Liechtenstein liege.

**False Positives:**

- `Bezirksgericht Imst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_4`)


Kirsten Falterer, MA, vertreten durch Mag. Daniel Schöpf, Mag. Christian Maurer, Mag. Daniel Maurer, Rechtsanwälte in Salzburg, gegen die beklagte Partei Mona Gronmayer, BSc, vertreten durch die Steiner Anderwald Rechtsanwälte OG in Spittal an der Drau, wegen 28.017,16 EUR sA, über Vorlage des Akts AZ 3 C 361/20p des Bezirksgerichts Spittal an der Drau zur Entscheidung eines negativen Kompetenzkonflikts, den Beschluss gefasst:  Spruch Zur Fortführung dieser Rechtssache ist das Bezirksgericht Spittal an der Drau zuständig.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kirsten Falterer, MA`(person)
- `Mona Gronmayer, BSc`(person)

**Example 78** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_6`)


Text Begründung: Mit der beim Bezirksgericht Salzburg eingebrachten Mahnklage begehrte der Kläger von der Beklagten die Zahlung von 28.017,16 EUR sA.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_9`)


In ihrem Einspruch gegen den vom Bezirksgericht Salzburg erlassenen Zahlungsbefehl erhob die Beklagte die Einrede der sachlichen und örtlichen Unzuständigkeit mit der Begründung, die Rechnungen stünden in einem tatsächlichen und rechtlichen Zusammenhang und seien daher zusammenzurechnen.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_11`)


Der Kläger räumte daraufhin ein, dass die Forderungen gemäß § 55 JN zusammenzurechnen seien, und stellte für den Fall, dass sich das Bezirksgericht Salzburg für unzuständig erklärt, den Antrag, die Klage an das nicht offenbar unzuständige Landesgericht Salzburg zu überweisen.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_12`)


Für den Fall der Unzuständigkeit dieses Landesgerichts beantragte er die Überweisung an das Landesgericht Klagenfurt, allenfalls an das Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_13`)


Das Bezirksgericht Salzburg sprach mit rechtskräftigem Beschluss vom 6. Dezember 2019 seine sachliche Unzuständigkeit aus und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_17`)


Über Antrag des Klägers hob das Landesgericht Klagenfurt die Zurückweisung der Klage mit rechtskräftigem Beschluss vom 14. Februar 2020 auf und überwies die Rechtssache dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_18`)


Das Bezirksgericht Spittal an der Drau lehnte mit rechtskräftigem Beschluss vom 20. Mai 2020 „die Übernahme der überwiesenen Rechtssache ab“ und erklärte sich für sachlich unzuständig.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_20`)


Das Bezirksgericht Spittal an der Drau legte den Akt dem Oberlandesgericht Graz gemäß § 47 Abs 2 JN zur Entscheidung über den negativen Kompetenzkonflikt vor.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_24`)


Zwar haben hier das Bezirksgericht Salzburg, das Landesgericht Salzburg, das Landesgericht Klagenfurt und das Bezirksgericht Spittal an der Drau jeweils seine Zuständigkeit verneint.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation
- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 87** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_25`)


Allerdings besteht ein Streit über die Zuständigkeit iSd § 47 Abs 1 JN nur zwischen dem Landesgericht Klagenfurt und dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_36`)


5.Das Bezirksgericht Spittal an der Drau missachtete mit seiner Unzuständigkeitsentscheidung die dargestellte Bindungswirkung des vorausgehenden Beschlusses des Landesgerichts Klagenfurt.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und den Hofrat Dr. Steger als weitere Richter in der Pflegschaftssache des mj Dr.in Selina Mäntler, geboren am 1. Dezember 2003, Vater Techn R DDr. OStR KzlR Daniel von Reichardt, vertreten durch Prof. Dr. Georg Zanger, Rechtsanwalt in Wien, wegen Obsorge, über den Delegierungsantrag der Mutter Lynn Eisenbarth, vertreten durch Mag. Britta Schönhart-Loinig, Rechtsanwältin in Wien, den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Pflegschaftssache vom Bezirksgericht Gänserndorf an das Bezirksgericht Villach wird abgewiesen.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Selina Mäntler`(person)
- `1. Dezember 2003`(date)
- `Techn R DDr. OStR KzlR Daniel von Reichardt`(person)
- `Lynn Eisenbarth`(person)

**Example 90** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_22`)


7. 2019 die Delegierung der Pflegschaftssache an das Bezirksgericht Villach nach § 31 Abs 1 JN.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_28`)


Da der Mittelpunkt der Lebensführung des Kindes nunmehr in Velden liege und offene Anträge nicht gegen eine Zuständigkeitsübertragung sprächen, sei das Bezirksgericht Villach besser in der Lage, die pflegschaftsgerichtlichen Agenden zu besorgen.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_36`)


Die Handhabung des pflegschaftsgerichtlichen Schutzes des Kindes sei durch das Bezirksgericht Gänserndorf wirksamer gestaltbar als durch das Bezirksgericht Villach, das die Familie überhaupt noch nicht kenne.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_58`)


das delegierte Bezirksgericht Villach müsste sich in den mittlerweile bereits umfangreichen Pflegschaftsakt erst einarbeiten.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_62`)


Dass in diesem Verfahrensstadium die Delegierung der Pflegschaftssache an das Bezirksgericht Villach dem Kindeswohl besser entsprechen würde als die Weiterführung des Obsorge- und Kontaktrechtsverfahrens durch den bisher zuständigen Richter des Bezirksgerichts Gänserndorf, ist ebensowenig zu erkennen wie eine dadurch erzielbare Verfahrensbeschleunigung und Erleichterung des Gerichtszugangs für sämtliche Beteiligte.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_63`)


Der Umstand, dass der Minderjährige derzeit im Sprengel des Bezirksgerichts Villach wohnt und für die Mutter seine Betreuung bei Terminen am Bezirksgericht Villach leichter zu organisieren wäre als beim Bezirksgericht Gänserndorf, reicht daher für eine Bejahung der Zweckmäßigkeit iSd § 31 Abs 1 JN nicht aus.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_TRAIN/6Ob199_10y`) (sent_id: `deanon_TRAIN/6Ob199_10y_5`)


Im vorliegenden Verfahren geht es um die pflegschaftsbehördliche Genehmigung eines Vergleichs vor dem Bezirksgericht Meidling.

**False Positives:**

- `Bezirksgericht Meidling` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_4`)


Ophelia Kadlecova, und 2. Constanze Ishikawa, wegen Erlassung einer einstweiligen Verfügung, infolge der Vorlage des Aktes 1 C 16/12t des Bezirksgerichts Wiener Neustadt zur Entscheidung über den negativen Kompetenzkonflikt mit dem Bezirksgericht Mürzzuschlag nach § 47 JN den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag auf Erlassung der einstweiligen Verfügung ist das Bezirksgericht Wiener Neustadt zuständig.

**False Positives:**

- `Bezirksgericht Wiener Neustadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ophelia Kadlecova`(person)
- `Constanze Ishikawa`(person)

</details>

---

## `General GMBH Company`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `94ab9c6b`  
**Description:**
Matches companies ending in GMBH, excluding 'Firma' prefix and handling '+' in names.

**Content:**
```
(?:^|\s|\(|\[|\"|\'|,|\.)\s*([A-Z][a-zA-Z0-9+&]*(?:\s+[A-Z][a-zA-Z0-9+&]*)*\s+GMBH)(?=\s|$|\)|\]|\"|\'|,|\.|;)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 125 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_16`)


Deren Gesellschafter sind die Gesellschaft mit einer voll eingezahlten Stammeinlage von 6.033.242,30 EUR und die Hoenisch Energie GMBH mit einer voll eingezahlten Stammeinlage von 100 EUR.

| Predicted | Gold |
|---|---|
| `Hoenisch Energie GMBH` | `Hoenisch Energie GMBH` |

</details>

---

## `LG abbreviation`

**F1:** 0.006 | **Precision:** 0.167 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `e5b7265e`  
**Description:**
Matches 'LG' followed by city names, e.g., 'LG Innsbruck'.

**Content:**
```
\bLG\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.003 | 0.006 | 6 | 1 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 5 | 294 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `LG Wels` | `LG Wels` |

**Missed by this rule (FN):**

- `FN912691n` (business_register_number)
- `Landesgericht Klagenfurt` (organisation)
- `Holtschmidt Versicherung GmbH` (organisation)
- `Lohneis Pflege gesellschaft mbH` (organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `LG Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob68_14z`) (sent_id: `deanon_TRAIN/4Ob68_14z_22`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `LG Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_40`)


Dieser Auffassung hat sich zwischenzeitig bereits zweitinstanzliche Rechtsprechung ausdrücklich (vgl etwa LG Salzburg EFSlg 156.701 [2018], 159.791, 159.792 [2019];

**False Positives:**

- `LG Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_41`)


LG Linz EFSlg 156.702 [2018], 159.793 [2019]) und die Entscheidung 9 Ob 57/17y offensichtlich angeschlossen.

**False Positives:**

- `LG Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Ob127_14y`) (sent_id: `deanon_TRAIN/7Ob127_14y_64`)


2.1 In Deutschland setzt der Versicherungsfall „Schneedruck“ voraus, dass die versicherte Sache durch die Wirkung des Gewichts von Schnee oder Eismassen beschädigt wird (LG Meiningen r & s 2009, 69;

**False Positives:**

- `LG Meiningen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Greiner-Mai Event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `297fcc00`  
**Description:**
Matches the specific entity 'Greiner-Mai Event'.

**Content:**
```
\bGreiner-Mai\s+Event\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `NordDaten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1edc6ba7`  
**Description:**
Matches the specific entity 'NordDaten'.

**Content:**
```
\bNordDaten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Technik Ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `687bd956`  
**Description:**
Matches the specific entity 'Technik Ostbachal'.

**Content:**
```
\bTechnik\s+Ostbachal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Vossbein Lebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `606c3ff4`  
**Description:**
Matches the specific entity 'Vossbein Lebensmittel'.

**Content:**
```
\bVossbein\s+Lebensmittel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Paweltschik Telekom GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b15a7862`  
**Description:**
Matches the specific entity 'Paweltschik Telekom GMBH'.

**Content:**
```
\bPaweltschik\s+Telekom\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Nexgartuni Finanzen Planung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bcd7be36`  
**Description:**
Matches the specific entity 'Nexgartuni Finanzen Planung GMBH'.

**Content:**
```
\bNexgartuni\s+Finanzen\s+Planung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AlpenSicherheit GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5f0c9201`  
**Description:**
Matches the specific entity 'AlpenSicherheit GMBH'.

**Content:**
```
\bAlpenSicherheit\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinemut Smoch Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `470fcb8c`  
**Description:**
Matches the specific entity 'Reinemut + Smoch Handel' found in multiple failures.

**Content:**
```
Reinemut\s*\+\s*Smoch\s*Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7c422cd1`  
**Description:**
Matches 'FA Salzburg-Stadt' and 'Finanzamt Salzburg-Stadt' including the www. prefix.

**Content:**
```
(?:www\.)?FA\s*Salzburg\-Stadt|Finanzamt\s*Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TalVerverwerkGarten GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `92ef9b5e`  
**Description:**
Matches the specific entity 'TalVerverwerkGarten GMBH' including the ellipsis variant.

**Content:**
```
\bTalVerverwerkGarten\s+GMBH(?:\u2026)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Henken`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d026d57e`  
**Description:**
Matches the specific entity 'Henken'.

**Content:**
```
\bHenken\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Süd-Landwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7f815650`  
**Description:**
Matches the specific entity 'Süd-Landwirtschaft'.

**Content:**
```
\bSüd-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Grönemeier`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4eee39aa`  
**Description:**
Matches the specific entity 'Grönemeier&Hövelberndt E‑Commerce'.

**Content:**
```
\bGr\u00f6nemeier&H\u00f6velberndt\s+E\u2011Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Milan Händlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `41e4c5a7`  
**Description:**
Matches the specific entity 'Milan Händlein'.

**Content:**
```
\bMilan\s+H\u00e4ndlein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Annemie Bott`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c7f29664`  
**Description:**
Matches the specific entity 'Annemie Bott'.

**Content:**
```
\bAnnemie\s+Bott\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Krolitzki`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `45df2358`  
**Description:**
Matches the specific entity 'Krolitzki Beratung'.

**Content:**
```
\bKrolitzki\s+Beratung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Manfredo Herrschmann`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ff59234b`  
**Description:**
Matches the specific entity 'Manfredo Herrschmann'.

**Content:**
```
\bManfredo\s+Herrschmann\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company StadtEnergie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `16526f53`  
**Description:**
Matches the specific entity 'StadtEnergie Holding'.

**Content:**
```
\bStadtEnergie\s+Holding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Laskowsky`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9a352a4b`  
**Description:**
Matches the specific entity 'Laskowsky Umwelt'.

**Content:**
```
\bLaskowsky\s+Umwelt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company TraunChemie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `467653e9`  
**Description:**
Matches the specific entity 'TraunChemie GMBH'.

**Content:**
```
\bTraunChemie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Butkus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a70a0e0b`  
**Description:**
Matches the specific entity 'Butkus Metall'.

**Content:**
```
\bButkus\s+Metall\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Englert`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7fb61038`  
**Description:**
Matches the specific entity 'Englert Möbel'.

**Content:**
```
\bEnglert\s+M\u00f6bel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Keldonbach`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e899b8a9`  
**Description:**
Matches the specific entity 'Keldonbach Sicherheit GMBH'.

**Content:**
```
\bKeldonbach\s+Sicherheit\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Sanitär Talder GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f257002`  
**Description:**
Matches the specific entity 'Sanitär Talder GMBH'.

**Content:**
```
Sanitär\s+Talder\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Roelfsen Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `11028e60`  
**Description:**
Matches the specific entity 'Roelfsen Versicherung'.

**Content:**
```
Roelfsen\s+Versicherung
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lubomir Merschmeyer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `91685d83`  
**Description:**
Matches the specific entity 'Lubomir Merschmeyer'.

**Content:**
```
Lubomir\s+Merschmeyer
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Houdek Maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e110e4b5`  
**Description:**
Matches the specific entity 'Houdek Maschinenbau'.

**Content:**
```
Houdek\s+Maschinenbau
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schmeltz Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `19a4f00e`  
**Description:**
Matches the specific entity 'Schmeltz Luftfahrt'.

**Content:**
```
Schmeltz\s+Luftfahrt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dorfcon-Verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cfe657a4`  
**Description:**
Matches the specific entity 'Dorfcon-Verlag'.

**Content:**
```
Dorfcon-Verlag
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lexdon IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3407167e`  
**Description:**
Matches the specific entity 'Lexdon IT'.

**Content:**
```
Lexdon\s+IT
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stadt Logglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `733a2290`  
**Description:**
Matches the specific entity 'Stadt Logglanz'.

**Content:**
```
Stadt\s+Logglanz
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gözcü Getränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a13a0930`  
**Description:**
Matches the specific entity 'Gözcü Getränke'.

**Content:**
```
Gözcü\s+Getränke
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hörup Gastronomie AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e6cc383`  
**Description:**
Matches the specific entity 'Hörup Gastronomie AG'.

**Content:**
```
Hörup\s+Gastronomie\s+AG
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dammke KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2e5c5578`  
**Description:**
Matches the specific entity 'Dammke KI GMBH'.

**Content:**
```
Dammke\s+KI\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TraunChemie GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e8d7d3d8`  
**Description:**
Matches the specific entity 'TraunChemie GMBH'.

**Content:**
```
TraunChemie\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tritri-IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3850ee07`  
**Description:**
Matches the specific entity 'Tritri-IT'.

**Content:**
```
Tritri-IT
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien 1/23`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `46c6a075`  
**Description:**
Matches 'Finanzamt Wien 1/23'.

**Content:**
```
Finanzamt\s+Wien\s+1/23
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Wien 1/23`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1446165d`  
**Description:**
Matches 'FA Wien 1/23'.

**Content:**
```
\bFA\s+Wien\s+1/23
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Naaß Elektro GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66e0c123`  
**Description:**
Matches the specific entity 'Naaß Elektro GMBH'.

**Content:**
```
Naaß\s+Elektro\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bersud Möbel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `86f251e0`  
**Description:**
Matches the specific entity 'Bersud Möbel GMBH'.

**Content:**
```
Bersud\s+Möbel\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Unter Heimdorf GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ad00504a`  
**Description:**
Matches the specific entity 'Unter Heimdorf GMBH'.

**Content:**
```
Unter\s+Heimdorf\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WXE Textil GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d0cea1d1`  
**Description:**
Matches the specific entity 'WXE Textil GMBH'.

**Content:**
```
WXE\s+Textil\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kornfelder Recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8cb601c4`  
**Description:**
Matches the specific entity 'Kornfelder Recycling'.

**Content:**
```
Kornfelder\s+Recycling
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `DGCV E-Commerce GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b90a5241`  
**Description:**
Matches the specific entity 'DGCV E-Commerce GMBH' (handling both en-dash and hyphen variants if necessary, but focusing on the text provided).

**Content:**
```
DGCV\s+E[\u2011-]Commerce\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UGQQ Verlag OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2e67d665`  
**Description:**
Matches the specific entity 'UGQQ Verlag OG'.

**Content:**
```
UGQQ\s+Verlag\s+OG
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fatima Finkenbein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d1b9dad6`  
**Description:**
Matches the specific entity 'Fatima Finkenbein' as an organization in this context.

**Content:**
```
Fatima\s+Finkenbein
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wien Waldnor KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e85980b6`  
**Description:**
Matches the specific entity 'Wien Waldnor KG'.

**Content:**
```
\bWien\s+Waldnor\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Botho Mikloweit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `28965f3f`  
**Description:**
Matches the specific entity 'Botho Mikloweit' as an organization in this context.

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

## `Kraftver-Gastronomie GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b775ac82`  
**Description:**
Matches the specific entity 'Kraftver-Gastronomie GMBH'.

**Content:**
```
\bKraftver-Gastronomie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gartgart Dienstleistungen GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `980b9a06`  
**Description:**
Matches the specific entity 'Gartgart Dienstleistungen GMBH'.

**Content:**
```
\bGartgart\s+Dienstleistungen\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gogel Daten GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `197e92cb`  
**Description:**
Matches the specific entity 'Gogel Daten GMBH'.

**Content:**
```
\bGogel\s+Daten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Klein-Vorholt KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `db01081f`  
**Description:**
Matches the specific entity 'Klein-Vorholt KI GMBH'.

**Content:**
```
\bKlein-Vorholt\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenkasse Retz-Pulkautal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b6b0b60b`  
**Description:**
Matches the specific entity 'Raiffeisenkasse Retz-Pulkautal'.

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

## `Nord Kellex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cb0cc520`  
**Description:**
Matches the specific entity 'Nord Kellex'.

**Content:**
```
\bNord\s+Kellex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4e1374bc`  
**Description:**
Matches the specific entity 'Norconheim'.

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

## `Specific Company Nexdorf-Metall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `24d13a6b`  
**Description:**
Matches the specific entity 'Nexdorf-Metall'.

**Content:**
```
\bNexdorf-Metall\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Oppert Elektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bf14d09e`  
**Description:**
Matches the specific entity 'Oppert Elektro'.

**Content:**
```
\bOppert\s+Elektro\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Zimmerhackel Bau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `271fecc4`  
**Description:**
Matches the specific entity 'Zimmerhackel Bau'.

**Content:**
```
\bZimmerhackel\s+Bau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Vahrenkamp Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `14ac09bd`  
**Description:**
Matches the specific entity 'Vahrenkamp Luftfahrt'.

**Content:**
```
\bVahrenkamp\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Gorius und Ziegann Event GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c03e94b9`  
**Description:**
Matches the specific entity 'Gorius und Ziegann Event GMBH'.

**Content:**
```
\bGorius\s+und\s+Ziegann\s+Event\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Raiffeisenbank Rion Vöcklabruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e8f5f0e9`  
**Description:**
Matches the specific entity 'Raiffeisenbank Rion Vöcklabruck'.

**Content:**
```
\bRaiffeisenbank\s+Rion\s+V\u00f6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Basdas Pharma AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9d77209f`  
**Description:**
Matches the specific entity 'Basdas Pharma AG'.

**Content:**
```
\bBasdas\s+Pharma\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Depp Versand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5ad4913c`  
**Description:**
Matches the specific entity 'Depp Versand'.

**Content:**
```
\bDepp\s+Versand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SüdEvent AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ca4bc5ae`  
**Description:**
Matches the specific entity 'SüdEvent AG'.

**Content:**
```
\bSüdEvent\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Obernöder+Küsbert Touristik GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4470d15c`  
**Description:**
Matches the specific entity 'Obernöder+Küsbert Touristik GMBH'.

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

## `Talost GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3beed63c`  
**Description:**
Matches the specific entity 'Talost GMBH'.

**Content:**
```
\bTalost\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt with location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a87b0377`  
**Description:**
Matches full names of tax authorities, ensuring 'Oststeiermark' and 'Salzburg-Stadt' are covered.

**Content:**
```
\bFinanzamt\s+(?:Steiermark\s+Mitte|Nieder\u00f6sterreich\s+Mitte|Salzburg-Land|Salzburg-Stadt|Vorarlberg|Waldviertel|Klosterneuburg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Innsbruck|Linz|Tirol\s+Ost|Bruck\s+Leoben\s+M\u00fcrzzuschlag|Braunau\s+Ried\s+Sch\u00e4rding|Grieskirchen\s+Wels|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Amstetten\s+Melk\s+Scheibbs|Kirchdorf\s+Perg\s+Steyr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Landeck\s+Reutte|Schwechat\s+Gerasdorf|Freistadt\s+Rohrbach\s+Urfahr|Purkersdorf|Wien\s+\d+/\d+(?:/\d+)*(?:/\d+)*|Gmunden\s+V\u00f6cklabruck|Wels\s+S\u00fcd|Oststeiermark|[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 55 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/8Ob31_24b`) (sent_id: `deanon_TRAIN/8Ob31_24b_20`)


C-545/18,DP/Finanzamt Linz, C-920/19,FluctusundFluentum;

**False Positives:**

- `Finanzamt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `FA abbreviation with location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d5845d57`  
**Description:**
Matches abbreviated tax authorities, ensuring 'Oststeiermark' and 'Salzburg-Stadt' are covered.

**Content:**
```
\bFA\s+(?:Steiermark\s+Mitte|Nieder\u00f6sterreich\s+Mitte|Salzburg-Land|Salzburg-Stadt|Vorarlberg|Waldviertel|Klosterneuburg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Innsbruck|Linz|Tirol\s+Ost|Bruck\s+Leoben\s+M\u00fcrzzuschlag|Braunau\s+Ried\s+Sch\u00e4rding|Grieskirchen\s+Wels|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Amstetten\s+Melk\s+Scheibbs|Kirchdorf\s+Perg\s+Steyr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Landeck\s+Reutte|Schwechat\s+Gerasdorf|Freistadt\s+Rohrbach\s+Urfahr|Purkersdorf|Wien\s+\d+/\d+(?:/\d+)*(?:/\d+)*|Gmunden\s+V\u00f6cklabruck|Wels\s+S\u00fcd|Oststeiermark|[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Inn-Recycling Institut GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b3da11b4`  
**Description:**
Matches the specific entity 'Inn-Recycling Institut GMBH'.

**Content:**
```
\bInn-Recycling\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `EnnsBildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c0c96d4e`  
**Description:**
Matches the specific entity 'EnnsBildung'.

**Content:**
```
\bEnnsBildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Olivier u. Bartha Recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c87f2aeb`  
**Description:**
Matches the specific entity 'Olivier u. Bartha Recycling'.

**Content:**
```
\bOlivier\s+u\.\s+Bartha\s+Recycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `West-Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `30f675c7`  
**Description:**
Matches the specific entity 'West-Luftfahrt'.

**Content:**
```
\bWest-Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Chen Setzekorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7c18768f`  
**Description:**
Matches the specific entity 'Chen Setzekorn'.

**Content:**
```
\bChen\s+Setzekorn\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Istvan Gerart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `80112cb8`  
**Description:**
Matches the specific entity 'Istvan Gerart'.

**Content:**
```
\bIstvan\s+Gerart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Berwaldkel-Möbel AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0faa5e01`  
**Description:**
Matches the specific entity 'Berwaldkel-Möbel AG'.

**Content:**
```
\bBerwaldkel-Möbel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c413d0ce`  
**Description:**
Matches district courts like 'Landesgericht Innsbruck'.

**Content:**
```
\bLandesgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 87 | 0 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 87 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Verfahrenshilfesache der Antragstellerin Florenzia Elefterakis, gegen den Antragsgegner Univ.-Prof. Dr. Leander Rossetti, wegen Bewilligung der Verfahrenshilfe, über den Antrag der Antragstellerin auf Delegierung der Rechtssache an das Landesgericht Korneuburg den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Rechtssache an das Landesgericht Korneuburg wird abgewiesen.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation
- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Florenzia Elefterakis`(person)
- `Dr. Leander Rossetti`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_4`)


Text Begründung: Die Antragstellerin richtete an das Landesgericht Linz einen Antrag auf Bewilligung der Verfahrenshilfe, weil sie gegen einen gerichtlichen Sachverständigen wegen eines in einem Pflegegeldprozess unrichtig erstatteten Gutachtens eine Schadenersatzklage auf Zahlung entgangenen Pflegegeldes und von Schmerzengeld erheben wolle.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_5`)


Das Landesgericht Linz leitete ein Verbesserungsverfahren ein.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_6`)


Die Antragstellerin beantwortete den schriftlichen Verbesserungsauftrag und beantragte die Delegierung des Verfahrens an das Landesgericht Korneuburg mit der Begründung, dass sie wegen ihrer körperlichen Behinderungen der Einladung der Richterin des Landesgerichts Linz, sie wegen offener Fragen bei Gericht aufzusuchen, nicht folgen könne.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_8`)


Das Landesgericht Linz äußerte sich zu diesem Antrag dahin, eine Delegierung könnte zweckmäßig sein, erscheine doch eine persönliche (ergänzende) Befragung der Antragstellerin zum Verfahrenshilfeantrag sinnvoll.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_3`)


Kopf Der Oberste Gerichtshof hat am 30. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz als weitere Richter in Gegenwart der Richterin Dr. Sadoghi als Schriftführerin in den Strafsachen gegen Peter Hanrich zu AZ 35 Hv 99/12a des Landesgerichts St. Pölten und zu AZ 5 U 42/16w des Bezirksgerichts Steyr, zwischen diesen Gerichten geführten Zuständigkeitsstreit nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag des Verurteilten auf nachträgliche Milderung der mit Urteil des Landesgerichts St. Pölten vom 3. September 2012, GZ 35 Hv 99/12a-16, ausgesprochenen Freiheitsstrafe ist das Landesgericht St. Pölten zuständig.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hanrich`(person)

**Example 6** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_12`)


Mit Note vom 17. Februar 2017 teilte das Landesgericht St. Pölten dem Bezirksgericht Steyr mit, „dass derAntrag offensichtlich auf nachträgliche Milderung der mit Urteil des BG Steyr vom 11.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_16`)


hinsichtlich des widerrufenen Teils aus der bedingten Entlassung zu AZ 38 BE 50/13x des Landesgerichts Steyr komme die Zuständigkeit jedoch dem Landesgericht St. Pölten zu, weil dieses in erster Instanz erkannt habe.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_18`)


Daraufhin übermittelte das Bezirksgericht Steyr die Akten dem Landesgericht St. Pölten mit dem Ersuchen um Äußerung zur Zuständigkeitsfrage im Sinn der Ausführungen des Obersten Gerichtshofs.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_19`)


Nunmehr legt das Landesgericht St. Pölten die Akten dem Obersten Gerichtshof vor, weil nach Ansicht des Einzelrichters der Antrag des Verurteilten nicht darauf abziele, „dass das Landesgericht St. Pölten das mit Urteil vom 03.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation
- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 11** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_23`)


12. 2013 zu 38 BE 50/13x gewährte bedingte Entlassung widerrufen wurde, dahingehend mildern möge, dass vom Widerruf abgesehen wird“, und sich das Landesgericht St. Pölten für diese „Milderung des Urteils des Bezirksgerichts Steyr durch Absehen vom Widerruf der bedingten Entlassung“ für nicht zuständig erachtet (ON 61 der Hv-Akten).

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_6`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 13. Juni 2019, AZ 28 Bl 68/19p, nicht Folge gegeben.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_4`)


Gründe:  Rechtliche Beurteilung Nach dem Norbert Naegelkraemer durch das Landesgericht Krems an der Donau am 4. Dezember 2015, GZ 16 Hv 32/15g-23, mehrerer Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB schuldig erkannt und zu einer teilbedingten Freiheitsstrafe verurteilt worden war, ordnete der Einzelrichter des genannten Landesgerichts nach Rechtskraft des Urteils die Zustellung der Aufforderung zum Strafantritt an den Verurteilten an.

**False Positives:**

- `Landesgericht Krems` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__5`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 17. Mai 2018, AZ 22 Bl 38/18f, 22 Bl 43/18s, nicht Folge gegeben.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_12`)


Bei der Glaubwürdigkeitsbeurteilung ließ das Erstgericht weder die Divergenzen in den Angaben der Asli Dawids (vgl US 14) noch ihre Verurteilung durch das Landesgericht Feldkirch unberücksichtigt (vgl US 16).

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dawids`(person)

**Example 17** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__8`)


Mit zugleich gefasstem Beschluss sprach das Landesgericht Innsbruck gemäß § 265 StPO - ebenfalls unter Bestimmung einer dreijährigen Probezeit - die bedingte Entlassung aus dem im Urteilszeitpunkt noch nicht (durch Anrechnung der Vorhaft) verbüßten (unbedingten) Strafteil von einem Monat, zwanzig Tagen und einer Stunde aus (ON 48, nicht journalisierte Kopie des genannten Urteils).

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__11`)


Unter einem fasste das Landesgericht Innsbruck den Beschluss, vom Widerruf der mit Urteil dieses Gerichts vom 6. März 2009, GZ 23 Hv 189/07m-104, gewährten bedingten Strafnachsicht abzusehen, die mit dem gemeinsam mit diesem Urteil ergangenen Beschluss gewährte bedingte Entlassung jedoch zu widerrufen (ON 49 S 3).

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__13`)


Mit - unbekämpft in Rechtskraft erwachsenem - Beschluss vom 3. Februar 2012 (ON 54) rechnete das Landesgericht Innsbruck „gem § 400 StPO“ die in der Zeit vom 13. Dezember 2011, 17:00 Uhr, bis zum 23. Jänner 2012, 17:00 Uhr, im Verfahren AZ 27 HR 323/11h (= 20 Hv 43/12b) des Landesgerichts Feldkirch erlittene Verwahrungs- und Untersuchungshaft auf die mit Urteil vom 10. Jänner 2012 (ON 49) verhängte Freiheitsstrafe an (1) und sprach aus, dass der nach dieser Anrechnung aus dem genannten Urteil und dem gleichzeitig mit diesem gefassten Widerrufsbeschluss verbleibende Strafrest von einem Monat und zehn Tagen unter Bestimmung einer Probezeit von drei Jahren „bedingt nachgesehen“ werde (2).

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__21`)


Da das Landesgericht Innsbruck hinsichtlich der mit - sogleich in Rechtskraft erwachsenem (ON 49 S 4) - Urteil vom 10. Jänner 2012 ausgesprochenen (ON 49 S 2) und der mit dem unter einem gefassten Widerrufsbeschluss aktualisierten (ON 49 S 3; siehe dazu aber (3) des Erkenntnisses) Freiheitsstrafe keine Strafvollzugsanordnung erließ, verletzte es somit § 397 erster Satz StPO iVm § 3 Abs 1 StVG.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__26`)


Ein Nachteil entstand der Verurteilten dadurch auch in Bezug auf die einen Monat übersteigende Untersuchungshaftzeit nicht, weil das Landesgericht Feldkirch zu AZ 20 Hv 43/12b - unter Missachtung des § 38 Abs 1 StGB - die vom Punkt 1 des Beschlusses des Landesgerichts Innsbruck vom 3. Februar 2012 (ON 54) umfasste Haftzeit (erneut zur Gänze) auf die im bezeichneten Verfahren verhängte (unbedingte) Freiheitsstrafe anrechnete.

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/14Os159_11f_14Os160_11b_`) (sent_id: `deanon_TRAIN/14Os159_11f_14Os160_11b__19`)


Das Landesgericht Wr. Neustadt hat durch seine Beschlussfassung auf Verlängerung der Probezeit nach § 494a Abs 6 StPO eine ihm nicht (mehr) zustehende Kompetenz in Anspruch genommen und solcherart den sich aus dem 16.

**False Positives:**

- `Landesgericht Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_3`)


Kopf Der Oberste Gerichtshof hat am 1. Februar 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in der Strafsache gegen Christian Enghardt wegen Überwachung von Entscheidungen über Bewährungsmaßnahmen, AZ 196 Ns 10/16y des Landesgerichts für Strafsachen Wien, über den Zuständigkeitsstreit zwischen diesem Gericht und dem Landesgericht Klagenfurt nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Enghardt`(person)

**Example 24** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_4`)


2005 den Beschluss gefasst:  Spruch Zur Führung des Verfahrens zur Überwachung der Entscheidungen des Amtsgerichts Zehdenick vom 25. November 2014, AZ 41 Ds 3101 Js 9050/14 (41/14), ist das Landesgericht Klagenfurt zuständig.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_5`)


Gründe:  Rechtliche Beurteilung Mit einem am 8. September 2016 beim Landesgericht Klagenfurt eingelangten Schreiben ersucht die Staatsanwaltschaft Neuruppin um „Übernahme der weiteren Strafvollstreckung der Gesamtfreiheitsstrafe“ und (der Sache nach nur) um Überwachung der Entscheidungen des Amtsgerichts Zehdenick (Deutschland) vom 25. November 2014, AZ 41 Ds 3101 Js 9050/14 (41/14), mit denen Christian Emanuelli wegen Diebstahls in besonders schwerem Fall und wegen Urkundenfälschung zu einer – für eine Bewährungszeit von fünf Jahren ausgesetzten – Gesamtfreiheitsstrafe von einem Jahr und neun Monaten verurteilt wurde und die Anordnung von Bewährungshilfe sowie die Erteilung von Weisungen erfolgten (ON 12).

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_6`)


Das Landesgericht Klagenfurt trat das Verfahren nach einer Melderegisterabfrage – derzufolge der Verurteilte zuletzt am 17. August 2016 in Klagenfurt gemeldet war und seither keine aufrechte Meldung aufweist (ON 13 S 3) – am 15. September 2016 „gemäß § 40a Abs 3 EU-JZG iVm § 40a Abs 2 zweiter Satz EU-JZG“ dem Landesgericht für Strafsachen Wien ab, weil Christian Ewersmann „nicht mehr im Sprengel des Landesgerichts Klagenfurt wohnhaft“ sei (ON 1 S 5).

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ewersmann`(person)

**Example 27** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_7`)


Dieses Gericht legte die Akten dem Obersten Gerichtshof gemäß § 38 StPO (iVm § 1 Abs 2 EU-JZG iVm § 9 Abs 1 ARHG) zur Entscheidung über einen negativen Kompetenzkonflikt vor, weil das Ersuchen der Staatsanwaltschaft Neuruppin nicht die Übernahme der Vollstreckung einer unbedingten Freiheitsstrafe betreffe und zufolge der besonderen Bindung des Verurteilten zu Klagenfurt und aufgrund des letzten Wohnsitzes ebendort „gemäß § 83 Abs 1 und 2 EU-JZG iVm § 1 Abs 2 EU-JZG iVm § 67 Abs 1 ARHG iVm § 9 ARHG iVm § 25 Abs 2 StPO“ das Landesgericht Klagenfurt zuständig sei.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_14`)


Da Christian Ernstschneider im Zeitpunkt des Einlangens des Ersuchens der deutschen Behörden keine aufrechte Meldung in Österreich aufwies und Anhaltspunkte dafür bestehen, dass auch der zuvor ständige Aufenthalt des Verurteilten in Klagenfurt nicht mehr gegeben ist (vgl das Erhebungsergebnis ON 18), hätte das Landesgericht Klagenfurt die Staatsanwaltschaft Neuruppin um Ergänzungen iSd § 84 Abs 2 Z 2 EU-JZG ersuchen müssen.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernstschneider`(person)

**Example 29** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_18`)


Liegt auch nach Durchführung des Ergänzungsverfahrens gemäß § 84 Abs 2 EU-JZG keiner der in § 83 Abs 2 EU-JZG genannten Anknüpfungspunkte vor, hat das von der ersuchenden Behörde als zuständig behauptete angerufene Gericht (hier: das Landesgericht Klagenfurt) die begehrte Überwachung mit Blick auf § 82 Abs 1 und 2 EU-JZG abzulehnen.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in Punkt A./2./ des Schuldspruchs sowie im Strafausspruch aufgehoben und es wird die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/15Os97_10v`) (sent_id: `deanon_TRAIN/15Os97_10v_11`)


Das Landesgericht Innsbruck als Berufungsgericht gab dieser Berufung der Staatsanwaltschaft wegen des Ausspruchs über die Strafe schließlich mit Urteil vom 9. März 2010, AZ 21 B1 478/09s (= ON 26 im Erkenntnisakt) Folge und erhöhte die Freiheitsstrafe auf drei Monate.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/1Nc10_18p`) (sent_id: `deanon_TRAIN/1Nc10_18p_4`)


Text Begründung: Das Landesgericht Klagenfurt entzog mit Beschluss vom 28.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Landesgericht Wiener Neustadt` — no gold match — likely missing annotation
- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)

**Example 34** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_7`)


Die Klägerin begehrte die Delegierung des Verfahrens gemäß § 31 JN an das Landesgericht Feldkirch.

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_23`)


Im vorliegenden Fall haben sowohl die Klägerin als auch das vorlegende Gericht zutreffend auf jene Umstände hingewiesen, die insgesamt eine Delegierung an das Landesgericht Feldkirch zweckmäßig erscheinen lassen (vgl dazu RIS-Justiz RS0046540), kann doch vor diesem Gericht unter Wahrung des Unmittelbarkeitsgrundsatzes das gesamte Beweisverfahren in einem Zug durchgeführt werden, was typischerweise nicht nur zu einer Erleichterung der Gerichtstätigkeit, sondern auch zu einer Verbilligung und Verkürzung des Verfahrens führt.

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben Amtshaftungsanspr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_6`)


Nach Zurück- bzw Abweisung seiner Begehren in erster Instanz lehnte er wiederholt Richter des Landesgerichts Leoben und des Oberlandesgerichts Graz erfolglos ab (vgl Landesgericht Leoben 2 Nc 24/11d, 2 Nc 25/11a, 2 Nc 28/11t;

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_9`)


Am 26. Februar 2013 lehnte er den Vorsitzenden des Ablehnungssenats beim Landesgericht Leoben als befangen und nach Zurückweisung dieses Antrags (2 Nc 3/13v) die Entscheidungsträger dieses Beschlusses als befangen ab.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_11`)


Diese Ablehnung wies der Ablehnungssenat beim Landesgericht Leoben (ohne Beteiligung des abgelehnten Richters) mit Beschluss vom 4. Dezember 2013, 2 Nc 31/13m, zurück.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d__5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben Amtshaftungsanspr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 42** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_109`)


Nr 18/2008 habe ein anderer Senat des Oberlandesgerichts Linz bzw das Landesgericht Salzburg die dort geregelten Pflegeaufwandsätze zuerkannt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_11`)


Seine am 4. Februar 2009 eingebrachte Oppositionsklage, deren Begehren darauf abzielt, dass der Anspruch der Beklagten aus dem Unterhaltsvergleich „sowie auf Unterhalt insgesamt“ erloschen ist, stützt derKlägerzusammengefasst auf eine Unterhaltsverwirkung iSd § 94 Abs 2 Satz 2 ABGB: Die Beklagte habe in dem gegen den Kläger geführten Strafverfahren vor dem Landesgericht Salzburg (31 Hv 139/07k), bezogen auf einen Vorfall am 3. Jänner 2006, unrichtig ausgesagt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_21`)


Unter anderem aufgrund dieses Vorfalls wurde der Kläger im Strafverfahren vor dem Landesgericht Salzburg wegen des Vergehens des Imstichlassens eines Verletzten nach § 94 StGB angeklagt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/3Ob203_11s`) (sent_id: `deanon_TRAIN/3Ob203_11s_14`)


Mit Beschluss des Landesgerichts Salzburg vom 18. Mai 2011, AZ 22 R 192/11f, 22 R 193/11b, wies das Landesgericht Salzburg die Berufung der Antragsteller mit der Begründung zurück, sie seien im Verfahren mehrfach und umfassend darüber belehrt worden, dass die von ihnen angestrebte Umbestellung der Verfahrenshelfer mangels Vorliegens der gesetzlichen Voraussetzungen nicht stattfinden könne.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/3Ob204_13s`) (sent_id: `deanon_TRAIN/3Ob204_13s_5`)


Text Begründung: Der Kläger brachte gegen den in Graz ansässigen Beklagten beim Landesgericht für Zivilrechtssachen Graz eine Schadenersatzklage über 62.769,86 EUR ein und beantragte gleichzeitig die Delegierung gemäß § 31 JN an das Landesgericht Klagenfurt.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/3Ob204_13s`) (sent_id: `deanon_TRAIN/3Ob204_13s_13`)


Gegen diese Entscheidung richtet sich der Rekurs des Klägers, mit dem er weiterhin die Delegierung an das Landesgericht Klagenfurt anstrebt.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_6`)


Mit rechtskräftigem Urteil vom 10. Mai 2007, AZ 19 Cg 136/06a, hat das Landesgericht Leoben infolge erfolgreicher Irrtumsanfechtung (im Hinblick auf die fehlende Vorschadensfreiheit des Fahrzeugs) die nunmehrige Oppositionsklägerin schuldig erkannt, an Philippa Carau Zug um Zug gegen Rückgabe des Pkw einen Betrag von 71.320 EUR sA zu bezahlen.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Philippa Carau`(person)

**Example 49** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_6`)


Text Begründung: Am 4. Oktober 2010 erließ das Landesgericht Mailand (Tribunale Ordinario di Milano) über Antrag der Betreibenden, einer Gesellschaft mit Sitz in Italien, den elektronischen Mahnbescheid (decreto ingiunitivo telematico) zur Zahl 34300/2010, mit dem der Verpflichteten, einer GmbH mit Sitz in Wien, die in Geschäftsverbindung mit der Betreibenden stand, die Zahlung von 522.094,53 EUR sA an die Betreibende innerhalb von 50 Tagen nach Bekanntmachung des Mahnbescheids aufgetragen wurde.

**False Positives:**

- `Landesgericht Mailand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_7`)


Dieser enthielt den Hinweis, dass die Verpflichtete Anspruch darauf habe, vor dem Landesgericht Mailand innerhalb von 50 Tagen nach der Bekanntmachung Einspruch zu erheben, widrigenfalls der Mahnbescheid für endgültig und vollstreckbar erklärt werde.

**False Positives:**

- `Landesgericht Mailand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_11`)


[3] Die vom Beklagten entsprechend dem Wunsch und über ausdrücklichen Auftrag der Klägerin im Mai 2017 beim Landesgericht Salzburg eingebrachte Werklohnklage gegen die in Deutschland ansässige Bauherrschaft wurde wegen fehlender internationaler Zuständigkeit zurückgewiesen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_12`)


Der Klägerin war bei Klagseinbringung bewusst, dass die Werklohnforderung gegenüber der Bauherrschaft bereits verjährt und das Landesgericht Salzburg unzuständig sein könnte.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_43`)


Vielmehr war der Klägerin bei Klagseinbringung bewusst, dass die Werklohnforderung gegenüber der Bauherrschaft bereits verjährt und das Landesgericht Salzburg unzuständig sein könnte.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation
- `Landesgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Rudigkeit Finanzen GmbH`(organisation)
- `Ing. Sascha Rohkrämer`(person)
- `Suddorftra Manufaktur GmbH`(organisation)
- `Ludmilla Nottelmann`(person)

**Example 55** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_6`)


Die Klägerin brachte beim Landesgericht Innsbruck eine Unterlassungs- und Zahlungsklage ein.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_11`)


Nach Einbringen der Klagebeantwortung beantragte sie die Delegierung an das „Landesgericht Wien“.

**False Positives:**

- `Landesgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/4Ob68_14z`) (sent_id: `deanon_TRAIN/4Ob68_14z_22`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_10`)


Die Streitteile hätten außerdem keine Gerichtsstandvereinbarung getroffen, weshalb das Landesgericht Klagenfurt zuständig sei.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_11`)


Der Kläger räumte daraufhin ein, dass die Forderungen gemäß § 55 JN zusammenzurechnen seien, und stellte für den Fall, dass sich das Bezirksgericht Salzburg für unzuständig erklärt, den Antrag, die Klage an das nicht offenbar unzuständige Landesgericht Salzburg zu überweisen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_12`)


Für den Fall der Unzuständigkeit dieses Landesgerichts beantragte er die Überweisung an das Landesgericht Klagenfurt, allenfalls an das Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_13`)


Das Bezirksgericht Salzburg sprach mit rechtskräftigem Beschluss vom 6. Dezember 2019 seine sachliche Unzuständigkeit aus und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Salzburg.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_14`)


Das Landesgericht Salzburg erklärte sich mit dem in der Verhandlung am 15. Jänner 2020 verkündeten Beschluss für örtlich unzuständig und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Klagenfurt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation
- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 63** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_16`)


Mit rechtskräftigem Beschluss vom 23. Jänner 2020 wies das Landesgericht Klagenfurt die Klage wegen sachlicher Unzuständigkeit zurück, weil ein Vorbringen in der Klage, wonach die Ansprüche zusammenzurechnen seien, nicht erstattet worden sei.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_17`)


Über Antrag des Klägers hob das Landesgericht Klagenfurt die Zurückweisung der Klage mit rechtskräftigem Beschluss vom 14. Februar 2020 auf und überwies die Rechtssache dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_19`)


Das Landesgericht Klagenfurt sei an den Unzuständigkeitsbeschluss des Bezirksgerichts Salzburg betreffend die sachliche Unzuständigkeit der Bezirksgerichte gebunden und habe daher seine sachliche Unzuständigkeit, mit der Begründung ein Bezirksgericht sei zuständig, nicht mehr aussprechen können.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_24`)


Zwar haben hier das Bezirksgericht Salzburg, das Landesgericht Salzburg, das Landesgericht Klagenfurt und das Bezirksgericht Spittal an der Drau jeweils seine Zuständigkeit verneint.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation
- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 67** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_25`)


Allerdings besteht ein Streit über die Zuständigkeit iSd § 47 Abs 1 JN nur zwischen dem Landesgericht Klagenfurt und dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Lovrek sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Dr. Sean Schoenenborn, gegen die beklagte Partei Dr. Hagen Kanat, vertreten durch Eisenberger & Herzog Rechtsanwalts GmbH in Graz, wegen 234.164,98 EUR sA, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, gemäß § 31 JN anstelle des Landesgerichts für Zivilrechtssachen Graz das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben, zur Verhandlung und Entscheidung dieser Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht Wiener Neustadt` — no gold match — likely missing annotation
- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Sean Schoenenborn`(person)
- `Dr. Hagen Kanat`(person)

**Example 69** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_6`)


Der Kläger beantragte die Delegation der Rechtsache an das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben.

**False Positives:**

- `Landesgericht Wiener Neustadt` — no gold match — likely missing annotation
- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 70** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Landesgericht Landesgericht Klagenfurt` — partial — gold is substring of pred: `Landesgericht Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN912691n`(business_register_number)
- `Landesgericht Klagenfurt`(organisation)
- `Holtschmidt Versicherung GmbH`(organisation)
- `LG Wels`(organisation)
- `Lohneis Pflege gesellschaft mbH`(organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich`(address)

**Example 71** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_9`)


Dagegen erhob der Ablehnungswerber Rekurs an das Landesgericht Leoben, mit dem er die Ablehnung von Richtern der Rechtsmittelsenate in Zivilrechtssachen verband.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_10`)


Gegen die im Ablehnungsverfahren vor dem Landesgericht Leoben ergangene Entscheidung (GZ 2 Nc 20/10i-3) erhob er Rekurs an das Oberlandesgericht Graz, den er mit einer Ablehnung „sämtlicher Richter des Oberlandesgerichts im Zivilrechtsberufungssenat mit Ausnahme von Dr. Florentine Fromeyer “ verband.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Florentine Fromeyer`(person)

**Example 73** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_7`)


Das Landesgericht Innsbruck eröffnete mit Beschluss vom 24.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_4`)


Text Begründung: Mit ihrer am 22. 12. 2015 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Klage begehrt die in Kagraner Anger 19, 4943 Nonsbach, Österreich (Sbg) ansässige Klägerin vom in Wien wohnhaften Beklagten die Zahlung einer Vertragsstrafe wegen mehrfacher Verstöße gegen das in seinem Agentenvertrag vereinbarte Wettbewerbsverbot.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kagraner Anger 19, 4943 Nonsbach, Österreich`(address)

**Example 75** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_14`)


Das Landesgericht Salzburg als Arbeits- und Sozialgericht sei auch mit den Rechtsangelegenheiten und regelmäßig gleichlautenden Vertragsgrundlagen und Provisions-abrechnungen der Klägerin seit Jahren vertraut.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_15`)


Auch das Landesgericht Salzburg als Arbeits- und Sozialgericht gab im Ergebnis nach Abwägung von Für und Wider eine negative Stellungnahme ab.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_18`)


Am 15. 2. 2016 übermittelte das Landesgericht Salzburg als Arbeits- und Sozialgericht im Nachhang eine von der Klägerin am 8.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_35`)


Zu bedenken ist auch, dass das Landesgericht Salzburg als Arbeits- und Sozialgericht bereits eine Tagsatzung abgehalten und das Prozessprogramm festgelegt hat und mit der Problematik auch aus einem anderen Verfahren vertraut ist, während sich ein Wiener Gericht neu in die Sache einzuarbeiten hätte.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Raiffeisen Rionalbank Hall in Tirol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8193c833`  
**Description:**
Matches the specific entity 'Raiffeisen Rionalbank Hall in Tirol'.

**Content:**
```
\bRaiffeisen\s+Rionalbank\s+Hall\s+in\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `General KG Company`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `251b6b11`  
**Description:**
Matches companies ending in KG, excluding 'Co KG' false positives and 'Firma' prefix.

**Content:**
```
(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&]*(?:\s+[A-Z][a-zA-Z0-9+&]*)*\s+KG)(?=\s|$|\)|\]|\"|\'|,|\.|;)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 33 | 0 | 33 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 33 | 318 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Energie Conwald GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob28_17s`) (sent_id: `deanon_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Jaroslaw Mlynarik, geboren am 1. Juli 2009, wegen Kontaktrechts des Vaters Dr. Eckard Tschernig, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Bettina Makswietat, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Partner KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jaroslaw Mlynarik`(person)
- `1. Juli 2009`(date)
- `Dr. Eckard Tschernig`(person)
- `Dr. Bettina Makswietat`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Contra GmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation
- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Beinicke`(person)
- `Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Szczech vertretenen Inn Triconal Holding GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Szczech`(person)
- `Inn Triconal Holding GesmbH`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Volkmar Acar KG, FN FN823951l, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Nemtschok Touristik “ Wilnorlex Werke gmbH, FN FN545761v, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei VetR Volkmar Acar KG` — partial — gold is substring of pred: `VetR Volkmar Acar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VetR Volkmar Acar`(person)
- `FN823951l`(business_register_number)
- `Nemtschok Touristik`(organisation)
- `Wilnorlex Werke gmbH`(organisation)
- `FN545761v`(business_register_number)

**Example 10** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 11** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 12** (doc_id: `deanon_TRAIN/2Ob193_23f`) (sent_id: `deanon_TRAIN/2Ob193_23f_5`)


Kff. Magdalena Münsterberg, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Gisela Ammenn, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Co KG` — no gold match — likely missing annotation
- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Gisela Ammenn`(person)

**Example 13** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `LLP Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 14** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Co KG` — no gold match — likely missing annotation
- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

**Example 15** (doc_id: `deanon_TRAIN/3Ob223_19v`) (sent_id: `deanon_TRAIN/3Ob223_19v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Özbolat Forschung GesmbH, KommR James Anthis, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die verpflichtete Partei Dkfm.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Özbolat Forschung GesmbH`(organisation)
- `KommR James Anthis`(person)

**Example 16** (doc_id: `deanon_TRAIN/4Ob119_22m`) (sent_id: `deanon_TRAIN/4Ob119_22m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek sowie die Hofräte Dr. Schwarzenbacher, Dr. Nowotny und Hon.-Prof. PD Dr. Rassi und die Hofrätin Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Hartwig Schimmangk KG, Pawel Lorenczyk, vertreten durch Dr. Franz Krainer, Rechtsanwalt in Graz, gegen die beklagte Partei Wien Bachtal GmbH, Kai Mündelein, vertreten durch die Hohenberg Rechtsanwälte GmbH in Graz, wegen 84.521,61 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz vom 12. Mai 2022, GZ 5 R 170/21s-33, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Hartwig Schimmangk KG` — partial — gold is substring of pred: `Hartwig Schimmangk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hartwig Schimmangk`(person)
- `Pawel Lorenczyk`(person)
- `Wien Bachtal GmbH`(organisation)
- `Kai Mündelein`(person)

**Example 17** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Klingenbeil Versand GmbH`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ruggenthaler Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JQV Finanzen Gruppe GmbH`(organisation)
- `Innovationsplatz 79, 9751 Nigglai, Österreich`(address)

**Example 19** (doc_id: `deanon_TRAIN/4Ob56_14k`) (sent_id: `deanon_TRAIN/4Ob56_14k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Andrea Schliekermann KG, Veit Faustmann, vertreten durch Dr. Ludwig Beurle und andere Rechtsanwälte in Linz, gegen die beklagte Partei Boerrigter Planung GmbH, Edith Merschmeier, vertreten durch Univ.-Prof. Dr. Bruno Binder und andere Rechtsanwälte in Linz, wegen 101.736,01 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Februar 2014, GZ 6 R 12/14y-69, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Andrea Schliekermann KG` — partial — gold is substring of pred: `Andrea Schliekermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andrea Schliekermann`(person)
- `Veit Faustmann`(person)
- `Boerrigter Planung GmbH`(organisation)
- `Edith Merschmeier`(person)

**Example 20** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 21** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OMedR Louisa Dutzke`(person)
- `Alsud-Pflege GmbH`(organisation)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich`(address)

**Example 22** (doc_id: `deanon_TRAIN/5Ob71_24p`) (sent_id: `deanon_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ignaz Schaufel, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Mur Waldbach GmbH, StR Martin Leitenbauer, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ignaz Schaufel`(person)
- `Mur Waldbach GmbH`(organisation)
- `StR Martin Leitenbauer`(person)

**Example 23** (doc_id: `deanon_TRAIN/6Ob146_18s`) (sent_id: `deanon_TRAIN/6Ob146_18s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paolo Weinrich, vertreten durch Mag. Max Verdino und andere Rechtsanwälte in St. Veit an der Glan, gegen die beklagte Partei Oberüber&Spanjardt Landwirtschaft GmbH, Karola Löcke, vertreten durch PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG in Wien, wegen 18.664,48 EUR und Feststellung, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 6. Juni 2018, GZ 4 R 51/18d-12, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2018, GZ 28 Cg 75/17s-8, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Paolo Weinrich`(person)
- `Oberüber&Spanjardt Landwirtschaft GmbH`(organisation)
- `Karola Löcke`(person)

**Example 24** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

**Example 25** (doc_id: `deanon_TRAIN/9Ob10_21t`) (sent_id: `deanon_TRAIN/9Ob10_21t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte Dr. Fichtenau, Hon.-Prof. Dr. Dehn, Dr. Hargassner, und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Schnake Robotik gmbh, Jeanne Großkopf, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Volkmar Kapelner GmbH, Reinberg-Litschau 11, 9343 Aich, Österreich, vertreten durch Advokatur Dr. Herbert Schöpf, LL.M., Rechtsanwalt-GmbH in Innsbruck, sowie die Nebenintervenientin auf Seiten der beklagten Partei EKFS Landwirtschaft AG & Co KG, Burgstallerstraße 10, 4892 Röth, Österreich, vertreten durch Hämmerle & Hübner Rechtsanwälte OG in Innsbruck, wegen 115.062,53 EUR sA, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 104.999,62 EUR sA) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Jänner 2021, GZ 3 R 76/20f-144, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schnake Robotik gmbh`(organisation)
- `Jeanne Großkopf`(person)
- `Volkmar Kapelner`(person)
- `Reinberg-Litschau 11, 9343 Aich, Österreich`(address)
- `EKFS Landwirtschaft AG`(organisation)
- `Burgstallerstraße 10, 4892 Röth, Österreich`(address)

**Example 26** (doc_id: `deanon_TRAIN/9Ob58_20z`) (sent_id: `deanon_TRAIN/9Ob58_20z_6`)


Die Beklagte ist eine Treuhandgesellschaft mit Sitz in Deutschland und Gründungskommanditistin einer deutschen GmbH & Co KG, deren Geschäftsgegenstand die Beteiligung an nicht börsenotierten Kapitalgesellschaften ist, die unter anderem Grundstücke entwickeln und verwalten.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/9Ob58_20z`) (sent_id: `deanon_TRAIN/9Ob58_20z_48`)


Nach den Feststellungen sollte sich der Kläger als Treugeber über die Beklagte an einer GmbH & Co KG beteiligen, welche wiederum bis zu 90 % der Anteile an einer Kapitalgesellschaft in den VAE erwerben sollte.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_4`)


Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Angelika Blochinger, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Laurence Klüs Gesellschaft m.b.H. (FN FN026367d ), FN434768w, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Angelika Blochinger`(person)
- `Laurence Klüs`(person)
- `FN026367d`(business_register_number)
- `FN434768w`(business_register_number)

**Example 29** (doc_id: `deanon_TRAIN/9ObA91_10p`) (sent_id: `deanon_TRAIN/9ObA91_10p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Dr. Hopf und Hon.-Prof Dr. Kuras sowie die fachkundigen Laienrichter Dr. Johannes Pflug und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Rudolfa Miekeley, vertreten durch Dr. Walter Silbermayr, Rechtsanwalt in Wien, gegen die beklagte Partei Immanuel Goess KG, Ulrike Gogulla, vertreten durch Mag. Jürgen Zahradnik, Rechtsanwalt in Lambach, wegen 9.198 EUR brutto sA (Revisionsinteresse 6.998,14 EUR), über die Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2010, GZ 9 Ra 22/10m-13, womit über Berufung der beklagten Partei das Zwischenurteil des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 3. September 2009, GZ 4 Cga 60/09a-9, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Immanuel Goess KG` — partial — gold is substring of pred: `Immanuel Goess`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rudolfa Miekeley`(person)
- `Immanuel Goess`(person)
- `Ulrike Gogulla`(person)

</details>

---

## `SüdVersand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d168562`  
**Description:**
Matches the specific entity 'SüdVersand'.

**Content:**
```
\bSüdVersand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank Wels Süd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `045672f7`  
**Description:**
Matches the specific entity 'Raiffeisenbank Wels Süd'.

**Content:**
```
\bRaiffeisenbank\s+Wels\s+Süd\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TraunLuftfahrt Solutions`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `410590b8`  
**Description:**
Matches the specific entity 'TraunLuftfahrt Solutions'.

**Content:**
```
\bTraunLuftfahrt\s+Solutions\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mittel-Logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `913a2c4e`  
**Description:**
Matches the specific entity 'Mittel-Logistik'.

**Content:**
```
\bMittel-Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fensudlog GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8cf2120f`  
**Description:**
Matches the specific entity 'Fensudlog GMBH'.

**Content:**
```
\bFensudlog\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Psomadakis Touristik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03c5bade`  
**Description:**
Matches the specific entity 'Psomadakis Touristik'.

**Content:**
```
\bPsomadakis\s+Touristik\b
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

