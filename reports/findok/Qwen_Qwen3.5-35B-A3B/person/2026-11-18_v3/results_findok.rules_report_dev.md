# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-18T11:13:05.125995

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-18_v3/config.yaml 
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
| Validation sentences | 2144 |
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
| Batch size | 100 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.4% |
| True Positives | 908 |
| False Positives | 379 |
| False Negatives | 943 |
| Total Gold Entities | 1851 |
| Micro Precision | 70.6% |
| Micro Recall | 49.1% |
| Micro F1 | 57.9% |
| Macro F1 | 57.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `salutation_herr_frau` | 5.4% | 96.2% | 2.8% | 53 | 51 | 2 |
| `beschwerdesache_name` | 25.4% | 92.2% | 14.7% | 296 | 273 | 23 |
| `academic_titles` | 40.9% | 74.0% | 28.3% | 707 | 523 | 184 |
| `genitive_name_no_title` | 4.2% | 33.1% | 2.3% | 127 | 42 | 85 |
| `represented_by` | 1.9% | 28.1% | 1.0% | 64 | 18 | 46 |
| `role_anchor_name` | 0.1% | 2.7% | 0.1% | 37 | 1 | 36 |
| `initial_only_name` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `standalone_name_after_role` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `salutation_herr_frau` 🏆

**F1:** 0.054 | **Precision:** 0.962 | **Recall:** 0.028  

**Format:** `regex`  
**Rule ID:** `3c56bfa5`  
**Description:**
Matches names following 'Herr' or 'Frau', strictly requiring a second capitalized word (surname) to avoid matching nouns like 'Einkünfte'.

**Content:**
```
(?:Herrn?\.?|Fr\.?|Frau\.?)\s+([A-ZÄÖÜ][a-zäöüß]+(?:\s+[A-ZÄÖÜ][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.962 | 0.028 | 0.054 | 53 | 51 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 51 | 2 | 1800 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_11`)


Weiters legte die Beschwerdeführerin den Dienstvertrag vom 12.03.2014 vor, mit dem  folgenden entscheidungsrelevanten Inhalt:   "DIENSTVEREINBARUNG abgeschlossen zwischen DG als Dienstgeber und Frau James Hainig,  Adr.**** als Dienstnehmerin.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_105`)


Herr Eugen Volchert  ist polizeilich in der Adr, Plz_1  d_Ort_1 gemeldet und deshalb ist sein Fahrzeug auch in d_Ort_1 zugelassen.

| Predicted | Gold |
|---|---|
| `Eugen Volchert` | `Eugen Volchert` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Kirsten Renneissen – ist Malermeister und betreibt ein  Einzelunternehmen.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Starnberg Beratung GmbH` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `M.` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_269`)


Herr Albert Sengeisen  ist nach eigenen Angaben für das  Geschäftskonto der M. bei der Bank allein zeichnungsberechtigt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_270`)


Bedeutsame  Firmenunterlagen - Rechnungslegungen - sind von durchwegs von Herrn Albert Sengeisen  approbiert.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_271`)


Barauszahlungen an Fremdleister wurden, so seine Angaben dazu, von ihm abgewickelt. Bei  drei Außenprüfungen ist stets Herr Albert Sengeisen  als Machthaber über die Gesellschaft  aufgetreten.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Habdank` | `Bernhard Habdank` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Raimund Ladwig` | `Raimund Ladwig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Aron Pommeränke` | `Aron Pommeränke` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_21`)


Da der Gutachter Herr Karina Burfeindt selber sagte, wenn wir auch einen ärztlichen Befund haben, ändert es die ganzen Prozente,  und das haben wir jetzt.

| Predicted | Gold |
|---|---|
| `Karina Burfeindt` | `Karina Burfeindt` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_45`)


Zu den vereinbarten Einkaufskonditionen gab Herr Inn Trikraftglanz  zu Protokoll, dass es eine Vereinbarung  gegeben habe, dass die Fa. e. um € 1,00 je 100 Liter billiger anbieten müsse als die Fa. „F. KG“,  was auch regelmäßig geschah.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)


Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Borisowa` (person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_244`)


6. Zum Vorwurf Verwechselung K.  Die diesbezüglichen Ausführungen sind sehr verkürzt: Konkret hat Herr Inn Trikraftglanz ausgesagt, dass er  nur im Erstgespräch über die Funktion von Herrn K. geirrt hat.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_409`)


Es ist auch darauf hinzuweisen, dass beim Mineralölhandel nur sehr kleine Gewinnspannen  möglich sind, es hätte daher für die Bf. fragwürdig sein müssen, wieso neue Anbieter billiger  sein können, wie alt eingesessene große Mineralöllieferanten wie die g. oder H.. Fraglich sei  auch, wieso die Bf. bei den anderen Lieferanten kein Skonto in Anspruch genommen hat,  obwohl dies nach Angabe von Herrn Inn Trikraftglanz möglich gewesen wäre.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_415`)


Die Anfrage beim Finanzamt deute vielmehr darauf hin,  dass Herr Inn Trikraftglanz  selbst Zweifel an der Seriosität der in Rede stehenden Lieferanten gehabt habe  und möglicherweise auch ein Naheverhältnis.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_424`)


Ein Naheverhältnis zwischen Herrn Inn Trikraftglanz und den gegenständlichen  Lieferanten hat es nicht gegeben.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_518`)


Aktenkundig ist, dass die Bf. in folgende Unterlagen Einsicht genommen hat bzw.  Überprüfungshandlungen gesetzt hat:  Fa. c:   Auszug aus dem Gewerberegister (13.6.2013)   Bescheid über die Erteilung der UID -Nummer (26. Juni 2013)   Bescheid vom 8. Juli 2013 Zollamt Wien (Registrierung-Identifizierung von  Wirtschaftsbeteiligten, Zuteilung einer EORI-Nummer)   Bescheid vom 1. August 2013 (Bewilligung zum Bezug von Mineralöl)  Fa. e.   Auszug aus dem Gewerberegister (18.11.2013)   Firmenbuchauszug (27.5.2013)   Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.   Passkopie Hr. K.   1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.   3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel   Eingangstüre)   Bescheid über die Erteilung der UID -Nummer (31.7.2013)   Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)   Bescheid über die Registrierung als Empfänger für Mineralöl   Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH    Auszug Gewerberegister (4.9.2013)   Firmenbuchauszug (4.9.2013)   Angebot vom 26.9.2013   Passkopie Hr. d.   Rückstandsbescheinigungen Finanzamt (31.10.2013,25.11 .2013, 6.12.2013)  Darüberhinaus hat der Gf. der Bf.  – wie dem Protokoll vom 1. März 2017 mit Herrn Inn Trikraftglanz  zu  entnehmen ist - nach der Außenprüfung (betreffend die Jahre 2010-2012) und Belehrung  (26.9.2013) folgende Schritte geändert bzw genauer beachtet und freiwillig zusätzliche  Maßnahmen gesetzt wie regelmäßige Abfrage der UID Nummern, regelmäßige Anforderung  von Rückstandsbescheinigungen, keine Barzahlungen, Zahlung ausschließlich auf  österreichische Konten, ausschließlich Lieferbeziehungen zu österreichischen Gesellschaften.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Zollamt Wien` (organisation)
- `M.` (person)
- `Finanzamt` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)


Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr Alois Kleynsteuber (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Finanzamt Salzburg-Land` (organisation)
- `Finanzamt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_20`)


In einem weiteren Schriftverkehr mit der  steuerlichen Vertretung wurde durch diese bekannt gegeben, dass der zuständige  Geschäftsführer, Herr Harald Hilderink, die Abgabenforderungen aus Umsatzsteuern in der 45.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_32`)


In dem eingeleiteten Finanzstrafverfahren wurde Herr Harald Hilderink  jedoch beschuldigt,  vorsätzlich die Abgabe und Zahlung der Umsatzsteuervoranmeldungen unterlassen zu haben  und zu einer Geldstrafe von EUR 10.000,00 verurteilt. Gegen diese Straffestsetzung richtet sich  die vorliegende Beschwerde und geben wir als Begründung an:   Die ARGE wurde von einem Steuerberater vertreten, der mit der Abgabe der  Umsatzsteuervoranmeldungen beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_33`)


Herr Harald Hilderink  konnte daher davon  ausgehen, dass alle Meldungen ordnungsgemäß und fristgerecht abgegeben werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_34`)


 Herr Harald Hilderink  ist zwar handelsrechtlicher Geschäftsführer österreichischer  Kapitalgesellschaften, jedoch besteht ein Unterschied zwischen einer GmbH und einer  ARGE, weshalb er sich steuerlichen Rat durch eine Steuerberatungsgesellschaft suchte  und diese mit der Buchführung beauftragte.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_38`)


Auf die Einhaltung von Fristen war Herr  Harald Hilderink  daher auf seine steuerliche Vertretung angewiesen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_40`)


Herr Harald Hilderink  ist nicht alleine dafür  verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)


 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr Harald Hilderink  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |
| `Harald Hilderink` | `Harald Hilderink` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_50`)


Eine Straffestsetzung von EUR 10.000,00 ist daher unangemessen  und unverhältnismäßig!   Die Abgabe der Umsatzsteuervoranmeldungen wurde von Herrn Harald Hilderink  irrtümlich  im Vertrauen auf die steuerliche Vertretung übersehen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_53`)


Da Herr Harald Hilderink  mit seinen Unternehmen an öffentlichen Ausschreibungen teilnimmt ist es  für ihn wichtig, finanzstrafrechtlich unbescholten zu sein.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_78`)


In einer E-Mail der steuerlichen Vertretung vom 7. November 2018 an Herrn R. vom  zuständigen BV-Team der Abgabenbehörde wurde als verantwortlicher Geschäftsführer der  ARGE Herr Harald Hilderink  genannt.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_79`)


Herr Harald Hilderink  ist außerdem der Geschäftsführer der P-GmbH, welche im Tatzeitraum  Vertreter nach § 81 BAO der ARGE ist.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_81`)


Herr Harald Hilderink  ist verantwortlicher Geschäftsführer der ARGE.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_89`)


Zum Beschwerdevorbringen, „Herr Harald Hilderink  war auf die Einhaltung von Fristen auf seine  steuerliche Vertretung angewiesen, die mit der Abgabe der Umsatzsteuervoranmeldungen  beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_95`)


Herr Harald Hilderink  ist nicht alleine dafür verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 3. September 2021, Zahl:  MA67/216700658355/2021, wurde Herr Roland Rößle (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Roland Rößle` | `Roland Rößle` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_7`)


Im Zuge der Überprüfung des Familienbeihilfenanspruches der Frau Verena Piechura (=  Beschwerdeführerin, Bf) im Dezember 2021 ua. für den Sohn B, geb. 03/1999, wurden  Studienbestätigungen der Universität Ort1 vorgelegt, wonach der Sohn B im Wintersemester  (WS) 2021/2022 im Bachelorstudium Lehramt für Bewegung und Sport sowie Französisch (KZ  UC 198 452 459;

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 4. Oktober 2022, Zahl  MA67/Zahl/2022, wurde Herr Annette Preußing (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  in der Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Annette Preußing` | `Annette Preußing` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Dagobert Duewel (= Beschwerdeführerin, Bf) hat mit Anträgen Beih100 und Beih3 vom  11.8.2022 für den Enkelsohn A, geb. 05/2004, ab Juni 2022 die Familienbeihilfe (FB) und den  FB-Erhöhungsbetrag wegen erheblicher Behinderung, konkret "Autismus-Spektrum-Störung  Asperger-Syndrom", beantragt.

| Predicted | Gold |
|---|---|
| `Dagobert Duewel` | `Dagobert Duewel` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Olivia Trienes (= Beschwerdeführerin, Bf) bezieht für den Sohn A, geb. 06/1997, laufend  die Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Olivia Trienes` | `Olivia Trienes` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/144646.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144646.1_44`)


Die  diesbezügliche Aufforderung (Bescheid vom 28.10.2021) hat Herr Jakob Dombrink  an das Finanzamt  retourniert und vermerkt, dass er eine Rente aus der Schweiz bekommt und diese zur Gänze in  die landwirtschaftliche Gesellschaft fließt (siehe "Schreiben Jakob Dombrink  v. 15.11.2021").

| Predicted | Gold |
|---|---|
| `Jakob Dombrink` | `Jakob Dombrink` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145368.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145368.1_34`)


Herr Gotthard Dinkelmann  hat in eigener Recherche noch herausgefunden, dass bei unbeschränkter  Schweizer Steuerpflicht nur ein sehr enger Kostenkatalog berücksichtigt werden könnte:  „Schuldzinsen, Beiträge in die Säule 2b und 3a, berufliche Weiterbildungskosten, bezahlte  Alimente, Unterstützungsbeiträge“ und bei beschränkter Steuerpflicht lediglich „Beiträge an  die Säule 2b und 3a sowie Wochenaufenthaltskosten“.

| Predicted | Gold |
|---|---|
| `Gotthard Dinkelmann` | `Gotthard Dinkelmann` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_726`)


In ihrer per Mail überreichten Vorhaltsbeantwortung vom 23. Mai 2024 (OZ. 111) nahm die  Bf. zu beiden Vorhalten (hg. GZ. RV/2100888/2022 vom 30. April 2024) und RV/2100046/2023  v. 23. April 2024) wie folgt Stellung:  „Sehr geehrter Herr Hartmut Berning   im Namen unseres o.a. Klienten und unter Berufung auf die uns erteilte Vollmacht können wir  zu Ihren Vorhalten vom 30.4.2024 (zugestellt am 6.5.2024) im Verfahren RV/2100888/2022  sowie vom 23.4.2024 (zugestellt am 26.4.2024) im Verfahren RV/2100046/2023 gerne wie  folgt Stellung nehmen:   1. Unternehmereigenschaft der Kunden   Wir haben von unserem Klienten keine weiteren Unterlagen betreffend die unternehmerischen  Leistungsempfänger erhalten, sodass wir keine weiterführenden Angaben zu diesen machen  können.

| Predicted | Gold |
|---|---|
| `Hartmut Berning` | `Hartmut Berning` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_13`)


Im Rahmen einer zweiten Stellungsuntersuchung vom  05.01.1989 wurde Herr Luna Fruechtenicht  als für den Präsenzdienst „untauglich“ eingestuft und dies  mit den festgestellten Diagnosen: Grand Mal Epilepsie, chronischer Alkoholabusus sowie  Oligrophenie begründet.

| Predicted | Gold |
|---|---|
| `Luna Fruechtenicht` | `Luna Fruechtenicht` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Schneppensiefen   Gegenstand` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_27`)


Mit Vorlageantrag vom 16.07.2024 wurde die Entscheidung über die Beschwerde durch das  Bundesfinanzgericht beantragt und ergänzend wie folgt begründet:  „[…] Ergänzend zur Beschwerde vom 15.02.2024 wird vorgebracht, dass Herrn Luna Fruechtenicht  Seitens der Pensionsversicherungsanstalt zwischenzeitlich eine Waisenpension zugesprochen  wurde und entsprechend die Erwerbsunfähigkeit infolge Krankheit oder Gebrechens ab der  Kindheit über das 18.

**False Positives:**

- `Luna Fruechtenicht  Seitens` — partial — gold is substring of pred: `Luna Fruechtenicht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Luna Fruechtenicht`(person)
- `Pensionsversicherungsanstalt`(organisation)

</details>

---

## `beschwerdesache_name` 🏆

**F1:** 0.254 | **Precision:** 0.922 | **Recall:** 0.147  

