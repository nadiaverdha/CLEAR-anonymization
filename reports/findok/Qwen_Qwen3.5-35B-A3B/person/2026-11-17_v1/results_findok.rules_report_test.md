# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-17T13:25:27.001270

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-17_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 3148 |
| Validation documents | 787 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 7310 |
| Validation sentences | 2501 |
| Dev sentences | 61673 |
| Test sentences | 61001 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 150 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
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

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.2% |
| True Positives | 808 |
| False Positives | 747 |
| False Negatives | 806 |
| Total Gold Entities | 1614 |
| Micro Precision | 52.0% |
| Micro Recall | 50.1% |
| Micro F1 | 51.0% |
| Macro F1 | 51.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Names in Parentheses/Context` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `Names in Legal Context (Complainant/Respondent) with Suffixes` | 28.0% | 73.4% | 17.3% | 380 | 279 | 101 |
| `Legal Titles with Full Names` | 36.8% | 72.0% | 24.7% | 554 | 399 | 155 |
| `Standalone Surnames in Narrative` | 9.2% | 68.4% | 5.0% | 117 | 80 | 37 |
| `Names after 'vertreten durch' (Tightened)` | 1.8% | 36.6% | 0.9% | 41 | 15 | 26 |
| `Ing. and Specialized Titles with Names` | 1.8% | 26.8% | 0.9% | 56 | 15 | 41 |
| `Frau Preceded Names with Suffixes` | 1.3% | 17.7% | 0.7% | 62 | 11 | 51 |
| `Gutachten von Names` | 0.1% | 12.5% | 0.1% | 8 | 1 | 7 |
| `Case Citation Surnames` | 0.1% | 5.0% | 0.1% | 20 | 1 | 19 |
| `Anonymized Initials with Title (Fixed)` | 0.2% | 1.3% | 0.1% | 155 | 2 | 153 |
| `Role Indicators (Richter/Richterin)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gesellschafter Full Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Richter Title Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `N.N. Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr.in with Placeholder Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after Hinsichtlich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after Preposition 'bei' (Tightened)` | 0.0% | 0.0% | 0.0% | 87 | 0 | 87 |
| `Names after Company Prefix 'Fa.' (Tightened)` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Names in Parentheses/Context (Fixed)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complex Academic Titles with Spacing` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Richter Title Names (Concatenated)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names with Suffixes in Legal Context (Fixed)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone Names in Narrative Context` | 0.0% | 0.0% | 0.0% | 43 | 0 | 43 |
| `Standalone Names in Context (von ... von)` | 0.0% | 0.0% | 0.0% | 18 | 0 | 18 |
| `Names after Specific Verbs/Contexts (Beschuldigter/Stellungnahme)` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Names in Parentheses/Context` 

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `0c036bc0`  
**Description:**
Matches names appearing in specific contexts like '(Nachname wie Bf.)' or '(geboren am ...)' which often follow a name, capturing the full name.

**Content:**
```
(?:für\s+die\s+Tochter|für\s+das\s+Kind|Nachname\s+wie\s+Bf\.?)\s+([A-Z][a-z]+(?:[ -][A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 0 | 1609 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_14`)


Das Finanzamt Österreich begründete diese Vorgehensweise dergestalt, dass der  Familienbonus Plus für das Kind OStR Priv.-Doz. Theodor Voelpel  hinsichtlich der Monate September bis  Dezember sowie für das Kind Herbert Schaffarik  hinsichtlich der Monate August bis Dezember  zustehe.

| Predicted | Gold |
|---|---|
| `Herbert Schaffarik` | `Herbert Schaffarik` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)
- `OStR Priv.-Doz. Theodor Voelpel` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_28`)


Die Mutter der beiden Kinder machte im Rahmen ihrer Steuererklärung vom 03. März 2021  weder den Familienbonus Plus für das Kind OStR Priv.-Doz. Theodor Voelpel  noch für das Kind Herbert Schaffarik  geltend.

| Predicted | Gold |
|---|---|
| `Herbert Schaffarik` | `Herbert Schaffarik` |

**Missed by this rule (FN):**

- `OStR Priv.-Doz. Theodor Voelpel` (person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Lisa Pucher in der Beschwerdesache  OStR Richarda Schönwaldt, Erich-Opitz-Weg 32, 4742 Großpoxruck, Österreich, über die Beschwerde vom 21. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. Juli 2023 betreffend die Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum November 2022 bis Juni 2023 für das Kind  Heidemarie Fitzenreiter, verbunden mit der Rückforderung der aus der Kinderstaffel (§ 8 Abs 3 FLAG  1967) resultierenden anteiligen Familienbeihilfe für die Kinder Florens Meulenkamp  und  Sara Liebreich, zu Recht:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Lisa Pucher` (person)
- `OStR Richarda Schönwaldt` (person)
- `Erich-Opitz-Weg 32, 4742 Großpoxruck, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Florens Meulenkamp` (person)
- `Sara Liebreich` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Das Finanzamt erließ am 06.07.2023 einen Bescheid an die Beschwerdeführerin (nachfolgend  „Bf“) über die Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum  November 2022 bis Juni 2023 für das Kind Heidemarie Fitzenreiter, verbunden mit der Rückforderung  der aus der Kinderstaffel resultierenden anteiligen Familienbeihilfe für die Kinder Florens Meulenkamp  und Sara Liebreich.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Florens Meulenkamp` (person)
- `Sara Liebreich` (person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_69`)


§ 5 Abs 3 FLAG 1967 schließt einen  Familienbeihilfenanspruch in den hier unter anderem streitgegenständlichen Monaten  November 2022 bis Mai 2023 für die Tochter Heidemarie Fitzenreiter  aus, weshalb auch dahingestellt  bleiben kann, ob aufgrund des College-Besuches der Tochter der Bf in Israel in den Monaten  November 2022 bis Mai 2023 eine Berufsausbildung im Sinne des § 2 Abs 1 lit b FLAG 1967  vorgelegen ist.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

</details>

---

## `Names in Legal Context (Complainant/Respondent) with Suffixes` 🏆

**F1:** 0.280 | **Precision:** 0.734 | **Recall:** 0.173  

**Format:** `regex`  
**Rule ID:** `b35975d7`  
**Description:**
Matches full names following 'in der Beschwerdesache' or similar legal contexts, capturing suffixes like LL.M., MBA, Bakk. techn., while explicitly excluding company names (GmbH, AG) and locations.

**Content:**
```
(?:in\s+der\s+Beschwerdesache(?:\s+(?:der|des))?\s+|des\s+)([A-Z][a-z\u00c0-\u00ff]+(?:[ -][A-Z][a-z\u00c0-\u00ff]+)+)(?:,?\s*(?:LL\.M|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MAS|Bakk\. rer\. nat|Bakk\. art\. BEd|BEd\. phil|Bakk\. iur|Bakk\. techn)?)?(?=,|$|[,.](?!.*(?:Straße|Gasse|Platz|Weg|Avenue|Landstraße|Finanzamt|GmbH|AG|Gesellschaft|m\.b\.H)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.734 | 0.173 | 0.280 | 380 | 279 | 101 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 279 | 101 | 1335 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Waltraud Hinterlandt` | `Waltraud Hinterlandt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Günter Lehwaldt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jeanne Weiermann` | `Jeanne Weiermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lewis Rzehula` | `Lewis Rzehula` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Neustädterstraße 3, 9560 Wabl, Österreich` (address)
- `43-839/6567` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Siegfried Basyurt` | `Siegfried Basyurt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

| Predicted | Gold |
|---|---|
| `Chen Walcker` | `Chen Walcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `63-698/2600` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Mackiewicz` | `Hedwig Mackiewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Daniel Parys` | `Daniel Parys` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Krafft` (person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Buchholz` | `Ursula Buchholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Li Schukardt` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chantal Eligüzel` | `Chantal Eligüzel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Oberstelehn` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Guntram Antepoth` | `Guntram Antepoth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `70-875/4351` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Sven Mitterhuber` | `Sven Mitterhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Mag.a Livia Korowski` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Roxana Dellner` | `Roxana Dellner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `RA Mag. Robert Bitsche` (person)
- `Magistrats der Stadt Wien` (organisation)
- `88-034/0292` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Laetitia Kuban, Karawankenplatz 8, 8046 Graz, Österreich, über die Beschwerde vom 16. Dezember 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 14. November 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für das Kind x in den Zeiträumen vom 01.07.2018 bis zum 30.09.2018  sowie vom 01.07.2019 bis zum 30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Laetitia Kuban` | `Laetitia Kuban` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karawankenplatz 8, 8046 Graz, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

| Predicted | Gold |
|---|---|
| `Günter Gopfauf` | `Günter Gopfauf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Maria-Luise Wohlmayr` (person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich` (address)
- `Finanzamtes Salzburg – Stadt` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wladimir Dammkoehler, Grolzham 15, 3123 Obermerking, Österreich, über die Beschwerde vom 24. Jänner 2020  gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Jänner 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 47-339/1168, zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wladimir Dammkoehler` | `Wladimir Dammkoehler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Grolzham 15, 3123 Obermerking, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `47-339/1168` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karina Ditzler` | `Karina Ditzler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Serena Weidlich  in der Beschwerdesache Ruprecht Pesselt,  Blons 28, 9612 Michelhofen, Österreich, betreffend Beschwerde gegen die Buchungsmitteilung  des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel zur Steuernummer 89-624/1157, betreffend  Gebühr gemäß § 17a VfGG und Gebührenerhöhung gemäß § 9 Abs.1 GebG 1957 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ruprecht Pesselt` | `Ruprecht Pesselt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Serena Weidlich` (person)
- `Blons 28, 9612 Michelhofen, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `89-624/1157` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Isidor Czebulla` | `Isidor Czebulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Waldemar Faltermeir  in der Beschwerdesache  Elias Kendziorra,  Fernblick 3, 6410 Telfs, Österreich, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid des Finanzamt Waldviertel  vom 22. Mai 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 29-596/0625  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Kendziorra` | `Elias Kendziorra` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Waldemar Faltermeir` (person)
- `Fernblick 3, 6410 Telfs, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `29-596/0625` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Floriane Rötker` | `Floriane Rötker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn` (person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich` (address)
- `Heinz Neuböck Wthrd GmbH` (organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Leonhard Bianchini, Stixendorf 463, 6361 Glantersberg, Österreich,  über die Beschwerde vom 20.03.2018, eingebracht am 22. März 2018, gegen den Bescheid des  Finanzamtes Klagenfurt vom 16.02.2018, zu Steuernummer 13-665/9571, mittels welchem  der Antrag auf Wiederaufnahme der Verfahren betreffend Einkommensteuer für die Jahre  2012 bis 2015 abgewiesen wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Leonhard Bianchini` | `Leonhard Bianchini` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helga Woschank` (person)
- `Stixendorf 463, 6361 Glantersberg, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `13-665/9571` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Caroline Reinwaldt  in der Beschwerdesache Manuel Fortanz,  Zielgerade 30, 4950 Schwaig, Österreich, betreffend die Beschwerde vom 5. Juli 2017 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 9. Juni 2017 betreffend Umsatz- und Körperschaftsteuer 2010 bis 2015 sowie  Umsatzsteuerfestsetzung für die Zeiträume 01-03/2016, 04-06/201, 07-09/2016 und 10- 12/2016, Steuernummer , beschlossen:  Die Beschwerde wird als gegenstandslos geworden erklärt und das Verfahren eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Manuel Fortanz` | `Manuel Fortanz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Caroline Reinwaldt` (person)
- `Zielgerade 30, 4950 Schwaig, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Gorecki` | `Wieland Gorecki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Eugen Burgschweiger` | `Eugen Burgschweiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Bernarda Egli, Moosenweg 38, 5630 Harbach, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 8. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bernarda Egli` | `Bernarda Egli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Moosenweg 38, 5630 Harbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Susette Volmari` | `Susette Volmari` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich` (address)
- `Magistrates der  Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hartwig Simonson` | `Hartwig Simonson` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamtes` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sulamith Hördegen` | `Sulamith Hördegen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Serena Leutl` | `Serena Leutl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Daisy Große-Bölting` (person)
- `Wanderweg 7, 2763 Thal, Österreich` (address)
- `Bernhart Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-306/6017` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Natalie Nodurft` | `Natalie Nodurft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrich Petrag` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Mag. Marion Riezinger` (person)
- `Finanzamtes  Linz` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Elisabeth Sarigiannis,  Klesenza 7, 9587 Erlendorf, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerden vom 18. Dezember 2012 gegen die  Bescheide des Finanzamtes Österreich vom 21. November 2012 betreffend Einkommensteuer  2007 bis 2011, Steuernummer 84-729/8666, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Elisabeth Sarigiannis` | `Elisabeth Sarigiannis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klesenza 7, 9587 Erlendorf, Österreich` (address)
- `gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `84-729/8666` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Shoshana Döllmann` | `Shoshana Döllmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gernot Kirchenmayer` | `Gernot Kirchenmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Anneliese Wäsche` (person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich` (address)
- `Eckert Fries Carter Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Dominik Moebus,  Aichach 11m, 9375 Knappenberg, Österreich, vertreten durch Magistrat der Stadt Wien, Kinder- und Jugendhilfe,  Rechtsvertretung 16,17,18,19, Kalvarienberggasse 29, 1170 Wien, betreffend die Beschwerde  vom 25. August 2020 gegen den Abweisungsbescheid des Finanzamtes Österreich (bisher  Finanzamt Wien 2/20/21/22) vom 17. Juli 2020 betreffend Familienbeihilfe ab Jänner 2016  beschlossen:   Der am 12. Jänner 2021 eingebrachte, mit 07. Jänner 2021 datierte Vorlageantrag betreffend  die am 04. Dezember 2020 zugestellte Beschwerdevorentscheidung vom 12. November 2020  wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dominik Moebus` | `Dominik Moebus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aichach 11m, 9375 Knappenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Felizitas Johanesson` | `Felizitas Johanesson` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` (person)
- `Aspangweg 17, 9781 Gailberg, Österreich` (address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `48-504/5908` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Pawel Schuwirth  in der Beschwerdesache Griselda Hälmle,  Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich, über die Beschwerde vom 24. Oktober 2018 gegen die Bescheide des  Finanzamtes Landeck Reutte (jetzt Finanzamt Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und 2017, Steuernummer  49-622/1059, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Griselda Hälmle` | `Griselda Hälmle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Pawel Schuwirth` (person)
- `Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `49-622/1059` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Madeleine Göpffarth` | `Madeleine Göpffarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Gündüz` | `Ida Gündüz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Christina Tiebout` | `Christina Tiebout` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Dr. Sebastian Pfeiffer, LL.M.` (person)
- `Gerald Cuny-Kreuzer` (person)
- `Dr. Franz Kandlhofer` (person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Xaver Hüttenroth` | `Xaver Hüttenroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `57-139/5207` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Gudrun Terzoglou  in der Beschwerdesache Ruprecht Berkenkämper,  Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich ,Land, über die Beschwerde vom 28. August 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 26. Juli 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, Steuernummer 98-086/6338, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ruprecht Berkenkämper` | `Ruprecht Berkenkämper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Gudrun Terzoglou` (person)
- `Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `98-086/6338` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des Rocco Choudhury, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Rocco Choudhury` | `Rocco Choudhury` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wachtelgasse 7, 9543 Stadt, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Paolo Reppert  in der Beschwerdesache des  Wendelin Pham, Kremstal Bundesstraße 6, 4682 Thalham, Österreich, über die Beschwerden 1.) vom 17.10.2019 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 15.10.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 sowie  2.) vom 4.5.2020 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3.4.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Wendelin Pham` | `Wendelin Pham` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Paolo Reppert` (person)
- `Kremstal Bundesstraße 6, 4682 Thalham, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Juri Marstaller` | `Juri Marstaller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Lukas Dimitrieff` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Sonja Wennemann` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerden vom 18. Juni 2017 gegen die Bescheide des  Finanzamtes Bregenz vom 16. Juni 2017 betreffend Einkommensteuer 2015 und 2016  Steuernummer 88-412/8444  beschlossen:   Die Vorlageanträge vom 19.11.2018 gegen die Beschwerdevorentscheidungen vom 10.10.2018  werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Francois Hetkemper` | `Francois Hetkemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerde vom 29. Mai 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 17. Mai 2018 betreffend Einkommensteuer 2017, Steuernummer  88-412/8444  zu Recht erkannt:   Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Francois Hetkemper` | `Francois Hetkemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  Timon Reinhertz, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Timon Reinhertz` | `Timon Reinhertz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Adam Rueßbült` (person)
- `Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `15-325/9824` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

| Predicted | Gold |
|---|---|
| `Lydia Rehnen` | `Lydia Rehnen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Andrea Helbok` (person)
- `Roßbergl 5, 4923 Gunzing, Österreich` (address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH` (organisation)
- `Finanzamtes  Innsbruck` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_3`)


über die Beschwerde des Lukas Niedergesess, Staudenstraße 7, 3834 Eisenreichs, Österreich, Deutschland, vom 16. Februar 2021, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 13. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1 Parkometer- gesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Lukas Niedergesess` | `Lukas Niedergesess` |

**Missed by this rule (FN):**

- `Staudenstraße 7, 3834 Eisenreichs, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Lilienfeld St. Pölten) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Alexandra Hettrich` | `Alexandra Hettrich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Richard Schwanken` (person)
- `Kohleggweg 268, 4621 Schnarrndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Lilienfeld St. Pölten` (organisation)
- `86-148/2619` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Esra Luetje` | `Esra Luetje` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler` (person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich` (address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des Finanzamtes Spittal  Villach vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Sven Hoerlin` | `Sven Hoerlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Padasterjochhaus 6, 9562 Tobitsch, Österreich` (address)
- `Finanzamtes Spittal  Villach` (organisation)
- `51-093/9549` (tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Aloisa Antoni, Wassermanngasse 9, 4840 Vöcklabruck, Österreich  vertreten durch die Steuerfilter Steuerberatungs-GmbH,  Ischlerbahnstraße 23, 5301 Eugendorf, über die Beschwerde vom 11. Juni 2019 und 9. Oktober  2019 gegen die Bescheide des Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich)  vom 16. Mai 2019 und 2. Oktober 2019 betreffend die Wiederaufnahme der  Einkommensteuerverfahren 2013 bis 2015 zu Recht erkannt:  I)  Die Wiederaufnahmebescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Aloisa Antoni` | `Aloisa Antoni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Wassermanngasse 9, 4840 Vöcklabruck, Österreich` (address)
- `Steuerfilter Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juliana Untermeier` | `Juliana Untermeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Dr. Christoph Ganahl` (person)
- `Finanzamtes` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Florentine Mugge` | `Florentine Mugge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` (person)
- `Rodlhütte 36, 9782 Plone, Österreich` (address)
- `FA Kufstein  Schwaz` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-679/2034` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdeführers Jeremias Pretzel` — partial — gold is substring of pred: `Jeremias Pretzel`
- `Finanzamtes Salzburg-Land` — type mismatch — same span as gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Jeremias Pretzel`(person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich`(address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Josef Nußbaumer`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_54`)


Da die Bäckerei die Immobilie in ihrer Gesamtheit mietete wurde in Ansehung an den schlechten Gebäudezustand des Gebäudeteils Pf. (fensterlos, schlechte Zufahrt und Belieferungsmöglichkeit, kleiner Seiteneingang - siehe Fotos) ein niedriger Gesamt-m 2 Preis als Miete verlangt.

**False Positives:**

- `Gebäudeteils Pf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_60`)


Der Sachverständige kommt in der Ertragswertberechnung auf einen Verkehrswert beider Gebäudekörper von € 629.643 (nach Abzug von Umbaukosten des Bauteiles Pf.).

**False Positives:**

- `Bauteiles Pf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_173`)


Den Ausführungen des Gutachters Ing. O, es wären keine Instandhaltungskosten anzusetzen, Seite 14 von 23 weil diese vom Mieter getragen würden (vgl Gutachten vom 28.10.2014, Seite 12, Fußnote 7), kann daher nicht gefolgt werden.

**False Positives:**

- `Gutachters Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_276`)


Seite 20 von 23 Im zweiten Gutachten wurde im Zuge der Ertragswertberechnung auf einen Verkehrswert des Grundstückes samt Gebäude von € 629.643 (nach Abzug von Umbaukosten des Bauteiles Pf.) geschlossen.

**False Positives:**

- `Bauteiles Pf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_116`)


Aufgrund des Todes Hrn.

**False Positives:**

- `Todes Hrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Gruenleitner Event` — type mismatch — same span as gold: `Gruenleitner Event`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Donau-Elektro` — type mismatch — same span as gold: `Donau-Elektro`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_14`)


In beigefügter Auflistung als PDF Dateien finden sie die absolvierten Prüfungen und  Erfolgsnachweise meines Sohnes B. Unser Sohn hatte bereits bei Abschluss seiner Matura im  Juni 2014 den fixen Studienwunsch des Human-Medizinstudiums.

**False Positives:**

- `Human-Medizinstudiums` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_71`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung  der Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für  das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer  Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem  Muster der Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_75`)


Dieses wird durch  die Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird  (Parkometerabgabeverordnung), festgesetzt.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

**False Positives:**

- `Finanzamtes Neunkirchen Wr` — partial — pred is substring of gold: `Finanzamtes Neunkirchen Wr. Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Techn R Lilia Schöpcke`(person)
- `In der Klaus 8, 5651 Winkl, Österreich`(address)
- `Finanzamtes Neunkirchen Wr. Neustadt`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_8`)


Folgendes mitgeteilt:  Lenker und Zulassungsbesitzer des Fahrzeuges Ford Mustang, goldfarbig, Bj. 2005,  FahrgestellNr. 123x, mit dem deutschen Kennzeichen X1, sei der Bf; er habe einen Wohnsitz in  D/XX, Y-Str1, sowie einen weiteren Wohnsitz im Inland in A/XX, A-Str2.

**False Positives:**

- `Fahrzeuges Ford Mustang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_124`)


Im Ergänzungsersuchen vom 17.3.2016 hat das Finanzamt zunächst festgehalten, dass der  Bf seit Mai 2008 nahezu durchgehend in Österreich beschäftigt und mit Wohnsitz gemeldet  gewesen sei und hat vom Bf eine Vielzahl an Unterlagen – darunter Nachweise zu deutschen  Mietzahlungen, zum Verkauf des Ford Mustang, Service- und Reparaturrechnungen der  Fahrzeuge, zu einem allfälligen deutschen Handyvertrag und Girokonto - , die zum  Gegenbeweis dienen könnten, angefordert.

**False Positives:**

- `Ford Mustang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_391`)


Gemäß § 5 Abs. 2 der Verordnung des Wiener Gemeinderates, mit der für das Abstellen von  mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben  wird (Parkometerabgabeverordnung) idgF sind zur Entrichtung der Abgabe der Lenker, der  Besitzer und der Zulassungsbesitzer zur ungeteilten Hand verpflichtet.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Tamara Poertgen` — partial — pred is substring of gold: `Tamara Poertgen, LLB Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Babette Nimzyk`(person)
- `Tamara Poertgen, LLB Bakk. techn.`(person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich`(address)
- `Martin Friedl`(person)
- `Finanzamtes`(organisation)
- `08-216/2001`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_31`)


"Präambel  Die M-AG mit Sitz AdresseM-AG, und Firmenbuchnummer CH-***** des Handelsregisters des  Kantons St. Gallen betreibt eine internationale Einkaufsgemeinschaft, die den Teilnehmern (im  folgenden "Mitglieder" genannt) ermöglicht, durch den Bezug von Waren und Dienstleistungen  bei L Partnerunternehmen (im Folgenden "Partnerunternehmen" genannt) Vorteile zu erhalten  (im Folgenden "L Treueprogramm" genannt).

**False Positives:**

- `Kantons St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dominika Oehlerich` — partial — pred is substring of gold: `Dominika Oehlerich, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Ebner`(person)
- `Dominika Oehlerich, BEd`(person)
- `Zamberg 9, 3843 Hohenau, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der Cathleen Gröneweg, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Klagenfurt` — type mismatch — same span as gold: `Finanzamtes Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cathleen Gröneweg`(person)
- `Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich`(address)
- `Finanzamtes Klagenfurt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Simone Zemanek` — partial — pred is substring of gold: `Simone Zemanek, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Haim`(person)
- `Simone Zemanek, MSc`(person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `15-763/9594`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_137`)


Weiters sind nach der Rechtsprechung des Verwaltungsgerichthofes Zahlungen, die schlechthin  strittige Ansprüche aller Art abgelten, nicht etwa gleich Abfertigungen für die Beendigung eines  Dienstverhältnisses typisch (VwGH 20.11.2012, 2008/13/0252;

**False Positives:**

- `Verwaltungsgerichthofes Zahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Eleonore Sawadzki` — partial — pred is substring of gold: `Eleonore Sawadzki, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_17`)


Monatslohn  unter die begünstigte Besteuerung falle, nicht jedoch die anteilsmässig erfolgten Auszahlungen  des Kantons Zug.

**False Positives:**

- `Kantons Zug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_195`)


5. Ausschüttungsgleiche Erträge ausländischer Immobilienfonds gemäß § 42 Abs. 1 zweiter Satz  des Immobilien-Investmentfondsgesetzes.

**False Positives:**

- `Immobilien-Investmentfondsgesetzes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_198`)


Bei Wegzug in einen Staat der Europäischen Union oder einen Staat des  Europäischen Wirtschaftsraumes, mit dem eine umfassende Amts- und Vollstreckungshilfe  besteht, kann der Steuerpflichtige in der Steuererklärung beantragen, dass die Fälligkeit mit  dem Ablauf des Kalenderjahres des vom Steuerpflichtigen anzugebenden Zeitpunktes des  voraussichtlichen tatsächlichen Zuflusses festgesetzt wird.

**False Positives:**

- `Europäischen Wirtschaftsraumes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Europäischen Union`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_60`)


Am 1. Jänner 2021 trat das Finanzamt Österreich gemäß § 323b Abs. 1 BAO an die Stelle des  Finanzamtes Neunkirchen Wr. Neustadt.

**False Positives:**

- `Finanzamtes Neunkirchen Wr` — partial — pred is substring of gold: `Finanzamtes Neunkirchen Wr. Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich`(organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_54`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_87`)


Selbiges gilt für die bezahlte Möbelablöse für die Garconniere  in Ort3inA (deren Anmietung zwischen den Parteien unstrittig blieb), sowie den Verkauf des  Mercedes Benz.

**False Positives:**

- `Mercedes Benz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Wigand Maczkiewicz` — partial — pred is substring of gold: `Wigand Maczkiewicz, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_99`)


Dagegen sei die gutachterliche Stellungnahme des  Humangenetikers Univ. Prof. Dr. F unberücksichtigt geblieben.

**False Positives:**

- `Humangenetikers Univ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. F`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_230`)


Weder für die  Sachverständige noch für das BFG besteht ein Zweifel daran, dass bei der Tochter der Bf von  Geburt an ein Gendefekt vorliegt, was durch einen Teil der berücksichtigten, angeführten  Befunde wie auch in der gutachterlichen Stellungnahme des Humangenetikers Dr. F bestätigt  wird, insofern dessen Befund – entgegen dem Dafürhalten der Bf – nicht außer Acht gelassen  wurde.

**False Positives:**

- `Humangenetikers Dr` — positional overlap with gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Dr. F`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_43`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_83`)


Diese Feststellungen sind unstrittig und ergeben sich  aus der Einsichtnahme in das Firmenbuch und in den vom Bundesfinanzgericht angeforderten  Insolvenzakt des Landesgerichtes Feldkirch.

**False Positives:**

