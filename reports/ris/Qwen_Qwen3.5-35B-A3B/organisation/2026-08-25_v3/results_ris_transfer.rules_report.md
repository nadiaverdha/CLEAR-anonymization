# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (ris)

Generated on: 2026-08-25T21:30:49.278951

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-25_v3/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 100 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 160 |
| Validation documents | 40 |
| Test documents | 477 |
| Train sentences | 1706 |
| Validation sentences | 477 |
| Test sentences | 22727 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 5 |
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

**Transfer Learning**

| Property | Value |
|---|---|
| Seeded From | ris |
| Seed Rule Count | 24 |
| New Rules Added | 9 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 1351 |
| Phase1 Eval Sentences | 394 |
| Transfer Train Sentences | 355 |
| Transfer Eval Sentences | 83 |
| Best Batch Idx | 5 |
| Best Batch F1 | 0.8751987281399046 |
| Best Rules Serialized | [{'id': 'ca6e93fd', 'name': 'Courts', 'description': "Matches court names including 'Landesgerichts' with complex location suffixes like 'an der Donau' or 'St. Pölten', and handles genitive forms.", 'format': 'regex', 'content': '\\b(?:Verwaltungsgerichtshof(?:es)?|Bundesfinanzgericht(?:es)?|Bundesfinanzgerichts|B(?:undesfinanzgericht|FG)|Obersten\\s+Gerichtshof(?:es)?|Landesgericht(?:s)?\\s+(?:f\\u00fcr\\s+(?:Zivilrechtssachen|Strafsachen)?\\s+)?[A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)?(?:\\s+[A-Z][a-zA-Z]+)?(?:\\s+-\\s+[A-Z][a-zA-Z]+)?(?:\\s+an\\s+der\\s+Donau)?(?:\\s+St\\.\\sP\\u00f6lten)?|Gerichtshof\\sder\\sEurop\\u00e4ischen\\sUnion)(?:\\s*\\(\\s*BFG\\s*\\))?\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '03c11cff', 'name': 'GenericFirma', 'description': "Matches 'Firma' followed by a capitalized name that doesn't end in GmbH/m.b.H. (catching incomplete mentions or specific cases).", 'format': 'regex', 'content': '\\bFirma\\s+([A-Z][a-zA-Z0-9\\s]+?)(?=\\s*(?:in|mit|auf|der|die|das|ist|hat|ist|wurde|$))', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b57de570', 'name': 'TaxAuthorities', 'description': "Matches 'Finanzamt' (standalone or with genitive 'es') and specific location suffixes like 'Schwechat Gerasdorf' or 'Österreich'.", 'format': 'regex', 'content': '\\bFinanzamt(?:es)?(?:\\s+(?:Schwechat\\s+Gerasdorf|Österreich))?', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'fca60947', 'name': 'CompanyGmbH', 'description': "Matches company names ending in GmbH, AG, KG, OG, & Co KG, ensuring the match starts at the name and ends at the suffix, avoiding context like 'an der' or 'Kommanditbeteiligung'.", 'format': 'regex', 'content': '(?:^|\\s|\\(|,|\\.)\\s*([A-Z][a-zA-Z0-9\\s&+\\-]+(?:\\s+(?:GmbH|mbH|AG|Aktiengesellschaft|KG|OG|Partnerschaft|Rechtsanw\\u00e4lte(?:\\s+GmbH|\\s+OG|\\s+KG)?|Steuerberatungsgesellschaft|Wirtschaftspr\\u00fcfung|Consulting|Management|Service|Technik|International)))(?:\\s*&\\s*Co\\s*KG|\\s*\\(|\\s*$|\\s+[,\\.\\s]|\\s+\\))', 'priority': 12, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '3eb2075a', 'name': 'MinistryAbbreviations', 'description': 'Matches Bundesministeriums für Finanzen and its abbreviations BMF, BM für Finanzen.', 'format': 'regex', 'content': '\\b(?:Bundesministeriums\\sfür\\sFinanzen|BMF|BM\\sfür\\sFinanzen)\\b', 'priority': 7, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '0bce244b', 'name': 'MunicipalBodies', 'description': "Matches 'Magistrat der Stadt Wien' and 'Magistrates der Stadt Wien' variations, handling plural forms, extra spaces, and optional department suffixes.", 'format': 'regex', 'content': '\\b(?:Magistrat(?:es)?(?:\\s+der\\s+Stadt\\s+Wien(?:,\\s+Magistratsabteilung\\s+\\d+)?|der\\s+Stadt\\s+Wien)|Magistrates\\s+der\\s+Stadt\\s+Wien(?:,\\s+Magistratsabteilung\\s+\\d+)?)\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '3856d842', 'name': 'KAG', 'description': 'Matches the specific abbreviation KAG which appears frequently in the text as an organization.', 'format': 'regex', 'content': '\\bKAG\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '5d06e25b', 'name': 'BFH', 'description': 'Matches the German Federal Fiscal Court abbreviation BFH.', 'format': 'regex', 'content': '\\bBFH\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7652b5fe', 'name': 'PoliceAuthorities', 'description': "Matches 'Landespolizeidirektion' and similar police authority names, strictly bounded to prevent capturing trailing words.", 'format': 'regex', 'content': '\\bLandespolizeidirektion(?:\\s+(?:Wien))?\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8df62c8b', 'name': 'AMS', 'description': 'Matches the abbreviation AMS (Arbeitsmarktservice) as an organization.', 'format': 'regex', 'content': '\\bAMS\\b', 'priority': 7, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'ff333e7c', 'name': 'Verfassungsgerichtshof', 'description': 'Matches the Constitutional Court (Verfassungsgerichtshof) and its genitive form.', 'format': 'regex', 'content': '\\bVerfassungsgerichtshof(?:es)?\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e3c4aa61', 'name': 'Landesgericht', 'description': 'Matches Land Courts (Landesgericht) and its genitive form.', 'format': 'regex', 'content': '\\bLandesgericht(?:es)?\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8e381a0a', 'name': 'ÖGK', 'description': 'Matches the specific abbreviation ÖGK (Österreichische Gesundheitskasse) as an organization.', 'format': 'regex', 'content': '\\bÖGK\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b23075c0', 'name': 'TaxAuthorityFA', 'description': "Matches 'FA' followed by a location, ensuring the match stops before common prepositions or end of sentence to avoid capturing 'vom' or other trailing words.", 'format': 'regex', 'content': '\\bFA\\s+([A-Z][a-zA-Z\\s]+?)(?=\\s+(?:vom|am|des|der|in|an|bei|mit|nach|vor|über|unter|auf|zu|von|für|gegen|ohne|durch|seit|bis|um|an|bei|mit|nach|vor|über|unter|auf|zu|von|für|gegen|ohne|durch|seit|bis|um|\\.|,|\\)|\\]|\\s*$))', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '67e7c8f3', 'name': 'UniversityWien', 'description': "Matches 'Universität Wien' which was previously missing.", 'format': 'regex', 'content': '\\bUniversit\\u00e4t\\sWien\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '393052ea', 'name': 'MinistryBMI', 'description': "Matches 'BMI' (Bundesministerium für Inneres) as an organization.", 'format': 'regex', 'content': '\\bBMI\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '87469955', 'name': 'Pensionsversicherungsanstalt', 'description': "Matches the specific organization 'Pensionsversicherungsanstalt' which was missing.", 'format': 'regex', 'content': '\\bPensionsversicherungsanstalt\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '99ac9790', 'name': 'SKTelecom', 'description': "Matches 'SK Telecom' variations which appear frequently in legal texts regarding EU court cases.", 'format': 'regex', 'content': '\\bSK\\s+Telecom(?:\\s+Co\\.?\\s+Ltd)?\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '965ee445', 'name': 'WienerGemeinderat', 'description': "Matches 'Wiener Gemeinderat' and 'Wiener Gemeinderates' variations.", 'format': 'regex', 'content': '\\bWiener\\s+Gemeinderat(?:es)?\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'c51d21bb', 'name': 'BundesamtSoziales', 'description': "Matches 'Bundesamt für Soziales und Behindertenwesen'.", 'format': 'regex', 'content': '\\bBundesamt\\s+für\\s+Soziales\\s+und\\s+Behindertenwesen\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8d797d70', 'name': 'PostAG', 'description': "Matches 'Post AG' specifically to capture this common organization which was previously missed.", 'format': 'regex', 'content': '\\bPost\\s+AG\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7085fcac', 'name': 'COFAG', 'description': "Matches the specific organization COFAG (Corona-Fonds-Ausgleichsgesellschaft) which was frequently missed or incorrectly matched as part of 'COFAG-NoAG'.", 'format': 'regex', 'content': '\\bCOFAG\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '6d26651f', 'name': 'BHAG', 'description': 'Matches the specific organization BHAG (Bundeshaushaltsagentur) which was missed.', 'format': 'regex', 'content': '\\bBHAG\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '2157c7db', 'name': 'OGH', 'description': 'Matches the abbreviation OGH (Oberster Gerichtshof) which was frequently missed.', 'format': 'regex', 'content': '\\bOGH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '0dd1c9bb', 'name': 'ObersteGerichtshof', 'description': "Matches 'Oberste Gerichtshof', 'Obersten Gerichtshof', and the genitive 'Obersten Gerichtshofs'.", 'format': 'regex', 'content': '\\bOberste\\s+Gerichtshof\\b|\\bObersten\\s+Gerichtshof(?:es)?\\b|\\bObersten\\s+Gerichtshofs\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1d05c994', 'name': 'BezirksGericht', 'description': "Matches 'Bezirksgericht' and its genitive form 'Bezirksgerichts' with location suffixes including hyphenated names and multi-word locations like 'Graz-West' or 'Zell am See'.", 'format': 'regex', 'content': '\\bBezirksgericht(?:s)?\\s+(?:[A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)?(?:\\s+-\\s+[A-Z][a-zA-Z]+)?|Graz-Ost|Graz-West|Hernals|D\\u00f6bling|Favoriten|Ferlach|Korneuburg|Chisinau|Innere\\s+Stadt\\s+Wien|Salzburg|Bregenz|Hall\\s+in\\s+Tirol|Kitzb\\u00fchel|Wels|St\\.\\sP\\u00f6lten|Eisenstadt|Klagenfurt|Linz|Graz|Wien|Steyr|Feldkirch|Krems\\s+an\\s+der\\s+Donau|Wiener\\s+Neustadt|Zell\\s+am\\s+See|Bruck\\s+an\\s+der\\s+Mur|Innere\\s+Stadt)\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8adf3e88', 'name': 'Oberlandesgericht', 'description': "Matches 'Oberlandesgericht' and its genitive form 'Oberlandesgerichts' with location suffixes.", 'format': 'regex', 'content': '\\bOberlandesgericht(?:s)?\\s+(?:Wien|Graz|Innsbruck|Klagenfurt|Linz|Salzburg|Bregenz|Eisenstadt|St.\\sPölten)\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'c0420946', 'name': 'Handelsgericht', 'description': "Matches 'Handelsgericht' and its genitive form 'Handelsgerichts' with location suffixes.", 'format': 'regex', 'content': '\\bHandelsgericht(?:s)?\\s+(?:Wien|Graz|Linz|Salzburg|Innsbruck|Klagenfurt|Bregenz|Eisenstadt|St.\\sPölten)\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '92cfdcf2', 'name': 'VwGH', 'description': "Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof) which was frequently missed.", 'format': 'regex', 'content': '\\bVwGH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'bfed1f74', 'name': 'LawFirmOG', 'description': "Matches law firm names ending in 'Rechtsanwälte OG' or 'Rechtsanwälte-Partnerschaft' which were previously missed.", 'format': 'regex', 'content': '\\b[A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)*\\s+Rechtsanw\\u00e4lte\\s+(?:OG|Partnerschaft)\\b', 'priority': 14, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8e6374a6', 'name': 'LawFirmGmbH', 'description': "Matches law firm names ending in 'Rechtsanwälte GmbH' or 'Rechtsanwälte GmbH & Co KG'.", 'format': 'regex', 'content': '\\b[A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)*\\s+Rechtsanw\\u00e4lte\\s+GmbH(?:\\s*&\\s*Co\\s*KG)?\\b', 'priority': 14, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '12aa6f89', 'name': 'LandesgerichtComplex', 'description': "Matches 'Landesgericht' with complex location suffixes like 'für Zivilrechtssachen Graz' or 'St. Pölten' which were previously truncated.", 'format': 'regex', 'content': '\\bLandesgericht(?:s)?\\s+(?:f\\u00fcr\\s+(?:Zivilrechtssachen|Strafsachen)?\\s+)?[A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)?(?:\\s+[A-Z][a-zA-Z]+)?(?:\\s+-\\s+[A-Z][a-zA-Z]+)?(?:\\s+an\\s+der\\s+Donau)?(?:\\s+St\\.\\sP\\u00f6lten)?\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 97.6% |
| True Positives | 3340 |
| False Positives | 432 |
| False Negatives | 674 |
| Total Gold Entities | 4014 |
| Micro Precision | 88.5% |
| Micro Recall | 83.2% |
| Micro F1 | 85.8% |
| Macro F1 | 85.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `MunicipalBodies` | 0.4% | 100.0% | 0.2% | 8 | 8 | 0 |
| `Verfassungsgerichtshof` | 0.9% | 100.0% | 0.4% | 18 | 18 | 0 |
| `OGH` | 21.9% | 100.0% | 12.3% | 493 | 493 | 0 |
| `ObersteGerichtshof` | 55.5% | 100.0% | 38.4% | 1543 | 1543 | 0 |
| `Oberlandesgericht` | 17.0% | 100.0% | 9.3% | 373 | 373 | 0 |
| `Handelsgericht` | 1.7% | 100.0% | 0.8% | 34 | 34 | 0 |
| `VwGH` | 0.4% | 100.0% | 0.2% | 9 | 9 | 0 |
| `LandesgerichtComplex` | 22.6% | 95.4% | 12.8% | 539 | 514 | 25 |
| `LawFirmGmbH` | 1.7% | 77.3% | 0.8% | 44 | 34 | 10 |
| `LawFirmOG` | 1.0% | 76.9% | 0.5% | 26 | 20 | 6 |
| `BezirksGericht` | 10.6% | 75.7% | 5.7% | 301 | 228 | 73 |
| `GenericCompanyGmbH` | 3.0% | 20.5% | 1.6% | 322 | 66 | 256 |
| `Courts` | 0.0% | 0.0% | 0.0% | 16 | 0 | 16 |
| `GenericFirma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TaxAuthorities` | 0.0% | 0.0% | 0.0% | 14 | 0 | 14 |
| `CompanyGmbH` | 0.0% | 0.0% | 0.0% | 22 | 0 | 22 |
| `MinistryAbbreviations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PoliceAuthorities` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `AMS` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Landesgericht` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `ÖGK` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TaxAuthorityFA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UniversityWien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `MinistryBMI` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Pensionsversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `SKTelecom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WienerGemeinderat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BundesamtSoziales` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PostAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `COFAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BHAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `MunicipalBodies` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `0bce244b`  
**Description:**
Matches 'Magistrat der Stadt Wien' and 'Magistrates der Stadt Wien' variations, handling plural forms, extra spaces, and optional department suffixes.

**Content:**
```
\b(?:Magistrat(?:es)?(?:\s+der\s+Stadt\s+Wien(?:,\s+Magistratsabteilung\s+\d+)?|der\s+Stadt\s+Wien)|Magistrates\s+der\s+Stadt\s+Wien(?:,\s+Magistratsabteilung\s+\d+)?)\b
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

## `Verfassungsgerichtshof` 🏆

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `ff333e7c`  
**Description:**
Matches the Constitutional Court (Verfassungsgerichtshof) and its genitive form.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.009 | 18 | 18 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 3492 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_91`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_147`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_158`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_162`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/3Ob229_14v`) (sent_id: `deanon_260716_TRAIN/3Ob229_14v_44`)


Auch der Verfassungsgerichtshof hat in der vom Kläger zitierten Entscheidung B 97/91, B 284/91-303/91 (= VfSlg 13.006) zu einer - nicht dem § 38 Abs 6 OÖ ROG entsprechenden - Norm des früheren OÖ ROG 1972 eingeräumt, dass unter dem auch dort verwendeten Begriff „Grundstück“ nicht unbedingt nur ein einzelnes Grundstück verstanden werden kann, sondern gegebenenfalls auch mehrere Grundstücke, die miteinander eine „Einheit“ bilden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_51`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_147`)


3.2.6.Auch der Verfassungsgerichtshof hat sich bereits mehrfach (G 164/2014;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_152`)


Der Verfassungsgerichtshof führte allerdings aus, dass die Bestimmungen des Fern- und Auswärtsgeschäfte-Gesetzes den Vorschriften der Verbraucherrechte-RL entsprächen, welche den Mitgliedstaaten keinen Spielraum bei der Umsetzung einräumten;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_154`)


Auch von einem Vorabentscheidungsersuchen an den EuGH sah der Verfassungsgerichtshof ab (ErwG 74).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_155`)


Darüber hinaus setzte sich der Verfassungsgerichtshof in diesem Erkenntnis mit Art 14 Abs 2 der Verbraucherrechte-RL, der durch § 15 Abs 4 FAGG umgesetzt wurde, auseinander und äußerte keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz (entspricht § 15 Abs 4 letzter Satz FAGG): Der Verfassungsgerichtshof hat keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 11** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_159`)


Der Verfassungsgerichtshof kann nun nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL diesen von der Rechtsprechung des Gerichtshofes der Europäischen Union aufgestellten Kriterien im Rahmen der Verhältnismäßigkeitsprüfung eines Unionsrechtsakts widerspricht: Die Bestimmungen der Verbraucherrechte-RL verfolgen das Ziel eines umfassenden Verbraucherschutzes bei Fernabsatzverträgen und außerhalb von Geschäftsräumen geschlossenen Verträgen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_161`)


Der Verfassungsgerichtshof hat keine Zweifel, dass die in Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL normierte Rechtsfolge für den Unternehmer bei mangelnder Belehrung über das Widerrufsrecht geeignet ist, das Ziel des umfassenden Verbraucherschutzes bei Fernabsatzverträgen und bei außerhalb von Geschäftsräumen geschlossenen Verträgen zu erreichen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_162`)


Der Verfassungsgerichtshof kann auch nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL über das hinausgeht, was zur Verfolgung des mit der Regelung verfolgten Ziels des umfassenden Verbraucherschutzes erforderlich ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_165`)


Der Verfassungsgerichtshof hat sohin keine Zweifel an deren Gültigkeit.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 15** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Verfassungsgerichtshofs` (organisation)
- `ÖBB` (organisation)

</details>

---

## `OGH` 🏆

**F1:** 0.219 | **Precision:** 1.000 | **Recall:** 0.123  

**Format:** `regex`  
**Rule ID:** `2157c7db`  
**Description:**
Matches the abbreviation OGH (Oberster Gerichtshof) which was frequently missed.

**Content:**
```
\bOGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.123 | 0.219 | 493 | 493 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 493 | 0 | 3521 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 51** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 53** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 54** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 55** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 56** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 57** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 58** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 59** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 60** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bäseke` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Mag. Herwig Berto` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 63** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Oliver Pekarek` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 65** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Gerhard Bukowska` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 67** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bernts` (person)
- `Landesgerichts Linz` (organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 69** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Ahmed Koehnen` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)

**Example 70** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 71** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 80** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 81** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_3`)


Kopf Der Oberste Gerichtshof hat am 21. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Brenner über den von Ing. Sebastian Novko im Verfahren AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz gestellten Fristsetzungsantrag nach Einsichtnahme der Generalprokuratur in die Akten und Abstimmung gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Ing. Sebastian Novko` (person)
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 83** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 84** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 85** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 86** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 87** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 88** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 89** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 90** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 91** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 92** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 93** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 94** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 95** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 96** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 97** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 98** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 99** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

</details>

---

## `ObersteGerichtshof` 🏆

**F1:** 0.555 | **Precision:** 1.000 | **Recall:** 0.384  

**Format:** `regex`  
**Rule ID:** `0dd1c9bb`  
**Description:**
Matches 'Oberste Gerichtshof', 'Obersten Gerichtshof', and the genitive 'Obersten Gerichtshofs'.

**Content:**
```
\bOberste\s+Gerichtshof\b|\bObersten\s+Gerichtshof(?:es)?\b|\bObersten\s+Gerichtshofs\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.384 | 0.555 | 1543 | 1543 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1543 | 0 | 2470 |

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

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_23`)


Ohne rechtskräftigen Übertragungsbeschluss nach § 111 Abs 1 JN kommt eine Entscheidung des Obersten Gerichtshofs nach § 111 Abs 2 JN nicht in Betracht (RS0047067).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_24`)


Dies gilt jedenfalls dann, wenn das für die Entscheidung über einen Rekurs gegen den Übertragungsbeschluss zuständige Gericht mit dem zur Genehmigung nach § 111 Abs 2 JN berufenen Gericht (hier der Oberste Gerichtshof) nicht ident ist (RS0047067 [T14]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_6`)


Rechtliche Beurteilung Nach § 28 Abs 1 Z 2 JN hat der Oberste Gerichtshof, wenn für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts im Sinne dieses Gesetzes oder einer anderen Rechtsvorschrift nicht gegeben oder nicht zu ermitteln sind, aus den sachlich zuständigen Gerichten eines zu bestimmen, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn unter anderem der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_7`)


Der Oberste Gerichtshof hat in gleich gelagerten Fällen (4 Nc 11/19h, 6 Nc 1/19b, 7 Nc 23/19w) die Ordination bewilligt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


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

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_14`)


An die rechtskräftige Verneinung der internationalen Zuständigkeit des vom Kläger angerufenen Bezirksgerichts Schwechat ist der Oberste Gerichtshof gebunden (RIS-Justiz RS0046568).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgerichts Schwechat` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_16`)


Für den Fall, dass für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts nicht gegeben oder nicht zu ermitteln sind, bestimmt § 28 Abs 1 Z 2 JN, dass der Oberste Gerichtshof aus den sachlich zuständigen Gerichten eines zu bestimmen hat, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_21`)


[7] 4.1 Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (zB 6 Nc 1/19b ZVR 2019/114, 259 [Mayr];

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


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

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


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

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_40`)


2.2. Die Ansicht vonMayr(Die Delegation im zivilgerichtlichen Verfahren, JBl 1983, 293 [299]; in diesem Sinn auchSchneiderinFasching/Konecny3§ 31 JN Rz 18), der Vereinbarung des Gerichtsstands oder des Erfüllungsorts sei kein größeres Gewicht beizumessen als der gesetzlichen Zuständigkeit, hat der Oberste Gerichtshof bereits abgelehnt (RIS-Justiz RS0046198 [T10]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


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

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_54`)


1. Auf die Ausführungen der Revision, die sich gegen die dem Aufhebungsbeschluss zugrundeliegende rechtliche Beurteilung des Berufungsgerichts wenden, ist vom Obersten Gerichtshof mangels Bekämpfbarkeit des Aufhebungsbeschlusses derzeit nicht einzugehen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


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

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_57`)


Das Berufungsgericht ließ die Revision mit der Begründung zu, dass keine Rechtsprechung des Obersten Gerichtshofs zu den Folgen der unterbliebenen Mitübertragung der Anmerkung des selbständigen Eigentums an Bäumen bestehe.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


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

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_22`)


Das Rekursgericht sprach aus, dass der ordentliche Revisionsrekurs zulässig sei, weil noch keine Rechtsprechung des Obersten Gerichtshofs zu der Bestimmung des § 3 Z 2 UVG idF FamRÄG 2009 vorliege.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


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

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_65`)


Die Klage wurde daher lange vor Ablauf der Verjährungsfrist eingebracht und der Fortsetzungsantrag rund sechs Monate nach dem Ablauf der ursprünglichen Verjährungsfrist gestellt. In der Entscheidung 6 Ob 822/81 (RIS-Justiz RS0034674) ist der Oberste Gerichtshof in einem Fall, in dem Ruhen des Verfahrens eingetreten war und beinahe ein Jahr nach Ablauf der dreijährigen Verjährungsfrist andauerte, von einer Verjährung mangels gehöriger Fortsetzung ausgegangen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


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

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_32`)


Nach ständiger Rechtsprechung des Obersten Gerichtshofs umfasst dieser Schadenersatzanspruch auch die Vertretungskosten im Zusammenhang mit einem auf Nichtigerklärung einer vergaberechtswidrigen Ausschreibung gerichteten Verfahren (RIS-Justiz RS0121198;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


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

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_20`)


Das Rekursgericht sprach aus, dass der ordentliche Revisionsrekurs gegen seine Entscheidung zulässig sei, weil noch keine Rechtsprechung des Obersten Gerichtshofs zum Wegfall der Exportverpflichtung bei Gewährung von Unterhaltsvorschüssen nach § 4 Z 3 UVG vorliege.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_23`)


Rechtliche Beurteilung Der Revisionsrekurs ist zulässig, weil noch keine Rechtsprechung des Obersten Gerichtshofs zu der über den Einzelfall hinaus bedeutsamen Rechtsfrage, ob die in einem anderen EU-Mitgliedstaat wohnhaften Kinder einen Anspruch auf österreichische Unterhaltsvorschüsse aufgrund der Bestimmungen der VO (EWG) 1612/68 bzw der neuen VO (EU) 492/2011 haben, vorliegt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


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

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_13`)


Mit dem angefochtenen Beschluss gab das Rekursgericht dem Rekurs des Bundes nicht Folge und sprach aus, dass der ordentliche Revisionsrekurs zulässig sei, weil Rechtsprechung des Obersten Gerichtshofs zur Frage fehle, inwiefern das Erstgericht bei der Weitergewährung von Unterhaltsvorschüssen von Amts wegen zu prüfen habe, ob dem Minderjährigen nach wie vor die Flüchtlingseigenschaft zukomme.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_23`)


Rechtliche Beurteilung Der Revisionsrekurs des Bundes ist entgegen dem den Obersten Gerichtshof nicht bindenden Ausspruch des Rekursgerichts (§ 71 Abs 1 AußStrG) mangels einer Rechtsfrage im Sinn des § 62 Abs 1 AußStrG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_30`)


Nach der Rechtsprechung des Obersten Gerichtshofs liegt ein Grund für die amtswegige Versagung der Weitergewährung auch darin, dass bei einer Vorschussgewährung nach § 4 Z 2 UVG vom Kind nicht alles Zumutbare zur Schaffung eines Unterhaltstitels unternommen worden ist (RIS-Justiz RS0076105: 10 Ob 48/10x;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


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

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_95`)


In einem solchen Fall kann der Oberste Gerichtshof durch Urteil in der Sache selbst erkennen (§ 519 Abs 2 Satz 3 ZPO), sodass der Beschluss des Berufungsgerichts aufzuheben und die klageabweisende Entscheidung des Erstgerichts wiederherzustellen war.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


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

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_20`)


Dieser Fall liegt hier aber nach den den Obersten Gerichtshof bindenden Feststellungen nicht vor, weil der Beklagte - entgegen den Ausführungen des Revisionswerbers - die aufgekündigte Wohnungnichtregelmäßig zu Wohnzwecken verwendet, sondern lediglich sporadisch, als Absteigequartier.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_27`)


Ein Kostenersatz für die ohne Freistellung durch den Obersten Gerichtshof eingebrachte Revisionsbeantwortung steht der Klägerin nach § 508a Abs 2 Satz 2 ZPO nicht zu (RIS-Justiz RS0043690 [T6, T7]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


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

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_82`)


Es entspricht der ständigen Rechtsprechung des Obersten Gerichtshofs, dass Ansprüche aus verschiedenen Verträgen betreffend verschiedene Rechtsgüter auch bei Gleichartigkeit nicht in einem sachlichen oder rechtlichen Zusammenhang stehen (RS0037926 [T26]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_100`)


Nach der Rechtsprechung des Obersten Gerichtshofs sei der Pferdeeinstellungsvertrag als entgeltlicher Verwahrungsvertrag zu werten, der nach seinem überwiegenden Charakter nicht als Bestandvertrag zu qualifizieren sei.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_144`)


Das Berufungsgericht hat – ausgehend von seiner vom Obersten Gerichtshof nicht geteilten Rechtsansicht – sowohl die Mängelrüge (Nichteinholung eines Gutachtens für den Bereich Pferdehaltung und Pferdesport) als auch die (auch) die Feststellungen zu den behaupteten Mängeln betreffende Beweisrüge der Berufung nicht erledigt, weshalb sein Verfahren mangelhaft geblieben ist.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


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

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


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

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_56`)