**Format:** `regex`  
**Rule ID:** `07b6560f`  
**Description:**
Matches names following 'in der Beschwerdesache' or 'in der Sache', capturing full names including suffixes (Bakk. iur., MA, etc.), hyphenated names, and multi-part names.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|in\s+der\s+Sache)\s+(?:des\s+|der\s+|die\s+)?([A-ZÄÖÜ][a-zäöüß]+(?:\s+(?:von|van|de|zu|u\.\s*)?[A-ZÄÖÜ][a-zäöüß]+)*(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*(?:\s*,\s*(?:MBA|MSc|BSc|LL\.M|LLB|BEd|Bakk\.\s*(?:iur|phil|rer\.nat|art|techn)|MA|Dr\.in|Mag\.a|Priv\.-Doz\.in|Hon\.-Prof\.in|Techn\s+R|Techn\.\s*R|Techn\s+R\.|R|PhD|Bakk\.\s*(?:iur|phil|rer\.nat|art)))?)\s*(?:,|\n|$|\s+(?:Stra\u00dfe|Gasse|Platz|Weg|Allee|Nr\.|Haus|\d+|GmbH|AG|KG|Verein|Stiftung|Gesellschaft))(?!\s+(?:Finanzamt|Bundesfinanzgericht|Senat|Magistrat|Verwaltungsgericht|Oberlandesgericht|Landesgericht|Bezirksgericht|Bundesgerichtshof|Verwaltungsgerichtshof|Bundessozialgericht|Verfassungsgerichtshof|Bundesministerium|Landesregierung|Stadt|Gemeinde|Bezirk|Amt|Behörde|Wien|Graz|Linz|Salzburg|Innsbruck|Klagenfurt|Bregenz|Eisenstadt|St\.\s*P\u00f6lten|Steuerberatung|Rechtsanw\u00e4lte|Wirtschaftspr\u00fcfung|Partnerschaft|&\s+Partner|\(|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.922 | 0.147 | 0.254 | 296 | 273 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 273 | 23 | 1578 |

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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentin Pawils` | `Florentin Pawils` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Alva Jodgalweit` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gregor Klocksin` | `Gregor Klocksin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Unterguntschach 85, 3525 Armschlag, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Karl Morgenbesser` | `Karl Morgenbesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Susette Glaeßel` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Frauke Galleithner` | `Frauke Galleithner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Klutentreter` | `Gebhard Klutentreter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lee Kubbig` | `Lee Kubbig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Nancy Stuckenschneider  in der Beschwerdesache des  Bruno Karahasan, Ludowikaweg 5, 3602 Bacharnsdorf, Österreich, über die Beschwerde vom 2. Juli 2019 gegen den Bescheid des  FA St. Johann Tamsweg Zell am See  vom 26. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zur Steuernummer 12-630/0045  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Bruno Karahasan` | `Bruno Karahasan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Priv.-Doz.in Nancy Stuckenschneider` (person)
- `Ludowikaweg 5, 3602 Bacharnsdorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `12-630/0045` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


BESCHLUSS   Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Frederike Lipienski  in der Beschwerdesache des  Hademar Rüstow, Eck 124T, 2214 Auersthal, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des  FA Amstetten Melk Scheibbs (FA) vom 10. März 2021 über die Abweisung eines Antrages auf Wiederaufnahme §  303 BAO /  ESt 2017 zur Steuernummer 71-651/2158  beschlossen:   Der Vorlageantrag vom 29.Sept.2021 wird gemäß § 260 Abs. 1 lit. a iVm § 264 Abs. 4 lit e und  Abs. 5 BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hademar Rüstow` | `Hademar Rüstow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Frederike Lipienski` (person)
- `Eck 124T, 2214 Auersthal, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `71-651/2158` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


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

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Hilde Hassenzahl  in der Beschwerdesache des  Gwendolin Rittmüller, Matzlröth 29, 3970 Reinprechts, Österreich, vertreten durch StB, über die Beschwerde vom 14. Dezember 2020  gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 30. November 2020 betreffend Umsatzsteuer 2013 zu  Steuernummer 10-920/5174  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gwendolin Rittmüller` | `Gwendolin Rittmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Hon.-Prof.in Hilde Hassenzahl` (person)
- `Matzlröth 29, 3970 Reinprechts, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)
- `10-920/5174` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Saligergasse` — partial — pred is substring of gold: `Saligergasse 1, 3300 Haag Dorf, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Eugen Volchert Hochraingasse` — partial — gold is substring of pred: `Eugen Volchert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Lieselotte Akdas`(person)
- `Eugen Volchert`(person)
- `Hochraingasse 28, 4076 Valtau, Österreich`(address)
- `FA Baden Mödling`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

**False Positives:**

- `Kelderber Beratung Technologien` — type mismatch — same span as gold: `Kelderber Beratung Technologien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Silvia Gebhart`(person)
- `Kelderber Beratung Technologien`(organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich`(address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker`(person)
- `Mag Tatjana Kovacic`(person)
- `Dr  Heinrich Vana,`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `7867 150654`(social_security_number)
- `Europäischen Parlaments`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Theodora Urbanova` — partial — pred is substring of gold: `Theodora Urbanova, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Theodora Urbanova, Bakk. iur.`(person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `54-205/5010`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Gueldner Garten` — type mismatch — same span as gold: `Gueldner Garten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Tamara Steinmüller`(person)
- `Gueldner Garten`(organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich`(address)
- `FA Deutschlandsberg Leibnitz Voitsberg`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Raimund Diedering` — partial — pred is substring of gold: `Raimund Diedering, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Josepha Peifers Jägerberg` — partial — gold is substring of pred: `Josepha Peifers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Josepha Peifers`(person)
- `Jägerberg 5, 9062 Bärndorf, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich`(address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `73-948/8864`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Valentin Joebges` — partial — pred is substring of gold: `Valentin Joebges, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Stephan`(person)
- `Valentin Joebges, LLM`(person)
- `Bärngarten 17, 9713 Hochegg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `84-167/9727`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dominika Juhass  in der Beschwerdesache  Ludmilla Hühnerfuß, Bakk. techn., Singham 20, 3465 Unterstockstall, Österreich,   über die Beschwerde vom 27. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom  12. Juni 2019 betreffend Vorsteuererstattung 2018 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ludmilla Hühnerfuß` — partial — pred is substring of gold: `Ludmilla Hühnerfuß, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dominika Juhass`(person)
- `Ludmilla Hühnerfuß, Bakk. techn.`(person)
- `Singham 20, 3465 Unterstockstall, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

</details>

---

## `academic_titles` 🏆

**F1:** 0.409 | **Precision:** 0.740 | **Recall:** 0.283  

**Format:** `regex`  
**Rule ID:** `346fcc35`  
**Description:**
Matches names preceded by academic/professional titles, ensuring full name capture including suffixes (LL.M., MA, etc.) and excluding street names or partial matches.

**Content:**
```
(?:\b(?:Dr\.|Mag\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|OMedR|OStR|Ri|StR|RgR|KommR|MedR|Techn\s+R|Techn\.\s*R|Techn\s+R\.|R|PhD|Bakk\.\s*(?:iur|phil|rer\.nat|art)|LL\.M\.|LLB|M\.B\.L\.|ÖkR|Ing\.?|VetR|Dipl\.\-Ing\.?|Dkfm\.?|MMag\.?|BSc|MSc|DDr\.in|Prof\.\s*Prof\.|KzlR|em\.\s*Univ\.-Prof\.|Mag\.\s*\(FH\)|Mag\.a|HA|HR|KR|KomzR\.)\s+)+[A-ZÄÖÜ][a-zäöüß]+(?:\s+(?:von|van|de|zu|u\.\s*)?[A-ZÄÖÜ][a-zäöüß]+)*(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*(?:\s*,\s*(?:MBA|MSc|BSc|LL\.M|LLB|BEd|Bakk\.\s*(?:iur|phil|rer\.nat|art)))?(?!\s+(?:Straß|Gasse|Platz|Weg|Allee|Nr\.|Haus|Nr\.\s*\d+|Finanzamt|Bundesfinanzgericht|Senat|Magistrat|GmbH|AG|KG|Verein|Stiftung|Rechtsanwälte|Steuerberatung|Wirtschaftsprüfung|Teilnehmerin|Beschwerdeführerin|Antragstellerin|Kundin|Patientin|Erwachsenenvertreterin|Beschwerdesache|Sache|des\s+|der\s+|die\s+|Ges\-m\.b\.H\.|Gesellschaft|&\s+Partner|\s+Platz|\s+Straß|\s+Gasse|\s+Weg|\s+Allee|\s+Nr\.|\s+Stb|\s+Stb\.\s*KG|\s+Steuerberatungsgesellschaft|\s+Rechtsanwälte|\s+Partnerschaft|\s+GmbH|\s+AG|\s+KG|\s+Verein|\s+Stiftung|\s+Gesellschaft|\s+&\s+Partner|\s+\(|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.740 | 0.283 | 0.409 | 707 | 523 | 184 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 523 | 184 | 1328 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Hajicek` | `Dr. Alexander Hajicek` |
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |
| `Mag. Michael Franz` | `Mag. Michael Franz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Franz Josef Großin` (person)
- `Finanzamtes Baden Mödling` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_20`)


Seite 3 von 15 Erst anlässlich der mit Bericht vom 27.12.2010 abgeschlossenen Betriebsprüfung wurde die Ungewissheit, ob Liebhaberei im Zusammenhang mit der Vermietung des Objektes in Univ.-Prof.in Miriam Ungruh  vorliegt, beseitigt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_69`)


Die ersten Monate bis zur Erlangung der Aufenthalts- und Arbeitsbewilligung für Russland und bis mein Büro bei AG Russland und meine Dienstwohnung bezugsbereit waren, habe ich ausschließlich von Univ.-Prof.in Miriam Ungruh  aus gearbeitet.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_74`)


Sie haben mit mir in Univ.-Prof.in Miriam Ungruh  deren Strategie und Marktauftritt in Russland besprochen (z.B. DivFirmen DivFirmen uvm.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_75`)


o Ich habe russische Kunden, die Wien besuchten, von Univ.-Prof.in Miriam Ungruh  aus betreut;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_76`)


sie nach Univ.-Prof.in Miriam Ungruh  zu Besprechungen und Workshops eingeladen (z.B. DivFirmen DivFirmen; uvm.) o In allen Fällen war ausschlaggebend, dass ich in Univ.-Prof.in Miriam Ungruh (Österreich) für „Westler“ leichter erreichbar war, ohne dass die Leute ein Visum besorgen und den teuren Aufenthalt in Moskau bezahlen mussten, um mich zu sehen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_81`)


o Um mir diese Arbeit in Univ.-Prof.in Miriam Ungruh  und in Österreich zu erleichtern, teilte mir AG zwei Dienstwägen zu: einen in Univ.-Prof.in Miriam Ungruh  und einen in Moskau. In Russland war ich ebenfalls rund um die Uhr im Einsatz: 14 Büros, 14 direkt berichtende Manager, 1200 Mitarbeiter, eine Forschungsstätte, eine PC Fabrik und diverse zusätzliche Infrastruktur wie Service Center, 2000 Partner Firmen, Partnerschaften mit über 100 Universitäten und über 2 Millionen Kunden im Jahr müssen eben betreut werden.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)


Das Büro in Univ.-Prof.in Miriam Ungruh  war auch im Interesse meines Arbeitgebers.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Mag. Peter Staudinger` | `Mag. Peter Staudinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeannette Neuschwender` (person)
- `Zum Kogl 12, 4441 Penz, Österreich` (address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adalbert Köseoglu` | `Hon.-Prof. Adalbert Köseoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Jana Papenkord` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |
| `Mag. Manfred Frühwirth` | `Mag. Manfred Frühwirth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Lieselotte Akdas` | `Univ.-Prof.in Lieselotte Akdas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Sascha Hilcker` | `Ing. Sascha Hilcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich` (address)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Helge Göppele` | `Priv.-Doz. Helge Göppele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `GDJJ Versand` (organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich` (address)
- `Finanzamtes Graz` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Jodgalweit` | `Priv.-Doz.in Alva Jodgalweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Pawils` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Michaela Dehnert` | `Hon.-Prof.in Michaela Dehnert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Stiller` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.a Univ.-Prof.in Ada Schaeferlein` | `Mag.a Univ.-Prof.in Ada Schaeferlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leroy Sitterle` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Astoria Stb GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |
| `Univ.-Prof.in Shoshana Leuther` | `Univ.-Prof.in Shoshana Leuther` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hagleithen 8, 3345 Strohmarkt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `80-897/7654` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hermine Roj` | `Mag.a Hermine Roj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corinna Farke` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rosamunde Galanidis` | `Priv.-Doz.in Rosamunde Galanidis` |
| `Mag. Wolfgang Moser` | `Mag. Wolfgang Moser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hermine Ruprich` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Elias Voht` | `VetR Elias Voht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thomas Hutching` | `Hon.-Prof. Thomas Hutching` |
| `Hon.-Prof. Ruprecht Hauswerth` | `Hon.-Prof. Ruprecht Hauswerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `26-476/7368` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Tiwald` | `Mag. Wolfgang Tiwald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Renneissen` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` | `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` | `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` |

**Missed by this rule (FN):**

- `SeeAutomotive AG` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Matyschek` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |
| `Mag. Belinda  Maria Eder` | `Mag. Belinda  Maria Eder` |
| `Mag. Katharina Moravec` | `Mag. Katharina Moravec` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Agneter` (person)
- `Xaver Plaumert, BEd` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie Schan` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Rauscher` | `Dr. Michael Rauscher` |
| `Mag. Franz Glashüttner` | `Mag. Franz Glashüttner` |
| `Dr. Christian Haid` | `Dr. Christian Haid` |
| `Mag. Bruno  Sundl` | `Mag. Bruno  Sundl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

| Predicted | Gold |
|---|---|
| `Ing. StR Samuel Fraesdorff` | `Ing. StR Samuel Fraesdorff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich` (address)
- `Maximilian Jasper` (person)
- `Wetzles 9, 3243 Lunzen, Österreich` (address)
- `Prof. Dr. Thomas Keppert` (person)
- `Leroy Kusznierz` (person)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)


Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur Gustav Nowak.

| Predicted | Gold |
|---|---|
| `Ing. StR Samuel Fraesdorff` | `Ing. StR Samuel Fraesdorff` |

**Missed by this rule (FN):**

- `Leroy Kusznierz` (person)
- `Maximilian Jasper` (person)
- `Gustav Nowak` (person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `OMedR Ottfried Theißl` | `OMedR Ottfried Theißl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Ute Gspan` (person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Tamara Steinmüller` | `Mag.a Tamara Steinmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gueldner Garten` (organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich` (address)
- `FA Deutschlandsberg Leibnitz Voitsberg` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gertraud Hausherr` | `Mag. Gertraud Hausherr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Joachim Annanias` | `Dr. Joachim Annanias` |
| `VetR Burkhard Krautschenko` | `VetR Burkhard Krautschenko` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geizersgraben 6, 2823 Leiding, Österreich` (address)
- `Mag. Susanne Pöltenstein-Rosenegger` (person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Puntigam` | `Mag. Manuela Puntigam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Holzfuss` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |
| `KzlR Diethard Ringhand` | `KzlR Diethard Ringhand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Braunau Ried` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_55`)


Handschriftlich war darauf vermerkt „Bestätigung durch Frau E, Exfrau des Bf. und  Mutter der beiden unterhaltspflichtigen Kinder K1 und K2: Hiermit erkläre ich, dass mein  Exmann KzlR Diethard Ringhand  zu allen o.g.

| Predicted | Gold |
|---|---|
| `KzlR Diethard Ringhand` | `KzlR Diethard Ringhand` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Ladwig` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Susette Glaeßel` | `Mag.a Susette Glaeßel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl Morgenbesser` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |
| `StR Univ.-Prof. Alvin Paulikat` | `StR Univ.-Prof. Alvin Paulikat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Dr Christian Burghardt` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_25`)


Nach dem vorliegenden Beschluss des Bezirksgerichtes Innere Stadt vom 26.11.2010 wurde der  Rechtsanwalt Dr. Burghardt zum Sachwalter gemäß § 268 Abs. 3 Z 2 ABGB bestellt. Der  Sachwalter wurde u.a. für das Aufgabengebiet zur Vertretung vor Ämter und Behörden  bestellt. Die Sachwalterbestellung wirkt insofern konstitutiv, als ab ihrer Wirksamkeit die  Prozess- und Handlungsfähigkeit im dort umschriebenen Ausmaß für den Bf. keinesfalls mehr  gegeben war (VwGH 27.2.2006, 2004/05/0326).

| Predicted | Gold |
|---|---|
| `Dr. Burghardt` | `Dr. Burghardt` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |
| `Hon.-Prof.in Elvira Thielsen` | `Hon.-Prof.in Elvira Thielsen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |
| `Ing. Edith Schifferdecker` | `Ing. Edith Schifferdecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` | `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` |
| `OMedR Leonhard Hestermeyer` | `OMedR Leonhard Hestermeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sägerweg 5, 5450 Reitsam, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `52-932/8889` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_11`)


Fristgerecht wurde bekanntgegeben, dass das Fahrzeug zur Beanstandungszeit PhD Wilhelm Reschke, MBA,  Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich (= Beschwerdeführer, kurz: Bf.) überlassen war.

| Predicted | Gold |
|---|---|
| `PhD Wilhelm Reschke, MBA` | `PhD Wilhelm Reschke, MBA` |

**Missed by this rule (FN):**

- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich` (address)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Meyerhofer` | `Mag. Manuela Meyerhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sandra Fenn` (person)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt  Oberwart` (organisation)
- `49-433/1564` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

| Predicted | Gold |
|---|---|
| `Dr. Farid Rifaad` | `Dr. Farid Rifaad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Evelyn Antwerber` (person)
- `Hertzstraße 25, 5134 Spieglern, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Dr. Hedwig Bavenek` — partial — pred is substring of gold: `Mag.Dr. Hedwig Bavenek-Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Mag. Franz Josef Großi` — partial — pred is substring of gold: `Mag. Franz Josef Großin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alexander Hajicek`(person)
- `Mag. Helga Hochrieser`(person)
- `Mag. Michael Franz`(person)
- `Mag. Franz Josef Großin`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Elisabeth Schafstall`(person)
- `Leithagürtel 20, 4251 Steinwald, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

**False Positives:**

- `Mag. Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Dr.in Laurin Morgenschweis`(person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich`(address)
- `Fatima Beringschmidt`(person)
- `Finanzamtes Waldviertel`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`
- `Hon.-Prof. Thassilo Schoenrock` — partial — pred is substring of gold: `Hon.-Prof. Thassilo Schoenrock, LLM`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Thassilo Schoenrock, LLM`(person)
- `Hochscharten 126D, 5122 Dorfen, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-88-920/2630`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `Dr. Thomas Keppert Steuerberatung` — positional overlap with gold: `Prof. Dr. Thomas Keppert`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dkfm. Anton Lammer  Wirtschaftstreuhand Gmb` — positional overlap with gold: `Anton Lammer  Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Freilinger`(person)
- `Jacqueline Dittus`(person)
- `Sausal 90O, 4911 Schönfeld, Österreich`(address)
- `Anton Lammer  Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Mag. Susanne Pöltenstein` — partial — pred is substring of gold: `Mag. Susanne Pöltenstein-Rosenegger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Joachim Annanias`(person)
- `VetR Burkhard Krautschenko`(person)
- `Geizersgraben 6, 2823 Leiding, Österreich`(address)
- `Mag. Susanne Pöltenstein-Rosenegger`(person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

**False Positives:**

- `Dr. Nikolaus` — partial — pred is substring of gold: `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Titus Ohlmer`(person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich`(address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft`(organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `20-234/9874`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Gregor Klocksin`(person)
- `Unterguntschach 85, 3525 Armschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz.in Dr` — partial — pred is substring of gold: `Priv.-Doz.in Dr.in Bianca Gerasimczuk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Frauke Galleithner`(person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

**False Positives:**

- `Mag. Andrea Müller` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`
- `Dr. Adam Müller` — partial — pred is substring of gold: `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Timon Thoennißen`(person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`(address)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Heike Lehmensieck`(person)
- `Höllstein 11, 9852 Neuschitz, Österreich`(address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

**False Positives:**

- `Mag. Andrea Müller` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Evelyn Antwerber`(person)
- `Hertzstraße 25, 5134 Spieglern, Österreich`(address)
- `Dr. Farid Rifaad`(person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_20`)


2) bis 6): Die Dr.in Ing. Viktoria Weigart hafte für die mit diesen Bescheiden über die (den zur Vertretung  nach außen Berufenen Bf.) verhängten Geldstrafen und Verfahrenskosten sowie für sonstige in  Geld bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_65`)


Angemerkt wird noch, dass eine Anfrage beim zuständigen Arbeitsinspektorat Wien Wien  ergeben hat, dass von der Dr.in Ing. Viktoria Weigart kein verantwortlich Beauftragter gemäß § 9 VStG  gemeldet wurde, wie Ihnen bereits im Zuge anderer gegen Sie anhängiger Verfahren zur  Kenntnis gebracht wurde.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_108`)


In den betreffenden Einsprüchen hat der Beschwerdeführer dargelegt, dass er nur  handelsrechtlicher Geschäftsführer der Dr.in Ing. Viktoria Weigart ist.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_144`)


Über die Beschwerde wurde erwogen:  Aus dem Verwaltungsakt ergibt sich folgender Sachverhalt:  Die mehrspurigen Kraftfahrzeuge mit den behördlichen Kennzeichen 1) Auto1 (A), 2) Auto2 (A),  3) Auto1 (A), 4) Auto2 (A) und 5) Auto1 (A) waren zur jeweiligen Beanstandungszeit auf die Dr.in Ing. Viktoria Weigart  AdrFirma1, zugelassen.

**False Positives:**

- `Ing. Viktoria Weigart  Adr` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_145`)


Die Dr.in Ing. Viktoria Weigart wurde von der belangten Behörde mit (sechs) Schreiben als  Zulassungsbesitzerin aufgefordert, innerhalb einer Frist von zwei Wochen ab Zustellung  darüber Auskunft zu erteilen, wem sie das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen  1) Auto1 (A) überlassen gehabt habe, sodass es am 17.12.2019 um 10:15 Uhr in 1060 Wien,  Garbergasse 12, abgestellt gewesen sei (Schreiben vom 07.05.2020, GZ. MA67/Zahl1/2019).

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`
- `Ing. Viktoria Weigart` — similar text (different position): `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_162`)


Dem Verlangen der Behörde wurde von der Dr.in Ing. Viktoria Weigart nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_163`)


Mit sechs Strafverfügungen, eine zu 1) vom 05.06.2020 und fünf zu 2) bis 6) vom 14.07.2020  wurde dem Bf. jeweils angelastet, er habe als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der genannten Fahrzeuge dem jeweils ordnungsgemäß  zugestellten Verlangen der Behörde innerhalb von zwei Wochen ab Zustellung Auskunft zu  geben, wem er das jeweils genannte Fahrzeug mit dem jeweils näher genannten behördlichen  Kennzeichen zu näher bezeichneten Zeitpunkten überlassen gehabt habe, sodass sie jeweils in  näher bezeichneten gebührenpflichtigen Kurzparkzonen abgestellt waren, nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigar` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_168`)


