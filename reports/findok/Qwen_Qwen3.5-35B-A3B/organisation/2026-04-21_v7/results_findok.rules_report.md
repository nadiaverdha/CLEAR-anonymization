# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-21T18:14:27.516169

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-21_v7/config.yaml 
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
| Max rules | 30 |
| Max samples in prompt | 50 |
| Refinement iterations | 10 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | False |
| Enable Prune | True |
| Critic Interval | 0 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 40 |
| Refine per batch | 1 |
| Manually annotated examples | 1304 |
| First batch with manual data | 25 |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 90.9% |
| True Positives | 309 |
| False Positives | 24 |
| Micro Precision | 92.8% |
| Micro Recall | 17.7% |
| Micro F1 | 29.8% |
| Macro F1 | 29.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `ÖBB` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Mag. Ghesla Steuerberater GmbH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Education Institutions Consolidated` | 3.7% | 100.0% | 1.9% | 33 | 33 | 0 |
| `Organizations & Companies Consolidated` | 16.8% | 100.0% | 9.2% | 160 | 160 | 0 |
| `Specific Missing Companies 1` | 4.7% | 100.0% | 2.4% | 42 | 42 | 0 |
| `SENECURA` | 1.1% | 90.9% | 0.6% | 11 | 10 | 1 |
| `Tax Authorities (Finanzamt/FA)` | 4.7% | 89.4% | 2.4% | 47 | 42 | 5 |
| `Magistrat and Authorities` | 2.0% | 50.0% | 1.0% | 36 | 18 | 18 |
| `Magistrat and Authorities - Refined` | 2.0% | 50.0% | 1.0% | 36 | 18 | 18 |
| `London Film Academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundeskanzleramt Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missing Companies 2` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anonymized Companies (No GmbH)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Organizations & Companies Consolidated`

**F1:** 0.168 | **Precision:** 1.000 | **Recall:** 0.092  

**Format:** `regex`  
**Description:**
Added missing specific entities 'Gözcü Getränke' and 'Roelfsen Versicherung' to the list.

**Content:**
```
\b(?:Immobilienb\u00fcr\u00f6\s+Mandl|Garanta\s+VersicherungsAG|DA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG|Geschenkartikel\s+GmbH|AVED\s+cosmetic|Yoga\s+Vidya\s+GmbH|Rhein\s+Normonkel\s+Manufaktur\s+GMBH|Paugger\s+Steuerberatung\s+GmbH|Mittel\s+Unisyn\s+GMBH|Ober\s+Lemostnor\s+AG|Vennes\s+Recycling\s+AG|B\u00e4rs\s+&\s+Walterscheidt\s+Handel\s+GMBH|InnMarine\s+GMBH|Unter\s+Donunisee\s+AG|Raiffeisenbank\s+Karnische\s+Rion\s+\s+Bankstelle\s+St\.Stefan|Raiffeisenbank\s+Stallhofen|BDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.\b|Lubomir\s+Merschmeyer|LeitnerLeitner\s+GmbH\s+Wirtschaftspr\u00fcfer\s+und\s+Steuerberater|Houdek\s+Maschinenbau|Schmeltz\s+Luftfahrt|Dorfcon\-Verlag|Lexdon\s+IT|Betriebspr\u00fcfung\s+GmbH|Ikea|Obi|Leiner|M\u00f6belix|M\u00f6maX|Otto\.de|xxxLutz|Quelle\.at|Cervenka&Neun\u00fcbel\s+Telekom\s+AG|Bankhaus\s+Denzel|TAXCOACH\s+Wirtschaftspr\u00fcfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG|Lenfeld/Leys/Sonderegger\s+Rechtsanw\u00e4lte|The\s+International\s+Sivananda\s+Yoga\s+Vedanta\s+Centre|Kriminalpolizei\s+in\s+\u00d6sterreich|Tritri\-IT|G\u00f6zc\u00fc\s+Getr\u00e4nke|Roelfsen\s+Versicherung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.092 | 0.168 | 160 | 160 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 160 | 0 | 1410 |

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

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |
| `Obi` | `Obi` |
| `Leiner` | `Leiner` |
| `Möbelix` | `Möbelix` |
| `MömaX` | `MömaX` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |
| `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` | `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)


Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

