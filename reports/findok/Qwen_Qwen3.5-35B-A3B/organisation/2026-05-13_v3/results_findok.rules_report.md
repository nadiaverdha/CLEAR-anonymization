# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-13T10:39:42.240636

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-13_v3/config.yaml 
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
| Max rules | 25 |
| Max samples in prompt | 60 |
| Refinement iterations | 0 |
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
| Accuracy (exact match) | 82.5% |
| True Positives | 3 |
| False Positives | 36 |
| False Negatives | 253 |
| Total Gold Entities | 256 |
| Micro Precision | 7.7% |
| Micro Recall | 1.2% |
| Micro F1 | 2.0% |
| Macro F1 | 2.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Finanzamt Entities` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `Finanzamt Entities Expanded` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `Company Handel/Bildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Beratung Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `E-Commerce Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Versicherung Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Maschinenbau Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verlag Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `IT Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company KI GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hyphenated Company GMBH` | 0.0% | 0.0% | 0.0% | 36 | 0 | 36 |
| `Specific KG Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Luftfahrt Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company GMBH with Und` | 0.0% | 0.0% | 0.0% | 36 | 0 | 36 |
| `Specific EnnsBildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Inn-Recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bank in Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Chen Setzekorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Istvan Gerart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific InnMarine GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific HochLebensmittel Holding GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Bezirksgericht Silz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific LG Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Landesgericht Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Logkeltal Marine` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Zschieschank Transport` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Mullbrandt Digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific OberChemie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Grieskirchen Wels Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Hyphenated Company GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in GMBH/AG/OG, ensuring the match is a company name and not a phrase ending in GmbH.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&\-]*?(?:GmbH?|AG|OG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 36 | 0 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 36 | 250 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_38`)


Nach § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_48`)


§ 26 Abs. 1 FLAG 1967 normiert eine objektive Erstattungspflicht desjenigen, der die  Familienbeihilfe zu Unrecht bezogen hat.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_51`)


Gemäß § 33 Abs. 3 EStG 1988 ist für zu Unrecht bezogene Kinderabsetzbeträge § 26 FLAG 1967  anzuwenden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Company GMBH with Und`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in GMBH/AG/OG, ensuring no preceding German articles or prepositions are included. Tightened to avoid matching long sentences and partial names.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&\-]*?(?:GmbH?|AG|OG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 36 | 0 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 36 | 250 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_38`)


Nach § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_48`)


§ 26 Abs. 1 FLAG 1967 normiert eine objektive Erstattungspflicht desjenigen, der die  Familienbeihilfe zu Unrecht bezogen hat.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_51`)


Gemäß § 33 Abs. 3 EStG 1988 ist für zu Unrecht bezogene Kinderabsetzbeträge § 26 FLAG 1967  anzuwenden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Company Handel/Bildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Handel' or 'Bildung', strictly bounded to prevent crossing word boundaries.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?(?:Handel|Bildung))(?=\s*(?:GmbH?|AG|OG|\.|,|\)|\]|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Beratung Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Beratung' (Consultancy).

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?Beratung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `E-Commerce Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'E-Commerce' or 'E‑Commerce'.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?E(?:-|\u2011)Commerce)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Versicherung Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Versicherung, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?Versicherung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Maschinenbau Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Maschinenbau, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?Maschinenbau)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verlag Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Verlag.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?Verlag)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `IT Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in IT, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?IT)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Company KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in KI GMBH to catch specific cases like Wildorftra KI GMBH.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s]*?KI\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific KG Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific KG entities like Schoenfelder Textil KG, ensuring strict word boundaries to avoid capturing preceding context.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\-]*?KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Luftfahrt Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Luftfahrt followed by GMBH/AG, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?Luftfahrt\s+(?:GmbH?|AG))\b
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

## `Finanzamt Entities`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches Finanzamt entities with specific known location names, stopping before prepositions or dates.

**Content:**
```
\b(Finanzamt|FA)\s+(?:Judenburg Liezen|St\.\s*Johann\s*Tamsweg\s*Zell\s*am\s*See|Spittal\s*Villach|Braunau\s*Ried\s*Sch\u00e4rding|Kirchdorf\s*Perg\s*Steyr|Baden\s*M\u00f6dling|Purkersdorf|Innsbruck|Linz|Landeck\s*Reutte)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 31 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