Sachverhalt:  Der Einschreiter ist Geschäftsführer der Dr.in Ing. Viktoria Weigart  Dieses Unternehmen betreibt unter  anderem ein Taxi und Mietwagengewerbe.

**False Positives:**

- `Ing. Viktoria Weigart  Dieses Unternehmen` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)


Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

**False Positives:**

- `Ing. Viktoria Weigar` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

</details>

---

## `genitive_name_no_title` 🏆

**F1:** 0.042 | **Precision:** 0.331 | **Recall:** 0.023  

**Format:** `regex`  
**Rule ID:** `53c8a1f9`  
**Description:**
Matches names following genitive articles (des, der, die) in contexts like 'Beschwerde des [Name]', strictly excluding authorities and organizations.

**Content:**
```
(?:Beschwerde|Bescheid|Verfahren|Sache)\s+(?:des\s+|der\s+|die\s+)([A-ZÄÖÜ][a-zäöüß]+(?:\s+(?:von|van|de|zu|u\.\s*)?[A-ZÄÖÜ][a-zäöüß]+)*(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*(?:\s*,\s*(?:MBA|MSc|BSc|LL\.M|LLB|BEd|Bakk\.\s*(?:iur|phil|rer\.nat|art)))?)\s*(?:,|\n|$|\s+(?:Straß|Gasse|Platz|Weg|Allee|Nr\.|Haus|\d+|GmbH|AG|KG|Verein|Stiftung|Gesellschaft))(?!\s+(?:Finanzamt|Bundesfinanzgericht|Senat|Magistrat|Verwaltungsgericht|Oberlandesgericht|Landesgericht|Bezirksgericht|Bundesfinanzgerichtshof|Verwaltungsgerichtshof|Bundessozialgericht|Verfassungsgerichtshof|Bundesministerium|Landesregierung|Stadt|Gemeinde|Bezirk|Amt|Behörde|Wien|Graz|Linz|Salzburg|Innsbruck|Klagenfurt|Bregenz|Eisenstadt|St\.\s*Pölten|Steuerberatung|Rechtsanwälte|Wirtschaftsprüfung|Partnerschaft|&\s+Partner|\(|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.331 | 0.023 | 0.042 | 127 | 42 | 85 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 42 | 85 | 1809 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Xaver Plaumert, BEd` | `Xaver Plaumert, BEd` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Dr. Wolfgang Aigner` (person)
- `Erwin Agneter` (person)
- `Mag. Belinda  Maria Eder` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Mag. Katharina Moravec` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_2`)


Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des Rosalia Schmieter, Collmannstraße 3, 3335 Lindau, Österreich  vom 22. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. September 2020, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005,idgF,  iVm § 4 Abs. 1 Parkometergesetz 2006, Landesgesetzblatt Nr. 9/2006 idF LGBl für Wien Nr.  24/2012, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Rosalia Schmieter` | `Rosalia Schmieter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Collmannstraße 3, 3335 Lindau, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Jaden Holzfuss` | `Jaden Holzfuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Puntigam` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Harald Schwalbach` | `Harald Schwalbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_2`)


über die Beschwerde des Louisa Kannengiser, Pfaffensteig 10, 3595 Atzelsdorf, Österreich, vom 15. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. März 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016 in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise Folge gegeben als die von der belangten Behörde mit € 60,00 verhängte Geldstrafe  auf € 48,00 und die für den Fall der Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfrei- heitsstrafe auf 10 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Louisa Kannengiser` | `Louisa Kannengiser` |

**Missed by this rule (FN):**

- `Pfaffensteig 10, 3595 Atzelsdorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_3`)


über die Beschwerde der Balthasar Brendtke, Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich, vom 17. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 12. März 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl.  für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Balthasar Brendtke` | `Balthasar Brendtke` |

**Missed by this rule (FN):**

- `Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

