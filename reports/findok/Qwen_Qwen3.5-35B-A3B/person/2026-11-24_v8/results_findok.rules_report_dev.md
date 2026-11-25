# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-24T20:57:12.941925

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-24_v8/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Training documents | 3148 |
| Validation documents | 787 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 7310 |
| Validation sentences | 2144 |
| Dev sentences | 61673 |
| Test sentences | 61001 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 150 |
| Refinement iterations | 6 |
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
| True Positives | 593 |
| False Positives | 93 |
| False Negatives | 1258 |
| Total Gold Entities | 1851 |
| Micro Precision | 86.4% |
| Micro Recall | 32.0% |
| Micro F1 | 46.7% |
| Macro F1 | 46.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `names_after_herr_frau` | 0.6% | 100.0% | 0.3% | 6 | 6 | 0 |
| `names_after_herrn_frau` | 0.5% | 100.0% | 0.3% | 5 | 5 | 0 |
| `names_with_suffixes_tightened` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `names_after_legal_roles_generalized` | 25.5% | 98.2% | 14.6% | 276 | 271 | 5 |
| `names_after_beschwerdesache_no_title` | 24.4% | 97.0% | 13.9% | 266 | 258 | 8 |
| `names_after_beschwerdesache_generalized` | 1.9% | 94.7% | 1.0% | 19 | 18 | 1 |
| `names_after_genitive_context` | 0.8% | 58.3% | 0.4% | 12 | 7 | 5 |
| `names_after_von_durch` | 2.4% | 30.7% | 1.2% | 75 | 23 | 52 |
| `names_with_suffixes_fixed` | 0.4% | 18.2% | 0.2% | 22 | 4 | 18 |
| `names_after_born_son` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_at_sentence_start_with_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_at_sentence_start_tightened` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_after_vormaliger_steuerlicher` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_after_techn_r` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `names_with_phd_title` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `names_with_maga_title` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `names_after_herr_frau` 

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `0c7948f7`  
**Description:**
Matches names following 'Herr' or 'Frau', capturing only the name and suffixes, excluding the honorific.

**Content:**
```
(?:Herr|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+|[A-Z][a-zäöüß]+-[A-Z][a-zäöüß]+)+(?:\s*,\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM|M\.B\.L\.)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Behörde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|Büro|Praxis|Klinik|Krankenhaus|Schule|Universität|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|Büro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftsprüfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunfähigkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Geschäftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 6 | 0 | 1845 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `M.` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_268`)


Konkret war seitens der Betriebsprüfung (wie auch schon bei früheren Amtshandlungen) der  Gesellschafter/Geschäftsführer Herr Albert Sengeisen, geboren 1970, als maßgebliche Person in der  Firma Starnberg Beratung GmbH wahrzunehmen.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_20`)


In einem weiteren Schriftverkehr mit der  steuerlichen Vertretung wurde durch diese bekannt gegeben, dass der zuständige  Geschäftsführer, Herr Harald Hilderink, die Abgabenforderungen aus Umsatzsteuern in der 45.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)


 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr Harald Hilderink  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

</details>

---

## `names_after_herrn_frau` 

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `ef5869b4`  
**Description:**
Matches names following 'Herrn' or 'Frau' (accusative/dative), capturing only the name and suffixes, excluding the honorific.

**Content:**
```
(?:Herrn|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+|[A-Z][a-zäöüß]+-[A-Z][a-zäöüß]+)+(?:\s*,\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM|M\.B\.L\.)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Behörde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|Büro|Praxis|Klinik|Krankenhaus|Schule|Universität|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|Büro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftsprüfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunfähigkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Geschäftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.005 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 0 | 1846 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_11`)


Weiters legte die Beschwerdeführerin den Dienstvertrag vom 12.03.2014 vor, mit dem  folgenden entscheidungsrelevanten Inhalt:   "DIENSTVEREINBARUNG abgeschlossen zwischen DG als Dienstgeber und Frau James Hainig,  Adr.**** als Dienstnehmerin.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Albert Sengeisen, Wallnerfeld 8, 3751 Sigmundsherberg, Österreich, vertreten durch gfk Gartner Furherr Karandi Rechtsanwälte,  Westbahnstraße 5/11, 1070 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 21. April 2017 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. Jänner 2017, SpS 16, Strafnummer 007 in Abwesenheit des  Beschuldigte und seines Verteidigers, jedoch in Anwesenheit des Amtsbeauftragten sowie der  Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer  007 geführte Finanzstrafverfahren wegen des Verdachts der Abgabenhinterziehung gemäß §  33 Abs. 2 lit. a FinStrG betreffend Umsatzsteuervorauszahlungen 03/2014 in Höhe von €  433,00 und 07-11/2014 von € 1.785,72 wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Über Albert Sengeisen  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG eine  Geldstrafe in Höhe von € 20.600,00 Tage verhängt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Wallnerfeld 8, 3751 Sigmundsherberg, Österreich` (address)
- `Finanzamt  Wien 9/18/19` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Raimund Ladwig` | `Raimund Ladwig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

</details>

---

## `names_with_suffixes_tightened` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `001744f8`  
**Description:**
Matches names with suffixes (BEd, LLB, etc.) in contexts like 'Beschwerdesache' or sentence starts, ensuring only the name+suffix is captured, not the context.