</details>

---

## `Specific Missing Companies 1`

**F1:** 0.047 | **Precision:** 1.000 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches specific company names that were missing in training failures: Naaß Elektro, Bersud Möbel, Unter Heimdorf, KQPC Versand, Event Sudkraftlex, Sudver Handel, Glanznorost Institut, Mur Ververzor.

**Content:**
```
\b(?:Naaß\s+Elektro|Bersud\s+Möbel|Unter\s+Heimdorf|KQPC\s+Versand|Event\s+Sudkraftlex|Sudver\s+Handel|Glanznorost\s+Institut|Mur\s+Ververzor)\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.024 | 0.047 | 42 | 42 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 0 | 1561 |

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

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `Education Institutions Consolidated`

**F1:** 0.037 | **Precision:** 1.000 | **Recall:** 0.019  

**Format:** `regex`  
**Description:**
Merged: Rules 0a8a4dfd, 5cae2fc3, 2c622c19, 1fc37fb0, and c67c3dfa all target educational institutions (schools, universities). They are currently separate rules with 0 matches. Merging them into a single 'Education Institutions' rule reduces rule count and groups similar entities.

**Content:**
```
\b(?:Schule\s+f\u00fcr\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+(?:am\s+LKH\s+|in\s+)?Grillenreith|Gesundheits\-\s+und\s+Krankenpflege\-\s+Schule\s+am\s+LKH\s+Grillenreith\b|Karl\-Franzens\-\s+Universit\u00e4t\s+Graz\b|H\u00f6here\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit|HLF\s+Krems/Donau|H\u00f6heren\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit|Universit\u00e4t\s+Wien|University\s+of\s+Bristol|Universit\u00e4t\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.019 | 0.037 | 33 | 33 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 33 | 0 | 1643 |

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

</details>

---

## `SENECURA`

**F1:** 0.011 | **Precision:** 0.909 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches SeneCura and its variations including full names with Laurentius Park/Bludenz, handling case, hyphens, and spacing.

**Content:**
```
\b(?:SeneCura(?:\s+Laurentius\s+Park(?:\s+Bludenz)?)?|SENECURA|Senecura|SeneCura\s+Laurentius\-Park\s+Bludenz|SeneCura\s+Laurentius\s+Park\s+Bludenz|SeneCura\s+Laurentius\s+Park)\b
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

## `Tax Authorities (Finanzamt/FA)`

**F1:** 0.047 | **Precision:** 0.894 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches Finanzamt and FA abbreviations with specific Austrian city/region names found in training data.

**Content:**
```
\b(?:Finanzamt\s+(?:Steiermark\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Salzburg-Stadt|Österreich)|FA\s+(?:Steiermark\s+Mitte|Vorarlberg|Wien\s+2/20/21/22))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.894 | 0.024 | 0.047 | 47 | 42 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 5 | 1639 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Niklas Bußjann  in der Beschwerdesache ÖkR ÖkR Jonas Sternekicker,  Mühlbach 2, 4851 Fischhamering, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 15. Mai 2025  zu Steuernummer 98-117/5180  ausgefertigten Bescheid betreffend Einkommensteuer für  das Jahr 2024 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_50`)

**False Positives:**


Aufgrund dieses Sicherstellungsauftrages pfändete sie mit Bescheid  (Zahlungsverbot) vom 3.4.2024, adressiert an das Finanzamt Österreich (DST12), Dr. Adolf  Schärf Platz 2,1220 Wien, das der Beschwerdeführerin gegenüber dem Finanzamt Österreich  (DST12) zustehende Guthaben auf Steuernummer 01-186/7053.

FP: `Finanzamt Österreich` (organisation)


Aufgrund dieses Sicherstellungsauftrages pfändete sie mit Bescheid  (Zahlungsverbot) vom 3.4.2024, adressiert an das Finanzamt Österreich (DST12), Dr. Adolf  Schärf Platz 2,1220 Wien, das der Beschwerdeführerin gegenüber dem Finanzamt Österreich  (DST12) zustehende Guthaben auf Steuernummer 01-186/7053.

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)
- `Dr. Adolf  Schärf Platz 2,1220 Wien` (address)
- `Finanzamt Österreich  (DST12)` (organisation)
- `01-186/7053` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_52`)

