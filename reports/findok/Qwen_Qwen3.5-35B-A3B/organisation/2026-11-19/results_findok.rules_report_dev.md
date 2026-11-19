# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-19T13:15:58.939862

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-11-19/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 200 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 200 |
| Validation documents | 790 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 1567 |
| Validation sentences | 9322 |
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
| Accuracy (exact match) | 97.4% |
| True Positives | 3321 |
| False Positives | 993 |
| False Negatives | 1722 |
| Total Gold Entities | 5043 |
| Micro Precision | 77.0% |
| Micro Recall | 65.9% |
| Micro F1 | 71.0% |
| Macro F1 | 71.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `german_police_admin` | 1.5% | 100.0% | 0.8% | 38 | 38 | 0 |
| `german_courts` | 10.7% | 97.9% | 5.6% | 290 | 284 | 6 |
| `german_specific_orgs` | 4.5% | 92.1% | 2.3% | 126 | 116 | 10 |
| `german_tax_authorities` | 60.6% | 85.1% | 47.1% | 2787 | 2373 | 414 |
| `german_company_ag` | 4.1% | 61.4% | 2.1% | 176 | 108 | 68 |
| `german_company_gmbh` | 13.5% | 44.8% | 8.0% | 897 | 402 | 495 |
| `german_company_e_commerce` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `german_police_admin` 🏆

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `9e06e6f3`  
**Description:**
Matches police and administrative bodies with location suffixes, including genitive forms.

**Content:**
```
\b(Landespolizeidirektion\s+Wien|Magistrat(?:s)?\s+der\s+Stadt\s+Wien(?:\s+Magistratsabteilung\s+\d+)?|Wiener\s+Gemeinderat(?:s)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.015 | 38 | 38 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 38 | 0 | 5005 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_4`)


Weitere zur Beantragung der Familienbeihilfe gemachte Angaben:   Beruf der Antragstellerin: Auszubildender   Dienstgeber: Landespolizeidirektion Wien, [Adresse]  beschäftigt seit: 01.09.2018   Tätigkeit: Auszubildender  vorauss.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_29`)


Der Beschwerde war - wie erwähnt - eine Kopie des von der Landespolizeidirektion Wien mit  der Bf. am 1. September 2018 gemäß § 36 VBG 1948 abgeschlossenen Sondervertrages für die  exekutivdienstliche Ausbildung beigelegt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_63`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die im Jänner 1999 geborene Bf. begann am 1. September 2018 die Polizeigrundausbildung bei  der Landespolizeidirektion Wien im Bildungszentrum T. auf Grund eines mit Sondervertrag  gemäß § 36 VBG 1948 für die exekutivdienstliche Ausbildung begründeten privatrechtlichen  Dienstverhältnisses zum Bund (§ 1 Abs. 1 VBG).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_65`)


Aus diesem Dienstvertrag ist insbesondere ersichtlich:   Organisationseinheit, die für den Bund abschließt, und Dienstbehörde: Landespolizeidirektion  Wien   Befristung: Dieser Dienstvertrag ist auf 24 Monate befristet   Beschäftigungsart: VB des Bundes mit Sondervertrag für die exekutivdienstliche Ausbildung   Entlohnungsschema: …   Besoldungsdienstalter: … Die in diesem Ausbildungsverhältnis zurückgelegte Dienstzeit wird im  Falle der Übernahme in ein öffentlich rechtliches Dienstverhältnis oder im Falle eines  unbefristeten Dienstverhältnisses nach dem VBG 1948 zur Gänze angerechnet.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_33`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien gelegt wurde, und in die  eingeholte Lenkerauskunft auf Grund der Aufforderung zur Bekanntgabe des Fahrzeugienkers  erhoben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_253`)


Beweis wurde erhoben durch Einsichtnahme in die Anzeige vom 04.07.2018 samt Fotos, welche  von einem Organ der Landespolizeidirektion Wien erstattet wurde sowie der Lenkerauskunft  vom 02.02.2019.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31. Juli 2020 an, er habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 2. Juni 2020 in der  gebührenpflichtigen Kurzparkzone in 1030 Wien, Grailichgasse 3, ohne einem für den  Beanstandungszeitpunkt 17:47 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_11`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung gelegt wurde, sowie in die von diesem angefertigten Fotos.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 15. Oktober  1 von 9 Seite 2 von 9

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete der Beschwerdeführerin (in  Folge kurz Bf.) unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der  Parkraumüberwachung der Landespolizeidirektion Wien und nach einer bei der  Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen  Vienna eingeholten Lenkerauskunft mit Strafverfügung vom 16. August 2021 an, sie habe das  Fahrzeug am 26. Mai 2021 in der gebührenpflichtigen Kurzparkzone in 1180 Wien, Ranftlgasse  21 ggü, ohne einen für den Beanstandungszeitpunkt 18:57 Uhr gültigen Parkschein abgestellt,  da die Parkzeit überschritten gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_7`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien mit der  Dienstnummer DNr am 14. Mai 2021 um 10:55 Uhr in 1050 Wien, Reinprechtsdorfer Straße 1c  1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_8`)


Landespolizeidirektion Wien mit Strafverfügung vom 16. September 2021 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna (D) am 19. Juli 2021 um  14:31 Uhr ohne einem für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_13`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt:   „Aus der dem Verfahren zugrundeliegenden Beanstandung, welche von einem Organ der  Landespolizeidirektion Wien mittels Organstrafverfügung vorgenommen wurde, geht hervor,  dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug im Bereich der gebührenpflichtigen  Kurzparkzone abgestellt war, ohne dass die Parkometerabgabe entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_28`)


Bei den Parkraumüberwachungsorganen (Meldungsleger) handelt es sich um Kontrollorgane  der Landespolizeidirektion Wien.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_8`)


Fröbelgasse 39, vom Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion  Wien beanstandet, da nach dessen Wahrnehmungen der im Fahrzeug hinterlegte Parkschein  Spuren von entfernten Entwertungen aufwies.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_34`)


Es bestehe für die erkennende Behörde keinerlei Veranlassung, die schlüssigen und wider- spruchsfreien Angaben des meldungslegenden Organs der Landespolizeidirektion Wien in  Zweifel zu ziehen, zumal einem derartigen Organ die Wahrnehmung und richtige Wiedergabe  maßgeblicher Sachverhalte, insbesondere bezüglich eines im ruhenden Verkehr befindlichen  Kraftfahrzeuges, wohl zugemutet werden könne.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_35`)


Es bestehe kein Grund, an der Objektivität  des meldungslegenden Organs der Landespolizeidirektion Wien zu zweifeln und ergebe sich  kein Anhaltspunkt, dass dieses eine ihm unbekannte Person wahrheitswidrig belasten habe  wollen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_9`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem in Deutschland wohnhaften  Beschwerdeführer (Bf.), unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der  Parkraumüberwachung der Landespolizeidirektion Wien und nach einer bei der Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna (D)  (Fa. XY) eingeholten Lenkerauskunft mit Strafverfügung vom 16. August 2022 an, er habe das  Fahrzeug am 27. Mai 2022 in der gebührenpflichtigen Kurzparkzone in 1020 Wien,  Ausstellungstraße 33, ohne einen für den Beanstandungszeitpunkt 17:50 Uhr gültigen  Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_8`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans Nr der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 30. Dezember 2022 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 2. November 2022  um 09:18 Uhr in der der gebührenpflichtigen Kurzparkzone in 1070 Wien, Bernardgasse 42,  abgestellt, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen  Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/140644.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140644.1_7`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans A204 der Parkraumüberwachung  der Landespolizeidirektion Wien und nach einer bei der Zulassungsbesitzerin des mehrspurigen  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/141222.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141222.1_9`)


Entscheidungsgründe  Dem vom Magistrat der Stadt Wien, Magistratsabteilung 67, als belangter Behörde mit Bericht  vom 26. Mai 2023 dem Bundesfinanzgericht als zuständigem Verwaltungsgericht vorgelegten  Verwaltungsstrafakt ist folgender Verfahrensgang zu entnehmen:  Ein Parkraumüberwachungsorgan der Landespolizeidirektion Wien mit der Nummer ANr stellte  am 19. Jänner 2023 um 12:52 Uhr fest, dass das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) in einer gebührenpflichtigen Kurzparkzone in 1100 Wien,  Liesingbachstraße 73 gegenüber, abgestellt gewesen sei, ohne dass für seine Kennzeichnung  mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt worden sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_4`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug Type mit dem behördlichen Kennzeichen 123 (A) wurde am 28.  Februar 2023 um 12:49 Uhr in der gebührenpflichtigen Kurzparkzone in 1010 Wien,  Liebenberggasse 6, vom Kontrollorgan der Parkraumüberwachung Nr der  Landespolizeidirektion Wien zur Anzeige gebracht, da es sich nach dessen eigenen  1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_8`)


Landespolizeidirektion Wien mit Strafverfügung vom 7. September 2022 an , er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 11. Juli 2022 in einer  gebührenpflichtigen Kurzparkzone in 1210 Wien, Prager Straße 65 u. 67, ohne einen für den  Beanstandungszeitpunkt 11:21 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_11`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  unter Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 12. Juni 2023 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 11. April 2023 in der  gebührenpflichtigen Kurzparkzone in 1130 Wien, Hietzinger Hauptstraße 50, ohne einen für  den Beanstandungszeitpunkt 09:31 Uhr gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/142541.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142541.1_8`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer (Bf.)  nach einer bei der Zulassungsbesitzerin,MittelBruckuniuniEvent GmbH  eingeholten Lenkerauskunft und unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 12. April 2023 an , er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 13. Februar 2023 in  der gebührenpflichtigen Kurzparkzone in Gasse, abgestellt, ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt 12:04 Uhr gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `MittelBruckuniuniEvent GmbH` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/142541.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142541.1_38`)


Begründend stellte die Behörde fest, dass aus der dem Verfahren zugrundeliegenden  Beanstandung, welche von einem Parkraumüberwachungsorgan der Landespolizeidirektion  Wien mittels Organstrafverfügung vorgenommen worden sei, und dem Ermittlungsverfahren  hervorgehe, dass das Fahrzeug in einer gebührenpflichtigen Kurzparkzone gestanden sei, ohne  dass die Parkometerabgabe entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion  Wien` | `Landespolizeidirektion  Wien` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/142576.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142576.1_13`)


Zur Begründung wurde im angefochtenen Erkenntnis ausgeführt, das Fahrzeug sei von einem  Organ der Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung  beanstandet worden, weil es im Bereich einer gebührenpflichtigen Kurzparkzone ohne gültigen  Parkschein abgestellt gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/142576.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142576.1_19`)


Dazu werde Folgendes bemerkt:   Die Anzeigeangaben des anzeigelegenden Organes der Landespolizeidirektion Wien seien klar,  deutlich und frei von Widersprüchen.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_25`)


Begründend führte die Behörde aus, dass aus der dem Verfahren zugrundeliegenden Anzeige,  welche von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund  einer eigenen dienstlichen Wahrnehmung erstattet worden sei, hervorgehe, dass das vom Bf.  2 von 10 Seite 3 von 10

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/143412.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143412.1_8`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna, zugelassen auf die  Fa. ZL, wurde vom Parkraumüberwachungsorgan KO der Landespolizeidirektion Wien am 11.  Mai 2023 um 17:28 Uhr in der gebührenpflichtigen Kurzparkzone in 1060 Wien, Stumpergasse  24, beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_7`)


Entscheidungsgründe  Verfahrensgang:  Verfahren 1) GZ. MA67/Zahl1/2023:   Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (Organ1) am  2. März 2023 um 10:21 Uhr in 1010 Wien, Universitätsring gegenüber 4, zur Anzeige gebracht,  weil ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_58`)


Verfahren 2) GZ. MA67/Zahl2/2023:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (Organ2) am 13.  März 2023 um 12:01 Uhr in 1010 Wien, Universitätsring vor Baum 2156, zur Anzeige gebracht,  weil ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_70`)


Verfahren 3) GZ. MA67/Zahl3/2023:   Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) wurde von einem  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (Organ3) am 20.  Februar 2023 um 15:23 Uhr in 1010 Wien, Universitätsring vor Park, zur Anzeige gebracht, weil  ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_4`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde vom  Kontrollorgan KO der Parkraumüberwachung der Landespolizeidirektion Wien am 6. April 2023  um 16:33 Uhr in der gebührenpflichtigen Kurzparkzone in 1010 Wien, Josef-Meinrad-Platz, bei  Tankstelle rechts beanstandet, da es ohne einen für den Beanstandungszeitpunkt gültigen  Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_8`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67, lastete dem Beschwerdeführer unter  Zugrundelegung der Anzeigedaten des Kontrollorgans DNr der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 14. März 2024 an, er habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 16. Jänner 2024 um  08:59 Uhr in der gebührenpflichtigen Kurzparkzone in 1180 Wien, Währinger Straße gegenüber  81-83, abgestellt, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt  gültigen Parkschein gesorgt zu haben, da der Parkschein nicht entwertet gewesen sei.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/149083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149083.1_5`)


Entscheidungsgründe  Verfahrensgang:  Das Abstellen des Kraftfahrzeuges mit dem behördlichen Kennzeichen Kennz1 (A) wurde von  einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am 23.  Jänner 2025 um 19:50 Uhr in 1140 Wien, Stockhammerngasse gegenüber 19 beanstandet, da  ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/149274.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149274.1_12`)


Das Straferkenntnis wurde wie folgt begründet:  „Aus der dem Verfahren zugrundeliegenden Anzeige, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung erstattet wurde, geht hervor, dass das gegenständliche  mehrspurige Kraftfahrzeug an der im Spruch bezeichneten Örtlichkeit und zur angeführten Zeit  in einer gebührenpflichtigen Kurzparkzone abgestellt war, ohne dass die Parkometerabgabe  entrichtet worden ist.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/149672.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149672.1_23`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer eigenen  dienstlichen Wahrnehmung gelegt wurde, in die von diesem angefertigten Foto.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `german_courts` 🏆

**F1:** 0.107 | **Precision:** 0.979 | **Recall:** 0.056  

**Format:** `regex`  
**Rule ID:** `8abcded5`  
**Description:**
Matches specific German courts and administrative bodies including genitive forms (-s, -es) and specific names.

**Content:**
```
\b(Bundesfinanzgericht(?:s)?|Verwaltungsgerichtshof(?:s)?|Verfassungsgerichtshof(?:s)?|Pensionsversicherungsanstalt(?:s)?|AMS(?:\s+[A-Z])?|Landesgericht(?:s)?|Bezirksgericht\s+[A-Z]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.979 | 0.056 | 0.107 | 290 | 284 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 284 | 6 | 4759 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_39`)


Mit Schreiben vom 30.12.2019 nahm die Beschwerdeführerin bezugnehmend auf einen entsprechenden Vorhalt des Bundesfinanzgerichts unter anderem zu der Frage Stellung, wie hoch der wöchentliche Zeitaufwand der Tochter für die Vorbereitung auf die von ihr wahrgenommenen Prüfungstermine sowie für die Abfassung der sog vorwissenschaftlichen Arbeit im Zeitraum März 2018 bis Jänner 2019 gewesen sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_197`)


2. Auf Basis der zitierten ständigen Rechtsprechung des VwGH bestand bei dem im Beschwerdefall konkret festgestellten Sachverhalt nach Ansicht des Bundesfinanzgerichts aufgrund der im Vorlageantrag dargelegten glaubwürdigen beruflichen Gründe eine Notwendigkeit für die Nutzung eines betrieblich verwendeten Arbeitszimmers.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_15`)


Über die Beschwerde wurde erwogen: Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_30`)


Gegen das abweisende Erkenntnis vom 25.6.2019 des Bundesfinanzgerichts erhob der  rechtsfreundlich vertretene Bf Beschwerde gem. Art 144 B-VG an den Verfassungsgerichtshof.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_31`)


Mit Entscheidung vom 25.2.2020 hob der Verfassungsgerichtshof das Erkenntnis des  Bundesfinanzgerichts vom 25.6.2019 auf (VfGH vom 25.2.2020, E 2892/2019).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_60`)


Bei dem angefochtenen Bescheid vom 12.3.2013 handelt es sich jedoch nach Ansicht des  Bundesfinanzgerichts nicht um einen Aufhebungsbescheid gem. § 299 BAO im Sinne der  Bescheidbezeichnung, sondern um einen antragsgemäßen Aufhebungsbescheid gem. § 295  Abs. 4 BAO.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_64`)


Die Anführung des § 299 BAO in der dem Bescheidspruch vorangestellten Überschrift und in  der "Formularkennzeichnung" kommt keinerlei normativen Wirkung zu und beruht nach  Ansicht des Bundesfinanzgerichts aufgrund des eindeutigen Bescheidinhaltes offenkundig auf  einem Versehen der belangten Behörde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_112`)


Mit Schreiben vom 31.03.2020 beantwortete die Beschwerdeführerin den Vorhalt des  Bundesfinanzgerichts und führte dazu aus wie folgt:   "Die Nebentätigkeit "Erstellung von Werbetexten“ im Zuge meiner Tätigkeit im Bereich  Mediaberatung als Angestellte für das AG Druck und Verlags GmbH umfasste maximal 20  Arbeitsstunden pro Kalenderjahr!

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `AG Druck und Verlags GmbH` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_47`)


In weiterer Folge wurden am 26. Februar 2020 bei einer persönlichen Vorsprache der  Vertreterin der Bf. (laut ihren Angaben die ehemalige Lebensgefährtin des Vaters der Bf.) bei  der zuständigen Richterin des Bundesfinanzgerichts Zeugnisse (Unterlagen) der Bf. überreicht   (Kopien für Akt angefertigt).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_75`)


Wie schon im Erkenntnis des Bundesfinanzgerichts vom 9.1.2018 (welches in der  Beschwerdevorentscheidung vom 22.10.2018 zitiert wurde und den Vater der Bf. betrifft),  festgehalten wurde, ist der Antrag auf Direktzahlung nach § 14 Abs. 1 FLAG 1967 kein  Eigenantrag im Sinne des § 6 Abs. 5 FLAG 1967.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_153`)


Ein Fahrtenbuch muss nach  ständiger Rechtsprechung des VwGH und des Bundesfinanzgerichts fortlaufend und  übersichtlich geführt sein und Datum, Kilometerstrecke, Ausgangs- und Zielort sowie Zweck  jeder einzelnen Fahrt zweifelsfrei und klar angeben (vgl. VwGH 16.9.1970, 0373/70;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_10`)


Als Ergebnis eines unter anderem auf Vorlage der AMS-Karte abzielenden Vorhaltes wurde  eine derartige, – den Zeitraum vom 01.01.2017 bis zum 24.02.2019 umfassende - Karte sowie  eine ebenfalls diesen Zeitraum umfassende mit 11.10.2019 datierte AMS -Bezugsbestätigung  des Inhalts nachgereicht, dass der Bf. vom 01.01.2017 bis zum 24.04.2017; vom 27.04.2017 bis  zum 01.08.2017; vom 07.11.2017 bis zum 15.12.2017; vom 09.01.2018 bis zum 01.07.2018;  vom 15.12.2018 bis zum 31.12.2018 sowie vom 01.01.2019 bis zum 24.02.2019 Notstandshilfe  bezogen hat, bzw. diesem für den Zeitraum vom 25.10.2017 bis zum 06.11.2017 ein Vorschuss  Kündigungsentschädigung zugezählt worden ist.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_14`)


Begründung  Sachverhalt  „Sie sind polnischer Staatsbürger und in Österreich beschäftigt bzw. beziehen AMS Bezüge.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_10`)


Aufgrund der außerordentlichen Revision der GmbH & Co. KG gegen das Erkenntnis des  BFG vom 15.09.2016, Zl. RV/7102261/2011, betreffend u.a. Umsatzsteuer für das Jahr  2009, mit dem die Beschwerde gegen den Umsatzsteuerbescheid 2009 als unbegründet  abgewiesen wurde, erging das Erkenntnis des Verwaltungsgerichtshofs vom 21.02.2018, Ra  2016/13/0052-6, mit dem das angefochtene Erkenntnis im Umfang der Anfechtung  1 von 10 Seite 2 von 10

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_96`)


Nach dem Erkenntnis des Verwaltungsgerichtshofs vom 24.06.2009, 2007/15/0192, mit Bezug  u.a. auf die §§ 12 UStG 1994, 8 Abs.2 KStG 1988 und die Entscheidungen des Europäischen  Gerichtshofs 62003CJ0434 Charles und Charles-Tijmens VORAB;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_115`)


Da eine Rechtsprechung des Verwaltungsgerichtshofs zu der Frage, ob Körperschaften  öffentlichen Rechts für zum Teil hoheitlich genutzte Gebäude eine Vorsteuerberichtigung  vornehmen können, fehlt, ist die Revision zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_70`)


Mit der Fortführung des Beschwerdeverfahrens zu RV/7101586/2012 wurde bis zur Zustellung  der Entscheidung des Verfassungsgerichtshofs innegehalten.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_169`)


IV Streitgegenstand und Rechtstandpunkte der Parteien  Der Streit geht im Kern darüber, ob Österreich Beschäftigungsstaat iSd Art 11 Abs 3 Buchstabe  a) VO 883/2004 ist und damit nach Art 67, 68 VO 883/2004 vorrangig verpflichtet ist sowie –  nach Ansicht des Bundesfinanzgerichts – alternativ darüber, ob § 13 Abs 1 EHG aF für die Bf  einen Anspruch nach rein nationalem Recht, also losgelöst vom Unionsrecht, begründet, was  die Frage aufwirft, ob § 13 Abs 1 EHG aF mittelbar diskriminierend ausgestaltet ist oder  mittelbar diskriminierend ausgelegt wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_395`)


Zur Indexierung der  Familienbeihilfe wird auf das zur EuGH-Zahl C-163/20 protokollierte  Vorabentscheidungsersuchen des Bundesfinanzgerichts hingewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_26`)


Die von der Behörde vertretene Ansicht widerspreche der Entscheidung  des Bundesfinanzgerichts (BFG 16.1.2015, RV/3100406/2013), wonach vom Begriff  „körperliche Wirtschaftsgüter“ auch elektrische Energie umfasst sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_33`)


Nach der in Ritz, BAO6, § 250 Tz 11 zitierten Rechtsprechung des Verwaltungsgerichtshofs soll  der Antrag die Behörde in die Lage versetzen, klar zu erkennen, welche Unrichtigkeit der  Beschwerdeführer dem Bescheid anlastet (vgl. VwGH 21.01.2004, 99/13/0120;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_42`)


Nach BAO6, § 85 Tz. 15 und der dort zitierten Rechtsprechung des Verwaltungsgerichtshofs  VwGH 27.04.1981, 17/2599/79;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_59`)


Der festgestellte Sachverhalt ergibt sich aus den dem Bundesfinanzgericht von der  Abgabenbehörde vorgelegten Unterlagen, der E-Mail vom 03.06.2020 (Beantwortung des  Beschlusses des Bundesfinanzgerichts vom 11.05.2020) und der folgenden Beweiswürdigung:  2. Beweiswürdigung  In seiner Beschwerde vom 01.04.2019 gegen den Einkommensteuerbescheid 2018 vom  26.03.2019 machte der Bf erstmals Ausgaben für Arbeitsmittel in Höhe von 2.025 € als  Werbungskosten geltend.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_66`)


In seiner E-Mail vom 03.06.2020 zur Beantwortung des Beschlusses des Bundesfinanzgerichts  vom 11.05.2020, mit dem der Bf aufgefordert wurde, die berufliche Veranlassung jener  Arbeitsmittel nachzuweisen bzw glaubhaft zu machen, die als Werbungskosten geltend  gemacht, in der Beschwerdevorentscheidung aber nicht berücksichtigt worden seien, führte  der Bf aus, dass die mit den Rechnungen Nr. 4, 14, 17, 18, 19 und 25 erworbenen Arbeitsmittel  ausschließlich im Firmeninteresse, ohne Privatnutzen, erworben worden seien: Bei den  Rechnungen Nr. 4 und 25 handle es sich um Ausgaben für einen mobilen Router für seine USA  Reisen, damit auf einer Firmenbaustelle ein Hotspot mit Internet errichtet werden könne.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_84`)


Bezüglich der Aufforderung des Bundesfinanzgerichts im Beschluss vom 11.05.2020, jene  Ausgaben zu benennen, die laut Vorlageantrag „teilw. falsch bewertet“ worden seien, und  darzulegen, in welcher Höhe diese Ausgaben als Werbungskosten nach Meinung des Bf zu  berücksichtigen seien und dies nachvollziehbar – gegebenenfalls an Hand von Belegen – zu  begründen, führte der Bf in seiner E-Mail vom 03.06.2020 im Wesentlichen aus, dass er „seine  privaten Angelegenheiten größtenteils via mobilem Tablet inkl. separatem mobilem  Internetzugang abwickle, welches wie ein Laptop anzusehen sei, ohne beispielsweise Belege  dafür erbracht zu haben, dass er tatsächlich über ein privates Tablet und einen privaten  Internetzugang verfüge.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_554`)


Beweiswürdigung:   Aufgrund des Verwaltungsakts, insbesondere des Berichts gemäß § 150 BAO, dem  Arbeitsbogen in Verbindung mit der im fortgesetzten Verfahren vorgelegten Kalkulation des  steuerlichen Vertreters, mit der sämtliche Mängel, die in der Parteibeschwerde im  verwaltungsgerichtlichen Verfahren sowie im Erkenntnis des Verwaltungsgerichtshofs vom  22.07.2015, 2012/13/0037 angeführt wurden, in Zahlen berücksichtigt wurden, ist als erwiesen  anzunehmen, dass mit den Verweisen auf die Tz.4 PB bis 6 PB in dem für die Begründung der  Wiederaufnahmebescheide bestimmten Teil des Prüfberichts die Mängel in den  Grundaufzeichnungen UND das Ergebnis der kalkulatorischen Schätzung gemäß § 184 BAO für  die Streitjahre als Wiederaufnahmegründe im Sinn des § 303 BAO Bestandteil der  angefochtenen Wiederaufnahmebescheide sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_597`)


Hinsichtlich der im Erkenntnis des Verwaltungsgerichtshofs, Gz. 2012/13/0037,  angesprochenen Abschnitte ist auf die Ergebnisse der verschiedenen Anstalten zu verweisen,  die Abschnitte von den Fleischproben innerhalb einer Bandbreite von 6% bis 35% belegen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_625`)


Wie aus dem Erkenntnis des Verwaltungsgerichtshofs vom 10.05.1994,  94/14/0024, ersichtlich, ist aber bei der Beurteilung, ob ein in der Ermessensentscheidung  nach § 303 Abs. 4 BAO zu berücksichtigendes Missverhältnis zwischen Bedeutung des  Wiederaufnahmegrundes und den zu erwartenden tatsächlichen Bescheidänderungen vorliegt,  keine Saldierung von Umsatz- und Einkommensteuer schon aus finanzausgleichsrechtlichen  Gründen vorzunehmen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_628`)


2004 03.02.2006:   -6.157,13 € -5.612,51 € 544,62 €  Mehrergebnis   8.720,80 €  Auf die Bemessungsgrundlagen und Höhen der Abgaben für die Streitjahre, welche jenen  Berechnungsblättern zu entnehmen sind, die dem Erkenntnis des Bundesfinanzgerichts,  RV/7104420/2015, angefügt sind, sei verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_633`)


Von der einschlägigen Rechtsprechung des  Verwaltungsgerichtshofs wird mit diesem Erkenntnis des Bundesfinanzgerichts nicht  abgewichen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_666`)


In Hinblick auf das kassatorische Erkenntnis des Verwaltungsgerichtshofs vom VwGH  22.07.2015, 2012/13/0037 war im fortgesetzten Verfahren daher auf das sehr spezifische  Vorbringen vor allem über die Zusammenhänge zwischen den Umsätzen und dem Anfall von  Fleischabfällen in der Betriebsstätte W-Platz einerseits und im nahegelegenen Betrieb der  Tochtergesellschaft andererseits konkret einzugehen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_687`)


Nach der Rechtsprechung des Verwaltungsgerichtshofs zu § 166 BAO heißt beweisen, ein  behördliches Urteil über die Gewissheit des Vorliegens einer entscheidungsrelevanten  Tatsache herbeiführen (VwGH 14.12.1994, 93/16/0191;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_795`)


Wenn die Kalkulation der Betriebsprüfung die Daten der Gegenkalkulation der Bf. über größere  Portionen/einen erhöhten Warenverbrauch wegen Schwund und Personalverbrauch umfasst,  obwohl keine Aufzeichnungen bezüglich Schwund/Personalverbrauch vorgelegt worden sind,  ist es das kassatorische Erkenntnis des Verwaltungsgerichtshofs, welches Gewissheit darüber  50 von 63 Seite 51 von 63

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_823`)


