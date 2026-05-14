# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-14T08:15:10.790146

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-14/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 400 |
| Validation documents | 101 |
| Test documents | 12 |
| Train sentences | 1171 |
| Validation sentences | 213 |
| Test sentences | 1247 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 60 |
| Refinement iterations | 0 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 10 |
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
| Accuracy (exact match) | 84.4% |
| True Positives | 4 |
| False Positives | 10 |
| False Negatives | 252 |
| Total Gold Entities | 256 |
| Micro Precision | 28.6% |
| Micro Recall | 1.6% |
| Micro F1 | 3.0% |
| Macro F1 | 3.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Finanzamt and FA Districts` | 3.1% | 100.0% | 1.6% | 4 | 4 | 0 |
| `Specific Private Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Names (No Suffix)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Names (With Suffix)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Reinemut Smoch Handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Salzburg-Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Salzburg-Stadt URL` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Triloglex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company MittelHeizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Rosilius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity Zoruniglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity Sophie Wittmeir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Klusner` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Tschermack` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company TalVerverwerk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company SudLandwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Bank and Other Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `General Company with Suffix` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Specific Legal Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Versicherung Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific IT Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Verlag Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Maschinenbau Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Luftfahrt Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Finanzamt Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Named Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KG Company Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Trade Names (No Suffix)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH & Partner KG Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank Locations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WaldTouristik Technologies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Legal Case Organization Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bank and Institute Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Court Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific GMBH Names with Special Chars` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Two-Word Company Names (Marine/Wind)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `General Company with Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches generic company names ending in GmbH, AG, or OG. Explicitly handles 'GMBH' (uppercase) and ensures word boundaries. Updated to be more robust with special characters.

**Content:**
```
(?<!\w)(?<!durch\s)(?<!die\s)(?<!der\s)(?<!des\s)(?<!bei\sder\s)(?<!bei\sdem\s)(?<!bei\sden\s)(?<!Betriebspr\u00fcfung\s)(?<!\s)(?<!\s)(?<!\s)([A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df][A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\s\.\&\-\+\u00fc\u00f6\u00e4\u00c4\u00d6\u00DC]{1,40})(?:GmbH?\b|AG\b|OG\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 244 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_38`)


Nach § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `Ob eine Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_115`)


Das FLAG 1967 selbst enthält keine  abschließende Definition eines Studienwechsels.

**False Positives:**

- `Das FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Wirtschaftsprüfung Steuerberatung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Specific Private Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in GmbH/AG/OG, such as SüdVersand and Raiffeisenbank. Updated to ensure strict boundaries.

**Content:**
```
\b(S\u00fcdVersand|Raiffeisenbank\s+Wels\s+S\u00fcd|TraunLuftfahrt\s+Solutions)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (No Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in standard suffixes like GmbH/AG, based on training data.

**Content:**
```
\b(Textil\s+Steingartlog|Keltrizor\s+Handel|DLCG\s+Bildung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (With Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that include 'GMBH' or 'GmbH' but have unique prefixes.

**Content:**
```
\b(Hudec&Christian\s+Immobilien\s+GMBH|Hendrick\s+Recycling\s+GMBH|Stefansky\s+Bau\s+GMBH)\b
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
**Description:**
Matches the specific company name 'Reinemut + Smoch Handel'.

**Content:**
```
Reinemut\s+\+\s+Smoch\s+Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt' and 'FA Salzburg-Stadt' variations.

**Content:**
```
\b(?:Finanzamt|FA)\s+Salzburg\-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt URL`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the URL variant 'www.FA Salzburg-Stadt'.

**Content:**
```
www\.FA\s+Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Triloglex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Triloglex GMBH.

**Content:**
```
\bTriloglex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company MittelHeizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name MittelHeizung Werke AG.

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

## `Specific Company Rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Rosilius Pflege AG.

**Content:**
```
\bRosilius\s+Pflege\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Yavasoglu Analyse AG.

**Content:**
```
\bYavasoglu\s+Analyse\s+AG\b
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

## `Finanzamt and FA Districts`

**F1:** 0.031 | **Precision:** 1.000 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt', 'FA', or 'www.FA' followed by specific Austrian district names. Updated to capture 'www.' prefix.

**Content:**
```
\b(?:www\.)?(?:Finanzamt|FA)\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Salzburg-Stadt|Salzburg-Land|Oststeiermark|Tirol\s+Ost|Nieder\u00f6sterreich\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Innsbruck|Klosterneuburg|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Bruck\s+Leoben\s+M\u00fcrzzuschlag|Linz|Baden\s+M\u00f6dling|Freistadt\s+Rohrbach\s+Urfahr|Wien\s+1/23|Wien\s+2/20/21/22|Amstetten\s+Melk\s+Scheibbs|Graz-Stadt|Judenburg\s+Liezen|Lilienfeld\s+St\.\s+P\u00f6lten|Grieskirchen\s+Wels|Deutschlandsberg\s+Leibnitz\s+Voitsberg)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.016 | 0.031 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 252 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

</details>

---

## `Specific Private Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in GmbH/AG/OG, such as SüdVersand and Raiffeisenbank. Updated to ensure strict boundaries.

**Content:**
```
\b(S\u00fcdVersand|Raiffeisenbank\s+Wels\s+S\u00fcd|TraunLuftfahrt\s+Solutions)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (No Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in standard suffixes like GmbH/AG, based on training data.

**Content:**
```
\b(Textil\s+Steingartlog|Keltrizor\s+Handel|DLCG\s+Bildung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (With Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that include 'GMBH' or 'GmbH' but have unique prefixes.

**Content:**
```
\b(Hudec&Christian\s+Immobilien\s+GMBH|Hendrick\s+Recycling\s+GMBH|Stefansky\s+Bau\s+GMBH)\b
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
**Description:**
Matches the specific company name 'Reinemut + Smoch Handel'.

**Content:**
```
Reinemut\s+\+\s+Smoch\s+Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt' and 'FA Salzburg-Stadt' variations.

**Content:**
```
\b(?:Finanzamt|FA)\s+Salzburg\-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt URL`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the URL variant 'www.FA Salzburg-Stadt'.

**Content:**
```
www\.FA\s+Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Triloglex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Triloglex GMBH.

**Content:**
```
\bTriloglex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company MittelHeizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name MittelHeizung Werke AG.

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

## `Specific Company Rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Rosilius Pflege AG.

**Content:**
```
\bRosilius\s+Pflege\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Yavasoglu Analyse AG.

**Content:**
```
\bYavasoglu\s+Analyse\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity Zoruniglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity Zoruniglanz.

**Content:**
```
\bZoruniglanz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity Sophie Wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity Sophie Wittmeir (labeled as organisation in training data).

**Content:**
```
\bSophie\s+Wittmeir\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Klusner`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Klusner&P\u00e4ffgen Bildung GMBH' which contains an ampersand.

**Content:**
```
\bKlusner\&P\u00e4ffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Tschermack`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Tschermack Pharma GMBH'.

**Content:**
```
\bTschermack\s+Pharma\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company TalVerverwerk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'TalVerverwerkGarten GMBH' and its ellipsis variant.

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

## `Specific Company SudLandwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'S\u00fcd-Landwirtschaft'.

**Content:**
```
\bS\u00fcd\-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known compound company names with hyphens or specific structures that the generic rule misses.

**Content:**
```
\b(?:Dongartcon\-Landwirtschaft|Monlogtri\-Analyse|RheinMetall\s+Technologien|Logseemon\-Metall|Gumpold\s+Technik)\s+(?:GMBH|AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Bank and Other Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known company names like VOLKSBANK WIEN, Conwil-Marine, Tal-Druck, DIAS Telekom Institut.

**Content:**
```
\b(?:VOLKSBANK\s+WIEN|Conwil\-Marine|Tal\-Druck|DIAS\s+Telekom\s+Institut)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `General Company with Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches generic company names ending in GmbH, AG, or OG. Explicitly handles 'GMBH' (uppercase) and ensures word boundaries. Updated to be more robust with special characters.

**Content:**
```
(?<!\w)(?<!durch\s)(?<!die\s)(?<!der\s)(?<!des\s)(?<!bei\sder\s)(?<!bei\sdem\s)(?<!bei\sden\s)(?<!Betriebspr\u00fcfung\s)(?<!\s)(?<!\s)(?<!\s)([A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df][A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\s\.\&\-\+\u00fc\u00f6\u00e4\u00c4\u00d6\u00DC]{1,40})(?:GmbH?\b|AG\b|OG\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 244 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_38`)


Nach § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `Ob eine Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_115`)


Das FLAG 1967 selbst enthält keine  abschließende Definition eines Studienwechsels.

**False Positives:**

- `Das FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Wirtschaftsprüfung Steuerberatung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_15`)


Die genannten Beträge seien bei der GmbH als uneinbringlich anzusehen.

**False Positives:**

- `Die genannten Beträge seien bei der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_19`)


Sofern die GmbH bereits ab den jeweiligen Fälligkeitstagen der Abgaben nicht mehr über  ausreichende liquide Mittel zur (vollen) Bezahlung aller Verbindlichkeiten verfügt habe, werde  der Bf. ersucht, dies durch eine Auflistung sämtlicher Gläubiger ab dem Zeitpunkt der  Abgabenfälligkeit gleichzeitig oder früher fällig gewordenen Forderungen darzulegen.

**False Positives:**

- `Sofern die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_42`)


Zur Stellung als Vertreter führte das Finanzamt in der Begründung aus, dass der Bf. von  22.06.2001 bis zur Insolvenzeröffnung der Primärschuldnerin (in weiterer Folge kurz GmbH) im  Firmenbuch als handelsrechtlicher Geschäftsführer der GmbH eingetragen gewesen sei.

**False Positives:**

- `in weiterer Folge kurz GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_43`)