- `Landesgerichtes Feldkirch` — partial — gold is substring of pred: `Landesgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Landesgerichtes`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_54`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

</details>

---

## `Legal Titles with Full Names` 🏆

**F1:** 0.368 | **Precision:** 0.720 | **Recall:** 0.247  

**Format:** `regex`  
**Rule ID:** `fb1bfea3`  
**Description:**
Matches persons with titles (Dr., Mag., Hon.-Prof., etc.) followed by full names, ensuring multiple titles and suffixes are captured correctly, including cases where title and name are concatenated (e.g., Mag.Dr.).

**Content:**
```
(?:HR|MMag\.|Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Univ\.-Prof\.|Priv\.-Doz\.in?|Priv\.-Doz\.|Hon\.-Prof\.|Hon\.-Prof\.in?|DDr\.in?|RgR|StR|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)(?:\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.|Hon\.-Prof\.in?|DDr\.in?))*\s*[A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+(?:von\s+der\s+|von\s+dem\s+)?[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB(?!.*LLB)|BEd(?!.*BEd)|B\.K(?!.*BK)|Dipl\.Kfm(?!.*Kfm)|MA(?!.*MA)|MBA(?!.*MBA)|MSc(?!.*MSc)|MAS(?!.*MAS)|Bakk\. rer\. nat(?!.*nat)|Bakk\. art\. BEd(?!.*BEd)))?(?=\s|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.720 | 0.247 | 0.368 | 554 | 399 | 155 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 399 | 155 | 1215 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Mag. Josef Nußbaumer` | `Mag. Josef Nußbaumer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Pretzel` (person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich` (address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Michael Nierla` | `Mag. Michael Nierla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `N.N.` (person)
- `Finanzamt für Gebühren` (organisation)
- `N.N.` (person)
- `Verwaltungsgerichtshof` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `RgR Amalia Schuetzke` | `RgR Amalia Schuetzke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Günter Lehwaldt` | `Univ.-Prof. Günter Lehwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waltraud Hinterlandt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Saphira Blazejewicz` | `Priv.-Doz.in Saphira Blazejewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ophelia Dutschka` | `Hon.-Prof.in Ophelia Dutschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Cassandra Witzenhause` | `Univ.-Prof.in Cassandra Witzenhause` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hedwig Mackiewicz` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Dr.in Hemma Ramelow` | `Univ.-Prof.in Dr.in Hemma Ramelow` |
| `Mag. Damian Wiecher` | `Mag. Damian Wiecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Li Schukardt` | `Priv.-Doz. Li Schukardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Buchholz` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Corbinian Friemuth` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Mag.a Livia Korowski` | `Priv.-Doz.in Mag.a Livia Korowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Mitterhuber` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Anna Mechtler-Höger` | `Mag. Anna Mechtler-Höger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roxana Dellner` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `RA Mag. Robert Bitsche` (person)
- `Magistrats der Stadt Wien` (organisation)
- `88-034/0292` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `MMag. Elisabeth Brunner` | `MMag. Elisabeth Brunner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Serge Pechert` (person)
- `Texing 43, 3143 Oberloitzenberg, Österreich` (address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wladimir Dammkoehler, Grolzham 15, 3123 Obermerking, Österreich, über die Beschwerde vom 24. Jänner 2020  gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Jänner 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 47-339/1168, zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wladimir Dammkoehler` (person)
- `Grolzham 15, 3123 Obermerking, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `47-339/1168` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Ditzler` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Linn Förstle` | `Hon.-Prof. Linn Förstle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich` (address)
- `Finanzamtes` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Serena Weidlich  in der Beschwerdesache Ruprecht Pesselt,  Blons 28, 9612 Michelhofen, Österreich, betreffend Beschwerde gegen die Buchungsmitteilung  des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel zur Steuernummer 89-624/1157, betreffend  Gebühr gemäß § 17a VfGG und Gebührenerhöhung gemäß § 9 Abs.1 GebG 1957 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Serena Weidlich` | `Hon.-Prof.in Serena Weidlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruprecht Pesselt` (person)
- `Blons 28, 9612 Michelhofen, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `89-624/1157` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Babette Nimzyk` | `Hon.-Prof.in Babette Nimzyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tamara Poertgen, LLB Bakk. techn.` (person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich` (address)
- `Martin Friedl` (person)
- `Finanzamtes` (organisation)
- `08-216/2001` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Fabienne Kattner` | `Univ.-Prof.in Fabienne Kattner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Özgür` (person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich` (address)
- `Thomas Krampl` (person)
- `Finanzamtes für Gebühren` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Daisy Hoopt` | `Univ.-Prof.in Daisy Hoopt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in StR DDr.in Reneé Plein` (person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Anna Mechtler-Höger` | `Mag. Anna Mechtler-Höger` |
| `VetR OMedR Constantin Wiedewilt` | `VetR OMedR Constantin Wiedewilt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich` (address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominika Oehlerich, BEd` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Isidor Czebulla` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heinz Herper` (person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Mag.a Hilde Heidorn` | `Univ.-Prof.in Mag.a Hilde Heidorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Floriane Rötker` (person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich` (address)
- `Heinz Neuböck Wthrd GmbH` (organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Anna Mechtler-Höger` | `Mag. Anna Mechtler-Höger` |
| `StR Mag. Dirk Bröders` | `StR Mag. Dirk Bröders` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `77-629/3506` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Heidemarie Lueckemeyer  in der Verwaltungsstrafsache gegen  Amber Demirdöven, Wiedneralm 4, 4906 Feichtet, Österreich, 1.) über die Beschwerde vom 07.09.2020 gegen das Straferkennt- nis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639161/2020, und 2.) über die Beschwerde vom 07.09.2020 gegen das Strafer- kenntnis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639163/2020, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der Stadt  Wien vom 24.08.2020, Geschäftszahl MA67/206700639161/2020, als unbegründet abgewie- sen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Heidemarie Lueckemeyer` | `Univ.-Prof.in Heidemarie Lueckemeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Amber Demirdöven` (person)
- `Wiedneralm 4, 4906 Feichtet, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt  Wien` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Schraders` | `Univ.-Prof.in Anastasia Schraders` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `KommR Serge Salameh` (person)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Clemens Mooß` | `Hon.-Prof. Clemens Mooß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `PROCURA Steuerberatung  GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Simone Zemanek, MSc` (person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `15-763/9594` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Charlotte Hirschmueller Silberhumerweg 2, 9163 Bodental, Österreich,  vertreten durch HR Danielle Schochert, Haßreidterstraße 75, 8831 Raiming, Österreich, über die Beschwerde vom  21. Dezember 2018 gegen die Bescheide des FA vom 28. September 2018 betreffend  Wiederaufnahme des Verfahren betreffend Einkommensteuer 2011 bis 2014,  Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014, Steuernummer  46-246/2967, zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide betreffend Wiederaufnahme des Verfahren  betreffend Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014  werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `HR Danielle Schochert` | `HR Danielle Schochert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Hirschmueller` (person)
- `Silberhumerweg 2, 9163 Bodental, Österreich` (address)
- `Haßreidterstraße 75, 8831 Raiming, Österreich` (address)
- `46-246/2967` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  Elias von Wnuk-Lipinski, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Ada Forstner` | `Univ.-Prof.in Ada Forstner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Elias von Wnuk-Lipinski` (person)
- `Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich` (address)
- `Finanzamt` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `26-066/9346` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Caroline Schröer` | `Mag.a Caroline Schröer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Beha` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Caroline Reinwaldt  in der Beschwerdesache Manuel Fortanz,  Zielgerade 30, 4950 Schwaig, Österreich, betreffend die Beschwerde vom 5. Juli 2017 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 9. Juni 2017 betreffend Umsatz- und Körperschaftsteuer 2010 bis 2015 sowie  Umsatzsteuerfestsetzung für die Zeiträume 01-03/2016, 04-06/201, 07-09/2016 und 10- 12/2016, Steuernummer , beschlossen:  Die Beschwerde wird als gegenstandslos geworden erklärt und das Verfahren eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Caroline Reinwaldt` | `Priv.-Doz.in Caroline Reinwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Manuel Fortanz` (person)
- `Zielgerade 30, 4950 Schwaig, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Daisy Große-Bölting` | `Hon.-Prof.in Daisy Große-Bölting` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Serena Leutl` (person)
- `Wanderweg 7, 2763 Thal, Österreich` (address)
- `Bernhart Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-306/6017` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ulrich Petrag` | `Mag. Ulrich Petrag` |
| `Mag. Marion Riezinger` | `Mag. Marion Riezinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natalie Nodurft` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Finanzamtes  Linz` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |
| `Mag. Monika Schmalzl` | `Mag. Monika Schmalzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Thassilo Wedekinn` | `Mag. Thassilo Wedekinn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elisabeth Hafner` (person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Dr.in Regina Manegold` | `Dr.in Regina Manegold` |
| `Dr.in KzlR Helge Erwied` | `Dr.in KzlR Helge Erwied` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterfeichten 5, 4055 Sipbach, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Müller-Dobler MBA MSc` | `Mag. Andrea Müller-Dobler MBA MSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Shoshana Döllmann` (person)
- `U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anneliese Wäsche` | `Univ.-Prof.in Anneliese Wäsche` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gernot Kirchenmayer` (person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich` (address)
- `Eckert Fries Carter Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Mag. Peter  Mayerhofer` | `Mag. Peter  Mayerhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nina Rasem` (person)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` | `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Johanesson` (person)
- `Aspangweg 17, 9781 Gailberg, Österreich` (address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `48-504/5908` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Mag. Basil Eberhards` | `Mag. Basil Eberhards` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `PhD Nancy Prätor` (person)
- `FA Linz` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Pawel Schuwirth  in der Beschwerdesache Griselda Hälmle,  Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich, über die Beschwerde vom 24. Oktober 2018 gegen die Bescheide des  Finanzamtes Landeck Reutte (jetzt Finanzamt Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und 2017, Steuernummer  49-622/1059, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Pawel Schuwirth` | `Hon.-Prof. Pawel Schuwirth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Griselda Hälmle` (person)
- `Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `49-622/1059` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Madeleine Göpffarth` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jaden Mikulla` | `Priv.-Doz.in Jaden Mikulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ida Gündüz` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Ing. Alexandra Ebermaier, MBA` (person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/132474.1`) (sent_id: `deanon_BFG_20260814_TEST/132474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Violetta Colberg  in der Beschwerdesache KzlR Kurt Bätzgen,  Alte Zeile 11, 4084 Sonnleiten, Österreich, gegen den Bescheid des FAF vom 10. Mai 2013 über die Festsetzung eines  Säumniszuschlages für die Umsatzsteuer 2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dr.in Violetta Colberg` | `Hon.-Prof.in Dr.in Violetta Colberg` |
| `KzlR Kurt Bätzgen` | `KzlR Kurt Bätzgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alte Zeile 11, 4084 Sonnleiten, Österreich` (address)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Gudrun Terzoglou  in der Beschwerdesache Ruprecht Berkenkämper,  Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich ,Land, über die Beschwerde vom 28. August 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 26. Juli 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, Steuernummer 98-086/6338, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Gudrun Terzoglou` | `Hon.-Prof.in Gudrun Terzoglou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruprecht Berkenkämper` (person)
- `Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `98-086/6338` (tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag.a Lukas Dimitrieff` | `Mag.a Lukas Dimitrieff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Marstaller` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Sonja Wennemann` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/132622.1`) (sent_id: `deanon_BFG_20260814_TEST/132622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache RgR VetR Cassandra Sczech, Hainbuchen 119, 3423 Wördern, Österreich, betreffend Beschwerde vom 22. September 2020 gegen die Bescheide  2015/2016/2017/2018 des Finanzamtes Gänserndorf Mistelbach beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `RgR VetR Cassandra Sczech` | `RgR VetR Cassandra Sczech` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hainbuchen 119, 3423 Wördern, Österreich` (address)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde der  Florentin Blatner, Hetzerstraße 11, 4712 Armau, Österreich, vom 18. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 18. Dezember 2020, Zl. MA67/Zahl/2020, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Blatner` (person)
- `Hetzerstraße 11, 4712 Armau, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt  Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hugo Pietzak` | `Priv.-Doz. Hugo Pietzak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Florens Weißer` (person)
- `Straubingerplatz 57, 4691 Römerberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `09-64-114/4837` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerden vom 18. Juni 2017 gegen die Bescheide des  Finanzamtes Bregenz vom 16. Juni 2017 betreffend Einkommensteuer 2015 und 2016  Steuernummer 88-412/8444  beschlossen:   Die Vorlageanträge vom 19.11.2018 gegen die Beschwerdevorentscheidungen vom 10.10.2018  werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Hetkemper` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerde vom 29. Mai 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 17. Mai 2018 betreffend Einkommensteuer 2017, Steuernummer  88-412/8444  zu Recht erkannt:   Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Hetkemper` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Hademar Sachteleben, MSc, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

| Predicted | Gold |
|---|---|
| `Mag. Andrea Müller-Dobler MBA MSc` | `Mag. Andrea Müller-Dobler MBA MSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hademar Sachteleben, MSc` (person)
- `Fröhlichgasse 31, 3244 Hofstetten, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Merlin Morkam` | `Hon.-Prof.in Merlin Morkam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Jens Koudela, BSc` (person)
- `Veitschersiedlung 40, 4048 Puchenau, Österreich` (address)
- `Finanzamt Salzburg-Stadt` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Dr.in Esra Schlink` | `Dr.in Esra Schlink` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Sibylle Wahlscheid` (person)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  Timon Reinhertz, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adam Rueßbült` | `Hon.-Prof. Adam Rueßbült` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timon Reinhertz` (person)
- `Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `15-325/9824` (tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

| Predicted | Gold |
|---|---|
| `Dr.in Andrea Helbok` | `Dr.in Andrea Helbok` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lydia Rehnen` (person)
- `Roßbergl 5, 4923 Gunzing, Österreich` (address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH` (organisation)
- `Finanzamtes  Innsbruck` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Sven Weichmann` | `Mag. Sven Weichmann` |
| `Mag. Kurt Kreith` | `Mag. Kurt Kreith` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Lilienfeld St. Pölten) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Richard Schwanken` | `Priv.-Doz. Richard Schwanken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexandra Hettrich` (person)
- `Kohleggweg 268, 4621 Schnarrndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Lilienfeld St. Pölten` (organisation)
- `86-148/2619` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Mag.a Heidrun Eifeler` | `Univ.-Prof.in Mag.a Heidrun Eifeler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Esra Luetje` (person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich` (address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die vorsitzende Richterin Mag. Aloisia Bergauer und die  beisitzende Richterin Mag. Andrea Ebner sowie die fachkundigen Laienrichter Mag. Johannes  Denk und Friedrich Nagl in der Beschwerdesache Dipl. Kfm. Rüdiger Schäffler, Anton-Dengler-Gasse 16, 8330 Krennach, Österreich, vertreten durch  BONAFIDE Treuhand- und Revisionsgesellschaft m.b.H., Berggasse 10, 1090 Wien, über die  Beschwerde vom 17. Oktober 2011 gegen die Bescheide des Finanzamtes Wien 12/13/14  Purkersdorf vom 11. Oktober 2011 betreffend Einkommensteuer für die Jahre 2006 bis 2009  nach Durchführung einer mündlichen Verhandlung beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Aloisia Bergauer` | `Mag. Aloisia Bergauer` |
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |
| `Mag. Johannes  Denk` | `Mag. Johannes  Denk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Friedrich Nagl` (person)
- `Dipl. Kfm. Rüdiger Schäffler` (person)
- `Anton-Dengler-Gasse 16, 8330 Krennach, Österreich` (address)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des Finanzamtes Spittal  Villach vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Hoerlin` (person)
- `Padasterjochhaus 6, 9562 Tobitsch, Österreich` (address)
- `Finanzamtes Spittal  Villach` (organisation)
- `51-093/9549` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Eizenhammer  in der Beschwerdesache KommR Ashley Tönisen,  Filzbergweg 63, 4924 Födering, Österreich, betreffend die Beschwerde vom 5. August 2011 gegen die Bescheide des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) datiert mit 22. Februar 2011  betreffend Haftung und Zahlung von Lohnsteuer sowie Festsetzung des Dienstgeberbeitrages  zum Ausgleichsfonds für Familienbeihilfen und Zuschlag zu diesem Beitrag, jeweils für die Jahre  2005 bis 2007, Steuernummer 16-543/4492,  beschlossen:    I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Eizenhammer` | `Priv.-Doz. Eckard Eizenhammer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ashley Tönisen` (person)
- `Filzbergweg 63, 4924 Födering, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-543/4492` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Aloisa Antoni, Wassermanngasse 9, 4840 Vöcklabruck, Österreich  vertreten durch die Steuerfilter Steuerberatungs-GmbH,  Ischlerbahnstraße 23, 5301 Eugendorf, über die Beschwerde vom 11. Juni 2019 und 9. Oktober  2019 gegen die Bescheide des Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich)  vom 16. Mai 2019 und 2. Oktober 2019 betreffend die Wiederaufnahme der  Einkommensteuerverfahren 2013 bis 2015 zu Recht erkannt:  I)  Die Wiederaufnahmebescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aloisa Antoni` (person)
- `Wassermanngasse 9, 4840 Vöcklabruck, Österreich` (address)
- `Steuerfilter Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Untermeier` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Dr. Christoph Ganahl` (person)
- `Finanzamtes` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` | `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentine Mugge` (person)
- `Rodlhütte 36, 9782 Plone, Österreich` (address)
- `FA Kufstein  Schwaz` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-679/2034` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag Stefan Raab` (person)
- `Leopold Pichlbauer` (person)
- `Bettina Domigall, Bakk. iur.` (person)
- `Zickhöhe 66, 3361 Biberbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Tanja Grottenthaler` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

**False Positives:**

- `Mag. Pichler` — partial — pred is substring of gold: `ECA Mag. Pichler & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Priv.-Doz. Dr` — partial — pred is substring of gold: `Priv.-Doz. Dr. Kurt Bartold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_57`)


Sie ging zu KzlR Gregor Scholt, BA einem Chirurg der wollte ihr einen Nadel reinstecken, sie  wurde dort festgehalten.

**False Positives:**

- `KzlR Gregor Scholt` — partial — pred is substring of gold: `KzlR Gregor Scholt, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Gregor Scholt, BA`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Finn van Aken, Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich, vertreten durch Mag. Musa Işlek, Achardgasse 6,  1210 Wien, über die Beschwerde vom 29. Juni 2018 gegen den Bescheid des Finanzamtes Wien  1/23 vom 28. Mai 2018 betreffend Umsatzsteuer 2016 zu Recht:   1.

**False Positives:**

- `Mag. Musa` — partial — pred is substring of gold: `Mag. Musa Işlek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Adebiola Bayer`(person)
- `Finn van Aken`(person)
- `Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich`(address)
- `Mag. Musa Işlek`(organisation)
- `Finanzamtes Wien  1/23`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Robert Bitsche` — partial — pred is substring of gold: `RA Mag. Robert Bitsche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Roxana Dellner`(person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich`(address)
- `RA Mag. Robert Bitsche`(person)
- `Magistrats der Stadt Wien`(organisation)
- `88-034/0292`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `LLB Bakk` — partial — pred is substring of gold: `Tamara Poertgen, LLB Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Babette Nimzyk`(person)
- `Tamara Poertgen, LLB Bakk. techn.`(person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich`(address)
- `Martin Friedl`(person)
- `Finanzamtes`(organisation)
- `08-216/2001`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

**False Positives:**

- `StR DDr.in Reneé Plein` — partial — pred is substring of gold: `Prof.in StR DDr.in Reneé Plein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Daisy Hoopt`(person)
- `Prof.in StR DDr.in Reneé Plein`(person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_16`)


Nachdem binnen der zweiwöchigen Frist (§ 2 Abs. 2 Wiener Parkometergesetz 2006) keine  Lenkerauskunft erteilt wurde, lastete der Magistrat der Stadt Wien, MA 67, Prof.in StR DDr.in Reneé Plein  (Beschwerdeführer, kurz: Bf.) als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin des näher bezeichneten Fahrzeuges mit Strafverfügung vom 25. März  2020, MA67/456/2020, an, dass er dem ordnungsgemäß zugestellten  Lenkerauskunftsersuchen der MA 67 vom 23. Jänner 2020 innerhalb von zwei Wochen ab  Zustellung nicht entsprochen habe.

**False Positives:**

- `StR DDr.in Reneé Plein` — partial — pred is substring of gold: `Prof.in StR DDr.in Reneé Plein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Prof.in StR DDr.in Reneé Plein`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_26`)


Relevante vorgelegte Befunde:  2009-09-29 BASB WIEN  primär chronisch progrediente Multiple Sklerose 100% GdB  2009-03-02 BEFUNDBERICHT PROF.

**False Positives:**

- `BASB WIEN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_96`)


29.9.2009, BASB Wien: primär chron.

**False Positives:**

- `BASB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_111`)


Gutachten erstellt am 31.01.2017 von Dr.in Silvia Bauer  Gutachten vidiert am 31.01.2017 von Dr.in Renate Reininger"

**False Positives:**

- `Dr.in Silvia Bauer  Gutachten` — partial — gold is substring of pred: `Dr.in Silvia Bauer`
- `Dr.in Renate` — partial — pred is substring of gold: `Dr.in Renate Reininger`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Silvia Bauer`(person)
- `Dr.in Renate Reininger`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

**False Positives:**

- `BASB-Gutachten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Universität Wien`(organisation)
- `Prof. Maida`(person)
- `Dr. Wolfgang Baischer`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_180`)


Der mit dem Gutachten vom 7. Juli 2014 befassten Gutachterin, einer Fachärztin für  Neurologie, standen im Rahmen der Gutachtenserstellung das Gutachten des BASB Wien vom  29. September 2009 und der Befundbericht von Prof. Maida vom 2. März 2009 sowie ein  Bericht der MA 15 vom 13. November 2006 zur Verfügung.

**False Positives:**

- `BASB Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Prof. Maida`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_207`)


Das Gutachten von Prof. Maida datiert mit 2. März  2009, das BASB-Gutachten  vom 29. September 2009, die Befunde/Arztbriefe der  Psychiatrischen Abteilung des SMZ-Ost aus 2012 und das Gutachten von Dr. Baischer vom 21.  Februar 2013.

**False Positives:**

- `BASB-Gutachten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Prof. Maida`(person)
- `Dr. Baischer`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der Cathleen Gröneweg, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `BA MA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cathleen Gröneweg`(person)
- `Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich`(address)
- `Finanzamtes Klagenfurt`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_307`)


Nach der Verwaltungspraxis gilt Art. 3  Abs. 8 Satz 2 auch dann, wenn der Erwerber die UID des Ausgangsmitgliedstaates der  Warenbewegung bekannt gibt (UStR Rz 3777).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `Mag. Heinrich Hambücher` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_19`)


Als Auftragnehmer fungierten - laut den  vorliegenden Eingangsrechnungen – die Firma1 GmbH, die Firma2 GmbH & CoKG, die Firma3  GmbH & CoKG, die PhD Mag. Heinrich Hambücher  und die Firma4 GmbH. Die Firma1 GmbH habe sich bei der  Leistungserbringung diverser Subunternehmer bedient, die wiederum in einem Naheverhältnis  zum Kommanditisten bzw. Komplementär der Rechtsvorgängerin & CoKG gestanden seien.

**False Positives:**

- `Mag. Heinrich Hambücher` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Firma2 GmbH & CoKG`(organisation)
- `Firma3  GmbH & CoKG`(organisation)
- `PhD Mag. Heinrich Hambücher`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_37`)


Nachdem die Rechtsvorgängerin & CoKG infolge Anwachsung der Gesellschaftsanteile nach §  142 UGB an die PhD Mag. Heinrich Hambücher  mit Wirksamkeit zum xx.xx.xxxx im Firmenbuch gelöscht worden  war, teilte die steuerliche Vertretung am 11.02.2020 mit, dass zur Rechtsnachfolgerin ein  aufrechtes Bevollmächtigungsverhältnis bestehe.

**False Positives:**

- `Mag. Heinrich Hambücher` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Mag. Heinrich Hambücher`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_75`)


ihr  Geschäftsanteil wurde von der PhD Mag. Heinrich Hambücher (FN xxxxxx) übernommen;

**False Positives:**

- `Mag. Heinrich Hambücher` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Mag. Heinrich Hambücher`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131857.1`) (sent_id: `deanon_BFG_20260814_TEST/131857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterD in der Beschwerdesache VetR Eduard van den Berge, Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich, über die Beschwerde vom 6. Juni 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 31. Mai 2019 betreffend Rückforderung Familienbeihilfe und  Kinderabsetzbetrag für September 2018 bis Mai 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `VetR Eduard` — partial — pred is substring of gold: `VetR Eduard van den Berge`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Eduard van den Berge`(person)
- `Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Petra Özkanli  in der Beschwerdesache des  Betriebes gewerblicher Art Radweg A-Tal des Tourismusverbandes A B, Dornackerstraße 480, 4352 Innernstein, Österreich  vertreten durch StB, über die Beschwerden vom 16. August 2017 gegen die Bescheide des  Finanzamt Wien 2/20/21/22  vom 2. Juni 2017 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Körperschaftsteuer 2016 und Körperschaftsteuer 2016 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Körperschaftsteuer 2016 wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Petra` — partial — pred is substring of gold: `Dr.in Petra Özkanli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Petra Özkanli`(person)
- `Dornackerstraße 480, 4352 Innernstein, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_72`)


Am 26.1.2018 (am Tag danach) seien zwei Poststücke per Einschreiben mit den  Aufgabenummern RQ … 747 und 748 versendet worden, die von Herrn Mag. Sch. auf dem  Nachhauseweg beim Postamt W. aufgegeben worden seien.

**False Positives:**

- `Mag. Sch` — partial — pred is substring of gold: `Mag. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Sch.`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

**False Positives:**

- `StR Ing` — partial — pred is substring of gold: `StR Ing. Alexandra Ebermaier, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `StR Ing. Alexandra Ebermaier, MBA`(person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `KzlR Jens Koudela` — partial — pred is substring of gold: `KzlR Jens Koudela, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Merlin Morkam`(person)
- `KzlR Jens Koudela, BSc`(person)
- `Veitschersiedlung 40, 4048 Puchenau, Österreich`(address)
- `Finanzamt Salzburg-Stadt`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

**False Positives:**

- `Mag. Pjotr` — partial — pred is substring of gold: `Mag. Pjotr Übereiter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Pjotr Übereiter`(person)
- `Linn Gouthier`(person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof. Univ` — partial — pred is substring of gold: `Univ.-Prof. Univ.-Prof. Kai Menrath`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

**False Positives:**

- `VetR Dipl` — partial — pred is substring of gold: `VetR Dipl. Kff. Ingrid Klockgiesser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `VetR Dipl. Kff. Ingrid Klockgiesser`(person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_220`)


Auch in  den UStR Rz 759 werde ausschließlich die virtuelle Währung Bitcoin erwähnt.

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Standalone Surnames in Narrative` 🏆

**F1:** 0.092 | **Precision:** 0.684 | **Recall:** 0.050  

**Format:** `regex`  
**Rule ID:** `b7143f86`  
**Description:**
Matches standalone surnames in narrative contexts where they appear as subjects or objects, specifically targeting cases like 'Frau Ekardt' or 'Karsten Sofka' that were missed. Requires a space after the first word to avoid cutting multi-word names.

**Content:**
```
(?:Frau|Herrn?)\s+([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:\s+[A-Z][a-zA-Z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.684 | 0.050 | 0.092 | 117 | 80 | 37 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 80 | 37 | 1534 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_8`)


Frau Basyurt erzielt selber keinerlei Einkünfte, auch keine (ausländischen) Kapitaleinkünfte.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_12`)


Der Familienwohnsitz ist in A1.  Pkw:Frau Basyurt benützt den Range Rover Sport, s. beiliegenden Zulassungsschein, dieser steht ihr  tagtäglich zur Verfügung.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_14`)


Frau Basyurt wurde darauf hingewiesen, dass der Pkw innerhalb der nächsten 3 Wochen in  Österreich angemeldet wird;

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_61`)


c) "Info-Schreiben" des Finanzamtes vom 4.11.2010, woraus hervorgeht:  "…Frau Basyurt hat am 27.7.2010 im FA vorgesprochen und machte folgende Angaben: s.  beiliegende Kopie der Niederschrift.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |
| `Basyurt` | `Basyurt` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_132`)


Ich war schon bei Frau Beerenbrock  da wurde mir gesagt, ich  brauche keine Befunde.

| Predicted | Gold |
|---|---|
| `Beerenbrock` | `Beerenbrock` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_36`)


Im Ermittlungsverfahren wurde bekannt gegeben, dass das Fahrzeug Herrn Vera Schliephacke  überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_40`)


Sie werden daher unter Hinweis auf Ihre Mitwirkungspﬂicht im Verwaltungsstrafverfahren,  binnen zwei Wochen ab Zustellung dieses Schreibens, aufgefordert, bekannt zu geben, wie  lange sich Herr Vera Schliephacke in Wien aufgehalten, wo er gewohnt hat und zu welchem Zweck  ihm das verfahrensgegenständliche Fahrzeug überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_108`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 01/2006  Herr Heinz Herper  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:    Die Unfähigkeit sich selbst den Unterhalt zu verschaffen ist ab 1/2006 belegbar da ab diesem  Zeitpunkt höhergradige körperliche Beeinträchtigungen vorhanden sind;

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |
| `Stavrakis` | `Stavrakis` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

| Predicted | Gold |
|---|---|
| `Dimitri Witkoski` | `Dimitri Witkoski` |

**Missed by this rule (FN):**

- `Ruckelshaußen` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Mag. Wolfgang Moser` (person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_25`)


Im Vorlagebericht wurde seitens des Finanzamtes folgende  Stellungnahme angeführt:  „Die Abgabenbehörde beantragt die Abweisung des Alleinverdienerabsetzbetrages, da Frau A.  nicht nur die von Herrn Bernett angeführten Einkünfte in Höhe von 5.118,52 Euro erzielt hat,  sondern auch eine Abfertigung von der Vorsorgekasse erhalten hat.

| Predicted | Gold |
|---|---|
| `Bernett` | `Bernett` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_8`)


Mit fristgerechter E-Mail vom 13. März 2021 (Anhang: Lenkerauskunft) nannte die  Zulassungsbesitzerin Herrn Bodewein als jene Person, der das genannte Kraftfahrzeug zum  Beanstandungszeitpunkt überlassen war.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_9`)


Mit Strafverfügung vom 16. März 2021 zu Zahl MA67/Zahl1/2020 lastete der Magistrat der  Stadt Wien, MA 67,Herrn Bodewein an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Autonummer (A) am 16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen  Kurzparkzone in 1020 Wien, Abstellort abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_11`)


Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2  Wiener Parkometerabgabeverordung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 wurde  über Herrn Bodewein eine Geldstrafe iHv € 60,00 und für den Uneinbringlichkeitsfall eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_14`)


Mit Schreiben des Magistrates der Stadt Wien, MA 67 vom 21. April 2021  (Verfahrensanordnung – Nachreichung Unterschrift bzw. Vollmachtsvorlage) wurde die Firma  X_KG zur Vorlage einer Vollmacht, aus welcher das Vertetungsverhältnis zu Herrn Bodewein sowie die  Berechtigung zur Einbringung des Rechtsmittels hervorgehe, binnen zwei Wochen nach  Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_16`)


Der Magistrat der Stadt Wien, MA 67, erließ an Herrn X einen mit 10. Mai 2021 datierten  Bescheid, mit welchem der Einspruch vom 21.03.2021 gegen die an Herrn Bodewein gerichtete  Strafverfügung vom 16.03.2021 infolge der Nichtvorlage der Vollmacht gemäß § 13 Abs. 3 AVG  als unzulässig zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_22`)


Herr Bodewein brachte mit E-Mail vom 15. September 2021 unter Angabe der GZ. MA67/Zahl1/2020  folgende Eingabe beim Magistrat der Stadt Wien ein:  „ich habe eine Mahnung bekommen, dass nicht weiß, wann und wo ich bestraft wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_31`)


Herr Bodewein müsste gemäß § 14 Abs. 2 Satz 2  VwGVG in der Fassung BGBl. I 109/2021 eine Mitteilung des Magistrates der Stadt Wien über  die Vorlage der (vermeintlichen) Beschwerde an das BFG erhalten haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `BFG` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_34`)


Das Anbringen, welches Herr Bodewein per E-Mail am 15. September 2021 beim Magistrat der Stadt  Wien eingebracht hat, ist keine Beschwerde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_39`)


Erst ein Telefonat zwischen Magistrat der Stadt Wien und Herrn Bodewein hat ergeben, dass es sich  um beim Anbringen vom 15. September 2021 um eine Beschwerde handeln solle.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_59`)


Für Herrn Bodewein geht hingegen die absolute Unzulässigkeit einer Revision gemäß § 25a Abs. 4  VwGG vor (siehe Rechtsmittelbelehrung).

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_14`)


Herr Julia Reittinger  ist voraussichtlich dauernd außerstande sich selbst den Unterhalt zu  verschaffen: NEIN

| Predicted | Gold |
|---|---|
| `Julia Reittinger` | `Julia Reittinger` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

| Predicted | Gold |
|---|---|
| `Franziska Fitzmann` | `Franziska Fitzmann` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_23`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grund- lage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_74`)


So hatte Frau Thyssen erst vor wenigen  Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass der EU-Vertrag  jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grundlage der Nationa- lität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_184`)


In dieser wird auf den Schriftsatz der Frau DI DM vom 10.3.2016 – als „integrierenden  Bestandteil“ der Beschwerdeschrift des Bf. – verwiesen.

| Predicted | Gold |
|---|---|
| `DI DM` | `DI DM` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_26`)


Im Vorlageantrag wird ausgeführt:  „Herr B ist nach Angaben meines Mandanten erst im Sommer 2013 nach Österreich gekommen  und war ausschließlich für Herrn Mathusczyk tätig.

| Predicted | Gold |
|---|---|
| `Mathusczyk` | `Mathusczyk` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr Katharina Bauckholt (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Katharina Bauckholt` | `Katharina Bauckholt` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_17`)


Im Gegenteil war es so, daß  die Touristik Werkvalbach GmbH die fälligen Gebäudemieten, welche an Herrn Jeanne Kraenzlin  zu zahlen gewesen  wären, nicht bedienen konnte.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Missed by this rule (FN):**

- `Touristik Werkvalbach GmbH` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_54`)


Der Verzicht wurde somit vom steuerlichen  Vertreter - auch im Namen von Herrn Jeanne Kraenzlin - abgegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)


Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn Jeanne Kraenzlin) getragen wird.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_38`)


Mit Aktenvermerk vom 20. April 2023 hielt die Magistratsabteilung 67 zur gegenständlichen  Geschäftszahl fest, ein Telefonat mit PÜG Dienstführung 1,Herr Mayerer (DW TelNr) habe  ergeben, das Überwachungsorgan DNr. ANr habe am Beanstandungstag (10.11.2022) im 22.

| Predicted | Gold |
|---|---|
| `Mayerer` | `Mayerer` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)


Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr Istvan  Melniczenko (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Istvan  Melniczenko` | `Istvan  Melniczenko` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_7`)


Herr Nadine Millradt  schulde ihm noch ausstehende Gehälter.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_12`)


Sollte Herr Nadine Millradt  die Vorsteuer zum Abzug gebracht haben, müsse sie von ihm zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_24`)


In der Begründung wird dazu ausgeführt:  „Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 8,4 Liter  Alkohol unter Abfindung, wobei diese Menge als "Hausbrand" steuerfrei belassen werden  sollte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_25`)


Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 15 Liter  Alkohol unter Abfindung, wobei diese Mengen als "Hausbrand" ebenfalls steuerfrei belassen  werden sollte.“

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_33`)


In der Begründung wurde ausgeführt: „Nach dem Auszug "Abfrage  Abfindungsberechtigte/Person" vom 31.08.2018 des Zollamtes Innsbruck war Herr Quentin Schwartkopp  jedenfalls als Abfindungsberechtigter ausgewiesen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_37`)


Mit Schreiben des Zollamtes Innsbruck vom 14.01.2019, GZ 800000/thrhtr, wurde Herr  Quentin Schwartkopp  zur Abgabe einer Stellungnahme gemäß § 115 BAO eingeladen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_38`)


Mit Schreiben vom  29.01.2019 gab Herr Quentin Schwartkopp  an, dass er nach Übergabe seines Hofes an seinen Sohn Sohn  mit diesem mündlich vereinbart habe, dass er die Obstveredelung weiterhin als  Fruchtgenussberechtigter betreiben dürfe.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_41`)


Überdies hätte Herr Quentin Schwartkopp  auch  vor der Übertragung des land- und forstwirtschaftlichen Betriebes die Freimenge für Herrn  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_142`)


Soweit der Bf. darauf verweist, dass Herr Abersfeller aus Gewerbebetrieb  erzielt bzw bei der SVA pflichtversichert sei, mag zwar richtig sein, ist aber bedeutungslos:  Aufgrund des funktionalen Verständnisses des Begriffes der Eingliederung gemäß der zitierten  Judikatur des VwGH ist es ohne Bedeutung, in welcher Weise die aus der Tätigkeit erzielten  Einkünfte zu qualifizieren wären;

| Predicted | Gold |
|---|---|
| `Abersfeller` | `Abersfeller` |

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

| Predicted | Gold |
|---|---|
| `Dominik Barfusz` | `Dominik Barfusz` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_34`)


Herr Corvin Billmaier  hat die Ausgaben getragen und bezahlt und Ausgaben sind bei jenem  abzugsfähig, der sie bezahlt hat und nicht bei jenem, den sie betroffen hätten.

| Predicted | Gold |
|---|---|
| `Corvin Billmaier` | `Corvin Billmaier` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Gudrun Joehnk` | `Gudrun Joehnk` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_38`)


Sie sehen im Anhang dass Herr Abeles damit bis 27 Dezember  gefahren ist.

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_41`)


Der Beschwerde waren zahlreiche Unterlagen zum Beweis dafür beigelegt, dass der Bf. nie mit  dem Kraftfahrzeug mit dem behördlichen Kennzeichen 123 gefahren sei und dass Herr Abeles bis  27. Dezember 2023 gefahren sei (bzw. an diesem Tag das Leasing Auto zurückgegeben habe).

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_47`)


Erst im Einspruch vom 18. März 2024 gegen die beiden Strafverfügungen vom 11. März  2024, GZ. 1) MA67/GZ1/2024 und 2) MA67/GZ2/2024, brachte der Bf. erstmals vor, dass das in  Rede stehende Fahrzeug zur jeweiligen Beanstandungszeit von Herrn Schwent gelenkt wurde.

| Predicted | Gold |
|---|---|
| `Schwent` | `Schwent` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_8`)


Begründung  Verlauf des Verfahrens  Mit Straferkenntnis vom 27. Dezember 2023, GZ MA67/111111/2023, hat der Magistrat der  Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Arthur Soyal (in weiterer Folge:  Beschwerdeführer) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt, indem er  das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen W-6789 (A) am 4. August  2023 um 11:10 Uhr in einer gebührenpflichtigen Kurzparkzone in 1160 Wien, Hasnerstraße  129, abgestellt habe, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Arthur Soyal` | `Arthur Soyal` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung vom 4. Juni 2024, GZ. MA67/GZ/2024, lastete der Magistrat der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde Frau Manhardt an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 4. April 2024 um  12:24 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien, Helenengasse zwischen  Praterstern und Hedwiggasse rechts, abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_5`)


Demnach habe Frau Manhardt die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_8`)


Mit an die Magistratsabteilung 67 gesendeter E-Mail vom 12. Juni 2024 erstattete Herr  Jeanne Pavlovitsch (in der Folge: Beschwerdeführer) eine von der belangten Behörde als Einspruch  gegen die Strafverfügung vom 4. Juni 2024 gewertete Eingabe.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_9`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertetungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_39`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_66`)


Nach der Aktenlage wurde der Einspruch gegen die an Frau Manhardt ergangene  Strafverfügung vom Beschwerdeführer erhoben, eine Vollmacht wurde jedoch (trotz  Aufforderung durch die belangte Behörde) nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_21`)


Nach telefonischer Rücksprache mit Frau Lensen füge ich das ganze nochmals als  Anhang hinzu.“

| Predicted | Gold |
|---|---|
| `Lensen` | `Lensen` |

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_16`)


Der E-Mail vom 5. Februar 2025 war folgende Vollmacht beigelegt:   „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024 , wohnt Adr1, den  Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt  Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte Akzeptieren Sie das  Einspruch.“

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_31`)


Mit E-Mail vom 5. Februar 2025 übermittelte der Beschwerdeführer ein Schreiben des M mit  folgendem Inhalt: „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024,  wohnt Adr1, den Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu  Magistrat der Stadt Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte  Akzeptieren Sie das Einspruch“.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_44`)