Angesichts des letztzitierten Erkenntnis des Verwaltungsgerichtshofs in Verbindung mit dem  Bericht gemäß § 150 BAO betreffend die Abgaben für die Jahre 2012 bis 2016 war zu den im  Arbeitsbogen abgelegten Beweismittel, die dem Bericht gemäß § 150 BAO betreffend die  Abgaben für die Streitjahre zugrunde gelegen waren, festzustellen, dass dem von der  Betriebsprüfung zitierten Bericht im F-Magazin, erschienen im Compress-Verlag, insoweit  vorrangig Reklamecharakter zuzusprechen war, als das (Ende 2015 eingestellte)  Monatsmagazin in den das Beschwerdeverfahren betreffenden Streitjahren eine Publikation  jenes Compress-Verlages gewesen war, der für die Stadt Wien in den Streitjahren  Auslandsbüros in Europa betrieben hatte.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_875`)


Da das Erkenntnis des Bundesfinanzgerichts der einschlägigen Rechtsprechung des  Verwaltungsgerichtshofs folgt, war somit spruchgemäß zu entscheiden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_905`)


Im gegenständlichen Beschwerdepunkt ist eine Revision unzulässig, weil eine Rechtsfrage von  grundsätzlicher Bedeutung dadurch, dass das Bundesfinanzgericht im fortgesetzten Verfahren  der Entscheidung des Verwaltungsgerichtshofs über die Beschwerde der Bf. gegen die  Abgaben- und Haftungsbescheide für die Jahre 2003 bis 2005 (VwGH 22.07.2015,  2012/13/0037) gefolgt ist, nicht vorliegt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_6`)


In seiner Beschwerde vom 4.9.2019 beantragte der Beschwerdeführer unter Verweis auf zwei  Erkenntnisse des Bundesfinanzgerichts, die Einkommensteuervorauszahlung für 2019 bei  Anwendung des § 124b Z 53 EStG auf die Auszahlung des Todesfallkapitals für ein zu  versteuerndes Einkommen von EUR 41.734,51 in Höhe von EUR 10.800,- festzusetzen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_7`)


Der  Beschwerdeführer erhalte Waisenrenten von der österreichischen  Pensionsversicherungsanstalt, der liechtensteinischen X-Versicherung und von der Y- Pensionskasse in Liechtenstein.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_14`)


Bezüge von der Pensionsversicherungsanstalt von EUR 682,- und eine  Waisenrente in Höhe von CHF 328,25 pro Monat sowie ein anteiliges Todesfallkapital in Höhe  von CHF 48.478,- von der Y-Pensionskasse in Liechtenstein.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_15`)


Dies ergibt sich aus den  vorgelegten Bestätigungen der auszahlenden liechtensteinischen Stellen und aus dem von der  Pensionsversicherungsanstalt übermittelten Lohnzettel.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_29`)


Die Qualifikation der monatlich zufließenden (Waisen-)Renten von der liechtensteinischen X- Versicherung, von der liechtensteinischen Y-Pensionskasse und von der  Pensionsversicherungsanstalt als Einkünfte aus nichtselbständiger Arbeit im Sinn des § 25 Abs.  1 Z 2 lit b EStG 1988 ist zwischen den Parteien unstrittig.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_386`)


Zu den persönlichen und wirtschaftlichen Verhältnissen des Beschuldigten wurde vom  Amtsbeauftragten in der mündlichen Verhandlung hingewiesen, dass der Beschuldigte seit  2015 durchgehend AMS-Bezüge erhält.  Bisher wurde die finanzstrafrechtliche Unbescholtenheit als mildernd gewertet, erschwerend  kein Umstand.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_101`)


Was die Rechtzeitigkeit der  Beschwerdeerhebung anlangt ist einerseits auf den klaren Gesetzestext sowie andererseits  darauf zu verweisen, dass eine in freier richterlicher Beweiswürdigung getroffene Feststellung  des Bundesfinanzgerichts der Kontrolle durch den Verwaltungsgerichtshof grundsätzlich  entzogen ist (vgl. VwGH 1.6.2017, Ra 2017/15/0037);

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_48`)


Die Bf führte ins Treffen, dass die Einschränkung der Energieabgabevergütung auf  Produktionsbetriebe durch das BBG 2011 wegen Verletzung des Bestimmtheitsgebotes des Art.  18 Abs. 1 B-VG als verfassungswidrig erachtet werde, und verwies zudem auf die Ausführungen  des Bundesfinanzgerichts (BFG 3.8.2016, RV/5100360/2013) zur möglichen  Verfassungswidrigkeit der Änderung des EnAbgVergG.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_71`)


Bei der Aufforderung zur Erteilung einer Lenkerauskunft handelt es sich um ein Administrativ- verfahren (vgl. VwGH 23.02.2000, 99/03/0314, ergangen zum vergleichbaren § 103 Abs. 2 KFG  nach ständiger Judikatur des Verwaltungsgerichtshofs (z.B. VwGH 23.02.2000, 99/03/0314).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_122`)


Judikatur des Verwaltungsgerichtshofs (z.B. VwGH 23.02.2000, 99/03/0314) um ein Admini- strativverfahren und somit um eine vom Vorwurf des Grunddeliktes unabhängige (admini- strative) Maßnahme, was bedeute, dass die Lenkeranfrage ein eigenständiges Verfahren bilde.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_118`)


Zur Frage des Bestandes einer Vereinbarung  zwischen der DG und dem Bf., wonach ersterer das in Österreich entstehende Steuerguthaben  zustehe, ist auf die Judikatur zu verweisen, wonach eine in freier Beweiswürdigung getroffene  Feststellung des Bundesfinanzgerichts der Kontrolle durch den Verwaltungsgerichtshof  grundsätzlich nicht zugänglich ist;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_94`)


Diese  Rechtsansicht wird auch in der Rechtsprechung des Bundesfinanzgerichts vertreten (vgl. zB  BFG 14.07.2020, RV/5101090/2018;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_103`)


Seitens des Bundesfinanzgerichts wird die  Verwendung dieses Verkehrsmittels im Hinblick auf eine nur geringfügige Überschreitung einer  Fahrzeit von einer Stunde um 8 Minuten (Abfahrt Ort1 06:26 Uhr und Ankunft in Ort2 07:34  Uhr) auch nicht als unzumutbar erachtet.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_112`)


Diese Rechtsauffassung wird  auf Grundlage des Verordnungstextes des § 2 der Verordnung, BGBl. Nr. 624/1995, seitens des  Bundesfinanzgerichts für den gegenständlichen Fall nicht übernommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_113`)


Hinzuweisen ist auch  darauf, dass in später ergangener Rechtsprechung des Bundesfinanzgerichts als auch nach der  einschlägigen Literatur die Rechtsansicht vertreten wird, dass selbst dann, wenn die Fahrzeit  von einer Stunde nur in einer Richtung überschritten wird, keine Überschreitung des  Einzugsbereiches vorliegen würde, da die Fahrzeit in beiden Richtungen mehr als eine Stunde  betragen muss (vgl. BFG 18.07.2018, RV/7103548/2014;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_339`)


BFH 13.4.2016, III R 14/13  sowie die Entscheidungen des Bundesfinanzgerichts BFG 19.8.2016, RV/7101889/2016  betreffend im Haushalt der Mutter und des Stiefvaters in der Slowakei lebende Kinder;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_343`)


ferner die Entscheidungen des Bundesfinanzgerichts BFG  31.5.2017, RV/5100349/2016;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_130`)


Entscheidung des Bundesfinanzgerichts wegen Rechtswidrigkeit infolge Verletzung von  Verfahrensvorschriften auf und führte u.a. aus, wie er mit Erkenntnis vom heutigen Tag,  Ro 2018/15/0011, zu einem vergleichbaren Revisionsfall ausgesprochen hat, sei zur  Beantwortung der Frage, welcher der beiden Lieferungen die innergemeinschaftliche  Beförderung zuzuordnen ist, insbesondere zu klären, zu welchem Zeitpunkt die zweite  Übertragung der Befähigung, wie ein Eigentümer über den Gegenstand zu verfügen, zugunsten  des Endabnehmers stattgefunden hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_169`)


Die Bf. verwies in diesem  Zusammenhang auch auf zwei inzwischen vom VwGH aufgehobene Erkenntnisse des  Bundesfinanzgerichts (RV/2100470/2018 v. 27.4.2018 und RV/2101122/2016 v. 30.11.2017)  sowie ein in Kraft erwachsenes Erkenntnis (RV/2101353/2014 v. 2.6.2016).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_136`)


Nach einigen Entscheidungen des Unabhängigen Finanzsenats (UFS) bzw. des  Bundesfinanzgerichts (BFG) kommt es für den Werbungskostenabzug neben der beruflichen  Veranlassung auf die Werbewirksamkeit im Rahmen einer politischen oder werbenden  Veranstaltung oder in anderer Form an (UFS 06.08.2007, RV/2132-W/07;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzsenats` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_90`)


Nach der ständigen Judikatur des Verwaltungsgerichtshofs fällt einem Verpflichteten, der nicht  selbst in der Lage ist, für die Einhaltung der Verwaltungsvorschriften zu sorgen, nur dann kein  Verschulden zur Last, wenn er glaubhaft macht, dass er es bei der Auswahl der von ihm  Beauftragten und deren Überwachung nicht an der pflichtgemäßen Sorgfalt hat fehlen lassen  (Erkenntnis des Verwaltungsgerichtshofes vers.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_28`)


In Beantwortung der Schreiben des Bundesfinanzgerichts an die Arbeitgeberin übersandte  diese die gewünschten Unterlagen und nahm zu den an sie gerichteten Fragen wie folgt  Stellung:   In welchem Labor war die Bf. im strittigen Jahr tätig?

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_56`)


Nach den Erkenntnissen des Verwaltungsgerichtshofs vom 2. Juni 2004, 2003/13/0074,  13. September 1977, 2696, 2753, 2754/76, und 10. September 1998, 93/15/0051 kann ein  Steuerpflichtiger, der wegen seiner Körperbehinderung zur Fortbewegung auf einen PKW  angewiesen ist, die anteiligen Kfz-Kosten, die ihm durch die Mehrbenützung seines Kfz  gegenüber gesunden Abgabepflichtigen entstehen, als außergewöhnliche Belastung geltend  machen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_41`)


Mit Erkenntnis des Verwaltungsgerichtshofes vom  26.05.2021, Ra 2019/15/0046, wurde das am 6. Februar 2019 zu GZ. RV/3101071/2017  ausgefertigten Erkenntnis des Bundesfinanzgerichts, soweit es die Körperschaftsteuer betrifft,  wegen Rechtswidrigkeit seines Inhaltes aufgehoben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_48`)


Der Verwaltungsgerichtshof hat das am 6. Februar 2019 zu GZ. RV/3101071/2017  ausgefertigten Erkenntnis des Bundesfinanzgerichts, soweit es die Körperschaftsteuer betrifft,  wegen Rechtswidrigkeit seines Inhaltes mit Erkenntnis VwGH 26.05.2021, Ra 2019/15/0046,  wegen Rechtswidrigkeit seines Inhaltes aufgehoben und begründend Folgendes ausgeführt:  2.1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_67`)


Den Sachverhaltsfeststellungen des Bundesfinanzgerichts ist zu entnehmen, dass die  mitbeteiligte Partei weiters jährlich eine große Anzahl von Grundstücken veräußert, die aus  Erbschaften stammen, welche zuvor professionell eingeworben wurden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_431`)


Finanzamtsvertreter: Das Protokoll ist insofern zu berichtigen, als das Faktum Fa. c auch von  der amtswegigen Ermittlungspflicht des Bundesfinanzgerichts umfasst ist und das  Bundesfinanzgericht die rechtliche Würdigung der Abgabenbehörde zu überprüfen hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_14`)


1997 Wechsel zu Dienstgeberin, Bf. war Verkäuferin  01.12.2009  Mietvertrag über eine Wohnung in Ort CH-1 („Ort CH-1“),  bestehend aus einem Wohn-Schlafraum mit Küche, Bad  und WC  01.11.2011 Mietvertrag betreffend die Wohnung am Ort.CH-1,  bestehend aus Wohnraum und Küche, Schlafzimmer, Bad  und WC   13.05.2011-29.05.2011  und 28.10.2011 -  13.11.2011  AMS-Bezug in Ö  7.5. 2012 bis 29.5.2012,  1.11.2012 bis 8.11.2012  und   10.11.2012 bis 18.11.2012  AMS-Bezug in Ö   Mai 2012 Kauf eines Kfz in Ö, Marke X, und Zulassung dieses Kfz in Ö   9.11.2012 GKK-Bezug in Ö   2 von 24 Seite 3 von 24

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_15`)


14.6.2013 bis 30.6.2013  und  4.11.2013 bis 17.11.2013  AMS-Bezug in Ö  23.6.2014 bis 6.7.2014  1.11.2014 bis 17.11.2014  AMS-Bezug in Ö  01.06.2015 Abmeldung des Hauptwohnsitzes der Bf. in Ö, ab diesem  Tag Nebenwohnsitz (Abfrage ZMR)  01.06.2015 Datum des vorgelegten, unbefristet abgeschlossenen  Arbeitsvertrages als Abteilungsleiterin  Ab 01.06.2015  wird die Wohnsitzdauer aufgrund einer B-Bewilligung in  der CH bis auf Weiteres (gültig bis 31.05.2020) bestätigt.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |
| `AMS` | `AMS` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_22`)


die Bezüge der Gebietskrankenkasse  und des AMS würden für eine Ansässigkeit in Österreich sprechen.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_51`)


Für die kurzen Zeiten habe sie in Österreich lediglich AMS-Geld bezogen,  das Haupteinkommen jedoch in der Schweiz.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_25`)


Zum Beschluss des Bundesfinanzgerichts vom 22.7.2021 wurde mit schriftlicher Stellungnahme  vom 27.7.2021 von der zuständigen Vertreterin des Finanzamtes vorgebracht, dass nach  Durchsicht des Steueraktes betreffend Aufliegen eines Vorlageantrages in Bezug auf die  Beschwerdevorentscheidung vom 24.02.2016 gegen die Bescheide über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012 und 2013 alle vom 09.11.2015 im Akt des Pflichtigen kein  Antrag mit den entsprechenden Daten aufzufinden war.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_11`)


Seine AMS-Bemessung liege bei € 27,65 pro Tag  (€ 857,15 pro Monat) und so komme er mit allen Basiszahlungen wie Miete, Telefon, Strom,  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_31`)


Daraus ergibt sich, dass der Bf. vom AMS eine Notstandshilfe von tgl.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_32`)


€ 27,65 (d.s. rd. € 860,00  monatlich) bezieht (Schreiben des AMS vom 25. Juni 2021).

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_71`)


Seine AMS-Bemessung liege bei € 27,65  täglich (€ 857,15 monatlich) und so komme er mit allen Basiszahlungen wie Miete, Telefon,  Strom, Gas und Rückzahlungen gerade einmal so über die Runden mit Verpflegung.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_76`)


Das Bundesfinanzgericht geht aufgrund folgender Umstände von der Zahlungsunfähigkeit des  Bf. aus:  Dem monatlichen AMS-Bezug von rd. € 860,00 stehen monatliche Belastungen von rund  € 800,00 gegenüber, wobei die Kosten des täglichen Lebens wie beispielsweise Ausgaben für  Lebensmittel, Medikamente, etc. dabei noch nicht berücksichtigt sind.

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_80`)


Eine nähere Definition des Vertreterbegriffs ist der Verordnung BGBL II 382/2001 idgF nicht zu  entnehmen, sodass nach der ständigen Rechtsprechung des Verwaltungsgerichtshofs auf die  Verkehrsauffassung abzustellen ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_9`)


2. Beweiswürdigung  Der Sachverhalt ergibt sich aus dem Verwaltungsakt und dem Akt des Bundesfinanzgerichts  und ist unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_14`)


Durch die Bekanntgabe der Aufhebung der angefochtenen Bescheide lebt die Zuständigkeit  und die Entscheidungspflicht des Bundesfinanzgerichts gemäß § 300 Abs 5 BAO wieder auf.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_10`)


Beweiswürdigung  Der unstrittige Sachverhalt ergibt sich aus dem Akt der Finanzverwaltung und des  Bundesfinanzgerichts.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/135937.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135937.1_11`)


Mit dem Beschluss vom 17.03.2021, Ra 2020/15/0113, wies der Verwaltungsgerichtshof im  zweiten Rechtsgang (siehe zuvor VwGH 19.04.2018, Ra 2017/15/0041) die Revision der Bf.  gegen das Erkenntnis des Bundesfinanzgerichts vom 13.02.2020, RV/1100190/2018, zurück.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_18`)


Mit Beschluss des Bundesfinanzgerichts vom 14. Februar 2022 wurde den Parteien dieser  Aktenstand vorgehalten und um Stellungnahme ersucht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_71`)


Mangels Beschwerde war daher die Unzuständigkeit des Bundesfinanzgerichts mit Beschluss  festzustellen und das Verfahren einzustellen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_40`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Entscheidung des Bundesfinanzgerichts basiert auf folgendem Sachverhalt, der in den  Akten der Abgabenbehörde sowie des Gerichtes abgebildet und soweit nicht gesondert  angeführt unbestritten ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_80`)


Im gegenständlichen Fall geht der Verwaltungsgerichtshof von folgendem Sachverhalt aus:  „Mit dem am 14. Juni 2011 ergangenen Körperschaftsteuerbescheid 2010 wurde - nach den  Feststellungen des Bundesfinanzgerichts (BFG) – die Körperschaftsteuer der  revisionswerbenden GmbH festgesetzt und dabei eine steuerliche Tangente der EDGG Event GmbH&  atypisch Still in Höhe von Null berücksichtigt, woraus sich Einkünfte aus Gewerbebetrieb und ein  Einkommen der revisionswerbenden GmbH für das Jahr 2010 in Höhe von Null ergaben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `EDGG Event GmbH` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_17`)


Weiters könne er die seitens der belangten Behörde vertretene  Rechtsansicht, wonach das Erkenntnis des Bundesfinanzgerichts keine ausreichende  Begründung zur Wiederaufnahme des Verfahrens sei, nicht nachvollziehen, zumal andere  Finanzämter in genau dieser Angelegenheit bereits Rückzahlungen getätigt hätten.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_15`)


Am 21.6.2021 erging das Erkenntnis des  Bundesfinanzgerichts zu GZ RV/3100362/2013.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_86`)


…“  Nach Ansicht des Bundesfinanzgerichts ist dem Bf. nun durchaus zuzugestehen, dass die Canon  Kamera inklusive Zubehör für Werbeaufnahmen bzw. für die vom Bf. angeführte  Internetplattform verwendet wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_87`)


Nach allgemeiner Lebenserfahrung und im Sinne der  Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht des Bundesfinanzgerichts aber  auch davon auszugehen, dass diese Kamera auch der privaten Nutzung diente.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_92`)


Nach Ansicht des Bundesfinanzgerichts ist auch davon auszugehen,  dass im Sinne des o.a. Erkenntnisses des VwGH 27.01.2011, 2010/15/0197, diesbezüglich bzw.  zum Zweck der erforderlichen (kurzfristigen) Buchungsabwicklung eine (nicht bloß  untergeordnete) anteilige Nutzung zur Einkünfteerzielung typischerweise unzweifelhaft  gegeben ist.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_122`)


Nach den  sachverhaltsmäßigen Gegebenheiten (Vermietung einer Ferienwohnung, Wohnsitz des Bf. an  der gleichen Adresse bzw. Wohnsitz der Mutter im unmittelbar gegenüberliegenden  Wohnhaus) ist nach Ansicht des Bundesfinanzgerichts zweifelsfrei von einer gemischt beruflich  und privaten Verwendung auszugehen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_124`)


Nach Ansicht des  Bundesfinanzgerichts ist damit der berufliche Nutzungsanteil mit sehr hoher  Wahrscheinlichkeit nicht unterdeckt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_130`)


Somit waren seitens des Bundesfinanzgerichts in teilweise stattgebender Erledigung der  vorliegenden Beschwerde Aufwendungen für das Tablet in Höhe von 206,10 Euro als  Werbungskosten zu berücksichtigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_58`)


Letztlich  stünden die Gutachten in eklatantem Widerspruch zu den Ergebnissen des Verfahrens vor der  Pensionsversicherungsanstalt, welches zum eindeutigen Ergebnis komme, dass der  Beschwerdeführer dauerhaft invalide sei.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_119`)


Unter Beachtung des oben Ausgeführten ist eine Unschlüssigkeit oder Ergänzungsbedürftigkeit  der ärztlichen Einschätzung nicht zu erkennen und sind die Gutachten und Bescheinigungen,  welche diesbezüglich auch mit den gutachterlichen Einschätzungen im Zusammenhang mit  dem Rehabilitationsgeld (aktenmäßige Beurteilung für die Pensionsversicherungsanstalt vom  4. Oktober 2018 mit Verweis auf ein Gutachten vom 22. August 2017 und die Berichte des  Casemanagers der zuständigen Krankenkasse sowie Bescheid der Pensionsversicherungsanstalt  vom 20. Oktober 2020, nach welchem medizinische Maßnahmen der Rehabilitation erst zu  diesem Zeitpunkt nicht mehr zweckmäßig sind) konform gehen, jedenfalls hinsichtlich des  Umstandes, dass beim Beschwerdeführer eine voraussichtlich dauernde Unfähigkeit sich selbst  den Unterhalt zu verschaffen bereits im Zeitpunkt der Vollendung des 21.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_156`)


Lebensjahres erstellt, befinden sich  im Einklang mit den in einem bei der Pensionsversicherungsanstalt abgeführten Verfahren und  sind daher (nicht nur) hinsichtlich der für dieses Verfahren relevanten Aussage schlüssig und  vollständig.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_11`)


Aus dem weiteren Text dieser  Eingabe ist auch ersichtlich, dass gegen die Entscheidung des Bundesfinanzgerichts vom  7.12.2021 eine Revision eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_97`)


Bestehen mehrere gleichwertige  unionsrechtskonforme Lösungen, hat nach dieser Rechtsprechung der Rechtsanwender nicht  ein freies Wahlrecht, sondern hat nach der Rechtsprechung des Verwaltungsgerichtshofs jene  Lösung zur Anwendung zu bringen, mit welcher materiell am wenigsten in das nationale Recht  eingegriffen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_98`)


Soweit als möglich ist nach der Rechtsprechung des Verwaltungsgerichtshofs  die normative Anordnung des nationalen Gesetzgebers aufrechtzuerhalten (vgl. VwGH  24.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_86`)


Die Rechtsvertretung ist der Feststellung des Bundesfinanzgerichts im Vorhalt, wonach der  Unterhalt (die Kosten der Unterbringung) des Bf. zur Gänze von der Stadt Wien getragen wird,  in der Vorhaltsbeantwortung nicht entgegengetreten.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_99`)


Bestehen mehrere gleichwertige  unionsrechtskonforme Lösungen, hat nach dieser Rechtsprechung der Rechtsanwender nicht  ein freies Wahlrecht, sondern hat nach der Rechtsprechung des Verwaltungsgerichtshofs jene  Lösung zur Anwendung zu bringen, mit welcher materiell am wenigsten in das nationale Recht  eingegriffen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_8`)


Um Vorlage dieser Unterlagen ersucht, wendet der Bf ein, diese seien an den Dienstgeber  übergeben worden, und er habe keinen Zugriff darauf, weil im Rahmen des Konkurses und  eines Strafverfahrens sämtliche Unterlagen des Dienstgebers beim Landesgericht für  Strafsachen, der WKStA oder dem vom Gericht beauftragten Sachverständigen SV1 lagerten.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für  Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für  Strafsachen`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_12`)


Der Hintergrund für die zahlreichen und  wiederholten Eingaben dürfte wird darin zu sehen sein, dass gegen den ehemaligen  Geschäftsführer und nunmehrigen Liquidator der Beschwerdeführerin beim Landesgericht für  Strafsachen ein Strafverfahren wegen Abgabenhinterziehung anhängig, jedoch unterbrochen /  ausgesetzt ist (vgl BFG 20.5.2022, RV/7101916/2020).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für  Strafsachen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für  Strafsachen`(organisation)

</details>

---

## `german_specific_orgs` 🏆

**F1:** 0.045 | **Precision:** 0.921 | **Recall:** 0.023  

**Format:** `regex`  
**Rule ID:** `9bbf5818`  
**Description:**
Matches specific known organizations including ministries, federal offices, and universities.

**Content:**
```
\b(ÖGK|Wirtschaftsuniversität\s+Wien|Bundesministerium\s+für\s+Finanzen|Bundesamt(?:s)?\s+für\s+Soziales\s+und\s+Behindertenwesen|Deutschen\s+Rentenversicherung\s+Bund|Magistrat(?:s)?\s+der\s+Stadt\s+Wien|Wiener\s+Gemeinderat(?:s)?|Bundesministers\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.921 | 0.023 | 0.045 | 126 | 116 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 116 | 10 | 4927 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_114`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt somit  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_17`)


Diese Zeitangabe sei deshalb  glaubwürdig, weil den Kontrollorganen des Magistrats der Stadt Wien als Hilfsmittel für die  Erfüllung der übertragenen Aufgaben elektronische Überwachungsgeräte (sog. PDA's) zur  Verfügung stünden, welche die zum Beanstandungszeitpunkt aktuelle Uhrzeit über einen  Server beziehen und vorgeben.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_37`)


Am 20.08.2020 wurde die im Bundesministerium für Finanzen für die automationsunterstützte  Datenverarbeitung zuständige Sektion I aufgefordert, Fragen im Zusammenhang mit den  konkreten Bescheiderstellungen zu beantworten, sowie diesbezügliche Beweismittel  vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_69`)


Dass die Einbringung  per Telefax erfolgte schadet aufgrund der Verordnung des Bundesministers für Finanzen über  die Zulassung von Telekopierern zur Einreichung von Anbringen an das Bundesministerium für  Finanzen, an die Verwaltungsgerichte sowie an die Finanzämter und Zollämter (BGBl. II  2013/447) nicht.

| Predicted | Gold |
|---|---|
| `Bundesministerium für  Finanzen` | `Bundesministerium für  Finanzen` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_176`)


Hier erweist sich das  Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem Magistrat der Stadt  Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den (anderen) Verwaltungs- gerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele ausführlich BFG  13.05.2014, RV/7500356/2014 sowie Wanke/Unger, BFGG § 25 BFGG Anm. 6).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_5`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_51`)


Informativ wird mitgeteilt, dass die Einzahlung der verhängten Geldstrafe sowie die Kosten des  Verfahrens von der belangten Behörde auf folgendes Bankkonto des Magistrats der Stadt Wien  bei der UniCredit Bank Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 – Strafen;

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank Austria AG` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_54`)


Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_159`)


Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_25`)


Der vom Bundesamt für Soziales und Behindertenwesen festgestellte Grad der  Behinderung beträgt ab März 2014 30%.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_39`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs 3 des Behinderteneinstellungsgesetzes, BGBl Nr 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  3 von 6 Seite 4 von 6

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_45`)


Um dem Bundesamt für Soziales und Behindertenwesen eine zuverlässige Einschätzung des  Grades der Behinderung und den von diesem beauftragten ärztlichen Sachverständigen eine  umfassende Befundaufnahme zu ermöglichen, ist es unerlässlich, zur Untersuchung bei den  ärztlichen Sachverständigen entsprechend aussagekräftige Vorbefunde und Unterlagen über  bereits erfolgte Diagnoseerstellungen durch behandelnde (Fach)Ärzte vorzulegen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_9`)


Die belangte Behörde veranlasste die sachverständige Begutachtung der Bf durch das  Bundesamt für Soziales und Behindertenwesen (im Folgenden BASB).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_171`)


Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_29`)


Zugleich  wurde der Bf darauf hingewiesen, dass Kosten der Behinderung aufgrund einer ausländischen  Bescheinigung nicht berücksichtigt werden könnten, sondern eine Einschätzung der  Behinderung durch das Bundesamt für Soziales und Behindertenwesen erforderlich sei.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_41`)


- In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_4`)


Die Geldstrafe (€ 60,00) ist gemeinsam mit dem Beitrag zu den Kosten der belangten Behörde  (€ 10,00) und des Beschwerdeverfahrens (€ 12,00), insgesamt somit € 82,00, an den Magistrat  der Stadt Wien binnen einer Frist von zwei Wochen ab Zustellung dieses Straferkenntnisses zu  entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_103`)