</details>

---

## `Finanzamt Entities Expanded`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches Finanzamt entities with expanded known location names including Tirol Ost, Salzburg-Land, Waldviertel, Deutschlandsberg Leibnitz Voitsberg, Wien 8/16/17, Wien 2/20/21/22, Freistadt Rohrbach Urfahr, Oststeiermark, and Purkersdorf.

**Content:**
```
\b(Finanzamt|FA)\s+(?:Judenburg Liezen|St\.\s*Johann\s*Tamsweg\s*Zell\s*am\s*See|Spittal\s*Villach|Braunau\s*Ried\s*Sch\u00e4rding|Kirchdorf\s*Perg\s*Steyr|Baden\s*M\u00f6dling|Purkersdorf|Innsbruck|Linz|Landeck\s*Reutte|Tirol\s*Ost|Salzburg\-Land|Waldviertel|Deutschlandsberg\s*Leibnitz\s*Voitsberg|Wien\s*8/16/17|Wien\s*2/20/21/22|Freistadt\s*Rohrbach\s*Urfahr|Oststeiermark)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 31 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

</details>

---

## `Company Handel/Bildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Handel' or 'Bildung', strictly bounded to prevent crossing word boundaries.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?(?:Handel|Bildung))(?=\s*(?:GmbH?|AG|OG|\.|,|\)|\]|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Beratung Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Beratung' (Consultancy).

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?Beratung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `E-Commerce Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'E-Commerce' or 'E‑Commerce'.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?E(?:-|\u2011)Commerce)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Versicherung Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Versicherung, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?Versicherung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Maschinenbau Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Maschinenbau, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?Maschinenbau)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verlag Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Verlag.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&]*?Verlag)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `IT Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in IT, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?IT)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Company KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in KI GMBH to catch specific cases like Wildorftra KI GMBH.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s]*?KI\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hyphenated Company GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in GMBH/AG/OG, ensuring the match is a company name and not a phrase ending in GmbH.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\+&\-]*?(?:GmbH?|AG|OG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 36 | 0 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 36 | 250 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_38`)


Nach § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_48`)


§ 26 Abs. 1 FLAG 1967 normiert eine objektive Erstattungspflicht desjenigen, der die  Familienbeihilfe zu Unrecht bezogen hat.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_51`)


Gemäß § 33 Abs. 3 EStG 1988 ist für zu Unrecht bezogene Kinderabsetzbeträge § 26 FLAG 1967  anzuwenden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `Ob eine Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_6`)


Aufgrund eines Arbeitsauftrages vom 21.05.2021 kam es zu einer Überprüfung des  Familienbeihilfe-Anspruches der Beschwerdeführerin (=Bf.) bezüglich ihrer Tochter  Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum, da zunächst aufgrund der COVID-Pandemie  sowohl Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt worden waren.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_50`)


Mit Vorlagebericht vom 26.07.2022 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und führte dazu aus:  „Sachverhalt:  Aufgrund eines Arbeitsauftrages vom 21.05.2021 sollte der Familienbeihilfe-Anspruch der  Beschwerdeführerin bezüglich ihrer Tochter Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum  überprüft werden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_115`)


Das FLAG 1967 selbst enthält keine  abschließende Definition eines Studienwechsels.

**False Positives:**

- `Das FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_122`)


Nach § 26 Abs. 1 FLAG 1967 idF. BGBl. I Nr. 104/2019 hat, wer Familienbeihilfe zu Unrecht  bezogen hat, die entsprechenden Beträge zurückzuzahlen.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_125`)