Der Oberste Gerichtshof habe festgehalten, dass die Weigerung des Netzbenutzers, dem Netzbetreiber für einen geplanten Zählertausch Zutritt zu einem Objekt zu gewähren, es nicht rechtfertige, anstelle der Inanspruchnahme gerichtlicher Hilfe faktisch zur Selbsthilfe im Wege der (Androhung der) Stromabschaltung zu greifen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_75`)


[17]5.Der Oberste Gerichtshof hat zu 9 Ob 95/24x, 7 Ob 167/24w und 3 Ob 191/24w (betreffend vergleichbare AB-VN einer anderen Netzbetreiberin) dargelegt, dass die Weigerung des Netzbenutzers, der Netzbetreiberin Zugang zu seinem Objekt zu gewähren, damit sie einen (grundsätzlich funktionsfähigen) Stromzähler austauschen kann, qualitativ nicht den Fällen des Zahlungsverzugs und der Verweigerung einer Vorauszahlung oder Sicherheitsleistung gleichzuhalten sei.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


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

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_50`)


4. 2011 enthaltenen Hinweise weitere Aufträge erteilt habe, werden keine Umstände aufgezeigt, die einen vom Obersten Gerichtshof aufzugreifenden Fehler in der Beurteilung des Berufungsgerichts, der nicht fachkundigen Klägerin könne kein Mitverschulden am Entstehen des Schadens angelastet werden, begründen könnten.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


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

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


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

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_9`)


Die Revision der Beklagten ist entgegen dem – den Obersten Gerichtshof nicht bindenden – Zulassungsausspruch mangels Vorliegens einer Rechtsfrage von erheblicher Bedeutung im Sinn des § 502 Abs 1 ZPO nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 68** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_11`)


Das Vorliegen einer Rechtsfrage von erheblicher Bedeutung ist nach dem Zeitpunkt der Entscheidung über das Rechtsmittel durch den Obersten Gerichtshof zu beurteilen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 69** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_12`)


Eine im Zeitpunkt der Einbringung des Rechtsmittels tatsächlich aufgeworfene erhebliche Rechtsfrage fällt somit weg, wenn sie vor der Erledigung des Rechtsmittels bereits durch eine andere Entscheidung des Obersten Gerichtshofs geklärt wurde (RS0112921 [T5]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 70** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_15`)


2010 geltenden Fassung des GSpG hat der Oberste Gerichtshof bereits in der – einen nahezu identen Sachverhalt betreffenden – Entscheidung 6 Ob 229/21a klargestellt, dass zwar das in § 21 Abs 2 Z 1 GSpG (bzw § 14 Abs 2 Z 1 GSpG) idF vor dem Budgetbegleitgesetz 2011 normierte Sitzerfordernis unionsrechtswidrig war und nach der Rechtsprechung des EuGH ein Mitgliedstaat keine (verwaltungs-)strafrechtlichen Sanktionen wegen einer nicht erfüllten Verwaltungsformalität verhängen darf, wenn er die Erfüllung dieser Formalität unter Verstoß gegen das Unionsrecht abgelehnt oder vereitelt hat, dass aber dieser Grundsatz schon deshalb nicht auf die vorliegende Konstellation übertragbar ist, weil die „Nichtigkeitssanktion“ im Sinn des § 879 Abs 1 ABGB keine vergleichbare staatliche Sanktion repressiver Natur darstellt. Weiters führte der Oberste Gerichtshof in der zitierten Entscheidung 6 Ob 229/21a aus, dass die zivilrechtliche Unerlaubtheit des Spiels eine Strafbarkeit im Sinn des § 168 StGB nicht voraussetzt (4 Ob 70/22f mwH; RS0102178 [T10]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 71** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_20`)


Der Oberste Gerichtshof hat mittlerweile auch die Passivlegitimation der Beklagten für den vom Kläger mit Leistungskondiktion begehrten Ersatz seiner Spielverluste aus Online-Pokerspielen in vergleichbaren Verfahren bereits mehrfach bejaht (6 Ob 229/21a;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 72** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


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

**Example 73** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_59`)


2.2 In der – bereits von den Vorinstanzen zitierten und verwerteten – Entscheidung 1 Ob 158/15i hat der Oberste Gerichtshof das folgende, in der Entscheidung 8 Ob 89/17x fortgeschriebene Modell für die Festsetzung des Differenzunterhalts entwickelt: Zunächst ist der fiktive Geldunterhaltsanspruch des Kindes gegen jeden Elternteil nach der Prozentmethode – bei weit überdurchschnittlichem Einkommen des besser verdienenden Elternteils unter Bedachtnahme auf die sogenannte Luxusgrenze – zu ermitteln.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 74** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_78`)


NeuhausersErgebnis beträgt 261 EUR, jenes des Obersten Gerichtshofs 252 EUR, wobei der Unterhaltsbetrag gerundet mit 260 EUR festgesetzt wurde.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 75** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_84`)


Senats des Obersten Gerichtshofs zufolge § 231 Abs 2 Satz 2 ABGB in Fällen als problematisch, in denen ein Elternteil nichts oder unterhalb des Existenzminimums verdient.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 76** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


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

**Example 77** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


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

**Example 78** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


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

**Example 79** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_79`)


Rechtliche Beurteilung DieRevisionist entgegen dem - den Obersten Gerichtshof nicht bindenden (§ 508 Abs 1 ZPO) - Ausspruch des Berufungsgerichts zulässig, weil das Berufungsgericht von der ständigen Rechtsprechung des Obersten Gerichtshofs zur Beurteilung von Kündigungserklärungen abweicht;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 80** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_108`)


Dabei wird übersehen, dass im Rechtsmittelverfahren vor dem Obersten Gerichtshof Verweise in der Revision bzw Revisionsbeantwortung auf Ausführungen in anderen Schriftsätzen (zB der Berufung) nach ständiger Rechtsprechung unzulässig und unbeachtlich sind (RIS-Justiz RS0043579 und RS0043616; vgl auch RS0007029).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 81** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

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

**Example 82** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_4`)


Begründung:  Rechtliche Beurteilung Der Oberste Gerichtshof befasste sich in seinem Aufhebungsbeschluss vom 13.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 83** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_39`)


2.1 Der gegen den abändernden Teil der Rekursentscheidung gerichtete – nach Freistellung durch den Obersten Gerichtshof vomVater beantwortete– Revisionsrekurs ist hingegen zulässig und im Sinne einer Aufhebung berechtigt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 84** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


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

**Example 85** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


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

**Example 86** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_16`)


Die Verhängung der Ordnungsstrafe hingegen sei grundsätzlich durch Rekurs an den Obersten Gerichtshof bekämpfbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 87** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_19`)


Mit dem dagegen erhobenen Rekurs an den Obersten Gerichtshof verband der Rechtsmittelwerber einen Ablehnungsantrag gegen die Vorsitzende und die beiden weiteren Mitglieder des 13.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 88** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_25`)


Der Beschluss ist daher, da dem Ablehnungsantrag nicht stattgegeben wurde, gemäß § 24 Abs 2 JN uneingeschränkt an den Obersten Gerichtshof anfechtbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 89** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_27`)


Vor Eingehen auf das Rechtsmittel selbst ist vorerst die Frage zu prüfen, ob die Rekursschrift von einem Rechtsanwalt zu fertigen und daher durch den Obersten Gerichtshof das Verbesserungsverfahren einzuleiten wäre.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 90** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_31`)


Das Oberlandesgericht Wien hat funktionell als Erstgericht entschieden, der Oberste Gerichtshof entscheidet daher im vorliegenden Fall als Rekursgericht.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_34`)


Soweit der Rechtsmittelwerber in seinem Rekurs ohne nähere Substantiierung „alle als befangen angezeigten Richter des Obersten Gerichtshofs" ablehnt, sieht sich der erkennende Senat nicht veranlasst, die pauschale Ablehnung derjenigen seiner Mitglieder, die bereits früher in Rechtssachen des Rechtsmittelwerbers entschieden haben, zum Gegenstand einer Entscheidung des für Ablehnungen zuständigen Senats des Obersten Gerichtshofs zu machen (vgl RIS-Justiz RS0111658).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 92** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


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

**Example 93** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_19`)


Nach Vorlage des Revisionsrekurses stellte der Oberste Gerichtshof mit Beschluss vom 25.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 94** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_26`)


Mit Beschluss des Erstgerichts vom 29. 11. 2013 (zugestellt am 9. 12. 2013) wurde dem Vertreter des Vaters in der Folge auch der ordentliche Revisionsrekurs „vom31. 1. 2013(ON 82)“ zur Verbesserung binnen 14 Tagen (gemäß dem Beschluss 10 Ob 29/13g [ON 93]) zurückgestellt. Den am 10. 12. 2013 im ERV eingebrachten verbesserten Revisionsrekurs legt das Erstgericht neuerlich dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 95** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_35`)


das ordentliche Rechtsmittel ist jedoch entgegen dem - gemäß § 71 Abs 1 AußStrG den Obersten Gerichtshof nicht bindenden - Ausspruch des Rekursgerichts wegen Fehlens einer erheblichen Rechtsfrage nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 96** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_54`)


3. Entgegen den Ausführungen zur Zulässigkeit des Revisionsrekurses hat sich der Oberste Gerichtshof bereits ausdrücklich mit der Frage befasst, ob die (wenn auch nur mögliche) Anwendung europäischen Primär- und Sekundärrechtes oder völkerrechtlicher Abkommen der EU mit anderen Staaten (unabhängig davon, ob eine „schwierige Rechtsfrage“ zu lösen ist) dem Begriff „ausländisches Recht“ im Sinn des § 16 Abs 2 Z 6 RpflG zuzurechnen ist und demgemäß auch dem Richtervorbehalt unterliegt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 97** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


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

**Example 98** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_10`)


Das Erstgericht wertete dieses Rechtsmittel als außerordentlichen Revisionsrekurs und ging davon aus, dass dieser sogleich dem Obersten Gerichtshof vorzulegen sei.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 99** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_15`)


Daraufhin legte das Erstgericht das Rechtsmittel dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

</details>

---

## `Oberlandesgericht` 🏆

**F1:** 0.170 | **Precision:** 1.000 | **Recall:** 0.093  

**Format:** `regex`  
**Rule ID:** `8adf3e88`  
**Description:**
Matches 'Oberlandesgericht' and its genitive form 'Oberlandesgerichts' with location suffixes.

**Content:**
```
\bOberlandesgericht(?:s)?\s+(?:Wien|Graz|Innsbruck|Klagenfurt|Linz|Salzburg|Bregenz|Eisenstadt|St.\sPölten)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.093 | 0.170 | 373 | 373 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 373 | 0 | 3507 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Landesgerichts Innsbruck` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_23`)


Gegen die Entscheidung des Rekursgerichts richtet sich der Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, mit dem Antrag, den angefochtenen Beschluss im Sinne einer Wiederherstellung der Beschlüsse des Erstgerichts abzuändern.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Handelsgerichts Wien` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Dr. Ralph Trischler` (person)
- `Bundesbeschaffung GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_17`)


DasRekursgerichtgab dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, Folge und wies den Unterhaltsvorschussantrag der beiden Kinder ab.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_22`)


Der Bund, vertreten durch den Präsidenten des Oberlandesgerichts Wien, beantragt in seiner Revisionsrekursbeantwortung, den Revisionsrekurs zurückzuweisen bzw ihm keine Folge zu geben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Enns-Umwelt` (organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich` (address)
- `Ing. Lara Markart` (person)
- `Radel Stampf Supper Rechtsanwälte OG` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Landesgerichts Wels` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Mag. Herwig Bortzlaff` (person)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_8`)


Dem gegen diesen Beschluss vom Ablehnungswerber erhobenen Rekurs gab das Oberlandesgericht Wien durch seinen 11.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_11`)


Senats des Oberlandesgerichts Wien wegen Befangenheit ab.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Paolo Barley` (person)
- `Mag. Klarissa Hausteiner` (person)
- `Mag. Viola Brauch` (person)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_14`)


Es wurde darauf hingewiesen, dass die Entscheidung des Oberlandesgerichts Wien vom 3. 8. 2009, AZ 11 R 105/09f, im Umfang der Bestätigung der Zurückweisung des Ablehnungsantrags bereits in Rechtskraft erwachsen sei.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_17`)


Eine Ablehnung der Richter des die Ordnungsstrafe verhängenden Rekurssenats des Oberlandesgerichts Wien sei daher grundsätzlich möglich.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_20`)


Senats des Oberlandesgerichts Wien, die über seine Ablehnungserklärung entschieden haben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_22`)


Senat des Oberlandesgerichts Wien (AZ 12 Nc 44/09a) entschieden, dass dieser offenbar rechtsmissbräuchlich erhobene Ablehnungsantrag nicht zum Gegenstand einer gerichtlichen Entscheidung gemacht werden müsse.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_24`)


Vorauszuschicken ist, dass das Oberlandesgerichts Wien nicht einen Beschluss im Rechtsmittelverfahren gefasst hat, sondern als Erstgericht entschieden hat.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_31`)


Das Oberlandesgericht Wien hat funktionell als Erstgericht entschieden, der Oberste Gerichtshof entscheidet daher im vorliegenden Fall als Rekursgericht.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_36`)


Senats des Oberlandesgerichts Wien aufzuzeigen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_22`)


DasRekursgerichtgab dem Rekurs des Präsidenten des Oberlandesgerichts Wien teilweise Folge und reduzierte die gewährten Unterhaltsvorschüsse auf 150 EUR monatlich.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Dr. Felix Cornils` (person)
- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

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
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_14`)


Das Erstgericht legte dem Rekursgericht die gegen den abweislichen Teil des Titelbeschlusses erhobenen Rekurse der Minderjährigen sowie den vom Präsidenten des Oberlandesgerichts Wien erhobenen Rekurs gegen die Bewilligung von Unterhaltsvorschüssen für den Monat April 2013 zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_26`)


Unter einem gab das Rekursgericht dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, Folge und wies die Anträge der beiden Minderjährigen auf Gewährung von Unterhaltsvorschüssen für den Monat April 2013 ab (Punkt 2a des Spruchs).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_38`)


Im Hinblick darauf, dass im vorliegenden Fall erst nachträglich bekannt geworden sei, dass ein Zustellmangel vorliege und der Wegfall der Rechtskraft des Unterhaltstitels den im § 7 UVG genannten Umständen zumindest vergleichbar sei, erscheine aus Anlass des Rekurses des Präsidenten des Oberlandesgerichts Wien eine bis zum Beginn der Vorschussbewilligung rückwirkende Wahrnehmung zulässig.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_69`)


Mangels Anfechtung durch den Präsidenten des Oberlandesgerichts Wien sind die erstinstanzlichen Gewährungsbeschlüsse betreffend den Zeitraum ab 1. 5. 2013 in (Teil-)Rechtskraft erwachsen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_71`)


Wenn das Rekursgericht dennoch aus Anlass des vom Präsidenten des Oberlandesgerichts Wien hinsichtlich des Monats April 2013 erhobenen Rekurses die (rechtskräftigen) erstgerichtlichen Gewährungsbeschlüsse zum Nachteil der beiden Minderjährigen (also zu Ungunsten der den Beschlussnichtanfechtenden Parteien) dahingehend abgeändert hat, dass deren Anträge auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden, hat es seine Kognitionsbefugnis überschritten.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Othmar Mertl` (person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG` (organisation)
- `Malik Fridt` (person)
- `Krist Bubits Rechtsanwälte OG` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Scarlett Achatzi` (person)
- `Mag. Ewald Aszmutat` (person)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_4`)


Der Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_16`)


Gegen diesen Beschluss richtet sich der Rekurs des Antragsgegners, verbunden mit einem Ablehnungsantrag wegen Befangenheit aller Richterinnen und Richter des Oberlandesgerichts Wien.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_17`)


Rechtliche Beurteilung 1.Zur Ablehnung sämtlicher Richterinnen und Richter des Oberlandesgerichts Wien: Auch als Begründung für den Ablehnungsantrag wegen Befangenheit aller Richterinnen und Richter des Oberlandesgerichts Wien führt der Ablehnungswerber aus, es sei im (seine Tochter betreffenden) Pflegschaftsverfahren zu kriminellen Handlungen, insbesondere zu Hochverrat nach § 242 StGB gekommen, wodurch sowohl ihm als auch seiner Tochter unwiederbringlicher Schaden an Lebensqualität und persönlicher Identität verursacht worden sei.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_18`)


Nicht nur die Mitglieder des an der Entscheidung beteiligten Senats des Oberlandesgerichts Wien, sondern alle Richter dieses Gerichts seien am Hochverrat an der Republik Österreich, an ihm selbst sowie seiner Tochter beteiligt.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_21`)


Da der Ablehnungswerber alle Richterinnen und Richter des Oberlandesgerichts Wien ablehnt, ist der Oberste Gerichtshof zur Entscheidung berufen (RIS-Justiz RS0045997).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_26`)


Inwiefern die Mitglieder des an der Entscheidung beteiligten Senats des Oberlandesgerichts Wien, aber auch alle anderen Richter und Richterinnen dieses Gerichtshofs den Tatbestand des Hochverrats nach § 242 StGB erfüllt haben sollten – indem sie es unternommen hätten, mit Gewalt oder durch Drohung mit Gewalt die Verfassung der Republik Österreich oder eines ihrer Bundesländer zu ändern oder ein zur Republik Österreich gehörendes Gebiet abzutrennen –, wird im Ablehnungsantrag nicht näher begründet und ausgeführt.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_28`)


2. DerRekursgegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017 ist zulässig (§ 24 Abs 2 JN; RIS-Justiz RS0043830);

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Josefstadt` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `DI Cassandra Wespi` (person)
- `Vogl Rechtsanwalt GmbH` (organisation)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mag. Claudia Gründel` (person)
- `Mathias Jendl` (person)
- `Dr. Thomas Stampfer` (person)
- `Dr. Christoph Orgler` (person)
- `Dr. Michael Stögerer` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Fichtenau` (person)
- `KR Hermann Furtner` (person)
- `AR Angelika Neuhauser` (person)
- `Birgit Jaros` (person)
- `Dr. Herbert Pochieser` (person)
- `Wiener Gebietskrankenkasse` (organisation)
- `Dr. Heinz Edelmann` (person)

**Example 49** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Gabriele Griehsel` (person)
- `Dr. Wolfgang Kozak` (person)
- `Roland Soukup` (person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_5`)


Dagegen richtet sich die als Rekurs bezeichnete, prozessordnungswidrig an das Oberlandesgericht Linz gerichtete Beschwerde des Richard Laumeyer.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Missed by this rule (FN):**

- `Richard Laumeyer` (person)

**Example 52** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_4`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 53** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_4`)


Zur Entscheidung über die Berufungen werden die Akten dem Oberlandesgericht Innsbruck zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Example 54** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oberressl` (person)
- `Mag. Wieser` (person)
- `Gerald Winand` (person)
- `Landesgerichts Korneuburg` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Gerald Wandscheer` (person)
- `Landesgerichts Korneuburg` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Mag. Herwig Bleuler` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist von der Entscheidung über die Beschwerde des Oliver Paukstat gegen den Beschluss des Oberlandesgerichts Wien vom 8. Februar 2016, AZ 32 Bs 12/16y, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Oliver Paukstat` (person)

**Example 58** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_9`)


An der angefochtenen Entscheidung des Oberlandesgerichts Wien hat die mit ihm in einem Angehörigenverhältnis im Sinne des § 72 StGB stehende Senatspräsidentin des Oberlandesgerichts Dr. Christine Schwab als Richterin mitgewirkt.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Christine Schwab` (person)

**Example 59** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Christine Schwab` (person)

**Example 60** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_14`)


Senat des Obersten Gerichtshofs - unter dem Aspekt der §§ 281 Abs 1 Z 5a, 362 StPO - auch der Tatverdacht hinsichtlich eines Tatzeitraums („August 2008 bis längstens 14. Dezember 2008“ - vgl Urteil des Landesgerichts für Strafsachen Wien vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, US 2) zu prüfen, auf den sich auch das Oberlandesgericht Wien in Entscheidungen bezog, die unter Mitwirkung der Angehörigen des Anzeigers getroffen wurden (vgl insb BS 32 f in AZ 19 Bs 465/12i).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_4`)


2005 den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski ist von der Entscheidung über die Beschwerde des Ahmed Kleinmayer gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 25. November 2019, AZ 23 Bs 343/19p, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Ahmed Kleinmayer` (person)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_7`)


Mit dem erwähnten Beschluss vom 25. November 2019 hatte das Oberlandesgericht Wien einer Beschwerde des Ahmed Kocks gegen einen Beschluss des Landesgerichts für Strafsachen Wien auf Ablehnung eines Antrags des Genannten auf Wiederaufnahme des Verfahrens AZ 606 Hv 1/11m jenes Gerichts nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Ahmed Kocks` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Mann` (person)
- `Dr. Brenner` (person)
- `Mag. Rögner` (person)
- `Thomas Michenfelder` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Mag. Gföller` (person)
- `Dr. Zeh-Gindl` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_4`)


Der Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, verletzt § 43 Abs 1 Z 3 StPO.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 65** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


Dieser Beschluss wird aufgehoben und es wird in der Sache selbst erkannt, dass der Senatspräsident des Oberlandesgerichts Wien Dr. Krenn sowie die Richterinnen des Oberlandesgerichts Wien Mag. Edwards und Mag. Sanda von der Entscheidung über die Berufung des Angeklagten gegen das Urteil des Landesgerichts Krems an der Donau vom 8. August 2018, GZ 38 Hv 40/18z-100, nicht ausgeschlossen sind.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)
- `Landesgerichts Krems an der Donau` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_7`)


Senat des Oberlandesgerichts Wien, dem der Senatspräsident Dr. Krenn sowie die Richterinnen Mag. Edwards und Mag. Sanda angehörten, dieses Urteil „in amtswegiger Wahrnehmung des Nichtigkeitsgrunds des § 281 Abs 1 Z 9 lit a iVm § 489 Abs 1 StPO“ wegen des Vorliegens von Rechtsfehlern mangels Feststellungen (vgl zu diesem BegriffRatz, WK-StPO § 281 Rz 605 ff) in den Schuldsprüchen I./ und III./, demgemäß im Strafausspruch und im Ausspruch über den Privatbeteiligtenanspruch auf und verwies die Sache in diesem Umfang zu neuerlicher Verhandlung und Entscheidung an das Erstgericht.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)

**Example 67** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_11`)


Dagegen ergriff der Genannte Berufung wegen Nichtigkeit und Strafe (ON 107), die dem Oberlandesgericht Wien mit Bericht vom 8. Oktober 2018 (ON 108) vorgelegt und über die bislang noch nicht entschieden wurde.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 68** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_12`)


Mit Beschluss vom 17. Oktober 2018, AZ 130 Ns 31/18w, stellte der Präsident des Oberlandesgerichts Wien fest, dass Senatspräsident Dr. Krenn sowie die Richterinnen Mag. Edwards und Mag. Sanda „im Berufungsverfahren über die vom Erstangeklagten Thomas Mecit erhobene Berufung (ON 107) ausgeschlossen“ seien.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)
- `Thomas Mecit` (person)

**Example 69** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_16`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt, steht dieser Beschluss des Präsidenten des Oberlandesgerichts Wien mit dem Gesetz nicht in Einklang: Schon aufgrund ihres Ausnahmecharakters, insbesondere aber mit Blick auf das Spannungsverhältnis zum verfassungsrechtlich gewährleisteten Recht auf den gesetzlichen Richter (Art 83 Abs 2 B-VG) und zum Prinzip der festen Geschäftsverteilung (Art 87 Abs 3 B-VG) erfordert die Wahrnehmung von Ausschließungsgründen (§ 43 StPO) eine strikte Auslegung dieser Norm, um die – neben der Unabsetzbarkeit und Unversetzbarkeit (Art 88 Abs 2 B-VG) – wesentlichsten Säulen der richterlichen Unabhängigkeit (Art 87 Abs 1 B-VG) nicht auszuhöhlen (vglLässig, WK-StPO Vor §§ 43–47 Rz 3).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 70** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_19`)


Gegenständlich aber hatte das Oberlandesgericht Wien im ersten Rechtsgang die Tatfrage im Rahmen der Strafberufung des Angeklagten Thomas Marczynkowski entgegen der Ausführungen im angefochtenen Beschluss weder „in voller Kognitionsbefugnis“ zu beurteilen, noch bezog es in den Entscheidungsgründen hiezu beweiswürdigend Stellung.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Thomas Marczynkowski` (person)

**Example 71** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_21`)


Gründe, die geeignet wären, im Sinn des § 43 Abs 1 Z 3 StPO die volle Unvoreingenommenheit und Unparteilichkeit des Senatspräsidenten des Oberlandesgerichts Wien Dr. Krenn sowie der Richterinnen Mag. Edwards und Mag. Sanda im zweiten Rechtsgang in Zweifel zu ziehen, liegen daher entgegen der im angefochtenen Beschluss vertretenen Auffassung nicht vor.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fruhmann` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Gebhard Sayin` (person)

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_4`)


Text Gründe: Mit der angefochtenen Entscheidung wies das Oberlandesgericht Wien die Beschwerde des Gebhard Senkfeil gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 25. September 2012, GZ 130 Bl 65/12s-10, mit welchem der Antrag des Beschwerdeführers auf Fortführung des Verfahrens AZ 20 UT 91/12p der Staatsanwaltschaft Wien gegen unbekannte Täter wegen § 302 Abs 1 StGB zurückgewiesen worden war, als unzulässig zurück (§ 196 Abs 1 StPO).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Gebhard Senkfeil` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_3`)


Kopf Der Oberste Gerichtshof hat am 15. März 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ettel als Schriftführerin in der Maßnahmenvollzugssache des Andreas Wegele, AZ 181 BE 143/17y des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 9. Jänner 2018, AZ 131 Bs 370/17z, und seinen Antrag auf Bewilligung der Verfahrenshilfe nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Mag. Ettel` (person)
- `Andreas Wegele` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_5`)


Text Gründe: Mit dem angefochtenen Beschluss vom 9. Jänner 2018, AZ 131 Bs 370/17z, gab das Oberlandesgericht Wien als Rechtsmittelgericht der Beschwerde des Andreas Wackerow gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 20. November 2017, GZ 181 BE 143/17y-16, mit dem die bedingte Entlassung aus einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 2 StGB abgelehnt worden war, nicht Folge.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Andreas Wackerow` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_6`)


Zur Entscheidung über die Berufung wegen des Strafausspruchs werden die Akten vorerst dem Oberlandesgericht Innsbruck zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Holzweber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Dr. Schwab` (person)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Bayer` (person)
- `Dr. Ernst` (person)
- `Nepomuk Lieschke` (person)
- `Landesgerichts St. Pölten` (organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Landesgerichts St. Pölten` (organisation)
- `Dr. Ernst` (person)
- `Paula Langehanke` (person)

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Hauer` (person)
- `Viktor Marschmeyer` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Dr. Stefan Toepfl` (person)

**Example 80** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_5`)


Das Oberlandesgericht Wien als Rechtsmittelgericht gab der dagegen erhobenen Beschwerde des Beschuldigten (ON 661) mit Beschluss vom 28. August 2018, AZ 20 Bs 199/18p, nicht Folge (ON 683).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 81** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_6`)


Rechtliche Beurteilung Gegen diesen Beschluss des Oberlandesgerichts Wien richtet sich der – nicht auf ein Erkenntnis des Europäischen Gerichtshofs für Menschenrechte (EGMR) gestützte – (rechtzeitige) Antrag des Beschuldigten Dr. Stefan Tilge auf Erneuerung des Strafverfahrens gemäß § 363a StPO per analogiam, mit welchem dieser einen „Verstoß gegen Art 6 und 8 EMRK, Art 1 1.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Stefan Tilge` (person)

**Example 82** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_4`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Graz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Graz` | `Oberlandesgericht Graz` |

**Example 83** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_20`)


Mit Beschluss des Oberlandesgerichts Innsbruck als Beschwerdegericht vom 25. November 2014, AZ 11 Bs 326/14z, 349/14g (ON 47 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch bzw ON 52 im Akt AZ 39 Hv 64/14h dieses Landesgerichts), wurde die Beschwerde als unzulässig (verspätet) zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Landesgerichts Feldkirch` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_34`)