Informativ wird mitgeteilt, dass die Einzahlung der Geldstrafe (€ 60,00) samt Kosten des  verwaltungsbehördlichen Verfahrens (€ 10,00) und des Beschwerdeverfahrens (€ 12,00) von  gesamt € 82,00 auf folgendes Bankkonto des Magistrats der Stadt Wien bei der UniCredit Bank  Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 - Verkehrsstrafen  IBAN: AT***, BIC: ***  Bitte die Geschäftszahl des Straferkenntnisses des Magistrats angeben: Zahl  Gemäß § 52 Abs. 6 VwGVG sind die §§ 14 und 54b Abs. 1 und 1a VStG sinngemäß anzuwenden.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `UniCredit Bank  Austria AG` (organisation)
- `Magistrats` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  somit 82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat  der Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien` | `Magistrat  der Stadt Wien` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_8`)


Diese Angaben wurden sodann schriftlich mit Eingaben vom 27. November 2018 und  vom 29. Jänner 2019 wiederholt.  Das Finanzamt beauftragte das Bundesamt für Soziales und Behindertenwesen mit der  Erstellung einer Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_19`)


Das Finanzamt übermittelte die Beschwerde neuerlich an das Bundesamt für Soziales und  Behindertenwesen und ersuchte dieses eine neue Bescheinigung zu erstellen, wobei besonders  auf die Prüfung einer etwaigen dauernden Erwerbsunfähigkeit hingewiesen wurde.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_137`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl II Nr 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_123`)


Für die Einschätzung des Grades der Behinderung  sind (für Begutachtungen nach dem Stichtag 1. September 2010) § 14 Abs. 3 des Behinderten- einstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere Be- stimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Heidemarie Winkler im  Beschwerdeverfahren des Siegfried Bentz, Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich, vom 13.02.2022 gegen den  Pfändungsgebührenbescheid des Magistrats der Stadt Wien Magistratssabteilung 6 Erhebungs-  und Vollstreckungsdienst, vom 31.01.2022, mit:  I. Nach Auffassung des Bundesfinanzgerichts ist in Bezug auf die Beschwerde vom 13.02.2022  gegen den Bescheid vom 31.01.2022 mit Beschwerdevorentscheidung abzusprechen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Heidemarie Winkler` (person)
- `Siegfried Bentz` (person)
- `Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich` (address)
- `Bundesfinanzgerichts` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_8`)


Mit 28. August 2020 wurde neuerlich eine Bescheinigung durch das Bundesamt für Soziales  und Behindertenwesen erstellt. Wiederum wurde der Grad der Behinderung ab Feber 2019  bescheinigt.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_13`)


Mit 6. November 2020 erstellte das Bundesamt für Soziales und Behindertenwesen neuerlich  eine Bescheinigung;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_24`)


Zur Feststellung des Grades der Behinderung wurden durch das Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumsservice) folgende auf ärztlichen Gutachten basierende  Bescheinigungen ausgestellt:  Bescheinigung vom 6. Mai 2019 (ärztliches Gutachten vom 5. Mai 2019)  Funktionseinschränkung lt Pos.Nr. 02.02.03, GdB 50% ab 2/2019  Bescheinigung vom 12. März 2020 (ärztliches Gutachten vom 11. März 2020)  Funktionseinschränkung lt Pos.Nr. 02.02.03, GdB 50% ab 2/2019  Bescheinigung vom 28. August 2020 (ärztliches Gutachten vom 28. August 2020)  Funktionseinschränkung lt Pos.Nr. 10.03.14, GdB 60% ab 2/2019  Bescheinigung vom 6. November 2020 (ärztliches Gutachten vom 31. Oktober 2020)  Funktionseinschränkung lt Pos.Nr. 10.03.14, GdB 60% ab 2/2019  In den ärztlichen Gutachten wurden sämtliche von der Beschwerdeführerin vorgelegten  ärztlichen Unterlagen vollständig berücksichtigt und steht auch die Art der Erkrankung  unbestritten fest.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_37`)


Für die Einschätzung des Grades der Behinderung  sind § 14 Abs 3 des Behinderteneinstellungsgesetzes, BGBl Nr 22/1970, in der jeweils  geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl II Nr 261/2010, in der  jeweils geltenden Fassung anzuwenden (§ 8 Abs 5 FLAG 1967).

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_43`)


Wie bereits vom begutachtenden Arzt ausgeführt, ergibt  sich die Höhe des Grades der Behinderung nicht bereits aus der Tatsache, dass eine bestimmte  Erkrankung besteht, sondern aus den Auswirkungen der aus dieser Erkrankung resultierenden  Funktionsbeeinträchtigungen auf die Teilhabe am Leben in der Gesellschaft und im  Erwerbsleben (§ 1 Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung), BGBl II 2010/261 idF BGBl II 2012/151).

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_4`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe (60,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt 82,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrats  der Stadt Wien` | `Magistrats  der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Anna Mechtler-Höger` (person)
- `Jeremias Kierstan` (person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich` (address)
- `Peter Schabel` (person)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Lee Gerstmayer, Wüsterstraße 92, 4972 Stelzham, Österreich, über die Beschwerde vom 13. Oktober 2014  gegen den Bescheid des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener Wasser  vom 12. September 2014 betreffend Wasser- und Abwassergebühr, MA 31-130652/15, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Anna Mechtler-Höger` (person)
- `Lee Gerstmayer` (person)
- `Wüsterstraße 92, 4972 Stelzham, Österreich` (address)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_3`)


Die Kosten des Beschwerdeverfahrens (28,00 Euro) sind gemeinsam mit der Geldstrafe (140,00  Euro) und dem Beitrag zu den Kosten der belangten Behörde (14,00 Euro), insgesamt 182,00  Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der Stadt  Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_22`)


Er wird dem Magistrat der Stadt  Wien nicht vorgelegt, wohl aber dem Verwaltungsgericht Wien im Zuge eines allfälligen Be- schwerdeverfahrens.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Missed by this rule (FN):**

- `Verwaltungsgericht Wien` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_40`)


über diesen Ausweis sind durch Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz zu treffen."

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_179`)


Die belangte Behörde stütze ihre Begründung im Rahmen der Beschwerdevorentscheidung auf  die Ergebnisse der beiden vom Bundesamt für Soziales und Behindertenwesen gemäß § 4 Ein- schätzungsverordnung 2010 eingeholten Sachverständigengutachten, laut derer nur eine  mäßige Einschränkung der sozialen Fähigkeiten und die Möglichkeit der Absolvierung eines  Studiums gegeben sei.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_233`)


jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_45`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung  gestellte Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_70`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des Behindertenein- stellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die Verordnung  des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend nähere  Bestimmungen über die Feststellung des Grades der Behinderung (Einschätzungsverordnung)  vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_104`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/141221.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141221.1_60`)


Über die Beschwerde wurde erwogen:  Feststellungen:  Die Zustellung der mit 20. Dezember 2022 datierten Strafverfügung wurde vom Magistrat der  Stadt Wien, MA 67, am 20. Dezember 2022 gemäß § 26 Zustellgesetz veranlasst.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_68`)


Unzumutbarkeit der Benützung öffentlicher Verkehrsmittel wegen dauerhafter  Mobilitätseinschränkung aufgrund einer Behinderung verfügen, als Nachweis über die  Berechtigungen nach Abs. 2 bis 4 auf Antrag vom Bundesamt für Soziales und  Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_69`)


Die näheren Bestimmungen über diesen Ausweis  sind durch Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz zu  treffen.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_126`)


Hier erweist sich das  Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem Magistrat der Stadt  Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den (anderen) Verwaltungs- gerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele ausführlich BFG  13.5.2014, RV/7500356/2014 sowie Wanke/Unger, BFGG § 25 BFGG Anm. 6).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_152`)


Für die Einschätzung des Grades der Behinderung sind § 14 Abs. 3 des  Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der jeweils geltenden Fassung, und die  Verordnung des Bundesministers für Arbeit, Soziales und Konsumentenschutz betreffend  nähere Bestimmungen über die Feststellung des Grades der Behinderung  (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der jeweils  geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und Konsumentenschutz` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_154`)


Nach § 8 Abs. 6 FLAG 1967 idgF ist der Grad der Behinderung oder die voraussichtlich  dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales  und Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales  und Behindertenwesen` | `Bundesamt für Soziales  und Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_165`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 zur Berufsausübung berechtigter Ärzte, die in  die bei dieser Behörde zu führende Sachverständigenliste eingetragen sind, als  Amtssachverständige bedient.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_126`)


Hier erweist sich das  Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem Magistrat der Stadt  Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den (anderen) Verwaltungs- gerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt  Wien` | `Magistrat der Stadt  Wien` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_75`)


§ 29b Abs. 1 StVO 1960 normiert:   "Inhabern und Inhaberinnen eines Behindertenpasses nach dem Bundesbehindertengesetz,  BGBl. Nr. 283/1990, die über die Zusatzeintragung "Unzumutbarkeit der Benützung öffentlicher  Verkehrsmittel wegen dauerhafter Mobilitätseinschränkung aufgrund einer Behinderung"  verfügen, ist als Nachweis über die Berechtigungen nach Abs. 2 bis 4 auf Antrag vom  Bundesamt für Soziales und Behindertenwesen ein Ausweis auszufolgen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_76`)


Die näheren  Bestimmungen über diesen Ausweis sind durch Verordnung des Bundesministers für Arbeit,  Soziales und Konsumentenschutz zu treffen."

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` | `Bundesministers für Arbeit,  Soziales und Konsumentenschutz` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_17`)


Mit Vorlagebericht vom 30.11.2022 legte das FA die gegenständliche Beschwerde samt einer  ausführlichen Begründung und Unterlagen wie z.B. dem E-Mail Schriftverkehr zwischen dem  ÖGK Prüfer und der zuständigen Mitarbeiterin des FA vor.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/144197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lukas Escherle  in der Verwaltungsstrafsache gegen  Kirsten Schneppensiefen, Poppenreithstraße 26, 7461 Goberling, Österreich, vertreten durch Albert Höferlin  wegen der  Verwaltungsübertretung gemäß § 16 Abs 1 des Gebrauchsabgabegesetz, über die Beschwerde  der Beschuldigten vom 31.7.2023 gegen das Straferkenntnis des Magistrats der Stadt Wien  vom 14.7.2023 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe auf je € 20,00 (also EUR 100,00) herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Magistrats der Stadt Wien` | `Magistrats der Stadt Wien` |

**Missed by this rule (FN):**

- `Priv.-Doz. Lukas Escherle` (person)
- `Kirsten Schneppensiefen` (person)
- `Poppenreithstraße 26, 7461 Goberling, Österreich` (address)
- `Albert Höferlin` (person)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_47`)


Eine der Angabe der Bf. im Zuge des Vorlageantrages entsprechende  Bestätigung für die angestrebte neuerliche Untersuchung am Bundesamt für Soziales und  Behindertenwesen - Sozialministeriumservice und den diesbezüglichen Termin am 30.04.2017  sei trotz Aufforderung nicht vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_48`)


Da seitens des Bundesamts für Soziales und  Behindertenwesen - Sozialministeriumservice eine rückwirkende Bestätigung einer  Behinderung nicht durchgeführt werde und auch aktuell aufgrund eines Augenleidens keine  Behinderung festgestellt worden sei, würden die in diesem Zusammenhang geltend gemachten  Aufwendungen Krankheitskosten gemäß § 34 EStG 1988 mit Selbstbehalt darstellen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_49`)


Mit Schreiben des BFG vom 17.07.2017 wurde die Bf. bezüglich ihres Augenleidens als Folge  der Nichtvorlage der im Vorlageantrag angesprochenen Bescheinigung des Bundesamts für  Soziales und Behindertenwesen - Sozialministeriumservice im Sinn des § 35 EStG 1988 ersucht,  sämtliche Beweismittel zwecks Veranlassung einer Anfrage an das Bundesamt für Soziales und  Behindertenwesen betreffend „Rückwirkung des Grads der Behinderung“ an das BFG zu  übermitteln.

| Predicted | Gold |
|---|---|
| `Bundesamts für  Soziales und Behindertenwesen` | `Bundesamts für  Soziales und Behindertenwesen` |
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_50`)


In Entsprechung dieses Ersuchens wurden diverse Berichte und Befunde als  Beilage zum Schreiben der Bf. vom 10.10.2017 an das BFG zugesandt, die in weiterer Folge  dem an das Bundesamt für Soziales und Behindertenwesen - Sozialministeriumservice  adressierten Schreiben des BFG vom 27.10.2017 mit dem Ersuchen um u.a. a) Aufgliederung  des u.a. Gesamtgrades der Behinderung samt Begründung und b) Angabe des Prozentsatzes  der Sehstörung in den Streitjahren beigelegt wurden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_55`)


Infolge Fehlens von  Augenbefunden für den Zeitraum von Juni 2012 bis Oktober 2014 hat das Bundesamt für  Soziales und Behindertenwesen - Sozialministeriumservice (früher Bundessozialamt) den Grad  der Augenbehinderung bei der Bf. von 20% mit ausreichender Wahrscheinlichkeit für den  Zeitraum Jänner bis Oktober 2014 aufgrund des Sehvermögens rechts mit 0,3 und links mit 0,7  - wie im Befund von Juni 2012 angeführt - angenommen.

| Predicted | Gold |
|---|---|
| `Bundesamt für  Soziales und Behindertenwesen` | `Bundesamt für  Soziales und Behindertenwesen` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_56`)


Der Grad der Behinderung für den  nach der Laseroperation gelegenen Zeitraum der Monate November und Dezember jeweils des  Jahres 2014 ist vom Bundesamt für Soziales und Behindertenwesen - Sozialministeriumservice  mit 10% eingeschätzt worden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_91`)


Zuständige Stelle ist das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_125`)


Eine Bestätigung für die im  Vorlageantrag thematisierte neuerliche Untersuchung beim Bundesamt für Soziales und  Behindertenwesen - Sozialministeriumservice (früher Bundessozialamt) am 30.04.2017 mit  dem Ergebnis der Erfüllung der medizinischen Voraussetzungen für die Vornahme der  Zusatzeintragung „Die Untersuchte ist sehbehindert“ mit Rückwirkung auf das Jahr 2014 wurde  trotz Vorhalts in der abgabenbehördlichen Stellungnahme zum Vorlageantrag nicht  nachgereicht.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_126`)


Angesichts der Tatsache, dass das Bundesamt für Soziales und Behindertenwesen -  Sozialministeriumservice (früher Bundessozialamt) eine Bestätigung für die Bf. hinsichtlich  einer Sehbehinderung mit Rückwirkung für das Jahr 2014, die den Grad der Behinderung von  25% im Zeitraum vor und nach der Laseroperation unterschritten hatte, ausgestellt hatte, war  davon auszugehen, dass die medizinischen Voraussetzungen für die Vornahme der  Zusatzeintragung „Die Untersuchte ist sehbehindert“ im Behindertenausweis der Bf. aufgrund  der funktionellen Einschränkungen der Bf. im Jahr 2014 nicht gegeben waren.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_131`)


Aufgrund der Abhängigkeit der Antwort auf die Frage, ob die Voraussetzungen für die  Anerkennung der in Rede stehenden Kosten der Bf. als außergewöhnliche Belastung gemäß  § 34 Abs. 6 EStG 1988 in Verbindung mit § 35 Abs. 5 EStG 1988 im Streitjahr 2014 gegeben  waren, von Eintragungen im Behindertenausweis der Bf. und dem Ergebnis von Gutachten des  Bundesamt für Soziales und Behindertenwesen - Sozialministeriumservice war das Vorliegen  einer Rechtsfrage von grundsätzlicher Bedeutung im Sinne des Artikel 133 Abs. 4 B-VG zu  verneinen und spruchgemäß zu entscheiden.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_3`)


Die Kosten des Beschwerdeverfahrens (12,00 Euro) sind gemeinsam mit der Geldstrafe  (60,00 Euro) und dem Beitrag zu den Kosten der belangten Behörde (10,00 Euro), insgesamt  82,00 Euro, binnen zwei Wochen nach Zustellung dieses Erkenntnisses an den Magistrat der  Stadt Wien zu entrichten.

| Predicted | Gold |
|---|---|
| `Magistrat der  Stadt Wien` | `Magistrat der  Stadt Wien` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_180`)


Da die Supplementierung bei seiner Ehegattin medizinisch indiziert sei, und trotz des Urteils  des OGH vom 08.11.2011, 10 ob S70/11h (Anm.: es geht um SV-rechtliche Vorschriften) die  ÖGK keinen den Bedürfnissen entsprechenden Leistungskatalog habe und die Ehegattin keine  titanoxidfreien Rezeptierungen erhalte, seien die Präparate als ag Bel anzuerkennen.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_85`)


Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_369`)


Für nachfolgende Aufwendungen fehlt es nach dem vorliegenden Ermittlungsergebnis an den  Voraussetzungen für einen Abzug als außergewöhnliche Belastung:   2018:  Behandlungs-/Therapiekosten, Medikamentenaufwand:  - 49,- € Dr-A (lt. Bf 17.2.2018): trotz FA-Anforderung vom 27.Aug.2020 kein Nachweis durch  Rechnung, Zahlungsbeleg oder ÖGK-Kostenersatz;  - 395,- € Dr-B (Zahlung 24.7.2018): trotz FA-Anforderung am 27.Aug.2020 kein Nachweis durch  Rechnung oder ÖGK-Kostenersatz ;  - 190,- € MRT Privatklinik-X (Zahlung 12.3.2018): trotz FA-Anforderung vom 27.Aug.2020 weder  Nachweis durch Rechnung/ ÖGK-Kostenersatz noch über die medizinische Notwendigkeit der  umgehenden Durchführung in einer Privateinrichtung;

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_373`)


kein  ÖGK-Kostenersatz oder sonstiger Nachweis der medizinischen Notwendigkeit iSd  VwGH-Judikatur;   - 742,- € M. M. für Physiotherapie/Heilmassage/osteopath.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Missed by this rule (FN):**

- `M.` (person)
- `M.` (person)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_374`)


Behandlung (lt. Bf Zahlung  8.Febr.2018): trotz FA-Anforderung am 27.Aug.2020 kein Nachweis durch Rechnung, Zahlung  oder ÖGK-Kostenersatz.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_375`)


Bei zwei Rechnungen des Physiotherapeuten aus 2018 ÖGK-Teilersatz (jeweils Ersatz für  Kosten der Physiotherapie/Heilmassage v. 201,60 €, nicht aber f. 546,40 € osteopath.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_386`)


Aus den zuvor dargestellten nicht abzugsfähigen „Krankheitskosten“ resultieren  Fahrtkostenkürzungen für nachfolgende Wegstrecken (Entfernungen lt. Bf-Aufstellungen):  - Dr-B: 128,8 km;  - ABC/Ort-10: 218,4 km;  - Ort-11/Krankenhaus an Bürotagen: 147 km (5x 29,4 km Wohnsitz/Arbeitsstätte);  - Ort-5/Privatklinik-X : 54,2 km;   - Ort-5/Physiotherapie (ÖGK-Ersatz 22.11.: 147 km/ 6x 29,4 km Wohnsitz/Arbeitsstätte);

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_387`)


(ÖGK-Ersatz 16.8.: keine betroffenen Bürotage/ keine Kürzung);

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_392`)


Des Weiteren ist die Zulässigkeit eines Abzuges als außergewöhnliche Belastung für die vom  ÖGK-Ersatz nicht umfassten 58 Fahrten zum Physiotherapeuten in Ort-5 mangels Nachweises  der medizinischen Notwendigkeit der vom Therapeuten bestätigten  „Elektrostimulationstherapie“ nicht erwiesen (Bf-Eing.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_402`)


Dazu kommen 19,66 € (anteilige Kosten Dr-D für  2019 lt. ÖGK-Ersatz 9.3.2020), insgesamt somit 974,25 €.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_406`)


Der zweite Wert enthält neben Fahrten zum Hausarzt bzw. zu zwei Ärzten,  zu deren Behandlungskosten dem Bf von der ÖGK eine Teilkostenerstattung gewährt wurde,  auch 232,8 km betreffend Fahrten, für deren Zweck der Bf trotz FA-Aufforderung zur  vollständigen Belegvorlage vom 20.Aug.2020 keinerlei Belege übermittelt hatte   (23.5. Dr-E/Ort-2, 29.10.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_408`)


Unter den Fahrten zum Physiotherapeuten waren auch fünf Fahrten erfasst, die im  Zusammenhang mit einer Teilkostenerstattung der ÖGK standen (6. - 28.Febr 2019, jeweils an  „Bürotagen“, mit Fahrtkostenberechnung ab Arbeitsstätte).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_410`)


Soweit die Behandlungen des Physiotherapeuten nicht zu Teilkostenerstattungen der ÖGK  führten (5.092,2 km), folgt das BFG auch für 2019 seiner Beurteilung zum Jahr 2018.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_118`)


– In allen übrigen Fällen sowie bei Zusammentreffen von Behinderungen verschiedener Art das  Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/145852.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145852.1_79`)


Das Bundesministerium für Finanzen ist ermächtigt, von der  Anwendung dieser Bestimmung bei Personen abzusehen, deren Aufenthalt im Inland nicht mehr  als ein Jahr beträgt, wenn diese im Inland weder ein Gewerbe betreiben noch einen anderen  Beruf ausüben.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_54`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung) vom 18. August 2010, BGBl. II Nr. 261/2010, in der  jeweils geltenden Fassung anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_65`)


Lebensjahres auf der Grundlage des nach Vorlage der Beschwerde an das Bundesfinanzgericht  erstellten Sachverständigengutachtens vom 17.09.2024 durch das Bundesamt für Soziales und  Behindertenwesen bescheinigt.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/146104.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146104.1_36`)


Die  beiden dahinterstehenden Vereine agieren über die BF als Verrechnungsstelle für  Vertragstherapeuten und die ÖGK, wobei sich die Vertragstherapeuten gegenüber der BF in  Einzelvereinbarungen zur Erbringung psychotherapeutischer Leistungen an Versicherte der  ÖGK verpflichten.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_321`)


Die Absätze 1 bis 6 des § 3 der Verordnung des Bundesministers für Finanzen über die Kriterien  zur Ermittlung des Pendlerpauschales und des Pendlereuros, zur Einrichtung eines  Pendlerrechners und zum Vorliegen eines Familienwohnsitzes (Pendlerverordnung), BGBl. II  Nr. 276/2013 in der Fassung BGBl. II Nr. 154/2014 und Nr. 324/2019, bestimmen:  „(1) Für die Ermittlung der Entfernung zwischen Wohnung und Arbeitsstätte bzw. zwischen  Arbeitsstätte und Wohnung (§ 1) und für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist (§ 2), ist für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  21 von 28 Seite 22 von 28

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_114`)


Für die Einschätzung des Grades der  Behinderung sind § 14 Abs. 3 des Behinderteneinstellungsgesetzes, BGBl. Nr. 22/1970, in der  jeweils geltenden Fassung, und die Verordnung des Bundesministers für Arbeit, Soziales und  Konsumentenschutz betreffend nähere Bestimmungen über die Feststellung des Grades der  Behinderung (Einschätzungsverordnung/EVO) vom 18. August 2010, BGBl. II Nr. 261/2010, in  der jeweils geltenden Fassung, anzuwenden.

| Predicted | Gold |
|---|---|
| `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` | `Bundesministers für Arbeit, Soziales und  Konsumentenschutz` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_116`)


Nach § 8 Abs. 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, vom Bundesamt für Soziales und  Behindertenwesen (Sozialministeriumservice) dem Finanzamt Österreich durch eine  Bescheinigung auf Grund eines ärztlichen Sachverständigengutachtens nachzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_140`)


Es ist nicht rechtswidrig, wenn das Bundesamt für Soziales und Behindertenwesen sich bei der  Erstattung von Bescheinigungen gem. § 8 Abs. 6 FLAG zur Berufsausübung berechtigter Ärzte  10 von 15 Seite 11 von 15

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_25`)


Die belangte  Behörde bestätigte, dass es einen Button für Vorlageanträge gibt, dieser aber vom Bf nicht  gedrückt wurde, weil er den Einzeiler unter dem Button „Beschwerde“ nochmals eingegeben  hatte, führte aber auch aus, dass die belangte Behörde auf den FinanzOnline Verlauf im Detail  nicht zugreifen könne und bot an, zu diesem Zweck, mit dem Bundesministerium für Finanzen  diesbezüglich Kontakt aufzunehmen, um die Daten aus FinanzOnline für den gegenständlichen  Akt auswerten zu lassen.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_28`)


Die belangte Behörde hätte nach  Auswertung durch das Bundesministerium für Finanzen festgestellt, dass die Beschwerde vom  27. Jänner 2024 sich gegen den Zurückweisungsbescheid vom 25. Jänner 2024 gerichtet hätte  und somit nicht als Vorlageantrag zu werten sei.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/146573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146573.1_36`)


Grenzgänger haben zwei Möglichkeiten sich in Österreich zu versichern:  Selbstversicherung bei der Österreichischen Gesundheitskasse (ÖGK).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_273`)


Auch das Bundesministerium für Finanzen ging ursprünglich davon aus, dass die angeführte  Bestimmung des Einkommensteuergesetzes sich ausschließlich auf inländische Privatstiftungen  bezog.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_426`)


[...]  Die Bestätigung der Gesellschaft, in deren Werkstatt sich das Fahrzeug, für welches eine  Ausnahmebewilligung erteilt wurde, zu den Tatzeitpunkten befand, wurde dem Magistrat der  Stadt Wien, Magistratsabteilung 67, zur Kenntnis gebracht.

**False Positives:**

- `Magistrat der  Stadt Wien` — partial — pred is substring of gold: `Magistrat der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_27`)


Mit Straferkenntnis des Magistrats der Stadt Wien, MA 67, vom 20. Jänner 2021, wurde der Bf.  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig befunden und  wegen Verletzung der Rechtsvorschriften des § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz  2006 eine Geldstrafe iHv € 60,00 und für den Fall der Uneinbringlichkeit eine Ersatzfreiheits- strafe von 14 Stunden verhängt.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien, MA 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, MA 67`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)
- `Aron Pommeränke`(person)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_75`)


Der Bf. wurde mit dem gegenständlichen Auskunftsverlangen - Schreiben des Magistrats der  Stadt Wien, Magistratsabteilung 67, vom 10. Jänner 2022 - als jene Person, der das ihr von der  Zulassungsbesitzerin zur Verfügung gestellte Kraftfahrzeug mit dem behördlichen Kennzeichen  123 (D) einem Dritten überlassen hat, aufgefordert Auskunft darüber zu erteilen, wem er das  genannte Kraftfahrzeug am 15. September 2021 um 19:20 Uhr überlassen gehabt habe, sodass  es zu diesem Zeitpunkt in 1020 Wien, Schiffamtsgasse 16 abgestellt gewesen sei.

**False Positives:**

- `Magistrats der  Stadt Wien` — partial — pred is substring of gold: `Magistrats der  Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/140698.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140698.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rafaela Heinss, Severgraben 12, 4343 Hütting, Österreich, über die Beschwerde vom 24. März 2016 gegen  die Bescheide des Magistrats der Stadt Wien, Magistratsabteilung 6, Rechnungs- und  Abgabenwesen, vom 09. Februar 2016 betreffend Kommunalsteuer für die Jahre 2010 bis  2012, hat nach Durchführung einer mündlichen Verhandlung am 26.04.2023 in Anwesenheit  der Schriftführerin FOIin SF zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Anna Mechtler-Höger`(person)
- `Rafaela Heinss`(person)
- `Severgraben 12, 4343 Hütting, Österreich`(address)
- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_22`)


Mit dem nunmehr angefochtenen Zurückweisungsbescheid des Magistrats der Stadt Wien,  Magistratsabteilung 67, vom 22. März 2023 wurde der Einspruch des Beschwerdeführers vom  16. Februar 2023 gegen die Strafverfügung vom 12. Jänner 2023 gemäß § 49 Abs. 1  Verwaltungsstrafgesetz (VStG) wegen Verspätung zurückgewiesen.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_44`)


Mit dem nunmehr angefochtenen Bescheid des Magistrats der Stadt Wien,  Magistratsabteilung 67, vom 22. März 2023 wurde der Einspruch des Beschwerdeführers vom  16. Februar 2023 gegen die Strafverfügung vom 12. Jänner 2023 gemäß § 49 Abs. 1  Verwaltungsstrafgesetz (VStG) wegen Verspätung zurückgewiesen.

**False Positives:**

- `Magistrats der Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien,  Magistratsabteilung 67`(organisation)

</details>

---

## `german_tax_authorities` 🏆

**F1:** 0.606 | **Precision:** 0.851 | **Recall:** 0.471  

**Format:** `regex`  
**Rule ID:** `e6a387e2`  
**Description:**
Matches Finanzamt variations including genitive endings, specific locations, and 'für' constructions.

**Content:**
```
\b(Finanzamt(?:es)?(?:\s+(?:Wien\s+3/6/7/11/15\s+Schwechat\s+Gerasdorf|Österreich|Baden\s+Mödling|Linz|Bruck\s+Eisenstadt\s+Oberwart|Großbetriebe|für\s+Gebühren|Innsbruck))?|Zollamt(?:es)?(?:\s+Klagenfurt)?|Finanzpolizei)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.851 | 0.471 | 0.606 | 2787 | 2373 | 414 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2373 | 414 | 2670 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Missed by this rule (FN):**