**False Positives:**


Am  3.4.2024 wurde der Pfändungsbescheid (Zahlungsverbot) vom 3.4.2024 durch persönliche  Übernahme auch an das Finanzamt Österreich (DST12) zugestellt.

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_65`)

**False Positives:**


Die  Feststellungen zum Vorhalt betreffend den Umfang der Vollmacht gründen sich auf das  Schreiben der belangten Behörde vom 4.4.2024 und die hierauf ergangene Eingabe der  Beschwerdeführerin vom 16.4.2024 (beides von der Beschwerdeführerin vorgelegt), die  Feststellung zur Zustellung des Pfändungsbescheides an das Finanzamt Österreich (DST12) auf  die diesbezüglich von der belangten Behörde vorgelegte, mit einer Übernahmebestätigung  versehene Bescheidausfertigung (ebenfalls im Verfahren RV/702183/2024).

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_125`)

**False Positives:**


Damit fehlt dem Pfändungsbescheid vom 3.4.2024, der - anders als der  Sicherstellungsauftrag - durch die Zustellung an das Finanzamt Österreich (DST12) rechtlich  existent geworden ist (vgl. VwGH 9.6.2017, Ra 2017/02/0060), der Titel (vgl. VwGH 10.5.2010,  2009/16/0102;

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Magistrat and Authorities`

**F1:** 0.020 | **Precision:** 0.500 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches Magistrat and related authorities more precisely to avoid partial matches like 'Magistrats der Stadt Wien, Magistratsabteilung 6' being treated as a single entity if not intended, focusing on the core entity.

**Content:**
```
\bMagistrat(?:s)?\s+(?:der\s+Stadt\s+(?:Wien|Klagenfurt)|abteilung\s+\d+|der\s+Stadt\s+Bludenz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.010 | 0.020 | 36 | 18 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 18 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_15`)


Wegen Verletzung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 verhängte der Magistrat der Stadt Wien über den Bf. eine Geldstrafe in  Höhe € 75,00 (Ersatzfreiheitsstrafe 17 Stunden).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

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

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_13`)

**False Positives:**


In der Folge lastete der Magistrat der Stadt Wien, MA 67, nach durchgeführter Lenkererhebung  (Erteilung der Lenkerauskunft durch Zulassungsbesitzerin per E-Mail am 10. Juli 2025) mit  Strafverfügung vom 11. Juli 2025, zugestellt am 17. Juli 2025, GZ MA67/MA-GZ/2025, dem  Beschwerdeführer (kurz Bf.) an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen W-Kennz. (A) am 07. Mai 2025 um 11:59 Uhr in der gebührenpflichtigen  Kurzparkzone in 1050 Wien, Bacherplatz gegenüber 14, abgestellt, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `1050 Wien, Bacherplatz` (address)

</details>

---

## `Magistrat and Authorities - Refined`

**F1:** 0.020 | **Precision:** 0.500 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches Magistrat entities more precisely, focusing on 'Magistrat der Stadt X' and 'Magistratsabteilung Y' to avoid partial matches.

**Content:**
```
\bMagistrat(?:s)?\s+(?:der\s+Stadt\s+(?:Wien|Klagenfurt|Bludenz)|abteilung\s+\d+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.010 | 0.020 | 36 | 18 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 18 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_15`)


Wegen Verletzung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 verhängte der Magistrat der Stadt Wien über den Bf. eine Geldstrafe in  Höhe € 75,00 (Ersatzfreiheitsstrafe 17 Stunden).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

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

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_13`)

**False Positives:**


In der Folge lastete der Magistrat der Stadt Wien, MA 67, nach durchgeführter Lenkererhebung  (Erteilung der Lenkerauskunft durch Zulassungsbesitzerin per E-Mail am 10. Juli 2025) mit  Strafverfügung vom 11. Juli 2025, zugestellt am 17. Juli 2025, GZ MA67/MA-GZ/2025, dem  Beschwerdeführer (kurz Bf.) an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen W-Kennz. (A) am 07. Mai 2025 um 11:59 Uhr in der gebührenpflichtigen  Kurzparkzone in 1050 Wien, Bacherplatz gegenüber 14, abgestellt, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `1050 Wien, Bacherplatz` (address)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `London Film Academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and its common misspelling 'London Film Acadamy', handling variable whitespace.

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