Dieser  Studienwechsel erfülle den Tatbestand des § 17 Abs. 1 Z 2 StudFG, weshalb ein günstiger  Studienerfolg, wie ihn § 2 Abs. 1 lit. b FLAG für die Gewährung der Familienbeihilfe fordere,  nicht vorliege.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_131`)


Ein Studienwechsel im Sinn des § 2 Abs. 1 lit. b FLAG, der beim Wechsel vom Studium einer  Studienrichtung zum Studium einer anderen Studienrichtung vorliegt, ist daher vom Wechsel  der Studieneinrichtung zu unterscheiden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_132`)


So unterscheidet der Verwaltungsgerichtshof zu § 2  Abs. 1 lit. b vorletzter Satz FLAG ausdrücklich zwischen dem Wechsel der Einrichtung und dem  Wechsel des Studiums.

**False Positives:**

- `Satz FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Steuerberatung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mandl & Mitterbauer GmbH` — partial — pred is substring of gold: `Anwälte Mandl & Mitterbauer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_13`)


In dieser Funktion als Geschäftsführer sei ihm die Wahrnehmung der  abgabenrechtlichen Verpflichtungen der GmbH oblegen.

**False Positives:**

- `Wahrnehmung der  abgabenrechtlichen Verpflichtungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_19`)


Sofern die GmbH bereits ab den jeweiligen Fälligkeitstagen der Abgaben nicht mehr über  ausreichende liquide Mittel zur (vollen) Bezahlung aller Verbindlichkeiten verfügt habe, werde  der Bf. ersucht, dies durch eine Auflistung sämtlicher Gläubiger ab dem Zeitpunkt der  Abgabenfälligkeit gleichzeitig oder früher fällig gewordenen Forderungen darzulegen.

**False Positives:**

- `Sofern die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_28`)


der Nichterbringung dieser Nachweise müsse das Finanzamt davon ausgehen, dass der Bf. die  ihm obliegende Verpflichtung, die fällig gewordenen Abgaben aus den verwaltenden Mitteln  zu entrichten, schuldhaft verletzt habe, und diese Pflichtverletzung auch ursächlich für den  Abgabenausfall bei der GmbH sei.

**False Positives:**

- `Abgabenausfall bei der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_30`)


Werde der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liege es im Ermessen des Finanzamtes, die Haftung für die genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

**False Positives:**

- `Verbindlichkeiten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_42`)


Zur Stellung als Vertreter führte das Finanzamt in der Begründung aus, dass der Bf. von  22.06.2001 bis zur Insolvenzeröffnung der Primärschuldnerin (in weiterer Folge kurz GmbH) im  Firmenbuch als handelsrechtlicher Geschäftsführer der GmbH eingetragen gewesen sei.

**False Positives:**

- `Folge kurz GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_43`)


Somit  sei er Vertreter der GmbH im Sinne der §§ 9 und 80 BAO.

**False Positives:**

- `Somit  sei er Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_46`)


Diese offenen Forderungen seien auch im Konkurs der GmbH anerkannt worden.

**False Positives:**

- `Diese offenen Forderungen seien auch im Konkurs der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_47`)


Somit  bestehe eine Abgabenforderung gegen die GmbH.

**False Positives:**

- `Somit  bestehe eine Abgabenforderung gegen die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_89`)


Es sei daher davon auszugehen, dass Mittel  der GmbH zur Verfügung gestanden seien, um die Verbindlichkeiten zu bezahlen, und dass die  vorhandenen Mittel nicht im gleichen Verhältnis zur Befriedigung der Schulden eingesetzt  worden seien.

**False Positives:**

- `Mittel  der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_91`)


Durch die Nichtbeachtung dieses  Grundsatzes für die Umsatzsteuer, den Dienstgeberbeitrag, den Zuschlag zum  Dienstgeberbeitrag und die Körperschaftsteuer habe der Bf. seine abgabenrechtlichen  Pflichten als Vertreter der GmbH verletzt.

**False Positives:**

- `Pflichten als Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Ihm als Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_100`)


Die Unterlassung der Abfuhr der Lohnsteuer stellt eine schuldhafte Verletzung der  abgabenrechtlichen Pflichten als Vertreter der GmbH dar.

**False Positives:**