**Content:**
```
(?:^|\n|\.|\s)(?:in\s+der\s+)?Beschwerdesache(?:\s+des\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+\s*,?\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM))(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Raimund Diedering, Bakk. iur.` | `Raimund Diedering, Bakk. iur.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk` (person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich` (address)

</details>

---

## `names_after_legal_roles_generalized` 🏆

**F1:** 0.255 | **Precision:** 0.982 | **Recall:** 0.146  

**Format:** `regex`  
**Rule ID:** `9e685033`  
**Description:**
Matches names following legal roles, strictly capturing name and suffixes, excluding trailing commas and context.

**Content:**
```
(?:Richterin|Richter|Bf\.in|Bf\.|Beschwerdef\u00fchrerin|Beschwerdef\u00fchrer|Schriftf\u00fchrerin|Schriftf\u00fchrer|Vorsitzende|Vorsitzender)\s+((?:Prof\.\s+)?(?:Dr\.|Mag\.(?:a|\.\s+a)?|Mag\.Dr\.|Dr\.in|StR\s+|Techn\s+R\s+|LL\.M\.|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|\u00d6kR|HR|KR|Ri\.|R\.)?\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+(?:\s*,\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Gericht|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.982 | 0.146 | 0.255 | 276 | 271 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 271 | 5 | 1580 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_0`)


GZ. RV/5101724/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter Dr. Elias Derneden  in der Beschwerdesache über die Beschwerde vom 14.01.2019 gegen den Bescheid der belangten Behörde vom 04.01.2019 betreffend Familienbeihilfe für den Zeitraum ab März 2018 zu Recht: 1.Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elias Derneden` | `Dr. Elias Derneden` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Dietlind Mahlstädt` | `Dr.in Dietlind Mahlstädt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kai Pipers` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adalbert Köseoglu` | `Hon.-Prof. Adalbert Köseoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Jana Papenkord` (person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Mag. Manfred Frühwirth` (person)
- `Finanzamtes Linz` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Lieselotte Akdas` | `Univ.-Prof.in Lieselotte Akdas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Helge Göppele` | `Priv.-Doz. Helge Göppele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `GDJJ Versand` (organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich` (address)
- `Finanzamtes Graz` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Jodgalweit` | `Priv.-Doz.in Alva Jodgalweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Pawils` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Kießerling` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `MITTEREGGER Steuerberatungs GmbH` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Michaela Dehnert` | `Hon.-Prof.in Michaela Dehnert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Stiller` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Shoshana Leuther` (person)
- `Hagleithen 8, 3345 Strohmarkt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `80-897/7654` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR OSR Leonie Ercklentz` (person)
- `Karnitzen 135, 9635 Kronhof, Österreich` (address)
- `LKP Steuerberatung OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hermine Roj` | `Mag.a Hermine Roj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corinna Farke` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Hammers` | `Dr.in Huberta Hammers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josefine Frikel` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theodora Urbanova, Bakk. iur.` (person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `54-205/5010` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rosamunde Galanidis` | `Priv.-Doz.in Rosamunde Galanidis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hermine Ruprich` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Mag. Wolfgang Moser` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thomas Hutching` | `Hon.-Prof. Thomas Hutching` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Ruprecht Hauswerth` (person)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `26-476/7368` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Zarin Eckartz` | `Priv.-Doz.in Zarin Eckartz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Volkmar Oortwyn` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Matyschek` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sean Herdling` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Othmar Feuerbaum` | `Mag. Othmar Feuerbaum` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingeborg Kollaczek` (person)
- `Hufgasse 10, 9062 Gabriel, Österreich` (address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `47-554/2547` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Melina Bankratz` | `Priv.-Doz.in Melina Bankratz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lars Huesgen` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf Bogdanowic` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie Schan` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Gspan` | `Dr.in Ute Gspan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Ottfried Theißl` (person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ottfried Ficici, Wilfersdorf 3, 4890 Asten, Österreich, über die Beschwerden vom 19. April 2018 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 17. April 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 Steuernummer 51-452/2856  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ottfried Ficici` (person)
- `Wilfersdorf 3, 4890 Asten, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `51-452/2856` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Tamara Steinmüller` | `Mag.a Tamara Steinmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gueldner Garten` (organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich` (address)
- `FA Deutschlandsberg Leibnitz Voitsberg` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gertraud Hausherr` | `Mag. Gertraud Hausherr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jacqueline Dittus` (person)
- `Sausal 90O, 4911 Schönfeld, Österreich` (address)
- `Anton Lammer  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Joachim Annanias` | `Dr. Joachim Annanias` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Burkhard Krautschenko` (person)
- `Geizersgraben 6, 2823 Leiding, Österreich` (address)
- `Mag. Susanne Pöltenstein-Rosenegger` (person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Titus Ohlmer` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Edwin Pfaefflin` (person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich` (address)
- `Finanzamtes` (organisation)
- `35-514/8431` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Diethard Ringhand` (person)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Braunau Ried` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Hasslbauer` (person)
- `Oed bei Haslach 48, 4782 Aigerding, Österreich` (address)
- `Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich` (address)
- `Procurator Treuhand- und Revisionsges.m.b.H.` (organisation)
- `Bundesministeriums für Finanzen` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Kirstin Matiascheck` | `Dr.in Kirstin Matiascheck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Schwinge` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Achmed Karolzak` | `Univ.-Prof. Achmed Karolzak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lilia Löffelmann` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `M.` (person)
- `Finanzamtes` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Olivia Ziegeler` | `Mag.a Olivia Ziegeler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mike Reislehner` (person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `44-773/5557` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Marceline Flory` | `Univ.-Prof.in Marceline Flory` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Zeitlhuber` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Susette Glaeßel` | `Mag.a Susette Glaeßel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl Morgenbesser` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Univ.-Prof. Alvin Paulikat` (person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Dr Christian Burghardt` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Elvira Thielsen` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Edith Schifferdecker` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich` (address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH` (organisation)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `73-948/8864` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Christoph Hasenfraz` | `Hon.-Prof. Christoph Hasenfraz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olivia Sahlmüller` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Milena Neidig` (person)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Dr. Adebiola Bayer` | `Dr. Adebiola Bayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jonas Gutkauf` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fiona Buedenbender` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich  über die Beschwerde vom 10. August 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 30. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 92-300/4861  zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fiona Buedenbender` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timothy Overlaender` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger` (person)
- `Paullehnerweg 72, 9584 Höfling, Österreich` (address)
- `UNICONSULT Steuerberatungs GmbH & Co KG` (organisation)
- `FA Braunau Ried Schärding` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Zoltan Dabrowski` | `Priv.-Doz. Zoltan Dabrowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Prof. Hartmut Szardemings` (person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich` (address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Martin Kuprian` | `Mag. Martin Kuprian` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Werner Böltl` (person)
- `Rydlweg 234, 3860 Dietweis, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Moses Dannebohm` | `Univ.-Prof. Moses Dannebohm` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruperta Schluckner` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Schippan  in der Beschwerdesache Judith Kapelle,  Saßbergweg 17, 4860 Haid, Österreich, betreffend Beschwerde vom 2. September 2012 gegen den Bescheid des FA  Waldviertel vom 3. August 2012 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 Steuernummer 31-042/8347  beschlossen:     Der Vorlageantrag vom 30.11.2012 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Petra Schippan` | `Priv.-Doz.in Petra Schippan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Judith Kapelle` (person)
- `Saßbergweg 17, 4860 Haid, Österreich` (address)
- `FA  Waldviertel` (organisation)
- `31-042/8347` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Maurice Bettenhäuser` | `Hon.-Prof. Maurice Bettenhäuser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Miranda Weissert` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Nancy Stuckenschneider  in der Beschwerdesache des  Bruno Karahasan, Ludowikaweg 5, 3602 Bacharnsdorf, Österreich, über die Beschwerde vom 2. Juli 2019 gegen den Bescheid des  FA St. Johann Tamsweg Zell am See  vom 26. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zur Steuernummer 12-630/0045  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Nancy Stuckenschneider` | `Priv.-Doz.in Nancy Stuckenschneider` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Bruno Karahasan` (person)
- `Ludowikaweg 5, 3602 Bacharnsdorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `12-630/0045` (tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Walter Monheim  in der Beschwerdesache Enrico Steudtle,  Assing 21, 9071 Wurdach, Österreich, vertreten durch GEYER & GEYER Wirtschaftstreuhand GmbH, Rudolf von Alt- Platz 1, 1030 Wien, hinsichtlich der Beschwerde vom 23. November 2011 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 - nunmehr Finanzamtes Österreich - vom 25. Oktober 2011  betreffend Festsetzung der Kapitalertragsteuer 2007 bis 2010, Steuernummer  10-940/7308, den Beschluss:   I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als  unzulässig geworden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Walter Monheim` | `Hon.-Prof. Walter Monheim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Enrico Steudtle` (person)
- `Assing 21, 9071 Wurdach, Österreich` (address)
- `GEYER & GEYER Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Österreich` (organisation)
- `10-940/7308` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Vanessa Nowikoff  in der Beschwerdesache des  KommR Lee Ponsard, Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich, über die Beschwerde vom 30. Juli 2020 gegen den Bescheid des  Finanzamtes X. (FA, jetzt Dienststelle des Finanzamt Freistadt Rohrbach Urfahr ) vom 10. Juli 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zur Steuernummer 63-102/2061  zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 (1) BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Vanessa Nowikoff` | `Hon.-Prof.in Vanessa Nowikoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `KommR Lee Ponsard` (person)
- `Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `63-102/2061` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Walter Aiglsdorfer` | `Mag. Walter Aiglsdorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hugo Engelsmann` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/135653.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135653.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Ibrahim de Vrese, LLB, Kitzlermühle 3, 2754 Wopfing, Österreich, über die Beschwerde vom 07.06.2021 wegen behaupteter  Verletzung der Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Familienbeihilfe ab 09/2019 Sozialversicherungsnummer 2872011080  beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Ulrike Stephan` | `Mag. Ulrike Stephan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibrahim de Vrese, LLB` (person)
- `Kitzlermühle 3, 2754 Wopfing, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `2872011080` (social_security_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Isakova, Hörgattern 37, 3244 Kühberg, Österreich, über die Beschwerde vom 1. Juni 2017 gegen  den Bescheid des Finanzamtes Österreich vom 15. Mai 2017 betreffend Familienbeihilfe  01.2016-12.2016 Steuernummer 93-163/8536  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, dass dieser betreffend T1 hinsichtlich der Monate April, August und  September 2016 ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimitri Isakova` (person)
- `Hörgattern 37, 3244 Kühberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `93-163/8536` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Edith Lohhausen` | `Dr.in Edith Lohhausen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Schmalohr + Kiekebusch Möbel` (organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich` (address)
- `Michael Haberl` (person)
- `Finanzamtes` (organisation)
- `Finanzamt Judenburg Liezen` (organisation)
- `71-763/1501` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


BESCHLUSS   Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Frederike Lipienski  in der Beschwerdesache des  Hademar Rüstow, Eck 124T, 2214 Auersthal, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des  FA Amstetten Melk Scheibbs (FA) vom 10. März 2021 über die Abweisung eines Antrages auf Wiederaufnahme §  303 BAO /  ESt 2017 zur Steuernummer 71-651/2158  beschlossen:   Der Vorlageantrag vom 29.Sept.2021 wird gemäß § 260 Abs. 1 lit. a iVm § 264 Abs. 4 lit e und  Abs. 5 BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Frederike Lipienski` | `Hon.-Prof.in Frederike Lipienski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hademar Rüstow` (person)
- `Eck 124T, 2214 Auersthal, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `71-651/2158` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Mittel-Verlag, Am Rothenbühl 45, 4690 Ennsberg, Österreich  vertreten durch Dr. Stephan Riel als  Insolvenzverwalter, Landstraßer Hauptstraße 1 Tür 2, 1030 Wien, über die Beschwerde der  Abgabepflichtigen vom 25. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  20. April 2021 betreffend Pfändung einer Geldforderung zur Steuernummer 44-993/1626  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mittel-Verlag` (organisation)
- `Am Rothenbühl 45, 4690 Ennsberg, Österreich` (address)
- `Dr. Stephan Riel` (person)
- `Finanzamtes Österreich` (organisation)
- `44-993/1626` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Christian Lemanowitz` | `Univ.-Prof. Christian Lemanowitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dietmar Kachelmuss` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Sheila Nonnmacher` | `Dr.in Sheila Nonnmacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Semertzidou` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `76-265/6028` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Denis Diekötter  in KLG Kreuzbau 16, 8242 Kronegg, Österreich, vertreten durch Rein & Partner Steuerberatung GmbH & Co KG in  8230 Hartberg, Alleegasse 13, über die Beschwerde vom 22.3.2017 gegen die Bescheide des  Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 14.3.2017 betreffend   - Einkommensteuer 2012, 2013, 2014 und 2015 und  - Umsatzsteuer 2012, 2013, 2014 und 2015  zu Recht erkannt:   I. Insoweit sich die Beschwerde gegen die Umsatzsteuerbescheide 2012, 2013, und  2014 richtet, wird dem Beschwerdebegehren gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Denis Diekötter` (person)
- `KLG Kreuzbau 16, 8242 Kronegg, Österreich` (address)
- `Rein & Partner Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Wolek  in der Verwaltungsstrafsache  MedR Uwe Vaculik, Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich, über die Eingabe der Beschuldigten vom 3. Februar 2022 den  Beschluss gefasst:  I. Gemäß § 28 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 31 VwGVG  und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) wird die Unzuständigkeit  des Bundesfinanzgerichtes festgestellt und das Beschwerdeverfahren betreffend die Eingabe  vom 3. Februar 2022 eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr.in Linn Wolek` | `Dr.in Linn Wolek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Uwe Vaculik` (person)
- `Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

| Predicted | Gold |
|---|---|
| `Mag. Natascha Gassner` | `Mag. Natascha Gassner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Mag. Renate Burtscher` (person)
- `Bernd Feldkircher` (person)
- `Vincent Kohlstruk` (person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich` (address)
- `Bischof-Fuchs Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Günter Jedamczik` | `Univ.-Prof. Günter Jedamczik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Tobias Schönyan` (person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich` (address)
- `Mag. Gernot Thonhauser` (person)
- `Finanzamtes Österreich` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Claire Wienhues, Hörweix 62, 3140 Pottenbrunn, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13 Tür  Turm 24, 1100 Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt VG betreffend Körperschaftsteuer 2010 Steuernummer 61-469/1778  zu Recht  erkannt:   I. Der Säumnisbeschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claire Wienhues` (person)
- `Hörweix 62, 3140 Pottenbrunn, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamt` (organisation)
- `61-469/1778` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/137039.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137039.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Susanne Rohrauer  in der Beschwerdesache der  StadtHandel Planung, Sebastianplatz 18, 3441 Dietersdorf, Österreich  vertreten durch StB, über die Beschwerde vom 7. April 2021 gegen  den Bescheid des FA Salzburg-Stadt  vom 25. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Steuernummer 89-257/7642  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Susanne Rohrauer` | `Priv.-Doz.in Susanne Rohrauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StadtHandel Planung` (organisation)
- `Sebastianplatz 18, 3441 Dietersdorf, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `89-257/7642` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Tanja Fützenreiter, Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich, über die Beschwerde der Beschwerdeführerin  (Bf.) vom 29. März 2021 gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) für  2019 des Finanzamtes Österreich vom 17. März 2021 zur Steuernummer 90-161/7779  zu  Recht erkannt:   Gemäß § 279 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tanja Fützenreiter` (person)
- `Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `90-161/7779` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ulrike Stephan` | `Mag. Ulrike Stephan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentin Joebges, LLM` (person)
- `Bärngarten 17, 9713 Hochegg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `84-167/9727` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Zlatan Nowizki  in der Beschwerdesache Janis Loewenthal,  Georg Grinninger-Straße 15, 3830 Pyhra, Österreich, vertreten durch die [Erwachsenenvertreterin], über die Beschwerde vom  23. August 2019 gegen den Bescheid des Finanzamtes Kitzbühel Lienz (nunmehr: Finanzamt  Österreich) vom 23. Juli 2019 betreffend Familienbeihilfe und Erhöhungsbetrag zur  Familienbeihilfe wegen erheblicher Behinderung ab November 2018, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Zlatan Nowizki` | `Mag. Zlatan Nowizki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janis Loewenthal` (person)
- `Georg Grinninger-Straße 15, 3830 Pyhra, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dominika Juhass  in der Beschwerdesache  Ludmilla Hühnerfuß, Bakk. techn., Singham 20, 3465 Unterstockstall, Österreich,   über die Beschwerde vom 27. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom  12. Juni 2019 betreffend Vorsteuererstattung 2018 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dominika Juhass` | `Hon.-Prof.in Dominika Juhass` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ludmilla Hühnerfuß, Bakk. techn.` (person)
- `Singham 20, 3465 Unterstockstall, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/137349.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Gebhard Kristupeit, Bakk. techn., Wörndlestraße 17, 9112 Untergrafenbach, Österreich, vertreten durch APP Steuerberatung GesmbH, Schenkenstraße  4, 1010 Wien, über die Beschwerde gegen die Bescheide des Finanzamtes Baden Mödling vom  31. Mai 2011 hinsichtlich Haftung betreffend Kapitalertragsteuer für 2007 und 2008,  Steuernummer 83-002/9356  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Kristupeit, Bakk. techn.` (person)
- `Wörndlestraße 17, 9112 Untergrafenbach, Österreich` (address)
- `APP Steuerberatung GesmbH` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `83-002/9356` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Penelope Splettstösser  in der Beschwerdesache Wilhelm Schöbel,  Leopoldgasse 23, 8674 Grubbauer, Österreich, über die Beschwerde vom 10. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 3. Februar 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 32-896/6207  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Penelope Splettstösser` | `Univ.-Prof.in Penelope Splettstösser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilhelm Schöbel` (person)
- `Leopoldgasse 23, 8674 Grubbauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-896/6207` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Anton Böckamp, Bakk. techn., Leopold Kunschak Gasse 25, 9343 Dielach, Österreich, über die Beschwerde vom 8. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich (vormals Finanzamt Gänserndorf Mistelbach, § 323b BAO) vom  25. November 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 84-669/5568  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO im Sinne des Beschwerdebegehrens  abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Böckamp, Bakk. techn.` (person)
- `Leopold Kunschak Gasse 25, 9343 Dielach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Gänserndorf Mistelbach` (organisation)
- `84-669/5568` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Chen Geßlein  in der Beschwerdesache MedR Techn R Mathilda Elfeldt,  Klingengasse 112, 9556 Waggendorf, Österreich, vertreten durch Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH, Kurandtplatz 1, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 29. Jänner  2021 gegen den Bescheid des Finanzamt Vorarlberg  vom 18. Jänner 2021 betreffend Einkommensteuer  2019 Steuernummer 43-811/9169  zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Chen Geßlein` | `Mag. Chen Geßlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Techn R Mathilda Elfeldt` (person)
- `Klingengasse 112, 9556 Waggendorf, Österreich` (address)
- `Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)
- `43-811/9169` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Adolf Brehmer  in der Beschwerdesache VetR Gotthard Lohscheider,  Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich, vertreten durch „Meinrad Kisewetter“ - Steuerberatungsgesellschaft m.b.H., Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich,  über die Beschwerde vom 28.06.2021, gegen den Bescheid des Finanzamtes Österreich vom  27.05.2021 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm § 111 BAO, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Adolf Brehmer` | `Mag. Adolf Brehmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Gotthard Lohscheider` (person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich` (address)
- `Meinrad Kisewetter` (person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julian Egiede` (person)
- `Theras 97, 4565 Haselbäckau, Österreich` (address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `Mag. Michael Sablatnik` (person)
- `88-033/6865` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Walter Aiglsdorfer` | `Mag. Walter Aiglsdorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gisbert Löhberg` (person)
- `Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich` (address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `73-737/2281` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Massimo Friedhoff` | `Univ.-Prof. Massimo Friedhoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Grothmann` (person)
- `Finanzamt Wien 1/23` (organisation)
- `32-847/2958` (tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache OSR Eugenia Balikci, Richardisweg 14, 5134 Ginshöring, Österreich, vertreten durch Wiener Kinder-und Jugendhilfe  2,20, Dresdner Straße 43, 1200 Wien, über die Beschwerde vom 20. März 2020 gegen den  Bescheid des Finanzamtes Österreich vom 25. Februar 2020 betreffend Familienbeihilfe ab  Jänner 2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Eugenia Balikci` (person)
- `Richardisweg 14, 5134 Ginshöring, Österreich` (address)
- `Wiener Kinder-und Jugendhilfe` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Barbara Schwalb  in der Beschwerdesache Annalena Mlynarcik,  Ledochowskastraße 5, 4040 Kammerschlag, Österreich, über die Beschwerde vom 02.03.2017 gegen die Bescheide des Finanzamtes  Österreich vom 28. Februar 2017 betreffend Abweisung des Antrages auf Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer für die Jahre Wiederaufnahme § 303 BAO /  ESt 2011  -2013 Steuernummer 09-012/5071  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Barbara Schwalb` | `Hon.-Prof.in Barbara Schwalb` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annalena Mlynarcik` (person)
- `Ledochowskastraße 5, 4040 Kammerschlag, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `09-012/5071` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Maximiliane Gasparetti, Gschwandtkopf 12, 9330 Althofen, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51,  1030 Wien, über die Beschwerde vom 23. Dezember 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. November 2016 betreffend  1.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximiliane Gasparetti` (person)
- `Gschwandtkopf 12, 9330 Althofen, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Thomas Schmidt in der Finanzstrafsache  gegen Linda Tumpach, Gengerberg 44, 4052 Ansfelden, Österreich, vertreten durch Rechtsanwälte Gloß Pucher Leitner Gloß  Enzenhofer, Wiener Straße 3, 3100 St. Pölten, über die Beschwerde der Beschuldigten vom  25.11.2019 gegen den Bescheid des Amtes für Betrugsbekämpfung als Finanzstrafbehörde  (ehemals des Finanzamtes Lilienfeld St. Pölten als Finanzstrafbehörde ) vom 17. Oktober 2019,  Strafkontonummer 91-951/0670, betreffend die Abweisung eines  Zahlungserleichterungsansuchens (Stundungs- und Ratenansuchen) gemäß § 156 Abs. 1 des  Finanzstrafgesetzes (FinStrG) in Verbindung mit   § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) beschlossen:  Die Beschwerde wird als unzulässig zurückgewiesen, da es sich beim gegenständlich  bekämpften so genannten Bescheid um einen Nichtbescheid handelt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Thomas Schmidt` | `Mag. Thomas Schmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Linda Tumpach` (person)
- `Gengerberg 44, 4052 Ansfelden, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `91-951/0670` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Richard Reithmayer, Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Bundesstraße  36, 6923 Lauterach, gegen die Bescheide des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer 2015 und 2016 sowie Festsetzung von  Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Richard Reithmayer` (person)
- `Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_93`)


3.2. Verlosung von 2 Tickets und Verlosung des Ersatzes diverser Auslagen des täglichen  Lebens durch die Bf.  Die Bf. bringt vor, dass einerseits ein Preisausschreiben eine Sonderform der Auslobung gemäß  § 860 ABGB und kein Spiel darstelle und andererseits „Spiel“ eine Aktivität mehrerer Mitspieler  begrifflich definiere, hingegen die Entgegennahme eines Geschenkes keine Beteiligung an einem  Spiel sei.

**False Positives:**

- ` Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Wolfgang Tiwald, ` — partial — gold is substring of pred: `Mag. Wolfgang Tiwald`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Wolfgang Tiwald`(person)
- `Kirsten Renneissen`(person)
- `Egererweg 9, 5760 Niederhaus, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `Mag. Armin Treichl, ` — partial — gold is substring of pred: `Mag. Armin Treichl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Treichl`(person)
- `Tristan Potente`(person)
- `Hürth 5, 4362 Schönfichten, Österreich`(address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `Finanzamtes`(organisation)
- `61-467/9522`(tax_number)

</details>

---

## `names_after_beschwerdesache_no_title` 🏆

**F1:** 0.244 | **Precision:** 0.970 | **Recall:** 0.139  

**Format:** `regex`  
**Rule ID:** `cea2e60b`  
**Description:**
Matches names following 'Beschwerdesache' without titles, ensuring strict boundaries to avoid capturing trailing commas or context words like 'Verein'.

**Content:**
```
Beschwerdesache\s+(?:der\s+des\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.970 | 0.139 | 0.244 | 266 | 258 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 258 | 8 | 1593 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elisabeth Schafstall` | `Elisabeth Schafstall` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Leithagürtel 20, 4251 Steinwald, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Pipers` | `Kai Pipers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Dietlind Mahlstädt` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `Finanzamtes` (organisation)
- `85-229/2263` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Höffert` | `Christine Höffert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Adalbert Köseoglu` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emmerich Frydrychowski` | `Emmerich Frydrychowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Walter Summersberger` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

| Predicted | Gold |
|---|---|
| `Ali Jäckle` | `Ali Jäckle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marion Endrulat` | `Marion Endrulat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabine Tiedicke` | `Sabine Tiedicke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.DDr. Hedwig Bavenek-Weber in der  Beschwerdesache Merlin Feucht, Alte Straße 2, 8114 Unterfriesach, Österreich, über die Beschwerde vom 12. Dezember 2011  gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14.  November 2011, Steuernummer 57-396/6782, betreffend die Festsetzung der ermäßigten  Glücksspielabgabe gemäß § 58 Abs. 3 GSpG für Glücksspiele im Rahmen von Gewinnspielen  (Preisausschreiben), zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Merlin Feucht` | `Merlin Feucht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.DDr. Hedwig Bavenek-Weber` (person)
- `Alte Straße 2, 8114 Unterfriesach, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `57-396/6782` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Sieglinde Kießerling` | `Sieglinde Kießerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `MITTEREGGER Steuerberatungs GmbH` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Leroy Sitterle` | `Leroy Sitterle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Astoria Stb GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Hermine Ruprich` | `Hermine Ruprich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Rosamunde Galanidis` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Mag. Wolfgang Moser` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Volkmar Oortwyn` | `Volkmar Oortwyn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Zarin Eckartz` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sean Herdling` | `Sean Herdling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

| Predicted | Gold |
|---|---|
| `Ingeborg Kollaczek` | `Ingeborg Kollaczek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Othmar Feuerbaum` (person)
- `Hufgasse 10, 9062 Gabriel, Österreich` (address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `47-554/2547` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Lars Huesgen` | `Lars Huesgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Melina Bankratz` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rudolf Bogdanowic` | `Rudolf Bogdanowic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ottfried Ficici, Wilfersdorf 3, 4890 Asten, Österreich, über die Beschwerden vom 19. April 2018 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 17. April 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 Steuernummer 51-452/2856  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ottfried Ficici` | `Ottfried Ficici` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Wilfersdorf 3, 4890 Asten, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `51-452/2856` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jacqueline Dittus` | `Jacqueline Dittus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Sausal 90O, 4911 Schönfeld, Österreich` (address)
- `Anton Lammer  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Titus Ohlmer` | `Titus Ohlmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Edwin Pfaefflin` | `Edwin Pfaefflin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich` (address)
- `Finanzamtes` (organisation)
- `35-514/8431` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Annemarie Schwinge` | `Annemarie Schwinge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Kirstin Matiascheck` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lilia Löffelmann` | `Lilia Löffelmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Achmed Karolzak` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `M.` (person)
- `Finanzamtes` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mike Reislehner` | `Mike Reislehner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Olivia Ziegeler` (person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `44-773/5557` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gregor Klocksin` | `Gregor Klocksin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Unterguntschach 85, 3525 Armschlag, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

| Predicted | Gold |
|---|---|
| `Chiara Duchan` | `Chiara Duchan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich` (address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Stephan Zeitlhuber` | `Stephan Zeitlhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Marceline Flory` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Frauke Galleithner` | `Frauke Galleithner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Heike Lehmensieck` | `Heike Lehmensieck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Höllstein 11, 9852 Neuschitz, Österreich` (address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Olivia Sahlmüller` | `Olivia Sahlmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Christoph Hasenfraz` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Klutentreter` | `Gebhard Klutentreter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sandra Fenn` | `Sandra Fenn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Mag. Manuela Meyerhofer` (person)
- `Finanzamtes Bruck Eisenstadt  Oberwart` (organisation)
- `49-433/1564` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Jonas Gutkauf` | `Jonas Gutkauf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Adebiola Bayer` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich  über die Beschwerde vom 10. August 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 30. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 92-300/4861  zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Tristan Potente` | `Tristan Potente` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Hürth 5, 4362 Schönfichten, Österreich` (address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)
- `61-467/9522` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde FA Oststeiermark,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

| Predicted | Gold |
|---|---|
| `Kevin Damiani` | `Kevin Damiani` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. René Neuendorf` (person)
- `Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich` (address)
- `Finanzamt Oststeiermark` (organisation)
- `Finanzamt Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Timothy Overlaender` | `Timothy Overlaender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fatima Eichmayr` | `Fatima Eichmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieskapellenweg 10, 8047 Graz, Österreich` (address)
- `Dr. Klaus Plätzer,` (person)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `67-455/2359` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lee Kubbig` | `Lee Kubbig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinI. in der Beschwerdesache Violetta Bailmann, Schlosserfeld 35, 9632 Hochwart, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 20. Oktober 2016 gegen  die Bescheide des Finanzamtes Spittal Villach vom 22. September 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012 (Steuernummer  82-877/4906 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Violetta Bailmann` | `Violetta Bailmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schlosserfeld 35, 9632 Hochwart, Österreich` (address)
- `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG` (organisation)
- `Finanzamtes Spittal Villach` (organisation)
- `82-877/4906` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erwin Döpkemeier` | `Erwin Döpkemeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Mag Kerstin Friedrich` (person)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

| Predicted | Gold |
|---|---|
| `Dora Szczepanowski` | `Dora Szczepanowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich` (address)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

| Predicted | Gold |
|---|---|
| `Ruperta Schluckner` | `Ruperta Schluckner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Moses Dannebohm` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Schippan  in der Beschwerdesache Judith Kapelle,  Saßbergweg 17, 4860 Haid, Österreich, betreffend Beschwerde vom 2. September 2012 gegen den Bescheid des FA  Waldviertel vom 3. August 2012 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 Steuernummer 31-042/8347  beschlossen:     Der Vorlageantrag vom 30.11.2012 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Judith Kapelle` | `Judith Kapelle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Petra Schippan` (person)
- `Saßbergweg 17, 4860 Haid, Österreich` (address)
- `FA  Waldviertel` (organisation)
- `31-042/8347` (tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache August Cernyj, Lusthausstraße 569, 4901 Bruckmühl, Österreich, vertreten durch Casapicola & Gross Wirtschafts- prüfungs- und Steuerberatungs  GmbH, Gluckgasse 3 Tür 15, 1010 Wien, über die Beschwerde vom 19. Juni 2019 gegen die  Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt für Großbetriebe) datiert jeweils  vom 30. April 2019 betreffend Umsatzsteuer für die Jahre 2013 bis 2016 und  Körperschaftsteuer für die Jahre 2013 – 2015 , Steuernummer 12-317/0890  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `August Cernyj` | `August Cernyj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lusthausstraße 569, 4901 Bruckmühl, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `12-317/0890` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Rauner, die RichterinR  sowie die fachkundigen Laienrichter Gregor Ableidinger und Dr. Franz Kandlhofer in der  Beschwerdesache Lieselotte Schluessel, Hannakstraße 205, 5121 Wimm, Österreich, über die Beschwerde vom 22. Februar 2016  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 10. Februar 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Lieselotte Schluessel` | `Lieselotte Schluessel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Rauner` (person)
- `Gregor Ableidinger` (person)
- `Dr. Franz Kandlhofer` (person)
- `Hannakstraße 205, 5121 Wimm, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Walter Monheim  in der Beschwerdesache Enrico Steudtle,  Assing 21, 9071 Wurdach, Österreich, vertreten durch GEYER & GEYER Wirtschaftstreuhand GmbH, Rudolf von Alt- Platz 1, 1030 Wien, hinsichtlich der Beschwerde vom 23. November 2011 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 - nunmehr Finanzamtes Österreich - vom 25. Oktober 2011  betreffend Festsetzung der Kapitalertragsteuer 2007 bis 2010, Steuernummer  10-940/7308, den Beschluss:   I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als  unzulässig geworden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Enrico Steudtle` | `Enrico Steudtle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Walter Monheim` (person)
- `Assing 21, 9071 Wurdach, Österreich` (address)
- `GEYER & GEYER Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Österreich` (organisation)
- `10-940/7308` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Laurin Überschar  in der Beschwerdesache Albert Theiselmann,  Hochmark 31g, 8323 Unterbuch, Österreich, vertreten durch Radike, Hammerl & Partner Steuerberatung GmbH,  Bisamberger Straße 2/1/8, 2100 Korneuburg, betreffend Beschwerde vom 17. Juni 2021 gegen  die Bescheide des Finanzamtes Österreich vom 20. Mai 2021 betreffend Einkommensteuer  2015 und 2016, Steuernummer 15-781/1702, den Beschluss:   I. Die Beschwerde wird gemäß § 256 Abs 3 Bundesabgabenordnung (BAO) als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Albert Theiselmann` | `Albert Theiselmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Laurin Überschar` (person)
- `Hochmark 31g, 8323 Unterbuch, Österreich` (address)
- `Radike, Hammerl & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `15-781/1702` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Ri, die Richterin Mag. Riin sowie  die fachkundigen Laienrichter A und B, in der Beschwerdesache Karina Schliekau, Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich,  vertreten durch die Kanzlei, über die Beschwerde vom 15. Februar 2018 gegen den Bescheid  des Finanzamtes Österreich, vormals Finanzamt Wien 3/6/7/11/15 Schwechat und Gerasdorf,  vom 1. Februar 2018 betreffend Feststellung der Einkünfte § 188 BAO 2016, nach  Durchführung einer mündlichen Verhandlung am 17. November 2021 in Anwesenheit der  Schriftführerin C, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Karina Schliekau` | `Karina Schliekau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Riin` (person)
- `Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Wien 3/6/7/11/15` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hugo Engelsmann` | `Hugo Engelsmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Armin Heckemanns, Nabuccogasse 10, 2630 Ternitz, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, (im  Beschwerdeverfahren nicht eingeschritten), über die Beschwerde vom 10. Februar 2020 gegen  den Einkommensteuerbescheid 2018 des Finanzamtes Baden Mödling vom 10. Jänner 2020  (und gemäß § 253 Satz 1 BAO auch gegen den Einkommensteuerbescheid 2018 vom  18. September 2020) zu Steuernummer 75-597/1615  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Armin Heckemanns` | `Armin Heckemanns` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nabuccogasse 10, 2630 Ternitz, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `Finanzamtes Baden Mödling` (organisation)
- `75-597/1615` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi als Vorsitzenden, den Richter Ri2 als  beisitzender Richter, SenLR1 als fachkundiger Laienrichter und SenLR2 als fachkundiger  Laienrichter in der Beschwerdesache Alois Kleynsteuber, Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich, vertreten durch Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien,  über die Beschwerde vom 14. September 2012 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg vom 6. September 2012, StNr. 79-708/0061, betreffend Einkommensteuer  2008 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich` (address)
- `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` (organisation)
- `FA Wien 9/18/19  Klosterneuburg` (organisation)
- `79-708/0061` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Isakova, Hörgattern 37, 3244 Kühberg, Österreich, über die Beschwerde vom 1. Juni 2017 gegen  den Bescheid des Finanzamtes Österreich vom 15. Mai 2017 betreffend Familienbeihilfe  01.2016-12.2016 Steuernummer 93-163/8536  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, dass dieser betreffend T1 hinsichtlich der Monate April, August und  September 2016 ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Dimitri Isakova` | `Dimitri Isakova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Hörgattern 37, 3244 Kühberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `93-163/8536` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sulamith Jedwillat` | `Sulamith Jedwillat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brandenbergweg 15, 8353 Pichla, Österreich` (address)
- `Mag. Michael Payr` (person)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `41-852/7395` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Sieglinde Semertzidou` | `Sieglinde Semertzidou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Sheila Nonnmacher` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `76-265/6028` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karina von Wnuck-Lipinski  in der Beschwerdesache Rosemarie Fortwängler,  Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich, über die Beschwerde vom 4. Oktober 2019 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 26. September 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe (FB) und  Kinderabsetzbetrag (KG) für den Zeitraum Oktober 2017 bis Feber 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Fortwängler` | `Rosemarie Fortwängler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Karina von Wnuck-Lipinski` (person)
- `Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

| Predicted | Gold |
|---|---|
| `Vincent Kohlstruk` | `Vincent Kohlstruk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Mag. Natascha Gassner` (person)
- `Mag. Renate Burtscher` (person)
- `Bernd Feldkircher` (person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich` (address)
- `Bischof-Fuchs Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ludger Endel` | `Ludger Endel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `63-868/1042` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Claire Wienhues, Hörweix 62, 3140 Pottenbrunn, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13 Tür  Turm 24, 1100 Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt VG betreffend Körperschaftsteuer 2010 Steuernummer 61-469/1778  zu Recht  erkannt:   I. Der Säumnisbeschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Claire Wienhues` | `Claire Wienhues` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `Hörweix 62, 3140 Pottenbrunn, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamt` (organisation)
- `61-469/1778` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Stockhorst` | `Jeanne Stockhorst` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Fridrichallee 42, 4084 Scheiblberg, Österreich` (address)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `22-242/2984` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Tanja Fützenreiter, Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich, über die Beschwerde der Beschwerdeführerin  (Bf.) vom 29. März 2021 gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) für  2019 des Finanzamtes Österreich vom 17. März 2021 zur Steuernummer 90-161/7779  zu  Recht erkannt:   Gemäß § 279 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Tanja Fützenreiter` | `Tanja Fützenreiter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Seywald` (person)
- `Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `90-161/7779` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Zlatan Nowizki  in der Beschwerdesache Janis Loewenthal,  Georg Grinninger-Straße 15, 3830 Pyhra, Österreich, vertreten durch die [Erwachsenenvertreterin], über die Beschwerde vom  23. August 2019 gegen den Bescheid des Finanzamtes Kitzbühel Lienz (nunmehr: Finanzamt  Österreich) vom 23. Juli 2019 betreffend Familienbeihilfe und Erhöhungsbetrag zur  Familienbeihilfe wegen erheblicher Behinderung ab November 2018, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Janis Loewenthal` | `Janis Loewenthal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Zlatan Nowizki` (person)
- `Georg Grinninger-Straße 15, 3830 Pyhra, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Robert Derici` | `Robert Derici` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Exlgasse 12, 9623 Karnitzen, Österreich` (address)
- `Erich Allbrand` (person)
- `12-876/0077` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Penelope Splettstösser  in der Beschwerdesache Wilhelm Schöbel,  Leopoldgasse 23, 8674 Grubbauer, Österreich, über die Beschwerde vom 10. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 3. Februar 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 32-896/6207  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wilhelm Schöbel` | `Wilhelm Schöbel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Penelope Splettstösser` (person)
- `Leopoldgasse 23, 8674 Grubbauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-896/6207` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marlies Seipold, Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich, über die Beschwerde vom 27. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 14. Jänner 2020 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum März 2017 bis September 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlies Seipold` | `Marlies Seipold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Julian Egiede` | `Julian Egiede` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elisabeth Hafner` (person)
- `Theras 97, 4565 Haselbäckau, Österreich` (address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `Mag. Michael Sablatnik` (person)
- `88-033/6865` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gisbert Löhberg` | `Gisbert Löhberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich` (address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `73-737/2281` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jaden Grothmann` | `Jaden Grothmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Massimo Friedhoff` (person)
- `Finanzamt Wien 1/23` (organisation)
- `32-847/2958` (tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Theodor Siel, Amesberg 28, 6321 Angath, Österreich, über die Beschwerde vom 4. November 2016 gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich) vom 13. Oktober  2016 betreffend Grunderwerbsteuer, Steuernummer 74-672/4502, Erfassungsnummer 10- 2015, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Theodor Siel` | `Theodor Siel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Amesberg 28, 6321 Angath, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)
- `74-672/4502` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Barbara Schwalb  in der Beschwerdesache Annalena Mlynarcik,  Ledochowskastraße 5, 4040 Kammerschlag, Österreich, über die Beschwerde vom 02.03.2017 gegen die Bescheide des Finanzamtes  Österreich vom 28. Februar 2017 betreffend Abweisung des Antrages auf Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer für die Jahre Wiederaufnahme § 303 BAO /  ESt 2011  -2013 Steuernummer 09-012/5071  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Annalena Mlynarcik` | `Annalena Mlynarcik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Barbara Schwalb` (person)
- `Ledochowskastraße 5, 4040 Kammerschlag, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `09-012/5071` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Maximiliane Gasparetti, Gschwandtkopf 12, 9330 Althofen, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51,  1030 Wien, über die Beschwerde vom 23. Dezember 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. November 2016 betreffend  1.

| Predicted | Gold |
|---|---|
| `Maximiliane Gasparetti` | `Maximiliane Gasparetti` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Gschwandtkopf 12, 9330 Althofen, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache David Radeke, Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich, über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 18. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierte Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019,   Steuernummer 15-752/7224, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `David Radeke` | `David Radeke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `15-752/7224` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Rebecca Hüllhorst,  Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich, über die Beschwerde vom 8. Juli 2021 gegen den Abweisungsbescheid des  Finanzamtes Österreich vom 25. Juni 2021 betreffend Familienbeihilfe für das Kind To für den  Zeitraum Februar 2020 bis Februar 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rebecca Hüllhorst` | `Rebecca Hüllhorst` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Richard Reithmayer, Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Bundesstraße  36, 6923 Lauterach, gegen die Bescheide des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer 2015 und 2016 sowie Festsetzung von  Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Richard Reithmayer` | `Richard Reithmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Herbert Lindermayer  in der Beschwerdesache Anneliese Dreschmann,  Nußbacher Straße 43, 3650 Kehrbach, Österreich, vertreten durch Schwaiger & Partner Steuerberatung, Anton-Eder-Straße 5,  6020 Innsbruck, über die Beschwerde vom 19. Jänner 2021 gegen den Bescheid des FA Graz-Stadt  vom 13. Jänner 2021 betreffend Energieabgabenvergütung 2015 Steuernummer  60-855/1189  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anneliese Dreschmann` | `Anneliese Dreschmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Herbert Lindermayer` (person)
- `Nußbacher Straße 43, 3650 Kehrbach, Österreich` (address)
- `Schwaiger & Partner Steuerberatung` (organisation)
- `FA Graz-Stadt` (organisation)
- `60-855/1189` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

</details>

---

## `names_after_beschwerdesache_generalized` 🏆

**F1:** 0.019 | **Precision:** 0.947 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `47031749`  
**Description:**
Matches names following 'Beschwerdesache' with titles, ensuring strict boundaries.

**Content:**
```
Beschwerdesache\s+(?:der\s+des\s+)?((?:Dr\.|Mag\.|Mag\.Dr\.|Dr\.in|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|StR\s+|Techn\s+R\s+|OSR\s+|RA\s+|Bf\.|Bf\.(?:in)?|Herr|Frau|\u00d6kR|HR|KR|Ri\.|R\.|OMedR|KommR|RgR|MedR|KzlR|MMag\.|Prof\.)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+(?:\s*,?\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.947 | 0.010 | 0.019 | 19 | 18 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 18 | 1 | 1833 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Dr.in Laurin Morgenschweis` | `Dr.in Laurin Morgenschweis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich` (address)
- `Fatima Beringschmidt` (person)
- `Finanzamtes Waldviertel` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Ruprecht Hauswerth` | `Hon.-Prof. Ruprecht Hauswerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thomas Hutching` (person)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `26-476/7368` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OMedR Leonhard Hestermeyer` | `OMedR Leonhard Hestermeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` (person)
- `Sägerweg 5, 5450 Reitsam, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `52-932/8889` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache MedR Gertrude Hartges,  Hübing 15, 9535 Farrendorf, Österreich, über die Beschwerde vom 10. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `MedR Gertrude Hartges` | `MedR Gertrude Hartges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hübing 15, 9535 Farrendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `ÖkR Tobias Schönyan` | `ÖkR Tobias Schönyan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Günter Jedamczik` (person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich` (address)
- `Mag. Gernot Thonhauser` (person)
- `Finanzamtes Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache RgR Denise Symang, Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich, vertreten durch Mag. Robert Bitsche,  Rechtsanwalt, Nikolsdorfergasse 7-11/15, 1050 Wien, über die Beschwerde vom 9. Oktober  2019 gegen die Bescheide des Finanzamtes Wien 4/5/10 (nunmehr Finanzamt Österreich) vom  11. September 2019 sowie vom 23. September 2019 betreffend Wiederaufnahme  Körperschaftsteuer 2015 bis 2017, Steuernummer 60-977/8084, nach Durchführung einer  mündlichen Verhandlung am 19. Dezember 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `RgR Denise Symang` | `RgR Denise Symang` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich` (address)
- `Mag. Robert Bitsche` (person)
- `Finanzamtes Wien 4/5/10` (organisation)
- `Finanzamt Österreich` (organisation)
- `60-977/8084` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/144195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144195.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Gottfried Dimitriou  in der Beschwerdesache RgR Adam Lenk,  Prüfing 9, 5451 Wimm, Österreich, betreffend die Beschwerden vom 20. November 2023 gegen die Bescheide des  Finanzamtes Österreich vom 22. August 2023 betreffend Einkommensteuer 2020 und 2021 zu  Steuernummer 47-369/1528  beschlossen:  Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `RgR Adam Lenk` | `RgR Adam Lenk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Gottfried Dimitriou` (person)
- `Prüfing 9, 5451 Wimm, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `47-369/1528` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/144397.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144397.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag. Dario Hukauf, Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich, vertreten durch ALTHUBER SPORNBERGER &  PARTNER Rechtsanwälte GmbH, Doblhoffgasse 9 Tür Top 14, 1010 Wien, über die Beschwerde  vom 3. Jänner 2020 gegen die Bescheide des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr Finanzamtes für Großbetriebe ) vom 28. November 2019 betreffend Rückforderung  gem. § 241a BAO von Kapitalertragsteuer 2010 bis 2012 (Evidenznummern ***, ***, ***, ***,  ***, ***, ***, ***), Steuernummer 45-917/5183, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dario Hukauf` | `Mag. Dario Hukauf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamtes für Großbetriebe` (organisation)
- `45-917/5183` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Calvin Liechtenstein  in der Beschwerdesache KommR Thorsten Voelkerling,  Kirchenbühl 12, 4463 Brunnbach, Österreich, vertreten durch Rechtsanwalt Dr. Gahleithner & Partner OG, Schottengasse 7  Tür 6, 1010 Wien, über die Beschwerde vom 25. September 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 11. September 2019 betreffend den Ablauf der Aussetzung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KommR Thorsten Voelkerling` | `KommR Thorsten Voelkerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Calvin Liechtenstein` (person)
- `Kirchenbühl 12, 4463 Brunnbach, Österreich` (address)
- `Dr. Gahleithner & Partner OG` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/146116.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146116.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Thomas Bäckert  in der Beschwerdesache Dr. Quentin Tessier,  Krottenhofweg 115, 4364 Großmaseldorf, Österreich, betreffend Beschwerde vom 18. Juni 2023 gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 15. Mai 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  Steuernummer 71-981/5443  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Quentin Tessier` | `Dr. Quentin Tessier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Thomas Bäckert` (person)
- `Krottenhofweg 115, 4364 Großmaseldorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `71-981/5443` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Niklas Hussung  in der Beschwerdesache Univ.-Prof. Oliver Ruhsbüldt,  Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich, vertreten durch Gattringer Steuerberatung GmbH, Sonnensteinstraße 12, 4040  Linz, über die Beschwerde vom 31. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 16. Mai 2023 betreffend Einkommensteuer 2021 Steuernummer 26-058/9655  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Oliver Ruhsbüldt` | `Univ.-Prof. Oliver Ruhsbüldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Niklas Hussung` (person)
- `Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich` (address)
- `Gattringer Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `26-058/9655` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/147137.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache RgR Shirley Ribler, Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich, vertreten durch Dr. Christian Lind,  Am Ausblick 17, 3110 Neidling, über die Beschwerde vom 2. Jänner 2023 gegen die Bescheide  des Finanzamtes Österreich vom 1. Dezember 2022 betreffend Anspruchszinsen (§ 205 BAO)  2016, 2017 und 2018, Steuernummer 64-511/1773, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `RgR Shirley Ribler` | `RgR Shirley Ribler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich` (address)
- `Dr. Christian Lind` (person)
- `Finanzamtes Österreich` (organisation)
- `64-511/1773` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/147990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Leila Garnschröder  in der Beschwerdesache  RgR Corbinian Baranowskij, Schwamingstraße 19, 5452 Reitsam, Österreich, über die Beschwerde vom 6. März 2025 gegen den Bescheid des  Finanzamtes Österreich vom 6. Februar 2025 betreffend Zwangsstrafen 2023 Steuernummer  15-984/7137  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die Zwangsstrafen mit  150,00 Euro für die Körperschaftssteuererklärung und mit 150,00 Euro für die  Umsatzsteuererklärung (insgesamt somit mit 300,00 Euro) festgesetzt.

| Predicted | Gold |
|---|---|
| `RgR Corbinian Baranowskij` | `RgR Corbinian Baranowskij` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Leila Garnschröder` (person)
- `Schwamingstraße 19, 5452 Reitsam, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `15-984/7137` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/148525.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148525.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Julia Schlegl in der Beschwerdesache  KommR Natascha Domroeß, Obere Mölten 6, 9500 St. Georgen, Österreich, über die Beschwerde vom 28. Juni 2024 gegen den Bescheid des  Finanzamt St. Johann Tamsweg Zell am See  vom 17. Juni 2024 betreffend Anspruchszinsen (§ 205 BAO), Steuernummer  55-147/5658, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KommR Natascha Domroeß` | `KommR Natascha Domroeß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Julia Schlegl` (person)
- `Obere Mölten 6, 9500 St. Georgen, Österreich` (address)
- `Finanzamt St. Johann Tamsweg Zell am See` (organisation)
- `55-147/5658` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/148554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Koolen  in der Beschwerdesache   Univ.-Prof. Brian Salemi, Ulrichskirchen 3, 4184 Neuschlag, Österreich, Philippinen, Steuernummer 63-391/9556  über die Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamt Grieskirchen Wels  vom 1. Februar  2018 betreffend Vorsteuererstattung 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Brian Salemi` | `Univ.-Prof. Brian Salemi` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Regina Koolen` (person)
- `Ulrichskirchen 3, 4184 Neuschlag, Österreich` (address)
- `63-391/9556` (tax_number)
- `Finanzamt Grieskirchen Wels` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/148710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Florentin Tyarks  in der Beschwerdesache KommR Thaddäus Borkowski,  Linke Quergasse 31, 4600 Berg, Österreich, über die Beschwerden vom 16. April 2016 gegen die Bescheide des  Finanzamtes Landeck Reutte (nunmehr: Finanzamt Österreich) vom 15. März 2016 betreffend  Festsetzung des Dienstgeberbeitrages für die Jahre 2010 bis 2014, Steuernummer  01-227/0941,  zu Recht erkannt:  I.  Die Beschwerdevorentscheidung des Finanzamtes Innsbruck vom 19. September 2018, mit  welcher über die Beschwerden vom 15. April 2016 "gegen die Bescheide über die Festsetzung  des Dienstgeberbeitrages 2010-2014" abgesprochen wurde, wird wegen Unzuständigkeit der  bescheiderlassenden Behörde aufgehoben.

| Predicted | Gold |
|---|---|
| `KommR Thaddäus Borkowski` | `KommR Thaddäus Borkowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Florentin Tyarks` (person)
- `Linke Quergasse 31, 4600 Berg, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `01-227/0941` (tax_number)
- `Finanzamtes Innsbruck` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Univ.-Prof. Jonas Nußer  in der Beschwerdesache Dr.in Flora Lallemand,  Rochusplatz 224, 9530 Bad Bleiberg, Österreich, über die Beschwerde vom 5. November 2024 gegen die Bescheide des  FA Graz-Stadt  vom 27. August 2024 über den Ablauf einer Aussetzung der Einhebung, über die  Festsetzung von Aussetzungszinsen und vom 1. Oktober 2024 über die Abweisung eines  Aussetzungsantrags, Steuernummer 29-953/8923, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Flora Lallemand` | `Dr.in Flora Lallemand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Univ.-Prof. Jonas Nußer` (person)
- `Rochusplatz 224, 9530 Bad Bleiberg, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `29-953/8923` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149745.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  HR Manuela Buskotte, Schulboden 10, 8742 Kienberg, Österreich  vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße 32,  6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2017 und 2018, 18-878/6086, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `HR Manuela Buskotte` | `HR Manuela Buskotte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Schulboden 10, 8742 Kienberg, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `18-878/6086` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache ÖkR Istvan  Thiebaud, Ziakpark 78, 3213 Hollenstein, Österreich, vertreten durch ECOVIS Scholler & Partner, Wirtschaftstreuhand GmbH,  Schmalzhofgase 4, Tür 12, 1060 Wien, über die Beschwerden vom 28. Juli 2017 gegen den  Bescheid des Finanzamtes Wien 4/5/10, nunmehr Finanzamt Österreich, vom 29. Juni 2017  betreffend Einkommensteuer 2015, Steuernummer 04-368/0800, sowie vom 23. Jänner 2020  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf, nunmehr Finanzamt  Österreich, vom 25. November 2019 betreffend Einkommensteuer der Jahre 2016 und 2017  sowie Anspruchszinsen 2016 und 2017, Steuernummer ****, nach der am 12. Mai 2022 in  Hintere Zollamtsstraße 2b, 1030 Wien, durchgeführten mündlichen Verhandlung im Beisein  der Schriftführerin S   1.) zu Recht erkannt:   Die Beschwerden gegen die Einkommensteuerbescheide der Jahre 2015 und 2016 sowie gegen  den Anspruchszinsenbescheid des Jahres 2016 wird gemäß § 279 BAO als unbegründet  abgewiesen  2.) beschlossen:  Die Beschwerden gegen den Einkommensteuerbescheid des Jahres 2017 sowie gegen den  Anspruchszinsenbescheid des Jahres 2017 wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `ÖkR Istvan  Thiebaud, ` — partial — gold is substring of pred: `ÖkR Istvan  Thiebaud`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `ÖkR Istvan  Thiebaud`(person)
- `Ziakpark 78, 3213 Hollenstein, Österreich`(address)
- `ECOVIS Scholler & Partner, Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `Finanzamt  Österreich`(organisation)

</details>

---

## `names_after_genitive_context` 🏆

**F1:** 0.008 | **Precision:** 0.583 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `88e8fc07`  
**Description:**
Matches names following genitive contexts like 'des', 'der' to capture standalone names or names with titles, ensuring strict boundaries.

**Content:**
```
(?:des\s+|der\s+)((?:Dr\.|Mag\.|Mag\.Dr\.|Dr\.in|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|StR\s+|Techn\s+R\s+|OSR\s+|RA\s+|Bf\.|Bf\.(?:in)?|Herr|Frau|\u00d6kR|HR|KR|Ri\.|R\.|OMedR|KommR|RgR|MedR|KzlR|MMag\.|Prof\.)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+(?:\s*,?\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.583 | 0.004 | 0.008 | 12 | 7 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 7 | 5 | 1844 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thassilo Schoenrock, LLM` | `Hon.-Prof. Thassilo Schoenrock, LLM` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Hochscharten 126D, 5122 Dorfen, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `06-88-920/2630` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Franz Glashüttner` | `Mag. Franz Glashüttner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Rauscher` (person)
- `Dr. Christian Haid` (person)
- `Mag. Bruno  Sundl` (person)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `OMedR Ottfried Theißl` | `OMedR Ottfried Theißl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Ute Gspan` (person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Vanessa Nowikoff  in der Beschwerdesache des  KommR Lee Ponsard, Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich, über die Beschwerde vom 30. Juli 2020 gegen den Bescheid des  Finanzamtes X. (FA, jetzt Dienststelle des Finanzamt Freistadt Rohrbach Urfahr ) vom 10. Juli 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zur Steuernummer 63-102/2061  zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 (1) BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `KommR Lee Ponsard` | `KommR Lee Ponsard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Vanessa Nowikoff` (person)
- `Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `63-102/2061` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde des  OMedR Tanja Kubatsch, Sand/Bundesstraße 2, 4170 Damreith, Österreich, vom 21. Oktober 2022, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 21. September 2022, GZ. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `OMedR Tanja Kubatsch` | `OMedR Tanja Kubatsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Diana Sammer` (person)
- `Sand/Bundesstraße 2, 4170 Damreith, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/142867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142867.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden MMag. Gerald Erwin Ehgartner und die  weiteren Senatsmitglieder Mag. Elisabeth Traxler, Mag. Harald Zeller und Christian Ringseis in  der Beschwerdesache Muran Iossifidis, Birken-Siedlung 22, 4715 Unterstetten, Österreich, vertreten durch KPMG Alpen-Treuhand  GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  über die Beschwerde vom 30. August 2023 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 11. Juli 2023 betreffend Beschwerdezinsen (§ 205a BAO) nach  Durchführung einer mündlichen Verhandlung am 29. November 2023 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Elisabeth Traxler` | `Mag. Elisabeth Traxler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Mag. Harald Zeller` (person)
- `Christian Ringseis` (person)
- `Muran Iossifidis` (person)
- `Birken-Siedlung 22, 4715 Unterstetten, Österreich` (address)
- `KPMG Alpen-Treuhand  GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/148407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  des MedR Erna Noellgen, Diesting 46, 4151 Salaberg, Österreich, über dessen Beschwerde vom 7. November 2021 gegen den  Bescheid des Finanzamtes Österreich vom 8. Oktober 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 01-405/3031, zu Recht erkannt:   I. Der angefochtene Bescheid wird im Umfang der Beschwerdevorentscheidung vom  16. Mai 2022 abgeändert.

| Predicted | Gold |
|---|---|
| `MedR Erna Noellgen` | `MedR Erna Noellgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Diesting 46, 4151 Salaberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `01-405/3031` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_170`)


5. EINKOMMENSTEUER 2011 und 2012  WOHNSITZE der Bf.  Die Frage, ob eine Person in Österreich unbeschränkt steuerpflichtig ist, richtet sich nicht nach  Doppelbesteuerungsabkommen, sondern ausschließlich nach den inländischen  steuerrechtlichen Vorschriften.

**False Positives:**

- `Bf.  Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_52`)


Einem Untersuchungsbefund des KzlR Karola Priester vom 09.07.2018 ist neben der Diagnose: BA: Myoper  Astigmatismus zu entnehmen, dass ein ausführliches Beratungsgespräch, sowohl über die  Möglichkeit der konservativen Korrektur (Brille und/oder Kontaktlinsen), als auch über die  5 von 8 Seite 6 von 8

**False Positives:**

- `KzlR Karola Priester ` — partial — gold is substring of pred: `KzlR Karola Priester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Karola Priester`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_76`)


Aus dem Untersuchungsbefund des KzlR Karola Priester vom 09.07.2018 ist vielmehr ableitbar,  dass bei der Ehegattin des Bf auch die Möglichkeit der konservativen Korrektur der  Fehlsichtigkeit durch eine von der gesetzlichen Sozialversicherung im Rahmen des § 137 ASVG  bezahlte Brille und/oder durch von der gesetzlichen Krankenkasse im Rahmen des § 137 ASVG  bezahlte Kontaktlinsen bestanden hätte.

**False Positives:**

- `KzlR Karola Priester ` — partial — gold is substring of pred: `KzlR Karola Priester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Karola Priester`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_196`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Ag Bel des Bf.  Der Bf. macht diverse ag Bel für sich und seine Ehegattin geltend.

**False Positives:**

- `Bf.  Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_15`)


Mit Beschluss vom 24.10.2024 bewilligt der Verwaltungsgerichtshof der Dr.in Flora Lallemand  Verfahrenshilfe für die außerordentliche Revision gegen das Erkenntnis des  Bundesfinanzgerichts Außenstelle Linz vom 20.08.2024, RV/7100825/2024, betreffend  Umsatzsteuer und Körperschaftsteuer 2015.

**False Positives:**

- `Dr.in Flora Lallemand  ` — partial — gold is substring of pred: `Dr.in Flora Lallemand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Dr.in Flora Lallemand`(person)
- `Bundesfinanzgerichts`(organisation)

</details>

---

## `names_after_von_durch` 🏆

**F1:** 0.024 | **Precision:** 0.307 | **Recall:** 0.012  

**Format:** `regex`  
**Rule ID:** `4a85b31e`  
**Description:**
Matches names following 'von' or 'durch', strictly excluding company names and ensuring person-like structure (two capitalized words or initials).

**Content:**
```
(?:von|durch)\s+((?:[A-Z]\.[A-Z]\.|[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM|M\.B\.L\.)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Behörde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|Büro|Praxis|Klinik|Krankenhaus|Schule|Universität|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|Büro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftsprüfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunfähigkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Geschäftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.307 | 0.012 | 0.024 | 75 | 23 | 52 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 52 | 1828 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Dr Vana Dr Kolbitsch Mag Breitenecker` | `Dr Vana Dr Kolbitsch Mag Breitenecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr Christian Burghardt` | `Dr Christian Burghardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `StR Univ.-Prof. Alvin Paulikat` (person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_138`)


Stellungnahme zu Vorgutachten:   unverändert zum VGA   Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:   x ja   □ nein   GdB liegt vor seit: 05/2018   Begründung – GdB liegt rückwirkend vor:   siehe Vorgutachten   x Dauerzustand   Gutachten erstellt am 21.09.2020 von Sandro Vulbrecht  Gutachten vidiert am 21.09.2020 von Janet Aspenleitner

| Predicted | Gold |
|---|---|
| `Janet Aspenleitner` | `Janet Aspenleitner` |

**Missed by this rule (FN):**

- `Sandro Vulbrecht` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lieselotte Reinicker` | `Lieselotte Reinicker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Maria-Luise Wohlmayr` (person)
- `Raingasse 32, 9552 Ossiachberg, Österreich` (address)
- `Dr. X` (person)
- `Finanzamtes` (organisation)
- `FA Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag Kerstin Friedrich` | `Mag Kerstin Friedrich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Erwin Döpkemeier` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alfred Klaus Fenzl` | `Alfred Klaus Fenzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Hugo Engelsmann` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Michael Haberl` | `Michael Haberl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Dr.in Edith Lohhausen` (person)
- `Schmalohr + Kiekebusch Möbel` (organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Judenburg Liezen` (organisation)
- `71-763/1501` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi über die am 25. Mai 2022 eingebrachte  Beschwerde von Elvira Akcakaya, Dr. Ludwig-Straße 12, 4184 Neuling, Österreich, Firmenbuchnummer FN gegen die an  Beschuldigte gerichtete Vollstreckungsverfügung des Magistrates der Stadt Wien (MA 6 – BA  32) vom 18. Mai 2022, Zahl MA67/Zahl/2021, beschlossen:  Gemäß § 50 in Verbindung mit (iVm) § 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  die Beschwerde als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Elvira Akcakaya` | `Elvira Akcakaya` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Schabel` | `Peter Schabel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Jeremias Kierstan` (person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich` (address)
- `Magistrats  der Stadt Wien` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/141195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141195.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paula Tschann  in der Beschwerdesache Merlin Dankwort,  Urtelgasse 9y, 8232 Stambach, Österreich  vertreten durch Valerian Stamataki, Schanze 29 12, 3661 Unterthalheim, Österreich, über die Beschwerde vom  6. September 2022 gegen den Bescheid des Finanzamtes Österreich vom 9. August 2022  betreffend Festsetzung eines ersten Säumniszuschlages, Steuernummer 88-049/5894  nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valerian Stamataki` | `Valerian Stamataki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Paula Tschann` (person)
- `Merlin Dankwort` (person)
- `Urtelgasse 9y, 8232 Stambach, Österreich` (address)
- `Schanze 29 12, 3661 Unterthalheim, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-049/5894` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

| Predicted | Gold |
|---|---|
| `Helga Kraus` | `Helga Kraus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Cassandra Schmedtje` (person)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_19`)


Arztbrief vom 4. Juli 2022 der Gruppenpraxis X.:  T. leidet an Panikstörung, Vd.a. somatoforme Störung und Insomnie (Anamnese: Vorstellung  aufgrund von zunehmenden Panikattacken und Vd.a. somatoforme Störung, Beginn der  Symptome im November 2021)  Arztbrief von Dr. H.:  Beginn der Panikattacken und der krankheitsbedingten Symptome November 2021  Fachärztlicher Befundbericht von Dalibor Thübel vom 21. April 2022:  T. leidet an einer Panikstörung und mittelgradigen depressiven Episoden  Folgende Unterlagen betreffend den Schulbesuch von T. betreffend den Streitzeitraum wurden  vorgelegt:  Im Wintersemester 2020/21 wurden folgende Leistungen erbracht:  2 von 11 Seite 3 von 11

| Predicted | Gold |
|---|---|
| `Dalibor Thübel` | `Dalibor Thübel` |

**Missed by this rule (FN):**

- `Dr. H.` (person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dr. Martin Wadepfuhl  in der Beschwerdesache Renate Bürvenig,  Kreuzkapellenweg 7, 5151 Hochberg, Österreich, vertreten durch Ludmilla Flaumbaum, Herrengschwendt 3, 8761 Mühltal, Österreich, über die Beschwerde vom  15. Februar 2021 gegen die Bescheide des Finanzamtes Österreich vom 19. Jänner 2021  betreffend die Haftung für Lohnsteuer für 2015, 2016, 2017, 2018 und 2019, sowie den  Dienstgeberbeitrag zum FLAF für 2015, 2016, 2017, 2018 und 2019 und den Zuschlag zum  Dienstgeberbeitrag für 2015, 2016, 2017, 2018 und 2019 zu Steuernummer 74-041/7335  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ludmilla Flaumbaum` | `Ludmilla Flaumbaum` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Dr. Martin Wadepfuhl` (person)
- `Renate Bürvenig` (person)
- `Kreuzkapellenweg 7, 5151 Hochberg, Österreich` (address)
- `Herrengschwendt 3, 8761 Mühltal, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `74-041/7335` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/144197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lukas Escherle  in der Verwaltungsstrafsache gegen  Kirsten Schneppensiefen, Poppenreithstraße 26, 7461 Goberling, Österreich, vertreten durch Albert Höferlin  wegen der  Verwaltungsübertretung gemäß § 16 Abs 1 des Gebrauchsabgabegesetz, über die Beschwerde  der Beschuldigten vom 31.7.2023 gegen das Straferkenntnis des Magistrats der Stadt Wien  vom 14.7.2023 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe auf je € 20,00 (also EUR 100,00) herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Albert Höferlin` | `Albert Höferlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Lukas Escherle` (person)
- `Kirsten Schneppensiefen` (person)
- `Poppenreithstraße 26, 7461 Goberling, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/146104.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146104.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Georg Kunstmann  in der Beschwerdesache Gerhard Weinbergs,  Löwengrub 29, 8680 Hönigsberg, Österreich, vertreten durch Damian Eccardt, Unterort 18, 4673 Bernhartsdorf, Österreich, über die Beschwerde vom 8.  Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom 4. April 2023 betreffend  Umsatzsteuer 2013 sowie über die Beschwerden vom 23. August 2023 gegen die Bescheide  des Finanzamtes Österreich vom 4. August 2023 betreffend Umsatzsteuer 2014, 2015, 2016  und 2017 zu Steuernummer 50-546/1107  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Damian Eccardt` | `Damian Eccardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Georg Kunstmann` (person)
- `Gerhard Weinbergs` (person)
- `Löwengrub 29, 8680 Hönigsberg, Österreich` (address)
- `Unterort 18, 4673 Bernhartsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)
- `50-546/1107` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Rosamunde Löckemann, Kirchblickweg 224, 3754 Haselberg, Österreich, vertreten durch Esra Röhlen, Glasergasse 4, 4240 Vierhöf, Österreich, über die  Beschwerde vom 1. Juni 2023 egen die folgenden in den fünf Sammelbescheiden des  Finanzamtes für Großbetriebe vom 18. April 2023 (Zeitraum Jänner 2018 bis September 2022)  enthaltenen Bescheide des Finanzamtes für Großbetriebe über die „Abweisung von  Vergütungsanträgen gem. § 12a NoVAG 1991“ betreffend die im Spruch genannten Fahrzeuge  zu Recht erkannt:  I.  Die in den Sammelbescheiden enthaltenen Bescheide zu den folgenden Exportfahrzeugen  werden abgeändert.

| Predicted | Gold |
|---|---|
| `Esra Röhlen` | `Esra Röhlen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Rosamunde Löckemann` (person)
- `Kirchblickweg 224, 3754 Haselberg, Österreich` (address)
- `Glasergasse 4, 4240 Vierhöf, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `Finanzamtes für Großbetriebe` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Dipl.-Ing. Mag.a Andrea Johanningmeyer, Tenniszeile 8, 5424 Rengerberg, Österreich, vertreten durch Susanne Neuhäuser, Hartiggasse  22/23, 2700 Wiener Neustadt, vom 12. Dezember 2019 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom  26. November 2019 betreffend Zwangsstrafen 2019 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susanne Neuhäuser` | `Susanne Neuhäuser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniela Regina Denk` (person)
- `Dipl.-Ing. Mag.a Andrea Johanningmeyer` (person)
- `Tenniszeile 8, 5424 Rengerberg, Österreich` (address)
- `Finanzamt Schwechat Gerasdorf` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Caroline Bolzen, Patschweg 38, 9635 Nölbling, Österreich, vertreten durch Christine Maria Brunnthaller, Baumgarten 20 Tür  2, 3512 Mautern/Donau, über die Beschwerde vom 25. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 18. März 2024 betreffend Familienbeihilfe 07.2023-03.2024 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Maria Brunnthaller` | `Christine Maria Brunnthaller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Caroline Bolzen` (person)
- `Patschweg 38, 9635 Nölbling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/147002.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Franz Quapp  in der Beschwerdesache  Elvira Mathis, Claudiastraße 7, 2061 Hadres, Österreich, vertreten durch Wladimir Kreissl, Seibersdorf 3, 8141 Bierbaum, Österreich,  über die Beschwerde vom 13. Mai 2015 gegen den Bescheid des (damaligen) Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 9. April 2015  betreffend Säumniszuschlag 2015 Steuernummer 98-983/4004  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wladimir Kreissl` | `Wladimir Kreissl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Franz Quapp` (person)
- `Elvira Mathis` (person)
- `Claudiastraße 7, 2061 Hadres, Österreich` (address)
- `Seibersdorf 3, 8141 Bierbaum, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `98-983/4004` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anneliese Furtmeier  in der Beschwerdesache Werner Kachelek,  Heideweg-Siedlung 7, 4030 Linz, Österreich, vertreten durch Eugen Josef Bertsch, Sportplatzweg 11, 6811 Göfis, betreffend  Beschwerde vom 22. August 2019 gegen den Bescheid des FA Spittal Villach (nunmehr Finanzamt  Österreich) vom 29. Juli 2019 über die Abweisung eines Antrages auf Nachsicht gemäß § 236  BAO, Steuernummer 85-278/4119, beschlossen:  Der Vorlageantrag vom 30. September 2019 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 lit. d BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Eugen Josef Bertsch` | `Eugen Josef Bertsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Anneliese Furtmeier` (person)
- `Werner Kachelek` (person)
- `Heideweg-Siedlung 7, 4030 Linz, Österreich` (address)
- `FA Spittal Villach` (organisation)
- `Finanzamt  Österreich` (organisation)
- `85-278/4119` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Univ.-Prof.in Maja Lauers  in der Säumnisbeschwerdesache  Univ.-Prof. Mehmet Klasema, Labon 67, 4861 Looh, Österreich  vertreten durch Jonathan Goessl, über die Beschwerde vom 8. Jänner  2025 wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend Bescheidbeschwerde vom 12. April 2024 gegen den Bescheid betreffend die  Abweisung des Antrages auf Wiederaufnahme des Verfahrens gemäß § 303 BAO  (Körperschaftsteuer 2021) vom 13. März 2024, Steuernummer 85-153/1153, den Beschluss:  I. Das Säumnisbeschwerdeverfahren wird eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 in Verbindung mit  Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Jonathan Goessl` | `Jonathan Goessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Maja Lauers` (person)
- `Univ.-Prof. Mehmet Klasema` (person)
- `Labon 67, 4861 Looh, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `85-153/1153` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gregor Heumann, Weberweg 49, 4274 Steinbichl, Österreich, vertreten durch Stefan Josef Glechner, Am  Schwarzenbach 8, 4921 Hohenzell, über die Beschwerde vom 10. Februar 2023 gegen den  Bescheid des Finanzamtes Österreich vom 9. Jänner 2023 betreffend Feststellung der Einkünfte  § 188 BAO 2021 Steuernummer 31-405/5720  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stefan Josef Glechner` | `Stefan Josef Glechner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Gregor Heumann` (person)
- `Weberweg 49, 4274 Steinbichl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `31-405/5720` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Annika Streicher BA LL.M.(WU) in der  Beschwerdesache Dimitri Gaessner, Sauerbrunnberg 15, 8124 Neuhof, Österreich, vertreten durch Miriam Wurmehl, Bakk. phil., Windparkstraße 7, 5092 Gumping, Österreich, über die Beschwerde vom 13. Februar 2024 gegen den Bescheid des Finanzamtes  Österreich vom 16. Jänner 2024 betreffend Verspätungszuschlag / ESt 2020 Steuernummer  90-683/6114  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Miriam Wurmehl, Bakk. phil.` | `Miriam Wurmehl, Bakk. phil.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Annika Streicher BA LL.M.(WU)` (person)
- `Dimitri Gaessner` (person)
- `Sauerbrunnberg 15, 8124 Neuhof, Österreich` (address)
- `Windparkstraße 7, 5092 Gumping, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `90-683/6114` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

**False Positives:**

- `Sera Trust` — partial — pred is substring of gold: `Sera Trust GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Thomas Mevis`(person)
- `Lindenhang 30, 4591 Ramsau, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Astoria Stb` — partial — pred is substring of gold: `Astoria Stb GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein`(person)
- `Leroy Sitterle`(person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich`(address)
- `Astoria Stb GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_25`)


Ich beantrage eine bescheidmäßige Erklärung von Ihrer Seite, dass mit der Weitergabe von  Daten der Zulassungsbesitzerin keine Verletzung des Datenschutzgesetzes vorliegt."

**False Positives:**

- `Ihrer Seite` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

**False Positives:**

- `Fa Witago` — partial — pred is substring of gold: `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Dr. Wolfgang Aigner`(person)
- `Erwin Agneter`(person)
- `Mag. Belinda  Maria Eder`(person)
- `Xaver Plaumert, BEd`(person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich`(address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Mag. Katharina Moravec`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_80`)


*) Printartikel: Laut Artikel von R.R. in der Zeitschrift Printartikel, würden laut Angaben des V.  A. ca. 150.000 A. Portionen pro Jahr umgesetzt werden.

**False Positives:**

- `R.R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_66`)


Festsetzung von Anspruchszinsen  Dem gegenständlichen Bescheid liegt eine ausgewiesene Nachforderung laut  Einkommensteuerbescheid vom 11.12.2018 zu Grunde.

**False Positives:**

- `Anspruchszinsen  Dem` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `Maggi Brandl Kathollnig  Rechtsanwalts` — partial — pred is substring of gold: `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Weiß Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Hon.-Prof.in Elvira Thielsen`(person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_71`)


Ich warte noch immer auf den Ärztebrief von  Klinik Floridsdorf.

**False Positives:**

- `Klinik Floridsdorf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Kanzlei Kiffmann` — partial — pred is substring of gold: `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Zoltan Dabrowski`(person)
- `OMedR Prof. Hartmut Szardemings`(person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_143`)


A5) Bestellung von Zigaretten  Wie von Ihnen schriftlich angefordert haben wir Ihnen den Bestellvorgang von Zigaretten und  hier insbesondere die Frage, inwieweit die D.-Mitarbeiter in den Bestellvorgang involviert sind,  wie folgt schriftlich beantwortet (schriftliche Stellungnahme vom 5.12.2018):  12 von 30 Seite 13 von 30

**False Positives:**

- `Zigaretten  Wie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_13`)


Lt. Kaufvertrag zum Objekt 9999 (Wohn-/Betriebsadresse) vom 28.Dez.2009 sind beide  Hälfteeigentümer von Beruf Dolmetscher.

**False Positives:**

- `Beruf Dolmetscher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Herrn Mag` — positional overlap with gold: `Mag. Gernot Thonhauser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Jedamczik`(person)
- `ÖkR Tobias Schönyan`(person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich`(address)
- `Mag. Gernot Thonhauser`(person)
- `Finanzamtes Österreich`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Erich Allbrand,  ` — partial — gold is substring of pred: `Erich Allbrand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Robert Derici`(person)
- `Exlgasse 12, 9623 Karnitzen, Österreich`(address)
- `Erich Allbrand`(person)
- `12-876/0077`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_139`)


Wir dürfen hierzu auf das Schreiben von Richter Dr. V hinweisen, der in  seinem Schreiben vom 23.07.2019 darauf hinweist, dass die Bestellung trotz Austragung aus  der Sachverständigenliste erfolgt ist, um Verzögerungen bei gerichtlichen Verfahren zu  vermeiden.

**False Positives:**

- `Richter Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_81`)


Die Seite … gibt für die  Meldung anhand von Screenshots Hilfestellung.

**False Positives:**

- `Screenshots Hilfestellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Thomas Schmidt in der Finanzstrafsache  gegen Linda Tumpach, Gengerberg 44, 4052 Ansfelden, Österreich, vertreten durch Rechtsanwälte Gloß Pucher Leitner Gloß  Enzenhofer, Wiener Straße 3, 3100 St. Pölten, über die Beschwerde der Beschuldigten vom  25.11.2019 gegen den Bescheid des Amtes für Betrugsbekämpfung als Finanzstrafbehörde  (ehemals des Finanzamtes Lilienfeld St. Pölten als Finanzstrafbehörde ) vom 17. Oktober 2019,  Strafkontonummer 91-951/0670, betreffend die Abweisung eines  Zahlungserleichterungsansuchens (Stundungs- und Ratenansuchen) gemäß § 156 Abs. 1 des  Finanzstrafgesetzes (FinStrG) in Verbindung mit   § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) beschlossen:  Die Beschwerde wird als unzulässig zurückgewiesen, da es sich beim gegenständlich  bekämpften so genannten Bescheid um einen Nichtbescheid handelt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Rechtsanwälte Gloß Pucher Leitner Gloß  Enzenhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Thomas Schmidt`(person)
- `Linda Tumpach`(person)
- `Gengerberg 44, 4052 Ansfelden, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `91-951/0670`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_58`)


Die Tätigkeitsvergütungen des BF wurden von West Werktri GmbH ausbezahlt und auch (endgültig) von  der und von West Werktri GmbH getragen und nicht an die K Bioscienses AB in Schweden / F  weiterverrechnet.

**False Positives:**

- `West Werktri` — partial — pred is substring of gold: `West Werktri GmbH`
- `West Werktri` — similar text (different position): `West Werktri GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `West Werktri GmbH`(organisation)
- `West Werktri GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Herrn  Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Olaf Koechig, Zmöllach 3, 3542 Litschgraben, Österreich, Beschwerde vom 25. Oktober 2019 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr Finanzamtes Österreich, vom  28. November 2018 betreffend Umsatzsteuer 2012, Umsatzsteuer 2013, Umsatzsteuer 2014  und Umsatzsteuer 2015, Steuernummer 17-913/2665, der Gartfentri Heizung Institut GmbH, vertreten durch  Gustke Forschung GmbH, hinsichtlich des Vorlageantrages der Gartfentri Heizung Institut GmbH  in  Liquidation, beschlossen:  I. Die Beschwerdevorentscheidungen vom 6. April 2022 betreffend Umsatzsteuer 2012,  2013, 2014 und 2015 der Gartfentri Heizung Institut GmbH  in Liquidation werden aufgehoben.

**False Positives:**

- `Gustke Forschung` — partial — pred is substring of gold: `Gustke Forschung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Konrad`(person)
- `Olaf Koechig`(person)
- `Zmöllach 3, 3542 Litschgraben, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `17-913/2665`(tax_number)
- `Gartfentri Heizung Institut GmbH`(organisation)
- `Gustke Forschung GmbH`(organisation)
- `Gartfentri Heizung Institut GmbH`(organisation)
- `Gartfentri Heizung Institut GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Freimüller Rechtsanwalts` — partial — pred is substring of gold: `Freimüller Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Cornelia Reifgerste`(person)
- `Scherzergütl 18K, 9622 Golz, Österreich`(address)
- `Freimüller Rechtsanwalts GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `M. F.`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_36`)


Der Wirtschaftstreuhänder hat sich – soweit aktenkundig – (nur) durch die Anmerkung der  Zustellungsbevollmächtigung im Wege von Finanz Online gegenüber der Abgabenbehörde auf  die erteilte Bevollmächtigung berufen.

**False Positives:**

- `Finanz Online` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_20`)


Zusammenfassend bleibe zu sagen,  dass sein digitaler Parkschein zum Zeitpunkt des Strafzettels gültig gewesen sei (Verweis auf  die im Anhang beigefügte Bestätigung von Kurzparkservice Easypark).

**False Positives:**

- `Kurzparkservice Easypark` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_15`)


In den restlichen Wochen der Sommerferien entfällt sein  Regelkontaktrecht zu S.. Der Vater ist berechtigt, Adrian gemeinsam mit S. in der zweiten  Woche von Fabios Sommerferien durchgehend zu betreuen.

**False Positives:**

- `Fabios Sommerferien` — partial — gold is substring of pred: `Fabios`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Adrian`(person)
- `Fabios`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_42`)


Die gänzliche, ersatzlose  Aufhebung des Bescheides über die Festsetzung von Dritten Säumniszuschlägen vom 11.1.2016  eingelangt am 16.3.2016 wird hiermit ausdrücklich beantragt sowie die Aussetzung jeglicher  Exekutionsmaßnahmen und Aufschiebung der Vollstreckung gemäß § 18 Z 1 AbgEO.“

**False Positives:**

- `Dritten Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/143501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143501.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Dimitri Usslar  in der Beschwerdesache Jessica Abdulkarim,  vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien,  gegen den Bescheid des Finanzamtes Österreich vom 15. Mai 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Deloitte Tax Wirtschaftsprüfungs` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dimitri Usslar`(person)
- `Jessica Abdulkarim`(person)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_73`)


Möglicherweise seien sie aber "vor" Erteilung eines Auftrags durch Herrn Dr.  Alma Goerts  einfach nicht für diese Angelegenheit zuständig.

**False Positives:**

- `Herrn Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/143822.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143822.1_2`)


Das Bundesfinanzgericht hat durch den Senat 6008-1 besetzt mit dem Senatsvorsitzenden  Mag. Johann Fischerlehner, der beisitzenden Richterin Maga. Ulrike Stephan, sowie den  fachkundigen Laienrichtern Michael Hinterreiter, LL.B. und Leopold Pichlbauer in der  Beschwerdesache Philippa Aufheimer, Teichschloßweg 11, 8162 Haufenreith, Österreich, vertreten durch Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH, Bahnhofstraße 13, 4400 Steyr, über die Beschwerde vom 9. März  2023 gegen den Bescheid des Finanzamtes Österreich vom 22. Februar 2023 mit dem der  Antrag gemäß § 299 Abs. 1 Bundesabgabenordnung vom 29.07.2022, eingebracht am  29.07.2022, betreffend den Bescheid über die Wiederaufnahme des Verfahrens gemäß  § 303  Abs. 1 BAO vom 21.12.2021 abgewiesen wurde, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben und der angefochtene  Bescheid dahingehend abgeändert, dass der Bescheid vom 21. Dezember 2021, mit  dem die belangte Behörde zu Einheitswertaktenzeichen EW-AZ die  Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 BAO des mit Bescheid vom  13.12.2016 abgeschlossenen Verfahrens betreffend die Zurechnungsfortschreibung  gemäß § 21 Abs. 4 BeWG zum 01.01.2015 verfügt hat, aufgehoben wird.

**False Positives:**

- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung` — partial — pred is substring of gold: `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Michael Hinterreiter, LL.B.`(person)
- `Leopold Pichlbauer`(person)
- `Philippa Aufheimer`(person)
- `Teichschloßweg 11, 8162 Haufenreith, Österreich`(address)
- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_31`)


Die Magistratsabteilung 67 forderte den Bf. mit Schreiben vom 13. November 2023 unter  Anführung der ihm vorgeworfenen Verwaltungsübertretung auf, der Behörde binnen zwei  Wochen ab Zustellung des Schreibens durch Vorlage von geeigneten Beweismitteln  (Detailinformation des Ladevorganges von Wien Energie) glaubhaft zu machen, dass sich das  Fahrzeug im Lademodus befunden habe.

**False Positives:**

- `Wien Energie` — type mismatch — same span as gold: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Energie`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_86`)


Beweiswürdigung:  Der Sachverhalt ergibt sich aus den eigenen Wahrnehmungen und Anzeigedaten des  Kontrollorgans der Parkraumüberwachung, den zur Beanstandungszeit angefertigten Fotos  sowie den Auskünften von Wien Energie.

**False Positives:**

- `Wien Energie` — type mismatch — same span as gold: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Energie`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_92`)


Laut Auskunft von Wien Energie Support vom 26. Februar 2024 war der Ladevorgang des ggstl.

**False Positives:**

- `Wien Energie Support` — partial — gold is substring of pred: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Energie`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_94`)


Nach weiterer Auskunft von Wien Energie vom 12. März 2024, bei der der Ladevorgang noch  detaillierter dargestellt wurde, war der Ladevorgang erst um 17:16:48 Uhr beendet und der  Ladevorgang zur Beanstandungszeit durch das Parkraumüberwachungsorgan (16:33 Uhr)  ausgesetzt.

**False Positives:**

- `Wien Energie` — type mismatch — same span as gold: `Wien Energie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Energie`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Gustav Franzki, Strebersdorfer Friedhof 80, 4712 Haus, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  14. Dezember 2023 gegen den Bescheid des Finanzamtes für Großbetriebe vom 17. November  2023 betreffend Festsetzung Energiekrisenbeitrag-Strom Dezember 2022 bis Juni 2023,  Steuernummer 92-724/7552  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Krafft`(person)
- `Gustav Franzki`(person)
- `Strebersdorfer Friedhof 80, 4712 Haus, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `92-724/7552`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Calvin Liechtenstein  in der Beschwerdesache KommR Thorsten Voelkerling,  Kirchenbühl 12, 4463 Brunnbach, Österreich, vertreten durch Rechtsanwalt Dr. Gahleithner & Partner OG, Schottengasse 7  Tür 6, 1010 Wien, über die Beschwerde vom 25. September 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 11. September 2019 betreffend den Ablauf der Aussetzung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwalt Dr` — positional overlap with gold: `Dr. Gahleithner & Partner OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Calvin Liechtenstein`(person)
- `KommR Thorsten Voelkerling`(person)
- `Kirchenbühl 12, 4463 Brunnbach, Österreich`(address)
- `Dr. Gahleithner & Partner OG`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Aloisia Bergauer in der Beschwerdesache  Ing. Christian Marckwordt, Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  8. Februar 2024 gegen den Bescheid des Finanzamtes Österreich vom 18. Jänner 2024  betreffend Festsetzung Energiekrisenbeitrag Strom für den Zeitraum 1.12.2022-30.06.2023,  Steuernummer 22-821/5972, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Aloisia Bergauer`(person)
- `Ing. Christian Marckwordt`(person)
- `Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `22-821/5972`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/145625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145625.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Fatima Auriga, Tiflisbrücke 7, 8673 Kirchenviertel, Österreich, vertreten durch Sachwalter Dr. Herbert Kaspar sowie die Vindobona-Interbruch  Wirtschaftstreuhand GmbH, Opernring 10/Eingang Goethegasse 3, 1010 Wien, über die  Beschwerde vom 6. Oktober 2020 gegen den Bescheid des Finanzamtes Österreich vom 16. Juli  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018, Steuernummer  36-261/6228  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Sachwalter Dr` — positional overlap with gold: `Dr. Herbert Kaspar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Fatima Auriga`(person)
- `Tiflisbrücke 7, 8673 Kirchenviertel, Österreich`(address)
- `Dr. Herbert Kaspar`(person)
- `Finanzamtes Österreich`(organisation)
- `36-261/6228`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_281`)


Zudem sind im Rahmen einer  sachgerechten Schätzung auch Umstände zugunsten des Steuerpflichtigen zu berücksichtigen  und ggf zu schätzen (vgl zB zur Schätzung von Vorsteuern Ritz, BAO6, § 184 Rz. 2).

**False Positives:**

- `Vorsteuern Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Wladimir Schaeffer  in der Beschwerdesache  Scarlett Ever, Felle 6, 4264 Unterrauchenödt, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom  10. Oktober 2024 gegen den Bescheid des Finanzamtes für Großbetriebe vom 18. September  2024 betreffend Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 1. Juli  2023 bis 31. Dezember 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Wladimir Schaeffer`(person)
- `Scarlett Ever`(person)
- `Felle 6, 4264 Unterrauchenödt, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Niklas Hussung  in der Beschwerdesache Univ.-Prof. Oliver Ruhsbüldt,  Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich, vertreten durch Gattringer Steuerberatung GmbH, Sonnensteinstraße 12, 4040  Linz, über die Beschwerde vom 31. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 16. Mai 2023 betreffend Einkommensteuer 2021 Steuernummer 26-058/9655  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gattringer Steuerberatung` — partial — pred is substring of gold: `Gattringer Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Niklas Hussung`(person)
- `Univ.-Prof. Oliver Ruhsbüldt`(person)
- `Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich`(address)
- `Gattringer Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `26-058/9655`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_470`)


Zur Akne-/Narbenbehandlung  07.02.2013 € 43,74 3 * Teebaum Medicamo24 Dr.S   31.05.2013 € 43,74 3* Teebaum Medicamo24 Theodora Hartzheim, BA Bakk. phil.  Ansicht FA:  Es liegt eine zeitnahe ärztliche Verordnung vom 25.3.2013 vor (Anm.: von Theodora Hartzheim, BA Bakk. phil. mit dem  Vermerk „Akne, Fructoseintoleranz, Zöliakie, Milchunverträglichkeit“).

**False Positives:**

- `Theodora Hartzheim` — similar text (different position): `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)
- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_510`)


In der Pilzmischung der Fa. Orthotherapia GmbH ist  Lutein als Inhaltsstoff angeführt, von Theodora Hartzheim, BA Bakk. phil. wurde Lutamax (Inhaltsstoff ebenfalls Lutein) als 6  Monatskur verordnet.

**False Positives:**

- `Theodora Hartzheim` — partial — pred is substring of gold: `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_382`)


In Konsequenz ist die beschwerdeführende Partei nicht  berechtigt, die Vorsteuerabzüge aus den von Eberler Bau KG  B KG, C KG, D KG, E KG und F KG erhaltenen  Rechnungen geltend zu machen.

**False Positives:**

- `Eberler Bau` — partial — pred is substring of gold: `Eberler Bau KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Eberler Bau KG`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/147343.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Bruno Kleinerts, Emil-Bertalanffy-Weg 4, 9422 Mitterpichling, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1/Freyung, 1010 Wien, über die Beschwerde vom  22. November 2024 gegen die Bescheide des Finanzamtes für Großbetriebe vom 30. August  2024 betreffend Umsatzsteuerzinsen für die Zeiträume 2015, 2016, 01-12/2017, 01-05/2018,  07-09/2018 und 11-12/2018, Steuernummer 41-358/9193, zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Deloitte Tax  Wirtschaftsprüfungs` — partial — pred is substring of gold: `Deloitte Tax  Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Bruno Kleinerts`(person)
- `Emil-Bertalanffy-Weg 4, 9422 Mitterpichling, Österreich`(address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `41-358/9193`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/147347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147347.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Tatjana Siegerist, Bakk. phil., Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich, vertreten durch Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH, Wiesentalstraße 40, 90419 Nürnberg, Deutschland, über die  Beschwerde vom 27. Juli 2023 gegen den Bescheid des Magistrats der Stadt Wien, MA 6  Rechnungs- und Abgabenwesen, MA 6/ARL-676259-2022, vom 28. Juni 2023 betreffend  Haftung zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Molitor Babel Singer Vitzthum` — partial — pred is substring of gold: `Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Lisa Fries`(person)
- `Tatjana Siegerist, Bakk. phil.`(person)
- `Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich`(address)
- `Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH`(organisation)
- `Magistrats der Stadt Wien`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Ing. Dagobert Almasri, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

**False Positives:**

- `Sera Trust` — partial — pred is substring of gold: `Sera Trust GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Ing. Dagobert Almasri`(person)
- `Übersbachgasse 50, 2100 Langenzersdorf, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/147955.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147955.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christian Soltendieck  in der Beschwerdesache des Dr. MV  als Masseverwalter (MV) im Insolvenzverfahren der Berthold Grosshans, Gruisla 3Q, 3231 Linsberg, Österreich  vertreten durch  die Berthold Grosshans, Seetal 31, 4661 Altmanning, Österreich  nunmehr vertreten durch Rechtsanwalt Mag. Gregor  Kohlbacher, Keesgasse 11, 8010 Graz, betreffend die Beschwerde vom 12. Oktober 2020 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 15. Mai 2020 über die Zurückweisung eines  Antrages auf Wiedereinsetzung in den vorigen Stand (hinsichtlich Umsatzsteuer 2014 bis 2017  und Umsatzsteuer 1-11/2018), Steuernummer 59-309/9934, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Rechtsanwalt Mag` — positional overlap with gold: `Mag. Gregor  Kohlbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Christian Soltendieck`(person)
- `Berthold Grosshans`(person)
- `Gruisla 3Q, 3231 Linsberg, Österreich`(address)
- `Berthold Grosshans`(person)
- `Seetal 31, 4661 Altmanning, Österreich`(address)
- `Mag. Gregor  Kohlbacher`(person)
- `Finanzamtes Graz-Stadt`(organisation)
- `59-309/9934`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_197`)


Dementsprechend bewirken Aufwendungen auf das Mietobjekt (einschließlich  AfA) auch schon vor der Erzielung von Einkünften Werbungskosten, weiters aber auch  Aufwendungen, die während einer Zeit der Unterbrechung der Einnahmenerzielung anfallen.

**False Positives:**

- `Einkünften Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/148639.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148639.1_38`)


Der Selbstbehalt wurde daher im Erstbescheid, in dem das Finanzamt noch von Einkünften Ihres  Ehegatten von höchsten 6.000,00 € ausging, wie folgt ermittelt:  36.651,52 Einkommen  + 7.843,08 sonstige Bezüge, Kz 220 des Lohnzettels  - 940,78 SV-Beiträge für sonstige Bezüge, Kz 225 des Lohnzettels  43.553,82 Bemessungsgrundlage  11 % Prozentsatz gemäß § 34 Abs. 4 EStG  4.790,92 Selbstbehalt (11 % der Bemessungsgrundlage)

**False Positives:**

- `Einkünften Ihres  Ehegatten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Bernhart Steuerberatungs` — partial — pred is substring of gold: `Bernhart Steuerberatungs  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

</details>

---

## `names_with_suffixes_fixed` 💣

**F1:** 0.004 | **Precision:** 0.182 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `81b61954`  
**Description:**
Matches names with suffixes (BEd, LL.M., etc.) including multi-suffixes like M.B.L., ensuring strict boundaries.

**Content:**
```
(?:^|\n|\.|\s)(?:Frau\s+|Herr\s+|\s)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+|[A-Z][a-zäöüß]+-[A-Z][a-zäöüß]+)+\s*,?\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM|M\.B\.L\.))(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Behörde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|Büro|Praxis|Klinik|Krankenhaus|Schule|Universität|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|Büro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftsprüfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunfähigkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Geschäftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.182 | 0.002 | 0.004 | 22 | 4 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 18 | 1847 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valentin Joebges, LLM` | `Valentin Joebges, LLM` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Stephan` (person)
- `Bärngarten 17, 9713 Hochegg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `84-167/9727` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dominika Juhass  in der Beschwerdesache  Ludmilla Hühnerfuß, Bakk. techn., Singham 20, 3465 Unterstockstall, Österreich,   über die Beschwerde vom 27. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom  12. Juni 2019 betreffend Vorsteuererstattung 2018 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ludmilla Hühnerfuß, Bakk. techn.` | `Ludmilla Hühnerfuß, Bakk. techn.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Dominika Juhass` (person)
- `Singham 20, 3465 Unterstockstall, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Anton Böckamp, Bakk. techn., Leopold Kunschak Gasse 25, 9343 Dielach, Österreich, über die Beschwerde vom 8. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich (vormals Finanzamt Gänserndorf Mistelbach, § 323b BAO) vom  25. November 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 84-669/5568  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO im Sinne des Beschwerdebegehrens  abgeändert.

| Predicted | Gold |
|---|---|
| `Anton Böckamp, Bakk. techn.` | `Anton Böckamp, Bakk. techn.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Leopold Kunschak Gasse 25, 9343 Dielach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Gänserndorf Mistelbach` (organisation)
- `84-669/5568` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/147347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147347.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Tatjana Siegerist, Bakk. phil., Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich, vertreten durch Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH, Wiesentalstraße 40, 90419 Nürnberg, Deutschland, über die  Beschwerde vom 27. Juli 2023 gegen den Bescheid des Magistrats der Stadt Wien, MA 6  Rechnungs- und Abgabenwesen, MA 6/ARL-676259-2022, vom 28. Juni 2023 betreffend  Haftung zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Tatjana Siegerist, Bakk. phil.` | `Tatjana Siegerist, Bakk. phil.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Lisa Fries` (person)
- `Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich` (address)
- `Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH` (organisation)
- `Magistrats der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mirha Karahodzic MA` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Elisabeth Schafstall`(person)
- `Leithagürtel 20, 4251 Steinwald, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Theodora Urbanova, Bakk. iur.` — partial — gold is substring of pred: `Theodora Urbanova, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Theodora Urbanova, Bakk. iur.`(person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `54-205/5010`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Dora Szczepanowski`(person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_24`)


2. Sachverhalt   Die Bf., eine Gemeinde im Kärntner Bezirk XY mit ca. xxx Einwohnern, war in den Streitjahren -  neben der Republik Österreich bzw. später der Bundesimmobiliengesellschaft -  grundbücherliche Miteigentümerin der Liegenschaft vorgetragen in der EZ xxx GB xxxxx Ort,  samt dem darauf befindlichen Amts-, Kultur- und Geschäftszentrum mit der Adresse Ort Hnr..

**False Positives:**

- `Sachverhalt   Die Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Roland Rößle, Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich, über die Beschwerde des  Beschuldigten vom 7. April 2022 gegen den Zurückweisungsbescheid des Magistrates der Stadt  Wien vom 5. April 2022, Zahl: MA67/216700658355/2021, mit dem der Einspruch vom 18.  Februar 2022 gegen die Strafverfügung vom 3. September 2021 mit derselben Geschäftszahl  gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Sebastian Pfeiffer LL.M.` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Roland Rößle`(person)
- `Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich`(address)
- `Magistrates der Stadt  Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Robert Derici`(person)
- `Exlgasse 12, 9623 Karnitzen, Österreich`(address)
- `Erich Allbrand`(person)
- `12-876/0077`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_18`)


Das Bundesfinanzgericht hat erwogen:  Sachverhalt  Der Bf., welcher Staatsangehöriger eines Mitgliedstaates der Europäischen Union ist, bezog  unstrittig im Zeitpunkt der Erlassung des gegenständlich bekämpften Bescheides  Familienbeihilfe und Kinderabsetzbeträge für seine drei bzw. ab Oktober 2019 vier in Polen  wohnhaften Kinder, welche aufgrund der zum damaligen Zeitpunkt geltenden innerstaatlichen  Bestimmung des § 8a FLAG 1967 seit Jänner 2019 einer Indexierung unterworfen wurde.

**False Positives:**

- `Sachverhalt  Der Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Europäischen Union`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_17`)


Das Bundesfinanzgericht hat erwogen:  Sachverhalt   Die Bf., welche Staatsangehörige eines Mitgliedstaates der Europäischen Union ist, bezog  unstrittig im Zeitpunkt der Erlassung des gegenständlich bekämpften Bescheides  Familienbeihilfe und Kinderabsetzbeträge für ihre beiden in der tschechischen Republik  wohnhaften Kinder, welche aufgrund der zum damaligen Zeitpunkt geltenden innerstaatlichen  Bestimmung des § 8a FLAG 1967 seit Jänner 2019 einer Indexierung unterworfen wurde.

**False Positives:**

- `Sachverhalt   Die Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Europäischen Union`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Annette Preußing, Am Neufeldersee 40, 3385 Uttendorf, Österreich, über die Beschwerde des  Beschuldigten vom 23. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 18. Jänner 2023, Zahl MA67/Zahl/2022, mit dem der Einspruch vom 6. Jänner  2023  gegen die Strafverfügung vom 4. Oktober 2022 mit derselben Geschäftszahl gemäß § 49  Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der  angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Sebastian Pfeiffer LL.M.` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Annette Preußing`(person)
- `Am Neufeldersee 40, 3385 Uttendorf, Österreich`(address)
- `Magistrates der  Stadt Wien`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/139968.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139968.1_22`)


Das Bundesfinanzgericht hat erwogen:  Sachverhalt   Der Bf., welcher Staatsangehöriger eines Mitgliedstaates der Europäischen Union ist, bezog  unstrittig im Zeitpunkt der Erlassung des gegenständlich bekämpften Bescheides  Familienbeihilfe und Kinderabsetzbeträge für seine drei in der Ungarn wohnhaften Kinder,  welche aufgrund der zum damaligen Zeitpunkt geltenden innerstaatlichen Bestimmung des  § 8a FLAG 1967 seit Jänner 2019 einer Indexierung unterworfen wurde.

**False Positives:**

- `Sachverhalt   Der Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Europäischen Union`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/141441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141441.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Finn Rosen  in der Beschwerdesache Dragan Ohlff,  vertreten durch Dr. Sven Rudolf Thorstensen LLM, Neustiftgasse 3/7, 1070 Wien, über die  Beschwerde vom 23. Juli 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom  10. Juli 2019 betreffend den Bescheid über den Ablauf einer Aussetzung der Einhebung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Sven Rudolf Thorstensen LLM` — partial — pred is substring of gold: `Dr. Sven Rudolf Thorstensen LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dr. Finn Rosen`(person)
- `Dragan Ohlff`(person)
- `Dr. Sven Rudolf Thorstensen LLM`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Saphira Schnaak`(person)
- `Kürschner Allee 44, 9300 Mail, Österreich`(address)
- `Ing. Mag. Hamza Ovacin`(person)
- `Finanzamtes Österreich`(organisation)
- `50-980/9446`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_22`)


Ergebnis der durchgeführten Begutachtung:   1 Sehstörungen, Störung des zentralen Sehens (Sehschärfe mit Korrektur)      Angeborene Hornhauttrübung BA, Hornhautvaskularisation BA,      Mikrophthalamus und kongenitale Sklerokorona                                                          Pos. Nr. 11.02.01                   GdB 100 %  Gesamtgrad der Behinderung                 100 v. H.   ……  Stellungnahme zu Vorgutachten: unverändert   GdB liegt vor seit:        07/1989   ……..  2 von 15 Seite 3 von 15

**False Positives:**

- `Angeborene Hornhauttrübung BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_53`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf., ein österreichisches Handelsunternehmen, hat durch ihre steuerliche Vertretung mit  Schreiben vom 17.08.2014 beim Finanzamt einen Antrag auf Ausstellung eines  Auskunftsbescheids nach § 118 BAO eingebracht.

**False Positives:**

- `Sachverhalt   Die Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Leopold Dobertin, Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich, über die Beschwerden gegen Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg   vom 30. Oktober 2015 gegen den Bescheid vom 9. Oktober 2015 betreffend Festsetzung von  zweiten Säumniszuschlägen,  vom 2. März 2016 gegen den Bescheid vom 11. Jänner 2016 betreffend Festsetzung von dritten  Säumniszuschlägen und  vom 2.1.2020 gegen den Bescheid vom 13.12.2019 betreffend Aufhebung/Abänderung von  Nebengebühren  nach der am 4.12.2023 am Bundesfinanzgericht in Wien über Antrag der Partei (§ 78 BAO  i.V.m. § 274 Abs. 1 Z 1 BAO) in Abwesenheit der Beschwerdeführerin bzw ihrer Vertretung und  in Anwesenheit von Mag. Martin Holzapfel und Mag. Sebastian Rivo-Wastl, BA für die belangte  Behörde durchgeführten mündlichen Verhandlung zur Steuernummer 38-992/7403  zu  Recht erkannt:   I. Der Beschwerde vom 30.10.2015 wird teilweise Folge gegeben und zweite  Säumniszuschläge in Höhe von 5.739,66 € festgesetzt.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Leopold Dobertin`(person)
- `Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Mag. Martin Holzapfel`(person)
- `Mag. Sebastian Rivo-Wastl, BA`(person)
- `38-992/7403`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/145448.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145448.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Ilhan Wolfer, Bakk. phil., Kleinsemmeringstraße 12, 3623 Singenreith, Österreich, (Beschwerdeführer, abgekürzt: Bf.), in  Erledigung der Säumnisbeschwerde vom 25. März 2024 wegen vorgebrachter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich hinsichtlich Einkommensteuer für die  Jahre 2001 bis 2005, Steuernummer 15-079/6612 :  I.) zu Recht erkannt:  Aufgrund der hinsichtlich Einkommensteuer 2004 auf das Bundesfinanzgericht übergegan- genen Zuständigkeit zur Entscheidung über die gemäß § 295 Abs. 1 Bundesabgabenordnung  (BAO) von Amts wegen vorzunehmende, geänderte Festsetzung der Abgabe wird die  Einkommensteuer des Beschwerdeführers für das Jahr 2004 mit -15.455,21 € festgesetzt.

**False Positives:**

- `Beschwerdesache Ilhan Wolfer, Bakk. phil.` — partial — gold is substring of pred: `Ilhan Wolfer, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `Ilhan Wolfer, Bakk. phil.`(person)
- `Kleinsemmeringstraße 12, 3623 Singenreith, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `15-079/6612`(tax_number)
- `Bundesfinanzgericht`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146522.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Francois Roeder, Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich, über die Beschwerde vom 12. Juni 2023 gegen  den Bescheid des Finanzamtes Österreich vom 9. Mai 2023 betreffend Säumniszuschlag 2023  nach der am 22.11.2024 am Bundesfinanzgericht in Wien über Antrag der Partei abgehaltenen  mündlichen Verhandlung in Abwesenheit des Beschwerdeführers und in Anwesenheit von  Bernadette Pommer BA MA für das Finanzamt sowie der Schriftführerin Mag. Magdalena  Preslmayr zur Steuernummer 48-847/1680  zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung eines ersten  Säumniszuschlages vom 9.5.2023 in Höhe von € 148,00 wird gemäß § 279 BAO als  unbegründet abgewiesen.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Francois Roeder`(person)
- `Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Bernadette Pommer`(person)
- `Finanzamt`(organisation)
- `Mag. Magdalena  Preslmayr`(person)
- `48-847/1680`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Leya Mentzel, MSc` — partial — pred is substring of gold: `Mag.a Dipl.-Ing. Leya Mentzel, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

</details>

---

## `names_after_born_son` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `47bc838c`  
**Description:**
Matches names following 'geborenen Sohn' (born son) to capture the child's name.

**Content:**
```
geborenen\s+Sohn\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Gericht|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `names_at_sentence_start_with_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e5f98ffe`  
**Description:**
Matches names at the start of a sentence or after specific legal context markers (Beschwerdesache, etc.) to reduce false positives from random capitalized words.

**Content:**
```
(?:^|\n|\.)\s+(?:in\s+der\s+)?Beschwerdesache(?:\s+des)?\s+((?:Dr\.|Mag\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|StR\s+|Techn\s+R\s+|OSR\s+|RA\s+|Bf\.|Bf\.(?:in)?|Herr|Frau|\u00d6kR|HR|KR|Ri\.|R\.)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `names_at_sentence_start_tightened` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e9e292d7`  
**Description:**
Matches names at sentence start but requires a title (Dr., Mag., etc.) or specific legal context to avoid false positives from common nouns.

**Content:**
```
(?:^|\n|\.)\s+(?:in\s+der\s+)?Beschwerdesache(?:\s+des)?\s+((?:Dr\.|Mag\.|Mag\.Dr\.|Dr\.in|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|StR\s+|Techn\s+R\s+|OSR\s+|RA\s+|Bf\.|Bf\.(?:in)?|Herr|Frau|\u00d6kR|HR|KR|Ri\.|R\.|OMedR|KommR|RgR|MedR|KzlR|MMag\.|Prof\.)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `names_after_vormaliger_steuerlicher` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4671f9c3`  
**Description:**
Matches names following 'vormaliger steuerlicher Vertreter' including suffixes.

**Content:**
```
vormaliger\s+steuerlicher\s+Vertreter,?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+(?:\s*,?\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `names_after_techn_r` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `42c6af6a`  
**Description:**
Matches names following 'Techn R' including suffixes like MBA, ensuring the title is part of the match.

**Content:**
```
Techn\s+R\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+(?:\s*,?\s*(?:BSc|BEd|MA|LL\.M\.|Bakk\.(?:\s+iur\.|\s+phil\.|\s+art\.|\s+techn\.)|LLB|BA|PhD|OMedR|KommR|RgR|MedR|OSR|Techn\s+R|Bf\.(?:in)?|VetR|MBA|StR|RA|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Techn\s+R\s+Dipl\.-Ing\.|Mag\.(?:a|\.\s+a)|MSc|LLM)?)?)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Beh\u00f6rde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|B\u00fcro|Praxis|Klinik|Krankenhaus|Schule|Universit\u00e4t|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|B\u00fcro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftspr\u00fcfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunf\u00e4higkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Gesch\u00e4ftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Chen Geßlein  in der Beschwerdesache MedR Techn R Mathilda Elfeldt,  Klingengasse 112, 9556 Waggendorf, Österreich, vertreten durch Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH, Kurandtplatz 1, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 29. Jänner  2021 gegen den Bescheid des Finanzamt Vorarlberg  vom 18. Jänner 2021 betreffend Einkommensteuer  2019 Steuernummer 43-811/9169  zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Mathilda Elfeldt` — partial — pred is substring of gold: `MedR Techn R Mathilda Elfeldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Chen Geßlein`(person)
- `MedR Techn R Mathilda Elfeldt`(person)
- `Klingengasse 112, 9556 Waggendorf, Österreich`(address)
- `Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH`(organisation)
- `Finanzamt Vorarlberg`(organisation)
- `43-811/9169`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Techn R Christina Heising, Angerweg 46, 4672 Unterseling, Österreich, vom 13. Februar 2023, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner 2023, Zahl MA67/Zahl1/2022, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für  Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Christina Heising` — partial — pred is substring of gold: `Techn R Christina Heising`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Techn R Christina Heising`(person)
- `Angerweg 46, 4672 Unterseling, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

</details>

---

## `names_with_phd_title` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `89216386`  
**Description:**
Matches names specifically with 'PhD' title, ensuring the full name and suffix are captured.

**Content:**
```
(?:PhD)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+|[A-Z][a-zäöüß]+-[A-Z][a-zäöüß]+)+)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Behörde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|Büro|Praxis|Klinik|Krankenhaus|Schule|Universität|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|Büro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftsprüfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunfähigkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Geschäftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_11`)


Fristgerecht wurde bekanntgegeben, dass das Fahrzeug zur Beanstandungszeit PhD Wilhelm Reschke, MBA,  Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich (= Beschwerdeführer, kurz: Bf.) überlassen war.

**False Positives:**

- `Wilhelm Reschke` — partial — pred is substring of gold: `PhD Wilhelm Reschke, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Wilhelm Reschke, MBA`(person)
- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich`(address)

</details>

---

## `names_with_maga_title` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a5d54a3b`  
**Description:**
Matches names with 'Maga.' (Magistra) title, ensuring the full name is captured.

**Content:**
```
(?:Maga\.)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+|[A-Z][a-zäöüß]+-[A-Z][a-zäöüß]+)+)(?=\s*(?:,|\.|\)|$|in\s+der|von|durch|vertreten|GmbH|KG|AG|Gesellschaft|Finanzamt|Behörde|Amt|Verwaltung|Firma|Unternehmen|Betrieb|Werk|Fabrik|Produktion|Dienstleistung|Beratung|Büro|Praxis|Klinik|Krankenhaus|Schule|Universität|Hochschule|Institute|Organisation|Verein|Stiftung|Kommission|Ausschuss|Gremium|Delegation|Vertretung|Botschaft|Konsulat|Mission|Büro|Zentrale|Niederlassung|Filiale|Abteilung|Referat|Sektion|Bereich|Sparte|Division|Konzern|Gruppe|Holding|Gesellschaftsform|Rechtsform|Steuerberatung|Wirtschaftsprüfung|Rechnungslegung|Buchhaltung|Finanzierung|Kredit|Darlehen|Hypothek|Versicherung|Pension|Rentenversicherung|Krankenversicherung|Unfallversicherung|Haftpflichtversicherung|Lebensversicherung|Sachversicherung|Rechtsschutzversicherung|Berufsunfähigkeitsversicherung|Krankenhausversicherung|Krankenhauskosten|Arztkosten|Heilbehandlung|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|Wochen|Monaten|Jahren|Tages|Monates|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates|Heilbehandlung|Arztkosten|Spitalskosten|Kurkosten|Therapiekosten|Kosten|Betrag|Summe|Zahl|Nr|Abs|Z|Punkt|Spruchpunkt|Familienbeihilfe|Personen|Wohnsitz|Geschäftsleitung|Sitz|Inland|Verfahren|Beschluss|Entscheidung|Bundesfinanzgericht|Magistrat|Stadt|Finanzamt|Gericht|Richter|Anwalt|Notar|Vertreter|Bf\.|Bf\.(?:in)?|Gesellschaft|GmbH|KG|AG|Steuerberatung|Rechtsanwalts|Notar|Partnerschaft|Bl|f\.|Strafe|Strasse|Weg|Gasse|Platz|Nr|Nummer|Hausnummer|Zl|Zahl|Ziffer|vom|gegen|betreffend|wegen|in\s+der|Wochen|Monaten|Jahren|Tages|Monates))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/143822.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143822.1_2`)


Das Bundesfinanzgericht hat durch den Senat 6008-1 besetzt mit dem Senatsvorsitzenden  Mag. Johann Fischerlehner, der beisitzenden Richterin Maga. Ulrike Stephan, sowie den  fachkundigen Laienrichtern Michael Hinterreiter, LL.B. und Leopold Pichlbauer in der  Beschwerdesache Philippa Aufheimer, Teichschloßweg 11, 8162 Haufenreith, Österreich, vertreten durch Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH, Bahnhofstraße 13, 4400 Steyr, über die Beschwerde vom 9. März  2023 gegen den Bescheid des Finanzamtes Österreich vom 22. Februar 2023 mit dem der  Antrag gemäß § 299 Abs. 1 Bundesabgabenordnung vom 29.07.2022, eingebracht am  29.07.2022, betreffend den Bescheid über die Wiederaufnahme des Verfahrens gemäß  § 303  Abs. 1 BAO vom 21.12.2021 abgewiesen wurde, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben und der angefochtene  Bescheid dahingehend abgeändert, dass der Bescheid vom 21. Dezember 2021, mit  dem die belangte Behörde zu Einheitswertaktenzeichen EW-AZ die  Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 BAO des mit Bescheid vom  13.12.2016 abgeschlossenen Verfahrens betreffend die Zurechnungsfortschreibung  gemäß § 21 Abs. 4 BeWG zum 01.01.2015 verfügt hat, aufgehoben wird.

**False Positives:**

- `Ulrike Stephan` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Michael Hinterreiter, LL.B.`(person)
- `Leopold Pichlbauer`(person)
- `Philippa Aufheimer`(person)
- `Teichschloßweg 11, 8162 Haufenreith, Österreich`(address)
- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1258, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_60`)

Weiters  wurde die Herbeischaffung des Aktes der WKStA zur AZ: AktWKStA, dessen Inhalt die  Übertragung der Meldepflicht gemäß § 9 VStG auf Herrn **Angelstein** beweisen soll, beantragt.

- missed: `Angelstein` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_293`)

Nach ständiger Rechtsprechung des EuGH ist  dieser Sachverhalt ausreichend, um eine hinreichend enge Anknüpfung an das Gebiet der  Union anzunehmen (EuGH vom 12. Juli 1984, C-237/83, Rs Prodest Rn 6; nochmals EuGH Rs  R.L. **Aldewereld** Rn 14).

- missed: `Aldewereld` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_7`)

Gegen diese Bescheide  habe das **Jaden Knauss**  fristgerecht eine Bescheidbeschwerde erhoben, die bis dato im  fortgesetzten Verfahren vor dem Bundesfinanzgericht noch nicht entschieden worden sei.

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_44`)

Auf dem Ausweis von RA1, ausgestellt von der RA-Kammer, wird ein **Dr. Karl**  RA1 ausgewiesen.

- missed: `Dr. Karl` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerde des  **Karim Hainzlmeier**, Gälaplana 43, 3205 Mühlhofen, Österreich, gegen den Bescheid des Finanzamtes Bregenz vom 20. Mai 2016  betreffend Einkommensteuer 2015, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Karim Hainzlmeier` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_46`)

Da das Beschwerdeverfahren gegen Frau A B als Geschäftsführerin der **Saskia Sinnwell**  und somit  als Entscheidungsträgerin iSd § 3 Abs. 2 VbVG kein rechtswidriges oder schuldhaftes Verhalten  ergeben hat, liegen die Voraussetzungen für die Verhängung einer Geldbuße über die  Saskia Sinnwell  als belangten Verband nicht vor.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_143`)

Für die in der  Ergänzung vom 28.9.2016 zum Vorlageantrag vom 1.6.2016 aufgestellten nicht näher  substantiierten Prozessbehauptungen des Vorliegens einer „gebrochenen Lieferungen“ in  einem von der Bf. angemieteten Lager bei der Firma **M.** finden sich keine ausreichenden  Hinweise auf bezahlte Lagermieten.

- missed: `M.` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_140`)

 2016 **Gerald Bährensmann**  Fremdleistungen (4900) ER16002 v.31.05.2016 + Fremdleistungen  (4900) ER 16005 v. 31.05.2016 – Gegenrechnung B KG Rechnung 01.07.2020  Leistungszeitraum 2016;

- missed: `Gerald Bährensmann` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Priv.-Doz.in Dr.in Bianca Gerasimczuk**  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Priv.-Doz.in Dr.in Bianca Gerasimczuk` (person)
- predicted in sentence: `Raimund Diedering, Bakk. iur.`

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/149083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149083.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Wladimir Ferrarese  über die Beschwerde des **Hademar Mühlenstedt**,  Kohlengasse 373, 8442 Sankt Andrä im Sausal, Österreich, vom 22. Juni 2025, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 20. Juni 2025, GZ. MA67/GZ1/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt  der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, Landesgesetzblatt für Wien Nr. 9/2006 in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als gemäß § 45 Abs. 1  VStG von der Verhängung einer Strafe abgesehen und dem Beschwerdeführer unter Hinweis  auf die Rechtswidrigkeit seines Verhaltens eine Ermahnung erteilt wird.

- missed: `Hademar Mühlenstedt` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/143412.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143412.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der  Verwaltungsstrafsache gegen **VetR Maria Naundorff, Bakk. rer. nat.**, Genigasse 90G, 8341 Saaz, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 23. Dezember 2023  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  14. Dezember 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

- missed: `VetR Maria Naundorff, Bakk. rer. nat.` (person)
- predicted in sentence: `Dr. Anna Radschek`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch **Mag. Wolfgang Moser**, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

- missed: `Mag. Wolfgang Moser` (person)
- predicted in sentence: `Priv.-Doz.in Rosamunde Galanidis`, `Hermine Ruprich`

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_73`)

Dieses Kfz wurde von Herrn **Frikel** selber angeschafft, wo und zu welchen  Bedingungen kann ich nicht angeben.

- missed: `Frikel` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_11`)

Fristgerecht wurde bekanntgegeben, dass das Fahrzeug zur Beanstandungszeit **PhD Wilhelm Reschke, MBA**,  Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich (= Beschwerdeführer, kurz: Bf.) überlassen war.

- missed: `PhD Wilhelm Reschke, MBA` (person)
- predicted in sentence: `Wilhelm Reschke`

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_90`)

Herr **Sahin** konnte daher davon ausgehen, dass alle Meldungen  ordnungsgemäß und fristgerecht abgegeben werden bzw. die verspätete Abgabe der  Umsatzsteuervoranmeldungen war nicht vorsätzlich!

- missed: `Sahin` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch **Erich Allbrand**,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

- missed: `Erich Allbrand` (person)
- predicted in sentence: `Markus Knechtl LL.M.`, `Robert Derici`, `Erich Allbrand,  `

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_163`)

M.M.A. und dessen Frau **M.M.B.** nur sehr ungenau abgesprochen.

- missed: `M.M.B.` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_8`)

Im Betriebsprüfungsbericht wurden folgende Feststellungen  getroffen (Bericht gem. § 150 BAO über das Ergebnis der Außenprüfung vom 15.02.2018):   „Tz. 1 Betriebsstätte Peru 2015   Die **Tamara Gottschalch** (X.) hat 2015 und 2016 die Errichtung und den Betrieb einer Seiltransportanlage  in Peru übernommen, wobei das Transportsystem nach der Errichtung an den Kunden  überlassen werden sollte, die Abgabepflichtige jedoch die Instandhaltung und Überwachung  des Betriebes der Anlage sowie die Unterstützung während der Projektdauer übernehmen  sollte.

- missed: `Tamara Gottschalch` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin **Mag.a Univ.-Prof.in Ada Schaeferlein**  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag.a Univ.-Prof.in Ada Schaeferlein` (person)
- predicted in sentence: `Leroy Sitterle`, `Astoria Stb`

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache **Ing. Dagobert Almasri**, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

- missed: `Ing. Dagobert Almasri` (person)
- predicted in sentence: `Mag.Dr. Katrin Allram`, `Sera Trust`

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_24`)

Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:   Sachverhalt:   Über die **Sulamith Jedwillat** (= Beschwerdeführerin) wurde am 24.02.2014 ein Insolvenzverfahren  (Sanierungsverfahren mit Eigenverwaltung, Aktenzeichen 3 S…) eröffnet.

- missed: `Sulamith Jedwillat` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/143315.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143315.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Dr. Wolfgang Pavlik** über die Beschwerde der  Emanuel Bulthuis, Martinsplatz 47, 6167 Neustift im Stubaital, Österreich, vom 7. Dezember 2022 gegen den Bescheid des Finanzamtes  Österreich vom 8. November 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für die Monate August und September 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Wolfgang Pavlik` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_78`)

Ich konnte hierzu noch die Anamnese (Aufnahmeabt.) vom 26.03.2018 **Dr. Ilka Danev** ausheben  lassen und lege diesen meinem diesem Schreiben ebenfalls bei.

- missed: `Dr. Ilka Danev` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_29`)

Seit der  Nachlaserung von Dr. A2 stehe die Bf. unter regelmäßiger Kontrolle bei **Dr. A2**.

- missed: `Dr. A2` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/148962.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148962.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Univ.-Prof. Ramon Löther  in der Beschwerdesache Axel Pommeränke,  Zum Hauptplatz 2, 4030 Linz, Österreich, vertreten durch **Mag. Niki Zaar**, Babenbergerstraße 9/1/8, 1010 Wien,  betreffend die Vorlage der Bescheide des Finanzamtes Österreich vom 9. Oktober 2023 über  die Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2018 und 2019 im Wege  des Vorlageberichtes vom 21. November 2024 zur Steuernummer 14-979/7189  den  Beschluss:  Das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `Mag. Niki Zaar` (person)
- predicted in sentence: `Axel Pommeränke`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_21`)

In der dagegen am rechtzeitig eingebrachten Beschwerde vom 07.01.2021 führte das **Jaden Knauss**  aus, dass die Abgabenbehörde die Rechtslage zu § 212a BAO grob verkenne und somit der  erlassene Bescheid vom 03.12.2020, ohne Berücksichtigung des Antrages auf Aussetzung-der  Einhebung (§ 212a BAO), in einem besonderen Maß mit der Rechtsvorschrift im Widerspruch  stehe und daher den Gleichheitssatz nach Art 7 B-VG (objektive Willkür) verletze.

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)

Das Büro in **Univ.-Prof.in Miriam Ungruh**  war auch im Interesse meines Arbeitgebers.

- missed: `Univ.-Prof.in Miriam Ungruh` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_337`)

Ich habe mehrere Angebote eingeholt, diese habe ich dann Herrn **M.** mitgeteilt und er hat mir  dann mitgeteilt, ob er günstiger anbieten kann oder nicht.

- missed: `M.` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin **Mag. Andrea Ebner** über die Beschwerde  des Herbert Leitzmann, Schörgendorfstraße 80D, 9560 Förolach, Österreich, vom 30. Juni 2023, gegen die drei Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 21. Juni 2023,   GZen 1) MA67/Zahl1/2023, 2) MA67/Zahl2/2023 und   3) MA67/Zahl3/2023, alle drei wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  werden die drei Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