- `Mag.Dr. Hedwig Bavenek-Weber` (person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_2`)


Entscheidungsgründe 1. Sachverhalt Mit Schreiben vom 15. Juli 2014 teilte der Bf. dem Finanzamt mit „Änderung Bewirtschaftung KG  URKJ Forschung KG , EZ x1, Grundstücke xx1 und xx2“ mit, dass der Weingarten Grundstück xx1 komplett gerodet worden sei und jetzt brachliege.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `URKJ Forschung KG` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_8`)


Name, Adresse und Geburtsdatum des Bf. Am 23. Juli 2014 erließ das Finanzamt einen Bescheid mit folgendem Inhalt: „Bescheid: Der Antrag von …. Bf. …. vom 15.7.2014, eingebracht am 22.7.2014 betreffend den Antrag auf Wertfortschreibung wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_14`)


“ Am 2. August 2014 langte beim Finanzamt ein Schreiben mit folgendem Inhalt ein: „Beschwerde gegen Bescheid vom 23.7.14 EZ x1  , Grundstücke xx1 u. xx2“….Ich bringe gegen den im Betreff angeführten Bescheid Beschwerde ein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_18`)


Mit „Bescheid – Mängelbehebungsauftrag“ vom 29. August 2014  stellte das Finanzamt fest, dass die Eingabe des Bf. vom 2.8.2014 hinsichtlich der Form (§ 85 Abs. 2 BAO) folgende Mängel aufweise: Gemäß § 250 Abs. 1 BAO hat eine Bescheidbeschwerde folgende Punkte zu enthalten: 1. die Erklärung, in welchen Punkten der Bescheid angefochten wird, 2. die Erklärung, welche Änderungen beantragt werden;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_21`)


Mit dem Formular „Bescheid – Zurücknahme/Gegenstandsloserklärung“ vom 8. Oktober 2014   entschied das Finanzamt, dass die Beschwerde des Bf. vom 2. August 2014 betreffend Bescheid vom 23. Juli 2014 gemäß § 85 Abs. 2 BAO als zurückgenommen gilt. Als Begründung gab es an, dass der Bf. dem Auftrag, die Mängel der Beschwerde bis 29. September 2014 zu beheben, nicht entsprochen habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_22`)


Am 28. Oktober 2014 brachte der Bf. beim Bundesfinanzgericht einen „Vorlageantrag betreffend Berufungsvorentscheidung vom 8.10.2014 (vom Finanzamt fälschlicherweise als Bescheid – Zurücknahme/Gegenstandsloserklärung bezeichnet)“ ein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_23`)


Gegen das Schreiben vom 29. August 2014 des Finanzamtes sei laut Rechtsmittelbelehrung kein Rechtsmittel zulässig gewesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_26`)


Im Vorlagebericht beantragte das Finanzamt, dass das Bundesfinanzgericht in der Sache selbst abweislich entscheide: „   Der Beschwerdeführer verlangt eine sofortige Fortschreibung des Einheitswertes wegen der im Juni 2014 erfolgten Rodung eines Weingartens.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_32`)


Nach Auffassung des Finanzamtes Baden Mödling ist dieser in Erledigung der Beschwerde ergangene Bescheid dennoch als formal rechtskonforme Beschwerdevorentscheidung im Sinne von § 263 Abs 1 lit b Bundesabgabenordnung anzusehen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_49`)


Seite 4 von 5 Das Finanzamt hat den Mängelbehebungsauftrag (vom 29. August 2014) auf § 250 Abs. 1 lit. b-d BAO gestützt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_60`)


Die Beschwerde (vom 2. August 2014) entspricht auch dieser Anforderung: das Finanzamt hat den Antrag des Bf. auf Wertfortschreibung mit der Begründung abgewiesen, dass es sich bei der Weingartenrodung des Bf. um keine Dauerrodung handle, da er bei der entsprechenden Meldung als Wiederbepflanzungsberechtigter aufscheine und mitgeteilt, dass eine Dauerrodung im Jahr 2014 erst zum 1.1.2015 berücksichtigt werden könne.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_62`)


Der Auffassung des Finanzamtes, dass die Beschwerde (vom 2. August 2014) den Bestimmungen des § 250 Abs. 1 BAO nicht Rechnung tragen würde, kann daher nicht gefolgt werden.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Baden Mödling` | `Finanzamtes Baden Mödling` |

**Missed by this rule (FN):**

- `Dr. Alexander Hajicek` (person)
- `Mag. Helga Hochrieser` (person)
- `Mag. Michael Franz` (person)
- `Mag. Franz Josef Großin` (person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_5`)


Zum Streitpunkt Verjährung: Der Beschwerdeführer (Bf.) bezog im Berufungs(Beschwerde)zeitraum neben Einkünften aus nichtselbständiger Arbeit beim Finanzamt Mödling unter St.Nr. 111 einheitlich und gesondert festgestellte Einkünfte aus Vermietung und Verpachtung (als Beteiligter der aus ihm und seiner Ehegattin bestehenden Hausgemeinschaft "HG").

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_7`)


Nach Ergehen neuer Feststellungsbescheide vom 23.12.2010 (2001) bzw. 27.12.2010 (2002 bis 2008), welche die Einkünfte aus Vermietung und Verpachtung des Bf. mit Seite 2 von 15 788,28 € (bzw. 10.847,00 S, 2001), 940,38 € (2002), 975,45 € (2003), 1.141.04 € (2004), 1.328,63 € (2005), 77,30 € (2006), 2.172,21 € (2007) und 2.165,91 € (2008) feststellten, erließ das Finanzamt mit Datum 12.1.2011 gemäß § 295 BAO geänderte, den neuen Feststellungen Rechnung tragende Einkommensteuerbescheide 2000 bis 2008.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_9`)


In seiner abweisenden Berufungsvorentscheidung führt das Finanzamt Folgendes aus: "Die Verjährung beginnt gemäß § 208 Abs. 1 lit. d BAO in den Fällen des § 200 (vorläufige Festsetzung von Abgaben) mit dem Ablauf des Jahres, in dem die Ungewissheit beseitigt wurde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_18`)


Mit Schreiben vom 21.12.1998 wurde seitens der Hausgemeinschaft HG um Anwendung der neuen Liebhaberei-Verordnung angesucht und nach neuerlicher Aufforderung seitens des Finanzamtes mit Vorhalt vom 6.6.2003 um ergänzende Abgabe einer Prognoserechnung, wurde von der Hausgemeinschaft schließlich eine grobe Darstellung der Ausgaben bis 2004 vorgelegt sowie darauf hingewiesen, dass das Haus unter Denkmalschutz stünde.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_44`)


Das Finanzamt meint, dass erst mit dem Faktum der Betriebsprüfung die Ungewissheit beseitigt worden sei.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_45`)


Mit diesem Hinweis legt das Finanzamt lediglich dar, wann für das Finanzamt - subjektiv - die Ungewissheit beseitigt worden ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |
| `Finanzamt` | `Finanzamt` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_46`)


Das Finanzamt hat sich im Rahmen des Ermittlungsverfahrens allenfalls Kenntnis über die objektiven Umstände über das Vorliegen der Einkunftsquelle verschafft, aber keine Fakten geschaffen, die Einfluss auf das Bestehen oder Nichtbestehen der Einkunftsquelle haben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_47`)


Die Erkenntnisse, die das Finanzamt bei der Betriebsprüfung gewonnen hat, hätten bei ordnungsgemäßen Ermittlungsverfahren auch bereits in den Streitjahren gewonnen werden können, spätestens jedoch mit der Beantwortung des Vorhaltes vom 6. Juni 2003."

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_124`)


Die vom Finanzamt Mödling in den Feststellungsbescheiden getroffene Feststellungen, die Hausgemeinschaft habe in den Jahren 2001 bis 2008 Einkünfte von 1.576,56 € (2001), 1.880,77 € (2002) 1.950,91 € (2003), 2.282,08 € (2004), 2.657,27 € (2005), 154,60 € (2006), 4.344,41 € (2007) und 4.344,81 € (2008) erzielt, sind daher für das Einkommensteuerverfahren des Bf. bindend.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_133`)


Einem im Einkünftefeststellungsakt des Finanzamtes Mödling einliegenden Vermerk vom 12. Juni 2003 ist zu entnehmen, dass die Feststellungsbescheide seit 1995 vorläufig und die Bescheide vorläufig zu belassen seien (es sei ein Beobachtungszeitraum von 20 Jahren (21.12.1998) gestellt worden).

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_135`)


Am 4.5.2009 vermerkte das Finanzamt im Zuge der Überprüfung der vorläufigen Veranlagung, dass es sich um ein Haus handle, dass unter Denkmalschutz stehe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_145`)


Nach der Betriebsprüfung stellte das Finanzamt Mödling für die Jahre 2001 bis 2008 mit endgültigen Bescheiden vom 23.12.2010 (2001) und vom 27.12.2010 (2002 bis 2008) fest, dass nur hinsichtlich der vermieteten Putzerei eine Einkunftsquelle vorliege.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_149`)


In Anbetracht der vom der Hausgemeinschaft erklärten Werbungskostenüberschüsse ist das Finanzamt anlässlich der Erlassung der Feststellungsbescheide 2001 bis 2008 zum Ergebnis gekommen, dass bei der gegenständlichen Vermietung nicht von vornherein von Liebhaberei ausgegangen werden könne und hat daher vorläufige Feststellungsbescheide für die Jahre 2000 bis 2008 erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_153`)


Aufgrund der erklärten Werbungskostenüberschüsse konnte eine endgültige Qualifizierung der Vermietungstätigkeit der Bf. als Einkunftsquelle oder Liebhaberei nicht vorgenommen Seite 11 von 15 werden und lag aus damaliger Sicht für das Finanzamt eine die Vorläufigkeit rechtfertigende Ungewissheit im Tatsachenbereich zweifelsfrei vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_154`)


Das Finanzamt hat daher zu Recht zunächst vorläufige Bescheide erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_169`)


Es kommt nicht darauf an, wann das Finanzamt davon Kenntnis erlangte, sondern wann die Ungewissheit objektiv weggefallen ist.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_179`)


2. Zum Streitpunkt "Home Office": 2.1. Beweiswürdigung: Die obigen Sachverhaltsfeststellungen ergeben sich aus der Aktenlage des Finanzamtes und den Angaben des Bf. in der Berufung und im Vorlageantrag.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_8`)


Mit Erstbescheid vom 10. August 2017 veranlagte das Finanzamt (kurz FA) die Einkommensteuer 2015 auf Basis der elektronisch eingereichten Erklärung, ließ allerdings von insgesamt EUR 93.491,00 nur EUR 38.011,01 zum als freigebige Zuwendungen zum Sonderausgabenabzug zu. Bei der dafür ausschlaggebenden Berechnung der 10 % - Grenze brachte das FA im Rahmen des Gesamtbetrages der Einkünfte nur die im Inland Seite 2 von 6 steuerpflichtigen Einkünfte in Ansatz.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_7`)


Das Bundesfinanzgericht leitete den Antrag zuständigkeitshalber an  das Finanzamt weiter, wo der Antrag am 14.2.2020 fristgerecht einlangte.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_9`)


Mit Bescheid vom 13.11.2000 veranlagte das Finanzamt den Bf zur Einkommensteuer für 1999  zunächst erklärungsgemäß.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_10`)


Aufgrund von abweichenden Mitteilungen des für die Einkünftefeststellung gem. § 188 BAO  der Beteiligung A und der Beteiligung C vom 1.12.2006 erließ das Finanzamt am 9.1.2007 einen  gem. § 295 Abs. 1 BAO geänderten Einkommensteuerbescheid 1999 und setzte darin die  Einkünfte aus Gewerbebetrieb neu lediglich mit der Beteiligung B fest.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_12`)


Folglich dieser Mitteilung änderte das belangte Finanzamt den Einkommensteuerbescheid  1999 des Bf am 7.12.2007 erneut gem. § 295 Abs. 1 BAO dahingehend ab, dass in diesem  nunmehr Einkünfte aus Gewerbebetrieb iHv ATS 0,00 angesetzt wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_16`)


Verstoß gegen das für Grundlagenbescheide iSd § 188 BAO geltende Einheitlichkeitsgebot  insgesamt um Nichtbescheide handelt.  Mit schriftlichem Anbringen vom 20.12.2012, eingelangt beim Finanzamt am 28.12.2012,  beantragte die steuerliche Vertreterin des Bf ua den Einkommensteuerbescheid 1999 vom  7.12.2007 gem. § 295 Abs. 4 BAO aufzuheben, weil diesem auf Grundlage des § 295 Abs. 1 BAO  ergangenen Einkommensteuerbescheid laut Berufungsentscheidung des UFS vom 15.11.2012,  RV/0102-K/08 (betreffend Beteiligung KEG), ein Nichtbescheid mit Folge seiner  Rechtswidrigkeit zugrunde liege, und somit die Anspruchsvoraussetzungen iSd § 295 Abs. 4  BAO erfüllt seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_17`)


Mit offenkundig versehentlich als „Aufhebungsbescheid gem. § 299 BAO betiteltem  Sammelbescheid vom 12.3.2013 hob das belangte Finanzamt ua den  Einkommensteuerbescheid 1999 vom 7.12.2007 nach eindeutigem Bescheidspruch und damit  im Einklang stehender Begründung wie beantragt auf Grundlage des § 295 Abs. 4 BAO auf.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_19`)


Das Finanzamt hätte unrichtigerweise die  notwendigen ersetzenden Bescheide gem. § 299 Abs. 2 BAO nicht erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `James Hainig` (person)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `85-229/2263` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_5`)


Entscheidungsgründe  I. Verfahrensgang:  Mit Schreiben vom 15.06.2016 wurden die Erklärungen betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015 beim Finanzamt eingebracht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_37`)


Mit Bescheiden vom 21.12.2016 erließ das Finanzamt die Erstbescheide betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015 in denen die  Berufsgruppenpauschale für VertreterInnen nicht gewährt wurde und begründete die  Bescheide wie folgt:   "Vertreter sind nach übereinstimmender Lehre (Hofstätter/Reichel, Einkommensteuer  Kommentar, Tz 6 zu § 17 EStG), Verwaltungsübung LstRL RZ 406) und Entscheidungspraxis (zB  BFG 23.05.2014, RV/6100146/2013) Personen, die im Außendienst zum Zwecke der Anbahnung  und des Abschlusses von Kaufgeschäften und zur Kundenbetreuung tätig sind.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_92`)


Inhaltlich  hätte sich das Finanzamt **** durch umfassendere Beweiswürdigung mit der tatsächlichen  Tätigkeit der Beschwerdeführerin auseinanderzusetzen gehabt.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_11`)


Das Bundesfinanzgericht erklärte die Beschwerde, soweit diese die nachträgliche buchmäßige  Erfassung von Eingangsabgaben (Zoll) betrifft, mit Beschluss vom 26. Mai 2017,  RV/6200002/2017, als zurückgenommen, weil die Bf einem Mängelbehebungsauftrag  (Musteranforderung) innerhalb der vom Zollamt gesetzten Frist nicht nachgekommen war, und  sprach aus, dass eine Revision nach Art 133 Abs 4 B-VG nicht zulässig ist.

| Predicted | Gold |
|---|---|
| `Zollamt` | `Zollamt` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_9`)


der Bf.  habe dem Zollamt hingegen nur eine Menge an 71,92 bekannt gegeben.

| Predicted | Gold |
|---|---|
| `Zollamt` | `Zollamt` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_17`)


Mit 13.7.2015 stellte das Zollamt einen Antrag nach § 10 ALSAG bezüglich der Ablagerung von  Abfällen auf den Grundstücken Gst.

| Predicted | Gold |
|---|---|
| `Zollamt` | `Zollamt` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_4`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Antrag  Der Beschwerdeführerin (Bf.) beantragte mit dem am 21. März 2018 beim Finanzamt (FA)  eingelangtem Formular Beih 1 (datiert mit 12. Februar 2018) Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_12`)


Mit Bescheid vom 12. Juni 2018 wies das Finanzamt den Antrag vom 21.3.2018 auf  Familienbeihilfe für Jana Papenkord  ab Jänner 2011 ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Missed by this rule (FN):**

- `Jana Papenkord` (person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_23`)


Beschwerdevorentscheidung   Mit Beschwerdevorentscheidung vom 22.10.2018 wies das Finanzamt die Beschwerde als  unbegründet ab:  „Gemäß § 5 Abs. 1 Familienlastenausgleichsgesetz 1967 (FLAG 1967) in der ab 1. Jänner 2011  gültigen Fassung besteht für Kinder, die das 18.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_51`)


II. Über die Beschwerde wurde erwogen:  1. Sachverhalt   Vom Finanzamt wurde folgender Sachverhalt festgehalten:  „Der Eigenantrag auf Familienbeihilfe wurde am 21.03.2018 eingebracht.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_6`)


Nach Durchführung umfangreicher Ermittlungen bei den steuerlichen Vertretern und der  Masseverwalterin des Ehemannes wies das Finanzamt die Beschwerde mit  Beschwerdevorentscheidung vom 12.7.2016 als unbegründet ab.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_8`)


Das Finanzamt legte die Beschwerde dem Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Finanzamtes Linz` | `Finanzamtes Linz` |

**Missed by this rule (FN):**

- `Mag. Marco Laudacher` (person)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Mag. Manfred Frühwirth` (person)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_51`)


Im Anschluss an eine Außenprüfung für 2013 bis 2015 habe das Finanzamt auch für 2011  einen neuen Körperschaftsteuerbescheid erlassen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_113`)


Diese ist zusammen mit  der Gewinn- und Verlustrechnung dem Finanzamt vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Marion Endrulat` (person)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_10`)


…   Das Finanzamt erließ am 5. September 2019 den beschwerdegegenständlichen  Abweisungsbescheid wie folgt:   Ihr Antrag vom 5.4.2019 auf Familienbeihilfe wird abgewiesen für:   Name des Kindes VNR/Geb.dat.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_15`)


Das Finanzamt Gänserndorf  Mistelbach hat mit Bescheid diesen Antrag abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_33`)


IV. Beschwerdeerklärung und Anträge   Ich erhebe daher gegen den Bescheid der belangten Behörde vom 05.09.2019, (ohne) GZ, in  offener Frist gem § 243 BAO iVm Art 130 Abs 1 Z 1 B-VG und Art 131 Abs 3 B-VG   Bescheidbeschwerde an das Verwaltungsgericht des Bundes für Finanzen und stelle den   Antrag das Verwaltungsgericht des Bundes für Finanzen möge   - den angefochtenen Bescheid vom 05.09.2019, (ohne) GZ, aufheben und die Angelegenheit  zur Erlassung eines neuen - meinem Antrag stattgebenden - Bescheides an das Finanzamt  Gänserndorf Mistelbach zurückverweisen,   - in eventu den angefochtenen Bescheid dahingehend abändern, dass meinem Antrag auf  Familienbeihilfe für meinen Sohn … ab April 2019 stattgegeben wird.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_34`)


Das Finanzamt erließ eine abweisende Beschwerdevorentscheidung mit folgender  Begründung:   Das Kind …, SVNR …, wurde mit Wirkung 13.05.2019 in den Polizeidienst eingestellt.   Der Bestätigung des Bildungszentrums der Sicherheitsakademie Y. -SIAK- entnehmbar  absolviert der Sohn … vom 13.05.2019 bis 12.05.2021 den Grundausbildungslehrgang Y-… für  den Exekutivdienst im Bildungszentrum der Sicherheitsakademie Y..   Mit Dienstvertrag – als Sondervertrag gem. § 36 VBG 1948 – vom 13.05.2019 wurde das  privatrechtliche Dienstverhältnis zum Bund (§ 1 Abs. 1 VBG 1948) begründet.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_57`)


Die Bf. brachte daraufhin den Vorlageantrag ein, mit dem sie die in der Beschwerde gemachten  Ausführungen wiederholt.   Die Beschwerdevorlage des Finanzamtes erfolgte mit nachstehendem Sachverhalt und  Anträgen:   Sachverhalt:   Der Sohn der Beschwerdeführerin … begann am 13.05.2019 die exekutivdienstliche Ausbildung  im Bildungszentrum Y.. Die Einstellung in den Polizeidienst bei der Landespolizeidirektion  Niederösterreich erfolgte mit Sondervertrag nach § 36 VBG 1948.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Missed by this rule (FN):**

- `Landespolizeidirektion  Niederösterreich` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_157`)


Die Bf. ist der Ansicht, dass das vom Finanzamt zitierte Erkenntnis des VwGH vom 18.12.2018,  Ra 2018/16/0203 auf die exekutivdienstliche Ausbildung nicht anzuwenden wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer Anzeige vom 20.4.2017 vernahm das Finanzamt den Beschwerdeführer am  9.5.2017 ein und verfasste darüber eine Niederschrift.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_12`)


Das Finanzamt setzte mit Bescheid vom 7.6.2017 die Normverbrauchsabgabe für das Fahrzeug  BMF 750d xDrive mit der Fahrgestellnummer 12345 und dem amtlichen Kennzeichen (D) XYZ in  1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_22`)


Mit Schreiben vom 16.10.2017 forderte das Finanzamt den Beschwerdeführer auf,  zweckdienliche Unterlagen zum Beweis des dauernden Standortes bzw. der weitaus  überwiegenden betrieblichen Verwendung des Fahrzeuges im Ausland und zum Beweis des  Mittelpunkts seiner Lebensinteressen im Ausland vorzulegen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_23`)


Weiter forderte das Finanzamt  eine Aufstellung der betrieblich bzw privat gefahrenen Kilometer im In- und Ausland an.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_24`)


Das  Finanzamt verwies dabei auf zwei vorliegenden Tankrechnungen (eni Reutte vom 4.5.2017 und  Shell d_Ort_1 vom 28.4.2017).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_36`)


Mit Beschwerdevorentscheidung vom 22.3.2018 wies das Finanzamt die Beschwerde ab und  begründete dies damit, dass der Beschwerdeführer bei seiner Einvernahme am 9.5.2017  angegeben habe, der Besitzer und Verwender des gegenständlichen Fahrzeuges zu sein.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_46`)


Im Vorlagebericht vom 25.5.2018 brachte das Finanzamt weiter vor, dass der  Beschwerdeführer die im Vorlageantrag angesprochene Anmeldebestätigung nicht vorgelegt  habe.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_67`)


Der Beschwerdeführer sagte bei  seiner Befragung durch Organe der Finanzpolizei am 9.5.2017 unter anderem aus, dass er bis  26.5.2017 ein Firmenfahrzeug der AG genutzt habe, und weiter: „Dieses Fahrzeug muss ich am  26.5.2017 zurückgeben.

| Predicted | Gold |
|---|---|
| `Finanzpolizei` | `Finanzpolizei` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_226`)


Einwendungen gegen die vom  Finanzamt ermittelten Bemessungsgrundlagen und die Höhe der festgesetzten Abgaben hat  der Beschwerdeführer nicht erhoben.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_43`)


1. Anspruchsberechtigung auf Familienbeihilfe/Ausgleichszahlung für das Kind x im Zeitraum  vom 01.02.2016 bis zum 30.11.2017  Unter Bezugnahme auf die Ausführungen der belangten Behörde in  der Beschwerdevorentscheidung (BVE) vom 08.01.2020 sowie in der Ihnen  übermittelten Stellungnahme im Vorlagebericht des Finanzamtes vom 14.04.2020 werden Sie  nochmals darauf hingewiesen, dass in Ermangelung des Bestehens eines gemeinsamen  Haushalts mit obigem Kind eine Anspruchsberechtigung für nämlichen Zeitraum nicht zum  Tragen kommt.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_5`)


Dauer der Tätigkeit: 31.08.2020  Bezeichnung der Schule: Sicherheitsakademie T.[Adresse]   Schulform: Sonstiges   Schuljahr: 2018/2019  Das Finanzamt erließ am 21. August 2019 den beschwerdegegenständlichen Bescheid, mit dem  der Antrag der Bf. vom 6. April 2019 auf Familienbeihilfe ab September 2018 abgewiesen  wurde;

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_8`)


Gegen den Abweisungsbescheid erhob die Bf. die Beschwerde vom 30. August 2019 wie folgt:   Die vom Finanzamt Wien 4/5/10 per 26. April 2019 mit Ersuchen um Ergänzung abverlangten  Unterlagen (Dienstvertrag) habe ich am 06. Mai 2019 (Frist bis 17. Mai 2019) mittels  „Einschreiben“, Sendungsnummer: RM 205067923AT, an das Finanzamt Wien 4/5/10  übermittelt.   Da ich in der Zwischenzeit (Anfang Juli 2019) umgezogen bin, habe ich via Finanzonline eine  Nachricht erhalten, dass von nun an das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf  zuständig sei.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` | `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` |

**Missed by this rule (FN):**

- `Finanzamt Wien 4/5/10` (organisation)
- `Finanzamt Wien 4/5/10` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_30`)


Das Finanzamt wies mit Beschwerdevorentscheidung vom 25. Oktober 2019, zugestellt durch  Hinterlegung am 30. Oktober 2019, die Beschwerde als unbegründet ab und begründete dies  wie folgt:   Gemäß § 2 Abs. 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die  im Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_62`)


In der Beschwerdevorlage wies das Finanzamt auf die exekutivdienstliche Ausbildung der Bf.  mit Sondervertrag für Vertragsbedienstete des Bundes sowie auf das Erkenntnis des VwGH  vom 18.12.2018, GZ Ra 2018/16/0203, hin und beantragte die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_167`)


Die Bf. ist der Ansicht, dass das vom Finanzamt zitierte Erkenntnis des VwGH vom 18.12.2018,  Ra 2018/16/0203 auf die exekutivdienstliche Ausbildung nicht anzuwenden wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_3`)


Begründung  Am 10.5.2019 erließ das Finanzamt gegenüber der Beschwerdeführerin (Bf.) die  Einkommensteuerbescheide (Arbeitnehmerveranlagung) für 2015 bis 2018 (die Bescheide der  Jahre 2015 bis 2017 ergingen im Rahmen einer beantragten Wiederaufnahme).

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_4`)


Mit Eingabe vom 11.4.2020, die vom Finanzamt – nach Ansicht des BFG zutreffend – als Antrag  auf Aufhebung der Einkommensteuerbescheide 2015 bis 2018 gemäß § 299 BAO gewertet  wurde, bemängelte die Bf., dass in den Bescheiden die Mietkosten für ihren Sohn nicht als  außergewöhnliche Belastungen berücksichtigt worden seien.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_8`)


Mit den angefochtenen Bescheiden wies das Finanzamt den Antrag der Bf. mit folgender  Begründung ab:  „Außergewöhnliche Belastungen müssen gemäß § 34 EStG 1988 folgende Voraussetzungen  erfüllen:  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_22`)


Die abweisenden Beschwerdevorentscheidungen begründete das Finanzamt wie folgt:  „Eine außergewöhnliche Belastung im Sinne des § 34 EStG 1988 liegt dann vor, wenn die  Ausgaben außergewöhnlich und zwangsläufig erwachsen sind und die wirtschaftliche  Leistungsfähigkeit beeinträchtigen.

| Predicted | Gold |
|---|---|
| `Finanzamt` | `Finanzamt` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_71`)


Dazu kommt, dass in den Bescheiden des Finanzamtes lediglich auf die Abs. 1 bis 4 des § 34  EStG 1988 verwiesen wird.