Der belangten Behörde ist zwar zuzustimmen, dass die schriftliche Vollmacht mit  5. Februar 2025 datiert und somit erst nach der Verfahrenshandlung (Erhebung des  Einspruches) vom 10. September 2024 errichtet wurde, die Behörde lässt hierbei jedoch außer  Betracht, dass es sich sowohl bei dem Beschwerdeführer als auch bei dem Vollmachtgeber um  Personen mit offenkundig mangelnden Sprachkenntnissen handelt. Aus der gewählten  Ausdrucksweise lässt sich nach Ansicht des Bundesfinanzgerichts jedoch ableiten, dass der  Beschwerdeführer bereits vor der Verschriftlichung der Vollmacht, nämlich bereits im  Zeitpunkt der Setzung der Verfahrenshandlung am 10. September 2024 mündlich von M zur  Erhebung eines Einspruches gegen die Strafverfügung bevollmächtigt war (Arg: „[…] Herrn  Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt Wien  Magistratsabteilung 67 schicken […]“).

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_5`)


Entscheidungsgründe  Nach dem das Finanzamt in der Beschwerdevorentscheidung (BVE) vom 17.11.2023 das  Pendlerpauschale, den Pendlereuro und den Alleinerzieherabsetzbetrag antragsgemäß  steuermindernd berücksichtigt hat, ist nur mehr strittig, ob sogenannte Familienheimfahrten  von Frau Kuehnhanss (in der Folge: Beschwerdeführerin: Bf) vorliegen und als Werbungskosten zu  berücksichtigen sind.

| Predicted | Gold |
|---|---|
| `Kuehnhanss` | `Kuehnhanss` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Basyurt`(person)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_17`)


Herr Bf benützt für seine Wochenendfahrten nach A1 einen anderen Pkw.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_18`)


Herr Bf-Gatte ist während der Woche in D-XY whft und in A1 nicht gemeldet;

**False Positives:**

- `Bf-Gatte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

**False Positives:**

- `Bf-Gatte` — no gold match — likely missing annotation
- `Bf-Gatte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Basyurt`(person)
- `Basyurt`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_18`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf hat seinen Familienwohnsitz gemeinsam mit seinen Kindern (im Beschwerdejahr 8 und  12 Jahre alt) in Ungarn, wo weder er noch seine Frau Einkünfte erzielen.

**False Positives:**

- `Eink` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_60`)


Auch gibt die Tante des Beschwerdeführers,Frau Freßdorf  an, dass sich  mit Beginn des Studiums zunehmend gegenüber seiner Umwelt verschloss und sich immer  4 von 21 Seite 5 von 21

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_63`)


Zur Untersuchung beim Bundessozialamt wurde der Beschwerdeführer von Frau Unverdroß  einer  Betreuerin der Einrichtung, in welcher der Beschwerdeführer betreut wird, begleitet.

**False Positives:**

- `Unverdro` — partial — pred is substring of gold: `Unverdroß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unverdroß`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`
- `Unverdro` — partial — pred is substring of gold: `Unverdroß`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_72`)


Bei der Erstellung des fachärztlichen Sachverständigengutachtens durch das Bundessozialamt  fanden weder der Befund der Stellungskommission noch die Aussagen von Frau Unverdroß  entsprechende Berücksichtigung.

**False Positives:**

- `Unverdro` — partial — pred is substring of gold: `Unverdroß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unverdroß`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_122`)


Herr Bf ist im Wesentlichen in der Lage, einfache Sachverhalte zu erfassen, zeigt sich bei  komplexeren Anforderungen allerdings überfordert.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_140`)


In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Der Rechtsanwalt verwies auf die Aufführungen in der Beschwerde sowie auf die beantragten  Zeugen, insbesondere auf die Tante des Beschwerdeführers (Bf.),Frau Freßdorf  die Aussagen zu dem  damaligen Gesundheitszustand des Bf. während seines Studiums treffen könne.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Freßdorf`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_200`)


Laut Sachwalter habe Frau Freßdorf (Tante des Bf.) erzählt, dass sich ihr Neffe mit Beginn des  Studiums zunehmend gegenüber seiner Umwelt verschlossen und sich immer mehr  zurückgezogen habe, was sich dadurch geäußert habe, dass er keinen Kontakt mit der Familie  haben wollte und auch gemeinsamen Familienaktivitäten ferngeblieben sei.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_218`)


Lebensjahr (bzw. dem 25. Lebensjahr) eingetreten ist,  brachte Frau Freßdorf doch nur vor, dass sich ihr Neffe mit Beginn des Studiums zunehmend  gegenüber seiner Umwelt verschlossen und sich immer mehr zurückgezogen habe, was sich  dadurch geäußert habe, dass er keinen Kontakt mit der Familie haben wollte und auch  gemeinsamen Familienaktivitäten ferngeblieben sei.

**False Positives:**

- `Fre` — partial — pred is substring of gold: `Freßdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

**False Positives:**

- `Ruckelshau` — partial — pred is substring of gold: `Ruckelshaußen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dimitri Witkoski`(person)
- `Ruckelshaußen`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_45`)


Nach Antwort von Herrn Ruckelshaußen vom 04.08.2015 betreffend  „asymmetrische Arrondierung und Immo-Est-Befreiung“ kommt im wörtlichen Sinne die  Befreiungsbestimmung des § 30 Abs 2 Z 4 EStG immer für denjenigen zur Anwendung, bei dem  ein Grundstückstausch einen Flurbereinigungsvorgang darstellt. Wenn für einen Tauschpartner  eine Flurbereinigung gegeben ist (und auch ein Tausch und keine Veräußerung vorliegt - dh  keine Aufzahlungen über 50%), dann greift für diesen die Befreiung, wohingegen der andere  Tauschpartner steuerpflichtig ist.

**False Positives:**

- `Ruckelshau` — partial — pred is substring of gold: `Ruckelshaußen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ruckelshaußen`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_34`)


Dazu wird auch auf den Bauvertrag und die Treuhandvereinbarung verwiesen, den die Firma  MH-Bau GmbH am 5.3.2015 unterfertigt hat und der in weiterer Folge am 18.3.2015 auch von  den Käufern in der Kanzlei von Herrn Dr-F, der die treuhändige Abwicklung übernommen hatte,  unterfertigt wurde.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MH-Bau GmbH`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_19`)


Zum  Masseverwalter wurde Herr Mag. G H bestellt.  Gesellschafter der AB sind Herr C D und die Verlassenschaft nach E F. Geschäftsführer waren  Herr C D und bis zu seinem Tod im Jahr 2011 Herr E F.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_126`)


Am 27. Juli 2022 teilte die Magistratsabteilung 67 (Frau Frau1) auf Nachfrage des  Bundesfinanzgerichtes mit, dass die Bf. entgegen ihren Beschwerdeausführungen bis dato  keine weitere Einzahlung zu gegenständlicher GZ. leistete.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_116`)


Das telefonische Vor - Aviso dieser Vorgangsweise wurde letzte Woche zwischen Dr. Kohlfürst  und Herrn Amtsdirektor V abgestimmt.

**False Positives:**

- `Amtsdirektor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Kohlfürst`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_87`)


Daher wurden bei Frau DM Abfragen zu den igE und igL  durchgeführt.

**False Positives:**

- `DM Abfragen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_31`)


Das Finanzamt hat dazu folgende Stellungnahme abgegeben:  „Der Mehmet Köprücü  gab am 20.04.2022 seine Vollmacht für das Haftungsverfahren  Evamaria Watenphul  bekannt und beschrieb sie wortwörtlich so:  Haftungsbescheide je vom 23.03.2022  Und:  In der außen bezeichneten Finanzsache haben die Beschwerdeführer … Evamaria Watenphul, … als  ehemalige Geschäftsführer der Özyilmaz Recycling GmbH., Herrn Mehmet Köprücü  Vollmacht erteilt,  wobei sich der gefertigte Anwalt auf diesem ihm erteilte Vollmacht beruft.

**False Positives:**

- `Mehmet` — similar text (different position): `Mehmet Köprücü`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Mehmet Köprücü`(person)
- `Evamaria Watenphul`(person)
- `Evamaria Watenphul`(person)
- `Özyilmaz Recycling GmbH.`(organisation)
- `Mehmet Köprücü`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)
- `Quentin Schwartkopp`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_36`)


Herr Sohn wurde zwischenzeitlich gemäß § 62 AlKStG als Abfindungsberechtigter  registriert.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_40`)


Unter Hinweis auf §§ 2 Abs. 1, 4 Abs. 2 Z 5, 8 Abs. 1 Z 2, § 9 Abs. 1 Ziffer 2, § 62 Abs. 2 Z 3, 64  Abs. 3 AlkStG betonte das Zollamt, dass durch den Übergabevertrag vom eee2011 Herr Sohn  unzweifelhaft Eigentümer an den Früchten (= alkoholbildende Stoffe) wurde; auf mündliche  Absprachen zwischen Vater und Sohn komme es nicht an.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_81`)


Herr Sohn hat seit 03.bbb.2013 seinen aktuellen  ordentlichen Wohnsitz (Hauptwohnsitz) in Adresse_Sohn.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

**False Positives:**

- `Manhardt  AdresseBeschuldigte` — partial — gold is substring of pred: `Manhardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Manhardt`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_108`)


Im erwähnten Straferkenntnis vom  7.11.2022 hat die belangte Behörde diese Ermittlungsergebnisse auch wiedergegeben und  dazu auszugsweise wie folgt ausgeführt:  „Ermittlungen ergaben, dass für Herrn Rudolf B kein Ausweis gemäß § 29b StVO ausgestellt  wurde.

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_110`)


……  Im Übrigen ist auch der lt. Anzeigeangaben im Fahrzeug nicht gut erkennbar hinter der  Windschutzscheibe eingelegte Parkausweis gemäß § 29b StVO, dessen Ausweisnummer  teilweise durch eine Postkarte verdeckt war, nicht für Herrn Rudolf B ausgestellt.“

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_17`)


Mit Schreiben vom 4. März 2025 teilte die belangte Behörde dem Bf. mit, mit Lenkerauskunft  vom 03.03.2025 zur Zahl MA67/GZ1/2024 habe er Herrn Lenker1, geb. am geb, als Lenker des  Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 am 20.11.2024 um 17:06 Uhr namhaft  gemacht.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_36`)


Auch die  Tatsache, dass der Bf. im Einspruch gegen die an ihn ergangene Strafverfügung (wegen  Erteilung einer unrichtigen Lenkerauskunft) eine dritte Person, nämlich Herrn Lenker5 als  Lenker genannt habe, wohingegen der Bf. in seiner Lenkerauskunft vom 03.03.2025 Herrn  Lenker4 angeführt habe, spreche dafür, dass es sich bei der Angabe des bzw. der vom Bf.  genannten Lenker um eine reine Schutzbehauptung handle.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation
- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_91`)


In der fristgerecht beantworteten Lenkererhebung vom 26. Februar 2025  gab er hingegen Herrn Lenker1 als Lenker an, der zum Zeitpunkt der Auskunft wiederum  keinen Wohnsitz in Österreich hatte.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names after 'vertreten durch' (Tightened)` 🏆

**F1:** 0.018 | **Precision:** 0.366 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `111f011a`  
**Description:**
Matches names following 'vertreten durch' ensuring the full name including titles is captured, but explicitly excludes company names by requiring a comma or end-of-string immediately after the name (or a known person suffix).

**Content:**
```
(?:vertreten durch)\s+([A-Z][a-zA-Z]+(?:[ -][A-Z][a-zA-Z]+)+)(?=,|$|[.](?!.*(?:GmbH|AG|Gesellschaft|Partnerschaft|OG|m\.b\.H)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.366 | 0.009 | 0.018 | 41 | 15 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 15 | 26 | 1599 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Babette Nimzyk` (person)
- `Tamara Poertgen, LLB Bakk. techn.` (person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich` (address)
- `Finanzamtes` (organisation)
- `08-216/2001` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Krampl` | `Thomas Krampl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Fabienne Kattner` (person)
- `Cornelia Özgür` (person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Sonja Wennemann` | `Sonja Wennemann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Lukas Dimitrieff` (person)
- `Juri Marstaller` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Christina Hildegard Stowasser` | `Christina Hildegard Stowasser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Wieland Starnberg` (person)
- `Ing. Linus Feyerherdt` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alfred Klaus Fenzl` | `Alfred Klaus Fenzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Prof. Leander Pfleumer, LLM` (person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich` (address)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `11-306/0925` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Delila Holsträter, Bakk. iur. BEd, Ziegelsdorf 25, 4723 Unterhörzing, Österreich, vertreten durch Harald Andreas Rumpler, Mattersburgerstraße 70, 7022 Schattendorf,  über die Beschwerde vom 24. September 2018 gegen den Bescheid des Finanzamtes  Österreich vom 22. August 2018 betreffend Einkommensteuer 2016 Steuernummer  76-140/9765  zu Recht erkannt:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Harald Andreas Rumpler` | `Harald Andreas Rumpler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Delila Holsträter, Bakk. iur. BEd` (person)
- `Ziegelsdorf 25, 4723 Unterhörzing, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `76-140/9765` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Anton Fleischhacker` | `Anton Fleischhacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Christine Kralova` (person)
- `Merlin Leuprecht` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Julia Reittinger, Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich, vertreten durch Annemarie Entschev-Kurzmann, Mariahilfer Straße  140 Tür 10, 1150 Wien, vom 25. November 2020, gegen den Bescheid des Finanzamtes  Österreich vom 10. November 2020 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe und des Erhöhungsbetrages ab März 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Entschev-Kurzmann` | `Annemarie Entschev-Kurzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Julia Reittinger` (person)
- `Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Walther Kendler` | `Walther Kendler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Brendon Spade` (person)
- `OMedR Milena Piechulik` (person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich` (address)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `16-827/1246` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Flora Tahir, Sommeregg 24, 9634 Oberbuchach, Österreich, vertreten durch Renate Dolezal, Speisinger Str 50-52 Tür 18, 1130  Wien, über die Beschwerde vom 5. Oktober 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. September 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016, Steuernummer 20-636/7581, beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Renate Dolezal` | `Renate Dolezal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Konrad` (person)
- `Flora Tahir` (person)
- `Sommeregg 24, 9634 Oberbuchach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `20-636/7581` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/144232.1`) (sent_id: `deanon_BFG_20260814_TEST/144232.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat in der  Beschwerdesache Fiona Reckerth, Am Tasen 60, 4941 Mehrnbach, Österreich  vertreten durch RA Michael Lux, Lange Weg 118,  B-3090 Overjise und DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Währinger Straße 2-4,  1090 Wien, Steuernummer: 03-123/0344, über die Beschwerde vom 15. Dezember 2023  gegen den Bescheid des Finanzamtes Österreich vom 28. November 2023 betreffend  Zurückweisung des Antrages auf Erteilung einer Fiskalvertreter-USt-ID Nummer gemäß § 27  Abs 8 UStG zu Recht:  I)  Der angefochtene Bescheid wird aufgehoben.

| Predicted | Gold |
|---|---|
| `RA Michael Lux` | `RA Michael Lux` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Günter Narat` (person)
- `Fiona Reckerth` (person)
- `Am Tasen 60, 4941 Mehrnbach, Österreich` (address)
- `DSC Doralt Seist Csoklich Rechtsanwälte GmbH` (organisation)
- `03-123/0344` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/147296.1`) (sent_id: `deanon_BFG_20260814_TEST/147296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Erwin Nikolasen  in der Beschwerdesache Doris Weierstahl,  Minibandlweg 18, 9473 Wunderstätten, Österreich, vertreten durch Kirstin Ever, Minibandlweg 18, 9473 Wunderstätten, Österreich, über die Beschwerde vom  21. Mai 2019 gegen den Bescheid des Finanzamtes Salzburg-Land (nun Finanzamt Österreich)  vom 9. Mai 2019 betreffend Säumniszuschlag 2018, Steuernummer 57-656/9365, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kirstin Ever` | `Kirstin Ever` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Erwin Nikolasen` (person)
- `Doris Weierstahl` (person)
- `Minibandlweg 18, 9473 Wunderstätten, Österreich` (address)
- `Minibandlweg 18, 9473 Wunderstätten, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)
- `57-656/9365` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_51`)


Daraus folgt, dass der Einspruch gegen die Strafverfügung vom 3. September 2024 des M,  vertreten durch Pjotr Niessl, wieder unerledigt ist und die belangte Behörde darüber zu  entscheiden hat.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/148979.1`) (sent_id: `deanon_BFG_20260814_TEST/148979.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Janosch Postema  in der Beschwerdesache Juri Gübele,  Gartnerweg 4, 5145 Eisenhub, Österreich, vertreten durch Lydia Alberth, Steuerberaterin, Am Hochsteg 13, 8434  Tillmitsch, betreffend die Beschwerde vom 23.4.2025 gegen den Bescheid des Finanzamtes  Österreich vom 28.1.2025 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm  § 111 BAO in Höhe von 1.000,00 Euro beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lydia Alberth` | `Lydia Alberth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Janosch Postema` (person)
- `Juri Gübele` (person)
- `Gartnerweg 4, 5145 Eisenhub, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/149201.1`) (sent_id: `deanon_BFG_20260814_TEST/149201.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Sven Pertsch  in der Beschwerdesache Hugo Ossiander,  Streit 58, 5204 Hochfeld, Österreich, vertreten durch Vlado Jovic, Meilstraße 7 Tür 5, 6170 Zirl, betreffend  Beschwerde vom 19. November 2024 gegen den Bescheid des Finanzamt Linz  vom 26. September  2024 betreffend Feststellung der Einkünfte § 188 BAO 2023, Steuernummer 75-331/1938,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm. § 278 Abs. 1 lit a BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vlado Jovic` | `Vlado Jovic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Sven Pertsch` (person)
- `Hugo Ossiander` (person)
- `Streit 58, 5204 Hochfeld, Österreich` (address)
- `Finanzamt Linz` (organisation)
- `75-331/1938` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

**False Positives:**

- `Steuerberatungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

**False Positives:**

- `TPA Steuerberatung GmbH` — type mismatch — same span as gold: `TPA Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Isidor Czebulla`(person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich`(address)
- `TPA Steuerberatung GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Bernhart Steuerberatungs GmbH` — type mismatch — same span as gold: `Bernhart Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_13`)


Der Spruch lautet:  „Es ergeht die Beschwerdevorentscheidung betreffend die Beschwerde vom 27.03.2018 des Bf.,  vertreten durch Steuerberater XY, gegen Körperschaftsteuer 2013, 2014, 2015;

**False Positives:**

- `Steuerberater XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft` — type mismatch — same span as gold: `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lisa Lindnau`(person)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich`(address)
- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `35-287/7417`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

**False Positives:**

- `APP Steuerberatung GmbH` — type mismatch — same span as gold: `APP Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Dr. Ashley Nagelschmidt`(person)
- `Hollenbach 37, 4872 Unterthumberg, Österreich`(address)
- `APP Steuerberatung GmbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `Finanzamt für Großbetriebe`(organisation)
- `16-165/9893`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Gutwirth Consulting Steuerberatungs GmbH` — partial — pred is substring of gold: `Gutwirth Consulting Steuerberatungs GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Prof.in Jeanne Sohns`(person)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich`(address)
- `Gutwirth Consulting Steuerberatungs GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lieselotte Stiglat  in der Beschwerdesache Sibylle Roßmayr,  Sierling 20, 3632 Pernthon, Österreich, vertreten durch RSM Austria Steuerberatung GmbH, Tegetthoffstraße 7, 1010  Wien, über die Beschwerde vom 16.11.2021 gegen den Bescheid des Finanzamtes Österreich  vom 5. November 2021 betreffend Verspätungszuschlag Umsatzsteuer 4-06/2021,  Steuernummer 58-418/2406  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `RSM Austria Steuerberatung GmbH` — type mismatch — same span as gold: `RSM Austria Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Lieselotte Stiglat`(person)
- `Sibylle Roßmayr`(person)
- `Sierling 20, 3632 Pernthon, Österreich`(address)
- `RSM Austria Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `58-418/2406`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Techn R Edwin Lamken, Steindl 32, 4076 Lengau, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse 17,  1030 Wien, wegen Verletzung der Entscheidungspflicht betreffend die Beschwerde gegen den  Bescheid des Finanzamtes Österreich vom 29.07.2009 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Umsatzsteuer 2006 der Gammersbach&Pelstring Telekom GmbH  Steuernummer 53-479/4428  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm § 284 Abs. 7 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Caroline Toifl Rechtsanwalt GmbH` — type mismatch — same span as gold: `Caroline Toifl Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Helmut Mittermayr`(person)
- `Techn R Edwin Lamken`(person)
- `Steindl 32, 4076 Lengau, Österreich`(address)
- `Caroline Toifl Rechtsanwalt GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `Gammersbach&Pelstring Telekom GmbH`(organisation)
- `53-479/4428`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Causa Wirtschaftstreuhand GmbH` — type mismatch — same span as gold: `Causa Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Frederik von Gruber`(person)
- `Laila Klimenkow`(person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich`(address)
- `Causa Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Alva Danell, Robert Lieben-Promenade 68, 5251 Thalheim, Österreich, vertreten durch Nikolaus WP GmbH Rnf. ÖBUG KG, St Veitg 8, 1130  Wien, über die Beschwerde vom 6. März 2014 gegen den Bescheid des Finanzamtes Wien  9/18/19 Klosterneuburg vom 10. Februar 2014 betreffend Einkommensteuer 2012  Steuernummer 48-595/6877  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Nikolaus WP GmbH Rnf` — partial — pred is substring of gold: `Nikolaus WP GmbH Rnf. ÖBUG KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Stefan Pipal`(person)
- `Alva Danell`(person)
- `Robert Lieben-Promenade 68, 5251 Thalheim, Österreich`(address)
- `Nikolaus WP GmbH Rnf. ÖBUG KG`(organisation)
- `Finanzamtes Wien  9/18/19 Klosterneuburg`(organisation)
- `48-595/6877`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  Simone Philipzig, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hofer Leitinger Steuerberatung GmbH` — type mismatch — same span as gold: `Hofer Leitinger Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Philippa Beßerdich`(person)
- `Simone Philipzig`(person)
- `Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich`(address)
- `Hofer Leitinger Steuerberatung GmbH`(organisation)
- `FA Kirchdorf Perg Steyr`(organisation)
- `59-060/2086`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Olivia Severien  in der Beschwerdesache  Denis Öztopal, Weidenbachstraße 3, 5131 Pimbach, Österreich, vertreten durch Pschera Steuerberatung GmbH, Gösser Straße 60,  8700 Leoben, über die Beschwerde vom 20. November 2013 gegen die zur Steuernummer 68- 060/6613 ergangenen Bescheide des Finanzamt Salzburg-Stadt (nun Dienststelle des Finanzamtes Österreich)  vom 22. Oktober 2013 betreffend Umsatz- und Einkommensteuer 2000  – 2010 zu Recht  erkannt:   I. Die Berufung/Beschwerde vom 20. Nov.

**False Positives:**

- `Pschera Steuerberatung GmbH` — type mismatch — same span as gold: `Pschera Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Olivia Severien`(person)
- `Denis Öztopal`(person)
- `Weidenbachstraße 3, 5131 Pimbach, Österreich`(address)
- `Pschera Steuerberatung GmbH`(organisation)
- `Finanzamt Salzburg-Stadt`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Janet Köhle  in der Beschwerdesache der  Textil Bermon, Hans-Bachmann-Straße 4, 2872 Langegg, Österreich  vertreten durch RA-Vertreter, über die Beschwerde vom 31. Mai  2017 gegen die zur Steuernummer 91-124/4580  ergangenen Bescheide des FA St. Johann Tamsweg Zell am See (jetzt  Dienststelle des Finanzamtes Österreich) vom 30. März 2017 betreffend  Einkommensteuer 2009 – 2014 nach Durchführung einer mündlichen Verhandlung am  15.März 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `RA-Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Janet Köhle`(person)
- `Textil Bermon`(organisation)
- `Hans-Bachmann-Straße 4, 2872 Langegg, Österreich`(address)
- `91-124/4580`(tax_number)
- `FA St. Johann Tamsweg Zell am See`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/141952.1`) (sent_id: `deanon_BFG_20260814_TEST/141952.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Niklas Dankwarth, Schüttaustraße 10, 9753 Raggnitz, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse  17, 1030 Wien, über die Beschwerde vom 24. September 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. August 2020 betreffend Einkommensteuer 2018  Steuernummer 01-612/4118  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Caroline Toifl Rechtsanwalt GmbH` — type mismatch — same span as gold: `Caroline Toifl Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Niklas Dankwarth`(person)
- `Schüttaustraße 10, 9753 Raggnitz, Österreich`(address)
- `Caroline Toifl Rechtsanwalt GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `01-612/4118`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. VN. NN., die Richterin Dr.in  Ri.N. sowie die fachkundigen Laienrichter Lena Pahlmann und Ch,Nn. in der Beschwerdesache  Esra Voskuhle, Brandstetterweg 76k, 4682 Buchet, Österreich, vertreten durch Beratungs GmbH, Str.x, plz Stadt, über die  Beschwerde vom 26. Juni 2019 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich Dienststelle  Sonderzuständigkeiten) vom 27. Mai 2019 betreffend Gebühren gemäß § 33 TP 20  Gebührengesetz (GebG) 1957 nach Durchführung einer mündlichen Verhandlung am  12. Oktober 2023 in Anwesenheit des Beschwerdeführers und dessen Ehegattin A.N.G und der  Schriftführerin Vn. Nn1 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Beratungs GmbH` — type mismatch — same span as gold: `Beratungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in  Ri.N.`(person)
- `Lena Pahlmann`(person)
- `Esra Voskuhle`(person)
- `Brandstetterweg 76k, 4682 Buchet, Österreich`(address)
- `Beratungs GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/143628.1`) (sent_id: `deanon_BFG_20260814_TEST/143628.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Jaroslaw Hoecker  in der Beschwerdesache Valerius Sülzbrück,  Mariazellerstraße 82, 4210 Unterweitrag, Österreich  nunmehr vertreten durch Steuerberaterin Danielle Tafelmeir, Andelberggasse 58, 4760 Niederham, Österreich, über die  Beschwerde vom 5. Oktober 2017 (Postaufgabetag) gegen den Bescheid des ehemaligen  Finanzamtes Wien 12/13/14 Purkersdorf vom 19. September 2017 betreffend Abweisung eines  Zahlungserleichterungsansuchens, Steuernummer 26-264/5699, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Danielle Tafelmeir` — partial — gold is substring of pred: `Danielle Tafelmeir`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Jaroslaw Hoecker`(person)
- `Valerius Sülzbrück`(person)
- `Mariazellerstraße 82, 4210 Unterweitrag, Österreich`(address)
- `Danielle Tafelmeir`(person)
- `Andelberggasse 58, 4760 Niederham, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `26-264/5699`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Dieter Fröhlich, den   Richter Mag. Christian Seywald, die fachkundigen Laienrichter Johannes Steiner und   Michael Kamper MSc über die Bescheidbeschwerde vom 24.07.2019 des Ulrike Ackermaier, Bakk. iur., Knödelhüttenstraße 12, 9184 Mühlbach, Österreich  vertreten durch Woditschka Steuerberatung GmbH, 2130 Mistelbach, Lanzendorfer  Hauptstraße 9/1, gegen die Umsatzsteuerbescheide für das Jahr 2017 und das Jahr 2018, vom  18.06.2019, des Finanzamtes Gänserndorf Mistelbach (nunmehr FA Österreich),  Steuernummer 75-013/8302, nach Durchführung einer mündlichen Verhandlung am 29.  Jänner 2024 in Anwesenheit des Schriftführers Dietmar Gratz  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Woditschka Steuerberatung GmbH` — type mismatch — same span as gold: `Woditschka Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Mag. Christian Seywald`(person)
- `Johannes Steiner`(person)
- `Michael Kamper MSc`(person)
- `Ulrike Ackermaier, Bakk. iur.`(person)
- `Knödelhüttenstraße 12, 9184 Mühlbach, Österreich`(address)
- `Woditschka Steuerberatung GmbH`(organisation)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `FA Österreich`(organisation)
- `75-013/8302`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Elena Sladek, Metnitztalweg 11, 9572 Gantschach, Österreich, vertreten durch Steuerberaterin Allegra Paulenz, Dornblüthstraße 2, 01277 Dresden,  über die Beschwerde vom 20. Juli 2020 gegen den Bescheid des Finanzamtes Österreich vom  22. Juni 2020 betreffend Feststellungsbescheid über die Nichtveranlagung zur Umsatzsteuer  2019 Steuernummer 61-618/5776  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Allegra Paulenz` — partial — gold is substring of pred: `Allegra Paulenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elena Sladek`(person)
- `Metnitztalweg 11, 9572 Gantschach, Österreich`(address)
- `Allegra Paulenz`(person)
- `Finanzamtes Österreich`(organisation)
- `61-618/5776`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/143803.1`) (sent_id: `deanon_BFG_20260814_TEST/143803.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dagobert Rönnecke  in der Revisionssache PhD ÖkR Peter Stankeit,  Im Alauntal 10, 3243 Eselsteiggraben, Österreich  vertreten durch Aigner Rechtsanwalts-GmbH, Lugeck 1-2/Stiege 2/Top 12, 1010  Wien, über den Antrag des Revisionswerbers vom 2.Februar 2024, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 12.Dezember 2023, RV/5100686/2021, betreffend  Einkommensteuer 2019 und die Aufhebung des Einkommenssteuerbescheides 2019  erhobenen außerordentlichen Revision die aufschiebende Wirkung zuzuerkennen,  beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Aigner Rechtsanwalts-GmbH` — type mismatch — same span as gold: `Aigner Rechtsanwalts-GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Dagobert Rönnecke`(person)
- `PhD ÖkR Peter Stankeit`(person)
- `Im Alauntal 10, 3243 Eselsteiggraben, Österreich`(address)
- `Aigner Rechtsanwalts-GmbH`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sabrina Ternes  in der Beschwerdesache Sheila Szikorra,  Brennersee 10, 9555 St. Gandolf, Österreich, vertreten durch Auxiliaris Steuerberatung GmbH, Grazer Straße 12, 8480  Mureck, über die Beschwerde vom 11. Jänner 2019 gegen den Bescheid des Finanzamtes  Klagenfurt vom 17. Dezember 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Steuernummer 67-828/8052  zu Recht erkannt:   I. Gemäß § 279 BAO wird die Beschwerde als unbegründet abgewiesen und wird der  angefochtene Bescheid abgeändert.

**False Positives:**

- `Auxiliaris Steuerberatung GmbH` — type mismatch — same span as gold: `Auxiliaris Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Sabrina Ternes`(person)
- `Sheila Szikorra`(person)
- `Brennersee 10, 9555 St. Gandolf, Österreich`(address)
- `Auxiliaris Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `67-828/8052`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der Cathleen Kirchgässner, Falz 3, 4320 Pragtal, Österreich, vertreten durch Stb-GmbH, Stb-GmbH-Adr, über die  Beschwerde vom 27.04.2018 gegen die Umsatzsteuerbescheide 2008, 2009, 2010, 2011, 2012,  2013, 2014, 2015 und 2016, sowie gegen die Körperschaftsteuerbescheide für das Jahr 20Q8,  2009, 2010, 2011, 2012, 2013, 2014, 2015 und 2016 des Finanzamtes Bregenz (alle Bescheide  vom 01.03.2018), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Stb-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Cathleen Kirchgässner`(person)
- `Falz 3, 4320 Pragtal, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/146305.1`) (sent_id: `deanon_BFG_20260814_TEST/146305.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Zlatan Türkyilmaz  über den Antrag der Revisionswerberin  Esmeralda Pfanne, Steinplattenweg 5, 8091 Pöllau, Österreich  vertreten durch Rechtsanwalt Mag. Dr. Helmut Blum und  Rechtsanwältin Mag.a Andrea Blum, Mozartstraße 11/6, 4020 Linz, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 21. März 2024, GZ. RV/7102000/2023, betreffend Abweisung  eines Nachsichtsansuchens erhobenen a.o. Revision vom 16. November 2024 aufschiebende  Wirkung zuzuerkennen, den Beschluss gefasst:  Der Antrag wird gemäß § 30 Abs. 2 Verwaltungsgerichtshofgesetz, VwGG, abgewiesen.

**False Positives:**

- `Rechtsanwalt Mag` — positional overlap with gold: `Mag. Dr. Helmut Blum`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Zlatan Türkyilmaz`(person)
- `Esmeralda Pfanne`(person)
- `Steinplattenweg 5, 8091 Pöllau, Österreich`(address)
- `Mag. Dr. Helmut Blum`(person)
- `Mag.a Andrea Blum`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/147657.1`) (sent_id: `deanon_BFG_20260814_TEST/147657.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hemma Fieber  in der Beschwerdesache Eleonore Isenhardt,  Bachwiesenstraße 12, 6401 Inzing, Österreich, vertreten durch TPA Regio Steuerberatung GmbH, Schwedengasse 2, 3500  Krems/Donau, über die Beschwerde vom 22. Mai 2019 gegen den Bescheid des Finanzamtes  Wien 12/13/14 Purkersdorf vom 6. Mai 2019 betreffend die Wiederaufnahme des Verfahrens  gem § 303 Abs 1 BAO hinsichtlich der Einkommensteuer 2010 zu Steuernummer  94-874/0419  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `TPA Regio Steuerberatung GmbH` — type mismatch — same span as gold: `TPA Regio Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hemma Fieber`(person)
- `Eleonore Isenhardt`(person)
- `Bachwiesenstraße 12, 6401 Inzing, Österreich`(address)
- `TPA Regio Steuerberatung GmbH`(organisation)
- `Finanzamtes  Wien 12/13/14 Purkersdorf`(organisation)
- `94-874/0419`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/148995.1`) (sent_id: `deanon_BFG_20260814_TEST/148995.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Nicola Fedrich, Fresachergasse 7, 5142 Unterhaunsberg, Österreich  vertreten durch Name Erwachsenenvertreter,  Adresse, (gerichtlicher Erwachsenenvertreter) betreffend die Beschwerde vom 9. Jänner 2023  gegen den Bescheid des Finanzamtes Österreich vom 16. Dezember 2022 betreffend  Aufforderung zur Einreichung von Abgabenerklärungen für das Jahr 2021 zu Steuernummer  54-293/0065  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Name Erwachsenenvertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Nicola Fedrich`(person)
- `Fresachergasse 7, 5142 Unterhaunsberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `54-293/0065`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/149829.1`) (sent_id: `deanon_BFG_20260814_TEST/149829.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Lothar Kriwet, Gaugen 11, 9150 Draurain, Österreich, vertreten durch Spiss Steuerberatung GmbH,  Timmlerweg 16, 6580 St. Anton am Arlberg, über die Beschwerde vom 31. Oktober 2025 gegen  die Bescheide des Finanzamtes Österreich vom 15. Oktober 2025 betreffend   1. Verzinsung gemäß § 16 COFAG-NoAG (Fixkostenzuschuss I),  2.

**False Positives:**

- `Spiss Steuerberatung GmbH` — type mismatch — same span as gold: `Spiss Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `Lothar Kriwet`(person)
- `Gaugen 11, 9150 Draurain, Österreich`(address)
- `Spiss Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Ing. and Specialized Titles with Names` 🏆

**F1:** 0.018 | **Precision:** 0.268 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `e4382ea1`  
**Description:**
Specifically targets titles like Ing., KommR, OSR, ÖkR followed by names, ensuring the full name is captured even if it contains placeholders or is a single word. Excludes 'RichterRi' which is a role, not a title.

**Content:**
```
(?:Ing\. |KommR |OSR |ÖkR |PhD |StR |OStR |OMedR |MedR |VetR |LLB |KzlR|Ri)(?:[A-Z]\.[A-Za-z]+|[A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.268 | 0.009 | 0.018 | 56 | 15 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 15 | 41 | 1599 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `OSR Corbinian Friemuth` | `OSR Corbinian Friemuth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Alexander Rimser` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_96`)