| Predicted | Gold |
|---|---|
| `Evelyn Antwerber` | `Evelyn Antwerber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Hertzstraße 25, 5134 Spieglern, Österreich` (address)
- `Dr. Farid Rifaad` (person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter über die Beschwerde des Ivan Thöner, Landlerweg 28, 4273 Kaltenberg, Österreich, vom 7. April 2021 gegen das Straferkenntnis des Magistrates der Stadt Wien vom 25.  Februar 2021, Zahl MA67/Zahl/2020,  betreffend Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016 in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, den Beschluss gefasst:  Die Beschwerde vom 7. April 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ivan Thöner` | `Ivan Thöner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Landlerweg 28, 4273 Kaltenberg, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Hilde Schorpp, Wandschaml 94, 4625 Grub, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 21. Dezember 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung der Rechtsvorschrift des § 2 in Verbindung mit § 4 Abs. 2  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 2 VStG eingestellt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Hilde Schorpp` | `Hilde Schorpp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Wandschaml 94, 4625 Grub, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_3`)


über die Beschwerde des Ludmilla Czimmerninks,  Sennemahd 7, 9832 Latzendorf, Österreich, vom 30. Juni 2021, gegen den Bescheid des Magistrates der Stadt Wien,  Magistratsabteilung 6, vom 7. Juni 2021, GZ. MA67/Zahl/2020, betreffend Abweisung des  Antrages vom 14. Mai 2021 auf Bewilligung eines Zahlungsaufschubes bzw. Ratenansuchens,  nach Durchführung einer mündlichen Verhandlung am 2. September 2021, in Anwesenheit des  Beschwerdeführers und der Schriftführerin IP, zu Recht erkannt:  Die Beschwerde wird gemäß § 50 VwGVG als unbegründet abgewiesen und der ange- fochtene Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Ludmilla Czimmerninks` | `Ludmilla Czimmerninks` |

**Missed by this rule (FN):**

- `Sennemahd 7, 9832 Latzendorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 6` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Theobald Atacan, Göschl 12, 3544 Eisenberg, Österreich, vom 22. November 2021, gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 13. Oktober  2021, Zl. MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 3 Abs. 1  Kontrolleinrichtungenverordnung, Abl. der Stadt Wien Nr. 33/2018, idgF, in Verbindung mit § 4  Abs. 3 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idgF, zu Recht:  Die Beschwerde wird gemäß § 50 VwGVG in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Theobald Atacan` | `Theobald Atacan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Göschl 12, 3544 Eisenberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Rauner über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Pjotr Astore` | `Pjotr Astore` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Rauner` (person)
- `Karl-Ahrer-Straße 11, 3593 Franzen, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Juliana Fassmer, Tillisweg 11, 8773 Sparsbach, Österreich, vom 10. Februar 2022, gegen die Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 31. Jänner 2022, Zlen.

| Predicted | Gold |
|---|---|
| `Juliana Fassmer` | `Juliana Fassmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Tillisweg 11, 8773 Sparsbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Uwe Köhn, Pizet 15, 9441 Waldenstein, Österreich, vom 26. Juli 2018, gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom  13. Juli 2018, betreffend Rückforderung von Familienbeihilfe für den Zeitraum September 2016  bis Februar 2018, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der  Beschwerdevorentscheidung, nämlich für 09/2016-02/2017, stattgegeben.

| Predicted | Gold |
|---|---|
| `Uwe Köhn` | `Uwe Köhn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Pizet 15, 9441 Waldenstein, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Henriette Pöpken, Stromsiedlung IV.R 11, 8510 Neurath, Österreich, Deutschland, vom 22. Mai 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 27. April 2022, Zl. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz  2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Henriette Pöpken` | `Henriette Pöpken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Stromsiedlung IV.R 11, 8510 Neurath, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerde des  Karim Hainzlmeier, Gälaplana 43, 3205 Mühlhofen, Österreich, gegen den Bescheid des Finanzamtes Bregenz vom 20. Mai 2016  betreffend Einkommensteuer 2015, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Karim Hainzlmeier` | `Karim Hainzlmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Gälaplana 43, 3205 Mühlhofen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Melinda Brotke, Jägerloch 26, 8443 Praratheregg, Österreich, vom 22. März 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 3.  März 2021, Zahl MA67/206700943579/2020, wegen einer Verwaltungsübertretung gemäß § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für  Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Melinda Brotke` | `Melinda Brotke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Jägerloch 26, 8443 Praratheregg, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt  Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Juri Boyarzyn, Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich, vom 28. Juli 2020, gegen den Bescheid des Finanzamtes Österreich  vom 16. Juli 2020, betreffend Familienbeihilfe 01.2019-01.2021, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juri Boyarzyn` | `Juri Boyarzyn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Volkmar Quadfasel, Forstbergstraße 5, 4144 Zanklbach, Österreich, vertreten durch Dr. Sebastian Mariano Volkmar Lenz,  Laurenzerberg 1, 1010 Wien, vom 25. April 2021, gegen den Bescheid des Finanzamtes  Österreich vom 26. März 2021, betreffend Abweisung des Antrages auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe ab Dezember 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Volkmar Quadfasel` | `Volkmar Quadfasel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Forstbergstraße 5, 4144 Zanklbach, Österreich` (address)
- `Dr. Sebastian Mariano Volkmar Lenz` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_2`)


Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde des Ariadne Schmalzried, Nejesgasse 7K, 6094 Bachl, Österreich, vom 20. Juli 2020, gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  12. Mai 2020, betreffend Abweisung des Antrages auf Gewährung der Familienbeihilfe in Höhe  der gemäß § 8 Abs. 3 und 4 FLAG 1967 festgesetzten Beträge sowie des Kinderabsetzbetrages  in Höhe des in § 33 Abs. 3 erster Satz EStG 1988 festgesetzten Betrages zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ariadne Schmalzried` | `Ariadne Schmalzried` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nejesgasse 7K, 6094 Bachl, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde der Adriana Wottge,  Ferstelgasse 22, 3282 Forsthub, Österreich, vom 20. Juli 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 14. Juli 2022, Zl. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz 2006, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Adriana Wottge` | `Adriana Wottge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ferstelgasse 22, 3282 Forsthub, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/138513.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Univ.-Prof.in Verena Sobzig  über die Beschwerde des  Peter Scheidhauer, Klimaweg 103, 8232 Untersafen, Österreich, vom 31.05.2022 gegen den Bescheid des Finanzamtes Österreich vom  26.04.2022 betreffend Abweisung eines Antrages auf Nachsicht zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Scheidhauer` | `Peter Scheidhauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Verena Sobzig` (person)
- `Klimaweg 103, 8232 Untersafen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Chantal Franzk,  Feldererweg 14 - 20, 5166 Rudersberg, Österreich, vom 14. Juni 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 31. Mai 2022, GZ MA 67/Z2/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit §  4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Berufungsverhandlung am 19. September 2022, im  Beisein der Schriftführerin IP, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Chantal Franzk` | `Chantal Franzk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Feldererweg 14 - 20, 5166 Rudersberg, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Magdalena Unterreiter, Anichstraße 5, 8953 Donnersbach, Österreich, Deutschland, vom 22. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, als Verwaltungsstrafbehörde vom  10. März 2022, Zl. Zahl, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magdalena Unterreiter` | `Magdalena Unterreiter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Anichstraße 5, 8953 Donnersbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Cornelia Reifgerste` | `Cornelia Reifgerste` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Scherzergütl 18K, 9622 Golz, Österreich` (address)
- `Freimüller Rechtsanwalts GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `M. F.` (person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

| Predicted | Gold |
|---|---|
| `Wladimir Leukhardt` | `Wladimir Leukhardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich` (address)
- `Stadt Wien` (organisation)
- `Bundesfinanzgerichts` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek über die Beschwerde des  Lubomir Vaist, Sulzbachfelderstraße 3, 9361 Judendorf, Österreich, vom 4. Jänner 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 12. Oktober 2022, GZ. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Lubomir Vaist` | `Lubomir Vaist` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Sulzbachfelderstraße 3, 9361 Judendorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde des Noah Blanck, Ägidiweg 63, 4111 Hamberg, Österreich, vom 7. Juni 2022, gegen den Bescheid des  Finanzamtes Österreich vom 24. Mai 2022, betreffend Abweisung des Antrages auf  Familienbeihilfe ab Juli 2020, zu Recht:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Noah Blanck` | `Noah Blanck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Ägidiweg 63, 4111 Hamberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/141221.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141221.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin ********** über die Beschwerde des  Ronja Rönecke, Brandseppengasse 25, 8342 Badenbrunn, Österreich, vom 28. März 2023 gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Februar 2023, GZ.  MA67/Zahl/2022, iZm einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht  erkannt:  Die Beschwerde gegen den Zurückweisungsbescheid wird gemäß § 50 VwGVG als unbe- gründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ronja Rönecke` | `Ronja Rönecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brandseppengasse 25, 8342 Badenbrunn, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck über die Beschwerde des  Maximilian Mlynarzyk, Kellersteig 6O, 9063 Techmannsdorf, Österreich, vom 7. Juni 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 9.  Mai 2023, GZ. MA67/GZ/2023, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde Folge gegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 1 VStG eingestellt.  II. Gemäß § 52 Abs. 1 und 2 VwGVG iVm § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Maximilian Mlynarzyk` | `Maximilian Mlynarzyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johannes Böck` (person)
- `Kellersteig 6O, 9063 Techmannsdorf, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/142233.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Silke Czejka, Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich, vom 01. September 2022 gegen den Bescheid des Finanzamtes  Österreich vom 30. August 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Monat Mai 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silke Czejka` | `Silke Czejka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri über die Beschwerde der Silvia Burscheid,  Sackgasse 48, 8664 Kleinveitsch, Österreich, vom 16. Jänner 2023 gegen den Bescheid des Finanzamtes Österreich vom  19. Dezember 2022 betreffend Abweisung des Antrages auf Gewährung der Familienbeihilfe  und Kinderabsetzbetrag von Juni 2021 bis September 2022, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO insofern teilweise Folge gegeben, als nur die für den  Zeitraum Juni 2021 bis August 2022 bezogenen Familienbeihilfen und Kinderabsetzbeträge  zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Silvia Burscheid` | `Silvia Burscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sackgasse 48, 8664 Kleinveitsch, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  des Bernhard Voronov, Prof.-Leopold-Farnleitner-Weg 18, 4673 Grub, Österreich, vom 3. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 22. April 2022, betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe vom 31. Jänner 2022 für S., V.nr. Nr., ab Jänner 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bernhard Voronov` | `Bernhard Voronov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Prof.-Leopold-Farnleitner-Weg 18, 4673 Grub, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142576.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142576.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Carla Würtele, Herta-Nest-Straße 15, 8046 Ursprung, Österreich, vom 23. Oktober 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 13. Oktober 2023,  GZ. MA67/Zahl/2023, wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Carla Würtele` | `Carla Würtele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Herta-Nest-Straße 15, 8046 Ursprung, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde des  Desiree Hannecken, Lasseestraße 13, 5144 Handenberg, Österreich, vom 5. Oktober 2023 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 28. September 2023, GZ. MA67/Zahl/2023,  wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung  in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Desiree Hannecken` | `Desiree Hannecken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Irene Kohler` (person)
- `Lasseestraße 13, 5144 Handenberg, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/143315.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143315.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Emanuel Bulthuis, Martinsplatz 47, 6167 Neustift im Stubaital, Österreich, vom 7. Dezember 2022 gegen den Bescheid des Finanzamtes  Österreich vom 8. November 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für die Monate August und September 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emanuel Bulthuis` | `Emanuel Bulthuis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Martinsplatz 47, 6167 Neustift im Stubaital, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner über die Beschwerde  des Herbert Leitzmann, Schörgendorfstraße 80D, 9560 Förolach, Österreich, vom 30. Juni 2023, gegen die drei Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 21. Juni 2023,   GZen 1) MA67/Zahl1/2023, 2) MA67/Zahl2/2023 und   3) MA67/Zahl3/2023, alle drei wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  werden die drei Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Herbert Leitzmann` | `Herbert Leitzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Ebner` (person)
- `Schörgendorfstraße 80D, 9560 Förolach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/143486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143486.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde des Danielle Conraths, Rollfährestraße 2I, 4132 Atzesberg, Österreich, vom 8. Mai 2022 gegen den Bescheid des  FA Gmunden Vöcklabruck  vom 12. April 2022 betreffend Zahlungserleichterungen § 212 BAO 2022 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Danielle Conraths` | `Danielle Conraths` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniela Regina Denk` (person)
- `Rollfährestraße 2I, 4132 Atzesberg, Österreich` (address)
- `FA Gmunden Vöcklabruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_159`)


Durch die Regelungen des § 188 BAO wird somit  ein Ausschnitt der Einkommensteuer-Verfahren der Beteiligten, der im Rahmen der  Festsetzung der Einkommensteuer für die Beteiligten durchzuführen wäre, in ein  einheitliches Sonderverfahren zusammengefasst (vgl. nochmals das hg.

**False Positives:**

- `Beteiligten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Elisabeth Schafstall`(person)
- `Leithagürtel 20, 4251 Steinwald, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Finanzamtes Wien 1/23`(organisation)
- `Jana Papenkord`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ali Jäckle`(person)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sabine Tiedicke`(person)
- `Ritterhof 8, 4280 Harlingsedt, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  3/6/7/11/15`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing. Sascha Hilcker`(person)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich`(address)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Juri Pfluegler`(person)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich`(address)
- `Finanzamtes Wien  4/5/10`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_2`)


Stock, 1150  Wien, über die Beschwerde vom 13. März 2020 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 4. März 2020 betreffend Umsatzsteuer 2018, Steuernummer ***, zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO im eingeschränkten Umfang Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien  4/5/10`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `Univ.-Prof.in Shoshana Leuther`(person)
- `Hagleithen 8, 3345 Strohmarkt, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `80-897/7654`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `HR OSR Leonie Ercklentz`(person)
- `Karnitzen 135, 9635 Kronhof, Österreich`(address)
- `LKP Steuerberatung OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_187`)


Es ist Sache des  Steuerpflichtigen, der Abgabenbehörde die Gründe zu nennen, aus denen er die Verlegung des  Familienwohnsitzes an den Ort der Beschäftigung als unzumutbar ansieht (vgl. Jakom- ESTG- Kommentar, 12.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Renate Schohaj`(person)
- `Vera Matyschek`(person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Imre Annecke`(person)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Othmar Feuerbaum`(person)
- `Ingeborg Kollaczek`(person)
- `Hufgasse 10, 9062 Gabriel, Österreich`(address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `47-554/2547`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Rudolf Bogdanowic`(person)
- `Am Gehrn 3, 9312 Gaming, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `90-074/8383`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Thassilo Schoenrock, LLM`(person)
- `Hochscharten 126D, 5122 Dorfen, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-88-920/2630`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Rosemarie Schan`(person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Susette Bertnik`(person)
- `Ehrenbachweg 31, 9322 Hirt, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)
- `32-807/7639`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_117`)


Zur Frage der fehlenden Zustellung:  § 7 Zustellgesetz (ZustG): Unterlaufen im Verfahren der Zustellung Mängel, so gilt die  Zustellung als in dem Zeitpunkt dennoch bewirkt, in dem das Dokument dem Empfänger  tatsächlich zugekommen ist.

**False Positives:**

- `Zustellung Mängel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_283`)


Die umfangreichen Ermittlungen der Abgabenbehörde haben ergeben, dass es sich bei den  drei genannten Firmen um Scheinfirmen handelt.   Anzumerken ist in diesem Zusammenhang, dass die in der Beschwerde erwähnte  abgabenrechtliche Beschwerde der Starnberg Beratung GmbH gegen den Haftungsbescheid mit ho.

**False Positives:**

- `Starnberg Beratung` — partial — pred is substring of gold: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

**False Positives:**

- `Finanzamtes Bruck Eisenstadt Oberwart` — type mismatch — same span as gold: `Finanzamtes Bruck Eisenstadt Oberwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Raimund Ladwig`(person)
- `Birkenring 18, 8451 Pernitsch, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Olivia Ziegeler`(person)
- `Mike Reislehner`(person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich`(address)
- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `44-773/5557`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_168`)


(5) Der Träger, der eine vorläufige Leistungszahlung vorgenommen hat, die höher ist als der  letztlich zu seinen Lasten gehende Betrag, kann den zu viel gezahlten Betrag nach dem  Verfahren des Artikels 73 der Durchführungsverordnung vom vorrangig zuständigen Träger  zurückfordern.

**False Positives:**

- `Artikels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_299`)


Es ist nach wie vor Sache der Mitgliedstaaten, wem sie unter welchen Voraussetzungen wie  lange Familienleistungen zuerkennen.

**False Positives:**

- `Mitgliedstaaten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_467`)


Durch diese Rechtsprechung des EuGH aus dem Jahr 2015 wurde klargestellt, dass das  Unionsrecht selbst keinen originären Anspruch auf nationale Familienleistungen vermittelt.   Es ist Sache der Mitgliedstaaten, wem sie unter welchen Voraussetzungen und wie lange  Familienleistungen zuerkennen.

**False Positives:**

- `Mitgliedstaaten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_88`)


Es ist Sache des Beschuldigten, initiativ alles darzulegen, was  seiner Entlastung dienen kann.

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_68`)


Wenn nach diesem Zeitraum der Familienwohnsitz beibehalten wird, ist es Sache des  Steuerpflichtigen, der Abgabenbehörde die Gründe zu nennen, aus denen er die Verlegung des  Familienwohnsitzes an den Ort der Beschäftigung als unzumutbar ansieht.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Dipl.-Ing. Melinda Herrwerth, Dürergasse 7, 4872 Windbichl, Österreich, Steuernummer 40-459/9630   1.) betreffend die Beschwerde vom 3. Juni 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 27. Mai 2020, mit dem der  Antrag vom 28. Februar 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den  Zeitraum ab Mai 2018 abgewiesen wurde, beschlossen:   Der Vorlageantrag vom 1. März 2021, insoweit damit die Vorlage der Beschwerde vom 3. Juni  2020 beantragt wird, wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) in  Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Melinda Herrwerth`(person)
- `Dürergasse 7, 4872 Windbichl, Österreich`(address)
- `40-459/9630`(tax_number)
- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `Finanzamt Österreich`(organisation)
- `Lubomir Nakajima`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_2`)


2.) über die Beschwerde vom 2. November 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 6. Oktober 2020 betreffend  Abweisung des Antrages vom 3. Juni 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den Zeitraum September 2015 bis April 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `Finanzamt Österreich`(organisation)
- `Lubomir Nakajima`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_65`)


Es ist Sache des Lieferanten, die Ware  zum vereinbarten Übergabeort zu transportieren, er hat die Kosten dafür zu tragen und er  trägt auch das Risiko von Beschädigungen der Ware, Diebstahl oder sonstigem Untergang der  Ware.

**False Positives:**

- `Lieferanten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_111`)


Demnach ist es klar Sache des  Ersterwerbers, die Ware zum Zweiterwerber zu transportieren und dieser kann erst nach  Ankunft der Ware bei ihm darüber wie ein Eigentümer verfügen.

**False Positives:**

- `Ersterwerbers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_529`)


Es ist nämlich grundsätzlich Sache der  Steuerbehörden, bei den Steuerpflichtigen die erforderlichen Kontrollen durchzuführen, um  Unregelmäßigkeiten und Mehrwertsteuerhinterziehung aufzudecken und gegen den  Steuerpflichtigen, er diese Unregelmäßigkeiten oder Steuerhinterziehung begangen hat,  Sanktionen zu verhängen.

**False Positives:**

- `Steuerbehörden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_595`)


Nach der angeführten Judikatur wäre es Sache der Abgabenbehörde, objektive Umstände  rechtlich hinreichend nachzuweisen, die auf eine fehlende Gutgläubigkeit der Bf. schließen  lassen.

**False Positives:**

- `Abgabenbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_193`)


Dabei ist es Sache des Abgabepflichtigen, die  außersteuerlichen Gründe darzutun (Ritz, BAO5, § 22 Tz 1 ff).

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_30`)


Es ist Sache des Beschuldigten, initiativ alles darzulegen, was  seiner Entlastung dienen kann.

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_184`)


Dabei ist es Sache des Abgabepflichtigen, die  außersteuerlichen Gründe darzutun (Ritz, BAO5, § 22 Tz 1 ff).

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_189`)