Durch die Aufhebung des Beschlusses auf Wiederaufnahme des Strafverfahrens wird die von diesem rechtslogisch abhängige Beschwerdeentscheidung des Oberlandesgerichts Innsbruck hinfällig (RIS-Justiz RS0100444).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Example 85** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_5`)


Mit Urteil vom 21. Mai 2019 gab das Oberlandesgericht Innsbruck der Berufung des Genannten Folge.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Example 86** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_5`)


Die dagegen gerichtete Beschwerde des Sebastian Naegeler wies das Oberlandesgericht Graz mit Beschluss vom 1. August 2019, AZ 10 Bs 202/19k, unter Hinweis auf § 196 Abs 1 zweiter Halbsatz StPO als unzulässig zurück.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Graz` | `Oberlandesgericht Graz` |

**Missed by this rule (FN):**

- `Sebastian Naegeler` (person)

**Example 87** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_4`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 88** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_4`)


Zur Entscheidung über die Berufung und die Beschwerde werden die Akten dem Oberlandesgericht Linz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Example 89** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_4`)


Zur Entscheidung über die Berufung gegen die Aussprüche über die Strafe und die privatrechtlichen Ansprüche werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 90** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Bachl` (person)
- `Mag. Johanna Fletcher` (person)
- `Herbert Onesseit` (person)

**Example 91** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Linz die Beschwerde des Herbert Oehlschlager gegen den Beschluss des Landesgerichts Wels vom 19. November 2014, AZ 24 Bl 81/14h (ON 9 der Ermittlungsakten), mit dem der Antrag des Genannten auf Fortführung des Verfahrens zurückgewiesen worden war, gemäß § 196 Abs 1 erster Satz StPO zurück (ON 12 der Ermittlungsakten).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Missed by this rule (FN):**

- `Herbert Oehlschlager` (person)
- `Landesgerichts Wels` (organisation)

**Example 92** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_4`)


Zur Entscheidung über die Berufung und die Beschwerde werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 93** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_5`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 94** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_4`)


Text Gründe: Mihai von Crailsheim wurde mit Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 19. April 2017, GZ 222 Hv 15/17v-207, des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB sowie weiterer strafbarer Handlungen schuldig erkannt und zu einer Freiheitsstrafe verurteilt, die das Oberlandesgericht Graz – in Stattgebung einer dagegen erhobenen Berufung des Angeklagten – mit Urteil vom 25. Oktober 2017, AZ 8 Bs 311/17x, herabsetzte.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Graz` | `Oberlandesgericht Graz` |

**Missed by this rule (FN):**

- `Mihai von Crailsheim` (person)
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 95** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_4`)


Zur Entscheidung über die Berufung und die Beschwerde werden die Akten dem Oberlandesgericht Linz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Example 96** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Lengjel und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wynand und des DI Georg Lu Brian Waltemate gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Mag. Temper` (person)
- `Michael Lengjel` (person)
- `Landesgerichts Innsbruck` (organisation)
- `Anna Wynand` (person)
- `Brian Waltemate` (person)

**Example 97** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Innsbruck die Beschwerden der Anna Waniek und des DI Georg Lu Carla Hanel gegen mehrere Verfügungen des Vorsitzenden eines Drei-Richter-Senats des Landesgerichts Innsbruck als unzulässig zurück.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Missed by this rule (FN):**

- `Anna Waniek` (person)
- `Carla Hanel` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_4`)


Zur Entscheidung über die Berufung wegen des Ausspruchs über die Strafe werden die Akten dem Oberlandesgericht Linz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Example 99** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Holthuijsen wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Dr. Ondreasova` (person)
- `Christoph Holthuijsen` (person)
- `Landesgerichts Klagenfurt` (organisation)
- `Mag. Höpler` (person)
- `Mag. Sternad` (person)
- `Mag. Höllwerth` (person)

</details>

---

## `Handelsgericht` 🏆

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `c0420946`  
**Description:**
Matches 'Handelsgericht' and its genitive form 'Handelsgerichts' with location suffixes.

**Content:**
```
\bHandelsgericht(?:s)?\s+(?:Wien|Graz|Linz|Salzburg|Innsbruck|Klagenfurt|Bregenz|Eisenstadt|St.\sPölten)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.017 | 34 | 34 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 34 | 0 | 3855 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Handelsgericht Wien` | `Handelsgericht Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_9`)


In der Streitverhandlung vom 27. Jänner 2015 beantragte die klagende Partei die Delegierung an das Handelsgericht Wien.

| Predicted | Gold |
|---|---|
| `Handelsgericht Wien` | `Handelsgericht Wien` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `DI Cassandra Wespi` (person)
- `Vogl Rechtsanwalt GmbH` (organisation)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_4`)


Wien Derconlex AG, Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich, vertreten durch Mag. Klemens Mayer, Mag. Stefan Herrmann Rechtsanwälte in Wien, wegen 410.325,23 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Mai 2020, GZ 30 R 106/20h-73, mit dem das Urteil des Handelsgerichts Wien vom 15. Jänner 2020, GZ 10 Cg 15/16k-69, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Wien Derconlex AG` (organisation)
- `Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich` (address)
- `Mag. Klemens Mayer` (person)
- `Mag. Stefan Herrmann` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Florenzia Münsterer` (person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH` (organisation)
- `MittelEnergie Werke Bank` (organisation)
- `Altlassing 110, 4183 Ahorn, Österreich` (address)
- `Urbanek Lind Schmied Reisch Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache klagenden Partei Rainer Baetzel, vertreten durch Dr. Harald Hauer, Rechtsanwalt in Wien, gegen die beklagte Partei Rimscha Versand GmbH in Liquidation, Götzau 193, 5452 Grub, Österreich, vertreten durch die Petsch Frosch Klein Arturo Rechtsanwälte OG, Wien, wegen 38.236,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Oktober 2020, GZ 3 R 51/20x-50, mit dem das Urteil des Handelsgerichts Wien vom 24. Juli 2020, GZ 34 Cg 51/18h-45, bestätigt wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Rainer Baetzel` (person)
- `Dr. Harald Hauer` (person)
- `Rimscha Versand GmbH` (organisation)
- `Götzau 193, 5452 Grub, Österreich` (address)
- `Petsch Frosch Klein Arturo Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_4`)


Gloria Hackenbuchner GmbH, Untere Kanalstraße 187, 2471 Hollern, Österreich, vertreten durch Mag. Manfred Sommerbauer und MMag. Dr. Michael Dohr LL.M., Rechtsanwälte in Wiener Neustadt, und 2. Nelleßen + Stümpfel Automotive AG, Villengasse 31, 8670 Krieglach, Österreich, vertreten durch die Kosch & Partner Rechtsanwälte GmbH, Wiener Neustadt, wegen 76.444,01 EUR sA über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2017, GZ 1 R 164/16v-174, mit dem das Urteil des Handelsgerichts Wien vom 12. August 2016, GZ 65 Cg 12/15x-169, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Gloria Hackenbuchner` (person)
- `Untere Kanalstraße 187, 2471 Hollern, Österreich` (address)
- `Mag. Manfred Sommerbauer` (person)
- `MMag. Dr. Michael Dohr LL.M.` (person)
- `Nelleßen + Stümpfel Automotive AG` (organisation)
- `Villengasse 31, 8670 Krieglach, Österreich` (address)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/2Ob86_12d`) (sent_id: `deanon_260716_TRAIN/2Ob86_12d_4`)


Die Akten werden dem Handelsgericht Wien zur Entscheidung über diesen Ablehnungsantrag und Wiedervorlage nach Rechtskraft dieser Entscheidung zurückgestellt.  Text Begründung: Das Berufungsgericht hat über die Berufung der Beklagten das (weit überwiegend) klagsstattgebende Urteil des Erstgerichts teilweise mit Teilurteil in einem 30.000 EUR übersteigenden Betrag bestätigt, teilweise aufgehoben und insoweit die Rechtssache zur neuerlichen Verhandlung und Entscheidung an das Erstgericht zurückverwiesen.

| Predicted | Gold |
|---|---|
| `Handelsgericht Wien` | `Handelsgericht Wien` |

**Example 10** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_6`)


Text Begründung: [1] Mit rechtskräftigem und vollstreckbarem Urteil des Handelsgerichts Wien vom 1. April 2021 wurde zwischen dem Betreibenden als Kläger und der beklagten Partei, einer Gesellschaft nach englischem Recht mit Sitz in Großbritannien, festgestellt, dass der Treuhandvertrag zwischen den Streitteilen bezüglich einer (in Wien gelegenen) Liegenschaft samt darauf errichtetem Zinshaus aufgelöst ist.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Example 11** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_5`)


Dr. Walter Johänntges, alle drei vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, wegen Anfechtung (Streitwert 868.223,10 EUR), über die (teils außerordentliche) Revision der klagenden Partei (Revisionsinteresse 299.996,80 EUR) und den Rekurs der beklagten Partei (Rekursinteresse 567.732,95 EUR) gegen das Teilurteil und den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 27. November 2009, GZ 3 R 121/08y-21, womit das Urteil des Handelsgerichts Wien vom 4. September 2008, GZ 46 Cg 58/07k-14, (neue AZ 24 Cg 49/08a), teils bestätigt und teils aufgehoben wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch Der Revision der klagenden Partei und dem Rekurs der beklagten Partei wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Walter Johänntges` (person)
- `Dr. Herwig Ernst` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Kelkel-Versicherung GmbH, Walkersdorf 16, 9761 Tröbelsberg, Österreich, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Zorzorzor GmbH, Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgericht Wien` | `Handelsgericht Wien` |

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
- `Landesgericht Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_13`)


In der Verhandlungstagsatzung am 2. Februar 2012 beantragte die Beklagte neuerlich die Delegierung der Rechtssache, diesmal an das Handelsgericht Wien und verwies zusätzlich zu den bereits ausgeführten Gründen auf eine Delegierungsentscheidung in einem Parallelverfahren.

| Predicted | Gold |
|---|---|
| `Handelsgericht Wien` | `Handelsgericht Wien` |

**Example 14** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_7`)


Text Begründung: Die Klägerinnen erwirkten gegen die Beklagten zu AZ 57 Cg 10/12i des Handelsgerichts Wien ein – in der Folge vom Oberlandesgericht Wien zu AZ 1 R 97/16s im Wesentlichen und mit Maßgabe bestätigtes – Urteil gegen die Beklagten, mit welchem den Beklagten unter anderem aufgetragen wurde, den das Unterlassungsbegehren betreffenden Urteilsspruch für die Dauer von zwei Monaten auf jener Website der Beklagten, die nähere Informationen zum Wohndachfenster liefert, unmittelbar unter der Überschrift „Wohndachfenster“ zu veröffentlichen, und zwar die Erstbeklagte auf der Website www.*****.at und die Zweitbeklagte auf der Website www.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/4Ob142_21t`) (sent_id: `deanon_260716_TRAIN/4Ob142_21t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Hon.-Prof. PD Dr. Rassi als Vorsitzenden und die Hofräte und Hofrätinnen Dr. Schwarzenbacher, Dr. Kodek, MMag. Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Laurence Perger, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei EIPD Chemie ges.m.b.H., Insel 21, 4840 Diesenbach, Österreich, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Kodek` (person)
- `MMag. Matzka` (person)
- `Mag. Istjan, LL.M.` (person)
- `Laurence Perger` (person)
- `Viehböck Breiter Schenk & Nau Rechtsanwälte OG` (organisation)
- `EIPD Chemie ges.m.b.H.` (organisation)
- `Insel 21, 4840 Diesenbach, Österreich` (address)
- `Weber-Wilfert Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/4Ob165_09g`) (sent_id: `deanon_260716_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei DRH Cloud AG, Viertlerweg 451, 2533 Glashütten, Österreich, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei West Steinfen AG, Josef-Kainzmayer-Gasse 9, 4271 Witzelsberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `DRH Cloud AG` (organisation)
- `Viertlerweg 451, 2533 Glashütten, Österreich` (address)
- `Ewald Weninger Rechtsanwalts GmbH` (organisation)
- `West Steinfen AG` (organisation)
- `Josef-Kainzmayer-Gasse 9, 4271 Witzelsberg, Österreich` (address)
- `Schönherr Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Nimtz Pharma GmbH, Mildenbergstraße 11, 3072 Furth, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1) Unikel Landwirtschaft GmbH & Co KG und 2) Gode+Panköker Getränke GmbH, Martinsplatz 1-31, 9831 Kleindorf, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Provisorialverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 6. August 2010, GZ 5 R 150/10f-7, womit der Beschluss des Handelsgerichts Wien vom 24. Juni 2010, GZ 11 Cg 117/10h-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

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
- `Unikel Landwirtschaft GmbH & Co KG` (organisation)
- `Gode+Panköker Getränke GmbH` (organisation)
- `Martinsplatz 1-31, 9831 Kleindorf, Österreich` (address)
- `Gheneff - Rami - Sommer Rechtsanwälte KG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/4Ob185_22t`) (sent_id: `deanon_260716_TRAIN/4Ob185_22t_4`)


Dr. Bernd Oberhofer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Ebler & Rieck Daten GmbH, Laubenbachgegend 2, 4203 Schwarzendorf, Österreich, vertreten durch Mag. Bert Ortner, Rechtsanwalt in Wien, wegen 95.150 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 30. Mai 2022, GZ 5 R 183/21z-131, womit das Urteil des Handelsgerichts Wien vom 30. September 2021, GZ 43 Cg 45/13k-125, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Bernd Oberhofer` (person)
- `Ebler & Rieck Daten GmbH` (organisation)
- `Laubenbachgegend 2, 4203 Schwarzendorf, Österreich` (address)
- `Mag. Bert Ortner` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Florentin Jakobautzki, vertreten durch die Konrad Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Lischke&Rohleff Solar AG, Volkshausplatz 46, 3830 Pyhra, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 106.196,74 EUR sA und Feststellung (Streitwert 156.303,26 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Oktober 2017, GZ 129 R 24/17y-24, womit das Urteil des Handelsgerichts Wien vom 2. August 2017, GZ 10 Cg 1/16a-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Vogel` (person)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `Mag. Florentin Jakobautzki` (person)
- `Konrad Rechtsanwälte GmbH` (organisation)
- `Lischke&Rohleff Solar AG` (organisation)
- `Volkshausplatz 46, 3830 Pyhra, Österreich` (address)
- `Binder Grösswang Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Savitski&Flashar Möbel GmbH, Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei Fryc+Brotzler Energie Rechtsanwälte GmbH, Lange Gasse 15, 4891 Plain, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `Savitski&Flashar Möbel GmbH` (organisation)
- `Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich` (address)
- `Dr. Manfred Sommerbauer` (person)
- `DDr. Michael Dohr, LL.M.` (person)
- `Fryc+Brotzler Energie Rechtsanwälte GmbH` (organisation)
- `Lange Gasse 15, 4891 Plain, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/6Ob207_18m`) (sent_id: `deanon_260716_TRAIN/6Ob207_18m_4`)


Bau Tratri GmbH, alle Alois Weber-Gasse 10, 9300 Blintendorf, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen (zuletzt) Widerrufs, Veröffentlichung und Zahlung von 9.000 EUR, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 30. Mai 2018, GZ 5 R 39/18v-27, womit über Berufung der beklagten Parteien das Urteil des Handelsgerichts Wien vom 24. Jänner 2018, GZ 39 Cg 26/17t-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Bau Tratri GmbH` (organisation)
- `Alois Weber-Gasse 10, 9300 Blintendorf, Österreich` (address)
- `Dr. Peter Zöchbauer` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der RheinLebensmittel Systeme GmbH, FN FN982022c, wegen § 10 Abs 2 FBG, über den Revisionsrekurs des Österreichischen Verbandes Gemeinnütziger Bauvereinigungen Revisionsverband, 1010 Wien, Bösendorferstraße 7, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 3. September 2020, GZ 6 R 158/20d-6, womit der Rekurs gegen den Beschluss des Handelsgerichts Wien vom 20. Juli 2020, GZ 72 Fr 3266/20f-3, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `RheinLebensmittel Systeme GmbH` (organisation)
- `FN982022c` (business_register_number)
- `KWR Karasek Wietrzyk Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/6Ob51_21z`) (sent_id: `deanon_260716_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Fabienne Müffler, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei See Conlemgart Gruppe Bank Schlötels&Katzenberg Digital AG, C - Obersee 27A, 4963 Nöfing, Österreich, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `Mag. Istjan, LL.M.` (person)
- `Mag. Fabienne Müffler` (person)
- `Dr. Wolfgang Haslinger, LL.M.` (person)
- `See Conlemgart Gruppe Bank` (organisation)
- `Schlötels&Katzenberg Digital AG` (organisation)
- `C - Obersee 27A, 4963 Nöfing, Österreich` (address)
- `Dr. Anton Ehm` (person)
- `Mag. Thomas Mödlagl` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/6Ob69_23z`) (sent_id: `deanon_260716_TRAIN/6Ob69_23z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Anton Endelein, BSc, vertreten durch Dr. Astrid Wagner, Rechtsanwältin in Wien, gegen die beklagte Partei Nicoletta Abtmeyer, vertreten durch Mag. Wolfgang Gartner, Rechtsanwalt in Wien, wegen 124.216,94 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2023, GZ 3 R 164/22t-29 mit dem das Urteil des Handelsgerichts Wien vom 10. August 2022, GZ 39 Cg 8/22b-24, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Dr. Nowotny` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Faber` (person)
- `Mag. Pertmayr` (person)
- `Anton Endelein, BSc` (person)
- `Dr. Astrid Wagner` (person)
- `Nicoletta Abtmeyer` (person)
- `Mag. Wolfgang Gartner` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/7Ob161_11v`) (sent_id: `deanon_260716_TRAIN/7Ob161_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei DI Wilhelm Firnekaes, vertreten durch Putz & Partner, Rechtsanwälte in Wien, gegen die beklagte und widerklagende Partei IYJW Bildung GmbH, Seeufer-Siedlung 53, 3033 Höfer, Österreich, vertreten durch die Rechtsanwälte Dr. Amhof & Dr. Damian GmbH, Wien, wegen jeweils 17.571,77 EUR (sA), über die „außerordentliche“ Revision der Beklagten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Mai 2011, GZ 3 R 42/10h-91, mit dem das Urteil des Handelsgerichts Wien vom 18. März 2010, GZ 35 Cg 42/04x (35 Cg 8/08b)-87, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Der Kläger und Widerbeklagte (im Folgenden Kläger) hat im Auftrag der Beklagten und Widerklägerin (im Folgenden Beklagte) für diese Planungs- und Prüfingenieurtätigkeiten durchgeführt.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Huber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schaumüller` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Dr. Wurdinger` (person)
- `DI Wilhelm Firnekaes` (person)
- `IYJW Bildung GmbH` (organisation)
- `Seeufer-Siedlung 53, 3033 Höfer, Österreich` (address)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, 1041 Wien, Prinz-Eugen-Straße 20-22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Sudlex Heizung AG, Weißenbachstraße 12, 9376 Lichtegg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2011, GZ 2 R 203/11d-11, womit das Urteil des Handelsgerichts Wien vom 26. Juni 2011, GZ 19 Cg 49/11v-5, teilweise abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Malesich` (person)
- `Dr. Walter Reichholf` (person)
- `Sudlex Heizung AG` (organisation)
- `Weißenbachstraße 12, 9376 Lichtegg, Österreich` (address)
- `Schönherr Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `Dr. Weber` (person)
- `Mag. Fitz` (person)
- `Mag. Jelinek` (person)
- `Gundula Aichmann` (person)
- `Poduschka Partner Anwaltsgesellschaft mbH` (organisation)
- `Plönnigs Technik AG` (organisation)
- `Wieden 35, 3390 Spielberg, Österreich` (address)
- `Themmer, Toth & Partner Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts für Handelssachen Wien` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. Roderich Florczyk, vertreten durch Dr. Norbert Nowak, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel-Energie AG, Gaunitzhof 8, 4632 Breitwies, Österreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen 6.342,73 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 8. November 2018, GZ 60 R 98/18v-12, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 15. Juni 2018, GZ 18 C 109/18p-8, abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Ing. Roderich Florczyk` (person)
- `Dr. Norbert Nowak` (person)
- `Mittel-Energie AG` (organisation)
- `Gaunitzhof 8, 4632 Breitwies, Österreich` (address)
- `Schönherr Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts für Handelssachen Wien` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_6`)


Renzlhausen 24, 6553 See, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Dorda Brugger Jordis Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts für Handelssachen Wien` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Karen Jansonius, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Schopf Automotive AG Grebien-Gasse 50, 4675 Dirisam, Österreich, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Karen Jansonius` (person)
- `Dr. Herwig Ernst` (person)
- `Schopf Automotive AG` (organisation)
- `Grebien-Gasse 50, 4675 Dirisam, Österreich` (address)
- `Dr. Herbert Laimböck` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/7Ob94_20d`) (sent_id: `deanon_260716_TRAIN/7Ob94_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Juliana Mündelein, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ACBK Elektro Solutions AG, Schwarzenseer Straße 25, 9560 Steuerberg, Österreich, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Mag. Juliana Mündelein` (person)
- `Brand Rechtsanwälte GmbH` (organisation)
- `ACBK Elektro Solutions AG` (organisation)
- `Schwarzenseer Straße 25, 9560 Steuerberg, Österreich` (address)
- `Dorda Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/8Ob35_23i`) (sent_id: `deanon_260716_TRAIN/8Ob35_23i_6`)


Die Klägerinnen führten vor dem Handelsgericht Wien zu AZ 31 Cg 110/05v ein Verfahren gegen den Hersteller eines Tresors, der nicht darauf hingewiesen hatte, dass bei der Festlegung des Codes eine Wiederholung von Ziffern vermieden werden müsse.

| Predicted | Gold |
|---|---|
| `Handelsgericht Wien` | `Handelsgericht Wien` |

**Example 33** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei UnterTransport GmbH, Arnold-Rosé-Gasse 16, 8345 Krusdorf, Österreich, vertreten durch Knirsch Gschaider & Cerha Rechtsanwälte OG in Wien, sowie des Nebenintervenienten auf Seiten der klagenden Partei Dr. Scarlett Grimmecke, gegen die beklagte Partei Siebentritt Transport GesmbH, Pungartweg 25, 5232 Moosdorf, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, wegen 159.824,87 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2018, GZ 129 R 55/18h-40, mit dem der Berufung der klagenden Partei gegen das Urteil des Handelsgerichts Wien vom 6. April 2018, GZ 21 Cg 23/15s-36, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

| Predicted | Gold |
|---|---|
| `Handelsgerichts Wien` | `Handelsgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `UnterTransport GmbH` (organisation)
- `Arnold-Rosé-Gasse 16, 8345 Krusdorf, Österreich` (address)
- `Gschaider & Cerha Rechtsanwälte OG` (organisation)
- `Dr. Scarlett Grimmecke` (person)
- `Siebentritt Transport GesmbH` (organisation)
- `Pungartweg 25, 5232 Moosdorf, Österreich` (address)
- `Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte` (organisation)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

## `VwGH` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `92cfdcf2`  
**Description:**
Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof) which was frequently missed.

**Content:**
```
\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 3838 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_29`)


Hingegen sind die Kosten einer rechtsfreundlichen Vertretung vom Bundesverwaltungsgericht nicht zuzusprechen (VwGH 2005/04/0257;ReisnerinHeid/Preslmayr, Vergaberecht4[2015] Rz 2034).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_44`)


Ein Antrag auf Feststellung des in einem Nachprüfungsverfahren geltend gemachten Vergaberechtsverstoßes ist nämlich nach dem Widerruf dieses Vergabeverfahrens nicht mehr möglich (VwGH 2012/04/0133).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_17`)


Da von mehreren vom Gesetz alternativ zur Verfügung gestellten Möglichkeiten der Verständigung des Empfängers von der Hinterlegung jene zu wählen ist, von der angenommen werden kann, dass sie die größere Gewähr dafür bietet, dass der Empfänger die Verständigung tatsächlich erhält (vglWalter/Mayer, Das Österreichische Zustellrecht [1983] § 17 ZustG Anm 21;WesselyinFrauenberger-Pfeiler/ Raschauer/Sander/Wessely, Österreichisches Zustellrecht² [2011] § 17 ZustG Rz 6 unter Hinweis auf 9 ObA 64/93; siehe auch VwGH Ra 2017/20/0290;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_22`)


Da die Vorschriften über die Zustellung (und daher auch über die Art der Zurücklassung der Hinterlegungsanzeige) durch eine Vereinbarung zwischen dem Postzusteller und dem Empfänger nicht geändert werden können (VwGH 87/05/0063), kommt es entgegen der Ansicht der Revisionsrekurswerberin nicht darauf an, ob die „Zeitungsröhre“ bisher „anstandslos“ für sämtliche Postzustellungen genutzt wurde.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/7Ob193_21i`) (sent_id: `deanon_260716_TRAIN/7Ob193_21i_23`)


[6] 4.1 Der hier interessierende Art 9.2.3.1.1 des Rahmenvertrags entspricht § 117 Abs 4 GewO 1994 (vgl VwGH 2007/04/0198 mwN).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8Ob101_14g`) (sent_id: `deanon_260716_TRAIN/8Ob101_14g_12`)


Hinsichtlich der vom Klagebegehren betroffenen Liegenschaften hat nicht nur die Agrarbehörde über diese Frage bereits entschieden, sondern liegt auch ein letztinstanzliches Erkenntnis des Verwaltungsgerichtshofs vor (VwGH 15.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_34`)


2.2.Demgegenüber erachtetMüller(Judikaturdivergenzen zwischen VwGH und OGH? - Eine Entwarnung, ZAS 2003/22;ders, Nochmals: Kollektivvertraglicher Mindestlohn und Sachbezug in der Sozialversicherung, ASoK 2002, 220), die kollektivvertraglichen Entlohnungsbestimmungen im Ergebnis als zweiseitig zwingende Anordnung eines Barzahlungsgebots, sodass es auf einen Günstigkeitsvergleich nicht mehr ankomme.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Missed by this rule (FN):**

- `OGH` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_35`)


Diese Ansicht teilen auchLöschnigg(Entscheidungsanmerkung zu VwGH 95/08/0037, DRdA 2003, 340 f),Spitzl/Huber(inKuras[Hrsg], Handbuch Arbeitsrecht [1997] Pkt. 3.2.3.),Preiss(in ZellKomm2§ 78 GewO Rz 7),Kozak(inReissner, AngG2§ 42 Rz 34) undKarner(inMazal/Risak, Arbeitsrecht, System und Praxiskommentar [2014] Kap.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_41`)


Ob der Marktwert der vom Arbeitgeber tatsächlich gewährten Naturalbezüge im Ergebnis höher sei als der „vereinbarte Wert“, dh höher als jener Teil des Barentgelts, an dessen Stelle die Sachbezüge geleistet werden sollten, sei daher unentscheidend (VwGH vom 22. 3. 1994, 92/08/0150;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

## `LandesgerichtComplex` 🏆

**F1:** 0.226 | **Precision:** 0.954 | **Recall:** 0.128  

**Format:** `regex`  
**Rule ID:** `12aa6f89`  
**Description:**
Matches 'Landesgericht' with complex location suffixes like 'für Zivilrechtssachen Graz' or 'St. Pölten' which were previously truncated.

**Content:**
```
\bLandesgericht(?:s)?\s+(?:f\u00fcr\s+(?:Zivilrechtssachen|Strafsachen)?\s+)?[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?(?:\s+[A-Z][a-zA-Z]+)?(?:\s+-\s+[A-Z][a-zA-Z]+)?(?:\s+an\s+der\s+Donau)?(?:\s+St\.\sP\u00f6lten)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.954 | 0.128 | 0.226 | 539 | 514 | 25 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 514 | 25 | 3481 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_6`)


Die in Wien ansässige klagende Gesellschaft nimmt die in Linz ansässige beklagte Gesellschaft beim Landesgericht Linz auf restliche Honorare für Planungsleistungen für ein Bauvorhaben in Klosterneuburg bei Wien in Anspruch.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_12`)


[3] Bereits in der Klage beantragt dieKlägerindie Delegierung der Rechtssache an das Landesgericht Korneuburg.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_29`)


Die Rechtssache weist keinen eindeutigen Schwerpunkt zum Landesgericht Korneuburg auf.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_30`)


Zwar ist das Bauvorhaben im Sprengel des Landesgerichts Korneuburg situiert.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_32`)