## `Bundeskanzleramt Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramtes' (genitive form) which was missing from the federal ministry rules.

**Content:**
```
\bBundeskanzleramtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Missing Companies 2`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names: Trafenfen Automotive.

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

## `Anonymized Companies (No GmbH)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches anonymized company names like 'Mur Ververzor Betriebe' that do not have a standard suffix.

**Content:**
```
\b(?:Mur\s+Ververzor\s+Betriebe|Buhrfeindt\s+Lebensmittel\s+GMBH|Hinklein)\b
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

## `Organizations & Companies Consolidated`

**F1:** 0.168 | **Precision:** 1.000 | **Recall:** 0.092  

**Format:** `regex`  
**Description:**
Added missing specific entities 'Gözcü Getränke' and 'Roelfsen Versicherung' to the list.

**Content:**
```
\b(?:Immobilienb\u00fcr\u00f6\s+Mandl|Garanta\s+VersicherungsAG|DA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG|Geschenkartikel\s+GmbH|AVED\s+cosmetic|Yoga\s+Vidya\s+GmbH|Rhein\s+Normonkel\s+Manufaktur\s+GMBH|Paugger\s+Steuerberatung\s+GmbH|Mittel\s+Unisyn\s+GMBH|Ober\s+Lemostnor\s+AG|Vennes\s+Recycling\s+AG|B\u00e4rs\s+&\s+Walterscheidt\s+Handel\s+GMBH|InnMarine\s+GMBH|Unter\s+Donunisee\s+AG|Raiffeisenbank\s+Karnische\s+Rion\s+\s+Bankstelle\s+St\.Stefan|Raiffeisenbank\s+Stallhofen|BDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.\b|Lubomir\s+Merschmeyer|LeitnerLeitner\s+GmbH\s+Wirtschaftspr\u00fcfer\s+und\s+Steuerberater|Houdek\s+Maschinenbau|Schmeltz\s+Luftfahrt|Dorfcon\-Verlag|Lexdon\s+IT|Betriebspr\u00fcfung\s+GmbH|Ikea|Obi|Leiner|M\u00f6belix|M\u00f6maX|Otto\.de|xxxLutz|Quelle\.at|Cervenka&Neun\u00fcbel\s+Telekom\s+AG|Bankhaus\s+Denzel|TAXCOACH\s+Wirtschaftspr\u00fcfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG|Lenfeld/Leys/Sonderegger\s+Rechtsanw\u00e4lte|The\s+International\s+Sivananda\s+Yoga\s+Vedanta\s+Centre|Kriminalpolizei\s+in\s+\u00d6sterreich|Tritri\-IT|G\u00f6zc\u00fc\s+Getr\u00e4nke|Roelfsen\s+Versicherung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.092 | 0.168 | 160 | 160 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 160 | 0 | 1410 |

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

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |
| `Obi` | `Obi` |
| `Leiner` | `Leiner` |
| `Möbelix` | `Möbelix` |
| `MömaX` | `MömaX` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |
| `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` | `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)


Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

</details>

---

## `Specific Missing Companies 1`

**F1:** 0.047 | **Precision:** 1.000 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches specific company names that were missing in training failures: Naaß Elektro, Bersud Möbel, Unter Heimdorf, KQPC Versand, Event Sudkraftlex, Sudver Handel, Glanznorost Institut, Mur Ververzor.

**Content:**
```
\b(?:Naaß\s+Elektro|Bersud\s+Möbel|Unter\s+Heimdorf|KQPC\s+Versand|Event\s+Sudkraftlex|Sudver\s+Handel|Glanznorost\s+Institut|Mur\s+Ververzor)\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.024 | 0.047 | 42 | 42 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 0 | 1561 |

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

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `Tax Authorities (Finanzamt/FA)`

**F1:** 0.047 | **Precision:** 0.894 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches Finanzamt and FA abbreviations with specific Austrian city/region names found in training data.

**Content:**
```
\b(?:Finanzamt\s+(?:Steiermark\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Salzburg-Stadt|Österreich)|FA\s+(?:Steiermark\s+Mitte|Vorarlberg|Wien\s+2/20/21/22))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.894 | 0.024 | 0.047 | 47 | 42 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 5 | 1639 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Niklas Bußjann  in der Beschwerdesache ÖkR ÖkR Jonas Sternekicker,  Mühlbach 2, 4851 Fischhamering, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 15. Mai 2025  zu Steuernummer 98-117/5180  ausgefertigten Bescheid betreffend Einkommensteuer für  das Jahr 2024 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_50`)

