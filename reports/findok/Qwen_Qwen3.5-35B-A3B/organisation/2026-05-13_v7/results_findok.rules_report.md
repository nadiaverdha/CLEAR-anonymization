# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-13T22:45:45.621287

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-13_v7/config.yaml 
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
| Max samples in prompt | 20 |
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
| Accuracy (exact match) | 83.2% |
| True Positives | 3 |
| False Positives | 55 |
| False Negatives | 253 |
| Total Gold Entities | 256 |
| Micro Precision | 5.2% |
| Micro Recall | 1.2% |
| Micro F1 | 1.9% |
| Macro F1 | 1.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `tax_authority_finanzamt` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `tax_authority_fa` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `organisation_finanzamt` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `german_fa_city_abbreviations` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `company_sudversand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenbank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_traunluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_office_fa` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_office_finanzamt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_textil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_keltrizor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dlcg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hudec` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hendrick` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_stefansky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_www_fa_org` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_partnership_handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_salzburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_multi_district` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_single_district` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sophie_wittmeir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_triloglex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_zoruniglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mittelheizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rosilius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `private_company_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_legal_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_stadt` | 0.0% | 0.0% | 0.0% | 11 | 0 | 11 |
| `organisation_specific_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_specific_verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_legal_organisation_1` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_wien_waldnor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_botho_mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_fa_linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_fa_innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_kraftver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_gartgart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_nord_kellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_raiffeisenkasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_klein_vorholt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_gogel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_finanzamt_st_johann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_mur_ververzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_pastl_bachle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_specific_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_rheindigital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_depp_verkehr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_sudevent` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_innluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_lutkehans` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_dorfkraft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_obernoder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_talost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_specific_org_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_firma_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_suffix_refined` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `german_fa_purkersdorf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_tax_office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_specific_orgs` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_fa_abbreviation` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `german_hyphenated_company` | 0.0% | 0.0% | 0.0% | 41 | 0 | 41 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `german_hyphenated_company`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific hyphenated company names like 'Donau-Druck' that do not have a suffix.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9]+\-[A-Z][A-Za-z0-9]+)(?=\s*(?:,|\.|\)|\]|:|$|\s+\d|\s+\w))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 41 | 256 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Elisabeth-Platz` — partial — pred is substring of gold: `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`
- `Graz-Stadt` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Krankenpflege-Schule` — partial — pred is substring of gold: `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Barre-Syndrom` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_15`)


Unbeschadet dieses  Umstandes habe ich sämtliche Unterhaltskosten für meine Tochter Maximiliane Sakschewsky, MA, wie  bereits seit Ihren Aufenthaltswechsel im Jahr 2014 in das Vereinigte Königreich, im  Antragszeitraum noch EU-Mitgliedstaat, weiter getragen.

**False Positives:**

- `EU-Mitgliedstaat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Vereinigte Königreich`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_51`)


monatlich € 1.000,- an meine Ex-Gattin überwiesen, die als Schulgeld galten.

**False Positives:**

- `Ex-Gattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `organisation_stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches city/municipality entities starting with 'Stadt' followed by a proper name, ensuring it's not just a generic noun.

**Content:**
```
\bStadt\s+([A-Z][A-Za-z0-9\s]+(?:\s+[A-Z][A-Za-z0-9\s]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 11 | 128 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, MA 67`
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Stadt Wien ` — positional overlap with gold: `Magistrates der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

**False Positives:**

- `Stadt Wien als ` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

**False Positives:**

- `Stadt Wien dem Bf` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_23`)


Die Abgabe sei mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt  Wien vom 22.12.2005, Heft Nr. 51).

**False Positives:**

- `Stadt Wien vom 22` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_24`)


Abgabepflichtige, die ein mehrspuriges Fahrzeug in einer Kurzparkzone abstellen, hätten dafür  zu sorgen, dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und  richtig entwerteten Parkschein gekennzeichnet oder ein elektronischer Parkschein aktiviert sei  (§§ 3 Abs. 1 und 7 Abs. 1 der Kontrolleinrichtungenverordnung, Amtsblatt der Stadt Wien  Nr. 33/2008).

**False Positives:**

- `Stadt Wien  Nr` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'SüdVersand'.

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

## `company_raiffeisenbank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Raiffeisenbank Wels Süd'.

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