Damit kann nicht gesagt werden, dass die Gründe für eine Übertragung der Rechtssache vom Landesgericht Linz an das Landesgericht Korneuburg überwiegen.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Dr. Roland Kassowitz` (person)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
- `Handelsgericht Wien` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Bezirksgerichts Rattenberg` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Klagenfurt` | `Landesgerichts Klagenfurt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Kevin Maassen` (person)
- `Dr. Clemens Lintschinger` (person)
- `Hon.-Prof. Friedhelm Adde` (person)
- `Mag. Dr. Georg Backhausen` (person)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Anita Schetzel` (person)
- `Bezirksgerichts Wels` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Bezirksgerichts Zwettl` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Mag. Florian Kucera` (person)
- `Mag. Timon Schönswetter` (person)
- `Doschek Rechtsanwalts GmbH` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_10`)


2008 erfolgte die Eintragung beim Firmenbuch des Landesgerichts Eisenstadt mit einer Niederlassung in Angyalföldstraße 52, 4193 Hayrl, Österreich.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Missed by this rule (FN):**

- `Angyalföldstraße 52, 4193 Hayrl, Österreich` (address)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Lars Ballogh` (person)
- `Mag. Anton Bohmert` (person)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

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
- `Pieler & Pieler & Partner KG` (organisation)
- `Dr. Madeleine Musialik` (person)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


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

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_5`)


Im Zusammenhang mit diesem Verfahren wies das Landesgericht für Zivilrechtssachen Wien mit Beschluss vom 26.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_6`)


11. 2008, GZ 38 Nc 13/08i-2, den Ablehnungsantrag des Mag. Herwig Berkenbrink in dessen Rekurs gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 13.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Mag. Herwig Berkenbrink` (person)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Bezirksgerichts Feldkirch` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Karsten Alberter` (person)
- `2. April 2010` (date)
- `Helmut Dreilich` (person)
- `Bezirksgerichts Schwechat` (organisation)
- `Lena Amini` (person)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Dr. Wallner-Friedl` (person)
- `Karim Mielewczik` (person)
- `Dr. Sandro Gädecken` (person)
- `Ing. Dr. Stefan Krall` (person)
- `Dr. Oliver Kühnl` (person)
- `Bezirksgerichts Seekirchen` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Klagenfurt` | `Landesgerichts Klagenfurt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Graz` | `Landesgerichts für Zivilrechtssachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `DI Dr. Bodo Kaczynski` (person)
- `25. Juli 1975` (date)
- `Mag. Werner Thurner` (person)
- `Wolfgang Lombardini` (person)
- `4. Dezember 2022` (date)
- `Livia Löblein` (person)
- `11. Januar 1966` (date)
- `Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft` (organisation)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Dr. Felix Cornils` (person)
- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

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
- `Magistrat der Stadt Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Othmar Mertl` (person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG` (organisation)
- `Malik Fridt` (person)
- `Krist Bubits Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_9`)


Im Rahmen seiner Äußerung zu diesem Unterhaltserhöhungsantrag lehnte der Antragsgegner jeweils alle Richter des Bezirksgerichts Josefstadt und des diesem übergeordneten Landesgerichts für Zivilrechtssachen Wien ab.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Bezirksgerichts Josefstadt` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_12`)


Da mehrere Senate des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht an dem genannten Verhalten beteiligt gewesen seien, sei auch das gesamte Landesgericht für Zivilrechtssachen Wien als befangen anzusehen, über den nunmehr geltend gemachten Unterhaltsanspruch zu entscheiden.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Bezirksgerichts Josefstadt` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mikolaj Eleftheriadou` (person)
- `Helge Schuchmann` (person)
- `Isabel Rahnfeld` (person)
- `PhD Daniel Coutand` (person)
- `Mag. Dirk Hükelheim` (person)
- `Mag. Roland Marko` (person)
- `Dr. Francisco Rumpf` (person)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Dr. Weber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Agatha von der Heide` (person)
- `MMag. Dr. Sebastian Pribas` (person)
- `Mag. Benedikt Walch` (person)
- `Alva Sengül` (person)
- `Selina Birkmeir` (person)
- `Harald Ladwig, LLM` (person)
- `In der Klaus 72, 4785 Bach, Österreich` (address)
- `Mag. German Bertsch` (person)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Graz` | `Landesgerichts für Zivilrechtssachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mag. Claudia Gründel` (person)
- `Mathias Jendl` (person)
- `Dr. Thomas Stampfer` (person)
- `Dr. Christoph Orgler` (person)
- `Dr. Michael Stögerer` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_12`)


Mit Beschluss des Landesgerichts für Strafsachen Graz vom 18.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_14`)


Mit Urteil des Landesgerichts für Strafsachen Graz vom 14. 12. 2016, 222 Hv 68/16m, wurde er gemäß § 21 Abs 1 StGB in eine Anstalt für geistig abnorme Rechtsbrecher eingewiesen, wo er seit 20.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 50** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Gabriele Griehsel` (person)
- `Dr. Wolfgang Kozak` (person)
- `Roland Soukup` (person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Graz` | `Landesgerichts für Zivilrechtssachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Mag. Lendl` (person)
- `Mag. Michel` (person)
- `Dr. Oshidari` (person)
- `Dr. Parapatits` (person)
- `Bernhard Buddäus` (person)
- `Norbert Wehrhahn` (person)
- `Mag. Höpler` (person)
- `Mag. Rienmüller` (person)

**Example 53** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 54** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Mag. Lendl` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Sommer` (person)
- `Richard Lindt` (person)

**Example 55** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wurde die von Richard Lilienfein erhobene Nichtigkeitsbeschwerde gegen das Urteil des Landesgerichts Salzburg vom 17. Juni 2011, GZ 40 Hv 147/10g-538, als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Richard Lilienfein` (person)

**Example 56** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_8`)


Die von Richard Leissner gegen das ihn freisprechende Urteil des Einzelrichters des Landesgerichts Salzburg vom 17. Juni 2011 ausdrücklich an den Obersten Gerichtshof gerichtete Nichtigkeitsbeschwerde wurde vom Erstgericht zutreffend gemäß § 285a Z 1 StPO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Richard Leissner` (person)
- `Obersten Gerichtshof` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Mag. Lendl` (person)
- `Mag. Michel` (person)
- `Dr. Oshidari` (person)
- `Mag. Kurzthaler` (person)
- `Andreas Schiessl` (person)

**Example 58** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oberressl` (person)
- `Mag. Rathgeb` (person)
- `Daniel Kur` (person)

**Example 59** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oberressl` (person)
- `Mag. Wieser` (person)
- `Gerald Winand` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Gerald Wandscheer` (person)

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bäseke` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `OGH` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Mag. Herwig Berto` (person)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Mag. Herwig Bleuler` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_9`)


Dieses Verfahren hat unter anderem auch als mit Strafe bedrohte Handlungen iSd § 107 Abs 1 und 2 erster Fall StGB subsumierte Anlasstaten zum Nachteil der genannten Richter des Obersten Gerichtshofs zum Gegenstand (US 7, 10 des erwähnten Urteils des Landesgerichts für Strafsachen Wien).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Oliver Pekarek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `OGH` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Gerhard Bukowska` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `OGH` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und Hofrätin des Obersten Gerichtshofs Mag. Michel sind von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Gerhard Boesl betreffend das Verfahren AZ 16 Hv20/14x des Landesgerichts für Strafsachen Wien ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `Gerhard Boesl` (person)

**Example 67** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_6`)


Gründe:  Rechtliche Beurteilung Der Oberste Gerichtshof hat zu AZ 11 Os 5/15t über die gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, ergriffene Nichtigkeitsbeschwerde und Berufung des Angeklagten Gerhard Bugnenings zu entscheiden.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Gerhard Bugnenings` (person)

**Example 68** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_14`)


Senat des Obersten Gerichtshofs - unter dem Aspekt der §§ 281 Abs 1 Z 5a, 362 StPO - auch der Tatverdacht hinsichtlich eines Tatzeitraums („August 2008 bis längstens 14. Dezember 2008“ - vgl Urteil des Landesgerichts für Strafsachen Wien vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, US 2) zu prüfen, auf den sich auch das Oberlandesgericht Wien in Entscheidungen bezog, die unter Mitwirkung der Angehörigen des Anzeigers getroffen wurden (vgl insb BS 32 f in AZ 19 Bs 465/12i).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Oberlandesgericht Wien` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bernts` (person)
- `OGH` (organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Ahmed Koehnen` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `OGH` (organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_7`)


Mit dem erwähnten Beschluss vom 25. November 2019 hatte das Oberlandesgericht Wien einer Beschwerde des Ahmed Kocks gegen einen Beschluss des Landesgerichts für Strafsachen Wien auf Ablehnung eines Antrags des Genannten auf Wiederaufnahme des Verfahrens AZ 606 Hv 1/11m jenes Gerichts nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Ahmed Kocks` (person)

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Mann` (person)
- `Dr. Brenner` (person)
- `Mag. Rögner` (person)
- `Thomas Michenfelder` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Gföller` (person)
- `Dr. Zeh-Gindl` (person)

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


Dieser Beschluss wird aufgehoben und es wird in der Sache selbst erkannt, dass der Senatspräsident des Oberlandesgerichts Wien Dr. Krenn sowie die Richterinnen des Oberlandesgerichts Wien Mag. Edwards und Mag. Sanda von der Entscheidung über die Berufung des Angeklagten gegen das Urteil des Landesgerichts Krems an der Donau vom 8. August 2018, GZ 38 Hv 40/18z-100, nicht ausgeschlossen sind.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Dr. Krenn` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_6`)


Text Gründe: Soweit für die Behandlung der Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Bedeutung wurde Thomas Maksym mit Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB (I./) sowie der Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB (II./) und des Betrugs nach § 146 StGB (III./) schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Aus Anlass der (allein aufrechterhaltenen) Berufung des Angeklagten wegen des Ausspruchs über die Strafe (ON 86) hob der zuständige 21.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Thomas Maksym` (person)

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_10`)


Im zweiten Rechtsgang sprach die Einzelrichterin des Landesgerichts Krems an der Donau Thomas Muthardt mit Urteil vom 8. August 2018 (ON 100) neuerlich anklagekonform schuldig und verurteilte ihn zu einer Freiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Thomas Muthardt` (person)

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_13`)


Dazu führte er aus, dass die genannten Richter das Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) in amtswegiger Wahrnehmung des Nichtigkeitsgrundes des § 281 Abs 1 Z 9 lit a [der Sache nach Z 10] StPO „großteils aufgehoben“ und „dabei“ „die Tatfrage mit Hinweis auf die Strafbarkeit des angelasteten Verhaltens indizierende Verfahrensergebnisse mit voller Kognitionsbefugnis [beurteilt] und […] beweiswürdigend Stellung bezogen“ hätten.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fruhmann` (person)
- `Gebhard Sayin` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_4`)


Text Gründe: Mit der angefochtenen Entscheidung wies das Oberlandesgericht Wien die Beschwerde des Gebhard Senkfeil gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 25. September 2012, GZ 130 Bl 65/12s-10, mit welchem der Antrag des Beschwerdeführers auf Fortführung des Verfahrens AZ 20 UT 91/12p der Staatsanwaltschaft Wien gegen unbekannte Täter wegen § 302 Abs 1 StGB zurückgewiesen worden war, als unzulässig zurück (§ 196 Abs 1 StPO).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Gebhard Senkfeil` (person)

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__4`)


Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt verletzen 1./ die Durchführung der Hauptverhandlung und Urteilsfällung am 26. September 2018 in Abwesenheit des Angeklagten § 427 Abs 1 StPO, 2./ die Verlesung des die Vernehmung des Zeugen Alexander Struttmann beinhaltenden Teils des Hauptverhandlungsprotokolls vom 28. Februar 2018 (ON 9) in der Hauptverhandlung am 26. September 2018 § 252 Abs 1 StPO iVm § 447 StPO, 3./ der unter einem mit dem Urteil vom 26. September 2018 (ON 25) gefasste Beschluss auf Widerruf der Nenad Pohlmann mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht § 494a Abs 3 StPO und 4./ das Urteil vom 26. September 2018 (ON 25) § 31 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Bezirksgerichts Leopoldstadt` (organisation)
- `Alexander Struttmann` (person)
- `Nenad Pohlmann` (person)

**Example 80** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__7`)


Ferner beantragte die Staatsanwaltschaft, die Nenad Pleßing mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährte bedingte Strafnachsicht (vgl ON 2 S 32) zu widerrufen, und wies darauf hin, dass der Widerruf der mit Urteil des genannten Gerichts vom 19. September 2017, AZ 44 Hv 88/17g, gewährten bedingten Strafnachsicht dem zuständigen Gerichtshof vorzubehalten sei.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Nenad Pleßing` (person)

**Example 81** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__14`)


Eine Bedachtnahme auf das Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, (unjournalisiert im Akt einliegend nach ON 27; vgl ON 22 Punkt 2./) gemäß § 31 StGB, erfolgte nicht.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 82** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__15`)


Zugleich fasste es den Beschluss auf Widerruf (§ 494a Abs 1 Z 4 StPO) der Nenad Plettener mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht einer Freiheitsstrafe, ohne zuvor diesen Akt oder zumindest eine Abschrift des Urteils beigeschafft zu haben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Nenad Plettener` (person)

**Example 83** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__16`)


In Ansehung der dem Angeklagten mit Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, gewährten bedingten Strafnachsicht erging ein auf § 494a Abs 2 letzter Satz StPO gestützter Vorbehaltsbeschluss.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 84** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__18`)


Über die rechtzeitige Beschwerde der Staatsanwaltschaft gegen den Beschluss auf Widerruf bedingter Strafnachsicht (ON 28) wurde noch nicht entschieden (AZ 131 Bl 94/18x des Landesgerichts für Strafsachen Wien).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 85** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__28`)


Der Strafantrag vom 28. November 2017, aus dem der Antrag der Staatsanwaltschaft auf Widerruf der bedingten Strafnachsicht zu AZ 162 Hv 117/14k des Landesgerichts für Strafsachen Wien ersichtlich ist (ON 4), wurde dem Angeklagten durch Zustellung zur Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 86** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__32`)


Die unterbliebene Bedachtnahme auf das aktenkundige Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, verletzt daher mit Blick auf den Zeitpunkt der dem Abwesenheitsurteil zugrunde liegenden Tat (3. Februar 2017) § 31 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 87** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_3`)


Kopf Der Oberste Gerichtshof hat am 15. März 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ettel als Schriftführerin in der Maßnahmenvollzugssache des Andreas Wegele, AZ 181 BE 143/17y des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 9. Jänner 2018, AZ 131 Bs 370/17z, und seinen Antrag auf Bewilligung der Verfahrenshilfe nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Mag. Ettel` (person)
- `Andreas Wegele` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_5`)


Text Gründe: Mit dem angefochtenen Beschluss vom 9. Jänner 2018, AZ 131 Bs 370/17z, gab das Oberlandesgericht Wien als Rechtsmittelgericht der Beschwerde des Andreas Wackerow gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 20. November 2017, GZ 181 BE 143/17y-16, mit dem die bedingte Entlassung aus einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 2 StGB abgelehnt worden war, nicht Folge.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Andreas Wackerow` (person)

**Example 89** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__9`)


Unter einem erging der Beschluss, gemäß § 494a Abs 1 Z 2 StPO vom Widerruf der zum AZ 36 Hv 118/05p des Landesgerichts Innsbruck und zum AZ 3 U 350/06d des Bezirksgerichts Kufstein jeweils gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Bezirksgerichts Kufstein` (organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


Kopf Der Oberste Gerichtshof hat am 12. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Ruckendorfer als Schriftführerin in der Strafsache gegen Thomas Leutz wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 13. September 2018, GZ 35 Hv 46/18m-130, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Ruckendorfer` (person)
- `Thomas Leutz` (person)

**Example 91** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, im Ausspruch über den Verfall aufgehoben, soweit er sich auf einen 35.353,95 Euro übersteigenden Betrag bezieht, und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Example 92** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_26`)


In Stattgebung der Nichtigkeitsbeschwerde des Angeklagten war daher das angefochtene Urteil wie im Spruch ersichtlich aufzuheben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck (§ 445 Abs 2 StPO;

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Example 93** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Hauer` (person)
- `Viktor Marschmeyer` (person)
- `Dr. Stefan Toepfl` (person)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_10`)


Die Klägerin stützte die Zuständigkeit des von ihr angerufenen Landesgerichts Wr. Neustadt als Handelsgericht auf § 88 Abs 1 und 2 JN.

**False Positives:**

- `Landesgerichts Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_11`)


Für den Fall der örtlichen Unzuständigkeit des angerufenen Gerichts beantragte die Klägerin gemäß § 28 JN die Bestimmung des Landesgerichts Wr. Neustadt als Handelsgericht als für den gegenständlichen Rechtsstreit örtlich zuständiges Gericht.

**False Positives:**

- `Landesgerichts Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns-Umwelt`(organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich`(address)
- `Ing. Lara Markart`(person)
- `Radel Stampf Supper Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

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

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

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

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

</details>

---

## `LawFirmGmbH` 🏆

**F1:** 0.017 | **Precision:** 0.773 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `2e8c885d`  
**Description:**
Matches law firm names ending in 'Rechtsanwälte GmbH' or 'Rechtsanwälte GmbH & Co KG', requiring at least two capitalized name parts to avoid partial matches like 'Ludwig Rechtsanwälte GmbH'.

**Content:**
```
\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+\s+Rechtsanw\u00e4lte\s+GmbH(?:\s*&\s*Co\s*KG)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.773 | 0.008 | 0.017 | 44 | 34 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 34 | 10 | 3738 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vavrovsky Heine Marth Rechtsanwälte GmbH` | `Vavrovsky Heine Marth Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Heimcon Software GmbH` (organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich` (address)
- `Gunter Landwirtschaft GmbH` (organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich` (address)
- `Stolz & Schartner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Brandl Talos Rechtsanwälte GmbH` | `Brandl Talos Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `DDr.in Cornelia Rinaldo` (person)
- `Dr. Sven Rudolf Thorstensen` (person)
- `Conmon-Verlag Limited` (organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende und die Hofräte Dr. Musger und Priv.-Doz. Dr. Rassi, die Hofrätin Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Dr. Joshua Reupold, als Masseverwalter über das Vermögen der Wald-Versand Gesellschaft mbH, Kugelmannplatz 4, 5121 Döstling, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, gegen die beklagten Parteien 1. Johanna Baldczus, und 2. MedR Nadja Grela, beide vertreten durch Schöpf & Maurer, Rechtsanwalt in Salzburg, wegen 59.028,60 EUR sA, aus Anlass der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. April 2019, GZ 1 R 161/18d-52, mit dem das Urteil des Landesgerichts Salzburg vom 30. August 2018, GZ 57 Cg 10/17z-43, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das angefochtene Urteil wird, soweit es die Abweisung des Teilbegehens, die beklagten Parteien seien zur ungeteilten Hand schuldig, der klagenden Partei 18.168,21 EUR samt 4 % Zinsen seit 15.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Dr. Joshua Reupold` (person)
- `Wald-Versand Gesellschaft mbH` (organisation)
- `Kugelmannplatz 4, 5121 Döstling, Österreich` (address)
- `Johanna Baldczus` (person)
- `MedR Nadja Grela` (person)
- `Maurer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/18OCg12_19t`) (sent_id: `deanon_260716_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Energie Glanzgart GmbH, Waldelweg 28, 4201 Maierleiten, Österreich, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Piedro Arnoult, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH` | `SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Veith` (person)
- `Dr. Höllwerth` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `Mag. Painsi` (person)
- `Energie Glanzgart GmbH` (organisation)
- `Waldelweg 28, 4201 Maierleiten, Österreich` (address)
- `Piedro Arnoult` (person)

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ludmilla Bonauer, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Henriette Geißendorf, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Puttinger Vogl Rechtsanwälte GmbH` | `Puttinger Vogl Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Ludmilla Bonauer` (person)
- `Korp Rechtsanwalts GmbH` (organisation)
- `Henriette Geißendorf` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob109_18p`) (sent_id: `deanon_260716_TRAIN/1Ob109_18p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Eva Voeglein, und 2. Ursula Preising, vertreten durch die HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH, Graz, gegen die beklagte Partei Gemeinde Veit Faeser, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 573.890,70 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 2. Mai 2018, GZ 5 R 172/17d-57, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 23. Oktober 2017, GZ 41 Cg 51/15m-47, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH` | `HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Eva Voeglein` (person)
- `Ursula Preising` (person)
- `Veit Faeser` (person)
- `Dr. Klaus Rainer` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Harald Adolphsen KG, FN FN214876m, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Alpen Donalcon “ OXS Bildung gmbH, FN FN067476g, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `GRAF ISOLA Rechtsanwälte GmbH` | `GRAF ISOLA Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Harald Adolphsen` (person)
- `FN214876m` (business_register_number)
- `Dr. Eva-Maria Bachmann` (person)
- `Dr. Christian Bachmann` (person)
- `Alpen Donalcon` (organisation)
- `OXS Bildung gmbH` (organisation)
- `FN067476g` (business_register_number)
- `Oberlandesgerichts Wien` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH, Orise 28, 9135 Unterort, Österreich, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Li Wachmeister, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Estermann Pock Rechtsanwälte GmbH` | `Estermann Pock Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Pia Geermann` (person)
- `Orise 28, 9135 Unterort, Österreich` (address)
- `Dr. Martin Leitner` (person)
- `Li Wachmeister` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/1Ob95_21h`) (sent_id: `deanon_260716_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Gawelzyk Pflege GmbH, Am See IX 247, 6320 Achleit, Österreich, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Loos und Woiciech Analyse GmbH, Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Gawelzyk Pflege GmbH` (organisation)
- `Am See IX 247, 6320 Achleit, Österreich` (address)
- `Zumtobel Kronberger Rechtsanwälte OG` (organisation)
- `Loos und Woiciech Analyse GmbH` (organisation)
- `Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Ried im Innkreis` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_5`)


Seecon Verlag GmbH, Krengasse 31, 3911 Marbach am Walde, Österreich, und 2. Mag. Lena Zikorski, beide vertreten durch die Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen jeweils 50.000,50 EUR sA (Klagen) und 483.000 EUR sA (Widerklagen), über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. April 2010, GZ 15 R 257/09p-58, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` | `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Seecon Verlag GmbH` (organisation)
- `Krengasse 31, 3911 Marbach am Walde, Österreich` (address)
- `Mag. Lena Zikorski` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/2Ob194_24d`) (sent_id: `deanon_260716_TRAIN/2Ob194_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dagobert Drügemöller, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Rosalinde Nölker, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH` | `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `MMag. Sloboda` (person)
- `Dr. Thunhart` (person)
- `Dr. Kikinger` (person)
- `Mag. Fitz` (person)
- `Dagobert Drügemöller` (person)
- `Rosalinde Nölker` (person)
- `Mag. Simon Wallner Rechtsanwalt GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/3Ob108_18f`) (sent_id: `deanon_260716_TRAIN/3Ob108_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Dr. Denis Aichmüller, vertreten durch Scherbaum Seebacher Rechtsanwälte GmbH in Graz, wider die beklagte Partei Hemma Fenski, vertreten durch Dr. Destaller ua, Rechtsanwälte in Graz, wegen (eingeschränkt) Räumung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 23. Februar 2018, GZ 7 R 137/17v-19, mit dem das Urteil des Bezirksgerichts Graz-Ost vom 29. September 2017, GZ 213 C 131/16m-15, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Scherbaum Seebacher Rechtsanwälte GmbH` | `Scherbaum Seebacher Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Roch` (person)
- `Dr. Rassi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Denis Aichmüller` (person)
- `Hemma Fenski` (person)
- `Dr. Destaller` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Moritz Absmeier, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei DENU Immobilien GmbH, Gürtel 12, 5145 Schmalzhofen, Österreich, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` | `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Moritz Absmeier` (person)
- `Dr. Martin Neuwirth` (person)
- `Dr. Alexander Neurauter` (person)
- `DENU Immobilien GmbH` (organisation)
- `Gürtel 12, 5145 Schmalzhofen, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


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

**Example 14** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Anton Reuschel, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde KommR Frieda Goetzens, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Ebner Aichinger Guggenberger Rechtsanwälte GmbH` | `Ebner Aichinger Guggenberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Anton Reuschel` (person)
- `Mag. Christopher Schmied` (person)
- `KommR Frieda Goetzens` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/4Nc30_22g`) (sent_id: `deanon_260716_TRAIN/4Nc30_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Iris Gscheider, vertreten durch Dr. Sabine C.M. Deutsch, Rechtsanwältin in Riegersburg, gegen die beklagte Partei Mag. Annette Salzbauer, als Masseverwalter im Konkursverfahren über das Vermögen von Lynn Galleitner (AZ 26 S 10/21x des Landesgerichts für Zivilrechtssachen Graz), vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Graz, wegen Unterlassung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der unmittelbar beim Obersten Gerichtshof eingebrachte Delegierungsantrag samt Beilagen wird dem Landesgericht für Zivilrechtssachen Graz als Erstgericht zu AZ 10 Cg 83/22z zur geschäftsordnungsgemäßen Behandlung übermittelt. Begründung:  Rechtliche Beurteilung [1]

| Predicted | Gold |
|---|---|
| `GRAF ISOLA Rechtsanwälte GmbH` | `GRAF ISOLA Rechtsanwälte GmbH` |

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
- `Obersten Gerichtshof` (organisation)
- `Landesgericht für Zivilrechtssachen Graz` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/4Ob100_13d`) (sent_id: `deanon_260716_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Karen Böckel, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Düwall + Rief Daten -Aktiengesellschaft, Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ Eberhard Besemer ” Linda Hukauf, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Raits Bleiziffer Rechtsanwälte GmbH` | `Raits Bleiziffer Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `Karen Böckel` (person)
- `Kosesnik-Wehrle & Langer Rechtsanwälte KG` (organisation)
- `Düwall + Rief Daten -Aktiengesellschaft` (organisation)
- `Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich` (address)
- `Eberhard Besemer` (person)
- `Linda Hukauf` (person)
- `Dr. Peter Zöchbauer` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/4Ob201_10b`) (sent_id: `deanon_260716_TRAIN/4Ob201_10b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kevin Woelfel OEG, Rudolf Radinger-Straße 110o, 4623 Moostal, Österreich, vertreten durch Dr. Martin Leitner und Dr. Ralph Trischler, Rechtsanwälte in Wien, gegen die beklagte Partei Rätz Handel GmbH, Schögglstraße 25, 4085 Dankmairing, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung, Rechnungslegung, Schadenersatz und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. September 2010, GZ 1 R 192/10b-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß Der Antrag auf Zuspruch der Kosten der Revisionsrekursbeantwortung wird gemäß § 508a Abs 2 Satz 2 und § 521a Abs 2 ZPO abgewiesen.

| Predicted | Gold |
|---|---|
| `Bichler Zrzavy Rechtsanwälte GmbH` | `Bichler Zrzavy Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `Kevin Woelfel` (person)
- `Rudolf Radinger-Straße 110o, 4623 Moostal, Österreich` (address)
- `Dr. Martin Leitner` (person)
- `Dr. Ralph Trischler` (person)
- `Rätz Handel GmbH` (organisation)
- `Schögglstraße 25, 4085 Dankmairing, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/4Ob9_20g`) (sent_id: `deanon_260716_TRAIN/4Ob9_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ingrid Marke, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) ZTYW Solar Vertrieb GmbH, Hans-Woerle-Weg 13, 4852 Gahberg, Österreich, und 2) Hoch Fenfurtmon Systeme AG, Raxer Straße 24, 8952 Kienach, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

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
- `Hoch Fenfurtmon Systeme AG` (organisation)
- `Raxer Straße 24, 8952 Kienach, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/5Ob102_24x`) (sent_id: `deanon_260716_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei ÖkR KzlR Sonja Doganoglu, wider die beklagte Partei Stoeberl Bau AG, Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `ÖkR KzlR Sonja Doganoglu` (person)
- `Stoeberl Bau AG` (organisation)
- `Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich` (address)
- `Landesgerichts Ried im Innkreis` (organisation)
- `Bezirksgerichts Schärding` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Svenja Brochtrup, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei EnnsFinanzen AG, Bartlstraße 9, 8490 Zelting, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `Svenja Brochtrup` (person)
- `EnnsFinanzen AG` (organisation)
- `Bartlstraße 9, 8490 Zelting, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_3`)


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

**Example 22** (doc_id: `deanon_260716_TRAIN/6Ob10_22x`) (sent_id: `deanon_260716_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Tralog-KI Versicherungs AG, Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei WaldRecycling GmbH, Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Dr. Nowotny` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Faber` (person)
- `Mag. Pertmayr` (person)
- `Tralog-KI Versicherungs AG` (organisation)
- `Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich` (address)
- `Musey Rechtsanwalt GmbH` (organisation)
- `WaldRecycling GmbH` (organisation)
- `Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/6Ob146_18s`) (sent_id: `deanon_260716_TRAIN/6Ob146_18s_3`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der RheinLebensmittel Systeme GmbH, FN FN982022c, wegen § 10 Abs 2 FBG, über den Revisionsrekurs des Österreichischen Verbandes Gemeinnütziger Bauvereinigungen Revisionsverband, 1010 Wien, Bösendorferstraße 7, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 3. September 2020, GZ 6 R 158/20d-6, womit der Rekurs gegen den Beschluss des Handelsgerichts Wien vom 20. Juli 2020, GZ 72 Fr 3266/20f-3, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `KWR Karasek Wietrzyk Rechtsanwälte GmbH` | `KWR Karasek Wietrzyk Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `RheinLebensmittel Systeme GmbH` (organisation)
- `FN982022c` (business_register_number)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/7Ob54_20x`) (sent_id: `deanon_260716_TRAIN/7Ob54_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Techn R Ramona Rössler, vertreten durch Mag. Astrid Roblyek, Rechtsanwältin in Klagenfurt am Wörthersee, gegen die beklagte Partei ZED Planung AG Haberditzlgasse 29, 9341 Kreuth, Österreich, vertreten durch Jarolim Partner Rechtsanwälte GmbH in Wien, wegen 7.339,70 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 31. Oktober 2019, GZ 4 R 325/19i-15, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 15. Juli 2019, GZ 15 C 998/18y-11, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Jarolim Partner Rechtsanwälte GmbH` | `Jarolim Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Techn R Ramona Rössler` (person)
- `Mag. Astrid Roblyek` (person)
- `ZED Planung AG` (organisation)
- `Haberditzlgasse 29, 9341 Kreuth, Österreich` (address)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_6`)


Renzlhausen 24, 6553 See, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dorda Brugger Jordis Rechtsanwälte GmbH` | `Dorda Brugger Jordis Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Handelsgerichts Wien` (organisation)
- `Bezirksgerichts für Handelssachen Wien` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/9Ob10_19i`) (sent_id: `deanon_260716_TRAIN/9Ob10_19i_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Oneseit Garten GmbH, Stephanieweg 12, 4901 Hub, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, gegen die beklagte Partei Brucknor-Planung GmbH, Tadtner Weg 4, 5133 Dick, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, wegen 6.265 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 29. November 2018, GZ 53 R 212/18k-19, mit dem der Berufung der klagenden Partei gegen das Urteil des Bezirksgerichts Salzburg vom 25. Juni 2018, GZ 17 C 965/17a-15, Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vavrovsky Heine Marth Rechtsanwälte GmbH` | `Vavrovsky Heine Marth Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Oneseit Garten GmbH` (organisation)
- `Stephanieweg 12, 4901 Hub, Österreich` (address)
- `Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte` (organisation)
- `Brucknor-Planung GmbH` (organisation)
- `Tadtner Weg 4, 5133 Dick, Österreich` (address)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/9Ob41_14s`) (sent_id: `deanon_260716_TRAIN/9Ob41_14s_4`)


OStR OMedR Gabriel Mittermiller, vertreten durch Mag. Petra Trauntschnig, Rechtsanwältin in Wien, gegen die beklagte Partei Allar Recycling GmbH, Eduardgasse 9, 5360 Rußbach, Österreich, vertreten durch Köhler Draskovits Unger Rechtsanwälte GmbH in Wien, wegen Wiederherstellung (Streitwert: 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. April 2014, GZ 15 R 35/14y-22, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Draskovits Unger Rechtsanwälte GmbH` | `Draskovits Unger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `OStR OMedR Gabriel Mittermiller` (person)
- `Mag. Petra Trauntschnig` (person)
- `Allar Recycling GmbH` (organisation)
- `Eduardgasse 9, 5360 Rußbach, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, Dr. Thunhart und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Lieselotte Mebesius, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Ahrenhold Druck AG, Brunnbichlweg 19, 3261 Figelsberg, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 22.140,32 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Juni 2019, GZ 2 R 92/19s-21, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Linz vom 12. April 2019, GZ 45 Cg 33/18v-17, nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch I. Das mit Beschluss vom 15. April 2020, AZ 9 Ob 61/19i, bis zur Entscheidung des Gerichtshofs der Europäischen Union über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Thunhart` (person)
- `MMag. Sloboda` (person)
- `Lieselotte Mebesius` (person)
- `Poduschka Partner Anwaltsgesellschaft mbH` (organisation)
- `Ahrenhold Druck AG` (organisation)
- `Brunnbichlweg 19, 3261 Figelsberg, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)
- `Obersten Gerichtshof` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, MMag. Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Niels Doerfel, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Gudrun Kovalschuk Gesellschaft m.b.H. (FN FN119735f ), FN297530m, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `MMag. Sloboda` (person)
- `Dr. Annerl` (person)
- `Niels Doerfel` (person)
- `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG` (organisation)
- `Gudrun Kovalschuk` (person)
- `FN119735f` (business_register_number)
- `FN297530m` (business_register_number)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/9Ob6_24h`) (sent_id: `deanon_260716_TRAIN/9Ob6_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Stiefsohn in der Rechtssache der klagenden Partei Jennifer Franckh, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Fürstentum Liechtenstein, gegen die beklagte Partei DrauGarten AG, Wamprechtsham 54, 4926 Untereselbach, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 2.375 EUR und Feststellung (Streitwert: 4.000 EUR), über die Revision der beklagten Partei gegen das Zwischenurteil des Landesgerichts Wels als Berufungsgericht vom 25. Oktober 2023, GZ 22 R 198/23h-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Vöcklabruck vom 15. Juni 2023, GZ 13 C 630/22f-26, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I.Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stiefsohn` (person)
- `Jennifer Franckh` (person)
- `Dr. Alexander Amann LL.M.` (person)
- `DrauGarten AG` (organisation)
- `Wamprechtsham 54, 4926 Untereselbach, Österreich` (address)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Vöcklabruck` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/9ObA150_21f`) (sent_id: `deanon_260716_TRAIN/9ObA150_21f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, den Hofrat Mag. Ziegelbauer und die Hofrätin Mag. Korn als weitere Richter (Senat gemäß § 11a ASGG) in der Arbeitsrechtssache der klagenden Partei Priv.-Doz. Peter Dannheisser, vertreten durch Mag. German Storch, Mag. Rainer Storch, Rechtsanwälte in Linz, gegen die beklagte Partei QZTV Versand gmbh in Liquidation, St. Sebastiani-Straße 35, 9972 Virgen, Österreich, vertreten durch Herbst Kinsky Rechtsanwälte GmbH in Wien, wegen 322,06 EUR brutto sA, über die Kostenbestimmungsanträge der klagenden und der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Kostenbestimmungsantrag wird dem Erstgericht zur Entscheidung übermittelt.  Text Begründung: [1]