| Predicted | Gold |
|---|---|
| `Finanzamtes` | `Finanzamtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Erich Schwaiger`(person)
- `Jeannette Neuschwender`(person)
- `Zum Kogl 12, 4441 Penz, Österreich`(address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Peter Staudinger`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Mirha Karahodzic MA`(person)
- `Elisabeth Schafstall`(person)
- `Leithagürtel 20, 4251 Steinwald, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Tirol Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dietlind Mahlstädt`(person)
- `Kai Pipers`(person)
- `Gottaweg 58, 9130 Annamischl, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH`(organisation)
- `Finanzamt Tirol Ost`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_11`)


Aufgrund einer weiteren Mitteilung setzte das damals auch für die einheitliche und gesonderte  Einkünftefeststellung der B K(E)G zuständig gewesene Finanzamt Wien 8/16/17  das Wohnsitzfinanzamt des  Bf davon in Kenntnis, dass im Feststellungsverfahren dieser Personengesellschaft am  28.11.2006 ebenfalls ua Erledigungen betreffend das Unterbleiben von Einkünftefeststellungen  für die beteiligten Kommanditisten für die Jahre 1998-2001 ausgefertigt worden sind.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 8/16/17`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_14`)


Im Dezember 2006 legte die B KEG ua Berufungen gegen die an sie adressierten „Bescheide“  des FA Wien 8/16/17  vom 1.12.2006 betreffend Einkünftefeststellung gem. § 188 BAO für die Jahre  1988 – 2001 sowie gegen die an sie und an die Kommanditisten adressierten „Bescheide“ des  Finanzamt Wien 8/16/17  vom 28.11.2006 betreffend Unterbleiben der Feststellungen von Einkünften in  Bezug auf die Kommanditisten für den Zeitraum 1998 – 2001 ein.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FA Wien 8/16/17`(organisation)
- `Finanzamt Wien 8/16/17`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zollamtes` — partial — pred is substring of gold: `Zollamtes  Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Adalbert Köseoglu`(person)
- `Christine Höffert`(person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich`(address)
- `Zollamtes  Salzburg`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zollamtes` — partial — pred is substring of gold: `Zollamtes Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Walter Summersberger`(person)
- `Emmerich Frydrychowski`(person)
- `Wassertheuer 21, 9112 Gletschach, Österreich`(address)
- `Zollamtes Innsbruck`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Helga Hochrieser`(person)
- `Finanzamtes Wien 1/23`(organisation)
- `Jana Papenkord`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ali Jäckle`(person)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_14`)


Gegen den Abweisungsbescheid erhob die Bf. die Beschwerde vom 15. September 2019 wie  folgt:   I. Sachverhalt:   Ich habe am 05.04.2019 für meinen Sohn … ab dem Zeitraum April 2019 die Familienbeihilfe  beim zuständigen Finanzamt Gänserndorf Mistelbach beantragt, da dieser seit Mai 2019 eine  Berufsausbildung (bis Ende März 2019 Zivildienst) absolviert.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Gänserndorf Mistelbach`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_17`)


III. Rechtsverletzung und Beschwerdegründe:   Der Abweisungsbescheid des Finanzamtes Gänserndorf Mistelbach vom 05.09.2019, (ohne) GZ,  verletzt mich in meinem subjektiven Recht.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_29`)


Das Finanzamt Gänserndorf Mistelbach hat unzutreffend und rechtswidrig eine  Ausbildungsphase der fremden- und grenzpolizeilichen exekutivdienstlichen Ausbildung, die  keinen Anspruch auf Familienbeihilfe begründet (weil das FLAG 1967 den Begriff der  Ausbildungsphase nicht kennt), bei der 24-monatigen durchgehenden Ausbildung meines  Sohnes … angenommen.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Gänserndorf Mistelbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Gänserndorf Mistelbach`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien  2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sabine Tiedicke`(person)
- `Ritterhof 8, 4280 Harlingsedt, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf` — partial — gold is substring of pred: `Finanzamtes Wien  3/6/7/11/15`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Sascha Hilcker`(person)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich`(address)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_8`)


Gegen den Abweisungsbescheid erhob die Bf. die Beschwerde vom 30. August 2019 wie folgt:   Die vom Finanzamt Wien 4/5/10 per 26. April 2019 mit Ersuchen um Ergänzung abverlangten  Unterlagen (Dienstvertrag) habe ich am 06. Mai 2019 (Frist bis 17. Mai 2019) mittels  „Einschreiben“, Sendungsnummer: RM 205067923AT, an das Finanzamt Wien 4/5/10  übermittelt.   Da ich in der Zwischenzeit (Anfang Juli 2019) umgezogen bin, habe ich via Finanzonline eine  Nachricht erhalten, dass von nun an das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf  zuständig sei.

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 4/5/10`
- `Finanzamt` — similar text (different position): `Finanzamt Wien 4/5/10`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 4/5/10`(organisation)
- `Finanzamt Wien 4/5/10`(organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_9`)


Nun erhielt ich am 26.08.2019 einen Abweisungsbescheid vom Finanzamt Wien 3/6/7/11/15  Schwechat Gerasdorf mit der Begründung, dass ich die abverlangten Unterlagen nicht  eingebracht hätte.

**False Positives:**

- `Finanzamt Wien 3/6/7/11/15  Schwechat Gerasdorf` — partial — gold is substring of pred: `Finanzamt Wien 3/6/7/11/15`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 3/6/7/11/15`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_45`)


Der Vorlageantrag der Bf. vom 28. November 2019, fristgerecht eingebracht durch  Postaufgabe am 29. November 2019, enthält nachstehende Begründung:   Die Beschwerdevorentscheidung des Finanzamtes Wien 3/6/7/11/15/ Schwechat Gerasdorf  vom 25.10.2019, verletzt mich in meinem subjektiven Recht.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Wien 3/6/7/11/15/ Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 3/6/7/11/15/ Schwechat Gerasdorf`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_56`)


Das Finanzamt Wien 3/6/7/11/15/ Schwechat Gerasdorf hat unzutreffend und rechtswidrig  5 von 17 Seite 6 von 17

**False Positives:**

- `Finanzamt` — partial — pred is substring of gold: `Finanzamt Wien 3/6/7/11/15`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 3/6/7/11/15`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

**False Positives:**

- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Helge Göppele`(person)
- `GDJJ Versand`(organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich`(address)
- `Finanzamtes Graz`(organisation)

</details>

---

## `german_company_ag` 🏆

**F1:** 0.041 | **Precision:** 0.614 | **Recall:** 0.021  

**Format:** `regex`  
**Rule ID:** `9a8e6f9f`  
**Description:**
Matches AG companies, requiring a valid name start and excluding common articles.

**Content:**
```
\b(?<!\w)(?:(?:Fa\.|[A-Z][a-zA-Z0-9\-+&]*(?:\s+[A-Z][a-zA-Z0-9\-+&]*)*)\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.614 | 0.021 | 0.041 | 176 | 108 | 68 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 108 | 68 | 4935 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_42`)


In Zusammenhang mit den in Höhe von 338,69 € als sonstige Werbungskosten geltend  gemachten, bislang aber noch nicht belegmäßig nachgewiesenen Ausgaben, führte der Bf aus,  dass es sich dabei um die Betriebsratsumlage der SeeAutomotive AG Österreich handle, welche in Höhe von  4 x 27,68 € (Jänner bis April), 5 x 28,47 € (Mai bis September) und 3 x 28,54 € (Oktober bis  Dezember) entrichtet worden sei und übermittelte diesbezüglich einen Ausschnitt eines  Lohnzettels für den Monat Jänner, aus dem hervorgeht, dass eine Betriebsratsumlage in Höhe  von 27,68 € in Abzug gebracht wurde.

| Predicted | Gold |
|---|---|
| `SeeAutomotive AG` | `SeeAutomotive AG` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_42`)


Im Rahmen seiner Geschäftsführertätigkeit für die Schilift GmbH habe der Beschwerdeführer  am 9.1.2008 ein Lieferübereinkommen mit der Traun-Handel AG abgeschlossen und eine persönliche  Garantieerklärung abgegeben.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_70`)


Der Beschwerdeführer unterfertigte am 9.1.2008 als Geschäftsführer der Schilift GmbH ein  Bierlieferungsübereinkommen mit der Traun-Handel AG  Gleichzeitig unterfertigte er eine „unwiderrufliche  Garantie, dass der Vertragspartner sämtliche Verpflichtungen aus dem Übereinkommen  ordnungsgemäß erfüllt. Ich … verpflichte mich … über erste schriftliche Aufforderung die  Verpflichtungen des Vertragspartners mit ihm zur ungeteilten Hand zu erfüllen …“.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_72`)


Der Beschwerdeführer bezahlte am 9.7.2010 einen Vergleichsbetrag von EUR 8.000,- an die Traun-Handel AG  welche ihn daraufhin aus der Haftung des Lieferungsübereinkommens vom 8.1.2007 und  der daraus entstandenen Forderung entließ.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_73`)


Dies ist aufgrund der bei den vom Finanzamt  vorgelegten Akten befindlichen Schreiben der Traun-Handel AG vom 28.6.2010 und vom 13.7.2010 und  durch einen vom Beschwerdeführer am 10.2.2021 vorgelegten Bankauszug erwiesen.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_92`)


Insgesamt zeigt sich, dass dem Finanzamt die entscheidungswesentlichen  Sachverhaltselemente im Zusammenhang mit den Zahlungen an die Traun-Handel AG und an RA Dr. E bei  der Erstveranlagung nicht bekannt waren und dass das Finanzamt erst im  Außenprüfungsverfahren von diesen Sachverhaltselementen Kenntnis erlangt hat.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `RA Dr. E` (person)
- `Finanzamt` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_96`)


Die steuerlichen  Auswirkungen können auch nicht als bloß geringfügig angesehen werden.“) samt Verweis auf  die Gesamtauswirkungen der Prüfungsfeststellungen laut Prüfungsbericht vom 13.9.2012 legt  die entscheidungswesentlichen Ermessenskriterien vollständig und in nachvollziehbarer Weise  offen, zumal auch der Prüfungsbericht vom 13.9.2012 unter Tz 5 (nochmals) eine Begründung  der Ermessensübung bezogen auf die getroffene Feststellung zur Vergleichszahlung an die Traun-Handel AG enthält.  Insgesamt erweist sich die Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer  2010 als zulässig.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_106`)


Der Beschwerdeführer war zum Zeitpunkt der Abgabe der Garantieerklärung gegenüber der Traun-Handel AG Gesellschafter und Geschäftsführer der Schilift GmbH, weshalb die Ausgaben im  Zusammenhang mit der Haftungsinanspruchnahme durch die Traun-Handel AG seiner  Gesellschafterstellung zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_111`)


Auch aus diesem Grund sind die Zahlungen im  Zusammenhang mit der Haftungsinanspruchnahme durch die Traun-Handel AG gemäß § 20 Abs. 2 EStG  1988 dem Grunde nach nicht als Werbungskosten bei Einkünften aus Kapitalvermögen  abzugsfähig.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_116`)


Insofern der Beschwerdeführer vermeint, seine (unentgeltliche) Geschäftsführertätigkeit für  die Schilift GmbH stelle bei wirtschaftlicher Betrachtungsweise einen Zusammenhang zwischen  seiner Garantieerklärung gegenüber der Traun-Handel AG und seinen Einkünften aus selbständiger Arbeit  als (wesentlich beteiligter) Gesellschafter-Geschäftsführer seiner Wirtschaftstreuhand GmbH  her, ist dem Folgendes entgegenzuhalten: Nach dem Beschwerdevorbringen war die Erzielung  von Einkünften durch die Bf. Steuerberatungsgesellschaft mbH aus Beratungstätigkeiten für D  und dessen Unternehmen und für die neu gewonnenen Mitgesellschafter der Schilift GmbH  von der Erhaltung der „langfristigen Werthaltigkeit der empfohlenen Investitionen und  Beteiligungen“ abhängig.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_118`)


Daher ist nicht einmal ein mittelbarer Zusammenhang  zwischen seiner Garantieerklärung gegenüber der Traun-Handel AG und seinen Einkünften aus  selbständiger Arbeit erkennbar.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_119`)


Somit stellen die Zahlungen im Zusammenhang mit der  Garantieerklärung gegenüber der Traun-Handel AG keine Betriebsausgaben dar.

| Predicted | Gold |
|---|---|
| `Traun-Handel AG` | `Traun-Handel AG` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_36`)


II. Sachverhalt   Der in xx geborene Bf. ist österreichischer Staatsbürger und steht zumindest seit 01.01.2009 in  einem aufrechten Dienstverhältnis zur Beratung Bruckbach AG  eingetragen im Firmenbuch des LG X zur FN  xxxxxxx, mit dem Sitz in xx..

| Predicted | Gold |
|---|---|
| `Beratung Bruckbach AG` | `Beratung Bruckbach AG` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_51`)


Informativ wird mitgeteilt, dass die Einzahlung der verhängten Geldstrafe sowie die Kosten des  Verfahrens von der belangten Behörde auf folgendes Bankkonto des Magistrats der Stadt Wien  bei der UniCredit Bank Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 – Strafen;

| Predicted | Gold |
|---|---|
| `UniCredit Bank Austria AG` | `UniCredit Bank Austria AG` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_12`)


Im Prüfungszeitraum 2015 bis 2016 kauft das geprüfte Unternehmen die Glukose aufgrund  eines mehrjährigen Rahmenvertrages bei der Gartsynval Dienstleistungen AG (J.) in W. ein und beliefert  verschiedene EU-Abnehmer (J. Konzerngesellschaften, Lebensmittelhersteller und chemisch- pharmazeutische Unternehmen).

| Predicted | Gold |
|---|---|
| `Gartsynval Dienstleistungen AG` | `Gartsynval Dienstleistungen AG` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_170`)


Diese Glukose bezieht Bf. u.a. vom österreichischen Lieferanten ZWOP Cloud AG  Bf. hat mit ZWOP Cloud AG mehrjährige Lieferverträge abgeschlossen.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_171`)


Im Konkreten erwarb Bf. mit Vertrag vom  10.12.2014 bei ZWOP Cloud AG als Lohnfertiger Glukose in bestimmten Mengen für die Jahre 2014, 2015,  2016 und 2017.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_174`)


Der  Transport wurde dabei stets von Bf. oder deren EU-Kunden durchgeführt, da die mit ZWOP Cloud AG  vereinbarte Lieferkondition „FCA“ war.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_175`)


Die von ZWOP Cloud AG erworbenen Waren wurden von Bf. an verschiedene EU- Kunden (Unternehmer)  weiterveräußert.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_176`)


Die Ware gelangte dabei direkt vom Werk von ZWOP Cloud AG in P. (Niederösterreich)  an die jeweiligen EUR-Kunden in verschiedenen EU-Mitgliedstaaten.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_182`)


In beiden Fällen (dh sowohl bei Transport durch den EU-Kunden als auch durch Bf.) hat ZWOP Cloud AG  Rechnungen mit 10% österreichischer Umsatzsteuer gelegt.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_183`)


Gegenüber ZWOP Cloud AG und den EU- Kunden ist Bf. stets mit ihrer österreichischen UID-Nummer aufgetreten, welche auch von ZWOP Cloud AG  in den Rechnungen angeführt wurde.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_189`)


wurde) wurden von der belangten Behörde dergestalt beurteilt, dass es sich bei der Lieferung ZWOP Cloud AG- Bf. um die bewegte Lieferung im Reihengeschäft gemäß § 3 Abs. 8 UStG handelt. Da Bf.  gegenüber ZWOP Cloud AG jedoch nicht mit einer UID-Nummer des Bestimmungslandes, sondern mit der  österreichischen UID-Nummer aufgetreten ist, wurde von der belangten Behörde ein sog.  fiktiver innergemeinschaftlicher Erwerb gem. Art 3 Abs. 8 zweiter Satz UStG ohne  Vorsteuerabzugsrecht festgesetzt, wogegen sich diese Beschwerde richtet.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Missed by this rule (FN):**

- `ZWOP Cloud AG-` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_191`)


Dies vor  allem deshalb, weil - anders als bei einem klassischen Reihengeschäft - Bf. an ihren EU-Kunden  Ware verkauft, die sie selber zeitlich aber weit vorgelagert und unabhängig von den weiteren  Veräußerungen bei ZWOP Cloud AG gekauft hat.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_192`)


Die beiden Lieferungen werden somit nicht dadurch  ausgeführt, dass der erste Unternehmer dem letzten Abnehmer in der Reihe unmittelbar die  Verfügungsmacht an dem Gegenstand verschafft (vgl. Ruppe/Achatz, UStG, 5. Auflage, § 3  Rz. 53 mwN), sondern es wird die Verfügungsmacht zuerst von ZWOP Cloud AG auf Bf. übertragen und  erst nachgelagert in einem zweiten Schritt von Bf. auf den EU-Kunden.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_193`)


So hat Bf. einen Vertrag über den Kauf von Produkten in bestimmten Mengen für die  streitgegenständlichen Jahre mit ZWOP Cloud AG abgeschlossen.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_195`)


Im Vertrag mit ZWOP Cloud AG wurde auch geregelt, dass die Lieferung mit Abgabe der Ware aus dem Füllstutzen als  ausgeführt gilt und in diesem Zeitpunkt der Eigentumsübergang erfolgt, aber auch Risiken des  Verlustes oder des zufälligen Untergangs übergehen.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_196`)


Mit Abholung der Produkte bzw. bei  Beladung der LKWs geht somit vertraglich die Verfügungsmacht von ZWOP Cloud AG auf Bf. über.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_198`)


Die Lieferungen von ZWOP Cloud AG sind folglich in Österreich steuerbar und  steuerpflichtig.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_207`)


- Verwendung der UID-Nummer  Bf. ist stets gegenüber ZWOP Cloud AG und ihren EU-Kunden mit ihrer österreichischen UID-Nummer  aufgetreten.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_216`)


Ganz im Gegenteil wurde von ZWOP Cloud AG österreichische Umsatzsteuer in Rechnung gestellt und  ordnungsgemäß erklärt und abgeführt.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_238`)


Wie oben bereits ausgeführt, war ZWOP Cloud AG über den Verkauf der Ware stets informiert.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_244`)


D.h. die Inrechnungstellung von österreichischer  Umsatzsteuer durch ZWOP Cloud AG ist zu Recht erfolgt, weil es sich bei dieser Lieferung mangels  Transportzuordnung nicht um die grenzüberschreitende innergemeinschaftliche Lieferung  handelt.  Als Zwischenergebnis kann somit festgehalten werden, dass unter Berücksichtigung aller  Umstände des Einzelfalles die Zuordnung des grenzüberschreitenden Transports zur zweiten  Lieferung, nämlich der von Bf. an den EU-Kunden, zu erfolgen hat.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_246`)


Die Lieferung von ZWOP Cloud AG an Bf. ist folglich als ruhende Lieferung zu beurteilen, die gem. § 3  Abs. 7 UStG in Österreich steuerbar und steuerpflichtig ist.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_254`)


Die ruhende Lieferung im Reihengeschäft kann allerdings (vgl. auch Ruppe/Achatz, UStG,  5. Auflage, § 3 Tz 56) nie als innergemeinschaftliche Lieferung bzw. innergemeinschaftlicher  Erwerb qualifiziert werden, sodass die Annahme eines fiktiven innergemeinschaftlichen  Erwerbs durch Bf. im Zuge des gegenständlichen Ankaufs der Waren von ZWOP Cloud AG durch  Verwendung der österreichischen Umsatzsteuer-Identifikationsnummer von vornherein nicht  denkbar ist.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_282`)


Im Prüfungszeitraum 2015 bis 2016 kauft das geprüfte Unternehmen die Glukose aufgrund  eines mehrjährigen Rahmenvertrages bei der ZWOP Cloud AG (J.) in W. ein und beliefert verschiedene EU- Abnehmer (J. Konzerngesellschaften, Lebensmittelhersteller und chemisch -pharmazeutische  Unternehmen).

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_290`)


In beiden Fällen (Lieferkondition DDP bzw. FCA in den Rechnungen von Bf.) legt ZWOP Cloud AG  Rechnungen mit 10% österreichischer Umsatzsteuer, die von Bf. als Vorsteuer in Abzug  gebracht wird.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_303`)


Die ruhende  Lieferung besteht zwischen ZWOP Cloud AG und Bf. (steuerbarer und steuerpflichtiger Umsatz von ZWOP Cloud AG.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_305`)


In diesen Fällen ist von  einer bewegten Lieferung gem. § 3 Abs. 8 UStG zwischen ZWOP Cloud AG und Bf. auszugehen.ZWOP Cloud AG tätigt   daher in Österreich steuerbare und bei Vorliegen der Voraussetzungen gem. Art. 6 Abs. 1 i.V.m.  20 von 59 Seite 21 von 59

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Missed by this rule (FN):**

- `.ZWOP Cloud AG` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_460`)


Eingangsrechnung vom 2.2.2015 ZWOP Cloud AG an Bf. über 24.620 kg á 223,16 € = 5.494,20 € (netto)  zuzügl.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_473`)


Zum Rahmenvertrag vom 10.12.2014 zwischen der ZWOP Cloud AG und der Bf. ist auszuführen, während  der Laufzeit des Vertrages sind im „Rahmen der festgelegten Mengen“ diese durch den  Auftraggeber (Bf.) dem Auftragnehmer (J. AG) Bestellungen über SAP, E-Mail oder Fax zwei  Werktage vor dem geplanten Liefertermin zu übermitteln.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Missed by this rule (FN):**

- `J. AG` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_480`)


Abgesehen davon werden von der ZWOP Cloud AG auch nicht die gesamte  Jahresmenge in einem, sondern lediglich die bestellten Mengen an die Bf. fakturiert.

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_885`)


Der von der Bf. aus den Rechnungen der  58 von 59 Seite 59 von 59 ZWOP Cloud AG (A) vorgenommene Vorsteuerabzug war abzuerkennen, weil er nicht aus steuerbaren und  steuerpflichtigen (ruhenden) Inlandslieferungen an die Bf., sondern aus steuerbaren, aber  steuerbefreiten innergemeinschaftlichen Lieferungen resultierte (VwGH 5.3.2020, Ro  2018/15/0004).

| Predicted | Gold |
|---|---|
| `ZWOP Cloud AG` | `ZWOP Cloud AG` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der in Österreich ansässige Beschwerdeführer (Bf.) war in den Jahren 2015 bis 2017 bei der  Holz Nexglanz AG  in Auersbach  in Frankreich als technischer Geschäftsführer beschäftigt.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Missed by this rule (FN):**

- `Auersbach` (city)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_11`)


Finanzamt an den Einkünften des Jahres 2014, in dem der Bf. noch bei der Alpen-Wind AG  in  Österreich beschäftigt war.

| Predicted | Gold |
|---|---|
| `Alpen-Wind AG` | `Alpen-Wind AG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_19`)


Mit der Beschwerde legte die Steuervertretung in Frankreich eingereichte Steuererklärungen  und Steuerbescheide sowie eine Kalenderaufstellung 2015 bis 2017 der Holz Nexglanz AG  über  die Aufenthalte des Bf. in Frankreich und außerhalb Frankreichs vor.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_23`)


Mit dem Antwortschreiben vom 14.11.2019 legte die Steuervertretung eine  Tätigkeitsbeschreibung durch die Holz Nexglanz AG  und die Kumulativjournale 2015 bis 2017 vor.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_38`)


Im Folgenden wird der aufgrund des bisherigen Verfahrenslaufes vorliegende  entscheidungsrelevante Sachverhalt noch einmal kurz zusammengefasst wie folgt:    Bis 31.12.2014 war der Bf. bei der Alpen-Wind AG  unselbständig beschäftig.

| Predicted | Gold |
|---|---|
| `Alpen-Wind AG` | `Alpen-Wind AG` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_39`)


 Seit 1.1.2015 ist er als technischer Geschäftsführer bei der Holz Nexglanz AG  in Auersbach  tätig, wo er die Bereiche Produktentwicklung, Technologieentwicklung und  das Qualitätsmanagement über hat.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Missed by this rule (FN):**

- `Auersbach` (city)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_48`)


Mit seinen aus der Tätigkeit für die Holz Nexglanz AG  bezogenen Einkünften unterlag der Bf.  in Frankreich der Einkommensteuer.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_52`)


Beweiswürdigung  Dieser Sachverhalt ergibt sich zweifelsfrei aus den dem Gericht vorliegenden Unterlagen, und  zwar der Arbeitsbeschreibung und Aufstellung über die Arbeitstage- und orte sowie der  Kumulativjournale 2015 bis 2017 der Holz Nexglanz AG; den Steuererklärungen und  Steuerbescheiden der Direction Génerale des Finances-Publique sowie den Eintragungen in das  Zentrale Melderegister.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_90`)


Das heißt, dass Frankreich als Tätigkeitsstaat das Besteuerungsrecht über die Einkünfte des Bf.  aus seiner Tätigkeit für die Holz Nexglanz AG  nur insoweit zustand, als die Tätigkeit auch  tatsächlich in Frankreich ausgeübt wurde.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_99`)


Im Beschwerdefall kam es zu keinem Rückfall des nach Artikel 15 Abs. 1 DBA Frankreich  zugewiesenen Besteuerungsrechts an den Ansässigkeitsstaat Österreich, weil der Bf. in allen  den Jahren 2015 bis 2017 an mehr als an 183 Tagen in Frankreich tätig war und zudem die  Vergütungen von einer Arbeitgeberin (die Holz Nexglanz AG) in ausbezahlt wurden, die in  Frankreich ansässig ist.

| Predicted | Gold |
|---|---|
| `Holz Nexglanz AG` | `Holz Nexglanz AG` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_103`)


Informativ wird mitgeteilt, dass die Einzahlung der Geldstrafe (€ 60,00) samt Kosten des  verwaltungsbehördlichen Verfahrens (€ 10,00) und des Beschwerdeverfahrens (€ 12,00) von  gesamt € 82,00 auf folgendes Bankkonto des Magistrats der Stadt Wien bei der UniCredit Bank  Austria AG erfolgen kann:  Empfänger: MA 6 - BA 32 - Verkehrsstrafen  IBAN: AT***, BIC: ***  Bitte die Geschäftszahl des Straferkenntnisses des Magistrats angeben: Zahl  Gemäß § 52 Abs. 6 VwGVG sind die §§ 14 und 54b Abs. 1 und 1a VStG sinngemäß anzuwenden.

| Predicted | Gold |
|---|---|
| `UniCredit Bank  Austria AG` | `UniCredit Bank  Austria AG` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien` (organisation)
- `Magistrats` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_46`)


In der am 16.5.2022 abgehaltenen mündlichen Verhandlung führte der steuerliche Vertreter  der Bf aus, bei der an der Bf beteiligten KI Lexnor AG  handle es sich um eine ausländische  Gesellschaft nach deutschem Recht.

| Predicted | Gold |
|---|---|
| `KI Lexnor AG` | `KI Lexnor AG` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_57`)


Ende 2021 änderte sich dies dahingehend, dass aufgrund einer  Umstrukturierung die in Deutschland ansässige KI Lexnor AG  und die in Österreich ansässige  Valgarttra-Sanitär GmbH  Gesellschafter der Bf wurden.

| Predicted | Gold |
|---|---|
| `KI Lexnor AG` | `KI Lexnor AG` |

**Missed by this rule (FN):**

- `Valgarttra-Sanitär GmbH` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_58`)


Die diesbezüglichen Eintragungen im  Firmenbuch erfolgten am 1.12.2021 (betreffend die KI Lexnor AG  als neue Gesellschafterin der  Bf) und am 3.12.2021 (betreffend die Valgarttra-Sanitär GmbH  als neue Gesellschafterin der Bf).

| Predicted | Gold |
|---|---|
| `KI Lexnor AG` | `KI Lexnor AG` |

**Missed by this rule (FN):**

- `Valgarttra-Sanitär GmbH` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_82`)


Aufgrund einer Umstrukturierung wurden Ende 2021 die in Deutschland ansässige KI Lexnor AG  und die in Österreich ansässige Valgarttra-Sanitär GmbH  Gesellschafter der Bf.

| Predicted | Gold |
|---|---|
| `KI Lexnor AG` | `KI Lexnor AG` |

**Missed by this rule (FN):**

- `Valgarttra-Sanitär GmbH` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_83`)


Die diesbezüglichen  Eintragungen im Firmenbuch erfolgten am 1.12.2021 (betreffend die KI Lexnor AG  als neue  Gesellschafterin der Bf) und am 3.12.2021 (betreffend die Valgarttra-Sanitär GmbH  als neue  Gesellschafterin der Bf).

| Predicted | Gold |
|---|---|
| `KI Lexnor AG` | `KI Lexnor AG` |

**Missed by this rule (FN):**

- `Valgarttra-Sanitär GmbH` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_85`)