**False Positives:**


Aufgrund dieses Sicherstellungsauftrages pfändete sie mit Bescheid  (Zahlungsverbot) vom 3.4.2024, adressiert an das Finanzamt Österreich (DST12), Dr. Adolf  Schärf Platz 2,1220 Wien, das der Beschwerdeführerin gegenüber dem Finanzamt Österreich  (DST12) zustehende Guthaben auf Steuernummer 01-186/7053.

FP: `Finanzamt Österreich` (organisation)


Aufgrund dieses Sicherstellungsauftrages pfändete sie mit Bescheid  (Zahlungsverbot) vom 3.4.2024, adressiert an das Finanzamt Österreich (DST12), Dr. Adolf  Schärf Platz 2,1220 Wien, das der Beschwerdeführerin gegenüber dem Finanzamt Österreich  (DST12) zustehende Guthaben auf Steuernummer 01-186/7053.

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)
- `Dr. Adolf  Schärf Platz 2,1220 Wien` (address)
- `Finanzamt Österreich  (DST12)` (organisation)
- `01-186/7053` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_52`)

**False Positives:**


Am  3.4.2024 wurde der Pfändungsbescheid (Zahlungsverbot) vom 3.4.2024 durch persönliche  Übernahme auch an das Finanzamt Österreich (DST12) zugestellt.

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_65`)

**False Positives:**


Die  Feststellungen zum Vorhalt betreffend den Umfang der Vollmacht gründen sich auf das  Schreiben der belangten Behörde vom 4.4.2024 und die hierauf ergangene Eingabe der  Beschwerdeführerin vom 16.4.2024 (beides von der Beschwerdeführerin vorgelegt), die  Feststellung zur Zustellung des Pfändungsbescheides an das Finanzamt Österreich (DST12) auf  die diesbezüglich von der belangten Behörde vorgelegte, mit einer Übernahmebestätigung  versehene Bescheidausfertigung (ebenfalls im Verfahren RV/702183/2024).

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_125`)

**False Positives:**


Damit fehlt dem Pfändungsbescheid vom 3.4.2024, der - anders als der  Sicherstellungsauftrag - durch die Zustellung an das Finanzamt Österreich (DST12) rechtlich  existent geworden ist (vgl. VwGH 9.6.2017, Ra 2017/02/0060), der Titel (vgl. VwGH 10.5.2010,  2009/16/0102;

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

</details>

---

## `Education Institutions Consolidated`

**F1:** 0.037 | **Precision:** 1.000 | **Recall:** 0.019  

**Format:** `regex`  
**Description:**
Merged: Rules 0a8a4dfd, 5cae2fc3, 2c622c19, 1fc37fb0, and c67c3dfa all target educational institutions (schools, universities). They are currently separate rules with 0 matches. Merging them into a single 'Education Institutions' rule reduces rule count and groups similar entities.

**Content:**
```
\b(?:Schule\s+f\u00fcr\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+(?:am\s+LKH\s+|in\s+)?Grillenreith|Gesundheits\-\s+und\s+Krankenpflege\-\s+Schule\s+am\s+LKH\s+Grillenreith\b|Karl\-Franzens\-\s+Universit\u00e4t\s+Graz\b|H\u00f6here\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit|HLF\s+Krems/Donau|H\u00f6heren\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit|Universit\u00e4t\s+Wien|University\s+of\s+Bristol|Universit\u00e4t\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.019 | 0.037 | 33 | 33 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 33 | 0 | 1643 |

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

</details>

---

## `Magistrat and Authorities`

**F1:** 0.020 | **Precision:** 0.500 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches Magistrat and related authorities more precisely to avoid partial matches like 'Magistrats der Stadt Wien, Magistratsabteilung 6' being treated as a single entity if not intended, focusing on the core entity.

**Content:**
```
\bMagistrat(?:s)?\s+(?:der\s+Stadt\s+(?:Wien|Klagenfurt)|abteilung\s+\d+|der\s+Stadt\s+Bludenz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.010 | 0.020 | 36 | 18 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 18 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_15`)