| Predicted | Gold |
|---|---|
| `Herbst Kinsky Rechtsanwälte GmbH` | `Herbst Kinsky Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Korn` (person)
- `Priv.-Doz. Peter Dannheisser` (person)
- `Mag. German Storch` (person)
- `Mag. Rainer Storch` (person)
- `QZTV Versand gmbh` (organisation)
- `St. Sebastiani-Straße 35, 9972 Virgen, Österreich` (address)

**Example 33** (doc_id: `deanon_260716_TRAIN/9ObA30_23m`) (sent_id: `deanon_260716_TRAIN/9ObA30_23m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Robert Hauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Immanuel Möllerke, vertreten durch bfp Brandstetter Feigl Pfleger Rechtsanwälte GmbH in Amstetten, gegen die beklagte Partei Land Mathilda Coulais, vertreten durch Mag. Thomas Reisch, Rechtsanwalt in Wien, wegen 13.868,98 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2023, GZ 7 Ra 69/22a-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Brandstetter Feigl Pfleger Rechtsanwälte GmbH` | `Brandstetter Feigl Pfleger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Hargassner` (person)
- `Mag. Thomas Stegmüller` (person)
- `Immanuel Möllerke` (person)
- `Mathilda Coulais` (person)
- `Mag. Thomas Reisch` (person)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_5`)


Zlatan Schempf, alle vertreten durch die Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH, Wien, wegen Feststellung und Räumung, über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2020, GZ 2 R 122/20d-54, mit dem das Urteil des Landesgerichts Wels vom 27. Juli 2020, GZ 2 Cg 84/18g-47, in der Hauptsache bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Proksch Manak Kraft Rechtsanwälte GmbH` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zlatan Schempf`(person)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Watschinger Zimmermann Rechtsanwälte GmbH` — partial — pred is substring of gold: `Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH`

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

**Example 2** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_5`)


Sanitär Norfurtwerk AG, Piburger Straße 20, 4204 Hadersdorf, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sanitär Norfurtwerk AG`(organisation)
- `Piburger Straße 20, 4204 Hadersdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Savitski&Flashar Möbel GmbH, Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei Fryc+Brotzler Energie Rechtsanwälte GmbH, Lange Gasse 15, 4891 Plain, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brotzler Energie Rechtsanwälte GmbH` — partial — pred is substring of gold: `Fryc+Brotzler Energie Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Savitski&Flashar Möbel GmbH`(organisation)
- `Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich`(address)
- `Dr. Manfred Sommerbauer`(person)
- `DDr. Michael Dohr, LL.M.`(person)
- `Fryc+Brotzler Energie Rechtsanwälte GmbH`(organisation)
- `Lange Gasse 15, 4891 Plain, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Tiffany Jähncke, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei Sudconbach-Bau AG, Hart, Akazienstraße 15v, 4064 Oftering, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 5** (doc_id: `deanon_260716_TRAIN/6Ob47_25t`) (sent_id: `deanon_260716_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Kimberly Schnellhardt, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Digital Trasudwerk AG, Galles 5, 8453 Kitzelsdorf, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 6** (doc_id: `deanon_260716_TRAIN/7Ob259_10d`) (sent_id: `deanon_260716_TRAIN/7Ob259_10d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Huber als Vorsitzende und durch die Hofräte Dr. Hoch, Dr. Kalivoda, Dr. Roch und Mag. Dr. Wurdinger als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Maule Digital Rechtsanwälte GmbH, Zur Fischwasserung 33, 4090 Stadl, Österreich, gegen die beklagte und widerklagende Partei Mag. Wolfgang Kojima, vertreten durch GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG in Linz, wegen 63.833,25 EUR sA (Klage) und 15.000 EUR sA (Widerklage), über die außerordentliche Revision der beklagten und widerklagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2010, GZ 15 R 64/10g-89, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Maule Digital Rechtsanwälte GmbH` — partial — gold is substring of pred: `Maule Digital Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Dr. Roch`(person)
- `Mag. Dr. Wurdinger`(person)
- `Maule Digital Rechtsanwälte GmbH`(organisation)
- `Zur Fischwasserung 33, 4090 Stadl, Österreich`(address)
- `Mag. Wolfgang Kojima`(person)
- `GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 8** (doc_id: `deanon_260716_TRAIN/8ObA71_14w`) (sent_id: `deanon_260716_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Cynthia Schamel, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Werkglanz-Verlag AG, Blattbühel 46, 9073 Klagenfurt, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 9** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Petra Tschurtschenthaler, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Uthe Getränke AG, Triester Bundesstraße 146, 3452 Trasdorf, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Johannes Püller`(person)
- `Mag. Michael Puhm`(person)
- `Petra Tschurtschenthaler`(person)
- `Dr. Markus Orgler`(person)
- `Uthe Getränke AG`(organisation)
- `Triester Bundesstraße 146, 3452 Trasdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

</details>

---

## `LawFirmOG` 🏆

**F1:** 0.010 | **Precision:** 0.769 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `b4ff7851`  
**Description:**
Matches law firm names ending in 'Rechtsanwälte OG' or 'Rechtsanwälte-Partnerschaft', requiring at least two capitalized name parts.

**Content:**
```
\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+\s+Rechtsanw\u00e4lte\s+(?:OG|Partnerschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.769 | 0.005 | 0.010 | 26 | 20 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 6 | 3975 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Huber Berchtold Rechtsanwälte OG` | `Huber Berchtold Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Landesgericht Linz` (organisation)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Linz` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Radel Stampf Supper Rechtsanwälte OG` | `Radel Stampf Supper Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Enns-Umwelt` (organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich` (address)
- `Ing. Lara Markart` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Krist Bubits Rechtsanwälte OG` | `Krist Bubits Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Othmar Mertl` (person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG` (organisation)
- `Malik Fridt` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mahringer Steinwender Bestebner Rechtsanwälte OG` | `Mahringer Steinwender Bestebner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Gabriele Griehsel` (person)
- `Dr. Wolfgang Kozak` (person)
- `Roland Soukup` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Urbanek Lind Schmied Reisch Rechtsanwälte OG` | `Urbanek Lind Schmied Reisch Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Florenzia Münsterer` (person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH` (organisation)
- `MittelEnergie Werke Bank` (organisation)
- `Altlassing 110, 4183 Ahorn, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob192_11h`) (sent_id: `deanon_260716_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hierle Sanitär Limited, London, Zirkinger Straße 3, 8082 Glatzau, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG` | `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Hierle Sanitär Limited` (organisation)
- `Zirkinger Straße 3, 8082 Glatzau, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache klagenden Partei Rainer Baetzel, vertreten durch Dr. Harald Hauer, Rechtsanwalt in Wien, gegen die beklagte Partei Rimscha Versand GmbH in Liquidation, Götzau 193, 5452 Grub, Österreich, vertreten durch die Petsch Frosch Klein Arturo Rechtsanwälte OG, Wien, wegen 38.236,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Oktober 2020, GZ 3 R 51/20x-50, mit dem das Urteil des Handelsgerichts Wien vom 24. Juli 2020, GZ 34 Cg 51/18h-45, bestätigt wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Petsch Frosch Klein Arturo Rechtsanwälte OG` | `Petsch Frosch Klein Arturo Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Rainer Baetzel` (person)
- `Dr. Harald Hauer` (person)
- `Rimscha Versand GmbH` (organisation)
- `Götzau 193, 5452 Grub, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob95_21h`) (sent_id: `deanon_260716_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Gawelzyk Pflege GmbH, Am See IX 247, 6320 Achleit, Österreich, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Loos und Woiciech Analyse GmbH, Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Zumtobel Kronberger Rechtsanwälte OG` | `Zumtobel Kronberger Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Gawelzyk Pflege GmbH` (organisation)
- `Am See IX 247, 6320 Achleit, Österreich` (address)
- `Loos und Woiciech Analyse GmbH` (organisation)
- `Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Ried im Innkreis` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Schwarzig Medien Aktiengesellschaft, Balthasar-Waltl-Weg 227, 3921 Kehrbach, Österreich, vertreten durch die Kunz Schima Wallentin Rechtsanwälte OG in Wien, und der Nebenintervenientinnen auf Seiten der klagenden Partei 1.

| Predicted | Gold |
|---|---|
| `Kunz Schima Wallentin Rechtsanwälte OG` | `Kunz Schima Wallentin Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Baumann` (person)
- `Dr. Veith` (person)
- `Dr. E. Solé` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Nowotny` (person)
- `Schwarzig Medien Aktiengesellschaft` (organisation)
- `Balthasar-Waltl-Weg 227, 3921 Kehrbach, Österreich` (address)

**Example 9** (doc_id: `deanon_260716_TRAIN/3Ob137_17v`) (sent_id: `deanon_260716_TRAIN/3Ob137_17v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Pflegschaftssache der Minderjährigen 1. StR Corvin Lengenfelder, geboren am 16. September 2007, 2. Alva Dielschneider, geboren am 28. April 2009, beide wohnhaft beim Vater Mag. Gottfried Clef, dieser vertreten durch Dr. Johann Etienne Korab, Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs der Mutter Mag. Alma Plohn, vertreten durch Hornek Hubacek Lichtenstrasser Rechtsanwälte OG in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Mai 2017, GZ 48 R 101/17b-137, womit Punkt 1. und 2. des Beschlusses des Bezirksgerichts Döbling vom 9. Jänner 2017, GZ 1 Ps 119/13b-90, bestätigt wurde, den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Hornek Hubacek Lichtenstrasser Rechtsanwälte OG` | `Hornek Hubacek Lichtenstrasser Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Roch` (person)
- `Dr. Kodek` (person)
- `StR Corvin Lengenfelder` (person)
- `16. September` (date)
- `Alva Dielschneider` (person)
- `28. April` (date)
- `Mag. Gottfried Clef` (person)
- `Dr. Johann Etienne Korab` (person)
- `Mag. Alma Plohn` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/3Ob166_25w`) (sent_id: `deanon_260716_TRAIN/3Ob166_25w_4`)


Eduard Mauderer, vertreten durch Mag. Sarah Abel, Rechtsanwältin in Salzburg, und 2. Schmiede Digital GmbH, Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich, vertreten durch die Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, wegen 7.164,36 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 10. Juli 2025, GZ 53 R 145/25t-18, mit dem das Teilurteil des Bezirksgerichts Salzburg vom 12. März 2025, GZ 31 C 1179/24h-12, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mahringer Steinwender Bestebner Rechtsanwälte OG` | `Mahringer Steinwender Bestebner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Eduard Mauderer` (person)
- `Mag. Sarah Abel` (person)
- `Schmiede Digital GmbH` (organisation)
- `Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich` (address)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/5Ob30_11i`) (sent_id: `deanon_260716_TRAIN/5Ob30_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätinnen Dr. Hurch und Dr. Lovrek sowie die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der wohnrechtlichen Außerstreitsache der Antragstellerin Edith Ilse Semyonov, vertreten durch Maraszto Milisits Rechtsanwälte OG in Wien, gegen den Antragsgegner DDr. Ernest Bayraktar, vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, wegen §§ 6 Abs 2, 37 Abs 1 Z 2 MRG, über den Revisionsrekurs des Antragsgegners gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. Oktober 2010, GZ 39 R 248/10z-60, mit dem infolge Rekurses des Antragsgegners der Sachbeschluss des Bezirksgerichts Döbling vom 27. April 2010, GZ 15 Msch 10/07p-51, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Maraszto Milisits Rechtsanwälte OG` | `Maraszto Milisits Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Danzl` (person)
- `Dr. Hurch` (person)
- `Dr. Lovrek` (person)
- `Dr. Höllwerth` (person)
- `Mag. Wurzer` (person)
- `Edith Ilse Semyonov` (person)
- `DDr. Ernest Bayraktar` (person)
- `Dr. Erich Kafka` (person)
- `Dr. Manfred Palkovits` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/7Ob110_13x`) (sent_id: `deanon_260716_TRAIN/7Ob110_13x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Gerdelbracht Telekom AG, KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, gegen die beklagte Partei Mag. (FH) Franz Burgschmidt, vertreten durch Binder Grösswang Rechtsanwälte OG in Wien, wegen Erteilung von Auskünften, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. April 2013, GZ 11 R 75/13z-12, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kunz Schima Wallentin Rechtsanwälte OG` | `Kunz Schima Wallentin Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Malesich` (person)
- `Gerdelbracht Telekom AG` (organisation)
- `KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich` (address)
- `Mag. (FH) Franz Burgschmidt` (person)
- `Binder Grösswang Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/7Ob165_18t`) (sent_id: `deanon_260716_TRAIN/7Ob165_18t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Pflegschaftssache der mj Jean Mak, geboren am 6. August 2012, vertreten durch ihre Mutter Liliana Oberlach, diese vertreten durch Maus Riedherr Rechtsanwälte OG in Salzburg, wegen Unterhalts, über den Revisionsrekurs des Vaters Mag. Ing. Bodo Caspersen, vertreten durch Sattlegger, Dorninger, Steiner & Partner, Rechtsanwälte in Linz, gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 11. Juli 2018, GZ 21 R 134/18d-77, mit dem der Beschluss des Bezirksgerichts Salzburg vom 20. April 2016, GZ 4 Pu 110/15x-43, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Maus Riedherr Rechtsanwälte OG` | `Maus Riedherr Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. E. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Jean Mak` (person)
- `6. August` (date)
- `Liliana Oberlach` (person)
- `Mag. Ing. Bodo Caspersen` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätin und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, MMag. Matzka und Dr. Weber als weitere Richter in der Rechtssache der klagenden Partei Dr. Shirley Steidten, vertreten durch Koch Jilek Rechtsanwälte Partnerschaft in Bruck an der Mur, gegen die beklagte Partei WienMonlemalTextil Aktiengesellschaft, Ernst Wolf-Gasse 216, 4650 Schußstatt, Österreich, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 15. Juli 2021, GZ 4 R 53/21b-25, womit das Urteil des Landesgerichts Leoben vom 16. Dezember 2020, GZ 5 Cg 57/19z-19, bestätigt wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Koch Jilek Rechtsanwälte Partnerschaft` | `Koch Jilek Rechtsanwälte Partnerschaft` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Dr. Weber` (person)
- `Dr. Shirley Steidten` (person)
- `WienMonlemalTextil Aktiengesellschaft` (organisation)
- `Ernst Wolf-Gasse 216, 4650 Schußstatt, Österreich` (address)
- `Dr. Andreas A. Lintl` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Leoben` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/7Ob259_10d`) (sent_id: `deanon_260716_TRAIN/7Ob259_10d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Huber als Vorsitzende und durch die Hofräte Dr. Hoch, Dr. Kalivoda, Dr. Roch und Mag. Dr. Wurdinger als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Maule Digital Rechtsanwälte GmbH, Zur Fischwasserung 33, 4090 Stadl, Österreich, gegen die beklagte und widerklagende Partei Mag. Wolfgang Kojima, vertreten durch GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG in Linz, wegen 63.833,25 EUR sA (Klage) und 15.000 EUR sA (Widerklage), über die außerordentliche Revision der beklagten und widerklagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2010, GZ 15 R 64/10g-89, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG` | `GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Dr. Roch` (person)
- `Mag. Dr. Wurdinger` (person)
- `Maule Digital Rechtsanwälte GmbH` (organisation)
- `Zur Fischwasserung 33, 4090 Stadl, Österreich` (address)
- `Mag. Wolfgang Kojima` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_4`)


Isabel Nestle AG, Reinsbach 186, 9131 Dolina, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2.

| Predicted | Gold |
|---|---|
| `Jank Weiler Operenyi Rechtsanwälte OG` | `Jank Weiler Operenyi Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Isabel Nestle` (person)
- `Reinsbach 186, 9131 Dolina, Österreich` (address)

**Example 17** (doc_id: `deanon_260716_TRAIN/8ObA74_22y`) (sent_id: `deanon_260716_TRAIN/8ObA74_22y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter und die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Robert Brunner (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Sibylle Singl, vertreten durch Mag. Christian Marchhart, Rechtsanwalt in St. Pölten, dieser vertreten durch die Urbanek Lind Schmied Reisch Rechtsanwälte OG in St. Pölten, gegen die beklagten Parteien 1. Yussuf Waszek, und 2. Nikolai Terlinden, beide vertreten durch Mag. Agnes Lepschy, Rechtsanwältin in Altlengbach, wegen 86.509,66 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Juli 2022, GZ 7 Ra 66/22k-63, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Urbanek Lind Schmied Reisch Rechtsanwälte OG` | `Urbanek Lind Schmied Reisch Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Stefula` (person)
- `Dr. Ingomar Stupar` (person)
- `Mag. Robert Brunner` (person)
- `Sibylle Singl` (person)
- `Mag. Christian Marchhart` (person)
- `Yussuf Waszek` (person)
- `Nikolai Terlinden` (person)
- `Mag. Agnes Lepschy` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/9Ob3_20m`) (sent_id: `deanon_260716_TRAIN/9Ob3_20m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Fichtenau, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Larissa Kleinicke, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber, Rechtsanwälte in Salzburg, gegen die beklagte Partei Ralph Heimersheim, vertreten durch Fahrner Unterrainer Rechtsanwälte OG in Zell am See, wegen Wiederaufnahme des Verfahrens AZ 17 C 29/13w des Bezirksgerichts Zell am See (wegen 11.658,48 EUR sA und Feststellung), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. April 2019, GZ 53 R 71/19a-9, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Fahrner Unterrainer Rechtsanwälte OG` | `Fahrner Unterrainer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Larissa Kleinicke` (person)
- `Dr. Harald Schwendinger` (person)
- `Dr. Brigitte Piber` (person)
- `Ralph Heimersheim` (person)
- `Bezirksgerichts Zell am See` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/9Ob49_19z`) (sent_id: `deanon_260716_TRAIN/9Ob49_19z_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Traude Fahner, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber, Rechtsanwälte in Salzburg, gegen die beklagte Partei Stella Vaßmers, vertreten durch Fahrner Unterrainer Rechtsanwälte OG in Zell am See, wegen Wiederaufnahme des Verfahrens AZ 17 C 29/13w des Bezirksgerichts Zell am See (wegen 11.658,48 EUR sA und Feststellung), über den Rekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 13. Juni 2019, GZ 53 R 71/19a-12, mit dem der Antrag auf Abänderung des Unzulässigkeitsausspruchs gemäß § 508 Abs 1 ZPO zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fahrner Unterrainer Rechtsanwälte OG` | `Fahrner Unterrainer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Traude Fahner` (person)
- `Dr. Harald Schwendinger` (person)
- `Dr. Brigitte Piber` (person)
- `Stella Vaßmers` (person)
- `Bezirksgerichts Zell am See` (organisation)
- `Landesgerichts Salzburg` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob128_17f`) (sent_id: `deanon_260716_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Josefine Rehn, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Susanne Lürkens, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Mag. Josefine Rehn`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Susanne Lürkens`(person)
- `Mag. Anna-Maria Freiberger`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Liesing`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Aloisa Moosleitner, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Catharina Uppenbrink, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Wurzer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Kodek`(person)
- `Aloisa Moosleitner`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Catharina Uppenbrink`(person)
- `Dr. Alexander Haas`(person)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Fürstenfeld`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/3Ob222_17v`) (sent_id: `deanon_260716_TRAIN/3Ob222_17v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Jensik und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Familienrechtssache des Antragstellers Janosch von Reichel, vertreten durch Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, gegen den Antragsgegner Vincent Niederführ, vertreten durch Dr. Heinz-Peter Wachter, Rechtsanwalt in Wien, wegen Unterhaltsherabsetzung, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2017, GZ 45 R 267/17y-81, womit der Beschluss des Bezirksgerichts Fünfhaus vom 12. April 2017, GZ 3 Fam 9/15b-72, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Jensik`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Janosch von Reichel`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Vincent Niederführ`(person)
- `Dr. Heinz-Peter Wachter`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Fünfhaus`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/6Ob169_12i`) (sent_id: `deanon_260716_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Seesteincon-Transport GmbH, Wildbacher Straße 174, 3623 Bernhards, Österreich, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Heimnor GmbH, Am Johannisgraben 44, 8200 Albersdorf, Österreich, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Severin Perschl Rechtsanwälte OG` — partial — pred is substring of gold: `Mag. Severin Perschl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Pimmer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Seesteincon-Transport GmbH`(organisation)
- `Wildbacher Straße 174, 3623 Bernhards, Österreich`(address)
- `List Rechtsanwälte GmbH`(organisation)
- `Heimnor GmbH`(organisation)
- `Am Johannisgraben 44, 8200 Albersdorf, Österreich`(address)
- `Dr. Christoph Brenner`(person)
- `Mag. Severin Perschl Rechtsanwälte OG`(organisation)
- `Landesgerichts Korneuburg`(organisation)
- `Bezirksgerichts Gänserndorf`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/7Ob180_16w`) (sent_id: `deanon_260716_TRAIN/7Ob180_16w_4`)


Dr. Anabel Heimboeckel, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dominik Westerberger, vertreten durch Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, wegen Ehescheidung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juni 2016, GZ 42 R 130/16b-33, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Dezember 2015, GZ 3 C 9/14w-27, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anabel Heimboeckel`(person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `Dominik Westerberger`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/7Ob80_18t`) (sent_id: `deanon_260716_TRAIN/7Ob80_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden und widerbeklagten Partei Martha Masius, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, gegen die beklagte und widerklagende Partei Evelyn Möckel, vertreten durch Mag. Petra Laback, Rechtsanwältin in Wien, wegen Ehescheidung, über die außerordentlichen Revisionen beider Parteien gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. Februar 2018, GZ 42 R 417/17k-57, den Beschluss gefasst:  Spruch Die außerordentlichen Revisionen beider Parteien werden gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Martha Masius`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Evelyn Möckel`(person)
- `Mag. Petra Laback`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

</details>

---

## `BezirksGericht` 🏆

**F1:** 0.106 | **Precision:** 0.757 | **Recall:** 0.057  

**Format:** `regex`  
**Rule ID:** `1d05c994`  
**Description:**
Matches 'Bezirksgericht' and its genitive form with location suffixes, explicitly including hyphenated names like 'Graz-West' and 'Graz-Ost'.

**Content:**
```
\bBezirksgericht(?:s)?\s+(?:[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?(?:\s+-\s+[A-Z][a-zA-Z]+)?|Graz-Ost|Graz-West|Hernals|D\u00f6bling|Favoriten|Ferlach|Korneuburg|Chisinau|Innere\s+Stadt\s+Wien|Salzburg|Bregenz|Hall\s+in\s+Tirol|Kitzb\u00fchel|Wels|St\.\sP\u00f6lten|Eisenstadt|Klagenfurt|Linz|Graz|Wien|Steyr|Feldkirch|Krems\s+an\s+der\s+Donau|Wiener\s+Neustadt|Zell\s+am\s+See|Bruck\s+an\s+der\s+Mur|Innere\s+Stadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.757 | 0.057 | 0.106 | 301 | 228 | 73 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 228 | 73 | 3785 |

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

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_9`)


Zudem befinde sich das in Rede stehende Fahrzeug im Sprengel des Bezirksgerichts Dornbirn.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_27`)


dieser könnte auch aus dem Sprengel des Bezirksgerichts Dornbirn oder dessen näherer Umgebung gewählt werden, was die Anreisekosten für eine Befundaufnahme jedenfalls reduzieren würde.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Judenburg` | `Bezirksgericht Judenburg` |
| `Bezirksgerichts Judenburg` | `Bezirksgerichts Judenburg` |

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

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Feldkirchen` | `Bezirksgerichts Feldkirchen` |
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

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Feldkirchen` | `Bezirksgericht Feldkirchen` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


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

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_7`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Kreutzerstraße 7, 4851 Haunolding, Österreich aufhalte (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Bezirksgericht Vöcklabruck` (organisation)
- `Kreutzerstraße 7, 4851 Haunolding, Österreich` (address)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_9`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_13`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_15`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_17`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_18`)


1. 2021 bzw mit Beschluss vom 29. 1. 2021 ab, weil § 111 JN auf Verfahren in Abstammungssachen keine Anwendung finde und die Minderjährige im Zeitpunkt der Antragstellung ihren gewöhnlichen Aufenthalt nicht im Sprengel des Bezirksgerichts Josefstadt gehabt habe (ON 28).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_20`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_5`)


Das von der Klägerin mit ihrer Klage angerufene Bezirksgericht Schwechat hat die internationale und örtliche Zuständigkeit rechtskräftig verneint (RIS-Justiz RS0046450).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_11`)


Unter Berücksichtigung dieser Vorgaben erscheint eine Zuweisung der Sache an das Bezirksgericht Schwechat als zweckmäßig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


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

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_7`)


Das vom Kläger angerufene Bezirksgericht Schwechat sprach rechtskräftig seine (internationale) Unzuständigkeit aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_14`)


An die rechtskräftige Verneinung der internationalen Zuständigkeit des vom Kläger angerufenen Bezirksgerichts Schwechat ist der Oberste Gerichtshof gebunden (RIS-Justiz RS0046568).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Schwechat` | `Bezirksgerichts Schwechat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_38`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel und wurde zum anderen die Klage bereits bei diesem Gericht behandelt (6 Nc 31/20s mwN ua).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kitzbühel` | `Bezirksgerichts Kitzbühel` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Karin Ciliberto` (person)
- `Mag. Maximilian Kocher` (person)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_4`)


Anstelle des Bezirksgerichts Kitzbühel wird das Bezirksgericht Mödling als zur Führung des Verlassenschaftsverfahrens zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kitzbühel` | `Bezirksgerichts Kitzbühel` |

**Missed by this rule (FN):**

- `Bezirksgericht Mödling` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_5`)


B e g r ü n d u n g :  Rechtliche Beurteilung Der am 9. September 2009 verstorbene Erblasser hatte seinen Wohnsitz im Sprengel des Bezirksgerichts Kitzbühel.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kitzbühel` | `Bezirksgerichts Kitzbühel` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Rattenberg` | `Bezirksgerichts Rattenberg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Favoriten` | `Bezirksgerichts Favoriten` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Donaustadt` | `Bezirksgerichts Donaustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Klagenfurt` | `Bezirksgerichts Klagenfurt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Grieskirchen` | `Bezirksgerichts Grieskirchen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Wels` | `Bezirksgerichts Wels` |

**Missed by this rule (FN):**

- `Anita Schetzel` (person)
- `Landesgerichts Wels` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Zwettl` | `Bezirksgerichts Zwettl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Favoriten` | `Bezirksgerichts Favoriten` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Döbling` | `Bezirksgerichts Döbling` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Mag. Florian Kucera` (person)
- `Mag. Timon Schönswetter` (person)
- `Doschek Rechtsanwalts GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Wiener Neustadt` | `Bezirksgerichts Wiener Neustadt` |

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
- `Pieler & Pieler & Partner KG` (organisation)
- `Dr. Madeleine Musialik` (person)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Feldkirch` | `Bezirksgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Schwechat` | `Bezirksgerichts Schwechat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Karsten Alberter` (person)
- `2. April 2010` (date)
- `Helmut Dreilich` (person)
- `Landesgerichts Korneuburg` (organisation)
- `Lena Amini` (person)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Melk` | `Bezirksgerichts Melk` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Maja Dolleschell` (person)
- `14. August` (date)
- `Bezirkshauptmannschaft Melk` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Seekirchen` | `Bezirksgerichts Seekirchen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Donaustadt` | `Bezirksgerichts Donaustadt` |
| `Bezirksgerichts Donaustadt` | `Bezirksgerichts Donaustadt` |

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
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_7`)