## `company_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'TraunLuftfahrt Solutions'.

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

## `tax_office_fa`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by city/district names (e.g., FA Wien 1/23, FA Innsbruck).

**Content:**
```
\bFA\s+(?:Wien\s+\d+/\d+|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_office_finanzamt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by city/district names.

**Content:**
```
\bFinanzamt\s+(?:Wien\s+1/23|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr|Feldkirch|Salzburg\-Land)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Textil Steingartlog'.

**Content:**
```
\bTextil\s+Steingartlog\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_keltrizor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Keltrizor Handel'.

**Content:**
```
\bKeltrizor\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_dlcg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DLCG Bildung'.

**Content:**
```
\bDLCG\s+Bildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hudec`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hudec&Christian Immobilien GMBH'.

**Content:**
```
\bHudec&Christian\s+Immobilien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hendrick`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hendrick Recycling GMBH'.

**Content:**
```
\bHendrick\s+Recycling\s+GMBH\b
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

## `tax_authority_finanzamt`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities starting with 'Finanzamt' or 'FA' followed by specific known location names.

**Content:**
```
\b(?:Finanzamt|FA)\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Spittal\s+Villach|Freistadt\s+Rohrbach\s+Urfahr)\b
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

## `organisation_finanzamt`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches tax authorities with known full location names. Updated to include Linz, Innsbruck, and ensure Oststeiermark/Judenburg Liezen are covered.

**Content:**
```
\b(?:Finanzamt|FA)\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Spittal\s+Villach|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Freistadt\s+Rohrbach\s+Urfahr|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Innsbruck|Klosterneuburg|Salzburg\-Land|Linz|Oststeiermark|Salzburg\-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Nieder\u00f6sterreich\s+Mitte)\b
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

## `tax_authority_fa`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities starting with 'FA' followed by specific known location names.

**Content:**
```
\bFA\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+Vöcklabruck|Braunau\s+Ried\s+Schärding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Spittal\s+Villach|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 33 |

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

</details>

---

## `german_fa_city_abbreviations`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'FA' abbreviations and full 'Finanzamt' names for specific regions. Consolidated to cover all tax office variations found in training data.

**Content:**
```
\b(?:FA\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Spittal\s+Villach|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Freistadt\s+Rohrbach\s+Urfahr|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Innsbruck|Klosterneuburg|Salzburg\-Land|Linz|Oststeiermark|Salzburg\-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Nieder\u00f6sterreich\s+Mitte)|Finanzamt\s+(?:Tirol\s+Ost|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Purkersdorf|Linz|Waldviertel))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 33 |

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

</details>

---

## `company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'SüdVersand'.

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

## `company_raiffeisenbank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Raiffeisenbank Wels Süd'.

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

## `company_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'TraunLuftfahrt Solutions'.

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

## `tax_office_fa`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by city/district names (e.g., FA Wien 1/23, FA Innsbruck).

**Content:**
```
\bFA\s+(?:Wien\s+\d+/\d+|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_office_finanzamt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by city/district names.

**Content:**
```
\bFinanzamt\s+(?:Wien\s+1/23|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr|Feldkirch|Salzburg\-Land)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Textil Steingartlog'.

**Content:**
```
\bTextil\s+Steingartlog\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_keltrizor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Keltrizor Handel'.

**Content:**
```
\bKeltrizor\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_dlcg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DLCG Bildung'.

**Content:**
```
\bDLCG\s+Bildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hudec`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hudec&Christian Immobilien GMBH'.

**Content:**
```
\bHudec&Christian\s+Immobilien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hendrick`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hendrick Recycling GMBH'.

**Content:**
```
\bHendrick\s+Recycling\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_stefansky`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Stefansky Bau GMBH'.

**Content:**
```
\bStefansky\s+Bau\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_www_fa_org`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific web URL variant 'www.FA Salzburg-Stadt'.

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

## `german_partnership_handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches legal partnership structures like 'Name + Name Handel' observed in 'Reinemut + Smoch Handel'.