Wegen Verletzung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 verhängte der Magistrat der Stadt Wien über den Bf. eine Geldstrafe in  Höhe € 75,00 (Ersatzfreiheitsstrafe 17 Stunden).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

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

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_13`)

**False Positives:**


In der Folge lastete der Magistrat der Stadt Wien, MA 67, nach durchgeführter Lenkererhebung  (Erteilung der Lenkerauskunft durch Zulassungsbesitzerin per E-Mail am 10. Juli 2025) mit  Strafverfügung vom 11. Juli 2025, zugestellt am 17. Juli 2025, GZ MA67/MA-GZ/2025, dem  Beschwerdeführer (kurz Bf.) an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen W-Kennz. (A) am 07. Mai 2025 um 11:59 Uhr in der gebührenpflichtigen  Kurzparkzone in 1050 Wien, Bacherplatz gegenüber 14, abgestellt, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `1050 Wien, Bacherplatz` (address)

</details>

---

## `Magistrat and Authorities - Refined`

**F1:** 0.020 | **Precision:** 0.500 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches Magistrat entities more precisely, focusing on 'Magistrat der Stadt X' and 'Magistratsabteilung Y' to avoid partial matches.

**Content:**
```
\bMagistrat(?:s)?\s+(?:der\s+Stadt\s+(?:Wien|Klagenfurt|Bludenz)|abteilung\s+\d+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.010 | 0.020 | 36 | 18 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 18 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_15`)


Wegen Verletzung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 verhängte der Magistrat der Stadt Wien über den Bf. eine Geldstrafe in  Höhe € 75,00 (Ersatzfreiheitsstrafe 17 Stunden).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)

**False Positives:**


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

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

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_13`)

**False Positives:**


In der Folge lastete der Magistrat der Stadt Wien, MA 67, nach durchgeführter Lenkererhebung  (Erteilung der Lenkerauskunft durch Zulassungsbesitzerin per E-Mail am 10. Juli 2025) mit  Strafverfügung vom 11. Juli 2025, zugestellt am 17. Juli 2025, GZ MA67/MA-GZ/2025, dem  Beschwerdeführer (kurz Bf.) an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen W-Kennz. (A) am 07. Mai 2025 um 11:59 Uhr in der gebührenpflichtigen  Kurzparkzone in 1050 Wien, Bacherplatz gegenüber 14, abgestellt, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

FP: `Magistrat der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `1050 Wien, Bacherplatz` (address)

</details>

---

## `SENECURA`

**F1:** 0.011 | **Precision:** 0.909 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches SeneCura and its variations including full names with Laurentius Park/Bludenz, handling case, hyphens, and spacing.

**Content:**
```
\b(?:SeneCura(?:\s+Laurentius\s+Park(?:\s+Bludenz)?)?|SENECURA|Senecura|SeneCura\s+Laurentius\-Park\s+Bludenz|SeneCura\s+Laurentius\s+Park\s+Bludenz|SeneCura\s+Laurentius\s+Park)\b
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

## `ÖBB`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches ÖBB (Austrian Federal Railways).

**Content:**
```
\b\u00d6BB\b
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

## `Mag. Ghesla Steuerberater GmbH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific law firm 'Mag. Ghesla Steuerberater GmbH' which was missing in training failures.

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

## `London Film Academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and its common misspelling 'London Film Acadamy', handling variable whitespace.

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

## `Bundeskanzleramt Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramtes' (genitive form) which was missing from the federal ministry rules.

**Content:**
```
\bBundeskanzleramtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Missing Companies 2`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names: Trafenfen Automotive.

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

## `Anonymized Companies (No GmbH)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches anonymized company names like 'Mur Ververzor Betriebe' that do not have a standard suffix.

**Content:**
```
\b(?:Mur\s+Ververzor\s+Betriebe|Buhrfeindt\s+Lebensmittel\s+GMBH|Hinklein)\b
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