Somit  sei er Vertreter der GmbH im Sinne der §§ 9 und 80 BAO.

**False Positives:**

- `Somit  sei er Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Ihm als Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Specific Legal Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific organization names found in the training data and failure cases, excluding the Finanzamt entries which are covered by the general rule.

**Content:**
```
\b(?:Milan\s+H\u00e4ndlein|Manfredo\s+Herrschmann|Englert\s+M\u00f6bel|Laskowsky\s+Umwelt|Annemie\s+Bott|StadtEnergie\s+Holding|Krolitzki\s+Beratung|Butkus\s+Metall|Keldonbach\s+Sicherheit\s+GMBH|TraunChemie\s+GMBH|G\u00f6zc\u00fc\s+Getr\u00e4nke|Lubomir\s+Merschmeyer|Roelfsen\s+Versicherung|H\u00f6rup\s+Gastronomie\s+AG|Houdek\s+Maschinenbau|Dorfcon-Verlag|Dammke\s+KI\s+GMBH|Naa\u00df\s+Elektro\s+GMBH|Bersud\s+M\u00f6bel\s+GMBH|Unter\s+Heimdorf\s+GMBH|Kornfelder\s+Recycling|WXE\s+Textil\s+GMBH|Obern\u00f6der\+K\u00fcsbert\s+Touristik\s+GMBH|Talost\s+GMBH|S\u00fcdEvent\s+AG|Kudla&K\u00fchnel\s+Solar|Logal\s+Gruppe|Hempel\s+Heizung\s+GMBH|Dorfkraft-Sanit\u00e4r\s+AG|ZYJY\s+Automotive\s+AG|NYJ\s+Event\s+AG|Kubzyk\s+Elektro\s+AG|L\u00fctkehans\s+Event\s+GMBH|InnLuftfahrt\s+GMBH|Depp\s+Versand|G\u00f6zc\u00fc\s+Getr\u00e4nke|Roelfsen\s+Versicherung|H\u00f6rup\s+Gastronomie\s+AG|Houdek\s+Maschinenbau|Dorfcon-Verlag|Dammke\s+KI\s+GMBH|Naa\u00df\s+Elektro\s+GMBH|Bersud\s+M\u00f6bel\s+GMBH|Unter\s+Heimdorf\s+GMBH|Kornfelder\s+Recycling|WXE\s+Textil\s+GMBH|Obern\u00f6der\+K\u00fcsbert\s+Touristik\s+GMBH|Talost\s+GMBH|S\u00fcdEvent\s+AG|Kudla&K\u00fchnel\s+Solar|Logal\s+Gruppe|Hempel\s+Heizung\s+GMBH|Dorfkraft-Sanit\u00e4r\s+AG|ZYJY\s+Automotive\s+AG|NYJ\s+Event\s+AG|Kubzyk\s+Elektro\s+AG|L\u00fctkehans\s+Event\s+GMBH|InnLuftfahrt\s+GMBH|Depp\s+Versand)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Versicherung Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Versicherung entities like 'Roelfsen Versicherung'.