- missed: `Mag. Andrea Ebner` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/139889.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139889.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag. Günter Narat** über die Beschwerde  vom 29. Dezember 2021 des Beschwerdeführers Ashley Claesson, Adr BF, Steuernummer:  66-163/5550, gegen den Bescheid des Finanzamtes Österreich vom 1. Dezember 2021  betreffend Einkommensteuer 2020 zu Recht:    I)  Der Beschwerde wird gem. § 279 BAO Folge gegeben.

- missed: `Mag. Günter Narat` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)

Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn **Inn Trikraftglanz** mitteilte, dass er „besser aufpassen muss".

- missed: `Inn Trikraftglanz` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_53`)

Da Herr **Harald Hilderink**  mit seinen Unternehmen an öffentlichen Ausschreibungen teilnimmt ist es  für ihn wichtig, finanzstrafrechtlich unbescholten zu sein.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/139845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139845.1_14`)

Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens, der  aktenkundigen Unterlagen, des Vorbringens der Parteien sowie der schriftlich eingeholten  Zeugenaussage von **Dipl. Kff. Sara Füßgen**  folgenden entscheidungswesentlichen Sachverhalt fest:  Der Bf. und Dipl. Kff. Sara Füßgen  waren bis 13.01.2014 verheiratet.

- missed: `Dipl. Kff. Sara Füßgen` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache **Ing. Edith Schifferdecker**,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