Beweis: Einvernahme OSR Corbinian Friemuth, beizuschaffende Transaktionsbeleg Nr.  275,888,722‚ zeugenschaftliche Einvernahme des Parkaufsichtsorgans A352.

| Predicted | Gold |
|---|---|
| `OSR Corbinian Friemuth` | `OSR Corbinian Friemuth` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `KommR Serge Salameh` | `KommR Serge Salameh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Anastasia Schraders` (person)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_2`)


in der Beschwerdesache PhD KommR Louisa Mühle, Waltersdorferstraße 9, 5310 Scharfling, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 6. Dezember 2017 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 6. November 2017 betreffend  1.

| Predicted | Gold |
|---|---|
| `PhD KommR Louisa Mühle` | `PhD KommR Louisa Mühle` |

**Missed by this rule (FN):**

- `Waltersdorferstraße 9, 5310 Scharfling, Österreich` (address)
- `N & N Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `PhD Nancy Prätor` | `PhD Nancy Prätor` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Basil Eberhards` (person)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `FA Linz` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache OSR Juliette Franzisi, Spitzesed 172, 4673 Baumgarting, Österreich, über die Beschwerde vom 17. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 17. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 47-760/2078  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `OSR Juliette Franzisi` | `OSR Juliette Franzisi` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Spitzesed 172, 4673 Baumgarting, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `47-760/2078` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ing. OSR Julia Strutwolf` | `Ing. OSR Julia Strutwolf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Emmat 72, 9063 Wrießnitz, Österreich` (address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH` (organisation)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Eizenhammer  in der Beschwerdesache KommR Ashley Tönisen,  Filzbergweg 63, 4924 Födering, Österreich, betreffend die Beschwerde vom 5. August 2011 gegen die Bescheide des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) datiert mit 22. Februar 2011  betreffend Haftung und Zahlung von Lohnsteuer sowie Festsetzung des Dienstgeberbeitrages  zum Ausgleichsfonds für Familienbeihilfen und Zuschlag zu diesem Beitrag, jeweils für die Jahre  2005 bis 2007, Steuernummer 16-543/4492,  beschlossen:    I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `KommR Ashley Tönisen` | `KommR Ashley Tönisen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Eckard Eizenhammer` (person)
- `Filzbergweg 63, 4924 Födering, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-543/4492` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Ing. Linus Feyerherdt` | `Ing. Linus Feyerherdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Wieland Starnberg` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Christina Hildegard Stowasser` (person)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138775.1`) (sent_id: `deanon_BFG_20260814_TEST/138775.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  OSR KommR Susette Stenczel, Amtweg 83, 9542 Tobitsch, Österreich, über die Beschwerde vom 28. Oktober 2019 gegen den Bescheid  des Finanzamtes für Gebühren, Verkehrsteuern und Glückspiel vom 25. September 2019  betreffend Gebühr Steuernummer 61-194/1325  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OSR KommR Susette Stenczel` | `OSR KommR Susette Stenczel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Amtweg 83, 9542 Tobitsch, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `61-194/1325` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Ing. Nicoletta Papastergios,  Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich  über die Beschwerde vom 12. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 31. März 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 94-528/7027  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ing. Nicoletta Papastergios` | `Ing. Nicoletta Papastergios` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `94-528/7027` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_26`)


Der einzige Gesellschafter, Ing. Leonie Veix,  wohnhaft in Polen, war von der Gründung im Jahr 2013 bis zur Löschung gemäß § 40 FBG  infolge Vermögenslosigkeit der Geschäftsführer der Firma.

| Predicted | Gold |
|---|---|
| `Ing. Leonie Veix` | `Ing. Leonie Veix` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/148827.1`) (sent_id: `deanon_BFG_20260814_TEST/148827.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  OSR Konstanze Dockweiler, Hasenkogl 4, 3572 St. Leonhard am Hornerwald, Österreich, betreffend die am 2. August 2024 beim Finanzamt Österreich  eingelangte Beschwerde gegen die als „festgesetzte Säumniszuschläge für 2021“ bezeichneten  Bescheide beschlossen:  I.  Die Beschwerde gilt gem. § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `OSR Konstanze Dockweiler` | `OSR Konstanze Dockweiler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Hasenkogl 4, 3572 St. Leonhard am Hornerwald, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/148827.1`) (sent_id: `deanon_BFG_20260814_TEST/148827.1_6`)


Dieser Schriftsatz stammt vom Beschwerdeführer OSR Konstanze Dockweiler (in der Folge kurz Bf.) bezieht sich  auf die Steuernummer 92-085/0684  und lautet wörtlich:  [...]  Das FAÖ erließ daraufhin mit 12. September 2024 unter Bezugnahme auf die Beschwerde  gegen Säumniszuschläge 2021 einen Mängelbehebungsauftrag (Adressierung an deutsche  Anschrift),  1 von 4 Seite 2 von 4

| Predicted | Gold |
|---|---|
| `OSR Konstanze Dockweiler` | `OSR Konstanze Dockweiler` |

**Missed by this rule (FN):**

- `92-085/0684` (tax_number)
- `FAÖ` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/148999.1`) (sent_id: `deanon_BFG_20260814_TEST/148999.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R 1 in der Beschwerdesache PhD OSR Nigel Westerfeld,  Timls 1191a, 8966 Auberg, Österreich, vertreten durch Dr. Michael Kotschnigg, Steuerberater, Stadlauer Straße  39/1/Top 12, 1220 Wien, über   die Beschwerde vom 3. Dezember 2020 gegen die Bescheide des FA 1 vom 12. Oktober 2020  betreffend Umsatz- und Einkommensteuer 2015 zu Steuernummer 06-918/7336  zu Recht  erkannt:   I. Die Beschwerde gegen den Umsatzsteuerbescheid 2015 wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `PhD OSR Nigel Westerfeld` | `PhD OSR Nigel Westerfeld` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timls 1191a, 8966 Auberg, Österreich` (address)
- `Dr. Michael Kotschnigg` (person)
- `06-918/7336` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

**False Positives:**

- `KommR Ing` — partial — pred is substring of gold: `KommR Ing. Ludwig Taspinar, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `KommR Ing. Ludwig Taspinar, MA`(person)
- `Alt Lenzing 13, 4076 Karling, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch in der Beschwerdesache von Herrn Dipl.-Ing. Astrid Gänsl, Heimito von Doderer-Straße 8, 2100 Stetten, Österreich, über dessen Beschwerde vom 30. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. August 2021 betreffend Festsetzung eines ersten Säumniszuschlages in Höhe  von € 299,40 zu Steuernummer 74-872/6854  in der Sitzung am 16. Dezember 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der Säumniszuschlag mit  € 249,50 festgesetzt.

**False Positives:**

- `Ing. Astrid Gänsl` — partial — pred is substring of gold: `Dipl.-Ing. Astrid Gänsl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Astrid Gänsl`(person)
- `Heimito von Doderer-Straße 8, 2100 Stetten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `74-872/6854`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_4`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 9. August 2021 wurde über Herrn Dipl.-Ing. Astrid Gänsl  ein  erster Säumniszuschlag (für einen Betrag an Umsatzsteuer 2015 von € 14.970,00) in Höhe von  € 299,40 festgesetzt, da die angeführte Abgabenschuldigkeit nicht bis 15. Februar 2016  entrichtet worden sei.

**False Positives:**

- `Ing. Astrid Gänsl` — partial — pred is substring of gold: `Dipl.-Ing. Astrid Gänsl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)
- `Dipl.-Ing. Astrid Gänsl`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dipl.-Ing. Jeanne Handke, Vornbacherweg 166, 5142 Weinberg, Österreich, über die Beschwerde vom 23. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 21. Juli 2021 betreffend Grunderwerbsteuer, Steuernummer 82-448/5450,  Erfassungsnummer 2017, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Jeanne Handke` — partial — pred is substring of gold: `Dipl.-Ing. Jeanne Handke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Jeanne Handke`(person)
- `Vornbacherweg 166, 5142 Weinberg, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `82-448/5450`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_8`)


Die Gesellschaftsanteile werden von Dipl. Ing.Ing. Bertram Hennlein und Dipl. Ing. B gehalten.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_9`)


Als  Geschäftsführer fungierte im Streitzeitraum Dipl. Ing.Ing. Bertram Hennlein  Im Zuge einer die Jahre 2015 bis 2019 umfassenden gemeinsamen Prüfung der Lohnabgaben  (GPLA) wurden folgende, nunmehr streitgegenständlichen Feststellungen getroffen:  1 von 17 Seite 2 von 17

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_39`)


Ad Geschäftsführerbezug, Diäten und GSVG-Beiträge  Im Prüfungszeitraum sei Dipl. Ing.Ing. Bertram Hennlein als Geschäftsführer der Beschwerdeführerin und Dipl.  Ing. B als Prokurist tätig gewesen.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_42`)


Dipl. Ing. B sei täglich an den Standorten W sowie Z anwesend gewesen und habe sich operativ  um die Durchführung der Geschäftsführeragenden gekümmert, während Dipl. Ing.Ing. Bertram Hennlein in  diese Tätigkeiten so gut wie gar nicht eingebunden gewesen sei.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_45`)


Dipl. Ing.Ing. Bertram Hennlein sei nur selten an den Bürostandorten körperlich anwesend gewesen und habe  daher organisatorisch gar nicht die Durchführung der originären Tätigkeiten eines  Geschäftsführers übernehmen können.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_46`)


Die Entlohnung des Dipl. Ing.Ing. Bertram Hennlein betreffe daher  ausschließlich seine Tätigkeit für die oben angeführten Projekte, für die Grenzverhandlungen  und als Sachverständiger.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_57`)


Die operativen Tätigkeiten des Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein hätten in der  Abwicklung der Projekte, in Grenzverhandlungen und im Tätigwerden als Sachverständiger  bestanden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_60`)


In den Jahren 2014-2020 seien auch alle Jahresabschlüsse vom alleinigen  Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein unterzeichnet worden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_88`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.1. Bezüge des wesentlich beteiligten Gesellschafter-Geschäftsführers  Dipl. Ing.Ing. Bertram Hennlein ist zu 90% an der beschwerdeführenden Gesellschaft beteiligt und vertritt diese  seit 19.11.2010 selbständig als ihr Geschäftsführer.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing.Ing. Bertram Hennlein`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_91`)


Insgesamt flossen ihm in den  Streitjahren folgende Beträge zu:  2015 2016 2017 2018 2019  26.447,13 € 37.786,37 € 36.058,96 € 52.441,49 € 54.658,22 €  Dipl. Ing.Ing. Bertram Hennlein war für die Beschwerdeführerin einerseits als Sachverständiger tätig und  andererseits mit der Abwicklung des Projektgeschäftes (z.B. Semmering Basistunnel,  Bosrucktunnel, Sensorik-Anwendungen bei der ÖBB und ASFINAG) betraut.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)
- `ÖBB`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140490.1`) (sent_id: `deanon_BFG_20260814_TEST/140490.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Dipl.-Ing. Milena Panagiotoglou, KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich, über die Beschwerde vom 11. September 2022  gegen den Bescheid des Finanzamtes Österreich vom 6. September 2022 betreffend  Einkommensteuer 2017 (Arbeitnehmerveranlagung) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Milena Panagiotoglou` — partial — pred is substring of gold: `Dipl.-Ing. Milena Panagiotoglou`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Dipl.-Ing. Milena Panagiotoglou`(person)
- `KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142969.1`) (sent_id: `deanon_BFG_20260814_TEST/142969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Dipl. Kfm. KommR Yussuf Bätzoldt,  Moserrautweg 4, 9872 Millstatt am See, Österreich, Schweiz, über die Beschwerde vom 13. Juli 2023 gegen den  Zurückweisungsbescheid des Finanzamtes Österreich vom 16. Juni 2023 betreffend den Antrag  auf Gewährung der Familienbeihilfe für das Kind Ki ab Jänner 2022 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `KommR Yussuf Bätzoldt` — partial — pred is substring of gold: `Dipl. Kfm. KommR Yussuf Bätzoldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl. Kfm. KommR Yussuf Bätzoldt`(person)
- `Moserrautweg 4, 9872 Millstatt am See, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/144910.1`) (sent_id: `deanon_BFG_20260814_TEST/144910.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Maria Daniel über die Beschwerde der Diana Wüste,Schönangerweg 35, 4925 Gumpling, Österreich, vertreten durch Ing. Mag. Dr. Roland Erwin Hansely, Mahlerstraße 13 Tür 3,  1010 Wien, wegen behaupteter rechtswidriger Ausübung verwaltungsbehördlicher Befehls-  und Zwangsgewalt durch Organe des Zollamtes Österreich am 19.11.2023 durch Ausübung  psychischen Zwangs den Beschluss:   Die Maßnahmenbeschwerde vom 19.12.2023 wird als unzulässig zurückgewiesen.

**False Positives:**

- `Ing. Mag` — partial — pred is substring of gold: `Ing. Mag. Dr. Roland Erwin Hansely`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Maria Daniel`(person)
- `Diana Wüste`(person)
- `Schönangerweg 35, 4925 Gumpling, Österreich`(address)
- `Ing. Mag. Dr. Roland Erwin Hansely`(person)
- `Zollamtes Österreich`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Wolfgang` — partial — pred is substring of gold: `Dipl.Ing. Wolfgang  Weichselbraun`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Mag. Sonja Stradner`(person)
- `Manfred Fiala`(person)
- `Dipl.Ing. Wolfgang  Weichselbraun`(person)
- `Kira Lentze`(person)
- `In der Krems 35, 3500 Gneixendorf, Österreich`(address)
- `Woditschka  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `97-126/0015`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/145343.1`) (sent_id: `deanon_BFG_20260814_TEST/145343.1_2`)


Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Ralf Schatzl, den Richter Mag.  Thomas Stieger sowie die fachkundigen Laienrichter Ing. Helmut Marchhart und Mag. Christian  Berger BA MSc LL.M. in der Beschwerdesache Franziskus Schymitzek, Gössering 48, 9314 St. Martin, Österreich, vertreten durch  KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Krassnigstr 36, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom 25. Oktober 2018  gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom  28. September 2018 betreffend Anspruchszinsen (§ 205 BAO) 2016 und Einkommensteuer  (Arbeitnehmerveranlagung) 2016 in der Sitzung am 5. Juli 2024 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Helmut Marchhart` — partial — pred is substring of gold: `Laienrichter Ing. Helmut Marchhart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ralf Schatzl`(person)
- `Mag.  Thomas Stieger`(person)
- `Laienrichter Ing. Helmut Marchhart`(person)
- `Mag. Christian  Berger BA MSc LL.M.`(person)
- `Franziskus Schymitzek`(person)
- `Gössering 48, 9314 St. Martin, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vivian Gastell  in der Beschwerdesache Dipl.-Ing. Tosca Toussaint,  Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 25. Mai 2023 betreffend Abweisung des Antrags vom 6. Februar 2023 auf  Erstattung des Mehrkindzuschlages auf Grund der  Verhältnisse des Jahres 2022,  Steuernummer 82-564/6636, SV-Nr. Nr., zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

**False Positives:**

- `Ing. Tosca Toussaint` — partial — pred is substring of gold: `Dipl.-Ing. Tosca Toussaint`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Vivian Gastell`(person)
- `Dipl.-Ing. Tosca Toussaint`(person)
- `Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `82-564/6636`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Vorsitzenden des Finanzstrafsenates 6008-6  Mag. Johann Fischerlehner in der Finanzstrafsache gegen Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich, wegen  der Finanzvergehen der Abgabenhinterziehungen gemäß § 33 Abs. 2a des Finanzstrafgesetzes  (FinStrG) über die Beschwerden der Beschuldigten vom 22.09.2023 und der Amtsbeauftragten  vom 09.10.2023 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung -  Team als Finanzstrafbehörde vom 14.07.2023 beschlossen:  Das angefochtene Erkenntnis des Spruchsenates vom 14.07.2023, Gz., Team wird gemäß § 161  Abs. 4 FinStrG aufgehoben und die Finanzstrafsache in ihrem gesamten Umfang an die  Finanzstrafbehörde zur neuerlichen Entscheidung zurückverwiesen.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Dipl.-Ing. Heinz Riechels`(person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich`(address)
- `Amt für Betrugsbekämpfung`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_3`)


Begründung  Verfahrensgang:  Mit Beschluss des Bezirksgerichtes BG vom TT. Februar 2023 zu Aktenzeichen Az. wurde  betreffend Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  das Schuldenregulierungsverfahren eröffnet und  Dr. Harald POHLHAMMER, Herrenstraße 29/2.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich`(address)
- `Dr. Harald POHLHAMMER`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_5`)


Mit Vorladung vom 22. Juni 2023 zur mündlichen Verhandlung am 14.07.2023 um 08:30 Uhr  vor dem Spruchsenat des Amtes für Betrugsbekämpfung - Bereich Finanzstrafsachen - Team als  Finanzstrafbehörde wurde Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  als Beschuldigter geladen.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amtes für Betrugsbekämpfung`(organisation)
- `Dipl.-Ing. Heinz Riechels`(person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_7`)


Finanzstrafbehörde wurde die Fa. NB zu Handen Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  als  Nebenbeteiligte geladen.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_8`)


Mit Eingangsdatum 14.07.2023 (Poststempel Finanzamt Österreich) ging von Rechtsanwalt  Dr. Harald Pohlhammer (Masseverwalter von Dipl.-Ing. Heinz Riechels) ein Schreiben samt Übermittlung von  2 RSa Briefen ein.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich`(organisation)
- `Dr. Harald Pohlhammer`(person)
- `Dipl.-Ing. Heinz Riechels`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_9`)


Demnach hätte Herr Dipl.-Ing. Heinz Riechels  trotz Aufforderung des Masseverwalters die  Post nicht beim Masseverwalter abgeholt. Beigeschlossen wurden die Vorladung des  Beschuldigten Dipl.-Ing. Heinz Riechels  zur Spruchsenatsverhandlung (RSa Brief) sowie die Vorladung des  Nebenbeteiligten NB zur Spruchsenatsverhandlung (RSa Brief).

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`
- `Ing. Heinz Riechels` — similar text (different position): `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Dipl.-Ing. Heinz Riechels`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_11`)


Festgehalten wurde, dass bei Aufruf der Sache weder der Beschuldigte Dipl.-Ing. Heinz Riechels  noch der  beschuldigte Verband NB erschienen sind.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_14`)


Der Senatsvorsitzende hat in einem Vorhalt vom 14.3.2025 die belangte Behörde aufgefordert,  binnen von vier Wochen ab Zustellung dieses Schreibens folgende Unterlagen vorzulegen:   Ladung der beschuldigten Parteien zur mündlichen Verhandlung am 14.07.2023 samt  Zustellnachweis   Auszug aus der Insolvenzdatei betreffend Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  Weiters wurde die belangte Behörde aufgefordert folgende Passage in der schriftlichen  Ausfertigung des angefochtenen Staferkenntnisses  (Seite 7) näher zu erläutern:  „Die Zustellung der Ladung ist ausgewiesen durch persönliche Übernahme per 27.06.2023.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_20`)


Unterschrift auf der gegenständlichen Beschwerde:  [...]  Zudem ist auf der Verständigung von der Hinterlegung eine Nachsendeadresse angeführt, die  jener des damaligen Insolvenzverwalters Dr. Pohlhammer des Dipl.-Ing. Heinz Riechels  entspricht.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Pohlhammer`(person)
- `Dipl.-Ing. Heinz Riechels`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_22`)


Die Ladungen zur Spruchsenatsverhandlung an den Beschuldigten Dipl.-Ing. Heinz Riechels  und den  nebenbeteiligten Verband NB gingen It. Eingangsstempel auf den RSa Schreiben jeweils am  27. Juni 2023 beim Masseverwalter Dr. Pohlhammer ein.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Dr. Pohlhammer`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_23`)


Offensichtlich wurde seitens des Spruchsenats die Tatsache, dass die Zustellung der Ladung zur  Spruchsenatsverhandlung an Dipl.-Ing. Heinz Riechels  nachweislich mittels Nachsendeauftrag an den  Masseverwalter erfolgte (siehe Nachsendeadresse links unten im Zustellnachweis der Ladung  an Dipl.-Ing. Heinz Riechels), nicht berücksichtigt und wurde daher im Glauben, dass die Ladung rechtmäßig  an den Beschuldigten ausgefolgt worden sei und dieser Kenntnis vom Verhandlungstermin  erlangt habe, die Spruchsenatsverhandlung in Abwesenheit des Beschuldigten Dipl.-Ing. Heinz Riechels  durchgeführt.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`
- `Ing. Heinz Riechels` — similar text (different position): `Dipl.-Ing. Heinz Riechels`
- `Ing. Heinz Riechels` — similar text (different position): `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Dipl.-Ing. Heinz Riechels`(person)
- `Dipl.-Ing. Heinz Riechels`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_24`)


Mit E-Mail vom 19.07.2023 wurde der Spruchsenatsvorsitzende Mag. Lichtenegger über das  Schreiben des Insolvenzverwalters Dr. Pohlhammer betreffend die nicht abgeholten  Spruchsenats-Vorladungen informiert und ihm das Schreiben übermittelt.  Über die Beschwerde wurde erwogen:  Festgestellter Sachverhalt:  Aus den vorgelegten und nunmehr auf Grund des Vorhaltes des Senatsvorsitzenden ergänzten  Akten ergibt sich zweifelsfrei, dass die Ladungen zur mündlichen Verhandlung am 14.07.2023  um 08:30 Uhr vor dem Spruchsenat des Amtes für Betrugsbekämpfung - Bereich  Finanzstrafsachen - Team als Finanzstrafbehörde weder dem Beschuldigten Dipl.-Ing. Heinz Riechels  noch  3 von 5 Seite 4 von 5

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Lichtenegger`(person)
- `Dr. Pohlhammer`(person)
- `Amtes für Betrugsbekämpfung`(organisation)
- `Dipl.-Ing. Heinz Riechels`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_26`)


Trotz Verfügung der eigenhändigen  Zustellung wurden die Poststücke an den damaligen Masseverwalter des Dipl.-Ing. Heinz Riechels  übermittelt und sind dem Beschuldigten und der Nebenbeteiligten auch tatsächlich nicht  zugekommen.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_50`)


Im gegenständlichen Fall hat sich herausgestellt, dass die Ladungen zur mündlichen  Verhandlung am 14.07.2023 um 08:30 Uhr vor dem Spruchsenat des Amtes für  Betrugsbekämpfung - Bereich Finanzstrafsachen - Team als Finanzstrafbehörde weder dem  Beschuldigten Dipl.-Ing. Heinz Riechels  noch dem nebenbeteiligten Verband NB zugestellt wurden.

**False Positives:**

- `Ing. Heinz Riechels` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amtes für  Betrugsbekämpfung`(organisation)
- `Dipl.-Ing. Heinz Riechels`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_4`)


Tatsächlich hat die Bf. die „Dipl.-Ing. KzlR Juri Strube“ mit der Vertretung beauftragt und diese auch im  Antrag auf Erstattung von Vorsteuern vom 20. Juni 2023 als Zustellungsbevollmächtigte  benannt.

**False Positives:**

- `Ing. KzlR Juri Strube` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_15`)


Da der Bescheid im Beschwerdefall nicht an den tatsächlichen Zustellungsbevollmächtigten  „Dipl.-Ing. KzlR Juri Strube“, sondern die „Hemma Bödker“ adressiert war, vermag er für die Bf. keine  Rechtswirkung zu entfalten.

**False Positives:**

- `Ing. KzlR Juri Strube` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)
- `Hemma Bödker`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_227`)


Seitens der Bf. wurde ein Privatgutachten von Dipl.Ing. Dr. H, anonymisiert aber mit RV-Zahl,  vorgelegt.

**False Positives:**

- `Ing. Dr` — partial — pred is substring of gold: `Dipl.Ing. Dr. H`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.Ing. Dr. H`(person)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_240`)


Bekannt sei, dass Dipl.Ing. Dr. H mehrere Gutachten erstellt habe.

**False Positives:**

- `Ing. Dr` — partial — pred is substring of gold: `Dipl.Ing. Dr. H`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.Ing. Dr. H`(person)

</details>

---

## `Frau Preceded Names with Suffixes` 🏆

**F1:** 0.013 | **Precision:** 0.177 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `2be8e62f`  
**Description:**
Matches persons preceded by 'Frau' or 'Herr', capturing the full name including suffixes (LL.M., MBA, Bakk. techn.), ensuring it's not just a title.

**Content:**
```
(?:Herrn?|Frau)\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MAS|Bakk\. rer\. nat|Bakk\. art\. BEd)?)?)?(?=,|$|[.](?!.*(?:GmbH|AG|Gesellschaft)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.177 | 0.007 | 0.013 | 62 | 11 | 51 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 51 | 1603 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Mag. Wolfgang Moser` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Waldviertel als Finanzstrafbehörde vom 12. November  2020, SpS, Strafnummer, wurde Herr Petra Port, geb. am 1980, schuldig erkannt, er habe im  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_4`)


Dass der Geschäftsführer der GmbH, Herr Nadine Millradt, dies bestreite, sei ihm bekannt und  derzeit Gegenstand mehrerer Verfahren.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_32`)


Im Bescheid II vom 20.2.2019 wurde für Herrn Quentin Schwartkopp, Adresse_Bf., gemäß § 8 Abs. 1 Z 2  AlkStG iVm. § 201 Abs. 1 und Abs. 2 Z 3 der Bundesabgabenordnung (BAO) die Alkoholsteuer  für 2016 in Höhe von € 280,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_34`)


Im Rahmen des Ermittlungsverfahrens wurde festgestellt, dass Herr Quentin Schwartkopp, belegt durch  den Übergabevertrag, GZ xxx vom 17.mt.2011 — mit Wirkung vom 01.mt.2011 — das  landwirtschaftliche Anwesen in Betriebssitz, an seinen Sohn Sohn, übergeben hat.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)


Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der Engelbert Schefe  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Engelbert Schefe` (person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/146473.1`) (sent_id: `deanon_BFG_20260814_TEST/146473.1_3`)


Begründung  Am 22.03.2024 erließ das Finanzamt für Frau Günter Salfetter, Beschwerdeführerin, einen  Einkommensteuerbescheid (Arbeitnehmerveranlagung) für das Jahr 2023.

| Predicted | Gold |
|---|---|
| `Günter Salfetter` | `Günter Salfetter` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Frau Christina Schwabendissen, Beschwerdeführerin, reichte ihre Erklärung zur Arbeitnehmerveranlagung  2015 am 7.12.2020 am Finanzamt ein.

| Predicted | Gold |
|---|---|
| `Christina Schwabendissen` | `Christina Schwabendissen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_28`)


Betreffend die Baurechtseinlage EZ 2 KG XY) wurde mit Schreiben vom 5.4.2017 von Notar Herr  Mag. Z die Befreiung gemäß § 3 Abs. 1 Z 2 GrEStG (damals fälschlicherweise die Befreiung  gemäß § 3 Abs. 1 Z 3 GrEStG bezeichnet) beantragt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Z`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Z`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_34`)


Herr KT Hubert, hat sich erst mit 17.  Februar 2020 mit Nebenwohnsitz bei Ihnen angemeldet.

**False Positives:**

- `KT Hubert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_68`)


Herr Dr. YYY hat das Fahrzeug am Morgen diesen Tages in der STRASSE-Hauptwohnsitz  übernommen und mitgeteilt, dass er einige Tage nach Ungarn fahren wird.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_105`)


ln Ihrer Stellungnahme gaben Sie im Wesentlichen an, dass das Fahrzeug am Morgen dieses  Tages in der STRASSE-Hauptwohnsitz von Herrn Dr. YYY übernommen worden wäre und Ihnen  dieser mitgeteilt hätte, dass er einige Tage nach Ungarn fahren werde.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_149`)


Herr  Dr. YYY ist für Ärzte ohne Grenzen tätig.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_150`)


Herr Dr. YYY hat mich nach einem schweren  Insektenbiss in GEBIET, mit Lebensgefahr für mich, hervorragend behandelt. Darauf gründet  sich die Freundschaft.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_151`)


Herr Dr. YYY arbeitet in Gebieten, wo kein Mobilfunknetz vorhanden ist.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_263`)


Nach Belehrung über das Entschlagungsrecht und Wahrheitserinnerung gemäß § 50 AVG  wurde das Organ der Parkraumüberwachung, welches ursprünglich die Beanstandung  durchgeführt hat, Frau NAME-Zeugin, als Zeugin einvernommen.

**False Positives:**

- `NAME-Zeugin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_385`)


Herr Dr. YYY arbeite in Gebieten, wo kein  Mobilfunknetz vorhanden sei.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_67`)


Unstrittig war, dass die Gesellschafter-Geschäftsführerin, Frau Ges-Gf, mit 25,25% im Sinne des  § 22 Z 2 zweiter Teilstrich EStG 1988 an der Bf. wesentlich beteiligt war.

**False Positives:**

- `Ges-Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Prim` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_35`)


Mit Schreiben vom 17.5.2019 stellte die steuerliche Vertretung des BF folgenden Antrag  (wörtlich):  "Betrifft:  Eventualantrag nach § 48 BAO    Ergänzung zum Antrag auf Einleitung eine Verständigungsverfahrens    vom 16.08.2018  Mit 16.08.2018 wurde für meinen Klienten, Herrn BF, die Einleitung eines  Verständigungsverfahrens betreffend einer Doppelbesteuerung zwischen Osterreich und Malta  geführt.

**False Positives:**

- `BF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_115`)


Es wurden einvernehmlich nicht nur Befunde beurteilt, sondern auch ausführliche persönliche  Gespräche mit Frau Mag. D (Neuropsychologisches Gutachten) und OA. Dr. G (Neuropädiaterin)  geführt.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. G`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lisa Lindnau`(person)
- `Lisa Lindnau`(person)
- `Lisa Lindnau`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch in der Beschwerdesache von Herrn Dipl.-Ing. Astrid Gänsl, Heimito von Doderer-Straße 8, 2100 Stetten, Österreich, über dessen Beschwerde vom 30. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. August 2021 betreffend Festsetzung eines ersten Säumniszuschlages in Höhe  von € 299,40 zu Steuernummer 74-872/6854  in der Sitzung am 16. Dezember 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der Säumniszuschlag mit  € 249,50 festgesetzt.

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Astrid Gänsl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Astrid Gänsl`(person)
- `Heimito von Doderer-Straße 8, 2100 Stetten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `74-872/6854`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_4`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 9. August 2021 wurde über Herrn Dipl.-Ing. Astrid Gänsl  ein  erster Säumniszuschlag (für einen Betrag an Umsatzsteuer 2015 von € 14.970,00) in Höhe von  € 299,40 festgesetzt, da die angeführte Abgabenschuldigkeit nicht bis 15. Februar 2016  entrichtet worden sei.

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Astrid Gänsl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)
- `Dipl.-Ing. Astrid Gänsl`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_35`)


Zusätzlich  sei der Beschwerdeführerin unbedingt empfohlen worden, die OP von Herrn Dr. B einem  anerkannten Schulterspezialisten ausführen zu lassen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_36`)


Herr Dr. B würde nur im KH der  Diakonissen operieren;

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_45`)


Als letzter  Versuch hätte sie auf Empfehlungen Herrn Dr. B, einen anerkannten Schulterspezialisten,  aufgesucht, welcher endlich nach einem langen Leidensweg die richtige Diagnose gestellt und  zu einer sofortigen Operation geraten hätte.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_58`)


Die streitgegenständliche Operation wurde schließlich in der Klinik Diakonissen Linz von Herrn  Dr. B durchgeführt (stationärer Aufenthalt von 15.5. bis 20.5.2019).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_71`)


Beide Gesellschaften wurden vom Alleingesellschafter-Geschäftsführer,  Herrn RB, vertreten (siehe Firmenbuch).

**False Positives:**

- `RB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_56`)


Die von Herrn Ing. Priv.-Doz.in Linda Schleglmilch zu Punkt 4 und 5 gemachten Angaben stellen für die Betriebsprüfung keine  zu akzeptierenden Argumente dar.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. Priv.-Doz.in Linda Schleglmilch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Priv.-Doz.in Linda Schleglmilch`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_19`)


Die Überprüfung der durchgeführten Selbstberechnungen erfolgte dergestalt, als Herrn Dr. F  dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel einen Datenträger zur Verfügung  gestellt hat.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_20`)


Nach den Angaben von Herrn Dr. F sollten auf diesem Datenträger alle notwendigen  Unterlagen gespeichert sein, welche für die ordnungsgemäße Selbstberechnung notwendig  gewesen sind (siehe dazu auch die Ausführungen in der Einleitung).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_22`)


In einer Besprechung vom 16.1.2015 hat Herr Dr. F zu  diesem Thema ua. angegeben, dass Schätzungsgutachten sich heute nicht in seinen Akten  befinden und er zum Zeitpunkt der Selbstberechnung davon ausgegangen ist, dass der  vereinbarte Kaufpreis zumindest dem gemeinen Wert entspricht und er sich damals auf die  Auskünfte der Vertragsparteien verlassen habe, wonach der Wert (gemeint gemeiner Wert)  dem vereinbarten Kaufpreis entspricht.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_23`)


Weiter hat Herr Dr. F angegeben, dass er zu allen  betroffenen Selbstberechnungen die entsprechenden Nachweise vorlegen wird.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_24`)