Ausgehend von § 5 Abs 1 WiEReG, demzufolge Änderungen der Angaben binnen vier Wochen  nach Kenntnis der Änderung zu übermitteln sind, wobei bei Daten des Rechtsträgers selbst, die  im jeweiligen Stammregister eingetragen sind, Kenntnis jedenfalls ab deren Eintragung im  jeweiligen Stammregister anzunehmen ist, hätte die Bf binnen vier Wochen nach der am  1.12.2021 erfolgten Eintragung der KI Lexnor AG  als neuer Gesellschafterin der Bf im  Firmenbuch, dh bis spätestens 28.12.2021 eine Meldung gemäß § 5 WiEReG zu erstatten  gehabt, was jedoch nicht geschehen ist.

| Predicted | Gold |
|---|---|
| `KI Lexnor AG` | `KI Lexnor AG` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_112`)


Wenn der steuerliche Vertreter der Bf überdies ins Treffen führt, hinsichtlich der seit Ende  2021 an der Bf beteiligten ausländischen KI Lexnor AG  sei es, wie bei Auslandssachverhalten  üblich, sehr schwierig gewesen, die für die Meldung notwendigen Informationen zu erlangen,  so wird in keinster Weise dargelegt, worin diese Schwierigkeiten konkret bestanden haben  7 von 10 Seite 8 von 10

| Predicted | Gold |
|---|---|
| `KI Lexnor AG` | `KI Lexnor AG` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_58`)


Der Bf. übermittelte mit gleichem Schreiben weiters eine Kopie einer Auftragsbestätigung der  Deniz-Bank AG auf der lediglich der Stempel paid-bezahlt sowie das Datum 30.12.2015  aufscheint.

| Predicted | Gold |
|---|---|
| `Deniz-Bank AG` | `Deniz-Bank AG` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_173`)


Ab diesem Zeitpunkt bis  einschließlich 2019 erhielt die Bf. steuerfreie Gelder vom Arbeitsmarktservice und von der  WGKK, im Jahr 2017 zusätzlich einen Bezug von der Bundespensionskasse AG.

| Predicted | Gold |
|---|---|
| `Bundespensionskasse AG` | `Bundespensionskasse AG` |

**Missed by this rule (FN):**

- `WGKK` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_186`)


Dem Finanzamt wurden die im Jahr 2017 von der Bundespensionskasse AG, von der Wiener  Gebietskrankenkasse und vom Arbeitsmarktservice an die Bf. ausgezahlten Bezüge und im Jahr  2018 die vom Arbeitsmarktservice ausgezahlten Bezüge übermittelt.  Die Einkommensteuerbescheide 2017, 2018 und 2019 sind aktenkundig.

| Predicted | Gold |
|---|---|
| `Bundespensionskasse AG` | `Bundespensionskasse AG` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Wiener  Gebietskrankenkasse` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Geraldine Matuschefski  in der Beschwerdesache der Demircan Metall AG&  atypisch stille Gesellschaft, vertreten durch xx Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen  1.

| Predicted | Gold |
|---|---|
| `Demircan Metall AG` | `Demircan Metall AG` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Geraldine Matuschefski` (person)
- `xx Steuerberatung und Wirtschaftsprüfung` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_65`)


Ich gebe daher nochmals eine Beschreibung meiner Tätigkeiten im Rahmen des Gesamtkonzerns im Allgemeinen und meiner Tätigkeiten im Home Ofﬁce im Besonderen: Bei AG (AG) war ich im Rang eines weltweiten Vizepräsidenten - bei einem Konzern, welcher weltweit über 300.000 Beschäftigte hat und über 120 Milliarden Dollar Umsatz macht.

**False Positives:**

- `Bei AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_88`)


Da AG Russland in einer Region auch mit den anderen BRIC - Ländern verbunden war, reiste ich auch regelmäßig nach Brasilien, China und Indien (einmal im Jahr).

**False Positives:**

- `Da AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_28`)


Sonderprodukte (Ferienwegweiser, Wohin im Sommer) bzw. Spenderthemen  (Wirtschaftskammerseiten, Allerheiligen, Ostern, Weihnachten ...) in allen AG Produkten und  deren komplette Abwicklung der Kunden für den Ort Bezirk, Schnittstelle Kunde- AG,  Werbetechnische Beratung und Erstellung von Sonderprodukten (Sonderheft Ort1),  Baureportagen, Einforderung von säumigen Zahlungen von Kunden.

**False Positives:**

- `Schnittstelle Kunde- AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_48`)


Mit Schreiben vom 19.01.2017 erhob die Beschwerdeführerin das Rechtsmittel der  Beschwerde und führte dazu aus:  "Hiermit erhebe ich Beschwerde gegen die Einkommensteuerbescheide 2014 und 2015 vom 21.  Dezember 2016 und beantrage die Berücksichtigung der Vertreterpauschale für 2014 und 2015  wie im Antrag vom 15. Juni 2016 ersichtlich, da ich seit März 2014 ausschließlich im  Anzeigenverkauf des AG für die Ort AG tätig bin."

**False Positives:**

- `Ort AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_54`)


Aussendung von Serienbriefen/Mails für Sonderprodukte (Ferienwegweiser, Wohin im Sommer)  bzw. Sonderthemen (Wirtschaftskammerseiten, Allerheiligen, Ostern, Weihnachten....) in allen  AG Produkten und deren komplette Abwicklung der Kunden für den Ort Bezirk, Schnittstelle  Kunde- AG.

**False Positives:**

- `Schnittstelle  Kunde- AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_59`)


In der am 19.01.2017 eingebrachten Beschwerde gegen die  Einkommensteuerbescheide 2014 und 2015 vom 21.12.2016 beantragt die Abgabepflichtige  neuerlich die Berücksichtigung des Vertreterpauschales, da sie seit März 2014 ausschließlich im  Anzeigenverkauf des AG für die Ort AG tätig ist.

**False Positives:**

- `Ort AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_16`)


Er nutze das Fahrzeug als Dienstfahrzeug für seine Tätigkeit als  Regionaldirektor für Südbayern in einem abhängigen Arbeitsverhältnis bei der Firma AG in  d_Ort_2 an 6 Werktagen die Woche.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_165`)


Vorbringen in der Beschwerde nutzt der Beschwerdeführer das gegenständliche Fahrzeug „als  Dienstfahrzeug für meine Tätigkeit als Regionaldirektor für Südbayern in einem abhängigen  Arbeitsverhältnis bei der Firma AG in d_Ort_2 an 6 Werktagen die Woche.

**False Positives:**

- `Firma AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Firma SeeAutomotive AG` — partial — gold is substring of pred: `SeeAutomotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_51`)


Folgender Sachverhalt wird der Entscheidung zu Grunde gelegt:  Der Bf war im Streitjahr 2018 als Sales Project Manager bei der Firma SeeAutomotive AG Österreich  beschäftigt.

**False Positives:**

- `Firma SeeAutomotive AG` — partial — gold is substring of pred: `SeeAutomotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SeeAutomotive AG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_70`)


Obwohl den Bf im Streitjahr 2018 mehrere Dienstreisen in die USA geführt haben und er die in  Zusammenhang mit den Rechnungen Nr. 4, 14, 17, 18, 19 und 25 stehenden Ausgaben zum Teil  auch mit US-spezifischen Gegebenheiten bzw Erfordernissen erklärte hat, erscheint es dem  Bundesfinanzgericht nicht nachvollziehbar, dass die Firma SeeAutomotive AG Österreich ihren Dienstnehmer  im Streitjahr 2018 mehrere Mal dienstlich in die USA entsendet, ohne dem Bf die für seine  10 von 18 Seite 11 von 18

**False Positives:**

- `Firma SeeAutomotive AG` — partial — gold is substring of pred: `SeeAutomotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SeeAutomotive AG`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_73`)


Es erscheint wenig glaubhaft,  dass die Firma SeeAutomotive AG Österreich vom Bf erwartet, sich mit für die Dienstverrichtung in den USA  unverzichtbaren Arbeitsmitteln selbst auszustatten, wie zB einen mobilen Router samt  Antenne (Rechnung Nr. 4: 19,01 € + Rechnung Nr. 25: 114,60 €), ein Netzgerät zum Betreiben  von US-spezifischen Bauteilen (Rechnung Nr. 18: 79,99 €), Kabeln (Rechnung Nr. 17: 8,99 € +  Rechnung Nr. 19: 7,99 €) und einer Halterung für eine Kamera (Rechnung Nr. 14: 19,27 €).

**False Positives:**

- `Firma SeeAutomotive AG` — partial — gold is substring of pred: `SeeAutomotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SeeAutomotive AG`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_13`)


Mit Schreiben vom 08.07.2020 ersuchte das Bundesfinanzgericht die Österreichische Post AG  um Beantwortung diverser Fragen im Zusammenhang mit dem von der belangten Behörde in  Kopie übermittelten internationalen Rückschein;

**False Positives:**

- `Post AG` — partial — pred is substring of gold: `Österreichische Post AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Post AG`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_52`)


In letzterer sei eine Ausgabenposition „Geschäftsführerhaftung i.S.Traun-Handel AG–  Vergleich“ und der Betrag von EUR 8.000,- und eine Position „Rechtskosten Dr. E i.S. A AG“ von  EUR 339,09 ausgewiesen, ohne dass dabei ein Zusammenhang mit der Schilift GmbH  erkennbar sei.

**False Positives:**

- `Traun-Handel AG` — partial — pred is substring of gold: `i.S.Traun-Handel AG`
- `A AG` — partial — pred is substring of gold: `Dr. E i.S. A AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `i.S.Traun-Handel AG`(organisation)
- `Dr. E i.S. A AG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_60`)


Unter den  Ausgaben finden sich die Positionen „Geschäftsführerhaftung i.S.Traun-Handel AG– Vergleich….

**False Positives:**

- `Traun-Handel AG` — partial — pred is substring of gold: `i.S.Traun-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `i.S.Traun-Handel AG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_61`)


8.000,-„  und „Rechtskosten Dr. E i.S. A AG….

**False Positives:**

- `A AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_85`)


Unstrittig enthält jene Beilage, in der die Einkünfte aus selbständiger  Arbeit dargestellt werden, die beiden Ausgabenpositionen „Geschäftsführerhaftung i.S.Traun-Handel AG–  Vergleich … 8.000,-„ und „Rechtskosten Cubukcu & Hahlgans Automotive AG… 339.09“.

**False Positives:**

- `Traun-Handel AG` — partial — pred is substring of gold: `i.S.Traun-Handel AG`
- `Hahlgans Automotive AG` — partial — pred is substring of gold: `Cubukcu & Hahlgans Automotive AG…`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `i.S.Traun-Handel AG`(organisation)
- `Cubukcu & Hahlgans Automotive AG…`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, Magistratsabteilung 67 (MA 67) forderte die Zulassungs- besitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna, Fa.Dankwardt Wind AG  mit Schreiben vom 3. September 2019 gemäß § 2 Wiener Parkometergesetz 2006) auf,  der Behörde binnen zwei Wochen ab Zustellung des Schreibens Auskunft darüber zu erteilen,  wem das näher bezeichnete Fahrzeug am 5. Juli 2019 um 17:47 Uhr überlassen war, sodass es  in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Altgasse 25a, stand.

**False Positives:**

- `Dankwardt Wind AG` — partial — pred is substring of gold: `Fa.Dankwardt Wind AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Fa.Dankwardt Wind AG`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_15`)


Die Behörde habe gegen seine  Person als diejenige Person, welcher vom Zulassungsbesitzer Dankwardt Wind AG das Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna überlassen gewesen sei, kein Ersuchen auf  Auskunftserteilung gemäß § 2 Abs. 1 Parkometergesetz gerichtet, sondern unmittelbar ein  Verwaltungsstrafverfahren eingeleitet, ohne dass sie einen Hinweis gehabt habe, wer das  Fahrzeug am gegenständlichen Ort zur gegenständlichen Zeit abgestellt habe.

**False Positives:**

- `Zulassungsbesitzer Dankwardt Wind AG` — partial — gold is substring of pred: `Dankwardt Wind AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dankwardt Wind AG`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_170`)


Diese Glukose bezieht Bf. u.a. vom österreichischen Lieferanten ZWOP Cloud AG  Bf. hat mit ZWOP Cloud AG mehrjährige Lieferverträge abgeschlossen.

**False Positives:**

- `Lieferanten ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)
- `ZWOP Cloud AG`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_180`)


Sofern der EU-Kunde einen Abruf macht, informiert auch Bf.  den Lieferanten ZWOP Cloud AG und macht ihrerseits einen Abruf der bereits im Jahr 2014 vertraglich  gekauften Waren.

**False Positives:**

- `Lieferanten ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_187`)


Die belangte Behörde ist, der Betriebsprüfung folgend, zu dem Ergebnis gekommen, dass in  den hier strittigen Fällen jeweils ein Reihengeschäft ZWOP Cloud AG- Bf. - EU-Kunde vorliegt.

**False Positives:**

- `ZWOP Cloud AG` — partial — pred is substring of gold: `ZWOP Cloud AG-`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG-`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_189`)


wurde) wurden von der belangten Behörde dergestalt beurteilt, dass es sich bei der Lieferung ZWOP Cloud AG- Bf. um die bewegte Lieferung im Reihengeschäft gemäß § 3 Abs. 8 UStG handelt. Da Bf.  gegenüber ZWOP Cloud AG jedoch nicht mit einer UID-Nummer des Bestimmungslandes, sondern mit der  österreichischen UID-Nummer aufgetreten ist, wurde von der belangten Behörde ein sog.  fiktiver innergemeinschaftlicher Erwerb gem. Art 3 Abs. 8 zweiter Satz UStG ohne  Vorsteuerabzugsrecht festgesetzt, wogegen sich diese Beschwerde richtet.

**False Positives:**

- `Lieferung ZWOP Cloud AG` — positional overlap with gold: `ZWOP Cloud AG-`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG-`(organisation)
- `ZWOP Cloud AG`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_199`)


Selbst wenn man der Ansicht der belangten Behörde folgt, dass ein Reihengeschäft ZWOP Cloud AG- Bf. –  EU-Kunde vorliegt, ist u.E. die Lieferung ZWOP Cloud AG– Bf. aus nachstehenden Gründen als ruhende  Lieferung gemäß § 3 Abs. 7 UStG, bei der der Gegenstand der Lieferung nicht befördert oder  versendet wird, zu betrachten.

**False Positives:**

- `ZWOP Cloud AG` — partial — pred is substring of gold: `ZWOP Cloud AG-`
- `Lieferung ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG-`(organisation)
- `ZWOP Cloud AG`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_210`)


-  Mitteilung an Erstlieferant ZWOP Cloud AG war über den Verkauf an die EU-Kunden und den anschließenden Transport in einen  anderen EU-Mitgliedstaat informiert.

**False Positives:**

- `Erstlieferant ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_224`)


Daraus wurde geschlossen, dass  die Lieferung Bf. an den EU-Kunden und somit die Verschaffung der Verfügungsmacht erst im  Bestimmungsland erfolgt ist und somit die bewegte Lieferung der Lieferung ZWOP Cloud AG Bf.  zuzurechnen ist.

**False Positives:**

- `Lieferung ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_240`)


Folglich ist die Verfügungsmacht über die Ware bei der Lieferung ZWOP Cloud AG– Bf. bereits in  Österreich auf Bf. übergegangen.

**False Positives:**

- `Lieferung ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_243`)


Nach Maßgabe der Ausführungen der Generalanwältin ist somit klargestellt, dass das  Reihengeschäft ZWOP Cloud AG- Bf. - EU-Kunde auch bei Incoterm DDP korrekt abgewickelt wurde, weil  unter den konkreten Umständen der (innergemeinschaftliche) Transport der zweiten Lieferung  von Bf. an den EU-Kunden zuzurechnen ist.

**False Positives:**

- `ZWOP Cloud AG` — partial — pred is substring of gold: `ZWOP Cloud AG-`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG-`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_248`)


Wie unter Punkt 2.1. bereits ausgeführt, handelt es sich bei der Lieferung ZWOP Cloud AG- Bf. um eine  ruhende Lieferung in Österreich.

**False Positives:**

- `Lieferung ZWOP Cloud AG` — positional overlap with gold: `ZWOP Cloud AG-`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG-`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_305`)


In diesen Fällen ist von  einer bewegten Lieferung gem. § 3 Abs. 8 UStG zwischen ZWOP Cloud AG und Bf. auszugehen.ZWOP Cloud AG tätigt   daher in Österreich steuerbare und bei Vorliegen der Voraussetzungen gem. Art. 6 Abs. 1 i.V.m.  20 von 59 Seite 21 von 59

**False Positives:**

- `ZWOP Cloud AG` — similar text (different position): `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)
- `.ZWOP Cloud AG`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_437`)


3/21: CMR 80723344 an Ko. (Polska) vom 13.6.2016  Anlage 4:  4/1: Letter of confirmation for VAT purposes Sektkellerei vom 28.6.2018 (in englischer  Sprache)  4/2: Letter of confirmation for VAT purposes Fro. vom 22.6.2018 (in englischer Sprache)  4/3: Übersetzung des Schreibens Sektkellerei vom 28.6.2018 (v. 26.6.2020)  4/4: Letter of confirmation for VAT purposes Sektkellerei vom 28.6.2018 (in englischer  Sprache)  4/5: Übersetzung des Schreiben Fro. vom 22.6.2018 (v. 26.6.2020)  4/6: Letter of confirmation for VAT purposes Fro. vom 22.6.2018  Anlage 5:  5/1: Letter of confirmation for VAT purposes C. Supply Company AG vom 22.9.2020  5/2: Übersetzung des Bestätigungsschreibens für Mehrwertsteuerzwecke vom 22.9.2020 (v.  29.9.2020)  5/3: Letter of confirmation for VAT purposes C. Supply Company AG vom 22.9.2020  5/4: CMR 80477538 an S. (Estland) vom 12.10.2015  Mit hg. Mail vom 20.10.2020 wurden die übersandten Anlagen mit der Maßgabe beanstandet,  dass das von der Bf. gewünschte Beweisergebnis nicht hergestellt werden könne.

**False Positives:**

- `Supply Company AG` — partial — pred is substring of gold: `C. Supply Company AG`
- `Supply Company AG` — similar text (different position): `C. Supply Company AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `C. Supply Company AG`(organisation)
- `C. Supply Company AG`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_447`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Eine österreichische Gesellschaft ZWOP Cloud AG (A) verkaufte an die Bf.(B), die als belgisches  Unternehmen sowohl über eine belgische als auch über eine österreichische Umsatzsteuer- Identifikationsnummer verfügte, Waren, die diese als mittleres Unternehmen (B) an EU- Gesellschaften (C) weiterveräußerte.

**False Positives:**

- `Gesellschaft ZWOP Cloud AG` — partial — gold is substring of pred: `ZWOP Cloud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ZWOP Cloud AG`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_4`)


Das damals zuständige Finanzamt Salzburg – Stadt erließ gegenüber dem  Beschwerdeführer (kurz: Bf.) für die Jahre 2015 bis 2018 am 6.11.2020  Einkommensteuerbescheide, in denen neben nichtselbständigen Einkünften auch sonstige  Einkünfte festgesetzt wurden mit der Begründung, es handle sich um ausländische Einkünfte  aus einer Lebensversicherungs AG.

**False Positives:**

- `Lebensversicherungs AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Salzburg`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_16`)


Er hat von Herrn AG lediglich ein  Entgelt von insgesamt EUR 2.506,82 erhalten.

**False Positives:**

- `Herrn AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_26`)


abzüglich Tankbelegen an Herrn AG abgegeben, 45% durfte der Bf. gleich behalten.

**False Positives:**

- `Herrn AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/142266.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142266.1_77`)


Aus den vom Beschwerdeführer mit Schreiben vom 24.7.2023 vorgelegten Unterlagen ist  ersichtlich, dass er im Jahr 2021 insgesamt EUR 45,60 an die Gränz + Hamele Pharma AG bezahlt hat (Buchungen am  Girokonto: EUR 14,90 – 25.1.2021;

**False Positives:**

- `Hamele Pharma AG` — partial — pred is substring of gold: `Gränz + Hamele Pharma AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gränz + Hamele Pharma AG`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/142266.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142266.1_80`)


Es  erscheint glaubwürdig, dass es sich dabei um Mobilfunkkosten handelt.   Weiter ist ersichtlich, dass er insgesamt EUR 99,64 an die Gränz + Hamele Pharma AG bezahlt hat (Buchungen am  Girokonto: EUR 32,90 – 11.1.2021;

**False Positives:**

- `Hamele Pharma AG` — partial — pred is substring of gold: `Gränz + Hamele Pharma AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gränz + Hamele Pharma AG`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_5`)


Gegen diesen Bescheid brachte der Beschwerdeführer Jason Oberbüscher  am 11. April 2023 das  Rechtsmittel der Beschwerde ein und führte begründend aus, dass seine   „unter Pkt. 2 angeführte Einkünfte von der ‚FA Linz  RS AG‘ keine Einkünfte aus Lohn- oder  selbstständiger Arbeit seien.

**False Positives:**

- `FA Linz  RS AG` — positional overlap with gold: `‚FA Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jason Oberbüscher`(person)
- `‚FA Linz`(organisation)

</details>

---

## `german_company_gmbh` 🏆

**F1:** 0.135 | **Precision:** 0.448 | **Recall:** 0.080  

**Format:** `regex`  
**Rule ID:** `8f8e291f`  
**Description:**
Matches GmbH companies, requiring a valid name start (letter or 'Fa.') and excluding common articles like 'Die' or 'Der'.

**Content:**
```
\b(?<!\w)(?:(?:Fa\.|[A-Z][a-zA-Z0-9\-+&]*(?:\s+[A-Z][a-zA-Z0-9\-+&]*)*)\s+GmbH(?:\s+&\s+CO\s+KG)?)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.448 | 0.080 | 0.135 | 897 | 402 | 495 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 402 | 495 | 4641 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KPMG Alpen-Treuhand GmbH` | `KPMG Alpen-Treuhand GmbH` |

**Missed by this rule (FN):**

- `Dr.in Dietlind Mahlstädt` (person)
- `Kai Pipers` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `Finanzamt Tirol Ost` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Sera Trust GmbH` | `Sera Trust GmbH` |

**Missed by this rule (FN):**

- `Dr. Anna Radschek` (person)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `MITTEREGGER Steuerberatungs GmbH` | `MITTEREGGER Steuerberatungs GmbH` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Sieglinde Kießerling` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1.) Aufgrund von Erhebungen der Finanzpolizei (Kontrollmitteilung vom 18.1.2010) wurde ua.  aufgrund einer Anhaltung (im September 2009) festgestellt, dass das von Josefine Frikel (=  Beschwerdeführer, Bf), österreichischer Staatsbürger, im Inland gelenkte Fahrzeug der Marke  Audi A6 AVANT mit dem deutschen Kennzeichen (Kz) W1, zugelassen auf den deutschen  Staatsbürger A, von diesem der Verwaldgart GmbH bzw. dem Bf als Geschäftsführer seit 1.11.2008 zur  Nutzung zur Verfügung gestellt worden sei;

| Predicted | Gold |
|---|---|
| `Verwaldgart GmbH` | `Verwaldgart GmbH` |

**Missed by this rule (FN):**

- `Finanzpolizei` (organisation)
- `Josefine Frikel` (person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_14`)


Am 2.8.2010 wurde mit dem Bf eine Niederschrift folgenden Inhaltes aufgenommen:  "Mein Hauptwohnsitz besteht seit 1991 in A/Adr1, wo ich auch das Y-Hotel unter der Verwaldgart GmbH  betreibe.

| Predicted | Gold |
|---|---|
| `Verwaldgart GmbH` | `Verwaldgart GmbH` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_16`)


D/XX, die VWWJ IT GmbH mit selber  Adresse.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_28`)


Dabei wurde  das Kfz auch bei mir am Y-Hotel in A/Adr1 abgestellt und nahezu ausschließlich für die VWWJ IT GmbH  verwendet.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_34`)


Service wird in  Deutschland durchgeführt, betankt wird er je nach Bedarf mit Abrechnung über die VWWJ IT GmbH  Weiters habe ich keine Angaben zu machen.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_38`)


die Zulassung auf die VWWJ IT GmbH in D/XX am 3.12.2009, Kz W2;  - Prospekt zum Hotel Y-Hotel in A/Adr1, betrieben von der Verwaldgart GmbH  mit      dem Anbot ua. von xxx-Anwendungen;  - Urkunde des dten.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |
| `Verwaldgart GmbH` | `Verwaldgart GmbH` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_39`)


Notars über die GmbH-Gründung am 9.10.2007 samt      Gesellschaftsvertrag, woraus ua. hervorkommt:     Der Bf und A errichten die VWWJ IT GmbH    mit Sitz in D/XX, je zur Hälfte übernommenes Stammkapital € 25.000;      zum Geschäftsführer wird A bestellt. Unternehmensgegenstand ist      neben Liegenschaftserwerb- und –verwaltung ua. die Vermittlung und der Handel     mit Waren aus dem Bereich medica/wellness.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_42`)


Audi A6 v. 8.10.2007 an      A, Kaufpreis netto € 45.378,15;  - zwei deutsche Zulassungsbescheinigungen: Zulassung mit Kz W1 auf      A am 9.10.2007, mit Kz W2 auf die VWWJ IT GmbH am 3.12.2009;  - ein Schreiben des A v. 11.8.2011, worin dieser als GF bestätigt,      dass die GmbH seit Mitte 2009 operativ tätig sei, Geschäftsbeziehungen unterhalte     und mehrere Mitarbeiter in Teil- und Vollzeit beschäftige.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_66`)


5. Anlagenverzeichnis und  Überschussrechnung (Bilanz) der VWWJ IT GmbH der Jahre 2007 bis 2009.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_68`)


In der Folge wurde über das – anstelle seines persönlichen Erscheinens wegen der  zurückzulegenden Strecke von ca. 700 km - mit A am 23.11.2010 geführte Telefonat ein  Protokoll angefertigt, dieses ihm zur Stellungnahme und allfälligen Berichtigung übermittelt  und mit mail am 26.11.2010 teils korrigiert mit folgendem Inhalt dem Finanzamt retourniert:  "… Ich bin Geschäftsführer der VWWJ IT GmbH mit Sitz in D/XX.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_76`)


Die Kunden der VWWJ IT GmbH sind zu 40 % in Österreich  angesiedelt, der Rest im Süddeutschen bzw. Südtiroler Raum.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_90`)


3. laut eigenen Angaben das Fahrzeug erst mit Dezember 2009 in das Betriebsvermögen der VWWJ IT GmbH aufgenommen worden und zuvor auf A angemeldet gewesen sei, welche Angaben  mangels mehrfach angefordeter, jedoch nicht vorgelegter Unterlagen (Bilanz,  Anlagenverzeichnis, Fahrtenbuch etc.) ebenso nicht überprüft werden konnten wie der  5 von 14 Seite 6 von 14

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_91`)


Umstand, ob diese Firma überhaupt operativ tätig gewesen sei, sowie   4. das Fahrzeug lt. Aussage des A (lt. Aktenvermerk v. 26.11.2010) zwar anfangs auf ihn  angemeldet und in die Firma eingebracht, aber vom Bf nach Österreich verbracht worden sei,  sich dann des Öfteren am inländischen Wohnsitz des Bf und erst ab 2010 im Betriebsvermögen  der VWWJ IT GmbH befunden habe,   sei davon auszugehen, dass aufgrund des Hauptwohnsitzes/Mittelpunktes der  Lebensinteressen des Bf das Fahrzeug seinen dauernden Standort in Österreich habe.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_99`)


An diesem Standort betreibt er als  Geschäftsführer der Verwaldgart GmbH ein Hotel (Niederschrift v. 2.8.2010;

| Predicted | Gold |
|---|---|
| `Verwaldgart GmbH` | `Verwaldgart GmbH` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_102`)


Am 9.10.2007 haben der Bf und A, deutscher Staatsbürger, die VWWJ IT GmbH mit dem Sitz in D/XX  gegründet;

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_112`)


Am 3.12.2009 erfolgte die Zulassung auf die VWWJ IT GmbH in D/XX mit  dem Kennzeichen W2 (siehe deutsche Zulassungsbescheinigungen).

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_121`)


Gegenständliches Fahrzeug scheint – wenn überhaupt – lt. Aussage des GF A  (erst) seit 2010 im Anlagevermögen der VWWJ IT GmbH auf.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_125`)


Bei den - neben obigen Sachverhaltsfeststellungen - vom Bf gemachten Angaben dahin, dass er  das Fahrzeug weitgehend beruflich verwendet habe und eine Privatverwendung  ausgeschlossen sei, dass er im Rahmen des Geschäftsbetriebes der VWWJ IT GmbH wöchentlich  mehrere Tage zwecks Produktverkauf in Deutschland und in Italien unterwegs gewesen sei  sowie Fahrzeugservice und Betankung in Deutschland bzw. mit Abrechnung über die Fa.VWWJ IT GmbH stattgefunden habe, handelt es sich um gänzlich unsubstantiierte, dh. nicht  nachgewiesene und teils auch widersprüchlich aufgestellte Behauptungen.

| Predicted | Gold |
|---|---|
| `VWWJ IT GmbH` | `VWWJ IT GmbH` |

**Missed by this rule (FN):**

- `Fa.VWWJ IT GmbH` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_4`)