**Content:**
```
([A-Z][a-z]+)\s*\+\s*([A-Z][a-z]+)\s+Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzamt_salzburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt' or 'FA Salzburg-Stadt' as a single entity.

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

## `german_finanzamt_multi_district`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt with multiple district names (e.g., Deutschlandsberg Leibnitz Voitsberg, Bruck Eisenstadt Oberwart).

**Content:**
```
\b(?:Finanzamt|FA)\s+(?:Deutschlandsberg\s+Leibnitz\s+Voitsberg|Bruck\s+Eisenstadt\s+Oberwart|Oststeiermark|Nieder\u00f6sterreich\s+Mitte|Tirol\s+Ost)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzamt_single_district`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt with specific known district combinations, including complex multi-word names and optional www. prefix.

**Content:**
```
\b(?:www\.|www)?(?:Finanzamt|FA)\s+(?:Innsbruck|Klosterneuburg|Salzburg\-Land|Vorarlberg|Amstetten\s+Melk\s+Scheibbs|Gmunden\s+V\u00f6cklabruck|Kirchdorf\s+Perg\s+Seyr|Schwechat\s+Gerasdorf|Waldviertel|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Steiermark\s+Mitte|Wien\s+\d+(?:/\d+)+|Wien\s+\d+/\d+|Salzburg\-Stadt|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Bruck\s+Eisenstadt\s+Oberwart|Grieskirchen\s+Wels|Freistadt\s+Rohrbach\s+Urfahr|Spittal\s+Villach)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_sophie_wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sophie Wittmeir' which appears as an organisation in the training data.

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

## `specific_company_triloglex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Triloglex GMBH'.

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

## `specific_company_zoruniglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Zoruniglanz'.

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

## `specific_company_mittelheizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'MittelHeizung Werke AG'.

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

## `specific_company_rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Rosilius Pflege AG'.

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

## `specific_company_yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Yavasoglu Analyse AG'.

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

## `private_company_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches private companies ending in GMBH, excluding Finanzamt patterns.

**Content:**
```
\b(?:(?:Tschermack\s+Pharma|Klusner\&P\u00e4ffgen\s+Bildung|TalVerverwerkGarten|ZFGQ\s+Pharma)\s+GMBH|S\u00fcd\-Landwirtschaft|Henken)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_legal_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known organisations from training data that lack standard suffixes or have unique structures.

**Content:**
```
\b(?:Gr\u00f6nemeier&H\u00f6velberndt\s+E\u2011Commerce|Annemie\s+Bott|Milan\s+H\u00e4ndlein|Krolitzki\s+Beratung|Manfredo\s+Herrschmann|FA\s+Grieskirchen\s+Wels|Finanzamt\s+Grieskirchen\s+Wels)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches insurance companies ending in 'Versicherung', ensuring no preceding word is part of the name.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s]+(?:\s+[A-Z][a-zA-Z0-9\s]+)*)\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches companies ending in 'Maschinenbau', ensuring no preceding word is part of the name.

**Content:**
```
(?<![A-Za-z])([A-Z][a-zA-Z0-9\s]+(?:\s+[A-Z][a-zA-Z0-9\s]+)*)\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches publishing houses ending in 'Verlag' or hyphenated 'Verlag'.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s&\-]+(?:\s+[A-Z][a-zA-Z0-9\s&\-]+)*)\s+Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches city/municipality entities starting with 'Stadt' followed by a proper name, ensuring it's not just a generic noun.

**Content:**
```
\bStadt\s+([A-Z][A-Za-z0-9\s]+(?:\s+[A-Z][A-Za-z0-9\s]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 11 | 128 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, MA 67`
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Stadt Wien ` — positional overlap with gold: `Magistrates der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

**False Positives:**

- `Stadt Wien als ` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

**False Positives:**

- `Stadt Wien dem Bf` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_23`)


Die Abgabe sei mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt  Wien vom 22.12.2005, Heft Nr. 51).

**False Positives:**