Mit Mail vom 9.2.2015 teilt Herr Dr. F dem Finanzamt für Gebühren Verkehrsteuern und  Glücksspiel mit, dass sich die entsprechenden Berechnungsgrundlagen (gemeint Nachweise  über die gemeinen Werte) bei der Firma K (die Bf) befinden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_26`)


Infolge sind von Herrn Dr. F Unterlagen - im Begleitschreiben als Gutachten bezeichnet sowie  Mietverträge - per Mail vorgelegt worden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_105`)


Dagegen erhob die Bf. fristgerecht Beschwerde und brachte unter Anführung der  gegenständlichen Geschäftszahl begründend (wörtlich) vor:  „Betrifft: Milderung der Strafe   Sehr geehrte Herr/Frau Frau,  ich habe Ihr Bescheid erhalten und bin gezwungen um eine Milderung anzusuchen.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_53`)


Im Einspruch gegen die Strafverfügung vom 22. Juli 2022, eingelangt bei der Behörde am 4.  August 2022, brachte der Bf erstmals vor, dass das Fahrzeug zur Beanstandungszeit von Herrn  LE, Gasse, 2700 Wr. Neustadt, gelenkt worden sei.

**False Positives:**

- `LE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_38`)


Das gegenständliche Einfamilienhaus stand bis Ende 2014 im Eigentum von  Frau EB.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_45`)


Auf die Gattin des BF, Frau EB, war von 04.01.2007 bis 04.09.2013 in Österreich ein  Kraftfahrzeug Nissan Navara mit dem Kennzeichen XY angemeldet.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_56`)


Dass auf die Gattin des BF, Frau EB, von 04.01.2007 bis 04.09.2013 in Österreich ein  Kraftfahrzeug Nissan Navara bzw. ab 13.09.2013 ein PKW VW Golf Plus mit dem Kennzeichen  XY angemeldet war, wurde anhand der vorgelegten Unterlagen nachgewiesen.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_14`)


Ziel der Bautätigkeit sei die Schaffung einer gemeinsamen  Wohnung für seine Familie, dh für seine Frau Prof. Engelbert Thuerrigl  verehelichte A, seine Kinder und für ihn  selbst, gewesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Engelbert Thuerrigl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Engelbert Thuerrigl`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_172`)


Lieferungen von Frau DM.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_57`)


Mit Beschluss des Bundesfinanzgerichtes vom 23.02.2023 wurden der BF die im Schreiben der  Firma I vom 10.11.2022 angeführten Anlagen, ausgenommen jene bei deren Übermittlung  durch das Bundesfinanzgericht gegen die abgabenrechtliche Geheimhaltungspflicht (§ 48a  BAO) verstoßen würde, zur Kenntnisnahme übermittelt. Weiters wurde die BF aufgefordert,  zum Vorbringen der belangten Behörde, wonach der Geschäftsführer der BF, Herr GK, früher  4 von 17 Seite 5 von 17

**False Positives:**

- `GK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_72`)


Geschäftsführer der BF im Jahr 2013 und in den Vorjahren war Herr GK.

**False Positives:**

- `GK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_76`)


Herr DO war bis Herbst  2004 Gesellschafter der Fa. I.  Alleiniger Geschäftsführer der Fa. I ist seit 2004 Herr KW.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_79`)


AS ist seit Gründung der Gesellschaft im Jahr 2001 Geschäftsführer und war bis Juli 2013  Gesellschafter der Fa. B. DM (auch MO geschrieben) ist seit Gründung der Gesellschaft im Jahr  2001 Gesellschafter der Fa. B. Seit Juli 2013 ist auch die U Gesellschafterin der Fa. B.  Geschäftsführer der U ist seit der Gründung im Jahr 2010 Herr AS.

**False Positives:**

- `AS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_80`)


Gesellschafter der U sind  seit Gründung Herr AS und Herr DO.

**False Positives:**

- `DO` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_83`)


Am 05.01.2005 wurde von der BF die Zahlung der zu diesem Zeitpunkt bestehenden Forderung  gegenüber der Fa. I in Höhe von € 367.290,00 per Email an Herrn KW, Geschäftsführer der Fa. I,  eingemahnt.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_94`)


Die im Vertrag vom 24.07.2007 vereinbarte Zahlung von jährlich € 30.000,00 ab dem Jahr 2011  wurde von der Fa. I nicht erfüllt.  Mit Email vom 15.02.2013 bot die BF dem Geschäftsführer der Fa. I, Herrn KW, an, auf 80 %  der zu diesem Zeitpunkt aushaftenden Forderung in Höhe von € 967.333,62, somit auf €  777.866,90, zu verzichten, wenn im Gegenzug von der Fa. I die verbleibende Restschuld von €  193.466,72 bis zum 31.03.2013 beglichen werde.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_86`)


Die Fahrstrecke zu Frau DDr. Ramon Luckmeier  Psychiaterin, Adr2, O1 O, betrage hin und zurück je 21 km.

**False Positives:**

- `DDr` — partial — pred is substring of gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_102`)


K1 befinde sich laut den Angaben der Bf in Behandlung von Frau DDr. Ramon Luckmeier  Fachärztin für  Psychiatrie und Psychotherapie, in der Adr.

**False Positives:**

- `DDr` — partial — pred is substring of gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_200`)


K1 befindet sich laut den Angaben der Bf in Behandlung von Frau DDr. Ramon Luckmeier  Fachärztin für  Psychiatrie und Psychotherapie, in der Adr.

**False Positives:**

- `DDr` — partial — pred is substring of gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)
- `Zollamt`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_88`)


Wie das Zollamt auch zu diesem Beschwerdepunkt ausführlichst und zu Recht betont hat,  wurde mit der Übergabe im Jahr 2011 der Übernehmer der Liegenschaft, Herr Sohn, auch  Eigentümer an den darauf befindlichen Obstbäumen und an deren Früchte.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_42`)


Zu den – durch die Finanzverwaltung – in den Fokus gesetzten administrativen Leistungen des  Herrn NR führt die Bf. aus, dass sich die Tätigkeiten zwingend vermischen würden: „Die dem  GPLA-Prüfer mehrfach erläuterte und durch Unterlagen nachgewiesene Vermischung und  Verschränkung der beiden Tätigkeiten (einerseits Betreuung und Verwaltung der eigenen  Geräte und Maschinen, andererseits kaufmännische Betreuung) oftmals auf derselben  Baustelle verunmöglicht eine genaue Trennung der Tätigkeitsbereiche des Herrn NR.

**False Positives:**

- `NR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_280`)


Dieses Produkt hat Herr Dr. B nicht verschrieben.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_304`)


Herr Dr. T ist ein Arzt.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_9`)


Demnach hätte Herr Dipl.-Ing. Heinz Riechels  trotz Aufforderung des Masseverwalters die  Post nicht beim Masseverwalter abgeholt. Beigeschlossen wurden die Vorladung des  Beschuldigten Dipl.-Ing. Heinz Riechels  zur Spruchsenatsverhandlung (RSa Brief) sowie die Vorladung des  Nebenbeteiligten NB zur Spruchsenatsverhandlung (RSa Brief).

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Heinz Riechels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Heinz Riechels`(person)
- `Dipl.-Ing. Heinz Riechels`(person)

</details>

---

## `Gutachten von Names` 

**F1:** 0.001 | **Precision:** 0.125 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `659cb5a6`  
**Description:**
Matches names appearing after 'Gutachten von' which introduces an expert witness or author.

**Content:**
```
(?:Gutachten von)\s+([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:[ -][A-Z][a-zA-Z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.125 | 0.001 | 0.001 | 8 | 1 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 7 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_116`)


Laut vorgelegtem Gutachten von Nicola Peterhansel  Fachärztin für Psychiatrie, vom 7. Jänner 2019, leidet  der Bf. an einer Intelligenzminderung mit einer ausgeprägten Lese- und Rechenschwäche und  kann auf Grund des vorliegenden Krankheitsbildes weder Vertragsinhalte richtig erfassen,  11 von 13 Seite 12 von 13

| Predicted | Gold |
|---|---|
| `Nicola Peterhansel` | `Nicola Peterhansel` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_100`)


Lebensjahr, dies wurde in dem  Gutachten von Frau Dr. 2 zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem  nicht attestiert.

**False Positives:**

- `Frau Dr` — positional overlap with gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_131`)


Lebensjahr, dies wurde in dem Gutachten von Frau Dr. 2  zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem nicht attestiert....  Derzeitige Beschwerden:  Die Antragstellerin gibt an: "Ich habe das gleiche seit meiner Jugend, das sind Panikattacken,  Kopfschmerzen und eine Sozialphobie.

**False Positives:**

- `Frau Dr` — positional overlap with gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_207`)


Das Gutachten von Prof. Maida datiert mit 2. März  2009, das BASB-Gutachten  vom 29. September 2009, die Befunde/Arztbriefe der  Psychiatrischen Abteilung des SMZ-Ost aus 2012 und das Gutachten von Dr. Baischer vom 21.  Februar 2013.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Maida`
- `Dr` — partial — pred is substring of gold: `Dr. Baischer`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)
- `Dr. Baischer`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_10`)


In Beantwortung der Schreiben des Finanzamtes übermittelte die Bf. am 25. Juni 2020 folgende  Unterlagen betreffend ihren Sohn A.:   – Psychologisches Gutachten von Dr. Mag. E.Sch., Klinische und Gesundheitspsychologin,  allgemein beeidete und gerichtlich zertifizierte Sachverständige für Psychologie,  Psychotherapeutin, und Quirin Spillmann, LLB  Klinische und Gesundheitspsychologin, vom 26. Juni 2019   – Hörverarbeitungsscreening durch Hörtrainer N.R. vom 14. November 2019   (Ergebnis auffällig;

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Dr. Mag. E.Sch.`(person)
- `Quirin Spillmann, LLB`(person)
- `N.R.`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_287`)


Die Reduktion des Grades der Behinderung von 50% auf 30% erscheint u.a. auch an folgenden  beispielhaft herangezogenen Umständen nachvollziehbar:   - War im ersten Bundessozialamts-Gutachten vom Juni 2016, gestützt auf damals vorgelegte  relevante Befunde, im Ergebnis der durchgeführten Begutachtung u.a. Dyskalkulie angeführt  worden und daraus die angeführte Entwicklungsstörung diagnostiziert worden,   so findet sich in dem – beiden BSA-Gutachten von Oktober 2019 und vom August 2020 –  zugrunde gelegten Befund der klinischen Psychologin vom 26. Juni 2019 die ausdrückliche  Feststellung: Es liegt keine Dyskalkulie vor (aus der retrospektiven Sicht wohl: nicht mehr vor)  (vgl. die oben wiedergegebenen Gutachten).

**False Positives:**

- `Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/143631.1`) (sent_id: `deanon_BFG_20260814_TEST/143631.1_43`)


Auf den Baulandumlegungsvertrag und das Gutachten von Dr-P  vom 16.04.2021 wird verwiesen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Case Citation Surnames` 💣

**F1:** 0.001 | **Precision:** 0.050 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `9f589fcd`  
**Description:**
Matches surnames appearing in case citations like 'C-280/10, Polski Trawertyn' or 'Rs Schmelz', capturing multi-word names.

**Content:**
```
(?:C-\d+/\d+,\s*|Rs\s+)([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*)[,.]
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.050 | 0.001 | 0.001 | 20 | 1 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 19 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_99`)


Im Urteil vom 26.10.2010, C-97/09, Schmelz, erwog der EuGH:  Nach alledem erweist es sich, dass beim gegenwärtigen Stand der Entwicklung der  Mehrwertsteuerregelung das Ziel, die Wirksamkeit der Steueraufsicht im Hinblick auf die  Bekämpfung von Steuerhinterziehungen, Steuerumgehungen und etwaigen Missbräuchen zu  gewährleisten, und das Ziel der Kleinunternehmerregelung, mit der die Wettbewerbsfähigkeit  der Kleinunternehmen gestärkt werden soll, es zum einen rechtfertigen, dass die  Anwendbarkeit der Mehrwertsteuerbefreiung auf die Tätigkeiten der Kleinunternehmen  beschränkt wird, die im Hoheitsgebiet des Mitgliedstaats, in dem die Mehrwertsteuer  geschuldet wird, ansässig sind, und zum anderen, dass der zu berücksichtigende Jahresumsatz  derjenige ist, der in dem Mitgliedstaat erzielt wird, in dem das Unternehmen ansässig ist.

| Predicted | Gold |
|---|---|
| `Schmelz` | `Schmelz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_65`)


C-273/11, Mescek Gabona Kft und vom 1.3.2012, Rs. C-280/10, Polski Travertyn.

**False Positives:**

- `Polski Travertyn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_177`)


Die  Behörde setze diesen Sachverhalt mit jenem gleich, der der Entscheidung des EuGH vom  22. Oktober 2015, C-264/14, Hedqvist, zugrunde liege, in dem es lediglich einen Umtausch von  konventioneller Währung in Einheiten der virtuellen Währung „Bitcoin“ komme.

**False Positives:**

- `Hedqvist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_196`)


f. Nach der Rspr des EuGH wäre für die Anwendbarkeit der Umsatzsteuerbefreiung des Art 135  Abs 1 Buchstabe d MWSt-RL Voraussetzung, dass der Zahlungsverkehr im Großen und Ganzen  ein eigenständiges Ganzes bilde und somit auch unabhängig von den restlichen angebotenen  Dienstleistungen sei (EuGH 25.7.2018, C-5/17, DPAS Limites, Rz 34).

**False Positives:**

- `DPAS Limites` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_727`)


Bei derartigen Umsätzen – wie sie sich bei  Tauschgeschäften ergeben – ist es unbedeutend, ob es sich dabei   - um den gewöhnlicherweise nach Art 135 Abs 1 lit e der MwStSyStRL steuerfreien Wechsel  von herkömmlichen Währungen handelt oder  - um den Wechsel von herkömmlichen Währungen in gegenseitig handhabbare  Kryptowährungen (bzw umgekehrt), die ein von den Transakteuren akzeptiertes  Zahlungsmittel darstellen (ohne gesetzliches Zahlungsmittel zu sein – EuGH C-264/14,  Hedqvist, Rz 50).

**False Positives:**

- `Hedqvist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_38`)


Der EuGH beantwortete diese Fragen im Urteil vom 15.04.2021, Rs C-593/19, SK Telecom, wie  folgt:  „Rn 29.

**False Positives:**

- `SK Telecom` — type mismatch — same span as gold: `SK Telecom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SK Telecom`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_59`)


2 der Mehrwertsteuerrichtlinie ergibt, dass jeder Umsatz in der Regel als eigene,  selbständige Leistung zu betrachten ist, und ein Umsatz, der eine wirtschaftlich einheitliche  Leistung darstellt, im Interesse eines funktionierenden Mehrwertsteuersystems nicht künstlich  aufgespalten werden darf (Urteil vom 4. September 2019, KPC Herning, C-71/18, EU, Rn. 36  und die dort angeführte Rechtsprechung).

**False Positives:**

- `EU` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_72`)


Allerdings ist darauf hinzuweisen, dass das Ziel der Regeln der Mehrwertsteuerrichtlinie,  nach denen der Ort der Besteuerung von Dienstleistungen zu bestimmen ist, darin besteht,  einerseits Kompetenzkonflikte, die zu einer Doppelbesteuerung führen könnten, und  andererseits die Nichtbesteuerung von Einnahmen zu verhindern (vgl. in diesem Sinne Urteile  vom 17. Dezember 2015, WebMindLicenses, C-419/14, Rn. 41, und vom 13. März 2019, Srf  konsulterna, C-647/17, Rn. 28 sowie die dort angeführte Rechtsprechung).

**False Positives:**

- `Rn` — no gold match — likely missing annotation
- `Rn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_112`)


Die gegenständliche Entscheidung entspricht den zitierten Erkenntnissen des VwGH in gleich  gelagerten Sachverhaltskonstellationen und der Rechtsansicht des EuGH im Urteil vom  15.04.2021, Rs C-593/19, Sk Telecom.

**False Positives:**

- `Sk Telecom` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_53`)


2. 2022, C-430/21, RS, EU:C:2022:99, Rn. 50).

**False Positives:**

- `RS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_68`)


Daraus folgt, dass die  Gerichte die Vorschrift in dieser Auslegung auch auf Rechtsverhältnisse, die nach Inkrafttreten  dieser Vorschrift und vor Erlass des auf das Ersuchen um Auslegung ergangenen Urteils  entstanden sind, anwenden können und müssen, wenn alle sonstigen Voraussetzungen für die  Anrufung der zuständigen Gerichte in einem die Anwendung dieser Vorschrift betreffenden  Streit vorliegen (vgl. EuGH 5. 9. 2019, C-331/18, TE, EU:C:2019:665, Rn. 53; EuGH 13.

**False Positives:**

- `TE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1001`)


EuGH 8.6.2000, Rs C-396/98, Schloßstraße, u.a.).

**False Positives:**

- `Schloßstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1048`)


Das Recht auf vollständigen und sofortigen Abzug der bei der Anschaffung eines  Investitionsgutes entrichteten Mehrwertsteuer führt zu einer entsprechenden Verpflichtung zur  Zahlung der Mehrwertsteuer auf die private Verwendung des Unternehmensgegenstandes (vgl.  EuGH vom 16. Februar 2012, C-594/10, Laarhoven, Rn. 27).“  69 von 90 Seite 70 von 90

**False Positives:**

- `Laarhoven` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_205`)


Aus dem Urteil des EuGH vom 13. Dezember 1989, C-342/87, Genius, sei abzuleiten, dass sich  der Vorsteuerabzug nicht auf eine Steuer erstrecke, die ausschließlich deshalb geschuldet  werde, weil sie in einer Rechnung ausgewiesen sei.

**False Positives:**

- `Genius` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_214`)


Dies gilt auch für die Fälle der  Vorsteuererstattung an ausländische Unternehmer (vgl. EuGH 15.3.2007, C-35/05, Rn. 27,  Reemtsma , sowie EuGH 13.12.1989, C-342/87, Genius Holding, Rn. 15).

**False Positives:**

- `Rn` — no gold match — likely missing annotation
- `Genius Holding` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/141757.1`) (sent_id: `deanon_BFG_20260814_TEST/141757.1_164`)


Verhindert die  Nichterfüllung der formalen Anforderungen (namentlich die Nennung des tatsächlichen  Leistungserbringers) die Überprüfung des Vorliegens der materiellen Voraussetzungen für den  Vorsteuerabzug, ist der Vorsteuerabzug nicht zu gewähren (EuGH 11.11.2021, C-281/20, Rs  Ferimet, Rn 27 und 37;

**False Positives:**

- `Ferimet` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_297`)


Der EuGH hat in seinen Urteilen vom 17.12.2015, C-419/14, WebMindLicenses, und vom  18.6.2020, C-276/18, KrakVet Marek Batko, zum Informationsaustausch nach der Verordnung  Nr. 904/2010 Stellung genommen.

**False Positives:**

- `WebMindLicenses` — no gold match — likely missing annotation
- `KrakVet Marek Batko` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Anonymized Initials with Title (Fixed)` 💣

**F1:** 0.002 | **Precision:** 0.013 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `b1d01cdf`  
**Description:**
Matches anonymized names with titles like 'Dr.in Dok1', 'Mag. NN', or 'Dr. X' where the name part is clearly a placeholder (mixed case/numbers) or specific known patterns, including single initials like 'M.'.

**Content:**
```
(?:Dr\.in?|Mag\.a?|RA|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|OMedR|MedR|StR|OStR|KzlR|Ri|Richter|Richterin|Herrn?|Frau)\s+([A-Z]\.[A-Za-z]*|[A-Z]\.[A-Z]\.[A-Z]\.|NN|Dok[0-9]+|[A-Z]{2,})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.013 | 0.001 | 0.002 | 155 | 2 | 153 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 153 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_176`)


Frau M. P. ist voraussichtlich nicht dauernd außerstande, sich selbst den Unterhalt zu  verschaffen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_15`)


Hinsichtlich des Unternehmens X.d.o.o. sei Herr A. auf einer Baustelle auf den Beschuldigten zugekommen und habe nach Arbeit gefragt und erklärt, dass er für eine slowenische Firma tätig sei.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_29`)


Letztlich gebe es außer der Aussage des Herrn A. keinen Hinweis darauf, dass der Beschuldigte hinsichtlich der X.d.o.o.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_40`)


------ Gegen dieses Erkenntnis des Spruchsenates richtet sich die vorliegende frist- und formgerechte Beschwerde des Amtsbeauftragten vom 7.1.2019, in der wie folgt ausgeführt wird: "Herr N.N., geb. am Datum, wohnhaft in Adresse1, hat vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bewirkt, dass festzusetzende Abgaben zu niedrig festgesetzt wurden sowie vorsätzlich Lohnabgaben nicht spätestens am fünften Tag nach Fälligkeit entrichtet (abgeführt).

**False Positives:**

- `N.N` — partial — pred is substring of gold: `N.N.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `N.N.`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_61`)


Um die Aussagen des Beschuldigten betreffend der Akontozahlungen an Herrn A. und der vorgelegten Schuldenerklärung zu überprüfen, wird hiermit der Antrag gestellt Herrn B. A., geb 19.07.1978, wohnhaft in Adresse2 als Zeugen zur mündlichen Verhandlung zu laden."

**False Positives:**

- `A.` — no gold match — likely missing annotation
- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_86`)


Abschließend bleibt zu den gegen mich erhobenen Vorwürfen noch auszuführen wie folgt: Einer der Hauptvorwürfe - wenn nicht der Hauptvorwurf überhaupt - gegen mich lautet, ich hätte Herrn A. um die Gründung der „Scheinfirma" X. in Slowenien ersucht bzw. ihn dazu überredet, um mir Lohnabgaben zu ersparen (Stellungnahme des Amtsbeauftragten vom 04.10.2018, Seite 2 unten und Seite 3, 4. Absatz).

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_93`)


Dazu kommt - und rundet dies das Bild ab - dass ich mit Herrn A. im Streit lebe, weil er mir einen Betrag von € 13 ‚000,00 schuldet.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_110`)


Zu den Eingangsrechnungen der Fa. X. d.o.o an das Einzelunternehmen N.N. in den Jahren 2012 und 2013 und Vorhalt Zeugenaussage B. A. vom 4.9.2018, dass die auf den Rechnungen ausgewiesenen Leistungen nicht von der Fa.  X. d.o.o erbracht worden seien, führte der Beschuldigte aus, Herr A. habe eigenständig eine Firma in Slowenien gegründet und sei mit dieser Firma zu ihm gekommen und habe um Aufträge ersucht.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `N.N.`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_111`)


Er habe mit der Firmengründung in Slowenien nichts zu tun gehabt, auch habe er das Stammkapital iHv € 7.500,00 für die Gründung in Slowenien nicht zur Verfügung gestellt. Herr A. habe auch eigene Beschäftigte auf seinen Baustellen eingesetzt.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_115`)


Seite 11 von 21 Auf die Frage warum der Beschuldigte glaube, dass Herr A. ihn unter der Strafdrohung einer unrichtigen Zeugenaussage belaste, führte der Beschuldigte aus, dass er annehme, dass sich A. wahrscheinlich selbst reinwaschen habe wollen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_181`)


Es ist aufgrund des vorliegenden Sachverhalts davon auszugehen, dass Herr A. seine Arbeitskraft geschuldet hat und somit ein Dienstverhältnis anzunehmen ist.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_182`)


Dafür sprechen auch folgende Tatsachen: Das zu verarbeitende Material sowie das benötigte Werkzeug wurden von der Fa. N. zur Verfügung gestellt. Herr A. wurde im gesamten Prüfungszeitraum mtl. mit € 1.300,00 entlohnt.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_184`)


Aus dem Gesamtbild des vorliegenden Sachverhalts und auf Grund der erfolgten Einvernahme von Herrn A. geht hervor, dass dieser lediglich seine Arbeitskraft zur Verfügung gestellt hat.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_185`)


Aus obgenannten Gründen wurde für Herrn A. ein Dienstverhältnis im Sinne des § 47 EStG 1988 angenommen und daher als Einkünfte aus nichtselbständiger Arbeit gem. § 25 EStG 1988 nachversteuert.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_203`)


Die Zeugenaussage des A. vor der Finanzstrafbehörde vom 4.9.2018 dahingehend, dass die auf den Rechnungen ausgewiesenen Leistungen nicht von der Fa. X. d.o.o erbracht worden seien, er zwar das „Auftragsschreiben – Subunternehmer“ unterschrieben, aber nicht ausgefüllt habe und er schwarz als weisungsunterworfener Dienstnehmer des N.N. mit einem Nettogehalt von € 1.300,00 für Herrn N. gearbeitet habe, widerspricht der Aussage des Beschuldigten in diesen wesentlichen Punkten diametral.

**False Positives:**

- `N.` — similar text (different position): `N.N.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `N.N.`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_0`)


GZ. RV/7102887/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache H. P. und F., Adresse, vertreten durch Steuerberatungs GmbH, über die Beschwerde vom 24.07.2013 gegen die Bescheide der belangten Behörde Finanzamt ******* vom 23.05.2013 betreffend Feststellung der Einkünfte gem. § 188 BAO aus Vermietung und Verpachtung für die Jahre 2005 - 2011 zu Recht erkannt:  Die angefochtenen Bescheide über die Feststellung der Einkünfte gem. § 188 BAO betreffend die Jahre 2005 bis 2011 werden abgeändert.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_51`)


Durch den Tod von Herrn H. senior kam es in 2001 erstmalig zu einer Entkoppelung von Besitz der Immobilie und Inhaber des Bäckereibetriebes.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_49`)


Herr F übertrug von Todes wegen unentgeltlich dieses  Sonderbetriebsvermögen (Baurechtseinlage EZ 2 KG XY) der Wohlgemut Getränke GmbH& Co KG bei gleichzeitiger  Zuwendung von 100% der Mitunternehmeranteile der Wohlgemut Getränke GmbH& Co an Frau A. Der Begriff  Sonderbetriebsvermögen  in § 3 Abs. 1 Z 2 lit a zweiter Teilstrich GrEStG ist ertragsteuerlich zu definieren.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wohlgemut Getränke GmbH`(organisation)
- `Wohlgemut Getränke GmbH&`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_9`)


Der Lebensunterhalt wird bestritten aus den Einkünften des Ehegatten, Herrn C. Dieser ist in D- XY als Angestellter der Firma F-AG tätig.

**False Positives:**

- `C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Chen Walcker`(person)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `63-698/2600`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Corbinian Friemuth`(person)
- `Mag. Alexander Rimser`(person)
- `Hermann`(person)
- `Magistrat der Stadt Wien`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_28`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 10/2012  Frau M.P. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

**False Positives:**

- `M.P` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_36`)


Herr KT  ist lt. Lohnausweis in Deutschland beschäftigt.

**False Positives:**

- `KT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_114`)


Dass die Bfin mit Herrn KT einen gemeinsamen Hausstand im Jahr 2018, der den Mittelpunkt  der Lebensinteressen in Polen gebildet hat, gehabt hat ergibt sich aus dem Vorbringen der Bfin  nicht, weil die Bfin im Schreiben vom 9.3.2020 selbst vorgebracht hat, dass die  Lebensgemeinschaft im Jahr 2020 begründet wurde.

**False Positives:**

- `KT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_316`)


Mit Mail vom 26.8.2020 übermittelte die Richterin dem Bf. per Mail die Beweisfotos, das  Schreiben, welches der Magistrat an Dr. YYY gerichtet hatte, den Rückschein, die Niederschrift  über die mündliche Verhandlung und ein Schreiben, dessen Inhalt in der Folge wiedergegeben  wird:  "Anbei wird die Niederschrift der heutigen mündlichen Verhandlung übermittelt, in welcher die  Zeugin (das Organ der Parkraumüberwachung, welches die Anzeige gelegt hat, Frau ZEUGIN)  einvernommen wurde.

**False Positives:**

- `ZEUGIN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat`(organisation)
- `Dr. YYY`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_217`)


Schließlich kann nach Ansicht des Bundesfinanzgerichtes auch durch die Einvernahme der  Tante des Bf. (Frau D.) als Zeugin nichts für die Feststellung gewonnen werden, ob beim Bf. die  Erwerbsunfähigkeit bereits vor dem 21.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Am 7.7.2008 wurde ein Strafantrag der belangten Behörde gegen die Geschäftsführerin Frau  GF der Beschwerdeführerin Floriane Rötker (in der Folge als Bf bezeichnet) an das Magistratische  Bezirksamt gestellt wegen illegaler Beschäftigung von Ausländern gem. § 3 Abs. 1 AuslBG.

**False Positives:**

- `GF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Floriane Rötker`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_56`)


Zum Nachweis dessen legte die bf. Vertreterin den Leistungsbericht des betreuenden  Sachbearbeiters der Kanzlei und einer Mitarbeiterin Frau H. bei.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_60`)


sei der Postausgang im kanzleieigenen EDV-Programm (BMD) von Frau L. erfasst und die  Gebühren dem Kunden verrechnet worden.

**False Positives:**

- `L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_62`)


Die Beschwerde wurde mit dem Einschreibzettel  (Einschreibvignette) versehen und von Frau L. (Mitarbeiterin der Kanzlei) als pdf- Datei  archiviert worden.

**False Positives:**

- `L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_38`)


Obmann ist  Herr B.  Der Bf ist Alleineigentümer der unbelasteten Liegenschaft an der Grundstücksadresse in  Grundstücksadresse

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

**False Positives:**

- `WM` — no gold match — likely missing annotation
- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Lisa Lindnau`(person)
- `Lisa Lindnau`(person)
- `Lisa Lindnau`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lisa Lindnau`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_54`)


Am 06.12.2013 wurde ein Tauschvertrag zwischen dem Beschwerdeführer … und Herrn WM …  abgeschlossen.

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_64`)


Im Bescheid wird festgestellt, dass der zwischen Herrn WM und dem Bf abgeschlossene  Flurbereinigungsvertrag vom 06.12.2013 hinsichtlich des neu gebildeten Grundstückes Nr. zz,  EZ2, für die Durchführung der Flurbereinigung im Sinne der §§ 1 und 28 Oö.

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_66`)


Bei dem angeführten Grundstück handelt es sich um jenes, welches Herr WM  dem Beschwerdeführer übertragen hat.

**False Positives:**

- `WM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_25`)


Im Vorlagebericht wurde seitens des Finanzamtes folgende  Stellungnahme angeführt:  „Die Abgabenbehörde beantragt die Abweisung des Alleinverdienerabsetzbetrages, da Frau A.  nicht nur die von Herrn Bernett angeführten Einkünfte in Höhe von 5.118,52 Euro erzielt hat,  sondern auch eine Abfertigung von der Vorsorgekasse erhalten hat.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Bernett`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_6`)


I. Verfahrensgang  Kaufvertrag, Werkvertrag  Mit Kaufvertrag vom 15./19.01.2015 erwarben die Beschwerdeführerin (kurz: Bf) und Herr CE  von der P-GmbH, als Verkäuferin, das neu gebildete Grundstück Nr. 433/20, vorgetragen ob  der Liegenschaft EZ-1, Grundbuch XY, Bezirksgericht A, jeweils zur Hälfte.

**False Positives:**

- `CE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht A`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_11`)


Weiters verwies sie darauf, dass der der Behörde vorgelegte klinische psychologische Befund  des Universitätsklinikums vom 21.05.2019 von Mag. W. der Grund für den Bezug der erhöhten  Familienbeihilfe (FB) wäre und die Notwendigkeit der Therapie beinhalte.

**False Positives:**

- `W.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_87`)


Die von der Bf für das Jahr 2019 geltend gemachten Therapiekosten für die Behebung der bei  ihrer Tochter festgestellten Lernstörung (Legasthenie, Mag. C.) in Höhe von gesamt € 1906,49  werden als ag. B. anerkannt.

**False Positives:**

- `C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache KzlR Hon.-Prof. Veit Balsottemeyer, Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich, über die Beschwerde vom 8. September 2021 gegen den Bescheid des Finanzamtes  Österreich vom 24. August 2021 betreffend Abweisung des Antrages vom 28. August 2020 auf  Auszahlung der Familienbeihilfe ohne Indexierung ab 1. Jänner 2019, Steuernummer 55-184/3803,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Hon.-Prof. Veit Balsottemeyer`(person)
- `Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `55-184/3803`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/137900.1`) (sent_id: `deanon_BFG_20260814_TEST/137900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Maurice Speckner,  Hinterweg 94, 2305 Pframa, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 88-902/6713  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Maurice Speckner`(person)
- `Hinterweg 94, 2305 Pframa, Österreich`(address)
- `Finanzamtes`(organisation)
- `88-902/6713`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_40`)


Bei den vorgelegten Unterlagen handelt es sich einerseits um Mietverträge und andererseits  um Schreiben des Herrn DI J M.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_41`)


Im angeführten Postskriptum dieser Schreiben hat Herr DI M  folgendes angeführt:  PS.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_18`)


Hinsichtlich der Haftungsbescheide zur KESt für die Jahre 2007-2009 wurde festgestellt, „dass  irrtümlich Herr GP als Empfänger der Kapitalerträge angeführt wurde.

**False Positives:**

- `GP` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. in der Verwaltungsstrafsache gegen  Pjotr Kristall, Schöngrabenweg 12I, 4870 Mösendorf, Österreich, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs 2  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 6. September 2022,  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  22. August 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Pjotr Kristall`(person)
- `Schöngrabenweg 12I, 4870 Mösendorf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/138846.1`) (sent_id: `deanon_BFG_20260814_TEST/138846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Techn R Simon Leyn,  Obere Mölten 37, 8232 Stambach, Österreich, über die Beschwerden vom 23. September 2021 gegen die Bescheid des  Finanzamtes Österreich vom 13. September 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 und Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 85-971/5131  zu Recht erkannt:   I. Der Beschwerde gegen den Einkommensteuerbescheid 2019 wird im Umfang der  Beschwerdevorentscheidung Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Techn R Simon Leyn`(person)
- `Obere Mölten 37, 8232 Stambach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-971/5131`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_575`)


Mieten (bis auf jene des Bruders) damit erklärte, dass „solche nicht darstellbar waren bzw.  voraussichtlich nicht beweisbar gewesen wäre, dass bzw. in welcher Höhe der Klient weitere  Mieteinnahmen bei ordnungsgemäßer Ausführung des Werkes durch Herrn XY erzielen hätte  können.“

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/138911.1`) (sent_id: `deanon_BFG_20260814_TEST/138911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde der Mag.a Selina Kreutle, Kaposigasse 101, 4906 Pumberg, Österreich, vom 6. September 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 1. August 2022, GZ. MA67/Zahl/2022, wegen einer der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, zu Recht erkannt:  Die Beschwerde vom 6. September 2022 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als  verspätet zurückgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Selina Kreutle`(person)
- `Kaposigasse 101, 4906 Pumberg, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Leonhard Osskinat, Schreyvogelgasse 2V, 8262 Leithen, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid des Finanzamtes  Baden Mödling, nunmehr Finanzamt Österreich, vom 18. Oktober 2019 betreffend Abweisung  des Antrages vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur  Familienbeihilfe für Hartmut Groebmair  ab Juli 2019,   Steuernummer 39-801/9564, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Leonhard Osskinat`(person)
- `Schreyvogelgasse 2V, 8262 Leithen, Österreich`(address)
- `Finanzamtes  Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)
- `Hartmut Groebmair`(person)
- `39-801/9564`(tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_10`)