Dabei ist es Sache des Abgabepflichtigen, die  außersteuerlichen Gründe darzutun (Ritz, BAO5, § 22 Tz 1 ff).

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Rauner, die RichterinR  sowie die fachkundigen Laienrichter Gregor Ableidinger und Dr. Franz Kandlhofer in der  Beschwerdesache Lieselotte Schluessel, Hannakstraße 205, 5121 Wimm, Österreich, über die Beschwerde vom 22. Februar 2016  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 10. Februar 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Rauner`(person)
- `Gregor Ableidinger`(person)
- `Dr. Franz Kandlhofer`(person)
- `Lieselotte Schluessel`(person)
- `Hannakstraße 205, 5121 Wimm, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Ri, die Richterin Mag. Riin sowie  die fachkundigen Laienrichter A und B, in der Beschwerdesache Karina Schliekau, Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich,  vertreten durch die Kanzlei, über die Beschwerde vom 15. Februar 2018 gegen den Bescheid  des Finanzamtes Österreich, vormals Finanzamt Wien 3/6/7/11/15 Schwechat und Gerasdorf,  vom 1. Februar 2018 betreffend Feststellung der Einkünfte § 188 BAO 2016, nach  Durchführung einer mündlichen Verhandlung am 17. November 2021 in Anwesenheit der  Schriftführerin C, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Österreich` — type mismatch — same span as gold: `Finanzamtes Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Riin`(person)
- `Karina Schliekau`(person)
- `Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Wien 3/6/7/11/15`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_2`)


Die Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes  Österreich vom 03. Juli 2013 bezüglich Wiederaufnahme der Verfahren die  Umsatzsteuer 2009-2011 betreffend wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes  Österreich`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_53`)


Es ist Sache des Fahrzeuglenkers, für eine geeignete Anbringung des Parkscheines hinter der  Windschutzscheibe zu sorgen.

**False Positives:**

- `Fahrzeuglenkers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gabriele Kuehberger`(person)
- `Wieser 53, 8341 Puch, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14  Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sulamith Jedwillat`(person)
- `Brandenbergweg 15, 8353 Pichla, Österreich`(address)
- `Mag. Michael Payr`(person)
- `Finanzamtes Wien 12/13/14  Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `41-852/7395`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_51`)


Es sei Sache des Beschuldigten, initiativ alles darzulegen, was seiner Entlastung dienen könne.

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Uwe Köhn, Pizet 15, 9441 Waldenstein, Österreich, vom 26. Juli 2018, gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom  13. Juli 2018, betreffend Rückforderung von Familienbeihilfe für den Zeitraum September 2016  bis Februar 2018, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der  Beschwerdevorentscheidung, nämlich für 09/2016-02/2017, stattgegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Heidemarie Winkler`(person)
- `Uwe Köhn`(person)
- `Pizet 15, 9441 Waldenstein, Österreich`(address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_42`)


Es ist Sache des Fahrzeuglenkers, für eine geeignete Anbringung des Parkscheines hinter der  Windschutzscheibe zu sorgen.

**False Positives:**

- `Fahrzeuglenkers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_97`)


Es ist Sache des Fahrzeuglenkers, für eine geeignete Anbringung des Parkscheines hinter der  Windschutzscheibe zu sorgen.

**False Positives:**

- `Fahrzeuglenkers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch der Richter R. in der Beschwerdesache Dipl.-Ing. Emma Chatzistamatis, Senden 22, 4673 Unterbergham, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 17. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierten Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019, Steuernummer 59-959/5444, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes  Hollabrunn Korneuburg Tulln` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Emma Chatzistamatis`(person)
- `Senden 22, 4673 Unterbergham, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `59-959/5444`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marlies Seipold, Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich, über die Beschwerde vom 27. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 14. Jänner 2020 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum März 2017 bis September 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Marlies Seipold`(person)
- `Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt Wien` — partial — pred is substring of gold: `Finanzamt Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Massimo Friedhoff`(person)
- `Jaden Grothmann`(person)
- `Finanzamt Wien 1/23`(organisation)
- `32-847/2958`(tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache David Radeke, Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich, über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 18. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierte Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019,   Steuernummer 15-752/7224, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes  Hollabrunn Korneuburg Tulln` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `David Radeke`(person)
- `Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `15-752/7224`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache ÖkR Istvan  Thiebaud, Ziakpark 78, 3213 Hollenstein, Österreich, vertreten durch ECOVIS Scholler & Partner, Wirtschaftstreuhand GmbH,  Schmalzhofgase 4, Tür 12, 1060 Wien, über die Beschwerden vom 28. Juli 2017 gegen den  Bescheid des Finanzamtes Wien 4/5/10, nunmehr Finanzamt Österreich, vom 29. Juni 2017  betreffend Einkommensteuer 2015, Steuernummer 04-368/0800, sowie vom 23. Jänner 2020  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf, nunmehr Finanzamt  Österreich, vom 25. November 2019 betreffend Einkommensteuer der Jahre 2016 und 2017  sowie Anspruchszinsen 2016 und 2017, Steuernummer ****, nach der am 12. Mai 2022 in  Hintere Zollamtsstraße 2b, 1030 Wien, durchgeführten mündlichen Verhandlung im Beisein  der Schriftführerin S   1.) zu Recht erkannt:   Die Beschwerden gegen die Einkommensteuerbescheide der Jahre 2015 und 2016 sowie gegen  den Anspruchszinsenbescheid des Jahres 2016 wird gemäß § 279 BAO als unbegründet  abgewiesen  2.) beschlossen:  Die Beschwerden gegen den Einkommensteuerbescheid des Jahres 2017 sowie gegen den  Anspruchszinsenbescheid des Jahres 2017 wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 4/5/10`

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

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_35`)


Die Beschwerde der Heimwerk GmbH war daher als unzulässig zurückzuweisen.

**False Positives:**

- `Heimwerk` — partial — pred is substring of gold: `Heimwerk GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heimwerk GmbH`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_41`)


Es ist Sache des Beschuldigten, initiativ alles darzulegen, was seiner  Entlastung dienen kann.

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Univ.-Prof.in Konstanze Lukass  in der Beschwerdesache Selma Katirci,  Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich  vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/Tür  10, 1060 Wien, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 7. Oktober 2019 betreffend Abweisung des  Antrags vom 23. September 2019 auf Gewährung der Familienbeihilfe und des  Kinderabsetzbetrages ohne Vornahme einer Indexierung  gemäß  § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`(person)
- `Selma Katirci`(person)
- `Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich`(address)
- `Brehm & Sahinol Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

**False Positives:**

- `Magistratsabteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Wladimir Leukhardt`(person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich`(address)
- `Stadt Wien`(organisation)
- `Bundesfinanzgerichts`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/139872.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Waldemar Kosiol,  Afinger Hauptstraße 4, 4870 Schneiderweg, Österreich, über die Beschwerde vom 10. Juli 2014 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 7. Juli 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012  Steuernummer 47-100/4541, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Waldemar Kosiol`(person)
- `Afinger Hauptstraße 4, 4870 Schneiderweg, Österreich`(address)
- `Finanzamtes  Wien 4/5/10`(organisation)
- `47-100/4541`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/139889.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139889.1_82`)


Es ist Sache des Steuerpflichtigen, der die Beibehaltung des in unüblicher Entfernung vom  Beschäftigungsort gelegenen Familienwohnsitzes als beruflich veranlasst geltend macht, der  Abgabenbehörde die Gründe zu nennen und nachzuweisen, aus denen er die Verlegung des  Familienwohnsitzes als unzumutbar ansieht, die Unzumutbarkeit der Wohnsitzverlegung kann  ihre Ursachen dabei aber auch in der privaten Lebensführung haben (VwGH 9.10.1991,  88/13/0121).

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/140529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140529.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Li Megerlein, Tungassingerstraße 18, 5061 Gfalls, Österreich, über die Beschwerde vom 5. April 2019 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 4. April 2019, Steuernummer  89-939/3728, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Li Megerlein`(person)
- `Tungassingerstraße 18, 5061 Gfalls, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `89-939/3728`(tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_285`)


Gem. § 119 iVm § 138 BAO ist es Sache des Abgabenpflichtigen, die für die Erlangung  abgabenrechtlicher Begünstigungen bedeutsamen Umstände nach Maßgabe der  Abgabenvorschriften vollständig und wahrheitsgemäß offenzulegen.

**False Positives:**