- `Stadt Wien vom 22` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_24`)


Abgabepflichtige, die ein mehrspuriges Fahrzeug in einer Kurzparkzone abstellen, hätten dafür  zu sorgen, dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und  richtig entwerteten Parkschein gekennzeichnet oder ein elektronischer Parkschein aktiviert sei  (§§ 3 Abs. 1 und 7 Abs. 1 der Kontrolleinrichtungenverordnung, Amtsblatt der Stadt Wien  Nr. 33/2008).

**False Positives:**

- `Stadt Wien  Nr` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `Stadt Wien als ` — positional overlap with gold: `Magistrat der Stadt Wien`
- `Stadt Wien bereits ` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

**False Positives:**

- `Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz` — positional overlap with gold: `Konservatorium  der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Musikhochschule Wien`(organisation)
- `Konservatorium  der Stadt Wien`(organisation)

</details>

---

## `organisation_specific_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific IT companies found in training data: Lexdon IT, Tritri-IT.

**Content:**
```
\b(?:Lexdon\s+IT|Tritri\-IT)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_specific_verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific Verlag companies found in training data: Dorfcon-Verlag.

**Content:**
```
\bDorfcon\-Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_legal_organisation_1`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known legal entities: Trafenfen Automotive, DrauFinanzen, Kelgart-Druck, Bezirksgericht Zell am See.

**Content:**
```
\b(?:Trafenfen\s+Automotive|DrauFinanzen|Kelgart\-Druck|Bezirksgericht\s+Zell\s+am\s+See)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_wien_waldnor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wien Waldnor KG' which was being truncated.

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

## `specific_organisation_botho_mikloweit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Botho Mikloweit' which is a person acting as an organisation in this context.

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

## `specific_organisation_fa_linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Linz' which was missing from the general Finanzamt rule.

**Content:**
```
\bFA\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_fa_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Innsbruck' which was missing from the general Finanzamt rule.

**Content:**
```
\bFA\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_kraftver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kraftver-Gastronomie GMBH' with hyphen handling.

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

## `specific_organisation_gartgart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gartgart Dienstleistungen GMBH'.

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

## `specific_organisation_nord_kellex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Nord Kellex'.

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

## `specific_organisation_raiffeisenkasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenkasse Retz-Pulkautal'.

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

## `specific_organisation_klein_vorholt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Klein-Vorholt KI GMBH'.

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

## `specific_organisation_gogel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gogel Daten GMBH'.

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

## `specific_organisation_finanzamt_st_johann`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt St. Johann Tamsweg Zell am See'.

**Content:**
```
\bFinanzamt\s+St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_mur_ververzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mur Ververzor Betriebe'.

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

## `specific_organisation_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Pastl+Bächle Handel'.

**Content:**
```
\bPastl\+Bächle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches companies ending in 'Luftfahrt' with strict boundaries, excluding titles like 'Frau' or 'Herr'.

**Content:**
```
(?<![A-Za-zäöüßÄÖÜ])\b([A-Z][a-zA-Zäöüß\-]+(?:\s+[A-Z][a-zA-Zäöüß\-]+)*)\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_specific_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known entity names that were missing: Norconheim, Oppert Elektro, Nexdorf-Metall, Zimmerhackel Bau, Bezirksgericht Neunkirchen, Raiffeisenbank Rion Vöcklabruck.

**Content:**
```
\b(?:Norconheim|Oppert\s+Elektro|Nexdorf\-Metall|Zimmerhackel\s+Bau|Bezirksgericht\s+Neunkirchen|Raiffeisenbank\s+Rion\s+V\u00f6cklabruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_rheindigital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known organisation names that do not follow standard suffix patterns, like RheinDigital.

**Content:**
```
\bRheinDigital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches German corporate entities with suffixes (AG, GMBH, KG, etc.) ensuring the suffix is the end of the entity. Handles 'AG GmbH' typos by matching 'AG' and stopping before 'GmbH'.

**Content:**
```
\b([A-Z][A-Za-z0-9\s&+\-]+(?:\s+(?:und|\+|\&)[A-Z][A-Za-z0-9\s&+\-]+)*)\s+(AG|GMBH|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft)(?=\s*(?:GmbH|AG|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft|,|\.|\)|\]|:|$|\s+\d))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_depp_verkehr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
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

## `specific_entity_sudevent`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
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

## `specific_entity_innluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'InnLuftfahrt GMBH'.

**Content:**
```
\bInnLuftfahrt\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_lutkehans`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lütkehans Event GMBH'.