- missed: `Ing. Edith Schifferdecker` (person)
- predicted in sentence: `Hon.-Prof. Dominik Mehlig`

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch **Ing. Mag. Hamza Ovacin**,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

- missed: `Ing. Mag. Hamza Ovacin` (person)
- predicted in sentence: `Markus Knechtl LL.M.`, `Saphira Schnaak`

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_226`)

Diese Auffassung ist spätestens seit den Urteilen EuGH 11.9.2014, C-394/13, B, und EuGH  22.10.2015, C-378/14, Tomisław **Trapkowski**, als überholt anzusehen (vgl. BFG 7.2.2017,  RV/7106469/2016).

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_34`)

dazu wurde der betreffende E-Mail- Verkehr mit dem SMS sowie die Stellungnahme des **Univ.-Prof. Dr. F**, Klinik Ort2, v. 23.3.2022  vorgelegt.

- missed: `Univ.-Prof. Dr. F` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Dr. Sebastian Pfeiffer LL.M.** in der  Verwaltungsstrafsache gegen Annette Preußing, Am Neufeldersee 40, 3385 Uttendorf, Österreich, über die Beschwerde des  Beschuldigten vom 23. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 18. Jänner 2023, Zahl MA67/Zahl/2022, mit dem der Einspruch vom 6. Jänner  2023  gegen die Strafverfügung vom 4. Oktober 2022 mit derselben Geschäftszahl gemäß § 49  Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der  angefochtene Zurückweisungsbescheid bestätigt.