In Beantwortung der Schreiben des Finanzamtes übermittelte die Bf. am 25. Juni 2020 folgende  Unterlagen betreffend ihren Sohn A.:   – Psychologisches Gutachten von Dr. Mag. E.Sch., Klinische und Gesundheitspsychologin,  allgemein beeidete und gerichtlich zertifizierte Sachverständige für Psychologie,  Psychotherapeutin, und Quirin Spillmann, LLB  Klinische und Gesundheitspsychologin, vom 26. Juni 2019   – Hörverarbeitungsscreening durch Hörtrainer N.R. vom 14. November 2019   (Ergebnis auffällig;

**False Positives:**

- `E.Sch` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Dr. Mag. E.Sch.`(person)
- `Quirin Spillmann, LLB`(person)
- `N.R.`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_11`)


Empfehlung zu weiteren Tests bzw. Beratungsgespräch)   – Schreiben der Dr. Mag. E.Sch., w.o., vom 18. Dezember 2019 (Zusammenfassung der  Ergebnisse der erfolgten Begutachtung bezüglich einer vermuteten Legasthenie)   – Schulnachricht der Klasse 6 (6. Schulstufe) der Rudolf Steiner … Freie Waldorfschule vom  14. Februar 2020 (Deutsch genügend, Mathematik nicht genügend, Englisch nicht genügend)   – Befundbericht von Univ. Prof.Charlotte Koebbe  Facharzt für Hals-, Nasen-, Ohrenheilkunde, Kopf- und  Halschirurgie, allgemein beeideter und gerichtlich zertifizierter Sachverständiger vom 27. Mai  2020 (Diagnose: Verdacht auf auditive Verarbeitungsstörung;

**False Positives:**

- `E.Sch` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)
- `Charlotte Koebbe`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_24`)


Um eine tiefgreifende Entwicklungsstörung zu diagnostizieren, wird  mein Sohn bei Hrn. Mag. L.N. diesbezüglich mehrere Tests durchlaufen müssen.

**False Positives:**

- `L.N` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_27`)


Die restlichen benötigten Termine bei Hm. Mag. L.N. gebe ich  gerne bekannt, sobald mir diese vorliegen.

**False Positives:**

- `L.N` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_36`)


Diesem Schreiben war ein klinisch-neuropsychologischer Befund der Mag.a B.A., Klinische und  Gesundheitspsychologin, Klinische Neuropsychologin, Arbeitspsychologin, vom 11. November  2020 über eine Untersuchung des Kindes am 9. November 2020 beigelegt.

**False Positives:**

- `B.A` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_80`)


Schließlich wurde von der Bf. der klinisch-psychologische Befund (dient zur Vorlage für  diagnostische und therapeutische Maßnahmen) von Mag. S.J., Klinische Psychologin,  Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021 nachgereicht.

**False Positives:**

- `S.J` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_92`)


Empfehlung:   -Psychotherapie für A. mit begleitenden Elterngesprächen   -Förderung der Konzentrationsfähigkeit, -Lese-Rechtschreibförderung   Diagnose nach ICD 10: expressive Sprachschwäche F 80.1, Lese-Rechtschreibschwäche F 81.0,  Störung mit sozialer Ängstlichkeit des Kindesalters F 93.2   II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Situation des im Jänner 2007 geborenen Sohn der Bf. stellt sich folgendermaßen dar  (Auszug aus dem zuletzt vorgelegten klinisch-psychologischen Befund von Mag. S.J., Klinische  Psychologin, Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021):   Der Sohn A. besucht die 3. Klasse einer Neuen Mittelschule.

**False Positives:**

- `S.J` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_232`)


Bei der Begutachtung fand das eingangs im Punkt Verfahrensgang genannte, von der Bf.  beschaffte und im Verfahren vorgelegte psychologische Gutachten der Dr. Mag. E.Sch.,  Klinische und Gesundheitspsychologin, allgemein beeidete und gerichtlich zertifizierte  19 von 24 Seite 20 von 24

**False Positives:**

- `E.Sch` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_273`)


- Schließlich wird im klinisch-psychologischen Befund von Mag. S.J., Klinische Psychologin,  Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021 – Vorstellungsgrund war  wiederum Verdacht auf Autismus – als Anlass für die Untersuchung festgehalten: „… die  Kriterien einer Autismus-Spektrums-Störung wurden nicht zur Gänze erfüllt. Speziell  eingeengten Interessen, stereotypen Verhaltensabläufe und die Über- bzw.  Unterempfindlichkeit gegenüber Reizen fehlen bei A. für eine eindeutige ASS-Diagnose.

**False Positives:**

- `S.J` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_37`)


Der BF lebte  im Beschwerdezeitraum an der Adresse Adr Ö BF gemeinsam mit seiner Frau EB in deren  Einfamilienhaus.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/139347.1`) (sent_id: `deanon_BFG_20260814_TEST/139347.1_46`)


Am 13.09.2013 wurde auf  Frau EB ein Kraftfahrzeug VW Golf Plus mit dem gleichen Kennzeichen in Österreich  angemeldet.

**False Positives:**

- `EB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Ing. Nicoletta Papastergios,  Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich  über die Beschwerde vom 12. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 31. März 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 94-528/7027  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `IBV` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing. Nicoletta Papastergios`(person)
- `Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `94-528/7027`(tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_15`)


Die Unterlagen [des Bf.] befanden sich in St. Marein,  die Unterlagen von Frau DM bei ihrem Steuerberater, Mag. H, in Graz.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_32`)


3. Missbrauch von Formen und Gestaltungsmöglichkeiten  Frau DM wohnte in den geprüften Jahren immer im Ausland.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_34`)


Frau DM handelte mit Kosmetikprodukten und Nahrungsergänzungsmitteln, sie lieferte Waren  an ihren Vater, [den Bf.] in Österreich und nach Deutschland.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_111`)


Zu Punkt 3 der Niederschrift:   Der Abgabepflichtige handelt(e) mit den von Frau DM (seiner Tochter) bezogenen Waren und  belieferte Kunden in Österreich sowie im europäischen Ausland.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_112`)


Es waren dies ausschließlich  Kunden des [Bf.], Frau DM unterhielt zum Großteil dieser Kunden keine geschäftlichen  Beziehungen.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_113`)


Der Abgabepflichtige handelte in eigenem Namen und auf eigene Rechnung und  trug das alleinige unternehmerische Risiko für den erfolgreichen Verkauf der von Frau DM  bezogenen Waren.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_162`)


Zu Pkt. 11 der Niederschrift   Es wird von der Behörde nicht schlüssig dargelegt, in welchem Zusammenhang die Unterlagen  von Herrn GM* mit dem Außenprüfungsverfahren stehen.

**False Positives:**

- `GM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_173`)


Natürlich wurden alle Waren, die von Frau DM an  [den Bf.] geliefert wurden, in beiden Buchhaltungen gleichermaßen erfasst.“  11 von 33 Seite 12 von 33

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_277`)


(„Frau DM wohnte in den geprüften Jahren immer im  Ausland…“) oder S. 8ff.

**False Positives:**

- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_18`)


Am 7. Oktober 2022 wurde von der Zulassungsbesitzerin bekanntgegeben, dass das Fahrzeug  zu den angeführten Beanstandungszeiten Herrn O., 1160 Wien, Str1, überlassen war.

**False Positives:**

- `O.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/140416.1`) (sent_id: `deanon_BFG_20260814_TEST/140416.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache OMedR Frauke Klutzuweit, Weberkogelstraße 114, 8632 Weichselboden, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 23. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 18. Februar 2021 betreffend Feststellung der Einkünfte § 188 BAO 2019 zu  Steuernummer 50-666/0525  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Frauke Klutzuweit`(person)
- `Weberkogelstraße 114, 8632 Weichselboden, Österreich`(address)
- `N & N Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `50-666/0525`(tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_58`)


den Namen GS geführt habe und dass Herr GK der Bruder von AS bzw Herr S der Vater von GK  (früher GS) und AS sei, Stellung zu nehmen.

**False Positives:**

- `GK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_73`)


Der frühere Name von  Herrn GK war GS.

**False Positives:**

- `GK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_75`)


Gesellschafter der BF im Jahr 2013 war Herr S.  Die Fa. I wurde von Herrn DO und Herrn KW im Jahr 2001 gegründet.

**False Positives:**

- `S.` — no gold match — likely missing annotation
- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_76`)


Herr DO war bis Herbst  2004 Gesellschafter der Fa. I.  Alleiniger Geschäftsführer der Fa. I ist seit 2004 Herr KW.

**False Positives:**

- `DO` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_80`)


Gesellschafter der U sind  seit Gründung Herr AS und Herr DO.

**False Positives:**

- `AS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_96`)


Mit Email vom 20.02.2013 teilte Herr KW der BF mit, dass die Fa. I aus wirtschaftlichen  Gründen das Angebot vom 15.02.2013 nicht annehmen könne, da die Gesellschafter den  genannten Betrag nicht aufbringen könnten.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_113`)


Die Feststellungen, dass der frühere Name von Herrn GK „GS“ war, dass GK der Sohn von S ist  sowie, dass AS der Bruder von GK ist, wurden von Herrn GK in der mündlichen Verhandlung vor  dem Bundesfinanzgericht am 04.05.2023 bestätigt.

**False Positives:**

- `GK` — no gold match — likely missing annotation
- `GK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_115`)


Die letzte dem Bundesfinanzgericht vorgelegte Mahnung gründet sich auf eine  Email der BF an den Geschäftsführer der Fa. I, Herrn KW vom 05.01.2005.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_116`)


Herr KW hat im Schreiben vom 10.11.2022 ausgeführt, dass es seitens der BF über einen  längeren Zeitraum mehrere Mahnungen per Email gegeben habe, um Druck auf die Fa. I  aufzubauen.

**False Positives:**

- `KW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_123`)


Die Feststellung, dass Herr DO und Herr DM keine nahestehenden Personen zu den  Machthabern der BF sind, gründet sich vor allem auf die festgestellten Beteiligungsverhältnisse  im Beschwerdezeitraum an der BF und an der Fa. I.   Die belangte Behörde hat zwar in der Beschwerdevorentscheidung vom 05.02.2020 bzw. im  Vorlagebericht vom 23.08.2022 aufgezeigt, dass teilweise vor Verkauf der Forderung und auch  9 von 17 Seite 10 von 17

**False Positives:**

- `DO` — no gold match — likely missing annotation
- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_126`)


Herr DO  und Herr DM waren im Beschwerdezeitraum weder an der BF noch an der Fa. I unmittelbar  oder mittelbar beteiligt noch mit dem Gesellschafter der BF verwandt.

**False Positives:**

- `DO` — no gold match — likely missing annotation
- `DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/140945.1`) (sent_id: `deanon_BFG_20260814_TEST/140945.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Klara Hienz, Oberfrödenegg 16W, 4952 Appersting, Österreich, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit §  4 Abs. 2 Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 24. März  2023 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  24. November 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Klara Hienz`(person)
- `Oberfrödenegg 16W, 4952 Appersting, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Cornelia Reifs,  Hub an der Mank 8, 9300 Draschelbach, Österreich, vom 25. Mai 2023, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 26. April  2023, GZ. MA67/Zahl/2022, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien  Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cornelia Reifs`(person)
- `Hub an der Mank 8, 9300 Draschelbach, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter X. in der Beschwerdesache Sibylle Bungards, Perratgasse 13, 7210 Mattersburg, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien, über die Beschwerde vom  18. Dezember 2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 22. November 2018  betreffend Umsatzsteuer 2015 und Umsatzsteuer 2016 Steuernummer 63-751/1771  zu  Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sibylle Bungards`(person)
- `Perratgasse 13, 7210 Mattersburg, Österreich`(address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `63-751/1771`(tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Nadja Bloemendaal, Rapsweg 11, 5151 Gastein, Österreich, vertreten durch CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.,  Klagenfurter Straße 32a, 9300 St.Veit/Glan, über die Beschwerde vom 25. März 2019 gegen  den Bescheid des Finanzamtes St. Veit Wolfsberg vom 19. März 2019 betreffend  Einkommensteuer 2017 Steuernummer 91-908/3748  nach der am 5. Juni 2023  durchgeführten mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nadja Bloemendaal`(person)
- `Rapsweg 11, 5151 Gastein, Österreich`(address)
- `CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.`(organisation)
- `Finanzamtes St. Veit Wolfsberg`(organisation)
- `91-908/3748`(tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Philipp Boniek, Montjolastraße 6l, 9815 Preisdorf, Österreich, vertreten durch CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.,  Klagenfurter Straße 32a, 9300 St.Veit/Glan, über die Beschwerde vom 31. August 2020 gegen  den Bescheid des Finanzamtes Österreich vom 24. August 2020 betreffend Einkommensteuer  2018 Steuernummer 69-366/4106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Philipp Boniek`(person)
- `Montjolastraße 6l, 9815 Preisdorf, Österreich`(address)
- `CONFIDA St. Veit Wirtschaftstreuhand- gesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `69-366/4106`(tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Istvan  Melniczenko, Stritzelberggasse 69, 9142 Jaunstein, Österreich, über die Beschwerde des Beschuldigten vom 16. Juni 2022 gegen  den Zurückweisungsbescheid des Magistrates der Stadt Wien vom 2. Juni 2022, Zahl:  MA67/XX/2021, mit dem der Einspruch vom 3. Mai 2022 gegen die Strafverfügung vom 29.  November 2021 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet  zurückgewiesen wurde, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Istvan  Melniczenko`(person)
- `Stritzelberggasse 69, 9142 Jaunstein, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/141392.1`) (sent_id: `deanon_BFG_20260814_TEST/141392.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Michaela Ondracsek, Arnsdorfer Straße 153, 4881 Kronberg, Österreich, über die Beschwerde vom 11. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 30. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-938/6957  zu Recht erkannt:   I.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Michaela Ondracsek`(person)
- `Arnsdorfer Straße 153, 4881 Kronberg, Österreich`(address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `92-938/6957`(tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/141421.1`) (sent_id: `deanon_BFG_20260814_TEST/141421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Christine Bortnyk,  Sproamüllergasse 9, 3970 Weitra, Österreich, über die Beschwerde vom 10. Oktober 2022 gegen den  Rückforderungsbescheid des Finanzamtes Österreich vom 26. August 2022 betreffend  Familienbeihilfe und Kinderabsetzbetrag für das Kind To für die Monate September 2021 bis  Mai 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `IBV` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Christine Bortnyk`(person)
- `Sproamüllergasse 9, 3970 Weitra, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_20`)


Das Ermittlungsverfahren habe ergeben, dass ein Ausweis gemäß § 29b mit der Nummer 123  für Frau N., ausgestellt worden sei.

**False Positives:**

- `N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_21`)


Auf Nachfrage beim Sozialministeriumservice, 1010 Wien,  sei der Behörde mitgeteilt worden, dass der für Frau N. ausgestellte Ausweis zum  Beanstandungszeitpunkt keine Gültigkeit mehr besessen habe, da dieser bis 1. August 2020  befristet gewesen sei.

**False Positives:**

- `N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_88`)


In der Mail vom 29.05.2018 habe der StV an die Versicherung folgendes Ersuchen gerichtet:  „Da Herr T.. VN Fn gerne eine Einmalzahlung von der GmbH haben möchte, würde ich  den kapitalisierten Betrag aus der zugesagten Pension in Höhe von € 1.452 (lt.  Pensionszusage vom 1.6.2006) benötigen.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_125`)


Auch eine steuerliche  Würdigung dieses Schreibens unsererseits war unseres Erachtens ohne Relevanz, da immer die  besprochene Einmalzahlung das wahre Wesen dieser Vereinbarung darstellt. Die  Pensionszusage des Herrn T.. VN Fn wurde somit mit einem Wert von € 420.000 abgefunden.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Ulrich Büldmöller,  Hochwassersiedlung 7, 4070 Simbach, Österreich, über die Beschwerde vom 18. März 2022 gegen den Bescheid des Finanzamtes  Österreich vom 21. Dezember 2021 betreffend Zwangsstrafen 2021, Steuernummer BF1StNr2  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrich Büldmöller`(person)
- `Hochwassersiedlung 7, 4070 Simbach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_33`)


Vom Finanzamt  Österreich/Dienststelle Fachbereich wurde uns hierzu mitgeteilt, dass die Vergabe einer zweiten  Steuernummer aus verwaltungstechnischen Gründen initiiert ist (Mail Mag. H. 27.07.2022).

**False Positives:**

- `H.` — partial — pred is substring of gold: `Mag. H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Mag. H.`(person)

**Example 97** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_46`)


Im Zuge eines Telefonats hat sich der Sachverhalt  aufgeklärt und der zuständige Bearbeiter Herr K. (BV-Team 23, Finanzamt1/23) hat den  bekämpften Bescheid noch am selben Tag mit Mail vom 17.03.2022 an uns gesandt.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Emilia Geyer,  Lukasberg 15, 9064 Ottmanach, Österreich, über die Beschwerde vom 14. September 2022 gegen den  Rückforderungsbescheid des Finanzamtes Österreich vom 9. September 2022 betreffend  Familienbeihilfe und Kinderabsetzbetrag für die Kinder K1, K2, K3 und K4 NN für die Monate  April 2022 bis September 2022 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `IBV` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Emilia Geyer`(person)
- `Lukasberg 15, 9064 Ottmanach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Role Indicators (Richter/Richterin)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b6b4a900`  
**Description:**
Matches full title+name sequences following judicial roles, ensuring titles like Dr., Mag., Priv.-Doz. are included in the capture and suffixes are handled.

**Content:**
```
(?:durch\s+(?:den|die)\s+(?:Richter|Richterin|Ri))\s+(?:OMedR|MedR|StR|OStR|KzlR|LLB|VetR|Ri)?\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|Hon\.-Prof\.|DDr\.in?|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Gesellschafter Full Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `46b44975`  
**Description:**
Matches full names following 'Gesellschafter', capturing multi-word names and suffixes, specifically handling cases where the name is just initials or a short form.

**Content:**
```
\bGesellschafter(?:n)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Richter Title Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `65772489`  
**Description:**
Matches full names following 'durch den Richter' or 'durch die Richterin', handling complex titles and ensuring the full name is captured including hyphenated surnames. Handles concatenated titles like 'RichterinRi'.

**Content:**
```
(?:durch\s+(?:den|die)\s+(?:Richter|Richterin|Ri))\s+(?:OMedR|MedR|StR|OStR|KzlR|LLB|VetR|Ri)?\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|Hon\.-Prof\.|DDr\.in?|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `N.N. Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `67cddbb2`  
**Description:**
Explicitly matches the anonymized name placeholder 'N.N.' which is common in legal texts.

**Content:**
```
\bN\.N\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Dr.in with Placeholder Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4624ae28`  
**Description:**
Matches anonymized names with titles like 'Dr.in Dok1' or 'Mag. NN'.

**Content:**
```
(?:Dr\.in|Mag\.|RA)\s+([A-Z]\.[A-Za-z]+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Names after Hinsichtlich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0df3f6e6`  
**Description:**
Matches names following 'hinsichtlich' which often introduces the person of interest in administrative proceedings.

**Content:**
```
(?:hinsichtlich)\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)+)(?=,|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Names after Preposition 'bei' (Tightened)` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a12c3bcc`  
**Description:**
Matches names after 'bei' but explicitly excludes common location suffixes and administrative terms to prevent false positives like city names or company names. Added stricter exclusion for common Austrian town names.

**Content:**
```
\bbei\s+([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:[ -][A-Z][a-zA-Z]+)*)(?=,|$|[.](?!.*(?:Straße|Gasse|Platz|Weg|Avenue|Landstraße|Finanzamt|GmbH|AG|Gesellschaft|m\.b\.H)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 87 | 0 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 87 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_59`)


Gesetzesunkenntnis oder irrtümliche, objektiv fehlerhafte Rechtsauffassungen sind nach der  stRsp des VwGH nur dann entschuldbar und nicht als Fahrlässigkeit zuzurechnen, wenn die  objektiv gebotene, der Sach e nach pflichtgemäße, nach den subjektiven Verhältnissen  zumutbare Sorgfalt nicht außer Acht gelassen wurde (vgl zB VwGH 27.9.2000, 96/14/0174, und  die bei Ritz, BAO6 § 135 Rz 10 angeführten Nachweis der Rsp des VwGH).

**False Positives:**

- `Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_30`)


§ 1 Abs. 1 der ab der Veranlagung 2013 anzuwendenden Verordnung lautet:  „Bei der Ermittlung des Gewinnes bei Betrieben, für die eine Gewerbeberechtigung für das  Gastgewerbe (§ 111 der Gewerbeordnung 1994 – GewO 1994, BGBl. I Nr. 194) erforderlich ist  und während des gesamten Wirtschaftsjahres vorliegt, können nach Maßgabe der folgenden  Bestimmungen Betriebsausgaben pauschal berücksichtigt werden.“  § 1 Abs.2 der VO nennt als weitere Anwendungsvoraussetzungen:   „1.

**False Positives:**

- `Betrieben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_175`)


Zur Unzulässigkeit einer Revision  Gegen dieses Erkenntnis ist eine Revision des Beschwerdeführers an den  Verwaltungsgerichtshof (Art. 133 Abs. 4 B-VG) gemäß § 25a Abs. 4 VwGG nicht zulässig,  da bei Verwaltungsstrafsachen, bei denen eine Geldstrafe von bis zu 750 Euro verhängt  werden darf und im Erkenntnis eine Geldstrafe von bis zu 400 Euro verhängt wird, eine  Verletzung in subjektiven Rechten (Art. 133 Abs. 6 Z 1 B-VG) ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_104`)


Gemäß § 11 Abs. 1 Z 3 UStG 1994 gehören zu den Angaben, die eine Rechnung enthalten muss,  u.a. der Name und die Anschrift des liefernden oder leistenden Unternehmers (lit. a), bei  Rechnungen, deren Gesamtbetrag EUR 10.000,00 übersteigt, weiters die dem  Leistungsempfänger vom Finanzamt erteilte Umsatzsteuer-Identifikationsnummer, wenn der  leistende Unternehmer im Inland einen Wohnsitz (Sitz), seinen gewöhnlichen Aufenthalt oder  eine Betriebsstätte hat und der Umsatz an einen anderen Unternehmer für dessen  Unternehmen ausgeführt wird (lit b.) sowie die dem Unternehmer vom Finanzamt erteilte  Umsatzsteuer-Identifikationsnummer, soweit der Unternehmer im Inland Lieferungen oder  sonstige Leistungen erbringt, für die das Recht auf Vorsteuerabzug besteht (lit. i).

**False Positives:**

- `Rechnungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_39`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (siehe dazu die bei Doralt, EStG  Kommentar, § 16 Tz 220 "Versicherungen" angeführten Judikate, wie zB VwGH vom  22.10.1991, 91/14/0043) sind Prämien für eine Berufsunfähigkeitsversicherung lediglich dann  als Werbungskosten abzugsfähig, wenn ausschließlich die Berufsunfähigkeit infolge eines  typischen Berufsrisikos versichert wird.

**False Positives:**

- `Doralt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_82`)


seit 2006 bei Prof. Maida in Behandlung.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_85`)


Behandlungen / Medikamente / Hilfsmittel: Efectin 225mg, Inkotan 15mg, Lasix 40mg,  Pantoprazol 20mg, PK-Merz, Pregabalin 75mg 2x1, Sirdalud 4mg 2x1, Zyprexa 2,5mg 1-2-4-0,  Copaxone Inj.lösung, etc.; FÄ-Betreuung bei Dr. Fux alle 6 Wochen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Fux`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Fux`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_205`)


Lebensjahr (bzw.  bei Berufsausbildung, 25. Lebensjahr) zugelassen hätten.

**False Positives:**

- `Berufsausbildung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_219`)


Nach dem medizinischen Wissensstand ist der Verlauf psychischer Störungsbilder sehr vielfältig  und die Verläufe bei Kindern, Erwachsenen und alten Menschen sehr unterschiedlich.

**False Positives:**

- `Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_58`)


Wegen dieser Verwaltungsübertretung werde über den Bf. gem. § 4 Abs. 1 Parkometergesetz  2006 eine Geldstrafe von 60 €, bei Uneinbringlichkeit, eine Ersatzfreiheitsstrafe von 14  Stunden, verhängt.

**False Positives:**

- `Uneinbringlichkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Stainz` — partial — pred is substring of gold: `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Eugen Burgschweiger`(person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_71`)


Wie bereits im angefochtenen Bescheid ausgeführt wurde, normiert § 48 BAO Folgendes:  „Das Bundesministerium für Finanzen kann bei Abgabepflichtigen, die der Abgabenhoheit  mehrerer Staaten unterliegen, soweit dies zur Ausgleichung der in- und ausländischen  Besteuerung oder zur Erzielung einer den Grundsätzen der Gegenseitigkeit entsprechenden  Behandlung erforderlich ist anordnen, bestimmte Gegenstände ganz oder teilweise aus der  5 von 12 Seite 6 von 12

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesministerium für Finanzen`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_23`)


Dabei ist bei Pensionsabfindungen, die im Jahre 2001 zufließen, nach Abzug der da- rauf entfallenden Beiträge im Sinne des § 62 Z 3, 4 und 5 ein Viertel steuerfrei zu belassen.

**False Positives:**

- `Pensionsabfindungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_67`)


Dabei ist bei Pensionsabfindungen, die im Jahre  2001 zufließen, nach Abzug der darauf entfallenden Beträge im Sinne des § 62 Z 3, 4 und 5  ein Viertel steuerfrei zu belassen.

**False Positives:**

- `Pensionsabfindungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_104`)


Dabei ist bei Pensionsabfindungen, die im Jahre 2001 zufließen, nach  Abzug der darauf entfallenden Beiträge im Sinne des § 62 Z 3, 4 und 5 ein Viertel steuerfrei  zu belassen.

**False Positives:**

- `Pensionsabfindungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_56`)


generell auch bei Ch. Nowotny in Straube/Ratka/Rauter, UGB II/RLG3 § 198 Rn 152 mwN sowie  Maschek/Csokay in Jabornegg/Artmann (Hrsg), UGB Band 22 (2017) zu § 198 UGB Rz 64).

**False Positives:**

- `Ch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_66`)


Dabei ist bei Pensionsabfindungen, die im Jahre  2001 zufließen, nach Abzug der darauf entfallenden Beiträge im Sinne des § 62 Z 3, 4 und 5 ein  Viertel steuerfrei zu belassen.

**False Positives:**

- `Pensionsabfindungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_219`)


In allen übrigen Fällen – also bei Sachverhalten, die länger oder teils sogar schon Jahrzehnte  zurückliegen – kann der Sachverständige nur aufgrund von Indizien, insbesondere anhand von  vorliegenden Befunden, Rückschlüsse darauf ziehen, zu welchem oder ab welchem Zeitpunkt  eine "erhebliche" Behinderung eingetreten ist.

**False Positives:**

- `Sachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_57`)


Gemäß § 31 Abs. 5 FinStrG erlischt bei Finanzvergehen, für deren Verfolgung die  Finanzstrafbehörde zuständig ist, die Strafbarkeit jedenfalls, wenn seit dem Beginn der  Verjährungsfrist zehn Jahre und gegebenenfalls die in Abs. 4 lit. c genannte Zeit verstrichen  sind.

**False Positives:**

- `Finanzvergehen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_43`)


b  der MwStSystRL bei Dienstleistungen, deren Erbringungsort sich u. a. gemäß Art. 59 der  Mehrwertsteuerrichtlinie bestimmt, diesen Ort, der grundsätzlich außerhalb der Union liegt, so  behandeln, als läge er in ihrem Gebiet, wenn in ihrem Gebiet die tatsächliche Nutzung oder  Auswertung der Dienstleistungen erfolgt.

**False Positives:**

- `Dienstleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_75`)


Der Wegfall der Forderung gegenüber dem Käufer könne  nur ex nunc im Jahr 2014 berücksichtigt werden, nicht aber ex tunc bei Vertragsabschluss.

**False Positives:**

- `Vertragsabschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_74`)


2. Ergibt sich bei Steuerpflichtigen, die Anspruch auf den Verkehrsabsetzbetrag haben, nach  Abs. 1 und 2 eine Einkommensteuer unter null, sind 50% der Werbungskosten im Sinne des § 16  Abs. 1 Z 3 lit. a (ausgenommen Betriebsratsumlagen) und des § 16 Abs. 1 Z 4 und 5, höchstens  5 von 10 Seite 6 von 10

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_77`)


3. Ergibt sich bei Steuerpflichtigen, die Anspruch auf den Pensionistenabsetzbetrag haben, nach  Abs. 1 und 2 eine Einkommensteuer unter null, sind 50% der Werbungskosten im Sinne des § 16  Abs. 1 Z 4, höchstens aber 110 Euro jährlich, rückzuerstatten (SV-Rückerstattung).

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Silvius Jaros, Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2019 betreffend Einkommensteuer 2017 Steuernummer  97-301/3674  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mauer` — partial — pred is substring of gold: `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Astrid Binder`(person)
- `Silvius Jaros`(person)
- `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `97-301/3674`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_64`)


Leichte Fahrlässigkeit liegt vor bei Fehlern, die auch einem sorgfältigen Menschen gelegentlich  unterlaufen.

**False Positives:**

- `Fehlern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_32`)


Der Vertragserrichter Dr-F hat sehr wohl darauf hingewiesen bei Vertragsunterfertigung, dass  die Firma MH-Bau GmbH hier auch bereits andere Häuser errichtet hat bzw. errichtet, hat  jedoch ebenso darauf hingewiesen, dass kein Kontrahierungszwang mit dieser Firma besteht.

**False Positives:**

- `Vertragsunterfertigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MH-Bau GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_44`)


Wenn also der  Grundstückserwerber an ein bestimmtes, durch die Planung des Verkäufers oder eines mit  diesem zusammenarbeitenden Organisators vorgegebenes Gebäude gebunden ist, dann ist ein  Kauf mit herzustellendem Gebäude anzunehmen (vgl. die bei Fellner, aaO, § 5 Rz 88a  dargestellte Rechtsprechung, siehe diesbezüglich auch VwGH vom 14.10.1999, 97/16/0219,  17.10.2001, 2001/16/0230 und vom 21.3.2002, 2001/16/0429).

**False Positives:**

- `Fellner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache Jörg Kuhstoss, Hasenberg 58, 3240 Grub bei Kilb, Österreich, über die Beschwerde vom 3. April 2020 gegen den Bescheid des Finanzamtes  Österreich vom 16. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 70-705/2274  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Kilb` — partial — pred is substring of gold: `Hasenberg 58, 3240 Grub bei Kilb, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Jörg Kuhstoss`(person)
- `Hasenberg 58, 3240 Grub bei Kilb, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `70-705/2274`(tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_60`)


2. Ergibt sich bei Steuerpflichtigen, die Anspruch auf den Verkehrsabsetzbetrag haben, nach  Abs. 1 und 2 eine Einkommensteuer unter null, sind 50% der Werbungskosten im Sinne des § 16  Abs. 1 Z 3 lit. a (ausgenommen Betriebsratsumlagen) und des § 16 Abs. 1 Z 4 und 5, höchstens  aber 400 Euro jährlich rückzuerstatten (SV-Rückerstattung).

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_87`)


Die Betriebskosten selbst werden,  außer bei Leerstand, meistens vom Mieter übernommen.

**False Positives:**

- `Leerstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_178`)


Zur Unzulässigkeit der Revision  Eine Revision der Bf. an den Verwaltungsgerichtshof ist auf der Grundlage des § 25a Abs. 4  VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine Geldstrafe von  bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von nicht mehr als 400  Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_149`)


Z 2. Ergibt sich bei Steuerpflichtigen, die Anspruch auf den Verkehrsabsetzbetrag haben, nach  Abs 1 und 2 eine Einkommensteuer unter null, sind 50% der Werbungskosten im Sinne des §  16 Abs 1 z 3 lit a EStG 1988 (ausgenommen Betriebsratsumlagen) und des § 16 Abs 1 Z 4 und 5   EStG 1988, höchstens aber 400 Euro jährlich rückzuerstatten (SV-Rückerstattung).

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_24`)


Um eine tiefgreifende Entwicklungsstörung zu diagnostizieren, wird  mein Sohn bei Hrn. Mag. L.N. diesbezüglich mehrere Tests durchlaufen müssen.

**False Positives:**

- `Hrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_27`)


Die restlichen benötigten Termine bei Hm. Mag. L.N. gebe ich  gerne bekannt, sobald mir diese vorliegen.

**False Positives:**

- `Hm` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_95`)


Mit diesem in Art. 11  Abs. 1 der Verordnung Nr. 883/2004 verankerten Grundsatz sollen Ungleichbehandlungen  beseitigt werden, die bei Arbeitnehmern, die innerhalb der Union zu- und abwandern, die Folge  einer teilweisen oder vollständigen Kumulierung der anwendbaren Rechtsvorschriften wären.

**False Positives:**

- `Arbeitnehmern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_36`)


Dabei ist bei Pensionsabfindungen, die im Jahre 2001 zufließen, nach Abzug der  darauf entfallenden Beiträge im Sinne des § 62 Z 3, 4 und 5 ein Viertel steuerfrei zu belassen.

**False Positives:**