**Content:**
```
\bLütkehans\s+Event\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_dorfkraft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Dorfkraft-Sanitär AG'.

**Content:**
```
\bDorfkraft-Sanitär\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_obernoder`

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

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_talost`

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

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_specific_org_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known organization names that are not covered by generic patterns, including those with 'und', '&', or specific suffixes.

**Content:**
```
\b(?:Schneppensieper\s+&\s+Bültbrunne\s+Touristik|Strohsack\s+und\s+Dresbeimdieke\s+Versand|Hagdorn\s+Robotik|Enns-Software|Gernot\s+Hirschkorn|WaldTouristik\s+Technologien|Liefeith\s+Immobilien|TalPflege|Valbruckzor-Energie|Raiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan|Unter\s+Gartglanz\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_firma_name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Firma' followed by a company name, capturing the name part only.

**Content:**
```
\bFirma\s+([A-Z][A-Za-z0-9\s&+\-]+(?:\s+(?:und|\+|\&)[A-Z][A-Za-z0-9\s&+\-]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_suffix_refined`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches German corporate entities with suffixes (AG, GMBH, KG, etc.). Handles double spaces and ensures the suffix is the end of the entity. Excludes preceding words like 'der' or 'Beschwerden'.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\s&+\-]+(?:\s+(?:und|\+|\&)[A-Z][A-Za-z0-9\s&+\-]+)*)\s+(AG|GMBH|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft)(?=\s*(?:GmbH|AG|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft|,|\.|\)|\]|:|$|\s+\d|\s+\w))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 190 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_42`)


Außerdem geht aus dem Curriculum hervor, dass es gemäß § 54 Abs 1 UG der Gruppe der  sozial- und wirtschaftswissenschaftlichen Studien zuzuordnen ist.

**False Positives:**

- `Abs 1 UG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_fa_purkersdorf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically matches FA Purkersdorf which might be missed by general patterns due to specific context.

**Content:**
```
\bFA\s+Purkersdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_tax_office`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific German tax office entities (Finanzamt/FA) with known district names found in training data.

**Content:**
```
\b(Finanzamt\s+(?:Oststeiermark|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen)|FA\s+Judenburg\s+Liezen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_specific_orgs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company and court names that failed in training: Chen Setzekorn, Ostgart AG, Istvan Gerart, InnMarine GMBH, HochLebensmittel Holding GMBH, Bezirksgericht Silz, LG Innsbruck, Landesgericht Innsbruck.

**Content:**
```
\b(?:Chen\s+Setzekorn|Ostgart\s+AG|Istvan\s+Gerart|InnMarine\s+GMBH|HochLebensmittel\s+Holding\s+GMBH|Bezirksgericht\s+Silz|LG\s+Innsbruck|Landesgericht\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_fa_abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities starting with 'FA' or 'Fa.' (Firma) followed by a name. Handles 'FA Purkersdorf' and 'Fa. Donau Furtkraftwald AG'.

**Content:**
```
(?<!\w)(?:FA|Fa\.?)\s+([A-Z][A-Za-z0-9\s&+\-]+(?:\s+(?:und|\+|\&)[A-Z][A-Za-z0-9\s&+\-]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 256 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Graz-Stadt  vom 12` — positional overlap with gold: `FA Graz-Stadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kirchdorf Perg Steyr  vom 11` — positional overlap with gold: `FA Kirchdorf Perg Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

</details>

---

## `german_hyphenated_company`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific hyphenated company names like 'Donau-Druck' that do not have a suffix.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9]+\-[A-Z][A-Za-z0-9]+)(?=\s*(?:,|\.|\)|\]|:|$|\s+\d|\s+\w))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 41 | 256 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Elisabeth-Platz` — partial — pred is substring of gold: `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`
- `Graz-Stadt` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Krankenpflege-Schule` — partial — pred is substring of gold: `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Barre-Syndrom` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_15`)


Unbeschadet dieses  Umstandes habe ich sämtliche Unterhaltskosten für meine Tochter Maximiliane Sakschewsky, MA, wie  bereits seit Ihren Aufenthaltswechsel im Jahr 2014 in das Vereinigte Königreich, im  Antragszeitraum noch EU-Mitgliedstaat, weiter getragen.

**False Positives:**

- `EU-Mitgliedstaat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Vereinigte Königreich`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_51`)


monatlich € 1.000,- an meine Ex-Gattin überwiesen, die als Schulgeld galten.

**False Positives:**

- `Ex-Gattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Ex-Gattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_6`)


Aufgrund eines Arbeitsauftrages vom 21.05.2021 kam es zu einer Überprüfung des  Familienbeihilfe-Anspruches der Beschwerdeführerin (=Bf.) bezüglich ihrer Tochter  Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum, da zunächst aufgrund der COVID-Pandemie  sowohl Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt worden waren.

**False Positives:**

- `Familienbeihilfe-Anspruches` — no gold match — likely missing annotation
- `COVID-Pandemie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `ECTS-Punkte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `ECTS-Punkten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

**False Positives:**

- `ECTS-Punkten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU Wien`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `ECTS-Punkten` — no gold match — likely missing annotation
- `ECTS-Punkten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_16`)


 Studienerfolgsnachweis der Hamburger Fern-Hochschule betreffend den Studiengang  Betriebswirtschaft für HAK-Absolventen betreffend im Jahr 2021 absolvierte Prüfungen  vom 02.08.2021  3.

**False Positives:**

- `Fern-Hochschule` — partial — pred is substring of gold: `Hamburger Fern-Hochschule`
- `HAK-Absolventen` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Hamburger Fern-Hochschule`(organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_38`)


Insbesondere ist den Curricula der beiden Studien entnehmbar, dass beide Studien „dasselbe  Ausbildungsergebnis" (im Sinne der BFG-Entscheidung RV/0180-L/10) zum Ziel haben (s.  angehängte Curricula und BFG-Entscheidung).

**False Positives:**

- `BFG-Entscheidung` — no gold match — likely missing annotation
- `BFG-Entscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_50`)