Mit Beschluss des Bezirksgerichts Josefstadt vom 28. 4. 2004, GZ 16 P 99/00g-363, war der Antragsgegner zur Zahlung eines Unterhalts ab 1. 8. 2004 bis auf weiteres, längstens jedoch bis zur Selbsterhaltungsfähigkeit der Antragstellerin in Höhe von monatlich 250 EUR verpflichtet worden.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_8`)


Am 20. 9. 2016 beantragte die Antragstellerin beim Bezirksgericht Josefstadt die Erhöhung der monatlichen Unterhaltszahlung auf 440 EUR ab 1. 9. 2016.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_9`)


Im Rahmen seiner Äußerung zu diesem Unterhaltserhöhungsantrag lehnte der Antragsgegner jeweils alle Richter des Bezirksgerichts Josefstadt und des diesem übergeordneten Landesgerichts für Zivilrechtssachen Wien ab.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Missed by this rule (FN):**

- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Feldkirch` | `Bezirksgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Dr. Weber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Agatha von der Heide` (person)
- `MMag. Dr. Sebastian Pribas` (person)
- `Mag. Benedikt Walch` (person)
- `Alva Sengül` (person)
- `Selina Birkmeir` (person)
- `Harald Ladwig, LLM` (person)
- `In der Klaus 72, 4785 Bach, Österreich` (address)
- `Mag. German Bertsch` (person)
- `Landesgerichts Feldkirch` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Mann` (person)
- `Dr. Brenner` (person)
- `Mag. Rögner` (person)
- `Nenad Pschor` (person)
- `Mag. Schneider, LL.M.` (person)

**Example 54** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__4`)


Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt verletzen 1./ die Durchführung der Hauptverhandlung und Urteilsfällung am 26. September 2018 in Abwesenheit des Angeklagten § 427 Abs 1 StPO, 2./ die Verlesung des die Vernehmung des Zeugen Alexander Struttmann beinhaltenden Teils des Hauptverhandlungsprotokolls vom 28. Februar 2018 (ON 9) in der Hauptverhandlung am 26. September 2018 § 252 Abs 1 StPO iVm § 447 StPO, 3./ der unter einem mit dem Urteil vom 26. September 2018 (ON 25) gefasste Beschluss auf Widerruf der Nenad Pohlmann mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht § 494a Abs 3 StPO und 4./ das Urteil vom 26. September 2018 (ON 25) § 31 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

**Missed by this rule (FN):**

- `Alexander Struttmann` (person)
- `Nenad Pohlmann` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 56** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__6`)


Text Gründe: Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt legte die Staatsanwaltschaft Wien Nenad Pielstick mit Strafantrag vom 28. November 2017 (ON 4) ein am 3. Februar 2017 in Langauweg 3, 3203 Röhrenbach, Österreich gesetztes und als Vergehen der Veruntreuung nach § 133 Abs 1 StGB beurteiltes Verhalten zur Last.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

**Missed by this rule (FN):**

- `Nenad Pielstick` (person)
- `Langauweg 3, 3203 Röhrenbach, Österreich` (address)

**Example 57** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 58** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__19`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer gemäß § 23 StPO ergriffenen Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend aufzeigt, wurde im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt das Gesetz mehrfach verletzt: 1./

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

**Example 59** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Holzweber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Dr. Schwab` (person)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Gotsmy` (person)
- `Jennifer Janauscheck` (person)
- `Dr. Eisenmenger` (person)

**Example 60** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__4`)


Im Verfahren AZ 3 U 166/07x des Bezirksgerichts Kufstein verletzen das Gesetz 1. das Urteil vom 30. Jänner 2008 in seinem Strafausspruch in § 5 Z 5 JGG und § 31 Abs 1 zweiter Satz StGB;

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 61** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__5`)


2. der unter einem gefasste Beschluss gemäß § 494a Abs 1 Z 2 StPO auf Absehen vom Widerruf der zum AZ 3 U 350/06d des Bezirksgerichts Kufstein gewährten bedingten Strafnachsicht in §§ 494a Abs 1 und 495 Abs 2 StPO sowie § 55 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 62** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__6`)


Das Urteil, das im Übrigen unberührt bleibt, wird in seinem Strafausspruch aufgehoben und dem Bezirksgericht Kufstein im Umfang der Aufhebung die neuerliche Verhandlung und Entscheidung aufgetragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 63** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__7`)


Text Gründe: Die am 26. Jänner 1991 geborene Jennifer Johannwerner wurde mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, mehrerer Vergehen der Körperverletzung nach § 83 Abs 1 StGB und des Vergehens der Sachbeschädigung nach § 125 StGB schuldig erkannt und hiefür unter Anwendung des § 5 Z 4 JGG zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von zwei Monaten verurteilt (Blg ./2 zum Bezugsakt AZ 3 U 166/07x des Bezirksgerichts Kufstein).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Missed by this rule (FN):**

- `Jennifer Johannwerner` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__8`)


Mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, wurde die auch damals noch Jugendliche des am 28. Oktober 2006 begangenen Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB schuldig erkannt und hiefür unter Bedachtnahme gemäß „§§ 31 Abs 1 und 40“ StGB auf das Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, nach dem zweiten Strafsatz des § 91 Abs 2 StGB zu einer Zusatzgeldstrafe von 200 Tagessätzen, für den Fall der Uneinbringlichkeit zu 100 Tagen Ersatzfreiheitsstrafe verurteilt (das mit Beschluss ON 64 richtig gestellte Urteilsdatum wurde entgegen richterlicher Anordnung [S 306] am Rande der Urteilsurschrift ON 49 nicht beigesetzt).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 65** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__9`)


Unter einem erging der Beschluss, gemäß § 494a Abs 1 Z 2 StPO vom Widerruf der zum AZ 36 Hv 118/05p des Landesgerichts Innsbruck und zum AZ 3 U 350/06d des Bezirksgerichts Kufstein jeweils gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Missed by this rule (FN):**

- `Landesgerichts Innsbruck` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__12`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, stehen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008 in seinem Strafausspruch sowie der unter einem gefasste Beschluss gemäß § 494a Abs 1 Z 2 StPO mit dem Gesetz nicht im Einklang: Die Beschuldigte stand zum Tatzeitpunkt im 16.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 67** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__19`)


Die vorliegende Jugendstraftat vom 28. Oktober 2006 hätte bereits in dem früheren Verfahren AZ 3 U 350/06d des Bezirksgerichts Kufstein abgeurteilt werden können.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 68** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__22`)


Durch die Verhängung einer (Zusatz-)Geldstrafe von 200 Tagessätzen in Missachtung des durch § 5 Z 5 JGG geänderten Strafrahmens bei ersichtlicher Nichtanwendung des § 37 Abs 1 StGB und demzufolge auch der bei Zusatzstrafen anzuwendenden Strafbemessungsvorschrift des § 31 Abs 1 zweiter Satz StGB hat das Bezirksgericht Kufstein das Gesetz in den genannten Bestimmungen zum Nachteil der Verurteilten verletzt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 69** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__23`)


Der Oberste Gerichtshof sah sich daher gemäß § 292 letzter Satz StPO veranlasst, das Urteil im Strafausspruch aufzuheben und dem Bezirksgericht Kufstein in diesem Umfang die Verfahrenserneuerung aufzutragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Linz` | `Bezirksgerichts Linz` |
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

**Example 71** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_5`)


Das Bezirksgericht Linz überwies die Sache dem Bezirksgericht Innere Stadt Wien mit der Begründung örtlicher Unzuständigkeit (vgl ON 1 S 3: „erste Taten in Wien“).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_13`)


Aus dem hier zur Anwendung kommenden Anknüpfungstatbestand des § 36 Abs 3 erster Satz (iVm § 37 Abs 2 zweiter Satz) StPO folgt demnach die Zuständigkeit des Bezirksgerichts Linz.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Linz` | `Bezirksgerichts Linz` |

**Example 73** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Weiz` | `Bezirksgerichts Weiz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Korner` (person)
- `Wolfgang Weide` (person)
- `Dr. Ulrich` (person)

**Example 74** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_4`)


In der Strafsache AZ 10 U 13/17b des Bezirksgerichts Weiz verletzt der zugleich mit dem Urteil dieses Gerichts vom 25. Juli 2018 ergangene Beschluss auf Widerruf bedingter Strafnachsicht (ON 69) § 494a Abs 3 erster und zweiter Satz StPO.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Weiz` | `Bezirksgerichts Weiz` |

**Example 75** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_8`)


Mit rechtskräftigem Abwesenheitsurteil des Bezirksgerichts Weiz vom 25. Juli 2018, GZ 10 U 13/17b-69, wurde Wenholz einer (vom 9. Mai 2016 bis zum 7. September 2017 begangenen) strafbaren Handlung schuldig erkannt.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Weiz` | `Bezirksgerichts Weiz` |

**Missed by this rule (FN):**

- `Wenholz` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

**False Positives:**

- `Bezirksgerichts Graz` — partial — pred is substring of gold: `Bezirksgerichts Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Mag. Schober`(person)
- `Dr. Vollmaier`(person)
- `Jason Langeloh`(person)
- `Mag. Martin Rützler`(person)
- `Selma Einoeder`(person)
- `Mag. Alexander Gerngross`(person)
- `Mag. Klaus Köck`(person)
- `Bezirksgerichts Graz-Ost`(organisation)
- `Bezirksgericht Dornbirn`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bezirksgericht Innere Stadt` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

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

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

**False Positives:**

- `Bezirksgericht Innere Stadt` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Bezirksgerichts Graz` — partial — pred is substring of gold: `Bezirksgerichts Graz-West`
- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Nowotny`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`
- `Bezirksgericht Braunau` — partial — pred is substring of gold: `Bezirksgericht Braunau am Inn`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Bezirksgericht Braunau am Inn`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_16`)


Mit Urteil des Bezirksgerichts Bezirksgericht für Handelssachen Wien vom 21.

**False Positives:**

- `Bezirksgerichts Bezirksgericht` — positional overlap with gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_26`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Hall (in Tirol) verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Bezirksgericht Bezirksgericht Hall` — positional overlap with gold: `Bezirksgericht Hall (in Tirol)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hall (in Tirol)`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Basil Biewer anhängig.

**False Positives:**

- `Bezirksgericht Innere Stadt` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)
- `Basil Biewer`(person)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Bezirksgerichts St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

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

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_6`)


Mit einstweiliger Verfügung des Bezirksgerichts Innere Stadt Wien vom 28. April 2022 wurde der Vater verpflichtet, dem Kind einen vorläufigen monatlichen Unterhaltsbeitrag in Höhe von 38 EUR zu leisten (ON 2).

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

**False Positives:**

- `Bezirksgerichts Graz` — partial — pred is substring of gold: `Bezirksgerichts Graz-Ost`

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

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

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

**Example 15** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_10`)


Für ihn ist ein Sachwalter bestellt, der seit 2011 alle Angelegenheiten (§ 268 Abs 3 Z 3 ABGB) zu besorgen hat (siehe den Beschluss des Bezirksgericht Bezirksgericht Freistadt vom 15.

**False Positives:**

- `Bezirksgericht Bezirksgericht Freistadt` — partial — gold is substring of pred: `Bezirksgericht Freistadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Freistadt`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Bezirksgericht Leopoldstadt Nenad` — partial — gold is substring of pred: `Bezirksgericht Leopoldstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Leopoldstadt`(organisation)
- `Nenad Panagiotakopoulou`(person)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

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

**Example 18** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_5`)


Das Bezirksgericht Linz überwies die Sache dem Bezirksgericht Innere Stadt Wien mit der Begründung örtlicher Unzuständigkeit (vgl ON 1 S 3: „erste Taten in Wien“).

**False Positives:**

- `Bezirksgericht Innere Stadt` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Linz`(organisation)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_9`)


In diesem Fall kommt das Verfahren (soweit hier von Interesse) gemäß § 37 Abs 2 zweiter Satz StPO jenem Gericht zu, in dessen Zuständigkeit die frühere Straftat fällt. Zutreffend weist das Bezirksgericht Innere Stadt darauf hin, dass nach der Aktenlage kein Anhaltspunkt für einen Tatort in Wien besteht.

**False Positives:**

- `Bezirksgericht Innere Stadt` — partial — gold is substring of pred: `Bezirksgericht Innere`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`
- `Bezirksgerichts Innere Stadt` — similar text (different position): `Bezirksgerichts Innere Stadt Wien`

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

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__6`)


2. Der Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) verletzt §§ 270 Abs 3, 271 Abs 7 StPO iVm §§ 447, 458 zweiter Satz StPO.

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__7`)


Text Gründe: Mit Urteil des Bezirksgerichts Innere Stadt Wien (ON 19) wurde Robert Ulrici jeweils eines Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB schuldig erkannt und hiefür zu einer bedingt nachgesehenen Freiheitsstrafe verurteilt. Nach Verkündung des Urteils und erteilter Rechtsmittelbelehrung erklärte der – nicht durch einen Verteidiger vertretene (vgl § 57 Abs 2 dritter Satz StPO;Fabrizy, StPO13§ 57 Rz 10) – Angeklagte zunächst, auf Rechtsmittel zu verzichten (ON 18 S 5).

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Robert Ulrici`(person)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__10`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

**False Positives:**

- `Bezirksgericht Innere Stadt` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__13`)


Mit Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30) wurden sowohl das Protokoll über die Hauptverhandlung (ON 18) als auch die Urteilsurschrift (ON 19) in Ansehung des „Verhandlungsdatum[s]“ von „23. 11. 2018“ auf „27. 11. 2018“ berichtigt.

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__14`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrem Antrag auf außerordentliche Wiederaufnahme des Verfahrens zutreffend darlegt, bestehen gegen die Richtigkeit der dem Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), zugrunde gelegten Tatsache, das erstinstanzliche Urteil sei am 23. November 2018 verkündet worden, erhebliche Bedenken: Die Verfügung des Bezirksgerichts Innere Stadt Wien vom 1. November 2018 auf Ladung des Angeklagten zur Hauptverhandlung am 27. November 2018 (ON 1 [unjournalisiert] S 6), das auf der letzten Seite der Urteilsurschrift angeführte Urteilsdatum „27. November 2018“ (ON 19 S 5), die im Verfahrensakt enthaltene (unjournalisierte) Äußerung der Staatsanwaltschaft Wien vom 15. November 2019, AZ 126 BAZ 822/11s, sowie der Berichtigungsbeschluss vom 4. Dezember 2019 (ON 30) legen qualifiziert nahe, dass das Urteil am27. November 2018verkündet wurde.

**False Positives:**

- `Bezirksgerichts Innere Stadt` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

</details>

---

## `GenericCompanyGmbH` 🏆

**F1:** 0.030 | **Precision:** 0.205 | **Recall:** 0.016  

**Format:** `regex`  
**Rule ID:** `84dc7e82`  
**Description:**
Matches generic company names ending in GmbH, AG, GesmbH, or KG that are not law firms, capturing names like 'OBZ Möbel Betriebe GmbH' or 'Katter Maschinenbau AG'.

**Content:**
```
\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\s+(?:GmbH|AG|GesmbH|KG|&\s*Co\s*KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.205 | 0.016 | 0.030 | 322 | 66 | 256 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 66 | 256 | 3929 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Skribe Rechtsanwaelte GmbH` | `Skribe Rechtsanwaelte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)
- `Bezirksgericht Schwechat` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Lederer Rechtsanwalt GmbH` | `Lederer Rechtsanwalt GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Eva Abdelrahman` (person)
- `Dr. Karl-Heinz Plankel` (person)
- `Hochenadel Immobilien GmbH` (organisation)
- `Ritterhof 11, 2661 Graben, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Doschek Rechtsanwalts GmbH` | `Doschek Rechtsanwalts GmbH` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Mag. Florian Kucera` (person)
- `Mag. Timon Schönswetter` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_4`)


Norsee Technologien GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Norsee Technologien GmbH & Co KG` | `Norsee Technologien GmbH & Co KG` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Unter Alver GmbH` | `Unter Alver GmbH` |

**Missed by this rule (FN):**

- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_13`)


Am 1. 5. 1999 schloss der Kläger als Lizenzgeber mit der Inn Wiltalver GesmbH und der Grünkorn Garten GesmbH als Lizenznehmerinnen zwei gleichlautende Lizenzverträge.

| Predicted | Gold |
|---|---|
| `Inn Wiltalver GesmbH` | `Inn Wiltalver GesmbH` |

**Missed by this rule (FN):**

- `Grünkorn Garten GesmbH` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_15`)


Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Albrucklog Event GmbH als übernehmende Gesellschaft verschmolzen, die am 26.

| Predicted | Gold |
|---|---|
| `Albrucklog Event GmbH` | `Albrucklog Event GmbH` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vogl Rechtsanwalt GmbH` | `Vogl Rechtsanwalt GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `DI Cassandra Wespi` (person)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


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

**Example 9** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die UAMA Analyse Consulting GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

| Predicted | Gold |
|---|---|
| `UAMA Analyse Consulting GmbH` | `UAMA Analyse Consulting GmbH` |

**Example 10** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Steen vertretenen Prentl Handel GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

| Predicted | Gold |
|---|---|
| `Prentl Handel GesmbH & Co KG` | `Prentl Handel GesmbH & Co KG` |

**Missed by this rule (FN):**

- `Susanna Steen` (person)

**Example 11** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Medien Lexsudtal GmbH hinweist.

| Predicted | Gold |
|---|---|
| `Medien Lexsudtal GmbH` | `Medien Lexsudtal GmbH` |

**Example 12** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_9`)


Den weiters mit Strafantrag vom 1. September 2011 (ON 3) erhobenen Vorwurf, der Angeklagte habe am 8. Juli 2010 die Verfügungsberechtigten der Nexlexlog Holding GmbH auch zur leihweisen Überlassung einer Kaffeemaschine im Wert von 390 Euro und eines sogenannten Schokodispensers Exquisit im Wert von 1.328 Euro veranlasst, erachtete das Erstgericht für nicht erweislich.

| Predicted | Gold |
|---|---|
| `Nexlexlog Holding GmbH` | `Nexlexlog Holding GmbH` |

**Example 13** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Stephan Briem Rechtsanwalt GmbH` | `Stephan Briem Rechtsanwalt GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Mag. Malesich` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Pascal Alsweh` (person)
- `Dr. Simone Pittruff` (person)
- `Unter-Analyse Aktiengesellschaft` (organisation)
- `Shamiyeh & Reiser Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


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

**Example 15** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_34`)


Der von den Beklagten erhobene (und mit dem Fehlen der Passivlegitimation verbundene) Einwand, es sei auch das Ersitzungsverbot öffentlichen Wasserguts (oder eine Ersitzung gegenüber der Österreichische Bundesforste AG bzw deren Rechtsvorgänger) zu prüfen, scheitert schon daran.

| Predicted | Gold |
|---|---|
| `Bundesforste AG` | `Bundesforste AG` |

**Example 16** (doc_id: `deanon_260716_TRAIN/1Ob139_18z`) (sent_id: `deanon_260716_TRAIN/1Ob139_18z_3`)


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

**Example 17** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_4`)


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

**Example 18** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


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

**Example 19** (doc_id: `deanon_260716_TRAIN/2Nc25_11s`) (sent_id: `deanon_260716_TRAIN/2Nc25_11s_3`)


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

**Example 20** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Fenuni AG` | `Fenuni AG` |

**Missed by this rule (FN):**

- `Uniber-Verlag AG` (organisation)
- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)
- `Liebenwein Rechtsanwälte GmbH` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_5`)


Seecon Verlag GmbH, Krengasse 31, 3911 Marbach am Walde, Österreich, und 2. Mag. Lena Zikorski, beide vertreten durch die Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen jeweils 50.000,50 EUR sA (Klagen) und 483.000 EUR sA (Widerklagen), über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. April 2010, GZ 15 R 257/09p-58, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Seecon Verlag GmbH` | `Seecon Verlag GmbH` |

**Missed by this rule (FN):**

- `Krengasse 31, 3911 Marbach am Walde, Österreich` (address)
- `Mag. Lena Zikorski` (person)
- `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_4`)


Guntram Wellenbring, vertreten durch Dr. Peter Sparer, Rechtsanwalt in Innsbruck, 2. Verbruckal AG, Stäpfle 16, 1020 Wien, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `Verbruckal AG` | `Verbruckal AG` |

**Missed by this rule (FN):**

- `Guntram Wellenbring` (person)
- `Dr. Peter` (person)
- `Stäpfle 16, 1020 Wien, Österreich` (address)
- `Dr. Harald Burmann` (person)