- `Abgabenpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait  in der Beschwerdesache   Prof. Ing. Eduard Skroblies, Forchetweg 18, 4692 Albertsham, Österreich,   über die Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf (nunmehr Finanzamt Österreich) vom 10. November 2014 betreffend  Körperschaftsteuer 2011, vom 19. November 2014 betreffend Körperschaftsteuer 2012 und  2013 sowie die Beschwerde vom 12. Juli 2016 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 7. Juli 2016 betreffend Körperschaftsteuer 2014   I. beschlossen:  Der Vorlageantrag betreffend Körperschaftsteuer 2011 wird zurückgewiesen.

**False Positives:**

- `Finanzamtes Wien` — similar text (different position): `Finanzamtes Wien  12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait`(person)
- `Prof. Ing. Eduard Skroblies`(person)
- `Forchetweg 18, 4692 Albertsham, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/141161.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141161.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor in der Beschwerdesache  Li Wilmering, Pichlernstraße 1, 4751 Stögen, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid  des Finanzamtes Wien 1/23 vom 21. Jänner 2020 betreffend Abweisung eines Antrages auf  Familienbeihilfe, Oktober 2019 bis Jänner 2020 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Doktor`(person)
- `Li Wilmering`(person)
- `Pichlernstraße 1, 4751 Stögen, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/143650.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143650.1_28`)


Unterlaufen im Verfahren der Zustellung Mängel, so gilt gemäß § 7 ZustG die Zustellung als in  dem Zeitpunkt dennoch bewirkt, in dem das Dokument dem Empfänger tatsächlich  zugekommen ist.

**False Positives:**

- `Zustellung Mängel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/143870.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143870.1_95`)


Es ist Sache des Steuerpflichtigen, der die Beibehaltung des in unüblicher Entfernung vom  Beschäftigungsort gelegenen Familienwohnsitzes als beruflich veranlasst geltend macht, der  Abgabenbehörde die Gründe zu nennen und nachzuweisen, aus denen er die Verlegung des  Familienwohnsitzes als unzumutbar ansieht.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `represented_by` 🏆

**F1:** 0.019 | **Precision:** 0.281 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `aeabc6b8`  
**Description:**
Matches names following 'vertreten durch', strictly requiring a full name structure and excluding company names or job titles without names.

**Content:**
```
(?:vertreten\s+durch)\s+([A-ZÄÖÜ][a-zäöüß]+(?:\s+(?:von|van|de|zu|u\.\s*)?[A-ZÄÖÜ][a-zäöüß]+)*(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*(?:\s*,\s*(?:MBA|MSc|BSc|LL\.M|BEd|Bakk\.\s*(?:iur|phil|rer\.nat|art)))?)\s*(?:GmbH|AG|KG|OG|e\.U\.|Verein|Stiftung|Gesellschaft|Rechtsanw\u00e4lte|Wirtschaftspr\u00fcfung|Steuerberatung|&\s+Partner|\(|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.281 | 0.010 | 0.019 | 64 | 18 | 46 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 18 | 46 | 1833 |

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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Erich Allbrand` | `Erich Allbrand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Robert Derici` (person)
- `Exlgasse 12, 9623 Karnitzen, Österreich` (address)
- `12-876/0077` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/141195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141195.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

| Predicted | Gold |
|---|---|
| `Helga Kraus` | `Helga Kraus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Cassandra Schmedtje` (person)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146104.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146104.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146141.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/147002.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147002.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vertr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Finanzamtes Wien 1/23`(organisation)
- `Jana Papenkord`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Wolfgang Tiwald`(person)
- `Kirsten Renneissen`(person)
- `Egererweg 9, 5760 Niederhaus, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Dr. Thomas Keppert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_2`)


Jeffrey Marinopoulos, Moosbauernstraße 12, 9341 Wattein, Österreich, als atypisch still Beteiligte an der vormaligen Leroy Kusznierz,  vertreten durch Prof. Thomas Keppert Steuerberatung und Wirtschaftsprüfung GmbH,  Theobaldgasse 19, 1060 Wien,  über die Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Klagenfurt vom  24. April 2012 die Wiederaufnahme des Verfahrens die Feststellung von Einkünften und die  Feststellung von Einkünften gemäß § 188 BAO betreffend, je für das Jahr 2007, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Prof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeffrey Marinopoulos`(person)
- `Moosbauernstraße 12, 9341 Wattein, Österreich`(address)
- `Leroy Kusznierz`(person)
- `Thomas`(person)
- `Finanzamtes Klagenfurt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Lieselotte Reinicker`(person)
- `Raingasse 32, 9552 Ossiachberg, Österreich`(address)
- `Dr. X`(person)
- `Finanzamtes`(organisation)
- `FA Österreich`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinI. in der Beschwerdesache Violetta Bailmann, Schlosserfeld 35, 9632 Hochwart, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 20. Oktober 2016 gegen  die Bescheide des Finanzamtes Spittal Villach vom 22. September 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012 (Steuernummer  82-877/4906 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vogelsberger Hoffmann Wacker` — partial — pred is substring of gold: `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Violetta Bailmann`(person)
- `Schlosserfeld 35, 9632 Hochwart, Österreich`(address)
- `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG`(organisation)
- `Finanzamtes Spittal Villach`(organisation)
- `82-877/4906`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Laurin Überschar  in der Beschwerdesache Albert Theiselmann,  Hochmark 31g, 8323 Unterbuch, Österreich, vertreten durch Radike, Hammerl & Partner Steuerberatung GmbH,  Bisamberger Straße 2/1/8, 2100 Korneuburg, betreffend Beschwerde vom 17. Juni 2021 gegen  die Bescheide des Finanzamtes Österreich vom 20. Mai 2021 betreffend Einkommensteuer  2015 und 2016, Steuernummer 15-781/1702, den Beschluss:   I. Die Beschwerde wird gemäß § 256 Abs 3 Bundesabgabenordnung (BAO) als  gegenstandslos erklärt.

**False Positives:**

- `Radike` — partial — pred is substring of gold: `Radike, Hammerl & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Laurin Überschar`(person)
- `Albert Theiselmann`(person)
- `Hochmark 31g, 8323 Unterbuch, Österreich`(address)
- `Radike, Hammerl & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `15-781/1702`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi als Vorsitzenden, den Richter Ri2 als  beisitzender Richter, SenLR1 als fachkundiger Laienrichter und SenLR2 als fachkundiger  Laienrichter in der Beschwerdesache Alois Kleynsteuber, Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich, vertreten durch Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien,  über die Beschwerde vom 14. September 2012 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg vom 6. September 2012, StNr. 79-708/0061, betreffend Einkommensteuer  2008 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hallas` — partial — pred is substring of gold: `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Alois Kleynsteuber`(person)
- `Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich`(address)
- `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG`(organisation)
- `FA Wien 9/18/19  Klosterneuburg`(organisation)
- `79-708/0061`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gabriele Kuehberger`(person)
- `Wieser 53, 8341 Puch, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Denis Diekötter  in KLG Kreuzbau 16, 8242 Kronegg, Österreich, vertreten durch Rein & Partner Steuerberatung GmbH & Co KG in  8230 Hartberg, Alleegasse 13, über die Beschwerde vom 22.3.2017 gegen die Bescheide des  Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 14.3.2017 betreffend   - Einkommensteuer 2012, 2013, 2014 und 2015 und  - Umsatzsteuer 2012, 2013, 2014 und 2015  zu Recht erkannt:   I. Insoweit sich die Beschwerde gegen die Umsatzsteuerbescheide 2012, 2013, und  2014 richtet, wird dem Beschwerdebegehren gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rein` — partial — pred is substring of gold: `Rein & Partner Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Denis Diekötter`(person)
- `KLG Kreuzbau 16, 8242 Kronegg, Österreich`(address)
- `Rein & Partner Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

**False Positives:**

- `Koch` — partial — pred is substring of gold: `Koch & Partner  SteuerberatungsgmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes`(organisation)
- `Harald Hilderink`(person)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich`(address)
- `Koch & Partner  SteuerberatungsgmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Chen Geßlein  in der Beschwerdesache MedR Techn R Mathilda Elfeldt,  Klingengasse 112, 9556 Waggendorf, Österreich, vertreten durch Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH, Kurandtplatz 1, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 29. Jänner  2021 gegen den Bescheid des Finanzamt Vorarlberg  vom 18. Jänner 2021 betreffend Einkommensteuer  2019 Steuernummer 43-811/9169  zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Dr` — similar text (different position): `MedR Techn R Mathilda Elfeldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Chen Geßlein`(person)
- `MedR Techn R Mathilda Elfeldt`(person)
- `Klingengasse 112, 9556 Waggendorf, Österreich`(address)
- `Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH`(organisation)
- `Finanzamt Vorarlberg`(organisation)
- `43-811/9169`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Gisbert Löhberg`(person)
- `Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich`(address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Österreich`(organisation)
- `73-737/2281`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Herbert Lindermayer  in der Beschwerdesache Anneliese Dreschmann,  Nußbacher Straße 43, 3650 Kehrbach, Österreich, vertreten durch Schwaiger & Partner Steuerberatung, Anton-Eder-Straße 5,  6020 Innsbruck, über die Beschwerde vom 19. Jänner 2021 gegen den Bescheid des FA Graz-Stadt  vom 13. Jänner 2021 betreffend Energieabgabenvergütung 2015 Steuernummer  60-855/1189  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Schwaiger` — partial — pred is substring of gold: `Schwaiger & Partner Steuerberatung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Herbert Lindermayer`(person)
- `Anneliese Dreschmann`(person)
- `Nußbacher Straße 43, 3650 Kehrbach, Österreich`(address)
- `Schwaiger & Partner Steuerberatung`(organisation)
- `FA Graz-Stadt`(organisation)
- `60-855/1189`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Herrn  Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Muran Grönewald, Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner, Rechtsanwälte,  Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 19. Dezember 2019 gegen  die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich) vom  11. Dezember 2019 betreffend Wiederaufnahme § 303 BAO /  ESt 2013 sowie vom 12.12.2019  betreffend Wiederaufnahme § 303 / ESt 2014 und betreffend Wiederaufnahme § 303 / ESt  2015 zu Steuernummer 87-098/9833  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Pallauf Meißnitzer Staindl` — partial — pred is substring of gold: `Pallauf Meißnitzer Staindl & Partner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Muran Grönewald`(person)
- `Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich`(address)
- `Pallauf Meißnitzer Staindl & Partner`(organisation)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `87-098/9833`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/140407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140407.1_3`)


Ri sowie die fachkundigen Laienrichter laienri1 und lairi2 in der Beschwerdesache  [...], Adr1, vertreten durch KomplGmbH als Komplementärin, diese vertreten durch Gf als  Geschäftsführer, Adr1, bzw.  KomplGmbH als Komplementärin, diese vertreten durch Gf als  Geschäftsführer in Adr4,  über die Beschwerde vom 8. März 2018 gegen die Bescheide des (seinerzeitigen) Finanzamtes  Klagenfurt, nunmehr Finanzamt Österreich, vom 14. Februar 2018 betreffend die  Wiederaufnahme der Verfahren bezüglich der Feststellung der Einkünfte gemäß § 188 BAO für  die Jahre 2007 bis 2010 sowie betreffend die Feststellungsbescheide gemäß § 188 BAO für die  Jahre 2007 bis 2010, zu Steuernummer 72-642/0195, nach der am 15.03.2023 in  Anwesenheit der Schriftführerin FOI Claudia Orasch durchgeführten mündlichen Verhandlung  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kompl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `72-642/0195`(tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/141184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141184.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Rosamunde Schmaus,  Josef Greiner-Gasse 2, 6450 Heiligkreuz, Österreich, vertreten durch Vertreter, VertreterAdr, betreffend die Beschwerde vom  9. Oktober 2013 gegen die Bescheide des FA (nunmehr Finanzamt Österreich) vom  5. September 2013 betreffend Umsatzsteuer 2011 und Einkommensteuer 2011 Steuernummer  74-084/1756  beschlossen:  Die Beschwerdevorentscheidung (vormals Berufungsvorentscheidung) vom 22. November  2013 betreffend den Umsatz- und den Einkommensteuerbescheid 2011 vom 05. September  2013 wird wegen Rechtswidrigkeit aufgehoben.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Rosamunde Schmaus`(person)
- `Josef Greiner-Gasse 2, 6450 Heiligkreuz, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `74-084/1756`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/142063.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142063.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Frauke Glowatsch, St.Georgen a.W. 12, 4776 Großwaging, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner,  Rechtsanwälte, Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 11.6.2019  und 26.11.2019 gegen die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt  Österreich;

**False Positives:**

- `Pallauf Meißnitzer Staindl` — partial — pred is substring of gold: `Pallauf Meißnitzer Staindl & Partner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Frauke Glowatsch`(person)
- `St.Georgen a.W. 12, 4776 Großwaging, Österreich`(address)
- `Pallauf Meißnitzer Staindl & Partner`(organisation)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143501.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143822.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143822.1_2`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hoffmann Reitsammer` — partial — pred is substring of gold: `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Ing. Marion Kloefkorn`(person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`(address)
- `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `40-620/0106`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_2`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Armin Treichl, den Richter Dr.  Roman Galehr sowie die fachkundigen Laienrichter Mag. Eva-Maria Düringer und Mag. Tino  Ricker in der Beschwerdesache Dirk Hironymus, Am See IV 25, 3071 Hinterholz, Österreich (vormals: RHO Pharma), vertreten  durch Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG, Alpstraße  23, 6890 Lustenau über die Beschwerde vom 05. Oktober 2016 gegen die Bescheide des  Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, Postfach 260, 1000 Wien) vom 12.  September 2016 betreffend Umsatzsteuer 2012, Bescheid über die Wiederaufnahme des  Verfahrens 2012 und vom 09. September 2016 betreffend Umsatzsteuer 2015 Steuernummer  63-114/3997  in Anwesenheit der Schriftführerin Isabella Längle zu Recht erkannt:     I. Die Beschwerde gegen die Wiederaufnahme des Verfahrens Umsatzsteuer 2012  wird als unbegründet abgewiesen.

**False Positives:**

- `Winkler` — partial — pred is substring of gold: `Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Treichl`(person)
- `Dr.  Roman Galehr`(person)
- `Mag. Eva-Maria Düringer`(person)
- `Mag. Tino  Ricker`(person)
- `Dirk Hironymus`(person)
- `Am See IV 25, 3071 Hinterholz, Österreich`(address)
- `RHO Pharma`(organisation)
- `Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG`(organisation)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt Österreich`(organisation)
- `63-114/3997`(tax_number)
- `Isabella Längle`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/144700.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144700.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Eugen Verstraaten, Lading 40, 4880 St. Georgen im Attergau, Österreich, vertreten durch Stb. über die Beschwerde vom  21. März 2024 gegen den Bescheid des Finanzamtes Österreich vom 1. März 2024 betreffend  Zahlungserleichterungen § 212 BAO 2024 zu Steuernummer 49-838/2256  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Eugen Verstraaten`(person)
- `Lading 40, 4880 St. Georgen im Attergau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `49-838/2256`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Dr. RgR Nepomuk Gillmeister (Beschwerdeführer, abgekürzt: Bf.), Kraygasse 26, 5134 Bruck im Holz, Österreich  vertreten  durch Steuerberaterin, AdresseSteuerberaterin, über die Beschwerde des Bf. vom 5. Mai 2022  gegen den Einkommensteuerbescheid 2020 des Finanzamtes Österreich vom 26. April 2022 zu  Steuernummer 08-648/8723  zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und der angefochtene Bescheid gemäß § 279  Abs. 1 BAO dahingehend abgeändert, dass die Einkommensteuer für das Jahr 2020 mit  2.663,00 € festgesetzt wird.

**False Positives:**

- `Steuerberaterin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag. Christian Seywald`(person)
- `Dr. RgR Nepomuk Gillmeister`(person)
- `Kraygasse 26, 5134 Bruck im Holz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `08-648/8723`(tax_number)

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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/147343.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147343.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Annika Streicher BA LL.M.(WU) in der  Beschwerdesache Dimitri Gaessner, Sauerbrunnberg 15, 8124 Neuhof, Österreich, vertreten durch Miriam Wurmehl, Bakk. phil., Windparkstraße 7, 5092 Gumping, Österreich, über die Beschwerde vom 13. Februar 2024 gegen den Bescheid des Finanzamtes  Österreich vom 16. Jänner 2024 betreffend Verspätungszuschlag / ESt 2020 Steuernummer  90-683/6114  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Miriam Wurmehl, Bakk. phil` — partial — pred is substring of gold: `Miriam Wurmehl, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Annika Streicher BA LL.M.(WU)`(person)
- `Dimitri Gaessner`(person)
- `Sauerbrunnberg 15, 8124 Neuhof, Österreich`(address)
- `Miriam Wurmehl, Bakk. phil.`(person)
- `Windparkstraße 7, 5092 Gumping, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `90-683/6114`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Piedro Klingebiel  in der Beschwerdesache 1. der  Tamara Gottschalch  und 2. der Heidemarie Egghart, beide in ***Bf1 und Bf2-Adr***, beide steuerlich vertreten  durch Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH, Schloßgraben 10,  6800 Feldkirch, über die Beschwerde vom 22.05.2018 gegen den Bescheid des Finanzamtes  Feldkirch vom 12. März 2018 betreffend Feststellungsbescheid Gruppenmitglied 2015  Tamara Gottschalch 22-144/9009  nach Durchführung einer mündlichen Verhandlung, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Allgäuer` — partial — pred is substring of gold: `Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Piedro Klingebiel`(person)
- `Tamara Gottschalch`(person)
- `Heidemarie Egghart`(person)
- `Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Tamara Gottschalch`(person)
- `22-144/9009`(tax_number)

</details>

---

## `role_anchor_name` 💣

**F1:** 0.001 | **Precision:** 0.027 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `ab1856a8`  
**Description:**
Matches names following role anchors like 'Richterin', 'Richter', etc., capturing the full name even without a title, ensuring it's not followed by a company or authority.

**Content:**
```
(?:Richterin|Richter|Vorsitzende|Vorsitzender|Beisitzer|Beisitzerin|Schriftführer|Schriftführerin|Anwalt|Anwältin|Steuerberater|Steuerberaterin|Geschäftsführer|Geschäftsführerin|Prokurist|Prokuristin|Leiter|Leiterin|Vertreter|Vertreterin)\s+(?:des\s+|der\s+|die\s+)?([A-ZÄÖÜ][a-zäöüß]+(?:\s+(?:von|van|de|zu|u\.\s*)?[A-ZÄÖÜ][a-zäöüß]+)*(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*)\s*(?:,|\n|$|\s+(?:Straß|Gasse|Platz|Weg|Allee|Nr\.|Haus|\d+|GmbH|AG|KG|Verein|Stiftung|Gesellschaft))(?!\s+(?:Finanzamt|Bundesfinanzgericht|Senat|Magistrat|Verwaltungsgericht|Oberlandesgericht|Landesgericht|Bezirksgericht|Bundesfinanzgerichtshof|Verwaltungsgerichtshof|Bundessozialgericht|Verfassungsgerichtshof|Bundesministerium|Landesregierung|Stadt|Gemeinde|Bezirk|Amt|Behörde|Wien|Graz|Linz|Salzburg|Innsbruck|Klagenfurt|Bregenz|Eisenstadt|St\.\s*Pölten|Steuerberatung|Rechtsanwälte|Wirtschaftsprüfung|Partnerschaft|&\s+Partner|\(|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.027 | 0.001 | 0.001 | 37 | 1 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 36 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_182`)


Im Antrag wurde ausgeführt, dass die  Geschäftsführung der A.-AG-FL von Herrn X. (Geschäftsführer der Madeleine Jahns, gleichzeitig auch  Geschäftsführer der B.-GmbH und Verwaltungsrat der A.-AG-FL) wahrgenommen und  Managementgebühren verrechnet werden sollten.

| Predicted | Gold |
|---|---|
| `Madeleine Jahns` | `Madeleine Jahns` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_61`)


Nach  übereinstimmender Lehre (Hofstätter/Reichel, Einkommensteuer Kommentar, Tz 6 zu § 17 EStG  1988), Verwaltungsübung (Rz 406 LStR 2002) und Entscheidungspraxis (zB BFG vom  23.05.2014, RV/6100146/2013) sind Vertreter Personen, die im Außendienst zum Zwecke der  Anbahnung und des Abschlusses von Kaufgeschäften und zur Kundenbetreuung tätig sind.

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_139`)


Danach sind  Vertreter Personen, die im Außendienst zum Zwecke der Anbahnung und des Abschlusses von  Geschäften und zur Kundenbetreuung tätig sind (VwGH 31.5.2017, Ro 2015/13/0009).

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_99`)


An diesem Standort betreibt er als  Geschäftsführer der Verwaldgart GmbH ein Hotel (Niederschrift v. 2.8.2010;

**False Positives:**

- `Verwaldgart` — partial — pred is substring of gold: `Verwaldgart GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaldgart GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

**False Positives:**

- `Starnberg Beratung` — partial — pred is substring of gold: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Albert Sengeisen`(person)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf`(organisation)
- `Starnberg Beratung GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

**False Positives:**

- `Firma Starnberg Beratung` — positional overlap with gold: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)
- `Albert Sengeisen`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_268`)


Konkret war seitens der Betriebsprüfung (wie auch schon bei früheren Amtshandlungen) der  Gesellschafter/Geschäftsführer Herr Albert Sengeisen, geboren 1970, als maßgebliche Person in der  Firma Starnberg Beratung GmbH wahrzunehmen.

**False Positives:**

- `Herr Albert Sengeisen` — partial — gold is substring of pred: `Albert Sengeisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albert Sengeisen`(person)
- `Starnberg Beratung GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_306`)


Im konkreten Fall handelt es sich bei Herrn Z4 um den anderen  Gesellschafter und Geschäftsführer der Firma Starnberg Beratung GmbH  Seine Parteilichkeit im Verfahren ist  anzunehmen, weshalb sein Beitrag zur Wahrheitsfindung als zweifelhaft zu werten ist.

**False Positives:**

- `Firma Starnberg Beratung` — positional overlap with gold: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_307`)


Überdies ist er als zweiter Geschäftsführer der Firma Starnberg Beratung GmbH sowieso in das  Abgabenverfahren involviert, weil für das Gebaren der Gesellschaft mitverantwortlich.

**False Positives:**

- `Firma Starnberg Beratung` — positional overlap with gold: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_18`)


Im Rahmen der Schlussbesprechung wurde ein  weiterer Vertrag betreffend Bierlieferungen vorgelegt, datiert mit 9.1.2008 und unterzeichnet  vom damaligen Geschäftsführer der Schilift GmbH, [dem Beschwerdeführer].

**False Positives:**

- `Schilift` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_69`)


Der Beschwerdeführer erhielt keinerlei Entlohnung aus seiner Tätigkeit als Geschäftsführer der  Schilift GmbH. Dies ist unstrittig (vgl. das Beschwerdevorbringen und die Angaben des  Beschwerdeführers im Schreiben an das Bundesfinanzgericht vom 8.2.2021).

**False Positives:**

- `Schilift` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_70`)


Der Beschwerdeführer unterfertigte am 9.1.2008 als Geschäftsführer der Schilift GmbH ein  Bierlieferungsübereinkommen mit der Traun-Handel AG  Gleichzeitig unterfertigte er eine „unwiderrufliche  Garantie, dass der Vertragspartner sämtliche Verpflichtungen aus dem Übereinkommen  ordnungsgemäß erfüllt. Ich … verpflichte mich … über erste schriftliche Aufforderung die  Verpflichtungen des Vertragspartners mit ihm zur ungeteilten Hand zu erfüllen …“.

**False Positives:**

- `Schilift` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traun-Handel AG`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_87`)


Es  findet sich auch kein Hinweis darauf, dass die diese beiden Ausgabenpositionen in  Zusammenhang mit der Stellung des Beschwerdeführers als Geschäftsführer der Schilift GmbH  gestanden hätten.

**False Positives:**

- `Schilift` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_106`)


Der Beschwerdeführer war zum Zeitpunkt der Abgabe der Garantieerklärung gegenüber der Traun-Handel AG Gesellschafter und Geschäftsführer der Schilift GmbH, weshalb die Ausgaben im  Zusammenhang mit der Haftungsinanspruchnahme durch die Traun-Handel AG seiner  Gesellschafterstellung zuzuordnen sind.

**False Positives:**

- `Schilift` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traun-Handel AG`(organisation)
- `Traun-Handel AG`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_168`)


Gegen die erlassenen Bescheide erhob die Bf. durch ihre steuerliche Vertreterin Beschwerde,  stellte den Antrag von der Erlassung einer Beschwerdevorentscheidung abzusehen und die  Entscheidungsfindung durch den Senat unter Anberaumung einer mündlichen Verhandlung  und führte u.a. aus:  12 von 59 Seite 13 von 59

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133681.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133681.1_288`)


Mit Schreiben vom 27. August 2020 entgegnete der steuerliche Vertreter des  Beschwerdeführers, dass die belangte Behörde, in ihrer E-Mail vom 21.07.2020 unter anderem  auf zwei vom Beschwerdeführer eingebrachte Beweismittel im Zusammenhang mit der  Nachweisführung des wirtschaftlichen Eigentums zugunsten des Bruders des  Beschwerdeführers verweise.

**False Positives:**

- `Beschwerdeführers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_235`)


5. Zum Vorwurf des Anrufs der steuerlichen Vertreterin beim Finanzamt  Nach der „Belehrung" und auf Basis der unklaren und schwammigen rechtlichen  Rahmenbedingungen kam der steuerlichen Vertreterin die Idee, ob man nicht den  Vorsteuerabzug sicherstellen könnte, wenn die Umsatzsteuer direkt auf das Abgabenkonto des  Lieferanten überwiesen werden würde (in Anlehnung an den Baubereich).

**False Positives:**

- `Idee` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_234`)