Mit Vorlagebericht vom 26.07.2022 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und führte dazu aus:  „Sachverhalt:  Aufgrund eines Arbeitsauftrages vom 21.05.2021 sollte der Familienbeihilfe-Anspruch der  Beschwerdeführerin bezüglich ihrer Tochter Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum  überprüft werden.

**False Positives:**

- `Familienbeihilfe-Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_51`)


Dies passierte, da ja aufgrund der COVID-Pandemie sowohl  Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt wurden.

**False Positives:**

- `COVID-Pandemie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_73`)


Von den an der WU Wien absolvierten  Lehrveranstaltungen mit 42 ECTS-Punkten wurden 24 ECTS-Punkte an der JKU Linz  angerechnet.

**False Positives:**

- `ECTS-Punkten` — no gold match — likely missing annotation
- `ECTS-Punkte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_76`)


Die beiden genannten Bachelor-Studien sind an der jeweiligen Universität jeweils die  „klassischen“ bzw. typischen wirtschaftswissenschaftlichen Bachelor-Studien, umfassen jeweils  einen Aufwand von 180 ECTS-Punkten bei 6 Semestern Mindeststudiendauer.

**False Positives:**

- `Bachelor-Studien` — no gold match — likely missing annotation
- `Bachelor-Studien` — no gold match — likely missing annotation
- `ECTS-Punkten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_89`)


Beide Bachelorstudien sind nach § 2 der jeweiligen Curricula ein sozial- und  wirtschaftswissenschaftliches Studium im Sinne des § 54 Abs. 1 Universitätsgesetz 2002 und  umfassen jeweils einen Arbeitsumfang von 180 ECTS-Punkten, 6 Semester  Mindeststudiendauer, die Absolvierung einer Studieneingangsphase und die Abfassung einer  Bachelorarbeit.

**False Positives:**

- `ECTS-Punkten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_93`)


Sie bilden somit jeweils das „typische“ wirtschaftswissenschaftliche Bachelor-Studium an der  jeweiligen Universität.

**False Positives:**

- `Bachelor-Studium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_99`)