**Content:**
```
(?<!\w)[A-Za-zÄÖÜäöüß]+\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific IT Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches IT entities like 'Lexdon IT'

**Content:**
```
(?<!\w)[A-Za-zäöüÄÖÜß]+\s+IT
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Verlag Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Verlag entities like 'Dorfcon-Verlag'

**Content:**
```
(?<!\w)[A-Za-zäöüÄÖÜß\-]+\s*Verlag
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Maschinenbau Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Maschinenbau entities like 'Houdek Maschinenbau'.

**Content:**
```
(?<!\w)[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df]+\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Luftfahrt Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Luftfahrt entities like 'Schmeltz Luftfahrt'.

**Content:**
```
(?<!\w)[A-Za-zÄÖÜäöüß]+\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Finanzamt Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt entities like 'Finanzamt Wien 1/23' with precise boundaries, stopping before common prepositions or verbs.

**Content:**
```
(?<!\w)Finanzamt\s+(?:Wien\s+\d+/\d+|\w+\s+\d+/\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Named Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known entities that do not follow standard patterns: Trafenfen Automotive, DrauFinanzen, Kelgart-Druck, Bezirksgericht Zell am See.

**Content:**
```
\b(?:Trafenfen\s+Automotive|DrauFinanzen|Kelgart-Druck|Bezirksgericht\s+Zell\s+am\s+See)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KG Company Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in KG. Strictly excludes preceding prepositions like 'der', 'bei der', 'an die' to prevent over-matching.

**Content:**
```
(?<!\w)(?<!durch\s)(?<!die\s)(?<!der\s)(?<!des\s)(?<!bei\sder\s)(?<!bei\sdem\s)(?<!bei\sden\s)(?<!an\sdie\s)(?<!an\sdem\s)(?<!an\sden\s)(?<!bei\s)(?<!in\s)(?<!von\s)([A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df][A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\s\.\&\-\+\u00fc\u00f6\u00e4\u00c4\u00d6\u00DC]{1,40})(?:KG\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not fit the generic pattern or have specific capitalization/spacing issues.

**Content:**
```
\b(?:Chen Setzekorn|Istvan Gerart|InnMarine GMBH|HochLebensmittel Holding GMBH|Ostgart AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Trade Names (No Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known trade names that appear without their legal suffix in the ground truth, prioritizing them over generic suffix rules.

**Content:**
```
\b(?:Kök\s+&\s+Heberlein\s+Bau|Leiss\s+Software|Okur\s+Automotive|Celikkanat\s+Garten|RheinDigital|Getränke\s+Nexdorfzor\s+GMBH|Depp\s+Versand)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GmbH & Partner KG Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific 'GmbH & Partner KG' patterns which are common in legal texts for law firms or tax advisors.

**Content:**
```
(?<!\w)([A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß\s\.\&\-]+?)(?:GmbH\s+&\s+Partner\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank Locations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures Raiffeisenbank entities followed by location names. Strictly bounded to prevent matching trailing verbs or prepositions.

**Content:**
```
\bRaiffeisenbank\s+[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df]+)*(?:\s+Bankstelle\s+[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\.]+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WaldTouristik Technologies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule for 'WaldTouristik Technologien' which appears frequently in the training data and is a unique name.

**Content:**
```
\bWaldTouristik\s+Technologien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Legal Case Organization Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures organization names in 'in der Beschwerdesache' context, specifically looking for names with suffixes (GmbH, AG) or compound structures (u., +) to avoid matching personal names.

**Content:**
```
(?:in der Beschwerdesache der|in der Beschwerdesache des)\s+([A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df][A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\s\.\&\-\+\u00fc\u00f6\u00e4\u00c4\u00d6\u00DC]+?(?:GmbH?|AG|u\.|\+)[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\s\.\&\-\+\u00fc\u00f6\u00e4\u00c4\u00d6\u00DC]+?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bank and Institute Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures specific bank or institute names that might not have standard suffixes or are long compound names, e.g., 'Raiffeisen ... in Tirol', 'Inn-Recycling Institut'.

**Content:**
```
(?:Inn\-Recycling\s+Institut|Raiffeisen\s+[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df]+\s+(?:Bank|in\s+Tirol))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Court Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific court names found in the text.

**Content:**
```
\b(?:Bezirksgericht Silz|LG Innsbruck|Landesgericht Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific GMBH Names with Special Chars`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known company names containing '&' or 'u.' followed by GMBH.

**Content:**
```
(?:Zschieschank&Hee\u00df Transport|M\u00fcllbrandt u\. Worthmeier Digital|Ober\-Chemie) GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Two-Word Company Names (Marine/Wind)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific two-word company names like 'Logkeltal Marine' and 'Nowothnig Wind' that lack standard suffixes.

**Content:**
```
\b(?:Logkeltal Marine|Nowothnig Wind|S\u00fcd Sudwil)\b
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