- `Pensionsabfindungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Imre Zeitner  in der Beschwerdesache des  Daisy Schlimme, Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich, vertreten durch Henning & Partner Steuerberatung GmbH,  Brockmanngasse 75, 8010 Graz, sowie durch Dr. Michael Kotschnigg, Franzensbrückenstraße 5,  1020 Wien, über die Beschwerde vom 15. Jänner 2016 gegen die Bescheide des Finanzamtes  Graz-Umgebung (nunmehr: Finanzamt Österreich) vom 9. Dezember 2015 betreffend   1) Wiederaufnahme der Verfahren hinsichtlich Umsatzsteuer 2009 bis 2011 sowie  2) Einkommensteuer und Umsatzsteuer je 2009 bis 2014   den BESCHLUSS gefasst:   I. Die angefochtenen Bescheide (sowie die bezüglichen Beschwerdevorentscheidungen)  werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an die Abgabenbehörde  aufgehoben.

**False Positives:**

- `Gleisdorf` — partial — pred is substring of gold: `Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Imre Zeitner`(person)
- `Daisy Schlimme`(person)
- `Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich`(address)
- `Henning & Partner Steuerberatung GmbH`(organisation)
- `Dr. Michael Kotschnigg`(person)
- `Finanzamtes  Graz-Umgebung`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_12`)


2. Allgemeine Feststellungen zur BP   Die Bp bei Fr. DI DM wurde am 04.12.2012 begonnen, nachdem zuvor eine Bp bei [dem Bf.],  dem Vater von Frau DM, durchgeführt worden war.

**False Positives:**

- `Fr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI DM`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_25`)


es kann  weder festgestellt werden, ob die Bf. bereits im Jahr 2020 wegen dieser Erkrankung bei Dr.XY –  einem Wahlarzt - in Behandlung stand, noch ob ihr die Einnahme diverser orthomolekularer  Substanzen ärztlich verordnet wurde.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_35`)


Die Negativfeststellung in Bezug auf die Behandlung bei Dr.XY gründet auf nachfolgenden  Überlegungen: Eingangs ist festzuhalten, dass das Beweisverfahren vom Grundsatz der freien  Beweiswürdigung beherrscht wird (§ 167 BAO).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_43`)


All diese Prämissen vorausgeschickt, bestand  aufgrund des durchgeführten Beweisverfahrens keine Veranlassung, festzustellen, dass die Bf.  im Jahr 2020 wegen der chronischen Polyarthritis bei Dr. XY in Behandlung gestanden wäre:  Einerseits datiert der Arztbrief mit 23.06.2022 und wurde somit – wie aus dem Verfahrensgang  ersichtlich – erst nach Erlassung des angefochtenen Bescheides im Zuge der  Beschwerdeerhebung verfasst bzw. vorgelegt.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_46`)


Die Zweifel an der Richtigkeit der  Verfahrensbehauptung der Bf. im Zusammenhang mit dem behandelnden Arzt werden auch  durch nachfolgendes Faktum unterstrichen: Wie eine Abfrage auf der Homepage der Kärntner  Ärztekammer ergab, handelt es sich bei Dr. XY um einen sog.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_53`)


beschwerdefrei ist“, und der strittige Arztbrief Dr. XY erst erstellt und vorgelegt wurde,  nachdem die belangte Behörde das Schreiben Dr. AB in ihrer Bescheidbegründung als  ungeeignetes Beweismittel erachtete, so können die Ausführungen der Bf., sie sei bereits seit  2019 bei Dr. XY in Behandlung, insgesamt nicht überzeugen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_55`)


wahrscheinlicher ist, dass sie 2020 in Behandlung bei Dr. AB stand, schließlich hat dieser Arzt  auch am 24.06.2020 Probenmaterial der Bf. an ein medizinisches Labor übermittelt (vgl.  Rechnungen DDr.GH vom 29.06.2020).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_49`)


Dabei gilt:  - Die Verluste müssen durch ordnungsmäßige Buchführung oder bei Steuerpflichtigen, die  ihren Gewinn gemäß § 4 Abs. 3 ermitteln, durch ordnungsgemäße Einnahmen- Ausgaben-Rechnung, ermittelt worden sein.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_235`)


§ 23 Abs. 4 FinStrG bestimmt,  dass bei Finanzvergehen, deren Strafdrohung sich nach einem Wertbetrag richtet, die  Bemessung der Geldstrafe mit mindestens einem Zehntel des Höchstmaßes der angedrohten  Geldstrafe zu erfolgen hat.

**False Positives:**

- `Finanzvergehen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_82`)


(2) Bemessungsgrundlage für die Grundvergütung ist bei  1. vom Bund gemieteten  a) Wohnungen und  b) sonstigen Räumlichkeiten  der Hauptmietzins, den der Bund zu leisten hat,  2. im Eigentum des Bundes stehenden Baulichkeiten oder bei Baulichkeiten, für die der Bund die  Kosten der notwendigen Erhaltung trägt, obgleich sie nicht im Eigentum des Bundes stehen,  sowie bei sonstigen Baulichkeiten jeweils jener Hauptmietzins, den der Bund bei Neuvermietung  der Baulichkeit üblicherweise erhalten würde.

**False Positives:**

- `Baulichkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_147`)


die Behörde ist vielmehr verpflichtet, von einer als  gesetzwidrig erkannten Verwaltungsübung abzugehen (s. dazu zB die bei Ritz, BAO 7.

**False Positives:**

- `Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_212`)


Es genügt nicht, dass ein solcher Antrag in einem  ergänzenden Schriftsatz gestellt wird (s. dazu die bei Ritz, BAO 7.

**False Positives:**

- `Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_185`)


Es wird gleichsam eine Conditio sine qua  non zwischen der Belastung des ersten Umsatzes (entweder Steuerbefreiung oder  Vorsteuerzug) und der Besteuerung nach Art. 41 Mehrwertsteuerrichtlinie aufgestellt. In  ähnlicher Weise wird das EuGH-Urteil auch in der Literatur interpretiert, die den fehlenden  Vorsteuerabzug aus der Lieferung (A-B) als unrichtigen Steuerausweis interpretieren und nicht  weiter in Frage stellen (vgl. Langer, Ronny, Straferwerbsteuer auch bei USt-IdNr. aus dem  Abgangsland – aber nicht bei Doppelbesteuerung, Umsatzsteuernewsletter 29/2022,  https://www.kmlz.de/sites/default/files/Umsatzsteuer%20Newsletter%2029_2022_0.pdf).

**False Positives:**

- `USt-IdNr` — no gold match — likely missing annotation
- `Doppelbesteuerung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/141383.1`) (sent_id: `deanon_BFG_20260814_TEST/141383.1_44`)


Gem. § 115 Abs. 1 BAO wird diese Verpflichtung durch eine erhöhte Mitwirkungspflicht der  Abgabepflichtigen, wie beispielsweise bei Auslandssachverhalten, eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_28`)


Auf die von Gesetzes wegen bestehenden Offenlegungspflichten gemäß §§ 119 und 138 BAO  und die erhöhte Mitwirkungspflicht der Partei bei Sachverhalten, die ihre Wurzeln im Ausland  haben, weist das Finanzamt explizit hin.“

**False Positives:**

- `Sachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_68`)


Dazu wurde in der Beschwerdevorentscheidung des Weiteren auch ausdrücklich auf die gem.  §§ 119 und 138 Bundesabgabenordnung (BAO) normierte Offenlegungspflichten und die  erhöhte Mitwirkungspflicht der Partei bei Sachverhalten, die ihre Wurzel im Ausland haben,  hingewiesen.

**False Positives:**

- `Sachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_53`)


Dies ist unecht steuerbefreiten Kleinunternehmern genauso der Fall wie bei Landwirten, für die  die Ust-Pauschalierung gilt.   Die Amtsvertreterin teilt mit, dass sie die Anmerkung eines Regelbesteuerungsantrages gemäß  § 6 Abs. 3 UStG (Verzicht auf die unechte Steuerbefreiung) im Steuerakt des Bf. umfassend  nachgeprüft habe.

**False Positives:**

- `Landwirten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/143721.1`) (sent_id: `deanon_BFG_20260814_TEST/143721.1_39`)


Ihre Tätigkeiten übte sie überwiegend in den Büroräumlichkeiten in der  öffentlichen Impfstraße im BB aus, ein geringer Teil der Tätigkeiten fand direkt in der  Impfstraße statt, etwa in der Problemlösung bei Beschwerden.

**False Positives:**

- `Beschwerden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_405`)


Bei einigen Produktkategorien  erfolge jedoch eine Beschaffung über zentral verwaltete Budgetmittel, zB bei Dienstkleidung.

**False Positives:**

- `Dienstkleidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_157`)


Nach § 11 Abs. 1 Z 5 GebG 1957 entsteht die Gebührenschuld bei Zeugnissen, die von  ausländischen Behörden ausgestellt worden sind, sobald von ihnen im Inland ein amtlicher  Gebrauch gemacht wird, auch wenn sie nur in beglaubigter oder unbeglaubigter Abschrift  verwendet werden (vgl. in Fellner, aaO, Rz 8 zu § 11 GebG).

**False Positives:**

- `Zeugnissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_97`)


Doch während bei Stromproduzenten, ohne dies, wie oben ausgeführt, sachlich zu begründen,  der Umsatz als Bemessungsgrundlage herangezogen werde, stelle der EKB-f auf den Gewinn  ab.

**False Positives:**

- `Stromproduzenten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_306`)


der Preis für alle Marktteilnehmer wird jedoch durch das letzte  Kraftwerk bestimmt, das zur Deckung der Nachfrage benötigt wird, d. h. durch das Kraftwerk  mit den höchsten Grenzkosten bei Markt-Clearing.

**False Positives:**

- `Markt-Clearing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thassilo Osipenko  in der Beschwerdesache des  Agatha Stingele, Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich, vertreten durch Mag. Hedwig Maria Weber, Ausseer Straße 32,  8940 Liezen, über die Beschwerden vom 5. August 2020 gegen die Bescheide des Finanzamtes  Österreich vom 7. Juli 2020 betreffend Festsetzung der Normverbrauchsabgabe (NoVA- Vergütung gemäß § 12a NoVAG) für   1) den Zeitraum 4 – 12/2019 und   2) den Zeitraum 1/2020,   Steuernummer 39-913/2428, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

**False Positives:**

- `Randegg` — partial — pred is substring of gold: `Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Thassilo Osipenko`(person)
- `Agatha Stingele`(person)
- `Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich`(address)
- `Mag. Hedwig Maria Weber`(person)
- `Finanzamtes  Österreich`(organisation)
- `39-913/2428`(tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_114`)


Zur Unzulässigkeit der Revision  Gegen dieses Erkenntnis ist eine Revision des Bf. an den Verwaltungsgerichtshof (Art. 133  Abs.4 B-VG) gemäß § 25a Abs. 4 VwGG nicht zulässig, da bei Verwaltungsstrafsachen, bei  denen eine Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine  Geldstrafe von bis zu 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten (Art. 133  Abs. 6 Z 1 B-VG) ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_199`)


Nach § 7 Abs. 3 KStG 1988 sind u.a. bei Steuerpflichtigen, die auf Grund der Rechtsform nach  unternehmensrechtlichen Vorschriften zur Rechnungslegung verpflichtet sind, alle Einkünfte  den Einkünften aus Gewerbebetrieb zuzurechnen.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/144968.1`) (sent_id: `deanon_BFG_20260814_TEST/144968.1_20`)


Dabei gilt:  - Die Verluste müssen durch ordnungsgemäße Buchführung oder bei Steuerpflichtigen,  die ihren Gewinn gemäß § 4 Abs.3 ermitteln, durch ordnungsgemäße Einnahmen- Ausgaben-Rechnung, ermittelt worden sein.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_104`)


Bleiben Sie bis zum Erhalt der Bestätigung bei Ihrem Fahrzeug.

**False Positives:**

- `Ihrem Fahrzeug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vivian Gastell  in der Beschwerdesache Dipl.-Ing. Tosca Toussaint,  Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 25. Mai 2023 betreffend Abweisung des Antrags vom 6. Februar 2023 auf  Erstattung des Mehrkindzuschlages auf Grund der  Verhältnisse des Jahres 2022,  Steuernummer 82-564/6636, SV-Nr. Nr., zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

**False Positives:**

- `Oed` — partial — pred is substring of gold: `Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Vivian Gastell`(person)
- `Dipl.-Ing. Tosca Toussaint`(person)
- `Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `82-564/6636`(tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_79`)


Der Rechtfertigungsbedarf sei somit bei Subjektsteuern höher  als bei Objektsteuern, weil bei letzteren idR ein zumutbares Ausweichverhalten möglich sei.

**False Positives:**

- `Objektsteuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_271`)


Während bei Stromproduzenten, ohne dies sachlich zu begründen, der Umsatz als  Bemessungsgrundlage herangezogen werde, stelle der EKB-f auf den Gewinn ab.

**False Positives:**

- `Stromproduzenten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_470`)


der Preis für alle Marktteilnehmer wird jedoch durch das letzte  Kraftwerk bestimmt, das zur Deckung der Nachfrage benötigt wird, d. h. durch das Kraftwerk  mit den höchsten Grenzkosten bei Markt-Clearing.

**False Positives:**

- `Markt-Clearing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_141`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/146305.1`) (sent_id: `deanon_BFG_20260814_TEST/146305.1_14`)


In den Fällen der Nichterteilung einer Erlaubnis kommt es für die Frage der Vollzugstauglichkeit  auf die konkrete Gestaltung der Rechtslage an und es ist zu prüfen, ob im Versagungsbescheid  nicht noch mehr an rechtlichen Wirkungen steckt als die bloße Nicht-Gewährung der  angestrebten Erlaubnis oder Begünstigung (vgl. die Beispiele bei Puck, Die aufschiebende  Wirkung bei Beschwerden vor den Gerichtshöfen des öffentlichen Rechts, ZfV 1982, 359, 363  f).

**False Positives:**

- `Puck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_68`)


So ist  VwGH 19.9.1995, 95/14/0050 bereits auf Ebene der Zurückweisung „strenger“ und fordert  nicht nur ein Vorhandensein, sondern eine bestimmte Qualität der Angaben über die  Rechtzeitigkeit in dem Sinn, dass die Angaben darüber Aufschluss geben, wann die  Beschwerdeführerin - tatsächlich - von diesen Vorgängen oder von der Fristversäumung  Kenntnis erlangt hat - somit, dass die Rechtzeitigkeit hieraus erkennbar ist; und nach VwGH  23.10.2002, 2002/16/0222, ist im Wiedereinsetzungsantrag darzustellen, wann das Hindernis,  das die Partei an der rechtzeitigen Vornahme der befristeten Prozesshandlung hinderte,  weggefallen (VwGH 23.10.2002, 2002/16/0222 unter Hinweis auf die bei Ritz, BAO- Kommentar2 unter Rz 7 zu § 309a BAO referierte hg.

**False Positives:**

- `Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/146819.1`) (sent_id: `deanon_BFG_20260814_TEST/146819.1_22`)


Über Ersuchen teilte die Bf. dem Bundesfinanzgericht mit, dass sie alle Tätigkeiten, welche  im Zusammenhang mit der Vermietungstätigkeit stehen, selbst vornehme wie die Bewerbung  freier Wohnungen, Mietersuche und Auswahl, Abschluss von Mietverträgen und Übergabe der  Wohnungen, Organisieren der Durchführung von Reinigungsarbeiten vor Übergabe und nach  Rückgabe der Wohnungen und der allgemeinen Teile, Entgegennahme und Verwahrung der  Kautionen, Veranlassung von Instandhaltungs- und Instandsetzungsaufwendungen, Ab/An-  Ummeldung bei Energieversorgern bei Mieterwechsel, Erstellung der Abrechnung und  Kontrolle der Mietzinsvorschreibungen, der Betriebs-, Heiz und Warmwasserkosten, etc..  2 von 12 Seite 3 von 12

**False Positives:**

- `Mieterwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_328`)


der Preis für alle Marktteilnehmer wird jedoch durch das letzte  Kraftwerk bestimmt, das zur Deckung der Nachfrage benötigt wird, d. h. durch das Kraftwerk  mit den höchsten Grenzkosten bei Markt-Clearing.

**False Positives:**

- `Markt-Clearing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_329`)


der Preis für alle Marktteilnehmer wird jedoch durch das letzte  Kraftwerk bestimmt, das zur Deckung der Nachfrage benötigt wird, d. h. durch das Kraftwerk  mit den höchsten Grenzkosten bei Markt-Clearing.

**False Positives:**

- `Markt-Clearing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_194`)


Diese  Verpflichtung wird durch eine erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie  beispielsweise bei Auslandssachverhalten, eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_370`)


Nach § 6 Abs 6 NoVAG 1991 idF BGBl. I Nr. 13/2014 ist bei Gebrauchtfahrzeugen, die  unmittelbar aus dem übrigen Gemeinschaftsgebiet in das Inland gebracht werden, ist bei  Vorliegen der Voraussetzungen die vor dem 1. März 2014 geltende Rechtslage anzuwenden.

**False Positives:**

- `Gebrauchtfahrzeugen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_169`)


Nach § 11 Abs. 1 Z 5 GebG 1957 entsteht die Gebührenschuld bei Zeugnissen, die von  ausländischen Behörden ausgestellt worden sind, sobald von ihnen im Inland ein amtlicher  Gebrauch gemacht wird, auch wenn sie nur in beglaubigter oder unbeglaubigter Abschrift  verwendet werden (vgl. in Fellner, aaO, Rz 8 zu § 11 GebG).

**False Positives:**

- `Zeugnissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_127`)


Zur Unzulässigkeit der Revision:   Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_124`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_101`)


Dies gilt nur,  – wenn die Verluste durch ordnungsmäßige Buchführung oder bei Steuerpflichtigen, die  ihren Gewinn gemäß § 4 Abs. 3 ermitteln, durch ordnungsgemäße Einnahmen- Ausgaben-Rechnung, ermittelt worden sind und  – soweit die Verluste nicht bereits bei der Veranlagung für die vorangegangenen  Kalenderjahre berücksichtigt wurden.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/148990.1`) (sent_id: `deanon_BFG_20260814_TEST/148990.1_21`)


Er wird von beiden Parteien übereinstimmend  dargestellt.  3. Rechtliche Beurteilung  3.1 Zu Spruchpunkt I. (Beschwerdeabweisung)  § 33 Abs 8 Z 3 des Einkommensteuergesetzes 1988 (EStG) in der Fassung BGBl I 153/2023 für  die Veranlagung 2024 lautet:  „Ergibt sich bei Steuerpflichtigen, die Anspruch auf den (erhöhten) Pensionistenabsetzbetrag  haben, nach Abs. 1 und 2 eine Einkommensteuer unter null, sind 80% der Werbungskosten im  Sinne des § 16 Abs. 1 Z 4, höchstens aber 637 Euro jährlich, rückzuerstatten (SV- 2 von 5 Seite 3 von 5

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/149120.1`) (sent_id: `deanon_BFG_20260814_TEST/149120.1_83`)


Der Umfang der Leistungen bei Alter, Tod und Invalidität ergibt  sich aus dem Vertrag oder Reglement (Art. 13 Abs. 1 FZV).

**False Positives:**

- `Alter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/149650.1`) (sent_id: `deanon_BFG_20260814_TEST/149650.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Angelika Nottebusch, Zickenberg 63, 2134 Ernsdorf bei Staatz, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018 über die Beschwerde des  Beschuldigten vom 18. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 3. September 2025, Zahl: MA67/MA-GZ/2025 zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit Folge gegeben, als die  Geldstrafe von € 175,00 auf € 40,00 und die für den Fall der Uneinbringlichkeit festgesetzte  Ersatzfreiheitsstrafe von 1 Tag und 17 Stunden auf 9 Stunden herabgesetzt wird.

**False Positives:**

- `Staatz` — partial — pred is substring of gold: `Zickenberg 63, 2134 Ernsdorf bei Staatz, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karoline Windsteig`(person)
- `Angelika Nottebusch`(person)
- `Zickenberg 63, 2134 Ernsdorf bei Staatz, Österreich`(address)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/149650.1`) (sent_id: `deanon_BFG_20260814_TEST/149650.1_121`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu € 750 verhängt werden darf und im Erkenntnis eine Geldstrafe von nicht  mehr als € 400 verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/149610.1`) (sent_id: `deanon_BFG_20260814_TEST/149610.1_193`)


Wenn die Bf. ihrer Mutter im Haus und Garten und ihrem Vater bei Leistungen, die ohne sie für  ihn nur schwer durchführbar gewesen wären, zur Seite stand, so basierte dies nicht auf einer  nachgewiesenen „Pflegebedürftigkeit“, sondern erfolgten ihre Leistungen im Rahmen der  familienhaften Beistandspflicht.

**False Positives:**

- `Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/149728.1`) (sent_id: `deanon_BFG_20260814_TEST/149728.1_135`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu € 750 verhängt werden darf und im Erkenntnis eine Geldstrafe von nicht  mehr als € 400 verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

</details>

---

## `Names after Company Prefix 'Fa.' (Tightened)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `eb203b20`  
**Description:**
Matches names after 'Fa.' ensuring the match is a person and not a company name, by requiring a space and capital letter pattern typical of names.

**Content:**
```
\bFa\.\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*)(?=,|$|[.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_58`)


Das PDA-Gerät bezieht die Daten von der Fa. Atos.

**False Positives:**

- `Atos` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_318`)


das Fahrzeug Ford Mustang wurde nachweislich in den Jahren  2012 – 2014 im Ausland gewartet und repariert (siehe vorgelegte Reparatur- und  Servicerechnungen der Fa. AA. in D/XX).

**False Positives:**

- `AA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_11`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (Fa. ZB, Straße, 1220 Wien)  eingeholten Lenkerauskunft mit Strafverfügung vom 28. Oktober 2020, an, er habe das  Fahrzeug am 19. August 2020 in der gebührenpflichtigen Kurzparkzone in 1220 Wien,  Schüttaustraße 4-10, ohne einem für den Beanstandungszeitpunkt 14:34 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

**False Positives:**

- `ZB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Landespolizeidirektion Wien`(organisation)

</details>

---

## `Names in Parentheses/Context (Fixed)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6efe971a`  
**Description:**
Matches names appearing in specific contexts like '(Nachname wie Bf.)' or '(geboren am ...)' which often follow a name, capturing the full name.

**Content:**
```
(?:für\s+die\s+Tochter|für\s+das\s+Kind|Nachname\s+wie\s+Bf\.?)\s+([A-Z][a-z]+(?:[ -][A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Complex Academic Titles with Spacing` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8d838eae`  
**Description:**
Matches persons with complex academic titles that may have spacing issues (e.g., 'Univ- Prof.'), ensuring the full name is captured.

**Content:**
```
(?:Univ\-?\s*Prof\.|Priv\.-Doz\.|Dipl\. Kfm\.|Dipl\.-Ing\.|Hon\.-Prof\.)\s+(?:Mag\.a?|Dr\.in?|RgR|KzlR|LLB|VetR|Ri)?\s+[A-Z][a-zA-ZÀ-ÿ]+(?:-[A-Z][a-zA-ZÀ-ÿ]+)*(?:\s+[A-Z][a-zA-ZÀ-ÿ]+)*(?:-[A-Z][a-zA-ZÀ-ÿ]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc))?(?=\s|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Diana Sammer`(person)
- `Dipl.-Ing. KzlR Otto Thiesgen`(person)
- `Gränzing 2, 4841 Brunau, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_5`)


Die dagegen von der Dipl.-Ing. KzlR Juri Strube  im Namen der Bf. erhobene Beschwerde vom 21. Dezember  2023 wurde mit Beschwerdevorentscheidung vom 22. März 2024 abgewiesen.

**False Positives:**

- `` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_6`)


Am 23. Juli 2024  stellte die Dipl.-Ing. KzlR Juri Strube  im Namen der Bf. innerhalb verlängerter Frist den Antrag auf Vorlage  der Beschwerde an das BFG.

**False Positives:**

- `` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)
- `BFG`(organisation)

</details>

---

## `Richter Title Names (Concatenated)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c5657986`  
**Description:**
Matches full names following 'durch den Richter' or 'durch die Richterin', handling concatenated titles like 'RichterRi'.

**Content:**
```
(?:durch\s+(?:den|die)\s+(?:Richter|Richterin|Ri|RichterRi))\s+(?:OMedR|MedR|StR|OStR|KzlR|LLB|VetR|Ri)?\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|Hon\.-Prof\.|DDr\.in?|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Names with Suffixes in Legal Context (Fixed)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `aa59ba58`  
**Description:**
Matches full names following legal context phrases like 'in der Beschwerdesache', ensuring suffixes like Bakk. techn., MBA are captured.

**Content:**
```
(?:in der Beschwerdesache(?: des)? )([A-Z][a-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+䑄[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+)(?:,? \s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?(?:,? \s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Standalone Names in Narrative Context` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d808da1`  
**Description:**
Matches standalone names following prepositions like 'von der', 'mit', 'bei' or appearing as subjects/objects in narrative sentences, capturing full names including hyphenated surnames and suffixes, while excluding company names.

**Content:**
```
(?:von\s+(?:der|die|dem|des)\s+|mit\s+|bei\s+(?!.*(?:Straße|Gasse|Platz|Weg|Avenue|Landstraße|Finanzamt|GmbH|AG|Gesellschaft|m\.b\.H)))\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MAS|Bakk\. rer\. nat|Bakk\. art\. BEd)?)?)?(?=,|$|[.](?!.*(?:GmbH|AG|Gesellschaft)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 43 | 0 | 43 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 43 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_67`)


darüber hinaus habe  er sich bereits nach der Teilnahme am ersten von drei Kursen der „Kurzausbildung mit  Dr. Gunther Schmidt – Hypnosystemische Konzepte für Coaching, Team &  Organisationsentwicklung und Supervision“ im Herbst 2018 entschieden, sich im Laufe der Zeit  ein weiteres „Standbein“ aufzubauen, um die erworbenen Kenntnisse als  freiberuflicher/selbständiger Coach anzubieten.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Gunther Schmidt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Gunther Schmidt`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_158`)


Mit Bescheid vom 4.8.1999 wurde ihr vom zuständigen Magistrat  gemäß den maßgeblichen Bestimmungen des Steiermärkischen Prostitutionsgesetzes (LGBl.  Nr. 16 vom 27.2.1998) die Bewilligung zum Betrieb bzw. zur Fortführung eines Bordells (einer  bordellähnlichen Einrichtung) unter den auszugsweise oben wörtlich wieder gegebenen  Auflagen erteilt. In der behördlich aufliegenden Hausordnung heißt es unter Punkt 10.: „Der  vom Betrieb für die Leistung der Prostituierten festgesetzte Preis darf nur von der  Betriebsleitung, nicht aber von der Prostituierten selbst, eingehoben werden.“

**False Positives:**

- `Betriebsleitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_313`)


Zur Zulässigkeit der Revision   Gegen dieses Erkenntnis ist eine Revision des Beschwerdeführers an den  Verwaltungsgerichtshof (Art. 133 Abs. 4 B-VG) gemäß § 25a Abs. 4 VwGG nicht zulässig, da bei  Verwaltungsstrafsachen, bei denen eine Geldstrafe von bis zu 750 Euro verhängt werden darf  und im Erkenntnis eine Geldstrafe von bis zu 400 Euro verhängt wird, eine Verletzung in  subjektiven Rechten (Art. 133 Abs. 6 Z 1 B-VG) ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_122`)


Zur Zulässigkeit der Revision   Gegen dieses Erkenntnis ist eine Revision des Beschwerdeführers an den  Verwaltungsgerichtshof (Art. 133 Abs. 4 B-VG) gemäß § 25a Abs. 4 VwGG nicht zulässig, da bei  Verwaltungsstrafsachen, bei denen eine Geldstrafe von bis zu 750 Euro verhängt werden darf  und im Erkenntnis eine Geldstrafe von bis zu 400 Euro verhängt wird, eine Verletzung in  subjektiven Rechten (Art. 133 Abs. 6 Z 1 B-VG) ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_134`)


Nr 400/1988 können bei  Gebäuden, die der Erzielung von Einkünften aus Vermietung und Verpachtung dienen, ohne  Nachweis der Nutzungsdauer jährlich 1,5 % der Bemessungsgrundlage (lit a bis d leg cit) als AfA  geltend gemacht werden.

**False Positives:**

- `Gebäuden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_17`)


Seit 2006 bei  Prof. Maida wegen MS in Behandlung.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_45`)


Selbst wenn Belange der Vermietungstätigkeit in Österreich vorgenommen werden, werden im  vorliegenden Fall alle für die Vermietungstätigkeit wesentlichen Entscheidungen (Beginn,  Dauer und Ende der Vermietungstätigkeit, Privatnutzung des Objektes, Veräußerung des  Objektes, Betrauung oder Nichtbetrauung einer Immobilienverwaltungsfirma mit  Dienstleistungsarbeiten, Betrauung oder Nichtbetrauung von Handwerkern, Erteilung und  Umfang einer allfälligen Bevollmächtigung) vom Vermieter außerhalb Österreichs getroffen.

**False Positives:**

- `Dienstleistungsarbeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_60`)


Selbst wenn Belange der Vermietungstätigkeit in Österreich vorgenommen werden, werden im  vorliegenden Fall alle für die Vermietungstätigkeit wesentlichen Entscheidungen (Beginn,  Dauer und Ende der Vermietungstätigkeit, Privatnutzung des Objektes, Veräußerung des  Objektes, Betrauung oder Nichtbetrauung einer Immobilienverwaltungsfirma mit  Dienstleistungsarbeiten, Betrauung oder Nichtbetrauung von Handwerkern, Erteilung und  Umfang einer allfälligen Bevollmächtigung) vom Vermieter außerhalb Österreichs getroffen.

**False Positives:**

- `Dienstleistungsarbeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_102`)


GP) der  Anpassung an die unionsrechtlichen Vorgaben dient und auf die EuGH-Urteile in den Rs  Schmelz und Stoppelkamp verweisen (vgl.: Ruppe/Achatz in Ruppe/Achatz (Hrsg),  Umsatzsteuergesetz: Kommentar5 (2017), § 6 UStG, Rz 446), richtet sich die Voraussetzung des  Betreibens eines Unternehmens im Inland nach den unionsrechtlichen Begriffen des Sitzes der  wirtschaftlichen Tätigkeit oder des Ortes einer festen Niederlassung, von dem aus Umsätze  bewirkt werden (vgl.: Luketina, Umsatzsteuerliche Ansässigkeit von Kleinunternehmern bei  Immobilienvermietung, ÖStZ 2019/234, 175).

**False Positives:**

- `Immobilienvermietung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schmelz`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_118`)


Aufgrund der in dieser Bestimmung normierten Fahrlässigkeitsvermutung bei  Ungehorsamdelikten, erschöpft sich der tatbestandliche Unwert diesfalls im Zuwiderhandeln  gegen den Handlungsbefehl einer ordnungsgemäßen Entrichtung der Parkometerabgabe bei  Abstellen eines mehrspurigen Kraftfahrzeuges in einer Kurzparkzone (vgl zB Lewisch in  Lewisch/Fister/Weilguni, VStG, § 5 Rz 6 mwN; sowie VwGH 23.11.2001, 2001/02/0184).

**False Positives:**

- `Ungehorsamdelikten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_12`)


5. Da in den Beschwerden bzw. im Vorlageantrag unterschiedliche Arbeitsbeginnzeiten von der  Bf. angegeben wurden (06:00 Uhr laut Beschwerden, 06:45 laut Vorlageantrag), ergaben sich  unterschiedliche Berechnungen des Pendlerpauschales bei der Abfrage im Pendlerrechner.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_42`)


(…) Der Wohnsitz meiner Eltern ist (…) in der Nähe von mir und daher bin ich in 10 Minuten bei  Ihnen.“

**False Positives:**

- `Ihnen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_76`)


Seit  6. Dezember 2010 ist der Beschwerdeführer durchgehend in Österreich gemeldet, im Zeitraum  16. April 2012 bis 5. Juni 2012 und seit 2. Mai 2013 (und somit auch in den  verfahrensgegenständlichen Jahren) mit Hauptwohnsitz, in der übrigen Zeit mit  Nebenwohnsitz.

**False Positives:**

- `Nebenwohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_25`)


Die Beurteilung, ob ein Tauschvorgang vorliegt, ist für jede von der  Zusammenlegung , Flurbereinigung oder Baulandumlegung betroffene Person gesondert  vorzunehmen;

**False Positives:**

- `Zusammenlegung ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_123`)


Erst wenn die Kryptowährung von der  Bf. in die digitale Geldbörse des Kunden übertragen worden sei, habe dieser selbst darüber  verfügen, sie für neue Managed-Hosting-Pakete verwenden oder in ein eigenes privates  „Wallet“ übertragen können.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_56`)


Gemäß § 31 Abs. 4 lit. b FinStrG werden in die Verjährungsfrist nicht eingerechnet die Zeit,  während der wegen der Tat gegen den Täter ein Strafverfahren bei der Staatsanwaltschaft, bei  Gericht, bei einer Finanzstrafbehörde oder beim Bundesfinanzgericht geführt wird.

**False Positives:**

- `Gericht` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_127`)


Weiters stellte die Bf. mit Schriftsätzen vom 3.4.2018 und 10.1.2019 klar, dass sich die von der  Bf. in der Selbstanzeige offen gelegten Beträge auf alle jene Kunden beziehen, die sich mit  einer österreichischen Adresse bei der Bf. registriert haben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_17`)


Die Werkverträge jener Fälle die nicht mit Baukosten selbstverechnet wurden, wurden von der  Fa. MH nach Vorhalt am 9.11.2017 vorgelegt.“  2 von 14 Seite 3 von 14

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_43`)


Die Rechtslage ab 1.1.2014 bis 31.12.2018 (diese sei vom VfGH Ende 2017 mit dem oben  angesprochenen Erkenntnis aufgehoben worden) erlaube die Wiederaufnahme nur bei  Anträgen, die vor Eintritt der Verjährung gestellt werden.

**False Positives:**

- `Anträgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_84`)


Bei grenzüberschreitenden Sachverhalten mit Bezug zum übrigen EU-Gebiet steht die  Anwendung der vorstehenden Bestimmungen unter dem Vorbehalt der Übereinstimmung mit  EU-Recht.

**False Positives:**

- `EU-Recht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_882`)


Das Vorliegen einer derartigen Absicht ist für jede organisatorisch in sich  geschlossene und mit einer gewissen Selbständigkeit ausgestattete Einheit gesondert zu  beurteilen.“  § 2 LVO legt in den Abs 1 und 2 für die durch § 1 Abs 1 der VO erfassten Betätigungen mit  Einkunftsquellenvermutung, soweit diese nicht unter Abs.3 der Bestimmung fallen, Kriterien  fest, an Hand welcher das Vorliegen einer Absicht im Sinn des § 1 Abs 1 zu prüfen ist.

**False Positives:**

- `Einkunftsquellenvermutung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_108`)


Das Arbeitszimmer war voll möbliert mit  Schreibtisch, Stuhl, Drucker und Bücherregal und ist ausschließlich als Homeoffice verwendet  worden.