Fazit: Die Ansicht (NiS. 2.6.Kämpker&Mooslechner Holz GmbHS. 6 -9), nur beratende Tätigkeiten der Strategen im  Namen der OG beruhten auf dem Managementvertrag , und die lenkenden und  überwachenden , dh geschäftsführenden Tätigkeiten der Strategen seien nicht auf Grund des  Managementvertrages erfolgt und auch nicht auf der Grundlage des Managementvertrages  oder sonstwie abgegolten worden, ist nicht überzeugend, weil   -der StB selbst die Lenkungs- und Überwachungstätigkeiten der Strategen im Zusammenhang  mit den Managementverträgen erwähnt hat (Schreiben des Steuerberaters vom 22.9.2016),  - weil man die Tätigkeiten der Strategen, die dem Konzern, bestehend aus den  Konzerngesellschaften, gedient haben (Lenkungs- Überwachungstätigkeiten, sonstige  unterstützende Tätigkeiten wie z.B. Beratungen lt. Vorlageantrag S. 3-5, lt. Schreiben des   Steuerberaters vom 22.9.2016, lt Unilemder-Versand GmbH2.6.2021, S. 7 und lt. Gesellschafter- Geschäftsführer Steblein Wind GmbH2.6. S. 11 und 12) nicht trennen kann.

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `2.6.Kämpker&Mooslechner Holz GmbHS.`(organisation)
- `Unilemder-Versand GmbH2.6.2021`(organisation)
- `Steblein Wind GmbH2.6.`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_302`)


Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 5, 11 und  12).

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_304`)


Die Fremdgeschäftsführer sollten zu Motivationszwecken mittelfristig auch eine  Beteiligung an der jeweiligen Tochtergesellschaft der Holding, für die sie tätig waren, erlangen  können (Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 11;

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_311`)


Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 5, 11 und 12).

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_316`)


Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6.2021, S. 5, 11 und 12).  ee.)

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_321`)


Bis jetzt hat diese im Jahr 2004 durch die drei Strategen einvernehmlich erdachte Planung  erfolgreich umgesetzt werden können; der Gesamtumsatz des Konzerns, bestehend aus den  oben erwähnten Konzerngesellschaften, hat sich in den letzten 15 Jahren vervielfacht  (Gesellschafter-Geschäftsführer Steblein Wind GmbH2.6., S. 11).

**False Positives:**

- `Steblein Wind` — partial — pred is substring of gold: `Steblein Wind GmbH2.6.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_481`)


Im Ergebnis machte es somit auch bei wirtschaftlicher und nicht nur bei rechtlicher  Betrachtung einen Unterschied, dass im Zusammenhang mit der Lenkung und Überwachung  der Rusnok IT GmbH die OG, vertreten durch die beiden Strategen und nicht nur der erste Stratege als  Gesellschafter-Geschäftsführer der Bf, tätig geworden ist.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rusnok IT GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_81`)


Danach sind Vertreter Personen, die im Außendienst zum  Zwecke der Anbahnung und des Abschlusses von Geschäften und zur Kundenbetreuung tätig  sind (vgl. VwGH 31.5.2017, Ro 2015/13/0009).

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/135937.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135937.1_91`)


Nach Information des Rechtsvertreters durch die Vorsitzende des Senates, dass die Abhaltung  der mündlichen Verhandlung vor dem Senat aus zeitlichen und organisatorischen Gründen  nicht in Feldkirch stattfinden könne, zog der Vertreter den Antrag auf Durchführung einer  mündlichen Verhandlung mit E-Mail vom 21.02.2022 zurück.

**False Positives:**

- `Senates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_26`)


Mit Verfügung des GV-Ausschusses vom 30.06.2021 wurden unter anderem die  gegenständlichen Beschwerden nach Pensionierung der dafür zuständigen Richterin der  Gerichtsabteilung 7022 abgenommen und in weiterer Folge mit Wirkung vom 05.07.2021 der  nunmehr zuständigen Gerichtsabteilung neu zugeteilt.  II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Das BFG legt seiner Entscheidung den im Folgenden dargestellten Sachverhalt zugrunde, der  sich aus dem Vorbringen der Verfahrensparteien im Beschwerdeverfahren und den  vorgelegten Verwaltungsakten ergibt.

**False Positives:**

- `Gerichtsabteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `BFG`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_38`)


Mit dem Pensionsantritt der Leiterin der Gerichtsabteilung 7022 und der in der  Folge nicht erfolgten Nachbesetzung liegt eine solche Verhinderung vor, durch die  Neuzuteilung wurde mit 05.07.2021 die nunmehr zuständige Gerichtsabteilung zur  Entscheidung zuständig gemacht.

**False Positives:**

- `Gerichtsabteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_285`)


Dafür sind- in Fällen , in welchen wie hier noch keinerlei Ermittlungen durchgeführt worden  sind,  Betriebsprüfer für internationale Beziehungen besser geeignet als Richter des  Bundesfinanzgerichtes, weil diese Betriebsprüfer größere Erfahrung im Auffinden  internationaler Wirtschaftsdaten haben.

**False Positives:**

- `Bundesfinanzgerichtes` — type mismatch — same span as gold: `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_32`)


Es gab keine ausdrückliche  oder konkludente Vereinbarung mit Ihrem Gatten als Geschäftsführer des Unternehmens, dass  diese Nutzung eines Firmenfahrzeugs als Teil Ihrer Entlohnung für die Tätigkeit als  Rezeptionistin zu sehen ist.

**False Positives:**

- `Unternehmens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/144990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144990.1_30`)


Herr Gf ist darüber hinaus  alleiniger Gesellschafter-Geschäftsführer der Carrasco Software GmbH  der 100%-igen Muttergesellschaft der  Bf.

**False Positives:**

- `Carrasco Software` — partial — pred is substring of gold: `Carrasco Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Carrasco Software GmbH`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/145821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145821.1_28`)


Mit Schreiben vom 20. August 2024 ersuchte der zuständige Richter die Bf, ihre aktuelle  wirtschaftliche Situation – beispielsweise anhand eines Vermögensverzeichnisses –   glaubwürdig darzulegen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_15`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf. war als selbständige Gesellschafter-Geschäftsführerin der Berg Norwerk Holding GmbH  tätig und  hat aus dieser Tätigkeit Einkünfte aus selbständiger Arbeit gemäß § 22 EStG 1988 bezogen.

**False Positives:**

- `Berg Norwerk Holding` — partial — pred is substring of gold: `Berg Norwerk Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Berg Norwerk Holding GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_49`)


Im beschwerdegegenständlichen Fall liegt nach Ansicht des Bundesfinanzgerichtes aber ein  anderer Sachverhalt vor:  Die Bf. war als selbständige Gesellschafter-Geschäftsführerin der Berg Norwerk Holding GmbH  tätig und  hat aus dieser Tätigkeit Einkünfte aus selbständiger Arbeit gemäß § 22 EStG 1988 bezogen.

**False Positives:**

- `Berg Norwerk Holding` — partial — pred is substring of gold: `Berg Norwerk Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Berg Norwerk Holding GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dieter Brennscheid, Bakk. rer. nat. in der Beschwerdesache Ines Gora,  Thunhausweg 19, 8311 Wetzawinkel, Österreich, über die Beschwerde vom 30. September 2016 gegen die Bescheide des  Finanzamtes Österreich vom 12. Juli 2016 betreff a) Umsatzsteuer für die Jahre 2011 bis 2015,  b) Festsetzung von ersten Säumniszuschlägen vom 09.08.2016,  c) Festsetzung von  Stundungszinsen vom 09.09.2016, Steuernummer 68-68-ZZZZZ (ehemals  18-383/0472 )  nach Durchführung einer mündlichen Verhandlung am 26.11.2024 zu Recht erkannt:      I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2011 bis 2015 wird gemäß        § 279 BAO Folge gegeben.

**False Positives:**

- `Dieter Brennscheid` — partial — pred is substring of gold: `Dieter Brennscheid, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dieter Brennscheid, Bakk. rer. nat.`(person)
- `Ines Gora`(person)
- `Thunhausweg 19, 8311 Wetzawinkel, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `18-383/0472`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/147920.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147920.1_66`)


Demnach sind Vertreter Personen, die im Außendienst zum Zwecke der  Anbahnung und des Abschlusses von Geschäften und zur Kundenbetreuung tätig sind (VwGH  28.6.2012, 2008/15/0231).

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/149672.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149672.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Verwaltungsstrafsache  gegen Oswald Küstler, Doppel Straße 1543, 8421 Zehensdorf, Österreich, wegen der Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom  20. August 2025 gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 7. August 2025, Zahl: MA67/MA-GZ/2025, in der mündlichen  Verhandlung am 24. Oktober 2025, im Beisein der Schriftführerin Nicole Schmid, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z. 2. VStG eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

**False Positives:**

- `Nicole Schmid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Oswald Küstler`(person)
- `Doppel Straße 1543, 8421 Zehensdorf, Österreich`(address)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

</details>

---

## `initial_only_name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `48c10b1f`  
**Description:**
Matches initial-only names (e.g., 'M.M.A.', 'M.') in contexts where a person is referenced but no full name is given.

**Content:**
```
(?:von|des|der|die)\s+([A-Z]\.[A-Z]\.[A-Z]\.|[A-Z]\.)\s*(?:,|\n|$|\s+(?:Straß|Gasse|Platz|Weg|Allee|Nr\.|Haus|\d+|GmbH|AG|KG|Verein|Stiftung|Gesellschaft))(?!\s+(?:Finanzamt|Bundesfinanzgericht|Senat|Magistrat|Verwaltungsgericht|Oberlandesgericht|Landesgericht|Bezirksgericht|Bundesfinanzgerichtshof|Verwaltungsgerichtshof|Bundessozialgericht|Verfassungsgerichtshof|Bundesministerium|Landesregierung|Stadt|Gemeinde|Bezirk|Amt|Behörde|Wien|Graz|Linz|Salzburg|Innsbruck|Klagenfurt|Bregenz|Eisenstadt|St\.\s*Pölten|Steuerberatung|Rechtsanwälte|Wirtschaftsprüfung|Partnerschaft|&\s+Partner|\(|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_533`)


2. Bei Anwendung von Abs. 3a wird die Beförderung oder Versendung abweichend von Z. 1 der  Lieferung durch den Unternehmer gemäß Abs. 3a Z. 1 bzw. 2 zugeordnet.

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_157`)


Empfänger waren die  Vertragspartner der D., für die die D. die Veranstaltungen geplant und durchgeführt hat.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_217`)


Das Vorbringen der Bf., wonach sich ihr Sohn vom Februar 2017 bis zum erneuten Termin im  Herbst 2017 sehr intensiv vorbereitet habe, ist jedenfalls genauso wenig ausreichend, um von  einer ernsthaft und zielstrebig betriebenen Ausbildung auszugehen wie die von ihr vorgelegte  Bestätigung des Z., wonach dieser mit ihrem Sohn von Dezember 2017 bis Jänner 2018  gemeinsam für die Matura gelernt hat.

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `standalone_name_after_role` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5d88465d`  
**Description:**
Matches names that appear immediately after a role anchor (e.g., 'Richterin', 'Richter') without a title, capturing the full name.

**Content:**
```
(?:Richterin|Richter|Vorsitzende|Vorsitzender|Beisitzer|Beisitzerin|Schriftführer|Schriftführerin|Anwalt|Anwältin|Steuerberater|Steuerberaterin|Geschäftsführer|Geschäftsführerin|Prokurist|Prokuristin|Leiter|Leiterin|Vertreter|Vertreterin)\s+([A-ZÄÖÜ][a-zäöüß]+(?:\s+(?:von|van|de|zu|u\.\s*)?[A-ZÄÖÜ][a-zäöüß]+)*(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*)\s*(?:,|\n|$|\s+(?:Straß|Gasse|Platz|Weg|Allee|Nr\.|Haus|\d+|GmbH|AG|KG|Verein|Stiftung|Gesellschaft))
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

</details>

---

<details>
<summary>❌ False Negatives (943, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/143870.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143870.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 27. April 2022 des Beschwerdeführers **Clemens Tetzlaw**, Goldbiegelgasse 217, 9854 Koschach, Österreich  Steuernummer:  11-569/6335, gegen den Bescheid des Finanzamtes Österreich vom 5. April 2022  betreffend Einkommensteuer 2021 zu Recht:    I)  Der Beschwerde wird gem. § 279 BAO teilweise Folge gegeben.

- missed: `Clemens Tetzlaw` (person)
- predicted in sentence: `Mag. Günter Narat`

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)

Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma **M.** Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

- missed: `M.` (person)
- predicted in sentence: `Albert Sengeisen`

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf.) ist die Komplementärin **Charles Rybalka**  in einer GmbH & Co. KG.

- missed: `Charles Rybalka` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_214`)

Der Mieter der 2. Wohnung       sei die Schwiegermutter des **M.M.A.** ab August 2012 bis Mitte 2014 gewesen.

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut`, `Lee Kubbig`

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  **Dipl. Kfm. Ing. Ing. Jonas Thumberger**, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dipl. Kfm. Ing. Ing. Jonas Thumberger` (person)
- predicted in sentence: `Mag. Karin Pitzer`, `Ing. Ing. Jonas Thumberger`

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_46`)

Da das Beschwerdeverfahren gegen Frau A B als Geschäftsführerin der Saskia Sinnwell  und somit  als Entscheidungsträgerin iSd § 3 Abs. 2 VbVG kein rechtswidriges oder schuldhaftes Verhalten  ergeben hat, liegen die Voraussetzungen für die Verhängung einer Geldbuße über die  **Saskia Sinnwell**  als belangten Verband nicht vor.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Andrea Müller-Dobler MBA MSc** in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