- `Die Unterlassung der Abfuhr der Lohnsteuer stellt eine schuldhafte Verletzung der  abgabenrechtlichen Pflichten als Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_106`)


Die Unterlassung der Abfuhr der Kapitalertragsteuer stelle eine schuldhafte Verletzung  abgabenrechtlichen Pflichten des Bf. als Vertreter der GmbH dar   Betreffend das Verschulden des Vertreters erläuterte das Finanzamt, dass Verletzungen  abgabenrechtlicher Pflichten nur dann zur Haftungsinanspruchnahme berechtigten, wenn die  Verletzung schuldhaft erfolgt sei.

**False Positives:**

- `Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_148`)


Wie bereits im Haftungsbescheid vom 11.01.2016 ausgeführt, obliege dem Vertreter der GmbH  der Nachweis, welcher Betrag bei Gleichbehandlung sämtlicher Gläubiger bezogen auf die  jeweiligen Fälligkeitszeitpunkte einerseits und das Vorhandensein liquider Mittel andererseits  an die Abgabenbehörde zu entrichten gewesen wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_177`)


Diese offenen Forderungen sind auch im Insolvenzverfahren der GmbH anerkannt worden.

**False Positives:**

- `Diese offenen Forderungen sind auch im Insolvenzverfahren der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_178`)


Somit besteht eine Abgabenforderung gegen die GmbH.

**False Positives:**

- `Somit besteht eine Abgabenforderung gegen die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_64`)


9. Bei der Normverbrauchsabgabe hat in den Fällen des innergemeinschaftlichen Erwerbs  durch Private der Abgabenschuldner spätestens einen Monat ab der Zulassung bzw. dem Tag  des Erwerbs (Fälligkeitstag) eine Anmeldung einzureichen, in der er den zu entrichtenden  Betrag selbst zu berechnen hat (§ 11 Abs. 3 NoVAG 1991;

**False Positives:**

- `NoVAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Specific KG Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific KG entities like Schoenfelder Textil KG, ensuring strict word boundaries to avoid capturing preceding context.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s\-]*?KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Luftfahrt Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in Luftfahrt followed by GMBH/AG, ensuring no preceding German articles or prepositions are included.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&]*?Luftfahrt\s+(?:GmbH?|AG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Company GMBH with Und`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in GMBH/AG/OG, ensuring no preceding German articles or prepositions are included. Tightened to avoid matching long sentences and partial names.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s\+&\-]*?(?:GmbH?|AG|OG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 36 | 0 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 36 | 250 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_38`)


Nach § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_48`)


§ 26 Abs. 1 FLAG 1967 normiert eine objektive Erstattungspflicht desjenigen, der die  Familienbeihilfe zu Unrecht bezogen hat.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_51`)


Gemäß § 33 Abs. 3 EStG 1988 ist für zu Unrecht bezogene Kinderabsetzbeträge § 26 FLAG 1967  anzuwenden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `Ob eine Berufsausbildung im Sinne des FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_6`)


Aufgrund eines Arbeitsauftrages vom 21.05.2021 kam es zu einer Überprüfung des  Familienbeihilfe-Anspruches der Beschwerdeführerin (=Bf.) bezüglich ihrer Tochter  Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum, da zunächst aufgrund der COVID-Pandemie  sowohl Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt worden waren.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_50`)


Mit Vorlagebericht vom 26.07.2022 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und führte dazu aus:  „Sachverhalt:  Aufgrund eines Arbeitsauftrages vom 21.05.2021 sollte der Familienbeihilfe-Anspruch der  Beschwerdeführerin bezüglich ihrer Tochter Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum  überprüft werden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_115`)


Das FLAG 1967 selbst enthält keine  abschließende Definition eines Studienwechsels.

**False Positives:**

- `Das FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_122`)