**False Positives:**

- `Schreibtisch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_160`)


Dieser Einzelarbeitsplatz ist zwar kein ständiger, ausschließlich von der  Bf. genutzter Einzelarbeitsplatz (da sie ihn 1 Woche im Voraus buchen muss), jedoch kann sie  einen derartigen Einzelarbeitsplatz immer dann benützen, wenn sie an einem  Einzelarbeitsplatz im Bürogebäude der Arbeitgeberin arbeiten will.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_84`)


Nach § 3 Abs. 2 GebG sind die festen Gebühren durch Barzahlung, durch Einzahlung mit  Erlagschein, mittels Bankomat- oder Kreditkarte oder durch andere bargeldlose elektronische  Zahlungsformen zu entrichten.

**False Positives:**

- `Erlagschein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_211`)


Diese Verpflichtung wird durch  eine erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt.“  17 von 30 Seite 18 von 30

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_149`)


Nach § 2 Abs. 2 EStG 1988 ist Einkommen der  Gesamtbetrag der Einkünfte aus den im Abs. 3 aufgezählten Einkunftsarten nach Ausgleich mit  Verlusten, die sich aus einzelnen Einkunftsarten ergeben, und nach Abzug der Sonderausgaben  (§ 18) und außergewöhnlichen Belastungen (§§ 34 und 35) sowie des Freibetrags nach § 105.

**False Positives:**

- `Verlusten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_112`)


Diese Verpflichtung wird durch  eine erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_138`)


Zur Unzulässigkeit der Revision  Gegen dieses Erkenntnis ist eine Revision des Beschwerdeführers an den  Verwaltungsgerichtshof (Art. 133 Abs. 4 B-VG) gemäß § 25a Abs. 4 VwGG nicht zulässig, da bei  Verwaltungsstrafsachen, bei denen eine Geldstrafe von bis zu 750 Euro verhängt werden darf  und im Erkenntnis eine Geldstrafe von bis zu 400 Euro verhängt wird, eine Verletzung in  subjektiven Rechten (Art. 133 Abs. 6 Z 1 B-VG) ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_13`)


In beiden Fällen hat A Rechnungen mit 10% österreichischer Umsatzsteuer gelegt, die von der  Bf. (B) als Vorsteuer in Abzug gebracht wurde.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/141421.1`) (sent_id: `deanon_BFG_20260814_TEST/141421.1_96`)


Diese Verpflichtung wird durch  eine erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_276`)


Da bei Außenprüfungen idR  Wiederaufnahmen der Einkommensteuerveranlagungen erfolgen, führt bei  Rechtsmittelverfahren, insbesondere, wenn noch außerordentlichen Rechtsmitteln zu den  Höchstgerichten anschließen, auch die Verjährung der Folgejahre zu einer realistischen  Begrenzung der Eingriffsmöglichkeiten.

**False Positives:**

- `Rechtsmittelverfahren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_67`)


Diese Verpflichtung wird allerdings durch eine  erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_24`)


Wie aus den Daten der  Finanzverwaltung ersichtlich ist, machte die Kindesmutter bis jetzt auch tatsächlich von der  Möglichkeit, den Antrag auf Familienbonus Plus zurückzuziehen, keinen Gebrauch.

**False Positives:**

- `Möglichkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_190`)


Hält man sich nämlich vor Augen, dass dem vom  VwGH entschiedenen Fall die Sanierung von bestehenden Aufzugssystemen zugrunde lag,  wobei einerseits Leichtbaukabinen sowie Notrufsysteme geliefert und eingebaut, wie auch  Mängel behoben wurden und die dort maßgeblichen Arbeiten auch die Erneuerung von  Fangkorbgleitachsen, Seilen, Antrieben, Dichtsätzen und Seilschlössern miteinschloss, somit  Maßnahmen, die keine Schadensbehebungen darstellen, kann der Rechtsansicht der Bf.,  wonach eine Großreparatur eine solche zur Voraussetzung haben müsse, nicht gefolgt werden.

**False Positives:**

- `Maßnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/143852.1`) (sent_id: `deanon_BFG_20260814_TEST/143852.1_38`)


4) …. .“  § 27a Abs 1 EStG 1988 idgF lautet:  „Einkünfte aus Kapitalvermögen unterliegen  1. im Fall von Geldeinlagen und nicht verbrieften sonstigen Forderungen bei       Kreditinstituten, ausgenommen Ausgleichzahlungen und Leihgebühren       gemäß § 27 Abs. 5 Z 4, einem besonderen Steuersatz von 25%,  2. in allen anderen Fällen einem besonderen Steuersatz von 27,5%       und sind bei der Berechnung der Einkommensteuer des Steuerpflichtigen        weder beim Gesamtbetrag der Einkünfte noch beim Einkommen        (§ 2 Abs. 2) zu berücksichtigen, sofern nicht die Regelbesteuerung (Abs. 5)        anzuwenden ist.

**False Positives:**

- `Kreditinstituten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_125`)


Ziel der EKB-S sei in eindeutiger Weise eine Reduzierung der Strompreise bei  Endverbraucherinnen.

**False Positives:**

- `Endverbraucherinnen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/144714.1`) (sent_id: `deanon_BFG_20260814_TEST/144714.1_31`)


Seit 1.6.2020 erhält der Sohn der Beschwerdeführerin Bezüge von der  Pensionsversicherungsanstalt.     2.

**False Positives:**

- `Pensionsversicherungsanstalt` — type mismatch — same span as gold: `Pensionsversicherungsanstalt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_217`)


- Durch den Hauptanprall wurde die komplette Radaufhängung mit allen Anbauteilen vorne  ausgerissen und verbogen, Vorderachsträger weist im Aufnahmebereich der unteren  Querlenker eine starke Verformung auf, Radhaus mit  Kotflügelbank, Federdomaufnahme und  Längsträgerschließteil sind erheblich nach innen verschoben sowie fortlaufend massiv   verformt, Batterieplusleitung im lnnenradhaus ist abgeknickt sowie die Hauptsicherungsdose  an der Batterie hat ausgelöst.

**False Positives:**

- `Kotflügelbank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_65`)


Diese Verpflichtung wird  durch eine erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt“.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_199`)


Bei einer Verwendung im Zusammenhang mit  Berufsbildern, bei welchen die berufliche Nutzung eines solchen Gerätes nach dem Urteil  gerecht und billig denkender Menschen zweckmäßig erscheint, kommt zugleich dem Kriterium  der Notwendigkeit seiner beruflichen Nutzung keine entscheidende Bedeutung zu. Doch  bedarf es, gerade wenn Aufwendungen vergleichbarer Art häufig auch in der Privatsphäre  anfallen, einer sorgfältigen Prüfung der beruflichen Veranlassung (VwGH 27.1.2011,  2010/15/0197;

**False Positives:**

- `Berufsbildern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/146446.1`) (sent_id: `deanon_BFG_20260814_TEST/146446.1_79`)


Daher habe etwa die Rechtsprechung des Verwaltungsgerichtshofes ausgesprochen, dass der  Wiedereinsetzungswerber alle Wiedereinsetzungsgründe innerhalb der gesetzlichen Frist  vorzubringen und glaubhaft zu machen hat und eine Auswechslung des Grundes im  Berufungsverfahren unzulässig ist (VwGH 26.1.1998, 96/17/0096, unter Hinweis auf die bei  Hauer-Leukauf, Handbuch des österreichischen Verwaltungsverfahrens5, 681, unter 2 und 7  zitierte Rechtsprechung).

**False Positives:**

- `Hauer-Leukauf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_409`)


Der Bf. erläuterte, dass die ag Bel ohne SB für das Kind Auslagen für Gerichtskosten im  Zusammenhang mit der Klage der GKK auf Kostenübernahme für verträgliche Therapien bei  Systemerkrankungen, Mehrfachallergien, allergischem Asthma und Immunschwäche betreffen.

**False Positives:**

- `Systemerkrankungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_236`)


Die Herkunft dieser Einlagen wurden von der  Bf. nicht aufgeklärt und wurde auch die vom Prokuristen aufgestellte Behauptung, dass die  Einlagen aus Einkünften des Prokuristen „in Kroatien und Riga“ stammten, weder  nachgewiesen noch glaubhaft gemacht.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Standalone Names in Context (von ... von)` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c993fc87`  
**Description:**
Matches standalone names appearing in contexts like 'von ... von' or 'bei ... bei', capturing full names including suffixes.

**Content:**
```
(?:von\s+)([A-Z][a-zA-Z]+(?:[ -][A-Z][a-zA-Z]+)+)(?:,?\s*(?:LL\.M(?!.*LLM)|LLB(?!.*LLB)|BEd(?!.*BEd)|B\.K(?!.*BK)|Dipl\.Kfm(?!.*Kfm)|MA(?!.*MA)|MBA(?!.*MBA)|MSc(?!.*MSc)|MAS(?!.*MAS)|Bakk\. rer\. nat(?!.*nat)|Bakk\. art\. BEd(?!.*BEd)))?(?=\s+(?:von|und|oder)|,|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 18 | 0 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 18 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_9`)


Der Beschuldigte habe dann im Ermittlungsverfahren gegenüber dem Amtsbeauftragten hinsichtlich sieben dieser Firmen den Vorwurf von Scheinrechnungen durch Vorlage von UID-Abfragen, Ausweiskopien und anderer Dokumente, die jeweils vor Zustandekommen der Geschäftsbeziehungen abverlangt worden waren, entkräften können.

**False Positives:**

- `UID-Abfragen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_90`)


Die Bf ist von Beruf Hausfrau, bezieht keine eigenen Einkünfte und  verfügte über ein Haushaltsgeld vom Ehegatten von mtl. rund € 1.200, womit sie die  Lebenshaltungskosten für sich und die beiden Kinder bestritten hat.

**False Positives:**

- `Beruf Hausfrau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_186`)


Parkscheine können durch das Senden von SMS-Nachrichten oder über die Handy Parken  App in Wien gebucht werden.

**False Positives:**

- `SMS-Nachrichten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  Elias von Wnuk-Lipinski, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Wnuk-Lipinski` — partial — pred is substring of gold: `Elias von Wnuk-Lipinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Univ.-Prof.in Ada Forstner`(person)
- `Elias von Wnuk-Lipinski`(person)
- `Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich`(address)
- `Finanzamt`(organisation)
- `FA St. Johann Tamsweg Zell am See`(organisation)
- `26-066/9346`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_119`)


30.4.2003, 99/13/0251)  schließt sich das Bundesfinanzgericht der vom Finanzamt in der Beschwerdevorentscheidung  vertretenen Auffassung bezüglich der Kosten für Literatur, in Bezug auf das Arbeitszimmer  (anteilige Kosten für Strom und Telefon) sowie der sonstigen beantragten Werbungskosten  (Deko, Eimer, DVDs, Kreditkartenetui, Privatanteil von Microsoft Office, Tinten Canon..) an.

**False Positives:**

- `Microsoft Office` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

**False Positives:**

- `Frau Nina Rasem` — partial — gold is substring of pred: `Nina Rasem`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nina Rasem`(person)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `Mag. Peter  Mayerhofer`(person)
- `Magistrates  der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_59`)


Mehrere  Immobiliengutachten wurden vorgelegt (Immobiliengutachten von GmbH XY,  Immobiliengutachten von Dr. Keppert selbst), die höhere Bewertungsansätze aufweisen, als  vom FA angesetzt.

**False Positives:**

- `GmbH XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Keppert`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_23`)


In seinem fristgerecht erhobenen Einspruch brachte der Bf vor, dass das Fahrzeug zur Bean- standungszeit von Herrn LE, Gasse, 2700 Wr. Neustadt, gelenkt worden sei.

**False Positives:**

- `Herrn LE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_12`)


2. Allgemeine Feststellungen zur BP   Die Bp bei Fr. DI DM wurde am 04.12.2012 begonnen, nachdem zuvor eine Bp bei [dem Bf.],  dem Vater von Frau DM, durchgeführt worden war.

**False Positives:**

- `Frau DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI DM`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_35`)


[Der Bf.] liefert dieselbe Ware, die von Frau DM von Deutschland nach Österreich geliefert  wurde wieder weiter nach Deutschland und andere Länder.

**False Positives:**

- `Frau DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_245`)


Im Verlauf der gegenständlichen Außenprüfung sind schließlich neue Tatsachen, wie  insbesondere Betriebsfinanzierung, Zahlungsströme, Warenströme, die enge betriebliche  Verbindung zum Betrieb der Tochter des Abgabepflichtigen, Fr. DI DM, sowie der gemeinsame  Wareneinkauf für beide Betriebe über das Unternehmen von Frau DM und die Warenverkäufe  (Sitz bzw. Wohnsitz der Abnehmer) neu hervorgekommen.

**False Positives:**

- `Frau DM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI DM`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140764.1`) (sent_id: `deanon_BFG_20260814_TEST/140764.1_75`)


Gesellschafter der BF im Jahr 2013 war Herr S.  Die Fa. I wurde von Herrn DO und Herrn KW im Jahr 2001 gegründet.

**False Positives:**

- `Herrn DO` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_55`)


Am 8.7.2008 erhob die Beschwerdeführerin gegen die Bescheide vom 10.6.2008 betreffend  Verfügung des Ablaufes der Aussetzung der Einhebung der Kapitalertragssteuer 1996 und der  Festsetzung von Aussetzungszinsen Berufung und beantragte deren Aussetzung.

**False Positives:**

- `Aussetzungszinsen Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_28`)


Im Zuge des Ermittlungsverfahrens wurde festgestellt, dass der aktuelle Hauptwohnsitz von  Herrn Sohn, geb. am 25.gggg.1981, seit 03.bbb.2013 in Adresse_Sohn, ist.“

**False Positives:**

- `Herrn Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_32`)


Wenn sie möchten kann ich gerne die befunde von kreuzbandriss und Magen  Bypass von Krankenhaus Hollabrunn und von türkischen Krankenhaus ihnen sofort einreichen.

**False Positives:**

- `Krankenhaus Hollabrunn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Groschedl über die  Beschwerde von Frau Theodora Berenwinkel, Klam 26, 8673 Steinhöf, Österreich, vom 12. Februar 2024, gegen die zwei  Straferkenntnisse der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67,  als Abgabenstrafbehörde (beide) vom 30. Jänner 2024, GZen 1) MA67/GZ1/2023 und 2)  MA67/GZ2/2023, beide wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für Wien Nr.  9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 40,00 Euro auf jeweils  30,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten Ersatzfreiheitsstrafen von  jeweils 9 auf jeweils 7 Stunden herabgesetzt werden.

**False Positives:**

- `Frau Theodora Berenwinkel` — partial — gold is substring of pred: `Theodora Berenwinkel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Theodora Berenwinkel`(person)
- `Klam 26, 8673 Steinhöf, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_46`)


Zum Audi:  „Ich lege der Beschwerde den Kaufvertrag vom 23.1.2020, den Zulassungsschein, den  Datenauszug von Porsche Austria, die Ausweiskopie des Käufers aus Ungarn, 9 Fotos des  Fahrzeuges beim Kauf und beim Verladen auf den in Ungarn zugelassenen Anhänger des  Käufers und 2 Fotos des Fahrzeuges im jetzigen Zustand bei.

**False Positives:**

- `Porsche Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/147139.1`) (sent_id: `deanon_BFG_20260814_TEST/147139.1_6`)


In rechtlicher Hinsicht verwies die Beilage auf die BMF-Info über die steuerliche Behandlung  von Krypto-Assets, Stand 1.1.2020.

**False Positives:**

- `Krypto-Assets` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

</details>

---

## `Names after Specific Verbs/Contexts (Beschuldigter/Stellungnahme)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `13cd73d9`  
**Description:**
Matches names following specific legal contexts like 'Beschuldigter an', 'Stellungnahme', or 'gegenst∘ndliche Antragstellerin' which often introduce the person of interest.

**Content:**
```
(?:Beschuldigter an |Stellungnahme |gegenst∘ndliche Antragstellerin \(AS \)|Antragstellerin )([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:[ -][A-Z][a-zA-Z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_51`)


…  ad 5) Verdeckte Ausschüttung:  Stellungnahme Dr. J:  Der Geschäftsführer gibt bekannt, dass die Miet- bzw. Kostenbeiträge von Herrn D und Herr F  im Jahr 2009 und 2010 ausschließlich deswegen erfolgte, da Investitionen vorgenommen  wurden (wie aus dem AVZ 2009 und 2010 zu ersehen ist).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. J`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. J`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_301`)


In den Verfahrensunterlagen  dokumentiert ist die Errichtung einer Stützmauer in Verbindung mit dem Bauvorhaben „neues  Wirtschaftsgebäude“ erstmals im Juli 2009 im Baubewilligungsverfahren betreffend die  oa. Carporterrichtung (Stellungnahme Gestaltungsbeirat Weinland v. 23.7.2009, Bauakt Teil V).

**False Positives:**

- `Gestaltungsbeirat Weinland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_487`)


Bereits im Vorfeld der Bauverhandlung stellte der Bf die Errichtung der Stützmauer mit dem  Hinweis zurück, dass diese erst „im Zusammenhang mit dem zukünftigen Wirtschaftsgebäude“  zu bearbeiten sein werde (Stellungnahme Gestaltungsbeirat Weinland vom 23.Juli 2009,  Bauakt Teil V).

**False Positives:**

- `Gestaltungsbeirat Weinland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (806, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/144968.1`) (sent_id: `deanon_BFG_20260814_TEST/144968.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache **Techn R RgR Jeffrey Geippel**, Dirisam 63, 2813 Pregart, Österreich, über die Beschwerde vom 3. Mai 2022 gegen  den Bescheid des Finanzamtes Österreich vom 2. Mai 2022 betreffend Einkommensteuer 2019  Steuernummer 84-874/5640  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Techn R RgR Jeffrey Geippel` (person)
- predicted in sentence: `RgR Jeffrey Geippel`

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_71`)

**Dr. Maida,** Neurologie- und Psychiatriefachärztin.

- missed: `Dr. Maida,` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_67`)

darüber hinaus habe  er sich bereits nach der Teilnahme am ersten von drei Kursen der „Kurzausbildung mit  **Dr. Gunther Schmidt** – Hypnosystemische Konzepte für Coaching, Team &  Organisationsentwicklung und Supervision“ im Herbst 2018 entschieden, sich im Laufe der Zeit  ein weiteres „Standbein“ aufzubauen, um die erworbenen Kenntnisse als  freiberuflicher/selbständiger Coach anzubieten.

- missed: `Dr. Gunther Schmidt` (person)
- predicted in sentence: `Dr`

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_3`)

Begründung  Am 30. August 2023 erließ das Finanzamt Österreich einen „Bescheid über die Erstattung von  Vorsteuern für 01-12/2022“, der an die Bf. „Prof. Raphael Grieben, z.H. **Hemma Bödker**“ adressiert war.

- missed: `Hemma Bödker` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_423`)

Hinsichtlich der Boni bei den Glücksspielabgaben führte die Bf. ergänzend aus, dass Aufgrund  der von **Oswald Rübberdt**  getrennten Führung eines „Echtgeld-" und eines „Bonuskontos" für den  Zeitraum 01/2012 bis 11/2016 eine klare Abgrenzung vorgenommen werden könne, welchen  Beträgen ein Vermögenswert zukommt und welchen nicht.

- missed: `Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag.Dr. Thomas Leitner** in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Mag.Dr. Thomas Leitner` (person)
- predicted in sentence: `Mag.Dr`, `Janis Dührkopp`

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die vorsitzende Richterin Mag. Aloisia Bergauer und die  beisitzende Richterin Mag. Andrea Ebner sowie die fachkundigen Laienrichter Mag. Johannes  Denk und **Friedrich Nagl** in der Beschwerdesache Dipl. Kfm. Rüdiger Schäffler, Anton-Dengler-Gasse 16, 8330 Krennach, Österreich, vertreten durch  BONAFIDE Treuhand- und Revisionsgesellschaft m.b.H., Berggasse 10, 1090 Wien, über die  Beschwerde vom 17. Oktober 2011 gegen die Bescheide des Finanzamtes Wien 12/13/14  Purkersdorf vom 11. Oktober 2011 betreffend Einkommensteuer für die Jahre 2006 bis 2009  nach Durchführung einer mündlichen Verhandlung beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

- missed: `Friedrich Nagl` (person)
- predicted in sentence: `Mag. Aloisia Bergauer`, `Mag. Andrea Ebner`, `Mag. Johannes  Denk`

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_2`)

in der Verwaltungsstrafsache gegen  Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich, über die Beschwerde vom 8. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. März 2020, Geschäftszahl MA  67/196701206198/2019, uRecht erkannt:    I. **Detlev Griessmer**, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich  wird eine Ermahnung erteilt. Das Straferkenntnis wird aufgeho- ben.

- missed: `Detlev Griessmer` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_28`)

Dagegen richtet sich der Vorlageantrag vom 13.01.2021, der keine weiteren Argumente  enthielt.   II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die **Charles Dormayr** (=Bf.) hatte der X GmbH 2 Kredite gewährt, welche auf den hier  gegenständlichen Liegenschaften EZ BBB sowie EZ CCC der KG XX mit Pfandrechten iHv  insgesamt 340.691,34 Euro sichergestellt wurden.

- missed: `Charles Dormayr` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)

Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des **Prof.in StR DDr.in Reneé Plein**,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

- missed: `Prof.in StR DDr.in Reneé Plein` (person)
- predicted in sentence: `Univ.-Prof.in Daisy Hoopt`, `StR DDr.in Reneé Plein`

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/146641.1`) (sent_id: `deanon_BFG_20260814_TEST/146641.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Lisa Fries in der Beschwerdesache  **Piedro Ringelsbacher, BEd**, Hollehnerweg 53, 2565 Schwarzensee, Österreich, über die Beschwerde vom 30. August 2023 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratsabteilung 6, Referat Parkometerabgabe und  Abgabenstrafen, vom 11. August 2023 betreffend Parkometerabgabe zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Piedro Ringelsbacher, BEd` (person)
- predicted in sentence: `Mag. Lisa Fries`, `Piedro Ringelsbacher`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_3`)

Begründung  Am 30. August 2023 erließ das Finanzamt Österreich einen „Bescheid über die Erstattung von  Vorsteuern für 01-12/2022“, der an die Bf. „**Prof. Raphael Grieben**, z.H. Hemma Bödker“ adressiert war.

- missed: `Prof. Raphael Grieben` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/142700.1`) (sent_id: `deanon_BFG_20260814_TEST/142700.1_2`)

der Beschwerdesache **Claudia Breithut**, Zieregg 36, 2134 Staatz-Kautendorf, Österreich, über die Beschwerde vom 14. September 2022 gegen den Bescheid des Finanzamtes  Österreich vom 8. September 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  für das Jahr 2018, Steuernummer 36-132/1785, zu Recht erkannt:   1.

- missed: `Claudia Breithut` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_156`)

Ich habe auf das Verlangen der Behörde nach  dem Hotelaufenthalt von **Dr. YYY** die von ihm normalerweise gewählten Hotels besucht und um  10 von 28 Seite 11 von 28

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_87`)

Am 12.01.2023 habe sie  eine Mitteilung über den Bezug der Familienbeihilfe für **Heidemarie Fitzenreiter** (also eine Art  „Zusage“) erhalten.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache **Ronja Oberth, LLM**, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Ronja Oberth, LLM` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer LL`, `Ronja Oberth`

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, **Hermann**-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Hermann` (person)
- predicted in sentence: `R.`, `OSR Corbinian Friemuth`, `Mag. Alexander Rimser`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Krafft** in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

- missed: `Dr. Gabriele Krafft` (person)
- predicted in sentence: `Daniel Parys`

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_338`)

**Dr. YYY** ist  außerdem hauptsächlich bei Krankenbesuchen im Buschland unterwegs, also nicht im  eigentlichen Krankenhaus.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_258`)

Zu diesem Zweck wurde, wie aus dem  Erstgutachten hervorkommt, nicht nur eine Vielzahl von bisher vorliegenden Befunden und  Untersuchungsergebnissen mitberücksichtigt, sondern wurde zusätzlich mit zwei der  behandelnden Ärztinnen, nämlich Mag. D (Neuropsychologischer Befund) und OA **Dr. G**  (Neuropädiaterin), ausführlich persönliche Rücksprache zur eingehenden Erhebung ua. der  anamnestischen Daten gehalten.

- missed: `Dr. G` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  **Leopold Pichlbauer** in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

- missed: `Leopold Pichlbauer` (person)
- predicted in sentence: `Mag. Marco Laudacher`, `Mag. Susanne Haim`, `Bettina Domigall`

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/141602.1`) (sent_id: `deanon_BFG_20260814_TEST/141602.1_44`)

Beweiswürdigung:  Aus der aktenkundigen Lenkererhebung ergibt sich, dass die Zulassungsbesitzerin **Olivia Zumbruch**  das gegenständliche Fahrzeug zur Beanstandungszeit (8. März 2023, 16:02 Uhr) gelenkt und in  1010 Wien, Wipplingerstraße 34, abgestellt hat.

- missed: `Olivia Zumbruch` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_1`)

BESCHLUSS  Der Vorsitzende des Finanzstrafsenates Wien 2 des Bundesfinanzgerichtes **Mag. Gerhard  Groschedl** hat in der Finanzstrafsache gegen   1.

- missed: `Mag. Gerhard  Groschedl` (person)
- predicted in sentence: `Bundesfinanzgerichtes Mag`

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) **Siegfried Basyurt**, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

- missed: `Siegfried Basyurt` (person)
- predicted in sentence: `Bf`

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/143262.1`) (sent_id: `deanon_BFG_20260814_TEST/143262.1_2`)

Das Bundesfinanzgericht hat durch den Richter Mag. Alan Sontheimer  in der Angelegenheit der Parteien  **Paul Sohm** (Beschwerdeführer), und Finanzamt Klagenfurt St. Veit Wolfsberg  als Amtspartei über die Säumnisbeschwerde,  datiert vom 16. Feber 2024, eingebracht beim Bundesfinanzgericht am 17. Jänner 2024   betreffend seine Beschwerde vom 14.8.2023 gegen den Bescheid des Finanzamtes vom  13.7.2023 betreffend Festsetzung von Anspruchszinsen 2021 in Höhe von 67,61 €  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Paul Sohm` (person)
- predicted in sentence: `Mag. Alan Sontheimer`

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_10`)

Ebenso legte der Bf. die Heiratsurkunde, sowie eine seine Ehegattin **Katalin** betreffende  Bestätigung (E9) für das Jahr 2018 vor, aus welcher Einkünfte derselben in Höhe von  2.824.116,- HUF vor.

- missed: `Katalin` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_8`)

S. wurde am 23. November 2021 (Nachuntersuchung) von **Dr.in Dok1** untersucht und folgendes  Gutachten erstellt:  Anamnese:  VGA, 08/2016:  kombinierter Entwicklungsrückstand mit Intelligenzminderung – 50%   1 von 16 Seite 2 von 16

- missed: `Dr.in Dok1` (person)
- predicted in sentence: `Dok1`

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/145583.1`) (sent_id: `deanon_BFG_20260814_TEST/145583.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin **Dr. Edith Stefan** in der Verwaltungsstrafsache  Pablo Stroetges, Ostweg 58, 4170 Frindorf, Österreich, über die Beschwerde der Beschuldigten vom 11. August 2024  gegen das Straferkenntnis des Magistrates der Stadt Wien vom 26. Juni 2024, GZ.  MA67/GZ/2024, betreffend Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, den  Beschluss:  I. Das Beschwerdeverfahren wird gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG nicht zulässig.

- missed: `Dr. Edith Stefan` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_22`)

Die Ladungen zur Spruchsenatsverhandlung an den Beschuldigten **Dipl.-Ing. Heinz Riechels**  und den  nebenbeteiligten Verband NB gingen It. Eingangsstempel auf den RSa Schreiben jeweils am  27. Juni 2023 beim Masseverwalter Dr. Pohlhammer ein.

- missed: `Dipl.-Ing. Heinz Riechels` (person)
- predicted in sentence: `Ing. Heinz Riechels`

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_182`)

Ansonsten  werde angesichts der Gleichartigkeit der Sach- und Rechtslage auf die Kurzfassung der  Begründung der Tochter, **DI DM**, „in ihrer parallelen Bescheidbeschwerde“ verwiesen.

- missed: `DI DM` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Dr. Viktoria Blaser** in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

- missed: `Dr. Viktoria Blaser` (person)
- predicted in sentence: `Mag. Sven Weichmann`, `Mag. Kurt Kreith`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_107`)

In Bezug auf den Sohn **OStR Priv.-Doz. Theodor Voelpel**  gilt es sodann auszuführen, dass dieser nach dem Auszug  der Mutter am 08. Jänner 2020 im Haushalt des Beschwerdeführers verblieben ist.

- missed: `OStR Priv.-Doz. Theodor Voelpel` (person)
- predicted in sentence: `OStR Priv`

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_85`)

Im Vorlageantrag erläuterte die Bf wie folgt: Sie habe das Finanzamt mit Schreiben vom  20.09.2022 um Verlängerung der Familienbeihilfe für ihre Tochter **Heidemarie Fitzenreiter**  ersucht.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Dr. Ansgar Unterberger** in der  Beschwerdesache Björn Stover, Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich, vertreten durch ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH, Landungsplatz 5, 4864  Attersee/Attersee, über die Beschwerde vom 14. September 2021 gegen die Bescheide des  Finanzamtes Österreich vom 23. August 2021 betreffend die Festsetzung von  Verspätungszuschlägen für die Monate 12/2020, 01/2021 und 03-05/2021, Steuernummer  57-952/0912, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Dr. Ansgar Unterberger` (person)
- predicted in sentence: `Björn Stover`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_141`)

Dieser hat im Zuge der gleichzeitig stattfindenden GPLA-Prüfung niederschriftlich bekanntgegeben, dass die Firmengründung in Slowenien nur deshalb erfolgte, weil **N.N.** dies so wollte, weil er sich für A., der in Wirklichkeit während des gesamten Prüfungszeitraumes (2012 - 2015) als Dienstnehmer für ihn beschäftigt war, die Lohn- und Sozialabgaben ersparen wollte.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_13`)

Die beschwerdeführende **Olga Kendziora, Bakk. rer. nat.** (Beschwerdeführerin, abgekürzt: Bf.),  Firmenbuchnummer FN 1, hat Frau A als alleinige Geschäftsführerin und Frau C B als alleinige  Gesellschafterin (Firmenbuchauszug: BFG-Akt I zu GZ. RV/7102163/2018, Bl. 107)  2)

- missed: `Olga Kendziora, Bakk. rer. nat.` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Dr. Peter Unger** über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Dr. Peter Unger` (person)
- predicted in sentence: `Susette Volmari`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_16`)

Erst im Nachhinein stellte sich heraus, dass der Insolvenzverwalter  **Dr. Pohlhammer** die übernommene Ladung zur Spruchsenatsverhandlung nicht an den  Beschuldigten ausfolgen konnte, weil dieser die Post nicht abhole.“

- missed: `Dr. Pohlhammer` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_8`)

Die Gesellschaftsanteile werden von Dipl. **Ing.Ing. Bertram Hennlein** und Dipl. Ing. B gehalten.

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: `Ing. Bertram Hennlein`

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer LL`, `Eleonore Sawadzki`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_232`)

Das "Vorliegen  der Störung seit Geburt" laut **Dr. F** aufgrund des Gendefektes ist sohin in obigem Sinne nicht,  wie die Bf vermeint, dem Eintritt bereits einer erheblichen Behinderung gleichzuhalten.

- missed: `Dr. F` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_33`)

Der tatsächliche Sachverhalt stellt sich somit so dar, dass die e GmbH den Auftrag für die  angeführten Arbeiten übernommen hatte, die Arbeiter von der D GmbH zur Verfügung gestellt  wurden (wie dies auch in der Vergangenheit bereits öfters der Fall war), die Bauführung und – aufsicht von der e GmbH (somit von mir) erbracht wurde und die gesamten Leistungen von der  e GmbH an die **Olga Kendziora, Bakk. rer.**

- missed: `Olga Kendziora, Bakk. rer.` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_56`)

Die von Herrn **Ing. Priv.-Doz.in Linda Schleglmilch** zu Punkt 4 und 5 gemachten Angaben stellen für die Betriebsprüfung keine  zu akzeptierenden Argumente dar.

- missed: `Ing. Priv.-Doz.in Linda Schleglmilch` (person)
- predicted in sentence: `Ing`, `Priv.-Doz.in Linda Schleglmilch`

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_319`)

Dies war für den Magistrat nicht überprüfbar, weil ein **Vera Schliephacke** an der  angegebenen Adresse nicht bekannt war.

- missed: `Vera Schliephacke` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_12`)

Mit Anonymverfügung vom 10. März 2022 wurde dem Zulassungsbesitzer des in Rede  stehenden Kraftfahrzeuges, **Pjotr Kristall** (Beschwerdeführer, kurz: Bf) wegen der  Verwaltungsübertretung gemäß § 5 Abs 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs 1  Wiener Parkometergesetz 2006 eine Geldstrafe von € 48,00 vorgeschrieben.

- missed: `Pjotr Kristall` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_381`)

Der Bf. erklärte weiters in mehreren Eingaben, er habe sich beim Hotel Mariott erkundigt, ob **Vera Schliephacke** bei diesem abgestiegen sei, habe jedoch keine Auskunft erhalten.

- missed: `Vera Schliephacke` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Sascha de Kort  in der Beschwerdesache **Matthew McCarthy**,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Matthew McCarthy` (person)
- predicted in sentence: `Univ.-Prof.in Sascha`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_45`)

Dipl. **Ing.Ing. Bertram Hennlein** sei nur selten an den Bürostandorten körperlich anwesend gewesen und habe  daher organisatorisch gar nicht die Durchführung der originären Tätigkeiten eines  Geschäftsführers übernehmen können.

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: `Ing. Bertram Hennlein`

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)

Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der **Engelbert Schefe**  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

- missed: `Engelbert Schefe` (person)
- predicted in sentence: `Dieter Avemaria`

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_66`)

Im Zuge einer vollständigen Offenlegung wurde jedoch auch dieser Betrag, der von unserem  Klienten zur Verfügung gestellt wurde, in der Selbstanzeige dargestellt.  Weiters bietet **Oswald Rübberdt**  seinen Kunden die Möglichkeit, an rund 20 verschiedenen Jackpot  Spielen teilzunehmen.

- missed: `Oswald Rübberdt` (person)
- predicted in sentence: —

</details>

---