- missed: `Mag. Andrea Müller-Dobler MBA MSc` (person)
- predicted in sentence: `Mag. Andrea Müller`, `Dr. Adam Müller`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_163`)

M.M.A. und dessen Frau **M.M.B.** nur sehr ungenau abgesprochen.

- missed: `M.M.B.` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_94`)

Eingangs ist - zumal die **Leroy Kusznierz**  per xx.xx.2020 endete - die Frage der Rechtsnachfolge zu  klären: Kraft der ausdrücklichen gesetzlichen Anordnung des § 191 Abs. 2 BAO – als lex  specialis zur im § 19 Abs. 1 BAO normierten Gesamtrechtsnachfolge – haben  Feststellungsbescheide nach Beendigung einer Personenvereinigung (Personengemeinschaft)  an die Personen, denen gemeinschaftliche Einkünfte zugeflossen sind, zu ergehen.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_190`)

Zu Vitamin B verwies  sie auf die Verschreibung von Neurobin durch **Fr.Dipl.-Ing. Joseph Szwarz** Dieses enthalte so viele andere  Zusatzstoffe.

- missed: `Fr.Dipl.-Ing. Joseph Szwarz` (person)
- predicted in sentence: `Dipl.-Ing. Joseph Szwarz Dieses`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_207`)

3) Die besonders luxuriöse Wohnausstattung in Top 1 sei nach Wünschen und Vorstellungen       des Mieters **M.M.A.** [z.B. Bezahlung der Bf. an Kosten für a) Küche und Esszimmer       (90.664,40 € netto) an die Tischlerei U., b) einen "Specksteinofen" (18.200 € netto)].

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_61`)

Am 27.4.2020 stellte die mit Gesellschaftsvertrag vom xx.xx.xxxx gegründete YY (FN xxxx) mit  dem Sitz ebenfalls an der zuletzt genannten Anschrift den Antrag, die Änderung der Firma der  Rechtsvorgängerin der Bf. („XX“) auf jene der Bf. („**Jeffrey Stubenrauch**“) vorzunehmen, da durch den  Beitritt weiterer Gesellschafter als Kommanditisten und dem Wechsel des Komplementärs der  Gesellschaftsvertrag per 22.4.2020 neu gefasst worden sei.

- missed: `Jeffrey Stubenrauch` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_140`)

Da zudem - wie bereits dargelegt - die Stellungnahme des **Dr. F**  nunmehr in die Begutachtung miteinbezogen wurde, die Gutachterin aber dennoch in  Bestätigung der Vorgutachten zum selben Ergebnis gelangt ist, kann nach dem Vorgesagten  insgesamt nicht davon gesprochen werden, dass den Gutachten mehrere Mängel anhaften  würden bzw. ist jedenfalls davon auszugehen, dass diese allfälligen Mängel mittlerweile  behoben sind.

- missed: `Dr. F` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_50`)

Mit Vertrag vom Datum nahm die Leroy Kusznierz  als Geschäftsherrin die **Jeffrey Marinopoulos** (FN xxxxxx) als  atypisch stille Gesellschafterin mit einer Einlage von insgesamt Euro Betrag auf, wobei das  Gesellschaftsverhältnis auf Grundlage des Artikels IV Umgründungssteuergesetz vereinbart  worden war.

- missed: `Jeffrey Marinopoulos` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_17`)

… Während **Fabios** Osterferien entfällt im Übrigen das Regelkontaktrecht zu beiden Kindern.

- missed: `Fabios` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_9`)

Mit Beschwerdevorentscheidung vom 05.11.2015, gerichtet an die **Jeremias Kierstan**, zu Handen  Herrn Vertreter, wurde die Beschwerde als unbegründet abgewiesen, wobei die belangte  Behörde davon ausging, dass die Beschwerde von der Jeremias Kierstan, erhoben worden sei.

- missed: `Jeremias Kierstan` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und **Dr  Heinrich Vana,** über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

- missed: `Dr  Heinrich Vana,` (person)
- predicted in sentence: `Kelderber Beratung Technologien`, `Dr Vana Dr Kolbitsch Mag Breitenecker`

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Silvia Gebhart** in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

- missed: `Silvia Gebhart` (person)
- predicted in sentence: `Kelderber Beratung Technologien`, `Dr Vana Dr Kolbitsch Mag Breitenecker`

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_61`)

sowie die atypisch stille Gesellschaft aufgeteilt.  Am Datum wurde die Verlegung des Sitzes der **Leroy Kusznierz**  in die politische Gemeinde Ort3 - der  zumindest bis ins Jahr 2016 dort beibehalten wurde - im Firmenbuch eingetragen.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_12`)

Diese Rechnung (die USt ausweisend, Beilage 3 zum Protokoll) vom 12.6.2019 wurde ihr vom  Steuerberater am 20.6.2019 wiederum per Email (Beilage 2 zum Protokoll) übermittelt.  Der Kaufvertrag wurde am 17.6.2019 unterfertigt, wobei der Käufer die Vorsteuer auf das  Abgabenkonto der **Saskia Sinnwell**  überrechnen hätte sollen und diese wiederum als USt abgeführt  hätte werden sollen.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_119`)

Nach weiteren Ausführungen von **Ida Katenstroth** sei Sinn und Zweck des fiktiven  innergemeinschaftlichen Erwerbes gem.  Art. 3 Abs. 8 UStG zweiter Satz sicherzustellen, dass  ein innergemeinschaftlicher Erwerb im Bestimmungsland beim Enderwerber der  Mehrwertsteuer unterliegt und gleichzeitig zu verhindern, dass dieser Umsatz doppelt  besteuert wird (vgl. EuGH Bühler, C-580/16, Rn 50 mit Verweis auf EuGH-Urteil X and Facet C- 536/08 und C-539/08).

- missed: `Ida Katenstroth` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/139845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139845.1_14`)

Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens, der  aktenkundigen Unterlagen, des Vorbringens der Parteien sowie der schriftlich eingeholten  Zeugenaussage von Dipl. Kff. Sara Füßgen  folgenden entscheidungswesentlichen Sachverhalt fest:  Der Bf. und **Dipl. Kff. Sara Füßgen**  waren bis 13.01.2014 verheiratet.

- missed: `Dipl. Kff. Sara Füßgen` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_9`)

Über Lenkererhebung vom 7. August 2023 teilte die Zulassungsbesitzerin des Fahrzeuges, A.  **M.**, der Behörde mit, dass das Fahrzeug zur Beanstandungszeit Desiree Hannecken (Beschwerdeführer,  kurz: Bf.) überlassen gewesen sei.

- missed: `M.` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_37`)

II. Das Bundesfinanzgericht hat erwogen:  Sachverhalt:  Die Beschwerdeführerin (Bf.) ist die Komplementärin **Charles Rybalka**  in einer GmbH & Co. KG.

- missed: `Charles Rybalka` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_81`)

Folglich kann aufgrund des Innehabens eines Wohnsitzes in Österreich,  wenn das Unternehmen im Ausland betrieben wird, gemäß § 6 Abs. 1 Z 27 UStG 19954 nicht  angewendet werden (vgl. EuGH 26.10.2010, Rs C-97/09, **Schmelz** und EuGH 6.10.2011,   C-421/10, Stoppelkamp).“  4. Die unionsrechtlichen Grundlagen für die Kleiununternehmerregelung findet sich in der  Richtlinie 206/112/EG des Rates über das gemeinsame Mehrwertsteuersystem  (Mehrwertsteuer-Richtlinie):  Nach Art. 272 Abs. 1 Buchst.

- missed: `Schmelz` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_204`)

Der Einschreiter **Evelyn Antwerber**  ist handelsrechtlicher Geschäftsführer der Firma1.

- missed: `Evelyn Antwerber` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_25`)

Seit 2023 wurde die Kanzlei von Mag. Roland Schmidt, **Kerstin Graf MSc (WU)**  und Isabella Hauer MA gemeinsam als Partner fortgeführt.

- missed: `Kerstin Graf MSc (WU)` (person)
- predicted in sentence: `Mag. Roland Schmidt`

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_3`)

Entscheidungsgründe  I. Verfahrensgang  Die **Gustav Franzki** (Beschwerdeführerin, Bf.) ist im Bereich der Stromerzeugung aus erneuerbaren  Energien, insbesondere der Windenergie, tätig.

- missed: `Gustav Franzki` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_96`)

Dazu wurden ein Curriculum vitae (CV) sowie eine Teilnahmebestätigung an einer  Fortbildungsveranstaltung 2020 vorgelegt, bei welcher ua. das DDX3X-Syndrom seitens **Prof.  XX** (USA) behandelt wurde.

- missed: `Prof.  XX` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Mag. Anna Mechtler-Höger** in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Mag. Anna Mechtler-Höger` (person)
- predicted in sentence: `Mag. Anna Mechtler`, `Jeremias Kierstan`, `Peter Schabel`

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_22`)

In der dagegen fristgerecht am eingebrachten Beschwerde des Amtsbeauftragten vom  3. Dezember 2020 wird wie folgt ausgeführt:  Angefochten werde die Einstellung gem. § 136 FinStrG hinsichtlich der Geschäftsführerin A B,  Adresse1, sowie des belangten Verbandes die Saskia Sinnwell, Franz-Michel-Willam-Weg 31, 3580 Groß Burgstall, Österreich  mit folgendem  Inhalt:  „Die Grundlage des Verfahrens bildet die Betriebsprüfung vom 09.10.2019 bei der **Saskia Sinnwell**,  bei welcher festgestellt wurde, dass ein Liegenschaftsverkauf im Juni 2019 nicht in der UVA  gemeldet wurde.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_177`)

Mit Beschwerdevorentscheidung vom 06.09.2021 verweise die belangte Behörde auf die  beiden fachärztlichen Gutachten des Bundesamtes für Soziales und Behindertenwesen vom  8. Juli 2020 und vom 6. November 2021, laut derer der Grad der Behinderung für **M. F.** 30 % ab  dem 01.11.2019 betrage und keine dauernde Erwerbsunfähigkeit vorliege.

- missed: `M. F.` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_15`)

In den restlichen Wochen der Sommerferien entfällt sein  Regelkontaktrecht zu S.. Der Vater ist berechtigt, Adrian gemeinsam mit S. in der zweiten  Woche von **Fabios** Sommerferien durchgehend zu betreuen.

- missed: `Fabios` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_169`)

2.)Gründung der bf **Jeremias Stuck** (Firmenbuchauszug Rusnok IT GmbH  Die Rusnok IT GmbH wurde am 4.8.2005 gegründet.

- missed: `Jeremias Stuck` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_559`)

Am Beleg scheint nur beim 23.5. der Zusatz „**Dr. S** 19.6.13“ auf.

- missed: `Dr. S` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_25`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Zum gegenständlichen und zu den gleichgelagerten Verfahren  Seit dem Frühjahr 2024 langten beim Bundesfinanzgericht im Wesentlichen gleichlautende  Beschwerden von über **Pjotr Gerisch**  betreffend die Stabilitätsabgabe ein.

- missed: `Pjotr Gerisch` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_10`)

Mit Schreiben vom 28.11.2016 legte die Beschwerdeführerin, eine beim AG GmbH angestellte  Anzeigenverkäuferin, eine Bestätigung ihres Dienstgebers vor, mit dem folgenden Wortlaut:   "Betreff: Bestätigung: Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung zu § 17 Abs 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau **Hainig** überwiegend  ihre Tätigkeit, als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom 01.01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

- missed: `Hainig` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_515`)

Im gegenständlichen Fall war das Mietverhältnis zwischen der Bf. als Vermieter und **M.M.A.** als  Mieter bzw. M.M.B. als Mieterin hinsichtlich der Miethöhe oder den sonstigen Konditionen des  Mietvertrages so gestaltet, wie es unter Fremden gestaltet worden wäre.

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_531`)

Seitens des Bf. wurde von Hr.  **Dr. B** keine Verordnung für die Einnahme von einem „MMS Mineralpräparat“ vorgelegt.

- missed: `Dr. B` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_34`)

Mit Lenkerauskunft des rechtsfreundlichen Vertreters der Zulassungsbesitzerin vom  1) 12.05.2020, 2) bis 5) 26.03.2020 und 6) 20.03.2020 wurde mitgeteilt, dass Verantwortlicher  für das Taxi- und Mietwagengewerbe Herr **Russbüldt**  geb. Herrgeb, AdrHerr, sei.

- missed: `Russbüldt` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_48`)

An Unterlagen wurden nochmals die Aufstellung Diagnosen **Dr. D**, der Zytogenetische Befund  v. 24.11.2022 sowie der Molekulargenetische Befund v. 27.3.2023 beigebracht.

- missed: `Dr. D` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_22`)

**A.B.** begann im WS 18/19 mit dem Bachelorstudium Commerce and Marketing und bestand  am 27. Jänner 2021 die Diplomprüfung an der Budapest Metropolitan Egyetem (BA/BSc).

- missed: `A.B.` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_148`)

Die **M.** sei verantwortlich für die Lagerung und Inventar aller Rohmaterialien  und Produkte, die im Eigentum der Bf. seien.

- missed: `M.` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_4`)

Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde  vom , Strafnummer 2019, SpS 2000, wurde das gegen   1) A B, Russland, derzeit in Karenz, wohnhaft Adresse1, und   2) **Saskia Sinnwell**, Wien;

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_537`)

Hinsichtlich der Überlassung der Wohneinheit Top 1 dem Gesellschafter der Bf. - **M.M.A.** –  bzw. Top 3 der Ehegattin des M.M.A. - M.M.B. - jeweils gegen Entgelt liegt Missbrauch im  Bereich der Umsatzsteuer nicht schon dann vor, wenn die Nutzung durch den Mieter selbst bei  ihm nicht zu einem Vorsteuerabzug geführt hat (vgl. VwGH 16.03.2022, Ra 2019/13/0090).

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_3`)

Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin, die **Ludmilla Hühnerfuß, Bakk. techn.** (im Folgenden Bf.) ist ein rumänisches  Transportunternehmen, das im Streitjahr 2018 Anträge auf Vorsteuererstattungen eingereicht  hat.

- missed: `Ludmilla Hühnerfuß, Bakk. techn.` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_57`)

Im weiters im Veranlagungsakt erliegenden von  der vormaligen steuerlichen Vertretung der **Leroy Kusznierz**  ausgefüllten Formular „Verf 60“  werden für das strittige Veranlagungsjahr neben dem Erst- und der ZweitBf.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_93`)

**Dr.in Dok3**, Fachgebiet: Ärztin für Allgemein-medizin, erstellte am 31. Jänner 2022 folgendes  Aktengutachten:  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Mag. W. klinische und Gesundheitspsychologin allgemein beeidigte und gerichtlich zertifizierte  Sachverständige klinisch psychologisches Privatgutachten vom 5.10.2021  Es liegt eine Asperger-Autismus-Störung vor, die zum Teil widersprüchlichen Ergebnisse,  insbesondere die Selbstbeurteilung des Mj sowie einige seiner Leistungstestergebnisse, welche  deutlich besser ausgefallen sind als es bei einer Person mit Asperger-Autismus zu erwarten  gewesen wäre, lässt sich dahingehend klären, dass der Mj wahrscheinlich auch mitbedingt  durch seine hohe Intelligenz-sich über Jahre hinweg sehr vielen sozialen Kompetenzen kognitiv  erschlossen hat und somit auf heuristischer Basis agieren kann sofern er das vorliegende soziale  Muster schnell und unbeeinträchtigt von Störvariablen erkennt.

- missed: `Dr.in Dok3` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_75`)

Es kann hingegen nicht festgestellt werden, ob der Gesellschaftsvertrag über die atypisch stille  Beteiligung der **Jeffrey Marinopoulos**  vom Datum an der Leroy Kusznierz  bis dato aufgelöst wurde.

- missed: `Jeffrey Marinopoulos` (person)
- predicted in sentence: —

</details>

---