- missed: `Dr. Sebastian Pfeiffer LL.M.` (person)
- predicted in sentence: `Sebastian Pfeiffer LL.M.`

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_103`)

Errichtung an den Kunden überlassen werden sollte, die **Tamara Gottschalch**  jedoch die Instandhaltung  und Überwachung des Betriebes der Anlage sowie die Unterstützung während der  Projektdauer übernehmen sollte.

- missed: `Tamara Gottschalch` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/137857.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137857.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Univ.-Prof. Aron Nierenberger  in der Beschwerdesache **DDr.in VetR Rosemarie Srama**,  Hollgasse 53, 3244 Riegers, Österreich, gegen die Bescheide des Finanzamtes Österreich vom 10. Februar 2020  betreffend Einkommensteuer 2014 bis 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

- missed: `DDr.in VetR Rosemarie Srama` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_484`)

Zur Beschwerde erklärte der steuerliche Vertreter, dass die Bf. das Rechtsmittel im Sinne der  bisherigen Ausführungen und des Erkenntnisses des Verwaltungsgerichtshofes vom 22.07.2015  (2012/13/0037) vollumfänglich aufrecht halte, und beantragte weiters die mündliche  Gutachtenserörterung durch die Sachverständigen **Iris Preining** von der B-Anstalt und M.M.B.  von der C-Anstalt, zum Beweis der Richtigkeit des jeweiligen Gutachtens, den Ablauf bei der  Probenentnahme und Erstellung des jeweiligen Gutachtens und damit der Unrichtigkeit der  Kalkulationsgrundlagen der Behörde sowie die Einvernahme des Geschäftsführers der Lemost-Handel GmbH  E.St., zum Beweis für die tatsächlich gelieferte Fleischqualität im Prüfungszeitraum und  damit zur Höhe des tatsächlichen Fleischabschnitts un der Fleischmenge, die verkaufbar  gewesen wäre.