Nach § 26 Abs. 1 FLAG 1967 idF. BGBl. I Nr. 104/2019 hat, wer Familienbeihilfe zu Unrecht  bezogen hat, die entsprechenden Beträge zurückzuzahlen.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_125`)


Dieser  Studienwechsel erfülle den Tatbestand des § 17 Abs. 1 Z 2 StudFG, weshalb ein günstiger  Studienerfolg, wie ihn § 2 Abs. 1 lit. b FLAG für die Gewährung der Familienbeihilfe fordere,  nicht vorliege.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_131`)


Ein Studienwechsel im Sinn des § 2 Abs. 1 lit. b FLAG, der beim Wechsel vom Studium einer  Studienrichtung zum Studium einer anderen Studienrichtung vorliegt, ist daher vom Wechsel  der Studieneinrichtung zu unterscheiden.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_132`)


So unterscheidet der Verwaltungsgerichtshof zu § 2  Abs. 1 lit. b vorletzter Satz FLAG ausdrücklich zwischen dem Wechsel der Einrichtung und dem  Wechsel des Studiums.

**False Positives:**

- `Satz FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Steuerberatung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mandl & Mitterbauer GmbH` — partial — pred is substring of gold: `Anwälte Mandl & Mitterbauer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_13`)


In dieser Funktion als Geschäftsführer sei ihm die Wahrnehmung der  abgabenrechtlichen Verpflichtungen der GmbH oblegen.

**False Positives:**

- `Wahrnehmung der  abgabenrechtlichen Verpflichtungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_19`)


Sofern die GmbH bereits ab den jeweiligen Fälligkeitstagen der Abgaben nicht mehr über  ausreichende liquide Mittel zur (vollen) Bezahlung aller Verbindlichkeiten verfügt habe, werde  der Bf. ersucht, dies durch eine Auflistung sämtlicher Gläubiger ab dem Zeitpunkt der  Abgabenfälligkeit gleichzeitig oder früher fällig gewordenen Forderungen darzulegen.

**False Positives:**

- `Sofern die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_28`)


der Nichterbringung dieser Nachweise müsse das Finanzamt davon ausgehen, dass der Bf. die  ihm obliegende Verpflichtung, die fällig gewordenen Abgaben aus den verwaltenden Mitteln  zu entrichten, schuldhaft verletzt habe, und diese Pflichtverletzung auch ursächlich für den  Abgabenausfall bei der GmbH sei.

**False Positives:**

- `Abgabenausfall bei der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_30`)


Werde der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liege es im Ermessen des Finanzamtes, die Haftung für die genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

**False Positives:**

- `Verbindlichkeiten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_42`)


Zur Stellung als Vertreter führte das Finanzamt in der Begründung aus, dass der Bf. von  22.06.2001 bis zur Insolvenzeröffnung der Primärschuldnerin (in weiterer Folge kurz GmbH) im  Firmenbuch als handelsrechtlicher Geschäftsführer der GmbH eingetragen gewesen sei.

**False Positives:**

- `Folge kurz GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_43`)


Somit  sei er Vertreter der GmbH im Sinne der §§ 9 und 80 BAO.

**False Positives:**

- `Somit  sei er Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_46`)


Diese offenen Forderungen seien auch im Konkurs der GmbH anerkannt worden.

**False Positives:**

- `Diese offenen Forderungen seien auch im Konkurs der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_47`)


Somit  bestehe eine Abgabenforderung gegen die GmbH.

**False Positives:**

- `Somit  bestehe eine Abgabenforderung gegen die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_89`)


Es sei daher davon auszugehen, dass Mittel  der GmbH zur Verfügung gestanden seien, um die Verbindlichkeiten zu bezahlen, und dass die  vorhandenen Mittel nicht im gleichen Verhältnis zur Befriedigung der Schulden eingesetzt  worden seien.

**False Positives:**

- `Mittel  der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_91`)


Durch die Nichtbeachtung dieses  Grundsatzes für die Umsatzsteuer, den Dienstgeberbeitrag, den Zuschlag zum  Dienstgeberbeitrag und die Körperschaftsteuer habe der Bf. seine abgabenrechtlichen  Pflichten als Vertreter der GmbH verletzt.

**False Positives:**

- `Pflichten als Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Ihm als Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_100`)


Die Unterlassung der Abfuhr der Lohnsteuer stellt eine schuldhafte Verletzung der  abgabenrechtlichen Pflichten als Vertreter der GmbH dar.

**False Positives:**

- `Die Unterlassung der Abfuhr der Lohnsteuer stellt eine schuldhafte Verletzung der  abgabenrechtlichen Pflichten als Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_106`)


Die Unterlassung der Abfuhr der Kapitalertragsteuer stelle eine schuldhafte Verletzung  abgabenrechtlichen Pflichten des Bf. als Vertreter der GmbH dar   Betreffend das Verschulden des Vertreters erläuterte das Finanzamt, dass Verletzungen  abgabenrechtlicher Pflichten nur dann zur Haftungsinanspruchnahme berechtigten, wenn die  Verletzung schuldhaft erfolgt sei.

**False Positives:**

- `Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_148`)


Wie bereits im Haftungsbescheid vom 11.01.2016 ausgeführt, obliege dem Vertreter der GmbH  der Nachweis, welcher Betrag bei Gleichbehandlung sämtlicher Gläubiger bezogen auf die  jeweiligen Fälligkeitszeitpunkte einerseits und das Vorhandensein liquider Mittel andererseits  an die Abgabenbehörde zu entrichten gewesen wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Vertreter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_177`)