Dies muss jedoch nicht zwangsläufig an  unterschiedlichen Ausbildungsinhalten liegen, sondern kann auch unterschiedlichen  Kursteilnahme-Voraussetzungsketten und Detailunterschieden der Studienpläne liegen, die  manche Lehrveranstaltungen entweder erst später (nach Absolvierung anderer Kurse)  anrechenbar machen bzw. die aufgrund unterschiedlicher (ECTS-)

**False Positives:**

- `Kursteilnahme-Voraussetzungsketten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_105`)


Die Studienpläne sind in Kernbereichen identisch, jedoch im Gesamten nicht gänzlich  deckungsgleich, was allerdings auch daran liegt, dass deckungsgleiche Studien an  verschiedenen Standorten aufgrund der Freiheiten und Entwicklungen des Bologna-Systems  (Spezialisierungen/Nuancierungen der Lehrinhalte im Detail, Schaffung diverser  Voraussetzungsketten bei Lehrveranstaltungs-Anmeldungen und Anrechnungen, welche auch  standortbezogen dem schnelleren Studienabschluss dienen sollen) in der Praxis nahezu  ausgeschlossen sind.

**False Positives:**

- `Lehrveranstaltungs-Anmeldungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_150`)


Würde man die Kriterien betreffend einen  bloßen Studienortwechsel noch enger ziehen, bliebe für die vom Verwaltungsgerichtshof  gezogene Unterscheidung zwischen Studienortwechsel und Studienwechsel (VwGH  09.07.2008, 2005/13/0142) in der Praxis kein Raum, da wie bereits ausgeführt, angesichts des  Bologna-Studiensystems anders als vor Jahrzehnten wohl kaum noch zwei zu 100% identische  Studien in Österreich bzw. europaweit existieren.

**False Positives:**

- `Bologna-Studiensystems` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Österreich`(country)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_153`)


Die beiden beschwerdegegenständlichen Studien bilden, wie bereits ausgeführt, jeweils das  „typische“ wirtschaftswissenschaftliche Bachelor-Studium an der jeweiligen Universität.

**False Positives:**

- `Bachelor-Studium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

**False Positives:**

- `Jazz-Abteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Musikhochschule Wien`(organisation)
- `Konservatorium  der Stadt Wien`(organisation)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_17`)


In der Folge wurden die Verluste aus der selbständigen Tätigkeit als Musiker in den Jahren  2012 bis 2014 nicht anerkannt und im Bp-Bericht wurde dies wie folgt dargestellt:      2 von 14 Seite 3 von 14

**False Positives:**

- `Bp-Bericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_78`)


Gerade kreative Berufe, wie der  eines Musikers, hätten ein völlig untypisches Einnahmen/Ausgaben-Profil, weshalb es zu  Schwankungen und zu einer Änderung der Verhältnisse zwischen Einnahmen und Ausgaben  kommen könne.

**False Positives:**

- `Ausgaben-Profil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Nach Abschluss der Betriebsprüfung (BP-Bericht vom 13.5.2024) erging (erstmalig) der  Einkommensteuerbescheid 2021 am 22.5.2024.

**False Positives:**

- `BP-Bericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_23`)


durchgeführt (Ankündigung vom 09.01.2024, BP-Bericht vom 13.05.2024).

**False Positives:**

- `BP-Bericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_27`)


Darüber wurde folgendermaßen entschieden:   - die Beschwerde gegen den ESt-Bescheid 2020 wurde mit Beschwerdevorentscheidung (BVE)  vom 12.3.2025 (Anm. laut BFG richtig: 11.03.2025) abgewiesen.

**False Positives:**

- `ESt-Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_28`)


- der Beschwerde gegen den ESt-Bescheid 2021 wurde mit BVE vom 12.03.2025 teilweise  stattgegeben.

**False Positives:**

- `ESt-Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_36`)


Da nicht vorgebracht werde, dass der ESt-Bescheid 2021  nicht rechtswirksam ergangen sei bzw. die Höhe der Anspruchszinsen nicht korrekt berechnet  worden sei, sei die Beschwerde als unbegründet abzuweisen.

**False Positives:**

- `ESt-Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Halmetschlager-Gasse` — partial — pred is substring of gold: `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_63`)


Die Steuer ist spätestens am Fälligkeitstag zu entrichten (Art.  21 Abs. 2 UStG-BMR).

**False Positives:**

- `UStG-BMR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