**Example 23** (doc_id: `deanon_260716_TRAIN/3Ob139_20t`) (sent_id: `deanon_260716_TRAIN/3Ob139_20t_3`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/3Ob150_16d`) (sent_id: `deanon_260716_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Fenmon Versicherung GmbH, Grundwiesenweg 291, 3141 Panzing, Österreich, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Unter Condon Consulting GmbH, Pengersdorf 5, 9556 Gößeberg, Österreich, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Doschek Rechtsanwalts GmbH` | `Doschek Rechtsanwalts GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Roch` (person)
- `Dr. Kodek` (person)
- `Fenmon Versicherung GmbH` (organisation)
- `Grundwiesenweg 291, 3141 Panzing, Österreich` (address)
- `Dr. Andrea Gesinger` (person)
- `Unter Condon Consulting GmbH` (organisation)
- `Pengersdorf 5, 9556 Gößeberg, Österreich` (address)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts St. Johann im Pongau` (organisation)
- `Bezirksgerichts St. Johann im Pongau` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/3Ob166_25w`) (sent_id: `deanon_260716_TRAIN/3Ob166_25w_4`)


Eduard Mauderer, vertreten durch Mag. Sarah Abel, Rechtsanwältin in Salzburg, und 2. Schmiede Digital GmbH, Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich, vertreten durch die Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, wegen 7.164,36 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 10. Juli 2025, GZ 53 R 145/25t-18, mit dem das Teilurteil des Bezirksgerichts Salzburg vom 12. März 2025, GZ 31 C 1179/24h-12, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Schmiede Digital GmbH` | `Schmiede Digital GmbH` |

**Missed by this rule (FN):**

- `Eduard Mauderer` (person)
- `Mag. Sarah Abel` (person)
- `Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich` (address)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_10`)


Text Entscheidungsgründe: Folgender vom Berufungsgericht übernommener und nach dem Akteninhalt ergänzter Sachverhalt ist unstrittig: Mit Beschluss des Erstgerichts vom 18. Juli 2006 wurde über das Vermögen der Derder GmbH (in der Folge: Gemeinschuldnerin) der Konkurs eröffnet.

| Predicted | Gold |
|---|---|
| `Derder GmbH` | `Derder GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Partei Hollengk Planung GmbH` — partial — gold is substring of pred: `Hollengk Planung GmbH`
- `Partei Wind Nexheimval GmbH` — partial — gold is substring of pred: `Wind Nexheimval GmbH`

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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Partei WestTelekom GmbH` — partial — gold is substring of pred: `WestTelekom GmbH`

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

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Automotive GmbH` — partial — pred is substring of gold: `Ober-Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Ober-Automotive GmbH`(organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich`(address)
- `Mag. Alexander Rimser`(person)
- `Katharina Rothschadl`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Ysner Daten GmbH` — partial — pred is substring of gold: `Steidlen+Ysner Daten GmbH`
- `Partei Verlag Waldlemder GmbH` — partial — gold is substring of pred: `Verlag Waldlemder GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Nebenintervenientin Ober Dertri GmbH` — partial — gold is substring of pred: `Ober Dertri GmbH`
- `Partei Rudolf Ketelhut GmbH` — partial — gold is substring of pred: `Rudolf Ketelhut`
- `Energie GmbH` — partial — pred is substring of gold: `Völkertz Energie GmbH`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Hochenadel Immobilien GmbH` — partial — gold is substring of pred: `Hochenadel Immobilien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Eva Abdelrahman`(person)
- `Dr. Karl-Heinz Plankel`(person)
- `Hochenadel Immobilien GmbH`(organisation)
- `Ritterhof 11, 2661 Graben, Österreich`(address)
- `Lederer Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Partei Juri Gerstl GmbH` — partial — gold is substring of pred: `Juri Gerstl`
- `Partei Bundesbeschaffung GmbH` — partial — gold is substring of pred: `Bundesbeschaffung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Gruppe GmbH` — partial — pred is substring of gold: `SüdSanitär Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Verein für Konsumenteninformation`(organisation)
- `Dr. Walter Reichholf`(person)
- `SüdSanitär Gruppe GmbH`(organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich`(address)
- `Kraft & Winternitz Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Partei Akbayrak Metall GmbH` — partial — gold is substring of pred: `Akbayrak Metall GmbH`

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

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Heimcon Software GmbH` — partial — gold is substring of pred: `Heimcon Software GmbH`
- `Partei Gunter Landwirtschaft GmbH` — partial — gold is substring of pred: `Gunter Landwirtschaft GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Heimcon Software GmbH`(organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich`(address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH`(organisation)
- `Gunter Landwirtschaft GmbH`(organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich`(address)
- `Stolz & Schartner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_13`)


Am 1. 5. 1999 schloss der Kläger als Lizenzgeber mit der Inn Wiltalver GesmbH und der Grünkorn Garten GesmbH als Lizenznehmerinnen zwei gleichlautende Lizenzverträge.

**False Positives:**

- `Garten GesmbH` — partial — pred is substring of gold: `Grünkorn Garten GesmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Wiltalver GesmbH`(organisation)
- `Grünkorn Garten GesmbH`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Partner KG` — partial — pred is substring of gold: `Pieler & Pieler & Partner KG`

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

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Bau Zorostfurt GmbH` — partial — gold is substring of pred: `Bau Zorostfurt GmbH`
- `Rothauge Landwirtschaft GmbH` — partial — pred is substring of gold: `Buitenkamp und Rothauge Landwirtschaft GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Bau Zorostfurt GmbH`(organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich`(address)
- `Dr. Alexandra Slama`(person)
- `Buitenkamp und Rothauge Landwirtschaft GmbH`(organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich`(address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_9`)


Er trat deswegen im Mai 2018 an die Klägerin heran, um eine Regelung seiner „persönlichen Haftungen“ über „rund 500.000 EUR“ aus der „Bürgschaft Norallex-Heizung GmbH“ zu erreichen.

**False Positives:**

- `Heizung GmbH` — partial — pred is substring of gold: `Norallex-Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Norallex-Heizung GmbH`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Antonewitz Chemie AG` — partial — pred is substring of gold: `Langhansl+Antonewitz Chemie AG`
- `Pharma GmbH` — partial — pred is substring of gold: `Drau-Pharma GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Bilek Lebensmittel GmbH` — partial — gold is substring of pred: `Bilek Lebensmittel GmbH`
- `Eckert Rechtsanwalts GmbH` — partial — pred is substring of gold: `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `DI Cassandra Wespi`(person)
- `Vogl Rechtsanwalt GmbH`(organisation)
- `Bilek Lebensmittel GmbH`(organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich`(address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der GBJU Getränke GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `GBJU Getränke GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GBJU Getränke GmbH & Co KG`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_27`)


Der Kläger konsumierte die bewilligten Leistungen im September und November 2009 bei der Pharma Glanzsynstein GmbH.

**False Positives:**

- `Pharma Glanzsynstein GmbH` — partial — pred is substring of gold: `Pharma Glanzsynstein GmbH.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pharma Glanzsynstein GmbH.`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_30`)


Die GmbH verfügt auch über keine Bewilligung als Krankenanstalt bzw selbständiges Ambulatorium im Sinne des WrKAG und über keinen ärztlichen Leiter.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Mesarec Medien GesmbH & Co KG` — partial — pred is substring of gold: `Hauenschildt&Mesarec Medien GesmbH & Co KG`
- `Transport GmbH` — partial — pred is substring of gold: `Donau-Transport GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Berti`(person)
- `Norbert Wierich`(person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich`(address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG`(organisation)
- `Susanne Schwarzhuber`(person)
- `Donau-Transport GmbH`(organisation)
- `TraunTouristik Werke GesmbH & Co KG`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Songül Bau GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Bau GmbH` — partial — pred is substring of gold: `Songül Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Songül Bau GmbH`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__16`)


Mit Urteil desselben Tages erkannte das Gericht den Angeklagten „im Sinne der Anklageschrift“ des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie mehrerer Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB schuldig, verhängte über ihn eine Freiheitsstrafe und verpflichtete ihn, an die Privatbeteiligte St Donau Triheim AG einen Geldbetrag zu bezahlen.

**False Positives:**

- `Privatbeteiligte St Donau Triheim AG` — partial — gold is substring of pred: `Donau Triheim AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donau Triheim AG`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__3`)


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

**Example 23** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__4`)


In der Medienrechtssache des Antragstellers Univ.-Prof.in Laurin Schramm gegen die Antragsgegnerin CDL Luftfahrt GmbH wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, verletzen die Urteile 1./ dieses Gerichts vom 26. März 2018 (ON 65) in seinem Punkt III./, womit der Antrag des Antragstellers, der Antragsgegnerin Drau-IT GmbH auch für die am 4. Juni 2017 auf dem Facebook-Account von www.

**False Positives:**

- `Antragsgegnerin CDL Luftfahrt GmbH` — partial — gold is substring of pred: `CDL Luftfahrt GmbH`
- `IT GmbH` — partial — pred is substring of gold: `Drau-IT GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Laurin Schramm`(person)
- `CDL Luftfahrt GmbH`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Drau-IT GmbH`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__10`)


für die dadurch zugefügte Kränkung wurde die Antragsgegnerin Tenholt Holz GmbH nach § 6 Abs 1 MedienG zur Zahlung einer Entschädigung sowie nach § 8a Abs 6 MedienG iVm § 34 Abs 1 MedienG zur Urteilsveröffentlichung verpflichtet.

**False Positives:**

- `Antragsgegnerin Tenholt Holz GmbH` — partial — gold is substring of pred: `Tenholt Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tenholt Holz GmbH`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__11`)


Hingegen wurde (ua) der Antrag des Antragstellers, der Antragsgegnerin TraunMarine GmbH für die am selben Tag auf dem Facebook-Account von www.

**False Positives:**

- `Antragsgegnerin TraunMarine GmbH` — partial — gold is substring of pred: `TraunMarine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunMarine GmbH`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__21`)


Zur Begründung führte das Berufungsgericht – soweit im Folgenden von Relevanz – in ausdrücklicher Abkehr von einer früher vertretenen Rechtsansicht (Urteil des Oberlandesgerichts Wien vom 14. Februar 2018, AZ 17 Bs 212/17a = MR 2018, 7) wie folgt aus (US 32 f): Die Antragsgegnerin Berg-Finanzen Planung GmbH habe auf einer Website (www. Hermani & Grebner Logistik.at) und damit in einem Medium (§ 1 Abs 1 Z 1 MedienG) den Tatbestand der üblen Nachrede hergestellt;

**False Positives:**

- `Finanzen Planung GmbH` — partial — pred is substring of gold: `Berg-Finanzen Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Berg-Finanzen Planung GmbH`(organisation)
- `Hermani & Grebner Logistik.at`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__34`)


Die Haftung des auf eigene Inhalte Verlinkenden als Content-Provider richtet sich daher nach den allgemeinen (straf-)rechtlichen Normen und soweit dieser – wie vorliegend – Medieninhaber ist, nach dem Mediengesetz (Reindl-Krauskopf/Salimi/Stricker, IT-Strafrecht [2018] Rz 3.3, 3.10 und 3.33;Koziol, Haftpflichtrecht II³ A/6/Rz 204;Zankl, E-Commerce-Gesetz, Kommentar2Rz 277), sodass § 17 ECG der geltend gemachten Verantwortlichkeit der Antragsgegnerin Kirmayer Heizung GmbH nach § 6 Abs 1 MedienG nicht entgegensteht.

**False Positives:**

- `Antragsgegnerin Kirmayer Heizung GmbH` — partial — gold is substring of pred: `Kirmayer Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kirmayer Heizung GmbH`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__40`)


Voraussetzung für die geltend gemachte Haftung der Antragsgegnerin TUEU Garten GmbH nach § 6 Abs 1 MedienG ist, dass im Medium „Website“ (§ 1 Abs 1 Z 5a lit b MedienG) der objektive Tatbestand der üblen Nachrede hergestellt wurde.

**False Positives:**

- `Antragsgegnerin TUEU Garten GmbH` — partial — gold is substring of pred: `TUEU Garten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TUEU Garten GmbH`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__60`)


Da sich diese Gesetzesverletzung nicht zum Nachteil der Antragsgegnerin Heimnexfen Planung Entwicklung GmbH, der als Medieninhaberin die Rechte des Angeklagten zukommen (§ 41 Abs 6 zweiter Satz MedienG), auswirkt, kommt ein Vorgehen nach § 292 letzter Satz StPO nicht in Betracht und hat es mit der Feststellung des Gesetzesverstoßes sein Bewenden.

**False Positives:**

- `Antragsgegnerin Heimnexfen Planung Entwicklung GmbH` — partial — gold is substring of pred: `Heimnexfen Planung Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heimnexfen Planung Entwicklung GmbH`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_4`)


In der Medienrechtssache der Antragsteller Dr. Patrick Schneeweiss und Chen Hölzle gegen die Antragsgegnerin TQGK Versicherung Holding GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p, verletzt der Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), § 395 Abs 2 StPO (iVm § 41 Abs 1 MedienG).

**False Positives:**

- `Antragsgegnerin TQGK Versicherung Holding GmbH & Co KG` — partial — gold is substring of pred: `TQGK Versicherung Holding GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Patrick Schneeweiss`(person)
- `Chen Hölzle`(person)
- `TQGK Versicherung Holding GmbH & Co KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_5`)


Dieses Urteil sowie der gemäß § 494a Abs 1 StPO gefasste Beschluss werden aufgehoben und es wird in der Sache selbst zu Recht erkannt: Georg Hamker wird von dem wider ihn erhobenen Vorwurf, er habe in Joseph-Mohr-Straße 15, 5233 Erlach, Österreich mit dem Vorsatz, durch das Verhalten des Getäuschten sich oder einen Dritten unrechtmäßig zu bereichern, Bedienstete der Firma Meyerotto u. Pleuler Handel GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu nachgenannten Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro, jedoch nicht 50.000 Euro übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Pleuler Handel GmbH` — partial — pred is substring of gold: `Meyerotto u. Pleuler Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Georg Hamker`(person)
- `Joseph-Mohr-Straße 15, 5233 Erlach, Österreich`(address)
- `Meyerotto u. Pleuler Handel GmbH`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_7`)


Text Gründe: Mit dem unangefochten in Rechtskraft erwachsenen Urteil des Landesgerichts Feldkirch vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, wurde Georg Höfs - abweichend von dem in Richtung §§ 146, 147 Abs 2 StGB erhobenen Strafantrag - des Vergehens des Betrugs nach § 146 StGB schuldig erkannt und zu einer teilweise bedingt nachgesehenen Geldstrafe verurteilt. Nach dem Schuldspruch hat er in Chikago 2. Gasse 8, 4613 Hupfau, Österreich mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz Bedienstete der (richtig:) Nobars und Huenecken E‑Commerce GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro nicht übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Nobars und Huenecken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Georg Höfs`(person)
- `Chikago 2. Gasse 8, 4613 Hupfau, Österreich`(address)
- `Nobars und Huenecken E‑Commerce GmbH`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/18OCg12_19t`) (sent_id: `deanon_260716_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Energie Glanzgart GmbH, Waldelweg 28, 4201 Maierleiten, Österreich, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Piedro Arnoult, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Partei Energie Glanzgart GmbH` — partial — gold is substring of pred: `Energie Glanzgart GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Veith`(person)
- `Dr. Höllwerth`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Mag. Painsi`(person)
- `Energie Glanzgart GmbH`(organisation)
- `Waldelweg 28, 4201 Maierleiten, Österreich`(address)
- `SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH`(organisation)
- `Piedro Arnoult`(person)

**Example 34** (doc_id: `deanon_260716_TRAIN/1Nc1_15k`) (sent_id: `deanon_260716_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Große-Schulte & Seufer E‑Commerce GmbH, Untererb 31, 3033 Altlengbach, Österreich, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Wilbachkel Luftfahrt GmbH, Andrä Idl-Straße 79, 4791 Haselbach, Österreich, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Große-Schulte & Seufer E‑Commerce GmbH`
- `Partei Wilbachkel Luftfahrt GmbH` — partial — gold is substring of pred: `Wilbachkel Luftfahrt GmbH`

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

**Example 35** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Melinda Steenbekke, und 3. Naujox und Obermauer Luftfahrt GmbH, Kreuten 4, 3385 Uttendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Obermauer Luftfahrt GmbH` — partial — pred is substring of gold: `Naujox und Obermauer Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Melinda Steenbekke`(person)
- `Naujox und Obermauer Luftfahrt GmbH`(organisation)
- `Kreuten 4, 3385 Uttendorf, Österreich`(address)
- `Dr. Hubert Simon`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Leoben`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


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

**Example 37** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_3`)


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

**Example 38** (doc_id: `deanon_260716_TRAIN/1Ob163_21h`) (sent_id: `deanon_260716_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Christine Neemeyer, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Synbach-Holz Bank AG, Bergbahnweg 7j, 4632 Oberthambach, Österreich, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Holz Bank AG` — positional overlap with gold: `Synbach-Holz Bank`

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

**Example 39** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Damian GmbH` — partial — pred is substring of gold: `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`
- `Partei MittelEnergie Werke Bank AG` — partial — gold is substring of pred: `MittelEnergie Werke Bank`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 40** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_5`)


Text Begründung: Eine GmbH, deren Mehrheitsgesellschafter und Geschäftsführer ein Cousin des Klägers war, beabsichtigte, bei der beklagten Bank einen Kredit aufzunehmen, dessen Gewährung allerdings von der Bestellung einer Sicherheit abhängig gemacht wurde, zumal damals nur ungefähr die Hälfte des Gesamtobligos der GmbH bei der Beklagten von rund 6,6 Mio EUR besichert war.

**False Positives:**

- `Eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_260716_TRAIN/1Ob216_15v`) (sent_id: `deanon_260716_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Suleika Kranigk, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Kelfen Transport Solutions GmbH, Geßlgasse 35, 9911 Thal-Wilfern, Österreich, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Kelfen Transport Solutions GmbH` — partial — gold is substring of pred: `Kelfen Transport Solutions GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Suleika Kranigk`(person)
- `Hon.-Prof. Dr. Michel Walter`(person)
- `Kelfen Transport Solutions GmbH`(organisation)
- `Geßlgasse 35, 9911 Thal-Wilfern, Österreich`(address)
- `Partner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Korneuburg`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache klagenden Partei Rainer Baetzel, vertreten durch Dr. Harald Hauer, Rechtsanwalt in Wien, gegen die beklagte Partei Rimscha Versand GmbH in Liquidation, Götzau 193, 5452 Grub, Österreich, vertreten durch die Petsch Frosch Klein Arturo Rechtsanwälte OG, Wien, wegen 38.236,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Oktober 2020, GZ 3 R 51/20x-50, mit dem das Urteil des Handelsgerichts Wien vom 24. Juli 2020, GZ 34 Cg 51/18h-45, bestätigt wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Rimscha Versand GmbH` — partial — gold is substring of pred: `Rimscha Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Rainer Baetzel`(person)
- `Dr. Harald Hauer`(person)
- `Rimscha Versand GmbH`(organisation)
- `Götzau 193, 5452 Grub, Österreich`(address)
- `Petsch Frosch Klein Arturo Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH, Orise 28, 9135 Unterort, Österreich, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Li Wachmeister, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Pia Geermann GmbH` — partial — gold is substring of pred: `Pia Geermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Pia Geermann`(person)
- `Orise 28, 9135 Unterort, Österreich`(address)
- `Dr. Martin Leitner`(person)
- `Li Wachmeister`(person)
- `Estermann Pock Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_52`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_260716_TRAIN/1Ob26_20k`) (sent_id: `deanon_260716_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Schrickel Luftfahrt GmbH, Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Monika Peikert, vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Schrickel Luftfahrt GmbH` — partial — gold is substring of pred: `Schrickel Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Schrickel Luftfahrt GmbH`(organisation)
- `Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich`(address)
- `Draxler Rexeis Sozietät von Rechtsanwälten OG`(organisation)
- `Monika Peikert`(person)
- `Mag. Dr. Alfred Wansch`(person)
- `Bezirksgerichts Hernals`(organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/1Ob29_20a`) (sent_id: `deanon_260716_TRAIN/1Ob29_20a_19`)


Der Mann hat sich an einem Immobilienprojekt, das von einer GmbH & Co KG verwirklicht wird, beteiligt.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_260716_TRAIN/1Ob51_11y`) (sent_id: `deanon_260716_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Luna Saar, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Bernexwald Heizung GmbH, Viaduktstraße 131, 4814 Gmundnerberg, Österreich, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Bernexwald Heizung GmbH` — partial — gold is substring of pred: `Bernexwald Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Luna Saar`(person)
- `Mag. Erich Frenner`(person)
- `Bernexwald Heizung GmbH`(organisation)
- `Viaduktstraße 131, 4814 Gmundnerberg, Österreich`(address)
- `Dr. Harald Schwendinger`(person)
- `Dr. Brigitte Piber`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Saalfelden`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/1Ob51_14b`) (sent_id: `deanon_260716_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Mittel-Landwirtschaft Betriebe GmbH, Baurat Schneider Straße 3, 4612 Finklham, Österreich, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

**False Positives:**

- `Landwirtschaft Betriebe GmbH` — partial — pred is substring of gold: `Mittel-Landwirtschaft Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mittel-Landwirtschaft Betriebe GmbH`(organisation)
- `Baurat Schneider Straße 3, 4612 Finklham, Österreich`(address)
- `Dr. Arno Kempf`(person)

**Example 49** (doc_id: `deanon_260716_TRAIN/1Ob53_25p`) (sent_id: `deanon_260716_TRAIN/1Ob53_25p_7`)


Die GmbH verkaufte diesen ohne sein Wissen an ihre rumänische Tochtergesellschaft, die ihn an einen Kunden weiterverkaufte.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Leonhard Lakmayer Ltd, Klauser Ried 27, 4880 Thalham, Österreich, vertreten durch Dr. Wolfgang G. Kretschmer, LL.M. Rechtsanwalt in Wien, gegen die beklagte Partei Frommenkord Technik GmbH, Wiesenthalgasse 20, 2000 Oberzögersdorf, Österreich, vertreten durch Dr. Herwig B. Schönbauer, Rechtsanwalt in Wien, und die Nebenintervenientinnen auf Seiten der beklagten Partei 1.

**False Positives:**

- `Partei Frommenkord Technik GmbH` — partial — gold is substring of pred: `Frommenkord Technik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Leonhard Lakmayer`(person)
- `Klauser Ried 27, 4880 Thalham, Österreich`(address)
- `Dr. Wolfgang G. Kretschmer, LL.M.`(person)
- `Frommenkord Technik GmbH`(organisation)
- `Wiesenthalgasse 20, 2000 Oberzögersdorf, Österreich`(address)
- `Dr. Herwig B. Schönbauer`(person)

**Example 51** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_4`)


Gloria Hackenbuchner GmbH, Untere Kanalstraße 187, 2471 Hollern, Österreich, vertreten durch Mag. Manfred Sommerbauer und MMag. Dr. Michael Dohr LL.M., Rechtsanwälte in Wiener Neustadt, und 2. Nelleßen + Stümpfel Automotive AG, Villengasse 31, 8670 Krieglach, Österreich, vertreten durch die Kosch & Partner Rechtsanwälte GmbH, Wiener Neustadt, wegen 76.444,01 EUR sA über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2017, GZ 1 R 164/16v-174, mit dem das Urteil des Handelsgerichts Wien vom 12. August 2016, GZ 65 Cg 12/15x-169, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gloria Hackenbuchner GmbH` — partial — gold is substring of pred: `Gloria Hackenbuchner`
- `Automotive AG` — partial — pred is substring of gold: `Nelleßen + Stümpfel Automotive AG`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 52** (doc_id: `deanon_260716_TRAIN/1Ob93_17h`) (sent_id: `deanon_260716_TRAIN/1Ob93_17h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Brechtold Textil GmbH, St. Anna Straße 10, 9564 Rottenstein, Österreich, Deutschland, vertreten durch Dr. Stefan Gulner, Rechtsanwalt in Wien, gegen die beklagte Partei ÖkR Ali Abramenko, vertreten durch die Maggi Brandl Kathollnig RechtsanwaltsGmbH-Studio Legale, Klagenfurt am Wörthersee, wegen 191.469 EUR sA, über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 10. April 2017, GZ 4 R 32/17h-28, mit dem der Beschluss des Landesgerichts Klagenfurt vom 25. Jänner 2017, GZ 49 Cg 60/14k-24, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Partei Brechtold Textil GmbH` — partial — gold is substring of pred: `Brechtold Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Brechtold Textil GmbH`(organisation)
- `St. Anna Straße 10, 9564 Rottenstein, Österreich`(address)
- `Dr. Stefan Gulner`(person)
- `ÖkR Ali Abramenko`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/1Ob95_21h`) (sent_id: `deanon_260716_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Gawelzyk Pflege GmbH, Am See IX 247, 6320 Achleit, Österreich, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Loos und Woiciech Analyse GmbH, Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Gawelzyk Pflege GmbH` — partial — gold is substring of pred: `Gawelzyk Pflege GmbH`
- `Woiciech Analyse GmbH` — partial — pred is substring of gold: `Loos und Woiciech Analyse GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Gawelzyk Pflege GmbH`(organisation)
- `Am See IX 247, 6320 Achleit, Österreich`(address)
- `Zumtobel Kronberger Rechtsanwälte OG`(organisation)
- `Loos und Woiciech Analyse GmbH`(organisation)
- `Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Ried im Innkreis`(organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_9`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Bornwasser & Plöckinger Druck AG; von derselben intendierte Verwertung der Liegenschaften in Thalstraße 358X, 5232 Aigen, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Am Weinbühel 2, 5201 Wimm, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Druck AG` — partial — pred is substring of gold: `Bornwasser & Plöckinger Druck AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bornwasser & Plöckinger Druck AG`(organisation)
- `Thalstraße 358X, 5232 Aigen, Österreich`(address)
- `Am Weinbühel 2, 5201 Wimm, Österreich`(address)

**Example 55** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_10`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Griete+Leine Technik AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Leine Technik AG` — partial — pred is substring of gold: `Griete+Leine Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Griete+Leine Technik AG`(organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

**False Positives:**

- `Verlag AG` — partial — pred is substring of gold: `Uniber-Verlag AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Uniber-Verlag AG`(organisation)
- `Jedretsberg 24, 4190 Brunnwald, Österreich`(address)
- `Fenuni AG`(organisation)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich`(address)
- `Liebenwein Rechtsanwälte GmbH`(organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


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

**Example 58** (doc_id: `deanon_260716_TRAIN/2Ob194_24d`) (sent_id: `deanon_260716_TRAIN/2Ob194_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dagobert Drügemöller, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Rosalinde Nölker, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Simon Wallner Rechtsanwalt GmbH` — partial — pred is substring of gold: `Mag. Simon Wallner Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `Dagobert Drügemöller`(person)
- `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH`(organisation)
- `Rosalinde Nölker`(person)
- `Mag. Simon Wallner Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/2Ob216_18f`) (sent_id: `deanon_260716_TRAIN/2Ob216_18f_3`)


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

**Example 60** (doc_id: `deanon_260716_TRAIN/2Ob71_18g`) (sent_id: `deanon_260716_TRAIN/2Ob71_18g_3`)


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

**Example 61** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_3`)


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

**Example 62** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_5`)


See-Umwelt Manufaktur AG, Zosen 244, 9543 Sauboden, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

**False Positives:**

- `Umwelt Manufaktur AG` — partial — pred is substring of gold: `See-Umwelt Manufaktur AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See-Umwelt Manufaktur AG`(organisation)
- `Zosen 244, 9543 Sauboden, Österreich`(address)
- `Dr. Walter Heel`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/3Nc11_13t`) (sent_id: `deanon_260716_TRAIN/3Nc11_13t_3`)


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

**Example 64** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_4`)


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

**Example 65** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_5`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_260716_TRAIN/3Ob139_20t`) (sent_id: `deanon_260716_TRAIN/3Ob139_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der gefährdeten Partei Dr. Günter Geusau, Rechtsanwalt in Wels, als Masseverwalter über das Vermögen der Kelwald GmbH, Friedelstraße 1, 8350 Pertlstein, Österreich, gegen die Gegnerin der gefährdeten Partei Füsslin Telekom GmbH, Kaltbach 4, 8733 Hof, Österreich, vertreten durch Stock Rechtsanwälte PartnerschaftsgesellschaftmbB in Siegen, Deutschland, im Einvernehmen mit Mag. Martin Schönmair, Rechtsanwalt in Wels, wegen einstweiliger Verfügung nach § 381 Z 1 EO (265.239,60 EUR), aus Anlass des außerordentlichen Revisionsrekurses der gefährdeten Partei gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 1. Juli 2020, GZ 22 R 129/20g-12, mit dem der Beschluss des Bezirksgerichts Wels vom 3. April 2020, GZ 8 C 302/20g-2, abgeändert wurde, den Beschluss gefasst:  Spruch Aus Anlass des Revisionsrekurses der gefährdeten Partei wird der Beschluss des Rekursgerichts, mit dem über den Rekurs der Gegnerin der gefährdeten Partei meritorisch entschieden wurde, als nichtig aufgehoben, und dem Erstgericht aufgetragen, den Schriftsatz der Gegnerin der gefährdeten Partei vom 29. April 2020 (nur) als Widerspruch gegen die Einstweilige Verfügung des Erstgerichts vom 3. April 2020, GZ 8 C 302/20g-2, zu behandeln und darüber das gesetzmäßige Verfahren einzuleiten.

**False Positives:**

- `Telekom GmbH` — partial — pred is substring of gold: `Füsslin Telekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Roch`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Dr. Günter Geusau`(person)
- `Kelwald GmbH`(organisation)
- `Friedelstraße 1, 8350 Pertlstein, Österreich`(address)
- `Füsslin Telekom GmbH`(organisation)
- `Kaltbach 4, 8733 Hof, Österreich`(address)
- `Stock Rechtsanwälte PartnerschaftsgesellschaftmbB`(organisation)
- `Mag. Martin Schönmair`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Wels`(organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/3Ob139_20t`) (sent_id: `deanon_260716_TRAIN/3Ob139_20t_5`)


Text Begründung: [1] Mit Vertrag vom 5. August 2018 vereinbarten die Gegnerin der gefährdeten Partei (im Folgenden: Bestellerin) und eine Maschinenbau GmbH (im Folgenden: Werkunternehmerin) die Lieferung einer Kesselbodenfräsmaschine.

**False Positives:**