Diese offenen Forderungen sind auch im Insolvenzverfahren der GmbH anerkannt worden.

**False Positives:**

- `Diese offenen Forderungen sind auch im Insolvenzverfahren der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_178`)


Somit besteht eine Abgabenforderung gegen die GmbH.

**False Positives:**

- `Somit besteht eine Abgabenforderung gegen die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_64`)


9. Bei der Normverbrauchsabgabe hat in den Fällen des innergemeinschaftlichen Erwerbs  durch Private der Abgabenschuldner spätestens einen Monat ab der Zulassung bzw. dem Tag  des Erwerbs (Fälligkeitstag) eine Anmeldung einzureichen, in der er den zu entrichtenden  Betrag selbst zu berechnen hat (§ 11 Abs. 3 NoVAG 1991;

**False Positives:**

- `NoVAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Specific EnnsBildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity EnnsBildung which might be missed by general patterns.

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

## `Specific Inn-Recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity Inn-Recycling Institut GMBH.

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

## `Bank in Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches bank names ending with 'in [Location]' like Raiffeisen Rionalbank Hall in Tirol.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s]*?Bank\s+in\s+[A-Z][a-zA-Z\s]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Chen Setzekorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Chen Setzekorn'.

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

## `Specific Istvan Gerart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Istvan Gerart'.

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

## `Specific InnMarine GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'InnMarine GMBH'.

**Content:**
```
\bInnMarine\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific HochLebensmittel Holding GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'HochLebensmittel Holding GMBH'.

**Content:**
```
\bHochLebensmittel\s+Holding\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Bezirksgericht Silz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific court 'Bezirksgericht Silz'.

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

## `Specific LG Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific court 'LG Innsbruck'.

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

## `Specific Landesgericht Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific court 'Landesgericht Innsbruck'.

**Content:**
```
\bLandesgericht\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Logkeltal Marine`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity Logkeltal Marine which lacks a standard suffix.

**Content:**
```
\bLogkeltal\s+Marine\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Zschieschank Transport`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization Zschieschank&Heeß Transport GMBH.

**Content:**
```
\bZschieschank&Hee\u00df\s+Transport\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Mullbrandt Digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization Müllbrandt u. Worthmeier Digital GMBH.

**Content:**
```
\bM\u00fcllbrandt\s+u\.\s+Worthmeier\s+Digital\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific OberChemie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization Ober-Chemie GMBH.

**Content:**
```
\bOber\-Chemie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Grieskirchen Wels Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt Grieskirchen Wels and its variations including www.FA Grieskirchen Wels found in training data.

**Content:**
```
(?:www\.)?(?:Finanzamt|FA)\s+Grieskirchen\s+Wels
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