Die Gesellschafter der Bf. - die Pflege Nexwerkwald GmbH und N.N. - sind jeweils mit einer Stammeinlage von  40.000 € an der Bf. beteiligt.

| Predicted | Gold |
|---|---|
| `Pflege Nexwerkwald GmbH` | `Pflege Nexwerkwald GmbH` |

**Missed by this rule (FN):**

- `N.N.` (person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_14`)


Seit 2001 hält die Bf. 100% der  Geschäftsanteile an der Nieder Waldbach GmbH   Die Gesellschafter der Bf. sind die Fa.Adeler&Glasener Textil GmbH und V.A. (=V.A.).

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Missed by this rule (FN):**

- `Fa.Adeler&Glasener Textil GmbH` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_21`)


Zu den Fleischlieferanten der Bf. zählten die Lemost-Handel GmbH unter der Geschäftsführung von E.St.  sowie die Dorfleitner+Ternis Versicherung GmbH unter der Geschäftsführung von K.F.St..  Bericht gemäß § 150 BAO vom 21.10.2009  Unter Tz.1ff.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_39`)


Bei der Verrechnung von Fleisch und Wein mit der Nieder Waldbach GmbH sei trotz des im Zuge der diversen  Besprechungen erklärten Verkaufs küchenfertiger Produkte (zugeschnitten, geklopft, paniert)  nur das Fleisch(gewicht) im gesamten Prüfungszeitraum weiterverrechnet worden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_50`)


*) (Gegen)Kalkulation - 25% Abschnitt: Die Kalkulation der Bf. berücksichtige einen Abschnitt  von 25% bei Schnitzelfleisch [Laut Bestätigung des Geschäftsführers der Lemost-Handel GmbH könnten bis  zu 25% Abfälle beim küchenfertigen Zuputzen von Karree Rose entstehen].

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_54`)


Ein 16%-Abschnitt trotz Entfernens von Fetträndern etc.  lasse den Schluss auf den Gefälligkeitscharakter der Bestätigung des Geschäftsführers der Lemost-Handel GmbH zu. Das dem "Schaukochen" zugrundegelegene Fleisch habe mangels Etikettierung nicht  eindeutig einem Lieferanten zugeordnet werden können und sei schon einige Tage alt  gewesen.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_57`)


*) Fleischqualität beim Schaukochen: Erhebungsfeststellungen bei der Lemost-Handel GmbH zufolge habe  es sich bei dem für das Schaukochen extra angelieferten Fleisch laut Auskunft einer  Angestellten um altes Fleisch, laut Auskunft des Lemost-Handel GmbH Geschäftsführers um eine Ware ohne  Wert gehandelt. Befragt nach dem Grund für die Bestellung von Fleisch mit so hohem  Fettgehalt, was dann weggeschnitten werde, obwohl wie beim Testkauf bestätigt, Fleisch ohne  Beinkette und mit geringem Fettgehalt geliefert werde, habe der steuerliche Vertreter erklärt:  Fleisch mit Fettrand und Beinkette sei viel saftiger.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_67`)


Laut Aussage des Geschäftsführers der Lemost-Handel GmbH vom 24.06.2008 sei Produktefleisch, Artikel  Nr.2190, bis Anfang 2006 geliefert worden.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_69`)


Die Untersuchung der A-Anstalt sei aufgrund der  Bestätigung des Geschäftsführers der Lemost-Handel GmbH  wonach Artikel 2190 dem durch die A-Anstalt  untersuchten Fleisch Artikel 2194 entspreche, relevant.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_71`)


Die Betriebsprüfung habe bei dieser Kalkulation das bei der Betriebsbesichtigung vorgezeigte  Fleisch (Abschnitt 16%) trotz der Aussage des Geschäftsführers der Lemost-Handel GmbH vom 24.06.2008,  die eine Berücksichtigung von nur 6% Abschnitt rechtfertigen würde, berücksichtigt.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_72`)


Aufgrund einer weiteren Aussage des Geschäftsführers der Dorfleitner+Ternis Versicherung GmbH betreffend Rückkauf von  Fleischabschnitten seien die zurückgenommenen Abschnitte für das Wirtschaftsjahr 2006 aus  den vorgelegten elektronischen Grundaufzeichnungen ermittelt und dem Gesamtverbrauch  Schnitzelfleisch gegenübergestellt worden.

| Predicted | Gold |
|---|---|
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_74`)


Mit der nachfolgenden Übersicht werden die nach Aussage des Geschäftsführers der Lemost-Handel GmbH  ab dem Jahr 2006 gelieferten, anderen Fleischprodukte samt Angabe des  Produkteinkaufspreises dargestellt:     Im Anschluss an die Übersicht wurde der Grund für eine verbesserte Fleischqualität zum  annähernd denselben Preis bzw. sogar billiger als unverständlich bezeichnet.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_88`)


Unglaubwürdigkeit des dem Schreiben vom 23.4.2009 beigelegten Gutachtens der C-Anstalt:  Laut den Aussagen laut Gutachten sei der Kauf für die Probe [Entnahme von zwei original  verpackten Stücken Schweinskarree Rose aus dem Lager bzw. zwei Stück Schweinskarree Rose  ohne Beinkette vom Arbeitsvorrat des zuständigen Mitarbeiters] zwischen 8:30 bis 12:30 Uhr  am 11.02.2009 bei der Lemost-Handel GmbH in A-Dorf gewesen.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_116`)


Betrieb B-Platz: Nach Erwerb der Anteile an der Nieder Waldbach GmbH im Insolvenzverfahren im Herbst  2001 habe die Bf. die Nieder Waldbach GmbH aus Haftungsgründen als 100%ige Tochtergesellschaft für den  Zeitraum von drei Jahren weitergeführt.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_122`)


Den Bilanzdaten für die Nieder Waldbach GmbH zufolge seien die Rohaufschläge der Küchen von Jahr zu Jahr  linear mit zunehmendem Fleischkonsum gestiegen, während davon das Ergebnis W- Platz negativ beeinträchtigt worden wäre.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_123`)


Trotz Hinweis auf diesen Umstand sei das Ersuchen  der Prüfungsausdehnung auf die Nieder Waldbach GmbH im Zuge des Prüfungsverfahrens abgelehnt worden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_142`)


Es liege kein repräsentativer Zeitablauf zwischen dem Verpacken bei der Lemost-Handel GmbH  der  Entnahme aus dem Lager und der sofortigen Aufarbeitung durch die A-Anstalt vor.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_143`)


Mit der Lieferung des von der Lemost-Handel GmbH am Montag aufgearbeiteten Fleisches bei der Bf. im  Laufe des Dienstagvormittag sei das Fleisch schon zwischen zwölf und vierzehn Stunden  verpackt.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_155`)


eine Verrechnung wie bei der Nieder Waldbach GmbH fehle.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_163`)


*) Wirtschaftliche Betrachtungsweise der Betriebe der Bf. und Nieder Waldbach GmbH als einheitlicher  Betrieb: Die Betriebe W-Platz und Nieder Waldbach GmbH seien zwei getrennt geführte GmbHs mit  getrennten Wareneinkauf und getrennter Umsatzermittlung.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_165`)


Eine Veranlassung zur Prüfung der Nieder Waldbach GmbH nur wegen der Verrechnung Produkte und Salat im  Betrieb bestehe nicht.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_166`)


Im Rahmen des inneren Betriebsvergleichs bei der Nieder Waldbach GmbH wären  branchenübliche, beim W-Platz  unübliche Aufschläge festgestellt worden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_172`)


Nach Akteneinsicht habe der steuerliche  Vertreter eine Bestätigung der Lemost-Handel GmbH betreffend Lieferung wieder eines anderen Fleisches  mit besseren Fleischzuschnitt ab Anfang 2006 vorgelegt.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_179`)


Die Lieferung der Lemost-Handel GmbH von drei Tage alten Fleisch (Verpackungsdatum: 7.01.2008) vor   der Betriebsbesichtigung (siehe Lieferschein v. 9.01.2008): Die Betriebsprüfung bestritt,  behauptet zu haben, dass es sich hier um minderwertiges Fleisch handle, und verwies auf eine  Angestellte der Lemost-Handel GmbH  die dieses Fleisch als alt bezeichnet hätte, bzw. auf den  Geschäftsführer der Lemost-Handel GmbH  demnach dieses Fleisch eine Ware ohne Wert sei.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_217`)


(Pkt. B) Schreiben der Bf. vom 15.7.2010 zum Schreiben des FA vom 20.04.2010  Für die Ansicht der Bf., wonach die beiden Betriebe wirtschaftlich als einheitlicher Betrieb  anzusehen wären, wurde u.a. ins Treffen geführt, dass die Behörde diese Tatsache aufgrund  der Verrechnungen zwischen der Bf. und der Nieder Waldbach GmbH nicht ignorieren könne.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_255`)


+) Verrechnung mit B-GmbH: Die Produkte wären fertig zugeschnitten an die Nieder Waldbach GmbH geliefert  worden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_256`)


W-Platz hätte der Nieder Waldbach GmbH nur das Nettofleisch ohne Berücksichtigung des Abschnitts  verrechnet.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_257`)


Bei einer Lieferung vom W-Platz an die Nieder Waldbach GmbH von hundert küchenfertigen  Produkten mit einem Gewicht von rund 250g/Produkt seien der GmbH 25 kg Fleisch in  Rechnung gestellt worden, ohne dass dabei berücksichtigt worden wäre, dass der Standort W- Platz für eine derartige Lieferung wegen der Zuschneidung der Produkte am W-Platz weitaus  mehr Fleisch benötigt habe.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_259`)


Der Fleischabschnitt sei am W-Platz hängen geblieben, ohne der Nieder Waldbach GmbH zugeordnet zu  werden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_261`)


Diesem Missverhältnis zwischen dem Umsatz  der Nieder Waldbach GmbH und dem gestiegenen, aber nicht weiterverrechneten Abschnitt am W-Platz habe  die Bf. keine Beachtung geschenkt, da sie nur den Gewinn insgesamt betrachtet und die  einzelnen Standorte und Gesellschaften als ein Unternehmen angesehen hätte.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_262`)


Angesichts der Nieder Waldbach GmbH als eine Tochtergesellschaft mit identem Betätigungsfeld [die  mittlerweile in die Bf. verschmolzen worden sei] sei es somit nicht nur aus  betriebswirtschaftlicher Sicht naheliegend gewesen, den Fleischeinkauf zentral über die Bf.  abzuwickeln und die Nieder Waldbach GmbH mit den entsprechenden Kosten anteilig zu belasten.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_263`)


Die anteilige Kostenbelastung sei aus dem Umsatz der Nieder Waldbach GmbH abgeleitet worden, da jede  andere Berechnungsmethode zu einem unverhältnismäßigen Verwaltungsaufwand geführt  hätte.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_273`)


Zu Tz.3 PB Kalkulationsdifferenzen: Die Ursache für das Absinken der Aufschläge sei in der  Übernahme der Nieder Waldbach GmbH im Jahr 2002 und der damit verbundenen Weiterbelastung der  Küchenwaren ohne Gewinnaufschlag gelegen.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_274`)


Durch die Legitimität des Verzichts auf einen  solchen Gewinnaufschlag bedingt (die Nieder Waldbach GmbH hätte die Ware auch direkt von den Lieferanten  beziehen können) sei das vorliegende Modell aus Gründen der Kostenökonomie gewählt  worden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_275`)


Das konstante Absinken der Aufschläge ergebe sich aus dem konstanten  Umsatzwachstum der Nieder Waldbach GmbH  Die Bf. habe diesen Umstand durch entsprechendes  Zahlenmaterial nachgewiesen.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_276`)


Dem Prüfersuchen betreffend die Nieder Waldbach GmbH sei das Finanzamt  nicht nachgekommen.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_278`)


Hinsichtlich der 1. Kalkulation bemängelte der steuerliche Vertreter im Wesentlichen, dass der  abgabenbehördlichen Berechnung für die Jahre 2003 - 2005 mehr Gewicht als der vorgelegten  ordnungsgemäßen doppelten Buchhaltung des Unternehmens beigemessen werde, obwohl die  ursprüngliche Berechnung des Finanzamts keinerlei Abschläge für Schwund, Fleischverluste,  Wasserverluste enthalte und auch keine Herausrechnung der für die Nieder Waldbach GmbH eingekauften  Küchenwaren erfolgt sei.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_280`)


Im  Bericht werde der Erwerb der Nieder Waldbach GmbH zu diesem Zeitpunkt samt den besagten Verrechnungen  in diesem Zeitraum ignoriert.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_288`)


Bestätigung des Geschäftsführers der Lemost-Handel GmbH& Verkaufsware der C-GmbH: Die Abschnitte  des Schaukochens hätten gemäß den vorliegenden Aufzeichnungen rund 20% und nicht 16%  ausgemacht.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_298`)


Warenqualität: Der Geschäftsführer der Lemost-Handel GmbH  dessen protokollierten Zeugenangaben vom  24.06.2008 zufolge ein Produkt ohne Beinkette erst ab 2006 geliefert worden sei, bestätige  den Hinweis des steuerlichen Vertreters betreffend die Verwendung einer anderen Sorte  Fleisch im Prüfungszeitraum.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_306`)


Die Lieferungen der Dorfleitner+Ternis Versicherung GmbH seien jedoch marginal gewesen.

| Predicted | Gold |
|---|---|
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_308`)


Die vom Geschäftsführer der Dorfleitner+Ternis Versicherung GmbH auf vorgehaltene Fotos des Prüfers hinauf wortwörtlich  protokollierte Zeugenaussage "Nein, einen so hohen Fettanteil hatten meine Produkte nie."  werde von der Prüfung unrichtig wiedergegeben.

| Predicted | Gold |
|---|---|
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_310`)


der Dorfleitner+Ternis Versicherung GmbH laut Prüfbericht, wonach derartig minderwertiges Fleisch wie im Gutachten ...  abgebildet niemals geliefert worden wäre, heiße, dass dieser Zeugenaussage zufolge das  gezeigte Fleischstück der Konkurrenz einen höheren Fettanteil als das von ihm gelieferte  (welches aber auch preislich über jenem der Lemost-Handel GmbH gelegen sei) habe.

| Predicted | Gold |
|---|---|
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_311`)


Aus dem Bericht gehe nicht hervor, dass es sich bei dem für das Gutachten verwendeten  Fleisch um Fleisch der Lemost-Handel GmbH handle.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_312`)


Aus der Zeugenaussage des Geschäftsführers der Dorfleitner+Ternis Versicherung GmbH (Gf. eines Lieferanten, dessen Fleisch gar nicht untersucht worden sei), das Gutachten  als eine Fälschung zu konstruieren, widerspreche dem Akteninhalt.  Die Behörde sei auf den Kern der Aussage des Geschäftsführers der Dorfleitner+Ternis Versicherung GmbH  nämlich dass im  Prüfzeitraum auch von der Dorfleitner+Ternis Versicherung GmbH eine, was den Zuschnitt anbelangt, mindere Fleischsorte  als heute geliefert worden sei, nicht eingegangen.

| Predicted | Gold |
|---|---|
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_313`)


Angaben des Geschäftsführers der Lemost-Handel GmbH betreffend geänderte Artikelnummern in  Zusammenhang mit der Untersuchung der A-Anstalt: Der steuerliche Vertreter verneinte,  dass der Geschäftsführer der Lemost-Handel GmbH die Entsprechung des Artikel 2190 dem untersuchten  Fleisch der A-Anstalt bestätigt hätte, mit der Begründung, dass dieser das von der A-Anstalt  untersuchte Fleisch ebensowenig wie die Bf. oder dessen steuerliche Vertretung jemals  gesehen habe.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_314`)


In der Zeugeneinvernahme sei dem Geschäftsführer der Lemost-Handel GmbH lediglich eine  Agrarmarktbeschreibung vorgehalten worden.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_316`)


Angaben des Geschäftsführers der Dorfleitner+Ternis Versicherung GmbH zu Warenrückkäufen/zum errechneten Abschnitt  von 11,45 % im Prüfbericht: Der steuerliche Vertreter sprach sich gegen eine Gleichsetzung  des Rückkaufs mit dem Abschnitt aus, weil -abgesehen von erheblichen Fleischsaftverlusten-  nicht angenommen werden könne, dass jeder einzelne Abschnitt tatsächlich zurückgekauft  worden sei.

| Predicted | Gold |
|---|---|
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_317`)


Die Lieferungen der Dorfleitner+Ternis Versicherung GmbH hätten lediglich einen geringen Teil der  Gesamtlieferungen ausgemacht und seien auch preislich über jenen der Lemost-Handel GmbH gelegen.

| Predicted | Gold |
|---|---|
| `Dorfleitner+Ternis Versicherung GmbH` | `Dorfleitner+Ternis Versicherung GmbH` |
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_319`)


Die  Bemühungen um eine Verbesserung der Fleischqualität seien erheblich durch den gestiegenen  Umsatz der Bf. bzw. der Nieder Waldbach GmbH unterstützt worden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_325`)


Bericht ziehe nicht in Betracht, dass die Differenzen bei der Kalkulation des Finanzamts aus  dieser Verrechnung mit der Nieder Waldbach GmbH sowie teilweise auch aus einem höheren Abschnitt,  teilweise womöglich aus anderen Gründen (insbesondere einem höheren Schwund durch  Personalmalversationen) herrühren könnten.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_337`)


Finanzamt in Form der vier Stunden langen Suche bei der Lemost-Handel GmbH nach jenen Fleischstücken  mit den größten Fettgehalt zu erkennen.

| Predicted | Gold |
|---|---|
| `Lemost-Handel GmbH` | `Lemost-Handel GmbH` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_358`)


Schätzungsbefugnis: Der steuerliche Vertreter verneinte die Existenz von zu einer Schätzung  berechtigenden Mängel in den Grundaufzeichnungen, leitete die Kalkulationsdifferenzen aus  der fehlenden Berücksichtigung der Lieferungen an die Nieder Waldbach GmbH ab 2002, den  innerbetrieblichen Warenbewegungen zwischen G-Platz und W-Platz sowie aus der  Nichtanerkennung des Gutachtens der C-Anstalt mit dem dort festgestellten Fleischabschnitt/  Saftverlust ab und bestritt, dass diese beiden Ursachen in Widerspruch zueinander stünden.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_359`)


Auf die Ignorierung der Ergebnisse des Gutachtens der C-Anstalt und die Ablehnung der  beantragten Prüfung der Nieder Waldbach GmbH wurde verwiesen.

| Predicted | Gold |
|---|---|
| `Nieder Waldbach GmbH` | `Nieder Waldbach GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_6`)


Die  Beschwerdeführerin, eine bei der AG GmbH angestellte Anzeigenverkäuferin, beantragte die  Berufsgruppenpauschale für VertreterInnen für den Zeitraum 03.03.2014 bis 31.12.2014 und  01.01.2015 bis 31.12.2015.

**False Positives:**

- `AG GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_10`)


Mit Schreiben vom 28.11.2016 legte die Beschwerdeführerin, eine beim AG GmbH angestellte  Anzeigenverkäuferin, eine Bestätigung ihres Dienstgebers vor, mit dem folgenden Wortlaut:   "Betreff: Bestätigung: Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung zu § 17 Abs 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig überwiegend  ihre Tätigkeit, als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom 01.01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

**False Positives:**

- `AG GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hainig`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_112`)


Mit Schreiben vom 31.03.2020 beantwortete die Beschwerdeführerin den Vorhalt des  Bundesfinanzgerichts und führte dazu aus wie folgt:   "Die Nebentätigkeit "Erstellung von Werbetexten“ im Zuge meiner Tätigkeit im Bereich  Mediaberatung als Angestellte für das AG Druck und Verlags GmbH umfasste maximal 20  Arbeitsstunden pro Kalenderjahr!

**False Positives:**

- `Verlags GmbH` — partial — pred is substring of gold: `AG Druck und Verlags GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)
- `AG Druck und Verlags GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

**False Positives:**

- `Steuerberatung GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Reneé Dreyssig`(person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich`(address)
- `Mag. Manfred Frühwirth`(person)
- `Finanzamtes Linz`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_16`)


Im wiederaufgenommenen Verfahren vom 31. Mai 2017 wurde der  Körperschaftsteuerbescheid 2011 der Klaaßens Versand GmbH mit folgender Begründung abgeändert:  Bei Einbringung des Einzelunternehmens des Alleingesellschafters in die Bf. zum 31. Dezember  2004 wurde in der unternehmensrechtlichen Bilanz ein Firmenwert iHv 514.229,34 € aktiviert,  der in weiterer Folge über 10 Jahre abgeschrieben wurde.

**False Positives:**

- `Versand GmbH` — partial — pred is substring of gold: `Klaaßens Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klaaßens Versand GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_62`)


lediglich für 2 Monate zusteht, hatte er keinen Anspruch auf Gewährung des  Kinderfreibetrages für W.  Die dem Bf. für seine Kinder zustehenden Ansprüche ermitteln sich wie folgt:  J:   - Kinderfreibetrag für ein haushaltszugehöriges Kind € 440,-  - Kinderbetreuungskosten (a.g. Belastung) € 1.560,-  W:  - Unterhaltsabsetzbetrag (2 Monate): € 58,40  Die Höhe der Abgabe beträgt:      2018    €  Einkünfte aus nichtselbständiger Arbeit    BUAK 2.213,15   A-Bau GmbH 15.278,78   Kontrollrechnung § 3 Abs. 2 EStG 3.578,58   Pauschbetrag f. Werbungkosten -132,00 20.938,51  Gesamtbetrag der Einkünfte  20.938,51

**False Positives:**

- `A-Bau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Astoria Stb GmbH` — partial — pred is substring of gold: `Astoria Stb GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Univ.-Prof.in Ada Schaeferlein`(person)
- `Leroy Sitterle`(person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich`(address)
- `Astoria Stb GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_8`)


- weitere ZEVIS-Abfrage:     Demnach wurde selbiges Fahrzeug am 3.12.2009 unter dem deutschen      Kennzeichen W2 auf die Firma VWWJ IT GmbH     mit Sitz in D/XX zugelassen;

**False Positives:**

- `Firma VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_70`)


Die VWWJ IT GmbH wurde 2008 gegründet.

**False Positives:**

- `Die VWWJ IT GmbH` — partial — gold is substring of pred: `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_79`)


Am 3.12.2009 wurde dann das KFZ auf das Kennzeichen W2 umgemeldet (auf die Fa.VWWJ IT GmbH  und scheint seit 2010 im Anlagevermögen der Firma auf.

**False Positives:**

- `VWWJ IT GmbH` — partial — pred is substring of gold: `Fa.VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.VWWJ IT GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_120`)


A verfügt über einen PrivatPkw, die Fa.VWWJ IT GmbH daneben über ein Poolfahrzeug als  Firmenfahrzeug.

**False Positives:**

- `VWWJ IT GmbH` — partial — pred is substring of gold: `Fa.VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.VWWJ IT GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_125`)


Bei den - neben obigen Sachverhaltsfeststellungen - vom Bf gemachten Angaben dahin, dass er  das Fahrzeug weitgehend beruflich verwendet habe und eine Privatverwendung  ausgeschlossen sei, dass er im Rahmen des Geschäftsbetriebes der VWWJ IT GmbH wöchentlich  mehrere Tage zwecks Produktverkauf in Deutschland und in Italien unterwegs gewesen sei  sowie Fahrzeugservice und Betankung in Deutschland bzw. mit Abrechnung über die Fa.VWWJ IT GmbH stattgefunden habe, handelt es sich um gänzlich unsubstantiierte, dh. nicht  nachgewiesene und teils auch widersprüchlich aufgestellte Behauptungen.

**False Positives:**

- `VWWJ IT GmbH` — similar text (different position): `VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VWWJ IT GmbH`(organisation)
- `Fa.VWWJ IT GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_132`)


Im Übrigen kann mangels Beibringung mehrfach vom Finanzamt angeforderter und zugesagter  Unterlagen – nämlich insbesondere eines ordnungsgemäß geführten Fahrtenbuches, von  Überschussrechnungen/Bilanzen der betreffenden Jahre sowie eines Anlagenverzeichnisses  der Fa.VWWJ IT GmbH– nicht einmal ansatzweise verifiziert werden, ob dieses Unternehmen  überhaupt operativ tätig war (lt. Schreiben des GF A v. 11.8.2011: "ab Mitte 2009"), in  welchem Umfang und von wem und wann mit dem Fahrzeug private oder betriebliche Fahrten  und mit welchem Fahrtziel (ob im In- oder Ausland und zu welchen Kunden genau)  durchgeführt wurden, sowie auch, wo die Service- und Reparaturleistungen am Fahrzeug und  die Betankung vorgenommen wurde und wer die betreffenden Kosten getragen hat.

**False Positives:**

- `VWWJ IT GmbH` — partial — pred is substring of gold: `Fa.VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Fa.VWWJ IT GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_190`)


Abgesehen davon, dass im Gegenstandsfalle Zulassungsbesitzer des Fahrzeuges ab 9.10.2007 A  und ab 3.12.2009 die Fa.VWWJ IT GmbH war, welchem Umstand wie auch der Frage nach dem  rechtmäßigen Besitzer oder auf wen die Zulassung im Inland erfolgen könnte, nach Obigem  keine ausschlaggebende Bedeutung zukommt, ist nach dem Dafürhalten des BFG der Bf als  Verwender im Sinne eines "Halters" des Fahrzeuges und damit als Steuerschuldner iSd NoVAG  zu qualifizieren:   Abgesehen davon, dass dem Bf aus der Verwendung des Fahrzeuges der Nutzen daran  zugekommen ist, ist das gewichtigste Indiz hiefür die vom Bf ab 1.11.2008 für das Fahrzeug  erwiesenermaßen abgeschlossene, betragsmäßig wohl nicht unerhebliche  Vollkaskoversicherung.

**False Positives:**

- `VWWJ IT GmbH` — partial — pred is substring of gold: `Fa.VWWJ IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.VWWJ IT GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_419`)


Auf einem der im Zuge der Beanstandung durch das Organ der Parkraumüberwachung  angefertigten Beweisfotos war ersichtlich, dass sich das Fahrzeug mit dem Kennzeichen  KENNZ2 bei der FIRMA GmbH in Reparatur befunden habe.

**False Positives:**

- `FIRMA GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_439`)


Aus einem in im Akt abgelegten,  im Zuge der Beanstandung angefertigten Beweisfoto war ersichtlich, dass im Fahrzeug ein  Schreiben mit der Angabe abgelegt war , dass es sich um ein Ersatzfahrzeug für das bei der  "FIRMA GmbH" in Reparatur befindliche Fahrzeug mit dem Kennzeichen  KENNZ2 handle.

**False Positives:**

- `FIRMA GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_20`)


– eine Rechnung von amazon.de vom 07.02.2018 über ein „Corsair HX1200 1200 W 80Plus  Platinum PC-Netzteil (Voll-Modulares Kabelmanagement, ATX) schwarz in Höhe von 211,67 €,  (= Rechnung Nr. 2 laut Auflistung),  – eine Rechnung von amazon.de vom 18.01.2018 über ein „Crucial 8GB DDR4 2400 MT/s (PC4- 19200) DR x8 DIMM 288-Oin – CT8G4DFD824A“ in Höhe von 84,73 €, (= Rechnung Nr. 3 laut  Auflistung),  – eine Rechnung der Firma Ganz Einfach GmbH, Hannover, vom 28.01.2018 über eine „CSL –  4 G Hochleistungs LTE Antenne 15 dBi MIMO Technik Verstärker-Antenne“ in Höhe von  19,01 €, (= Rechnung Nr. 4 laut Auflistung),  – eine Rechnung von amazon.de vom 15.05.2018 über einen „Bronson++ HE-D 1000 – 110 Volt  Spannungswandler / Transformer – 1000 Watt – In: EURO 220 – 240 Volt / Out: USA 110 Volt –  Ringkerntransformator 1000 W – Bronson“ in Höhe von 71,24 €, (= Rechnung Nr. 5 laut  Auflistung),  – eine Rechnung von amazon.de vom 16.05.2018 über eine „Saft LS 14250 ½ AA 3,6V Li-SOCI2  Batterie (5-er Pack) weiß/grün“ in Höhe von 14,26 €, (= Rechnung Nr. 6 laut Auflistung),  – eine Rechnung von amazon.de vom 04.07.2018 über einen „LUPUSEC Drahtloser  Sensoreingang für die XT Alarmanlagen kompatibel mit der XT1 und XT2 Funk Alarmanlagen,  Energieklasse A, 12020“ in Höhe von 60,14 €, (= Rechnung Nr. 7 laut Auflistung),  – eine Rechnung von amazon.de vom 03.07.2018 über eine 720P HD WLAN Wifi IP Kamera  LE203, Sicherheitskamera, Überwachungskamera, IP Cam, drahtlos, steuerbar mit  Bewegungsmelder, 2 Wege Audio, IR Nachtsicht, integrierbar in User Smarthome  Alarmsystem“ in Höhe von 153,36 €, (= Rechnung Nr. 8 laut Auflistung),  – eine Rechnung von amazon.de vom 22.07.2018 über eine „SanDisk Ultra 64 GB microSDXC  Speicherkarte + Adapter bis zu 100 MB/Sek, Class 10, U1, A1, Grau, Rot“ in Höhe von 18,65 €,  (= Rechnung Nr. 9 laut Auflistung),  – eine Rechnung von amazon.de vom 23.11.2018 über ein „Samsung Galaxy S7 Smartphone  (5,1 Zoll (12,9 cm) Touch-Display, 32GB interner Speicher, Android OS) black“ in Höhe von  261,18 €, (= Rechnung Nr. 10 laut Auflistung),  – eine Rechnung von amazon.de vom 23.11.2018 über eine Samsung EVO Select microSDXC 65  GB MB-ME64GA/EU Speicherkarte“ in Höhe von 17,14 €, (= Rechnung Nr. 11 laut Auflistung),  – eine Rechnung von amazon.de vom 23.11.2018 über eine „Medion P61078 Lifebeat- Muktiroom Soundbar mit 2 x 18 W RMS Ausgangsleistung, eingebautem 36 W RMS  Subwooofer, Bluetooth-Funktion und DLNA kompatibel“ in Höhe von 121 €, (= Rechnung Nr. 12  laut Auflistung),  4 von 18 Seite 5 von 18

**False Positives:**

- `Firma Ganz Einfach GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_13`)


Die Gaststätte B-Platz ist Folge des Insolvenzverfahrens der Nieder Waldbach GmbH  Diese GmbH  wurde mit Generalversammlungsbeschluss vom 06.09.2007 als übertragende Gesellschaft mit  der Bf. als übernehmender Gesellschaft verschmolzen.

**False Positives:**

- `Nieder Waldbach GmbH  Diese GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_14`)


Seit 2001 hält die Bf. 100% der  Geschäftsanteile an der Nieder Waldbach GmbH   Die Gesellschafter der Bf. sind die Fa.Adeler&Glasener Textil GmbH und V.A. (=V.A.).

**False Positives:**

- `Adeler&Glasener Textil GmbH` — partial — pred is substring of gold: `Fa.Adeler&Glasener Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)
- `Fa.Adeler&Glasener Textil GmbH`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_15`)


Am Stammkapital der  Bf. ist die Holding GmbH [mit der Privatstiftung als Gesellschafter] mit 95% beteiligt.

**False Positives:**

- `Holding GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_55`)


*) 6%-Abschnitt (Gutachten A-Anstalt):   Das bei einem Testeinkauf beim Hauptlieferanten für Schweinskarree am 27.03.2008  eingekaufte Fleisch der Fa.Lemost-Handel GmbH sei unverzüglich und gekühlt in die A-Anstalt verbracht  worden.

**False Positives:**

- `Lemost-Handel GmbH` — partial — pred is substring of gold: `Fa.Lemost-Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.Lemost-Handel GmbH`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_66`)