- missed: `Iris Preining` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_111`)

In der mündlichen Verhandlung begründete die den Bf. vertretende Ehegattin die fehlenden  aktuellen Rezepte für die eingenommenen Vitamine B, C und D damit, dass der Wahlarzt **Dr. B**,  der die Thrombopenie als Einziger erkannt habe, Privatrezepte ausstelle, die jedoch immer  Geld kosten.

- missed: `Dr. B` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_471`)

Aufgrund der  Neurodermitis stehe der Aufwand mit der Behinderung in Zusammenhang, € 87,48 seien daher  eine ag Bel ohne SB.   24.01.2013 € 50,64 Osspura Theodora Hartzheim, BA Bakk. phil. FK 25,32   26.02.2013 € 50,64 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32   26.03.2013 € 45,00 Osspura **Theodora Hartzheim, BA Bakk. phil.** FK € 25,32  19.06.2013 € 50,4 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32   32 von 43 Seite 33 von 43

- missed: `Theodora Hartzheim, BA Bakk. phil.` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_174`)

3. Zulässigkeit des Einspruches:  …  4. Gründe des Einspruches:  Der Vorwurf, der Einschreiter hätte als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin der Firma1 des Fahrzeuges mit dem behördlichen Kennzeichen Auto4  [Anmerkung BFG: nicht gegenständlich] dem ordnungsgemäß zugestellten Verlangen der MA  67 vom 28.01.2020, innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er  dieses Fahrzeug überlassen gehabt hat, sodass dieser zur in der Strafverfügung angegebenen  Tatzeit und Tatort gelenkt hat bzw. vor diesem Zeitpunkt abgestellt hat nicht entsprochen zu  haben und somit die Rechtsvorschriften des § 103 Abs 2 KFG [Anmerkung BFG, gemeint: § 2  (Wiener) Parkometerabgabeverordnung iVm § 4 Abs. 2 Parkometergesetz 2006] trifft nicht zu,  dies aus folgenden Gründen: Es wurde - wie oben erwähnt - vom Einschreiter die Übertragung  der Meldepflicht auf Herrn **Angelstein**  geb. Herrgeb, übertragen.

- missed: `Angelstein` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache **OStR Cassandra Schmedtje**,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

- missed: `OStR Cassandra Schmedtje` (person)
- predicted in sentence: `Helga Kraus`

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_308`)