- `Maschinenbau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_260716_TRAIN/3Ob147_20v`) (sent_id: `deanon_260716_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Glanzval Dienstleistungen GmbH, Otto-Hittmair-Platz 29, 9423 Steinberg-Hart, Österreich, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Gisela Filippovic, MBA verein Arthur Hoelle, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Glanzval Dienstleistungen GmbH` — partial — gold is substring of pred: `Glanzval Dienstleistungen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Roch`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Glanzval Dienstleistungen GmbH`(organisation)
- `Otto-Hittmair-Platz 29, 9423 Steinberg-Hart, Österreich`(address)
- `Mag. Andreas Kleiber`(person)
- `Gisela Filippovic, MBA`(person)
- `Arthur Hoelle`(person)
- `Pflaum Karlberger Wiener Opetnik, Rechtsanwälte`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/3Ob150_16d`) (sent_id: `deanon_260716_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Fenmon Versicherung GmbH, Grundwiesenweg 291, 3141 Panzing, Österreich, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Unter Condon Consulting GmbH, Pengersdorf 5, 9556 Gößeberg, Österreich, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

**False Positives:**

- `Partei Fenmon Versicherung GmbH` — partial — gold is substring of pred: `Fenmon Versicherung GmbH`
- `Partei Unter Condon Consulting GmbH` — partial — gold is substring of pred: `Unter Condon Consulting GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Dr. Kodek`(person)
- `Fenmon Versicherung GmbH`(organisation)
- `Grundwiesenweg 291, 3141 Panzing, Österreich`(address)
- `Dr. Andrea Gesinger`(person)
- `Unter Condon Consulting GmbH`(organisation)
- `Pengersdorf 5, 9556 Gößeberg, Österreich`(address)
- `Doschek Rechtsanwalts GmbH`(organisation)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts St. Johann im Pongau`(organisation)
- `Bezirksgerichts St. Johann im Pongau`(organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/3Ob182_11b`) (sent_id: `deanon_260716_TRAIN/3Ob182_11b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Traun Logtri gesellschaft mbH, Friedhofplatz 9, 5274 Weikerding, Österreich, vertreten durch Dr. Maximilian Gumpoldsberger, Rechtsanwalt in Wels, und der Nebenintervenientin auf Seiten der klagenden Partei Ruddies + Kasperrek Umwelt Gesellschaft mbH, Hohenkogl 4, 8255 Steinhöf, Österreich, vertreten durch Dr. Lydia Friedle, Rechtsanwältin in Mannersdorf am Leithagebirge, gegen die beklagte Partei Büchner Holz GmbH, Schedifkaplatz 3, 3134 Fräuleinmühle, Österreich, vertreten durch Dr. Franz Gütlbauer, Dr. Siegfried Sieghartsleitner und Dr. Michael Pichlmair, Rechtsanwälte in Wels, sowie der Nebenintervenientin auf Seiten der beklagten Partei Feigle + Hinzelin Cloud Gesellschaft mbH, Josef-Wolf-Platz 10, 4063 Rudelsdorf, Österreich, vertreten durch Mag. Thomas Braun, Rechtsanwalt in Wien, wegen restlich 52.596,75 EUR sA, infolge Revision der klagenden Partei gegen das Endurteil des Oberlandesgerichts Linz als Berufungsgericht vom 4. Juli 2011, GZ 4 R 108/11x-47, womit infolge Berufung der klagenden Partei das Endurteil des Landesgerichts Wels vom 14. März 2011, GZ 6 Cg 17/09w-42, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Holz GmbH` — partial — pred is substring of gold: `Büchner Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Traun Logtri gesellschaft mbH`(organisation)
- `Friedhofplatz 9, 5274 Weikerding, Österreich`(address)
- `Dr. Maximilian Gumpoldsberger`(person)
- `Ruddies + Kasperrek Umwelt Gesellschaft mbH`(organisation)
- `Hohenkogl 4, 8255 Steinhöf, Österreich`(address)
- `Dr. Lydia Friedle`(person)
- `Büchner Holz GmbH`(organisation)
- `Schedifkaplatz 3, 3134 Fräuleinmühle, Österreich`(address)
- `Dr. Franz Gütlbauer`(person)
- `Dr. Siegfried Sieghartsleitner`(person)
- `Dr. Michael Pichlmair`(person)
- `Feigle + Hinzelin Cloud Gesellschaft mbH`(organisation)
- `Josef-Wolf-Platz 10, 4063 Rudelsdorf, Österreich`(address)
- `Mag. Thomas Braun`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Moritz Absmeier, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei DENU Immobilien GmbH, Gürtel 12, 5145 Schmalzhofen, Österreich, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Partei DENU Immobilien GmbH` — partial — gold is substring of pred: `DENU Immobilien GmbH`

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

**Example 72** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Druck Steinnex GmbH, Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Partei Druck Steinnex GmbH` — partial — gold is substring of pred: `Druck Steinnex GmbH`

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

**Example 73** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Transport GmbH` — partial — pred is substring of gold: `Traun-Transport GmbH`

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

**Example 74** (doc_id: `deanon_260716_TRAIN/3Ob223_19v`) (sent_id: `deanon_260716_TRAIN/3Ob223_19v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei WestLebensmittel Betriebe GesmbH, Adalbert-Stifter-Platz 4, 3143 Gattring-Raking, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die verpflichtete Partei Dkfm.

**False Positives:**

- `Partei WestLebensmittel Betriebe GesmbH` — partial — gold is substring of pred: `WestLebensmittel Betriebe GesmbH`

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

**Example 75** (doc_id: `deanon_260716_TRAIN/3Ob45_19t`) (sent_id: `deanon_260716_TRAIN/3Ob45_19t_3`)


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

**Example 76** (doc_id: `deanon_260716_TRAIN/3Ob69_19x`) (sent_id: `deanon_260716_TRAIN/3Ob69_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Matthew Pfneissl, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Allex GmbH, Zur Kühlen Luft 10, 3435 Erpersdorf, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung (Streitwert 50.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Februar 2019, GZ 3 R 164/18k-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Allex GmbH` — partial — gold is substring of pred: `Allex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Matthew Pfneissl`(person)
- `Dr. Klaus Plätzer`(person)
- `Allex GmbH`(organisation)
- `Zur Kühlen Luft 10, 3435 Erpersdorf, Österreich`(address)
- `Dr. Patrick Ruth`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Garten AG` — partial — pred is substring of gold: `Lützeler Garten AG`
- `Analyse GmbH` — partial — pred is substring of gold: `Demeyer u. Köktas Analyse GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 78** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_23`)


Diese GmbH arbeitete daraufhin zwei Varianten aus;

**False Positives:**

- `Diese GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Sailer, den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und den Hofrat Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Dr. Johannes Müller, Rechtsanwalt, Wien 3, Ditscheinergasse 2, als Masseverwalter im Konkurs der Wald-Event GmbH, gegen die beklagte Partei Wiener Gebietskrankenkasse, Wien 10, Wienerbergstraße 15-19, vertreten durch Preslmayr Rechtsanwälte OG in Wien, und der Nebenintervenienten auf der Seite der beklagten Partei 1.)

**False Positives:**

- `Event GmbH` — partial — pred is substring of gold: `Wald-Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Hon.-Prof. Dr. Sailer`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Johannes Müller`(person)
- `Wald-Event GmbH`(organisation)
- `Wiener Gebietskrankenkasse`(organisation)
- `Preslmayr Rechtsanwälte OG`(organisation)

</details>

---

## `Courts` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ca6e93fd`  
**Description:**
Matches court names including 'Landesgerichts' with complex location suffixes like 'an der Donau' or 'St. Pölten', and handles genitive forms.

**Content:**
```
\b(?:Verwaltungsgerichtshof(?:es)?|Bundesfinanzgericht(?:es)?|Bundesfinanzgerichts|B(?:undesfinanzgericht|FG)|Obersten\s+Gerichtshof(?:es)?|Landesgericht(?:s)?\s+(?:f\u00fcr\s+(?:Zivilrechtssachen|Strafsachen)?\s+)?[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?(?:\s+[A-Z][a-zA-Z]+)?(?:\s+-\s+[A-Z][a-zA-Z]+)?(?:\s+an\s+der\s+Donau)?(?:\s+St\.\sP\u00f6lten)?|Gerichtshof\sder\sEurop\u00e4ischen\sUnion)(?:\s*\(\s*BFG\s*\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 16 | 0 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 16 | 2452 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_20`)


Ob die offene „Zeitungsröhre“ als solche überhaupt eine Abgabeeinrichtung iSd § 17 Abs 2 ZustG sein kann (der Verwaltungsgerichtshof verneinte eine solche Eigenschaft etwa bei einem frei zugänglichen „Holzverschlag“; vgl 2011/05/0076), muss nach dem Vorgesagten nicht geprüft werden.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_51`)


Auch der Gerichtshof der Europäischen Union wies in diesem Zusammenhang darauf hin, dass der Kausalzusammenhang zwischen dem vom Geschädigten geltend gemachten Schaden und dem (unionsrechtlichen) Vergaberechtsverstoß eine Voraussetzung des Ersatzanspruchs ist (vgl EuGH C-568/08,Combinatie Sijker Infrabouwua, Rn 87;

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/4Ob23_24x`) (sent_id: `deanon_260716_TRAIN/4Ob23_24x_30`)


Der Verwaltungsgerichtshof definiert „Handel“ als eine auf den Warenaustausch zwischen den einzelnen Wirtschaftsgliedern gerichtete gewerbsmäßige Tätigkeit (83/04/0257;

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_23`)


Das Landgericht Ravensburg (Deutschland) hat dem Gerichtshof der Europäischen Union am 9.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_158`)


Was die gerichtliche Nachprüfbarkeit der Einhaltung dieser Voraussetzungen betrifft, billigt der Gerichtshof der Europäischen Union dem Unionsrechtsgesetzgeber im Rahmen der Ausübung der ihm übertragenen Zuständigkeiten ein weites Ermessen in Bereichen zu, in denen seine Tätigkeit sowohl politische als auch wirtschaftliche oder soziale Entscheidungen verlangt und in denen er komplexe Prüfungen und Beurteilungen vornehmen muss.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_5`)


Der Antrag der Revisionswerberin, der Oberste Gerichtshof möge ein Vorabentscheidungsersuchen an den Gerichtshof der Europäischen Union stellen, wird zurückgewiesen.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


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

**Example 8** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_133`)


Der Oberste Gerichtshof hat beschlossen, ein Vorabentscheidungsersuchen an den Gerichtshof der Europäischen Union zu stellen.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_141`)


Der Oberste Gerichtshof würde es begrüßen, wenn der Gerichtshof der Europäischen Union über das vorliegende Vorabentscheidungsersuchen und über die Vorlage des Oberlandesgerichts Innsbruck gemeinsam entscheiden würde.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_163`)


3.2Der österreichische Verwaltungsgerichtshof lässt die Einführung eines neuen Anrechnungs- und Vorrückungssystems nicht genügen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_169`)


Der Verwaltungsgerichtshof gab der Beschwerde des Lehrers statt und sprach aus, dass dem Beschwerdeführer ein Gehalt in der höheren Gehaltsstufe gebühre.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_170`)


Der Verwaltungsgerichtshof korrigierte somit nur den Vorrückungsstichtag nach den zugrunde liegenden neuen Dienstvorschriften, ohne auch den verlängerten Vorrückungszeitraum, der ebenfalls mit den neuen Dienstvorschriften normiert worden war, zu berücksichtigen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_171`)


In seiner Begründung führte der Verwaltungsgerichtshof unter anderem aus, dass weiterhin eine unzulässige Ungleichbehandlung von Zeiten vor bzw nach Vollendung des 18.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_185`)


Der Verwaltungsgerichtshof inkriminiert anscheinend das Ergebnis der gesetzlichen Neuregelung, nach dem sich die Neuermittlung des Vorrückungsstichtags aufgrund der gleichzeitigen Verlängerung des Vorrückungszeitraums nicht auf denEntgeltanspruchdes Beschwerdeführers ausgewirkt hat.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_148`)


3. 2020 legte der Oberste Gerichtshof zu 10 Ob 44/19x dem Gerichtshof der Europäischen Union gemäß Art 267 AEUV folgende Fragen zur Vorabentscheidung vor: 2.1.„1.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

</details>

---

## `GenericFirma` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03c11cff`  
**Description:**
Matches 'Firma' followed by a capitalized name that doesn't end in GmbH/m.b.H. (catching incomplete mentions or specific cases).

**Content:**
```
\bFirma\s+([A-Z][a-zA-Z0-9\s]+?)(?=\s*(?:in|mit|auf|der|die|das|ist|hat|ist|wurde|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TaxAuthorities` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b57de570`  
**Description:**
Matches 'Finanzamt' (standalone or with genitive 'es') and specific location suffixes like 'Schwechat Gerasdorf' or 'Österreich'.

**Content:**
```
\bFinanzamt(?:es)?(?:\s+(?:Schwechat\s+Gerasdorf|Österreich))?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 14 | 1772 |

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

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob2_20t`) (sent_id: `deanon_260716_TRAIN/6Ob2_20t_10`)


Das Insolvenzgericht sprach aus, neben einem vollstreckbaren Rückstandsausweis des Finanzamts von rund 200.000 EUR seien auch Exekutionen mit Ansprüchen von insgesamt über 150.000 EUR anhängig.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_14`)


Die „Erfolgsprämien“ für die ihr für die Jahre 2009 und 2010 vom Finanzamt zuerkannten Forschungsprämien wurden der Klägerin von der Beklagten gezahlt. DieKlägerinerhob aufgrund der Nichtzahlung ihrer die Erfolgsprämie für das Jahr 2011 betreffenden Rechnung vom 7. 12. 2012 am 1. 12. 2015 Klage auf Zahlung von 65.850,37 EUR samt Zinsen.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_36`)


2012 erfolgte die Gutbuchung der Forschungsprämie 2011 auf dem Abgabenkonto der Beklagten durch das Finanzamt.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_37`)


Eine bescheidmäßige Erledigung erfolgt in solchen Fällen nicht, ein Bescheid wird in diesem Zusammenhang vom Finanzamt nur erlassen, wenn die beantragte Forschungsprämie nicht oder nicht zur Gänze gewährt wird.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_52`)


Im Zuge der Betriebsprüfungen durch das Finanzamt war die Klägerin noch zeitweise unterstützend bis in den Oktober 2014 hinein tätig, danach beendete sie ihre Tätigkeit für die Beklagte.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_54`)


Eine Gutbuchung einer Forschungsprämie für das Jahr 2012 durch das Finanzamt erfolgte bis zum Schluss der mündlichen Verhandlung erster Instanz durch das Finanzamt nicht am Abgabenkonto der Beklagten (unbestritten).

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation
- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 8** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_84`)


Das Erstgericht stützte vorliegend seine negative Feststellung – richtig: rechtliche Beurteilung – nun in erster Linie darauf (Ersturteil Seiten 7 f), dass der Geschäftsführer der Beklagten in Gesprächen mit dem Geschäftsführer der Klägerin stets darauf hingewiesen habe, er sei der Meinung, aufgrund der Zurückforderung der Forschungsprämien durch das Finanzamt nichts zu schulden und deshalb die offene Rechnung nicht bezahlen zu können.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_86`)


Gerade letzteres war hier aber nach der genannten (dislozierten) Feststellung der Fall: Der Geschäftsführer der Beklagten erklärte, wegen der Zurückforderung der Forschungsprämie durch das Finanzamt der Klägerin das in Rechnung gestellte Erfolgshonorar nicht bezahlen zu können.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_98`)


Die Klägerin befindet sich damit im Recht: Dass die Klägerin nicht substantiiert bestritt, dass in Hinsicht auf den Betrag von 93.974,50 EUR noch keine Gutschrift des Finanzamts vorliegt, hat allein zur Folge, dass Besagtes unstrittig ist.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_99`)


Hieraus ist aber nicht zwingend zu folgern, dass es sich beim Rechnungsbetrag von 93.974,50 EUR um einen solchen handelt, für dessen Fälligkeit nach der Vereinbarung an eine Gutschrift des Finanzamts angeknüpft wird.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_107`)


Daraus, dass unstrittig in Hinsicht auf den Betrag von 93.974,50 EUR noch keine Gutschrift des Finanzamts vorliegt, kann daher noch nicht automatisch die mangelnde Fälligkeit dieser Forderung abgeleitet werden.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `CompanyGmbH` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fca60947`  
**Description:**
Matches company names ending in GmbH, AG, KG, OG, & Co KG, ensuring the match starts at the name and ends at the suffix, avoiding context like 'an der' or 'Kommanditbeteiligung'.

**Content:**
```
(?:^|\s|\(|,|\.)\s*([A-Z][a-zA-Z0-9\s&+\-]+(?:\s+(?:GmbH|mbH|AG|Aktiengesellschaft|KG|OG|Partnerschaft|Rechtsanw\u00e4lte(?:\s+GmbH|\s+OG|\s+KG)?|Steuerberatungsgesellschaft|Wirtschaftspr\u00fcfung|Consulting|Management|Service|Technik|International)))(?:\s*&\s*Co\s*KG|\s*\(|\s*$|\s+[,\.\s]|\s+\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 22 | 0 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 22 | 3536 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der QVAO Planung GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

**False Positives:**

- `Inanspruchnahme der QVAO Planung GmbH` — partial — gold is substring of pred: `QVAO Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `QVAO Planung GmbH`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__7`)


Text Gründe: I./ In der Medienrechtssache des Antragstellers StR Anna Barkhausen gegen die Antragsgegnerin Tramoncon KI Consulting GmbH (als Medieninhaberin der Websites www.

**False Positives:**

- `In der Medienrechtssache des Antragstellers StR Anna Barkhausen gegen die Antragsgegnerin Tramoncon KI Consulting GmbH` — partial — gold is substring of pred: `StR Anna Barkhausen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Anna Barkhausen`(person)
- `Tramoncon KI Consulting GmbH`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

**False Positives:**

- `Antragsgegnerin Synzortal-Medien GmbH` — positional overlap with gold: `Synzortal-Medien GmbH & Co KG`

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

**Example 4** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH` — positional overlap with gold: `Priv.-Doz.in Heidrun Aguera, BA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wieland Skocdopole`(person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc`(person)
- `Wald Fenkraftal GmbH & Co KG`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_5`)


Text Begründung: Die Nortal-Energie Aktiengesellschaft (im Folgenden: Schuldnerin) betrieb einen Ferienclub.

**False Positives:**

- `Die Nortal-Energie Aktiengesellschaft` — partial — gold is substring of pred: `Nortal-Energie Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nortal-Energie Aktiengesellschaft`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Weber Rechtsanwälte GmbH` — partial — pred is substring of gold: `Weber Rechtsanwälte GmbH & Co KG`
- `BEURLE Rechtsanwälte GmbH` — partial — pred is substring of gold: `BEURLE Rechtsanwälte GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `MMag. Sloboda`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `Denise Markstaler`(person)
- `Weber Rechtsanwälte GmbH & Co KG`(organisation)
- `Rut Adamheit`(person)
- `BEURLE Rechtsanwälte GmbH & Co KG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/2Ob71_23i`) (sent_id: `deanon_260716_TRAIN/2Ob71_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Dr. Nowotny, Hon.-Prof. PD Dr. Rassi, MMag. Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof. Hon.-Prof. Egon Mlinaric, vertreten durch Klepp Nöbauer Hintringer Primetshofer Rechtsanwälte (GbR) in Linz, gegen die beklagte Partei Jaden Rembe, vertreten durch Dr. Christoph Arbeithuber, Rechtsanwalt in Linz, wegen 26.843,50 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Februar 2023, GZ 4 R 17/23g-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hintringer Primetshofer Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `MMag. Sloboda und Dr. Kikinger`(person)
- `Hon.-Prof. Hon.-Prof. Egon Mlinaric`(person)
- `Jaden Rembe`(person)
- `Dr. Christoph Arbeithuber`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Druck Steinnex GmbH, Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `In der Maur & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

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

**Example 9** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH` — positional overlap with gold: `Dr. Stefula`

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

**Example 10** (doc_id: `deanon_260716_TRAIN/3Ob223_19v`) (sent_id: `deanon_260716_TRAIN/3Ob223_19v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei WestLebensmittel Betriebe GesmbH, Adalbert-Stifter-Platz 4, 3143 Gattring-Raking, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die verpflichtete Partei Dkfm.

**False Positives:**

- `In der Maur & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

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

**Example 11** (doc_id: `deanon_260716_TRAIN/3Ob49_11v`) (sent_id: `deanon_260716_TRAIN/3Ob49_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Julius ZYR Automotive GmbH & Co KG, Schamingstraße 16, 8262 Reigersberg, Österreich, vertreten durch Dr. Wolfgang Dartmann und andere Rechtsanwälte in Linz, wider die beklagten Parteien 1. Friedrich Strahsburg und 2.

**False Positives:**

- `Roch als weitere Richter in der Rechtssache der klagenden Partei Julius ZYR Automotive GmbH` — positional overlap with gold: `Dr. Roch`

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

**Example 12** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Lemlemcon GmbH, Albert-Schultz-Eishalle 4, 6863 Großdorf, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1. Koldere und Heddrich Versicherung GmbH & Co KG, 2.

**False Positives:**

- `Koldere und Heddrich Versicherung GmbH` — partial — pred is substring of gold: `Koldere und Heddrich Versicherung GmbH & Co KG`

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

**Example 13** (doc_id: `deanon_260716_TRAIN/6Ob139_19p`) (sent_id: `deanon_260716_TRAIN/6Ob139_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Balthasar Teske, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagte Partei Prof. Dr. Roderich Claaßens, vertreten durch Brauneis Klauser Prändl Rechtsanwälte GmbH in Wien, wegen Rechnungslegung und Zahlung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. April 2019, GZ 14 R 152/18b-16, womit das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 27. September 2018, GZ 4 Cg 50/17b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `In der Maur & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

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

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_7`)


9. 2003 ist im Firmenbuch des Handelsgerichts Wien zu FN FN230079f die Werksteinfurt-Immobilien GmbH (im Folgenden: „Gesellschaft“) eingetragen.

**False Positives:**

- `Firmenbuch des Handelsgerichts Wien zu FN FN230079f die Werksteinfurt-Immobilien GmbH` — partial — gold is substring of pred: `Handelsgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Handelsgerichts Wien`(organisation)
- `FN230079f`(business_register_number)
- `Werksteinfurt-Immobilien GmbH`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN401718s ist im Firmenbuch des Handelsgerichts Wien die Bosman Gastronomie GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

**False Positives:**

- `Zu FN FN401718s ist im Firmenbuch des Handelsgerichts Wien die Bosman Gastronomie GmbH` — partial — gold is substring of pred: `FN401718s`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN401718s`(business_register_number)
- `Handelsgerichts Wien`(organisation)
- `Bosman Gastronomie GmbH`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/6Ob2_20t`) (sent_id: `deanon_260716_TRAIN/6Ob2_20t_4`)


Text Begründung: Eine Gesellschaft mbH („GmbH“) wollte ihr angeblich gegen die Beklagte zustehende, hier klagsgegenständliche Forderungen von über 2.000.000 EUR einklagen.

**False Positives:**

- `Eine Gesellschaft mbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_6`)


Text Entscheidungsgründe: [1] Zwischen der Sudwil-Lebensmittel GmbH (in Hinkunft: Versicherungsnehmerin) und der Beklagten besteht ein Rechtsschutzversicherungsvertrag, der auch den Rechtsschutz für den Privatbereich des Betriebsinhabers umfasst.

**False Positives:**

- `Zwischen der Sudwil-Lebensmittel GmbH` — partial — gold is substring of pred: `Sudwil-Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sudwil-Lebensmittel GmbH`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_15`)


Diese zog für die Lieferung der Isolierglasscheiben die Chmieleffski Umwelt GmbH (in Hinkunft Subunternehmerin) bei.

**False Positives:**

- `Lieferung der Isolierglasscheiben die Chmieleffski Umwelt GmbH` — partial — gold is substring of pred: `Chmieleffski Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Chmieleffski Umwelt GmbH`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/9ObA124_19d`) (sent_id: `deanon_260716_TRAIN/9ObA124_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hopf als Vorsitzenden, die Hofrätin Dr. Fichtenau und den Hofrat Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Bartscherer und Wagenknecht Holz GmbH & Co KG, Gotthelfgasse 57 - 74, 9361 Leimersberg, Österreich, vertreten durch Burgstaller & Preyer Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Richard Armgart, vertreten durch Mag. Franjo Schruiff, LL.M. Rechtsanwalt in Wien, wegen 14.927,23 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. August 2019, GZ 10 Ra 33/19z-30, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Arbeitsrechtssache der klagenden Partei Bartscherer und Wagenknecht Holz GmbH` — positional overlap with gold: `Bartscherer und Wagenknecht Holz GmbH & Co KG`

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

**Example 20** (doc_id: `deanon_260716_TRAIN/9ObA76_13m`) (sent_id: `deanon_260716_TRAIN/9ObA76_13m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Ernst Bassler als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adrian Leiße, BSc, vertreten durch Dr. H. Burmann ua, Rechtsanwälte in Innsbruck, gegen die beklagten Parteien 1. Logkraft-Verlag GmbH & Co KG, 2.

**False Positives:**

- `Logkraft-Verlag GmbH` — partial — pred is substring of gold: `Logkraft-Verlag GmbH & Co KG`

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

## `MinistryAbbreviations` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3eb2075a`  
**Description:**
Matches Bundesministeriums für Finanzen and its abbreviations BMF, BM für Finanzen.

**Content:**
```
\b(?:Bundesministeriums\sfür\sFinanzen|BMF|BM\sfür\sFinanzen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KAG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3856d842`  
**Description:**
Matches the specific abbreviation KAG which appears frequently in the text as an organization.

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

## `BFH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5d06e25b`  
**Description:**
Matches the German Federal Fiscal Court abbreviation BFH.

**Content:**
```
\bBFH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PoliceAuthorities` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7652b5fe`  
**Description:**
Matches 'Landespolizeidirektion' and similar police authority names, strictly bounded to prevent capturing trailing words.

**Content:**
```
\bLandespolizeidirektion(?:\s+(?:Wien))?\b
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

## `AMS` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8df62c8b`  
**Description:**
Matches the abbreviation AMS (Arbeitsmarktservice) as an organization.

**Content:**
```
\bAMS\b
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

## `Landesgericht` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e3c4aa61`  
**Description:**
Matches Land Courts (Landesgericht) and its genitive form.

**Content:**
```
\bLandesgericht(?:es)?\b
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

## `ÖGK` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e381a0a`  
**Description:**
Matches the specific abbreviation ÖGK (Österreichische Gesundheitskasse) as an organization.

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

## `TaxAuthorityFA` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b23075c0`  
**Description:**
Matches 'FA' followed by a location, ensuring the match stops before common prepositions or end of sentence to avoid capturing 'vom' or other trailing words.

**Content:**
```
\bFA\s+([A-Z][a-zA-Z\s]+?)(?=\s+(?:vom|am|des|der|in|an|bei|mit|nach|vor|über|unter|auf|zu|von|für|gegen|ohne|durch|seit|bis|um|an|bei|mit|nach|vor|über|unter|auf|zu|von|für|gegen|ohne|durch|seit|bis|um|\.|,|\)|\]|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UniversityWien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `67e7c8f3`  
**Description:**
Matches 'Universität Wien' which was previously missing.

**Content:**
```
\bUniversit\u00e4t\sWien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `MinistryBMI` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `393052ea`  
**Description:**
Matches 'BMI' (Bundesministerium für Inneres) as an organization.

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

## `Pensionsversicherungsanstalt` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `87469955`  
**Description:**
Matches the specific organization 'Pensionsversicherungsanstalt' which was missing.

**Content:**
```
\bPensionsversicherungsanstalt\b
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

## `SKTelecom` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `99ac9790`  
**Description:**
Matches 'SK Telecom' variations which appear frequently in legal texts regarding EU court cases.

**Content:**
```
\bSK\s+Telecom(?:\s+Co\.?\s+Ltd)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WienerGemeinderat` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `965ee445`  
**Description:**
Matches 'Wiener Gemeinderat' and 'Wiener Gemeinderates' variations.

**Content:**
```
\bWiener\s+Gemeinderat(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BundesamtSoziales` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c51d21bb`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamt\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PostAG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8d797d70`  
**Description:**
Matches 'Post AG' specifically to capture this common organization which was previously missed.

**Content:**
```
\bPost\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `COFAG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7085fcac`  
**Description:**
Matches the specific organization COFAG (Corona-Fonds-Ausgleichsgesellschaft) which was frequently missed or incorrectly matched as part of 'COFAG-NoAG'.

**Content:**
```
\bCOFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BHAG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6d26651f`  
**Description:**
Matches the specific organization BHAG (Bundeshaushaltsagentur) which was missed.

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

</details>

---