Nach einer weiteren Aussage des Geschäftsführers des weiteren Fleischlieferanten Dorfleitner+Ternis Versicherung GmbH (NS 11.08.2008) sei derartig minderwertiges Fleisch, wie im Gutachten der B-Anstalt  abgebildet, niemals geliefert worden.

**False Positives:**

- `Fleischlieferanten Dorfleitner+Ternis Versicherung GmbH` — partial — gold is substring of pred: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_78`)


*) "Kalkulationsdifferenzen können mit Verrechnung Nieder Waldbach GmbH erklärt werden":  Die These widerspreche den ersten Gegenargumenten zur Kalkulation: Immer sei behauptet  worden, dass das Absinken der Aufschläge durch die enormen Fleischabfälle begründet sei.

**False Positives:**

- `Verrechnung Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_91`)


Auf die niederschriftliche Bestätigung des Geschäftsführers des Lieferanten Dorfleitner+Ternis Versicherung GmbH  wonach  Fleisch in so einer schlechten Qualität nie geliefert worden sei, wurde verwiesen.

**False Positives:**

- `Lieferanten Dorfleitner+Ternis Versicherung GmbH` — partial — gold is substring of pred: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_169`)


*) Vorhalt betreffend nicht überprüfter/gewürdigter Dateien: Nach den aus der  Dateienauswertung resultierenden Feststellungen wären Fleischabfälle tiefgekühlt an die  D- GmbH ab 2005 weiterverkauft worden.

**False Positives:**

- `D- GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_187`)


Laut Bestätigung des Fleischlieferanten Dorfleitner+Ternis Versicherung GmbH wäre ein Fleisch mit so einer schlechten  Qualität nie ausgeliefert worden (sei im Bericht bereits dargestellt worden).

**False Positives:**

- `Fleischlieferanten Dorfleitner+Ternis Versicherung GmbH` — partial — gold is substring of pred: `Dorfleitner+Ternis Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfleitner+Ternis Versicherung GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_327`)


der Verrechnung Nieder Waldbach GmbH um Vorlage von Unterlagen als Nachweis für die  falsche Berechnung zwischen den beiden Betrieben ersucht worden sei; b) dies(e) Behauptung  "Kalkulationsdifferenzen können mit Verrechnung B GmbH erklärt werden" einen glatten  Widerspruch zu den Gegenargumenten zur Kalkulation darstelle;

**False Positives:**

- `Verrechnung Nieder Waldbach GmbH` — partial — gold is substring of pred: `Nieder Waldbach GmbH`
- `Verrechnung B GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

</details>

---

## `german_company_e_commerce` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e91d48ca`  
**Description:**
Matches specific E-Commerce company patterns.

**Content:**
```
\b([A-Z][a-zA-Z0-9\-]+\s+u\.\s+[A-Z][a-zA-Z0-9\-]+\s+E‑?Commerce)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 0 | 5043 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1721, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_23`)

Für jene Geräte, die von Liechtenstein oder der Schweiz nach Österreich zur Firma **FA Graz-Stadt**  Lamperstätten  gebracht wurden, wurden sogenannte Proformarechnungen ausgestellt, in  welchen das jeweilige Leihgerät mit dem Zeitwert angeführt wurde.

- missed: `FA Graz-Stadt` (organisation)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_176`)

Furtnor-Handel GmbH  Zur **Furtnor-Handel GmbH** wurde festgestellt, dass sie seit Stichtag 5.3.2012 weder als Dienstgeber noch als  Leistungserbringer mehr in Frage kam.

- missed: `Furtnor-Handel GmbH` (organisation)
- predicted in sentence: `Furtnor-Handel GmbH  Zur Furtnor-Handel GmbH`

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_2`)

Stock, 1150  Wien, über die Beschwerde vom 13. März 2020 gegen den Bescheid des **Finanzamtes Wien  4/5/10** vom 4. März 2020 betreffend Umsatzsteuer 2018, Steuernummer ***, zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO im eingeschränkten Umfang Folge gegeben.

- missed: `Finanzamtes Wien  4/5/10` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Wladimir Schaeffer  in der Beschwerdesache  Scarlett Ever, Felle 6, 4264 Unterrauchenödt, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom  10. Oktober 2024 gegen den Bescheid des **Finanzamtes für Großbetriebe** vom 18. September  2024 betreffend Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 1. Juli  2023 bis 31. Dezember 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Finanzamtes für Großbetriebe` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Martin Yüksekkaya, Bonnleiten 21S, 4724 Aigen, Österreich  vertreten durch **Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH**, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31. März 2014 gegen den Bescheid des Finanzamtes für Großbetriebe vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2012  (Steuernummer 68-939/1151 ) nach Durchführung einer mündlichen Verhandlung am  06.07.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_45`)

Es gebe mit jeder GmbH (BFK Holding GmbH,Rusnok IT GmbH**;Kämpker&Mooslechner Holz GmbH** Berg Donwilbach GmbH;Traver-Planung GmbH,EnnsTouristik Consulting GmbH  einen Managementvertrag mit identem Inhalt .  Es seien mehrere Gesellschaften mbH gegründet worden, um eine Baustellenausweitung im  Bundesgebiet erreichen zu können, um flexibel auf den Markt reagieren zu können, und um  eine unabhängige Entscheidungsfindung der einzelnen Geschäftsführer in den GmbH erreichen  zu können.

- missed: `;Kämpker&Mooslechner Holz GmbH` (organisation)
- predicted in sentence: `BFK Holding GmbH`, `Rusnok IT GmbH`, `Mooslechner Holz GmbH Berg Donwilbach GmbH`, `Traver-Planung GmbH`, `EnnsTouristik Consulting GmbH`

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_240`)

Folglich ist die Verfügungsmacht über die Ware bei der Lieferung **ZWOP Cloud AG**– Bf. bereits in  Österreich auf Bf. übergegangen.

- missed: `ZWOP Cloud AG` (organisation)
- predicted in sentence: `Lieferung ZWOP Cloud AG`

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_17`)

Mit Bescheiden vom 21. August 2015 nahm das **Finanzamt Braunau Ried Schärding** das  Verfahren betreffend Einkommensteuer 2009, 2010, 2011, 2012 und 2013 gemäß  § 303 Abs. 1 BAO wieder auf.

- missed: `Finanzamt Braunau Ried Schärding` (organisation)
- predicted in sentence: `Finanzamt`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_75`)

Die Beschwerdeführerin war bis einschließlich des Wirtschaftsjahres  2012/13 Teil des **Mur Zorheim** -Konzerns, danach des Dorfsudlex-IT -Konzerns.

- missed: `Mur Zorheim` (organisation)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_11`)

Tatsächlich wurden aber Subunternehmer beauftragt, die tatsächlich nicht existent waren, wie  die Firmen Furtnor-Handel GmbH **PGIV Umwelt Entwicklung GmbH** oder Burglechner Touristik GmbH & Co KG  die wohl Rechnungen ausstellten, die  2 von 29 Seite 3 von 29

- missed: `PGIV Umwelt Entwicklung GmbH` (organisation)
- predicted in sentence: `Firmen Furtnor-Handel GmbH PGIV Umwelt Entwicklung GmbH`, `Burglechner Touristik GmbH`

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/145448.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145448.1_37`)

33 war die Nummer des **Finanzamtes  Neunkirchen Wr. Neustadt**) von -1.311,65 € auf -1.291,61 € geändert;

- missed: `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_38`)

Diese Ansicht wird noch verstärkt durch die technischen IT-Auswertungen des  **Bundesministeriums für Finanzen**, die die belangte Behörde übermittelt hat und die besagen,  dass via Finanzonline mit 27. Jänner 2024 zwar eine Beschwerde eingebracht wurde, diese  jedoch überhaupt nur gegen den 2. gegenständlichen Bescheid vom 25. Jänner 2024 – die  Beschwerdevorentscheidung – technisch eingebracht werden konnte, weil es technisch  anscheinend nicht möglich ist, zweimal eine Beschwerde gegen denselben Erstbescheid  einzubringen.

- missed: `Bundesministeriums für Finanzen` (organisation)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/142502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142502.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Gloria Rejngardt   in der Beschwerdesache des Estelle Klaffer, Moosscheibe 14, 4942 Außerguggenberg, Österreich,   betreffend den Bescheid des **Finanzamt Schwechat Gerasdorf**  vom 24. März 2020   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2019, Steuernummer  88-435/1011,   zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Finanzamt Schwechat Gerasdorf` (organisation)
- predicted in sentence: `Finanzamt`

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_33`)

Bei der Beantwortung der Frage, welcher Grad der Behinderung ab welchem Zeitpunkt vorlag  ist die belangte Behörde bzw. das Bundesfinanzgericht an das der Bescheinigung des  **Bundesamtes für Soziales und Behindertenwesen** (Sozialministeriumservice) zugrunde liegende  Gutachten gebunden und darf dieses nur dahingehend prüfen, ob es schlüssig und vollständig  und im Fall mehrer Gutachten, diese nicht einander widersprechend sind (vgl. VwGH  29.9.2011, 2011/16/0063;

- missed: `Bundesamtes für Soziales und Behindertenwesen` (organisation)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/142867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142867.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden MMag. Gerald Erwin Ehgartner und die  weiteren Senatsmitglieder Mag. Elisabeth Traxler, Mag. Harald Zeller und Christian Ringseis in  der Beschwerdesache Muran Iossifidis, Birken-Siedlung 22, 4715 Unterstetten, Österreich, vertreten durch KPMG Alpen-Treuhand  GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  über die Beschwerde vom 30. August 2023 gegen den Bescheid des **Finanzamtes für  Großbetriebe** vom 11. Juli 2023 betreffend Beschwerdezinsen (§ 205a BAO) nach  Durchführung einer mündlichen Verhandlung am 29. November 2023 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Finanzamtes für  Großbetriebe` (organisation)
- predicted in sentence: `KPMG Alpen-Treuhand  GmbH`, `Finanzamtes`

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_48`)

Bedingt durch die Lockdown-Maßnahmen ab März 2020 wurde das Studium ab 03/2020 im  Distance Learning abgewickelt. Lediglich für Prüfungsvorbereitungen, Prüfungen und  Laborübungen war eine Anwesenheit am Standort der **FH Villach** zugelassen.

- missed: `FH Villach` (organisation)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_125`)

Während der Zeit des Mutterschutzes hielt sich die Bf in  Deutschland auf und bezog von der **Wiener Gebietskrankenkasse** Wochengeld.

- missed: `Wiener Gebietskrankenkasse` (organisation)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem **Gerichtshof der Europäischen Union** werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

- missed: `Gerichtshof der Europäischen Union` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_110`)

3. Zum Einwand der Unzuständigkeit der belangten Behörde  Die steuerliche Vertretung ist der Rechtsansicht, dass der Prüfungsauftrag vom 10.11.2010 von  der unzuständigen Behörde, nämlich dem Finanzamt Graz-Stadt, und nicht vom **Finanzamt  Klagenfurt** erlassen worden sei, was die belangte Behörde bestritt;

- missed: `Finanzamt  Klagenfurt` (organisation)
- predicted in sentence: `Finanzamt`, `Finanzamt`

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_180`)

Sofern der EU-Kunde einen Abruf macht, informiert auch Bf.  den Lieferanten **ZWOP Cloud AG** und macht ihrerseits einen Abruf der bereits im Jahr 2014 vertraglich  gekauften Waren.

- missed: `ZWOP Cloud AG` (organisation)
- predicted in sentence: `Lieferanten ZWOP Cloud AG`

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133681.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133681.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden R1, die RichterinR2 sowie die  fachkundigen Laienrichter R3 und R4 in der Beschwerdesache C als Gottfried Kamperschroer, Allentsgschwendt 4W, 8741 Allersdorf, Österreich,  vertreten durch **Schmidt & Schmidt KG**, Bahnzeile 10, 2130 Mistelbach, über die Beschwerde  vom 13. Dezember 2012 gegen die gem. § 200 Abs. 2 BAO endgültigen Bescheide des  Finanzamtes Gänserndorf Mistelbach (nunmehr Finanzamt Österreich) vom 4. Oktober 2012  betreffend Einkommensteuer 2005 bis 2008, Steuernummer 84-352/6923, nach  Durchführung einer mündlichen Verhandlung am 10. Juni 2021 in Anwesenheit der  Schriftführerin S1, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Schmidt & Schmidt KG` (organisation)
- predicted in sentence: `Finanzamtes`, `Finanzamt Österreich`

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_92`)

Nach § 8 Abs 6 FLAG 1967 ist der Grad der Behinderung oder die voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, durch eine Bescheinigung des  Sozialministeriumservice (früher **Bundesamtes für Soziales und Behindertenwesen**) auf Grund  eines ärztlichen Sachverständigengutachtens nachzuweisen (vgl. VwGH 20.09.1995,  95/13/0134, VwGH 27.04.2005, 2003/14/0105, VwGH 20.12.2006, 2003/13/0123, VwGH  30.05.2017, Ro 2017/16/0009).

- missed: `Bundesamtes für Soziales und Behindertenwesen` (organisation)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/143673.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143673.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Sebastian Kötters  in der Beschwerdesache Agnes Hundorf,  Bischofsberg 23, 9123 Unterkrain, Österreich, vertreten durch Mag. Helmut Hirsch Rechtsanwalt, Josef-Krainer-Straße 46/I,  8074 Raaba, über die Beschwerde vom 2. August 2013 gegen den Bescheid des **Finanzamt Judenburg Liezen**  vom  4. Juli 2013 betreffend Pfändung einer Geldforderung zu Steuernummer 65-832/4960  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Finanzamt Judenburg Liezen` (organisation)
- predicted in sentence: `Finanzamt`

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des **Finanzamtes Waldviertel** vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

- missed: `Finanzamtes Waldviertel` (organisation)
- predicted in sentence: `MITTEREGGER Steuerberatungs GmbH`, `Finanzamtes`

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_115`)

Die **Demircan Metall AG** ist eine kleine Aktiengesellschaft im Sinne des § 221 UGB und hat ihren Sitz in Ort4, BL.

- missed: `Demircan Metall AG` (organisation)
- predicted in sentence: `Die Demircan Metall AG`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_159`)

Somit handle es sich bei der ersten  Lieferung der **Möbel Zorkelglanz GmbH** an die Bf. um die „ruhende Lieferung“ iSd. § 3 Abs. 7 UStG 1994.

- missed: `Möbel Zorkelglanz GmbH` (organisation)
- predicted in sentence: `Zorkelglanz GmbH`

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/145816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145816.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Priv.-Doz. Lars Tezlow  in der Beschwerdesache Ilona Sadowske,  Laaer-Wald-Straße 254, 4040 Asberg, Österreich, vertreten durch **Hofmann - Wirtschaftstreuhand - Steuerberater KG -  Steuerbüro Specht**, Kirchweg 11, 6600 Reutte, gegen den von der belangten Behörde  Finanzamt Österreich am 24. April 2023 zu Steuernummer 48-791/6345  ausgefertigten  Bescheid betreffend Einkommensteuer 2021 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 Abs. 1 BAO abgeändert.

- missed: `Hofmann - Wirtschaftstreuhand - Steuerberater KG -  Steuerbüro Specht` (organisation)
- predicted in sentence: `Finanzamt Österreich`

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_113`)

Die für diese Verwendung von der **RHO Pharma**  entrichteten Mietentgelte stellen den  Kostenfaktor dar, welcher für die Zuordnung zum unternehmerischen Bereich wesentlich ist.

- missed: `RHO Pharma` (organisation)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_27`)

II. Über die Beschwerde wurde erwogen:  1. Sachverhalt   Mit zivilrechtlichem Vertrag vom 9. November 2018 zwischen der beschwerdeführenden Partei  und der ÖBB-Infrastruktur AG (im Folgenden: ÖBB Infra) übertrug die beschwerdeführende  Partei der ÖBB Infra näher genannte Liegenschaften und übertrug die **ÖBB** Infra ihrerseits  ebenfalls näher genannte andere Liegenschaften an die beschwerdeführende Partei.

- missed: `ÖBB` (organisation)
- predicted in sentence: `Infrastruktur AG`

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/138353.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138353.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hubert Wunderlin  in der Beschwerdesache Friedhelm Fomin,  Riedlbachstraße 8, 3970 Oberbrühl, Österreich, vertreten durch **ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H.**, Postfach 257, 1061 Wien Postfach, über die Beschwerde  vom 15. August 2021 gegen den Bescheid des Finanzamtes Österreich vom 13. Juli 2021  betreffend Covid-19 Zahlungserleichterung, Steuernummer 25-245/7156, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H.` (organisation)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_204`)

Dabei sind die vom EuGH in den Rs C-245/04 EMAG, C-430/09 **Euro Tyre Holding**,  C-587/10 VSTR, C-386/16 Toridas UAB, C-628/16 Kreuzmayr und C-580/16 Hans Bühler KG  aufgestellten Grundsätze sowie die Rechtsprechung des VwGH (25.6.2007, 2006/14/0107) zu  beachten.

- missed: `Euro Tyre Holding` (organisation)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Zlatan Tegtmeier  in der Angelegenheit der Parteien  Dipl. Kfm. VetR Gerhard Stranz (Beschwerdeführerin), vertreten durch die   Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H., 9400 Wolfsberg  und **Finanzamt Oststeiermark**, 1000 Wien, PF 251  als  Amtspartei über die Beschwerden vom 12.

- missed: `Finanzamt Oststeiermark` (organisation)
- predicted in sentence: `Finanzamt`

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/142680.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142680.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Moritz Lindstaedt  in der Beschwerdesache Samuel Rattai,  Hilzing 64, 2880 Kranichberg, Österreich, vertreten durch **Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH**, Lehargasse 3A Tür 14, 1060 Wien, über die Beschwerde vom  7. September 2023 gegen den Bescheid des Finanzamtes Österreich vom 30. August 2023  betreffend Zahlungserleichterungen gem. § 212 BAO, Steuernummer 30-750/1577, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH` (organisation)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_117`)

Somit ist in einem nächsten  Schritt zu prüfen, in wessen Zuständigkeitsbereich die Beschwerdesache ab dem 01.01.2021  fällt. Dabei ist § 61 Abs. 1 Z. 9 BAO idF BGBl I 2020/99 einschlägig, wonach das **Finanzamt für  Großbetriebe** für die Erhebung der verfahrensgegenständlichen Abgaben für Abgabepflichtige,  die Teil einer Unternehmensgruppe gemäß § 9 KStG 1988 sind, zuständig ist, wenn ua die  beiden zuletzt bekannt gegebenen Umsatzerlöse eines Gruppenmitgliedes jeweils mehr als €  10 Millionen überschritten haben.

- missed: `Finanzamt für  Großbetriebe` (organisation)
- predicted in sentence: `Finanzamt`

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/149085.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149085.1_48`)

Die geleisteten Zahlungen für  Wohnraumschaffung in der Höhe von 2.920 € war dem Schreiben der **Raiffeisenbank Rion Villach  Bankhaus Nötsch**  vom  12.01.2021 zu entnehmen.

- missed: `Raiffeisenbank Rion Villach  Bankhaus Nötsch` (organisation)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_84`)

Begründung: Ich übe meine Tätigkeit im Außen - und  Innendienst im Anzeigenverkauf/Mediaberatung im Auftrag des **Niederösterreichischen  Pressehauses**, wie in der Tätigkeitsbeschreibung des Dienstgebers beschrieben, seit 2014 aus.

- missed: `Niederösterreichischen  Pressehauses` (organisation)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_100`)

Die beschwerdeführende Partei besteuerte nach vereinbarten Entgelten, daher hätten mit den  Eingangsrechnungen der **Eberler Bau KG**  B KG, C KG, D KG, E KG und F KG Betriebsausgaben und  Vorsteuern geltend gemacht werden können, während bei den letzteren aufgrund der  Besteuerung nach vereinnahmten Entgelten mangels Zahlungseingängen keine Umsatzsteuer  abgeführt wurde und es auch sonst zu keiner Versteuerung von Erträgen gekommen sei.

- missed: `Eberler Bau KG` (organisation)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/148832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148832.1_47`)

Mit Email der **OstLemkraftMöbel GmbH** vom 20.05.2025 teilte diese dem Bundesfinanzgericht mit, dass der Bf  im Jahr 2020 an 304 Tagen die Tageszeitung zugestellt habe.

- missed: `OstLemkraftMöbel GmbH` (organisation)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_52`)

In letzterer sei eine Ausgabenposition „Geschäftsführerhaftung **i.S.Traun-Handel AG**–  Vergleich“ und der Betrag von EUR 8.000,- und eine Position „Rechtskosten Dr. E i.S. A AG“ von  EUR 339,09 ausgewiesen, ohne dass dabei ein Zusammenhang mit der Schilift GmbH  erkennbar sei.

- missed: `i.S.Traun-Handel AG` (organisation)
- predicted in sentence: `Traun-Handel AG`, `A AG`, `Schilift GmbH`

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/145656.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145656.1_16`)

Hätte der Gesetzgeber den Liegenschaftserwerb von der **ÖBB-Infrastruktur AG**  befreien wollen, hätte er dies im Gesetz zum Ausdruck gebracht.

- missed: `ÖBB-Infrastruktur AG` (organisation)
- predicted in sentence: `Infrastruktur AG`

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_92`)

Kann also die Verpflegung am auswärtigen (Tätigkeits-)Ort zu den gleichen Bedingungen wie an  der ständigen Arbeitsstätte in Anspruch genommen werden, stehen Tagesgelder nicht zu.  3. Da seit Studienbeginn im Oktober 2019 an der **FH Villach** dieser Ort wiederholt angefahren  wurde, was erst mit Beginn des Lockdown im März 2020 reduziert wurde, war ab bzw. im  Jänner 2020 in Villach streitgegenständlich ein als weiterer Mittelpunkt der Tätigkeit zu  qualifizierender Ort gegeben.

- missed: `FH Villach` (organisation)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)

Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen **Finanzamtes Wien 9/18/19 Klosterneuburg**  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

- missed: `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- predicted in sentence: `Finanzamt`, `Finanzamtes`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des **Finanzamtes Wien  1/23** vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Finanzamtes Wien  1/23` (organisation)
- predicted in sentence: `KPMG Alpen-Treuhand GmbH`, `Finanzamtes`

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde **FA Oststeiermark**,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

- missed: `FA Oststeiermark` (organisation)
- predicted in sentence: `Finanzamt`, `Finanzamt`

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_144`)

8. Strafrechtliche Verurteilung des *Name*   Nach dem Urteil des Landesgerichtes LG vom xx.03.2020, GZ, hätte *Name* u.a. folgende  Unternehmen am xx.12.2012 gegründet:  **Eberler Bau KG**    B KG    C KG    D KG    E KG    F KG  *Name* fungierte bei allen als Komplementär.

- missed: `Eberler Bau KG` (organisation)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des **Finanzamtes Lilienfeld St. Pölten** vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Finanzamtes Lilienfeld St. Pölten` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_86`)

Dass die angefochtenen Erledigungen  von der belangten Behörde (und nicht vom die Außenprüfung durchführenden Finanzamt  Graz-Stadt) genehmigt und folglich auch erlassen wurden (siehe dazu die Ausführungen unter  Punkt IV.3.), resultiert aus den Ausführungen des **Bundesministeriums für Finanzen**, Sektion I,  vom 22.09.2020 in Verbindung mit den Angaben der belangten Behörde im Schriftsatz vom  selben Tag: Demnach wurden die verfahrensgegenständlichen Erledigungen durch einen  Mitarbeiter der belangten Behörde, nämlich Name, freigegeben, sohin von diesem approbiert.

- missed: `Bundesministeriums für Finanzen` (organisation)
- predicted in sentence: `Finanzamt`

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_270`)

9. 2014, Ro 2014/01/0033  unter Hinweis auf die ständige Judikatur des **Obersten Gerichtshofes** zu § 502 ZPO, etwa OGH  28.

- missed: `Obersten Gerichtshofes` (organisation)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_142`)

Den weiteren Ausführungen zur Unzuständigkeit im Zusammenhang mit dem Befüllen der  Eingabebögen durch den Prüfer des Finanzamtes Graz-Stadt ist der unzweifelhafte Inhalt der  Ausführungen des **Bundesministeriums für Finanzen**, Sektion I und der belangten Behörde,  10 von 15 Seite 11 von 15

- missed: `Bundesministeriums für Finanzen` (organisation)
- predicted in sentence: `Finanzamtes`

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_106`)

Der Gesetzgeber hat für den Nachweis der entsprechenden Voraussetzung eine Bescheinigung  des **Bundesamtes für Soziales und Behindertenwesen** auf Grund eines ärztlichen  Sachverständigengutachtens als einziges zulässiges Beweismittel vorgesehen (vgl dazu VfGH  10.12.2007, B 700/07, und VwGH 27.4.2005, 2003/14/0105, sowie VwGH 20.12.2006,  2003/13/0123, oder VwGH 18.11.2008, 2007/15/0019).

- missed: `Bundesamtes für Soziales und Behindertenwesen` (organisation)
- predicted in sentence: —

</details>

---