Die andere Person wiederum ist dem Kreis jener Unternehmen zuzuordnen, welche entweder  von unlauteren Machenschaften auf Ebene der Subfirma **M.** profitiert, oder zumindest aus  Eigennutz das Auge davor verschließt.

- missed: `M.` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/147179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147179.1_1`)

BESCHLUSS  Das Bundesfinanzgericht beschließt durch die Richterin Dr. Lisa Pucher in der  Säumnisbeschwerdesache **Judith Mühlpforte**, Auleiten 8, 4775 Kalchgrub, Österreich, über die Beschwerde vom 27. November  2024 wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend den Antrag vom 30. Dezember 2020 auf Arbeitnehmerveranlagung für das Jahr  2015, zu Steuernummer 97-810/7095:  Die Säumnisbeschwerde wird als unzulässig zurückgewiesen.

- missed: `Judith Mühlpforte` (person)
- predicted in sentence: `Dr. Lisa Pucher`

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_6`)

Mit Haftungsbescheid vom 22. Mai 2019 wurde **Olaf Koechig** (Bf, Gesellschafter der Gartfentri Heizung Institut GmbH  als  Haftungspflichtiger gemäß § 9 iVm §§ 80 ff Bundesabgabenordnung (BAO) für die  aushaftenden Abgabenschuldigkeiten der Gartfentri Heizung Institut GmbH  im Ausmaß von 318.077,07 € in Anspruch  genommen und aufgefordert, diesen Betrag innerhalb eines Monats ab Zustellung dieses  Bescheides zu entrichten.

- missed: `Olaf Koechig` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_73`)

Die Serumkreatininwerte liegen im oberen  Grenzbereich, eine diabetische Retinopathie ist mir nicht bekannt  **Dr. F**  Untersuchungsbefund:   Allgemeinzustand: gut       Ernährungszustand: gut  Größe: 181,oo cm        Gewicht: 102,00 kg   …..  6 von 14 Seite 7 von 14

- missed: `Dr. F` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_31`)

Zur beschwerdeführenden Partei  Die beschwerdeführende Partei ist **Jonas Bruchmüller**  im Sinne des § 1 Bankwesengesetz  (Bundesgesetz über das Bankwesen -BWG) und unterliegt dem Stabilitätsabgabegesetz.

- missed: `Jonas Bruchmüller` (person)
- predicted in sentence: —

</details>

---

