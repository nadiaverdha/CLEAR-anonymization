# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-17T15:23:34.207478

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-17_v3/config.yaml 
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
| Accuracy (exact match) | 98.6% |
| True Positives | 680 |
| False Positives | 306 |
| False Negatives | 934 |
| Total Gold Entities | 1614 |
| Micro Precision | 69.0% |
| Micro Recall | 42.1% |
| Micro F1 | 52.3% |
| Macro F1 | 52.3% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Names after 'durch' (Judge/Representative)` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Names after 'Frau' or 'Herr' (Accusative/Dative)` | 3.6% | 96.8% | 1.9% | 31 | 30 | 1 |
| `Names after 'in der Beschwerdesache' context` | 22.8% | 92.1% | 13.0% | 228 | 210 | 18 |
| `Names after 'von' (Family/Relation Context)` | 2.0% | 88.9% | 1.0% | 18 | 16 | 2 |
| `Names after 'Beschwerde des' (Genitive)` | 2.8% | 88.5% | 1.4% | 26 | 23 | 3 |
| `Names with Split Titles (e.g. Univ- Prof.)` | 32.2% | 70.9% | 20.8% | 474 | 336 | 138 |
| `Single Word Names after 'Herrn' or 'Frau'` | 4.5% | 60.3% | 2.4% | 63 | 38 | 25 |
| `Names with 'VetR' and similar standalone titles` | 2.8% | 46.0% | 1.4% | 50 | 23 | 27 |
| `Names after 'von' (General Context)` | 0.2% | 33.3% | 0.1% | 6 | 2 | 4 |
| `Names after 'Bf,' (Comma separated)` | 0.1% | 1.2% | 0.1% | 82 | 1 | 81 |
| `Names after 'von' (Befunden/Gutachten)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after 'Arbeitsplatz des' (Contextual)` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `Names after 'Herrn' or 'Frau' (Accusative/Dative)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Names after 'durch' (Judge/Representative)` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `d7c5313e`  
**Description:**
Captures the name following 'durch den Richter' or 'durch die Richterin', handling split titles and ensuring full name capture.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin)\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn\s+R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Alexander Schnelldorfer` | `Alexander Schnelldorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

</details>

---

## `Names after 'Frau' or 'Herr' (Accusative/Dative)` 🏆

**F1:** 0.036 | **Precision:** 0.968 | **Recall:** 0.019  

**Format:** `regex`  
**Rule ID:** `7078c2ee`  
**Description:**
Captures full title and name following 'Herrn' or 'Frau', ensuring the name includes at least a first and last name (or title + first + last) to avoid partial matches.

**Content:**
```
(?:Herrn|Frau)\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.968 | 0.019 | 0.036 | 31 | 30 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 30 | 1 | 1584 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_36`)


Im Ermittlungsverfahren wurde bekannt gegeben, dass das Fahrzeug Herrn Vera Schliephacke  überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `Mag. Peter  Mayerhofer` (person)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

| Predicted | Gold |
|---|---|
| `Dimitri Witkoski` | `Dimitri Witkoski` |

**Missed by this rule (FN):**

- `Ruckelshaußen` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Mag. Wolfgang Moser` (person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

| Predicted | Gold |
|---|---|
| `Franziska Fitzmann` | `Franziska Fitzmann` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_17`)


Im Gegenteil war es so, daß  die Touristik Werkvalbach GmbH die fälligen Gebäudemieten, welche an Herrn Jeanne Kraenzlin  zu zahlen gewesen  wären, nicht bedienen konnte.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Missed by this rule (FN):**

- `Touristik Werkvalbach GmbH` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_54`)


Der Verzicht wurde somit vom steuerlichen  Vertreter - auch im Namen von Herrn Jeanne Kraenzlin - abgegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_32`)


Im Bescheid II vom 20.2.2019 wurde für Herrn Quentin Schwartkopp, Adresse_Bf., gemäß § 8 Abs. 1 Z 2  AlkStG iVm. § 201 Abs. 1 und Abs. 2 Z 3 der Bundesabgabenordnung (BAO) die Alkoholsteuer  für 2016 in Höhe von € 280,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

| Predicted | Gold |
|---|---|
| `Dominik Barfusz` | `Dominik Barfusz` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Groschedl über die  Beschwerde von Frau Theodora Berenwinkel, Klam 26, 8673 Steinhöf, Österreich, vom 12. Februar 2024, gegen die zwei  Straferkenntnisse der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67,  als Abgabenstrafbehörde (beide) vom 30. Jänner 2024, GZen 1) MA67/GZ1/2023 und 2)  MA67/GZ2/2023, beide wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für Wien Nr.  9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 40,00 Euro auf jeweils  30,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten Ersatzfreiheitsstrafen von  jeweils 9 auf jeweils 7 Stunden herabgesetzt werden.

| Predicted | Gold |
|---|---|
| `Theodora Berenwinkel` | `Theodora Berenwinkel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Klam 26, 8673 Steinhöf, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Gudrun Joehnk` | `Gudrun Joehnk` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_8`)


Begründung  Verlauf des Verfahrens  Mit Straferkenntnis vom 27. Dezember 2023, GZ MA67/111111/2023, hat der Magistrat der  Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Arthur Soyal (in weiterer Folge:  Beschwerdeführer) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt, indem er  das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen W-6789 (A) am 4. August  2023 um 11:10 Uhr in einer gebührenpflichtigen Kurzparkzone in 1160 Wien, Hasnerstraße  129, abgestellt habe, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Arthur Soyal` | `Arthur Soyal` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_16`)


Der E-Mail vom 5. Februar 2025 war folgende Vollmacht beigelegt:   „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024 , wohnt Adr1, den  Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt  Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte Akzeptieren Sie das  Einspruch.“

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_31`)


Mit E-Mail vom 5. Februar 2025 übermittelte der Beschwerdeführer ein Schreiben des M mit  folgendem Inhalt: „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024,  wohnt Adr1, den Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu  Magistrat der Stadt Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte  Akzeptieren Sie das Einspruch“.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_44`)


Der belangten Behörde ist zwar zuzustimmen, dass die schriftliche Vollmacht mit  5. Februar 2025 datiert und somit erst nach der Verfahrenshandlung (Erhebung des  Einspruches) vom 10. September 2024 errichtet wurde, die Behörde lässt hierbei jedoch außer  Betracht, dass es sich sowohl bei dem Beschwerdeführer als auch bei dem Vollmachtgeber um  Personen mit offenkundig mangelnden Sprachkenntnissen handelt. Aus der gewählten  Ausdrucksweise lässt sich nach Ansicht des Bundesfinanzgerichts jedoch ableiten, dass der  Beschwerdeführer bereits vor der Verschriftlichung der Vollmacht, nämlich bereits im  Zeitpunkt der Setzung der Verfahrenshandlung am 10. September 2024 mündlich von M zur  Erhebung eines Einspruches gegen die Strafverfügung bevollmächtigt war (Arg: „[…] Herrn  Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt Wien  Magistratsabteilung 67 schicken […]“).

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_16`)


Es wurde in diesem Zusammenhang auch die einschlägige  Gewerbeberechtigung bei Herrn Kaspar Sadowski  wieder als aktiv gemeldet.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_3`)


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

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Unverdroß  Behindertenbetreuerin` — partial — gold is substring of pred: `Unverdroß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

</details>

---

## `Names after 'in der Beschwerdesache' context` 🏆

**F1:** 0.228 | **Precision:** 0.921 | **Recall:** 0.130  

**Format:** `regex`  
**Rule ID:** `8ee5a0d4`  
**Description:**
Captures the name following 'in der Beschwerdesache' with titles, using a capture group to exclude the context phrase.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|in\s+der\s+Sache|in\s+der\s+Revisionssache|in\s+der\s+Verwaltungsstrafsache)\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+r\.\s+nat\.|\s+art\.|\s+techn\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.|Techn\s+R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.921 | 0.130 | 0.228 | 228 | 210 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 210 | 18 | 1404 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lewis Rzehula` | `Lewis Rzehula` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Neustädterstraße 3, 9560 Wabl, Österreich` (address)
- `43-839/6567` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Siegfried Basyurt` | `Siegfried Basyurt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

| Predicted | Gold |
|---|---|
| `Chen Walcker` | `Chen Walcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `63-698/2600` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Mackiewicz` | `Hedwig Mackiewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Buchholz` | `Ursula Buchholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Li Schukardt` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Sven Mitterhuber` | `Sven Mitterhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Mag.a Livia Korowski` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Laetitia Kuban, Karawankenplatz 8, 8046 Graz, Österreich, über die Beschwerde vom 16. Dezember 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 14. November 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für das Kind x in den Zeiträumen vom 01.07.2018 bis zum 30.09.2018  sowie vom 01.07.2019 bis zum 30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Laetitia Kuban` | `Laetitia Kuban` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karawankenplatz 8, 8046 Graz, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karina Ditzler` | `Karina Ditzler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Quentin Girharz` | `Quentin Girharz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Kandler` (person)
- `FA Landeck Reutte` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Gorecki` | `Wieland Gorecki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich` (address)
- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `35-287/7417` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

| Predicted | Gold |
|---|---|
| `Julian Gruening` | `Julian Gruening` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper` (person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (im Folgenden: BFG) hat durch den RichterRi in der Beschwerdesache  Anita Imkeller, Zum Roten Kreuzl 13, 4741 Penesedt, Österreich, betreffend Beschwerde vom 29. März 2021 gegen den Bescheid  des Finanzamt Niederösterreich Mitte  vom 4. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 Steuernummer 50-932/4879  beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Anita Imkeller` | `Anita Imkeller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)
- `Zum Roten Kreuzl 13, 4741 Penesedt, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)
- `50-932/4879` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Ingrid Dohrmaier` | `Ingrid Dohrmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Daläus 14O, 2301 Wittau, Österreich` (address)
- `Korber & Partner WTH-Stb  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Finanzamtes Österreich` (organisation)
- `41-654/1190` (tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Walter Guggenmoos` | `Walter Guggenmoos` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Alice Schöpfel` (person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich` (address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `79-464/0427` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Carla Winterkorn, Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich, über die Beschwerde vom 17. April 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 19. März 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer 43-645/1612  zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Carla Winterkorn` | `Carla Winterkorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `43-645/1612` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Leander Hättrich  in der Beschwerdesache Edith Grotehenn,  Karlhofstraße 20, 4212 Götschka, Österreich, vertreten durch Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Operngasse 6/4/9, 1010 Wien, gegen den Bescheid des FA Wien  4/5/10 vom 05.09.2009 betreffend Körperschaftsteuer 2006 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Edith Grotehenn` | `Edith Grotehenn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Leander Hättrich` (person)
- `Karlhofstraße 20, 4212 Götschka, Österreich` (address)
- `Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `FA Wien  4/5/10` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Revisionssache  Basil Vanak, Oberhof 221, 8345 Trössing, Österreich, über den Antrag des Finanzamtes für Großbetriebe, der zur Zahl  RR/7100124/2021 protokollierten außerordentlichen Revision gegen das Erkenntnis des BFG  vom 24.08.2021, RV/7101805/2021, betreffend   KESt-Rückzahlung gemäß § 21 Abs. 1 Z. 1a KStG 1988 die aufschiebende Wirkung  zuzuerkennen, beschlossen:  Dem Antrag der Revisionswerberin wird stattgegeben und die aufschiebende Wirkung  gemäß § 30 Abs. 2 VwGG zuerkannt.

| Predicted | Gold |
|---|---|
| `Basil Vanak` | `Basil Vanak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Oberhof 221, 8345 Trössing, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `BFG` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Siebgen` | `Juri Siebgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Josef Maurergasse 2, 5424 Riedl, Österreich` (address)
- `MITTEREGGER Steuerberatungs  GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Österreich` (organisation)
- `35-670/1415` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Andreas Kuschy  in der Beschwerdesache Angelika Oligschleger,  Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des Finanzamt Innsbruck  vom 29. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 49-970/7545  nach dem Einlangen des Vorlageantrages vom 10.6.2021  beschlossen:   Der Vorlageantrag wird gem. § 264 Abs 4 lit e Bundesabgabenordnung zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Angelika Oligschleger` | `Angelika Oligschleger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Andreas Kuschy` (person)
- `Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)
- `49-970/7545` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Silvius Jaros, Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2019 betreffend Einkommensteuer 2017 Steuernummer  97-301/3674  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvius Jaros` | `Silvius Jaros` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `97-301/3674` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ramon Reissdorf, Paul-Abl-Straße 9, 2822 Bromberg, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, und ECA Schmidt und  Hertwich Steuer- beratungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die  Beschwerde vom 17. September 2021 gegen die Bescheide des Finanzamtes Österreich vom  26. August 2021, Steuernummer 86-314/1061, betreffend Abweisung des Antrages auf  Wiederaufnahme der Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2017, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ramon Reissdorf` | `Ramon Reissdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag.Dr. Ingrid Fehrer` (person)
- `Paul-Abl-Straße 9, 2822 Bromberg, Österreich` (address)
- `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `86-314/1061` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lieselotte Stiglat  in der Beschwerdesache Sibylle Roßmayr,  Sierling 20, 3632 Pernthon, Österreich, vertreten durch RSM Austria Steuerberatung GmbH, Tegetthoffstraße 7, 1010  Wien, über die Beschwerde vom 16.11.2021 gegen den Bescheid des Finanzamtes Österreich  vom 5. November 2021 betreffend Verspätungszuschlag Umsatzsteuer 4-06/2021,  Steuernummer 58-418/2406  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sibylle Roßmayr` | `Sibylle Roßmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Lieselotte Stiglat` (person)
- `Sierling 20, 3632 Pernthon, Österreich` (address)
- `RSM Austria Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `58-418/2406` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elmira Baintner  in der Beschwerdesache Dietmar Grießmeyer,  Stiftgasse 12, 4654 Aigen, Österreich, über die Beschwerde vom 31. Juli 2021 gegen den Bescheid des FA Steiermark Mitte  vom  26. Juli 2021 betreffend Abweisung eines Rückzahlungsantrages, Steuernummer  64-502/6730, zu Recht erkannt:   I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dietmar Grießmeyer` | `Dietmar Grießmeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Elmira Baintner` (person)
- `Stiftgasse 12, 4654 Aigen, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `64-502/6730` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Klaus Krupok  in der Beschwerdesache Ernst Eschenbrenner,  Irenental 58, 4871 Tiefenbach, Österreich, über die Beschwerde vom 11. August 2016 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich)vom 13. Juli  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 Steuernummer  80-953/9265  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ernst Eschenbrenner` | `Ernst Eschenbrenner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Klaus Krupok` (person)
- `Irenental 58, 4871 Tiefenbach, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `80-953/9265` (tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Nadine Hupmann  in der Beschwerdesache Joachim Kotmann,  Weinbach 15, 8454 Saggau, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 13. Dezember 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum Juli 2018 bis Februar 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Nadine Hupmann` (person)
- `Weinbach 15, 8454 Saggau, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Niels Rustemeier  in der Beschwerdesache Nicoletta Walch,  Polheimerweg 2, 3464 Schmida, Österreich, Steuernummer 65-653/8677, gegen die von der belangten Behörde  Finanzamt Österreich am 13. April 2018 ausgefertigten Bescheide betreffend Umsatzsteuer  und Einkommensteuer für die Jahre 2015, den am 19. April 2018 ausgefertigten Bescheid  betreffend Einkommensteuer 2016 und den am 9. April 2019 ausgefertigten Bescheid  betreffend Einkommensteuervorauszahlung für 2019 und Folgejahre beschlossen:  I. Die angefochtenen Bescheide werden gemäß § 278 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Nicoletta Walch` | `Nicoletta Walch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mag. Niels Rustemeier` (person)
- `Polheimerweg 2, 3464 Schmida, Österreich` (address)
- `65-653/8677` (tax_number)
- `Finanzamt Österreich` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Adriana Eiffler, Waldhofweg 36a, 8321 Entschendorf, Österreich, betreffend Beschwerde vom 24. Februar 2021  gegen die Bescheide des Finanzamtes Österreich vom 9. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 78-550/2209, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Adriana Eiffler` | `Adriana Eiffler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Waldhofweg 36a, 8321 Entschendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-550/2209` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Hartmut Schalk, Parhamerplatz 8, 9112 Gletschach, Österreich, betreffend Beschwerde vom 31. Juli 2012 gegen die Bescheide des  FA Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 29. Juli 2011 betreffend  Einkommensteuer der Jahre 2006 bis 2010, Steuernummer 16-753/5618  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hartmut Schalk` | `Hartmut Schalk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Parhamerplatz 8, 9112 Gletschach, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-753/5618` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Severin Iwanowsky  in der Beschwerdesache Richard Joistgen,  Breitenbachstraße 15, 4794 Glatzing, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 31. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 81-572/7905  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Richard Joistgen` | `Richard Joistgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Severin Iwanowsky` (person)
- `Breitenbachstraße 15, 4794 Glatzing, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)
- `81-572/7905` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Harald Adriaans, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Harald Adriaans` | `Harald Adriaans` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Pflaster 68, 2872 Neustift am Alpenwalde, Österreich` (address)
- `Mag. Markus Wagner` (person)
- `Finanzamtes Österreich` (organisation)
- `81-584/4494` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Laila Klimenkow` | `Laila Klimenkow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Frederik von Gruber` (person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich` (address)
- `Causa Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Björn Augusto  in der Beschwerdesache Mona Reinhard,  Urschendorf 19, 4261 Kerschbaum, Österreich, vertreten durch IMMUNITAS Wirtschaftsprüfung GmbH, Schlickgasse 3 Tür 7,  1090 Wien, über die Beschwerde der beschwerdeführenden Partei vom 17.05.2022, beim  Bundesfinanzgericht eingelangt am 19.05.2022, wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt für Großbetriebe betreffend Einkommen- und  Umsatzsteuer 2020 den Beschluss:   I. Das Säumnisbeschwerdeverfahren wird eingestellt.    II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mona Reinhard` | `Mona Reinhard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Björn Augusto` (person)
- `Urschendorf 19, 4261 Kerschbaum, Österreich` (address)
- `IMMUNITAS Wirtschaftsprüfung GmbH` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/137175.1`) (sent_id: `deanon_BFG_20260814_TEST/137175.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Ashley Wanagat, Dörfles 5, 9182 Greuth, Österreich, vertreten durch LBG Niederösterreich  Steuerberatung GmbH, Schloßparkgasse 6, 3950 Gmünd, betreffend Beschwerde vom  14. Februar 2020 gegen den Bescheid des Finanzamtes Österreich vom 21. Jänner 2020  betreffend Einkommensteuer 2017 Steuernummer 33-883/1280  den Beschluss:  I. Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als  zurückgenommen.

| Predicted | Gold |
|---|---|
| `Ashley Wanagat` | `Ashley Wanagat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniel Philip Pfau` (person)
- `Dörfles 5, 9182 Greuth, Österreich` (address)
- `LBG Niederösterreich  Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `33-883/1280` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Johanna Housein, Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich, über die Beschwerde vom 17. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 15. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 85-874/2370, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Johanna Housein` | `Johanna Housein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-874/2370` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Merlin Leuprecht` | `Merlin Leuprecht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Christine Kralova` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Anton Fleischhacker` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bertha Unverich` | `Bertha Unverich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Hinterseberweg 13D, 4742 Gewerbepark, Österreich` (address)
- `Dr. Robert Karl Galler` (person)
- `92-593/4806` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Alva Danell, Robert Lieben-Promenade 68, 5251 Thalheim, Österreich, vertreten durch Nikolaus WP GmbH Rnf. ÖBUG KG, St Veitg 8, 1130  Wien, über die Beschwerde vom 6. März 2014 gegen den Bescheid des Finanzamtes Wien  9/18/19 Klosterneuburg vom 10. Februar 2014 betreffend Einkommensteuer 2012  Steuernummer 48-595/6877  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alva Danell` | `Alva Danell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Stefan Pipal` (person)
- `Robert Lieben-Promenade 68, 5251 Thalheim, Österreich` (address)
- `Nikolaus WP GmbH Rnf. ÖBUG KG` (organisation)
- `Finanzamtes Wien  9/18/19 Klosterneuburg` (organisation)
- `48-595/6877` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/137595.1`) (sent_id: `deanon_BFG_20260814_TEST/137595.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter [Richter] in der Beschwerdesache Shirley Adamczewski,  Stein 26, 9313 Töplach, Österreich, über die Beschwerde vom 13. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 30. Juni 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Februar bis Dezember 2020 zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Shirley Adamczewski` | `Shirley Adamczewski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stein 26, 9313 Töplach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Muran Unverricht, Bleischweg 3, 9500 Rennstein, Österreich, über die Beschwerden vom 28. Oktober 2018, vom 9. Februar 2019  und vom 7. Februar 2020 gegen die Bescheide des Finanzamtes Österreich vom 26. Juli 2018  betreffend Abweisung eines Antrages auf Aufhebung des Körperschaftsteuerbescheides 2016  sowie vom 31. Jänner 2019 und vom 16. Jänner 2020 betreffend Körperschaftsteuer 2017 und  2018 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Abweisung eines Antrages auf Aufhebung  des Körperschaftsteuerbescheides 2016 wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Muran Unverricht` | `Muran Unverricht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Bleischweg 3, 9500 Rennstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/137900.1`) (sent_id: `deanon_BFG_20260814_TEST/137900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Maurice Speckner,  Hinterweg 94, 2305 Pframa, Österreich, über die Beschwerde vom 5. Juni 2020 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 88-902/6713  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Maurice Speckner` | `Maurice Speckner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterweg 94, 2305 Pframa, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-902/6713` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Roderich Stenczel, St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich, über die Beschwerde vom 20. August 2013 gegen die Bescheide  des FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Wiederaufnahme gemäß § 303 BAO  der Körperschaftsteuerbescheide 2008 bis 2010, Steuernummer 60-379/9146  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Stenczel` | `Roderich Stenczel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `60-379/9146` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/137956.1`) (sent_id: `deanon_BFG_20260814_TEST/137956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Dorothea Grosseholz  in der Beschwerdesache Miroslav Runau,  Neu Amerika 13, 4623 Fernreith, Österreich, über die Beschwerde vom 19. Juni 2019 gegen den Einkommensteuerbescheid  2018 des FA Steiermark Mitte  vom 18. Juni 2019, Steuernummer 89-067/6879, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Miroslav Runau` | `Miroslav Runau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Dorothea Grosseholz` (person)
- `Neu Amerika 13, 4623 Fernreith, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `89-067/6879` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/138120.1`) (sent_id: `deanon_BFG_20260814_TEST/138120.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Birgit Altvater, Pizachweg 11, 2020 Oberfellabrunn, Österreich, vertreten durch JM Wirtschaftsprüfungs-GmbH,  Sonnhubergasse 9, 4060 Leonding, und JM Wirtschaftsprüfungs-GmbH, Sonnhubergasse 9,  4060 Leonding, betreffend Beschwerde vom 15. April 2022 gegen die Bescheide des  Finanzamtes Österreich vom  1. 25. Oktober 2021 betreffend Festsetzung einer Zwangsstrafe iHv 1.000 Euro und   2. 12. Jänner 2022 betreffend Festsetzung einer Zwangsstrafe iHv 4.000 Euro,

| Predicted | Gold |
|---|---|
| `Birgit Altvater` | `Birgit Altvater` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniel Philip Pfau` (person)
- `Pizachweg 11, 2020 Oberfellabrunn, Österreich` (address)
- `JM Wirtschaftsprüfungs-GmbH` (organisation)
- `JM Wirtschaftsprüfungs-GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Nadine Tomczack` | `Nadine Tomczack` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Finanzamtes Österreich` (organisation)
- `15-984/4583` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hemma Mauermair  in der   Beschwerdesache Franziska Fitzmann, Larchwald 7, 8850 Sankt Egidi, Österreich, vertreten durch Mag. Markus Franz Ganzer,  Anichstraße 13, 6020 Innsbruck, über die Beschwerde vom 29. Oktober 2021 gegen den  Bescheid des Finanzamtes Österreich vom 29. September 2021, Ordnungsbegriff Nr1,  betreffend Abweisung der Anträge auf Gewährung der erhöhten Familienbeihilfe ab Jänner  2015 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Franziska Fitzmann` | `Franziska Fitzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hemma Mauermair` (person)
- `Larchwald 7, 8850 Sankt Egidi, Österreich` (address)
- `Mag. Markus Franz Ganzer` (person)
- `Finanzamtes Österreich` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Gotthard Kirchhoffs, Unterriese 2, 7432 Oberschützen, Österreich, vertreten durch WWV-GROUP  SteuerberatungsGmbH, Bahnhofstraße 4, 3950 Gmünd, über die Beschwerde vom  28. September 2021 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli 2021  betreffend Haftung für Lohnsteuer, Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  für die Jahre 2015 bis 2019, Steuernummer 19-927/9012, zu Recht erkannt:   I. Der Beschwerde gegen die Bescheide betreffend Festsetzung des Zuschlags zum  Dienstgeberbeitrag 2015 bis 2019 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gotthard Kirchhoffs` | `Gotthard Kirchhoffs` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Unterriese 2, 7432 Oberschützen, Österreich` (address)
- `WWV-GROUP  SteuerberatungsGmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `19-927/9012` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Heike Lohoff, Odescalchigasse 154, 4264 Lichtenau, Österreich, vertreten durch Vertreter, AdrVertreter, über die Beschwerde vom 15. Juli 2015 gegen  den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr:  Finanzamt Österreich) vom 6. Juli 2015 betreffend Grunderwerbsteuer, Steuernummer  77-421/3532, Erfassungsnummer 10-2012, nach Durchführung von mündlichen  Verhandlungen am 13.10.2021 und 10.08.2022 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heike Lohoff` | `Heike Lohoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Odescalchigasse 154, 4264 Lichtenau, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)
- `77-421/3532` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Richarda Blatzer, Rolfis 18, 5144 Feichten, Österreich, wegen behaupteter Verletzung der  Entscheidungspflicht des Finanzamtes Österreich betreffend die Erlassung eines  Einkommensteuerbescheides für das Veranlagungsjahr 2021 (Steuernummer 32-825/9727  ) beschlossen:   I. Die Säumnisbeschwerde vom 02.09.2022 wird gemäß § 260 Abs. 1 lit. a iVm § 284  Abs. 7 lit. b BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Richarda Blatzer` | `Richarda Blatzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Rolfis 18, 5144 Feichten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-825/9727` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner als Vorsitzende, den  Richter Mag. Dieter Ortner sowie die fachkundigen Laienrichter Mag. Reinhard Krassnig und  Komm. Rat Max Stechauner in der Beschwerdesache Dirk Ambrose, Herrnberg 22, 5152 Schönberg, Österreich, vertreten  durch Kohlfürst, Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH, St. Veiter Ring  1A, 9020 Klagenfurt/Wörthersee, und Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerde vom 20. Dezember 2017 gegen den Bescheid des Finanzamtes  Klagenfurt (nunmehr Finanzamt Österreich) vom 23. November 2017 mit dem ein Antrag  gemäß § 303 Abs. 1 BAO vom 27. Februar 2017 auf Wiederaufnahme des Verfahrens  betreffend Einkommensteuer 2002, Steuernummer 21-063/4049, abgewiesen worden ist,  nach Durchführung einer mündlichen Verhandlung am 10. August 2022 in Anwesenheit der  Schriftführerin FOI Alexandra Dumpelnik zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dirk Ambrose` | `Dirk Ambrose` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Elisabeth Hafner` (person)
- `Mag. Dieter Ortner` (person)
- `Mag. Reinhard Krassnig` (person)
- `Komm. Rat Max Stechauner` (person)
- `Herrnberg 22, 5152 Schönberg, Österreich` (address)
- `Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-063/4049` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/138977.1`) (sent_id: `deanon_BFG_20260814_TEST/138977.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Yelec Tummascheit  in der Beschwerdesache Gerda Staigl,  Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich, über die Beschwerde vom 11.08.2022 gegen den Bescheid des Finanzamtes  Österreich vom 05.08.2022, Steuernummer 64-583/4801, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021, zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gerda Staigl` | `Gerda Staigl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Yelec Tummascheit` (person)
- `Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `64-583/4801` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Dr.in Wendy Chudak  in der Beschwerdesache Susette Hadenfelt,  Burgergasse 57, 2632 St. Valentin-Landschach, Österreich, vertreten durch Huber & Rosenthal Steuerberatung KG, Stadtplatz 56, 5280  Braunau/Inn, über die Beschwerde vom 9. August 2017 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 17. Juli 2017 betreffend Einkommensteuer 2016 Steuernummer  34-724/8270  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Hadenfelt` | `Susette Hadenfelt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Priv.-Doz.in Dr.in Wendy Chudak` (person)
- `Burgergasse 57, 2632 St. Valentin-Landschach, Österreich` (address)
- `Huber & Rosenthal Steuerberatung KG` (organisation)
- `Finanzamtes  Braunau Ried Schärding` (organisation)
- `34-724/8270` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Leonhard Osskinat, Schreyvogelgasse 2V, 8262 Leithen, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid des Finanzamtes  Baden Mödling, nunmehr Finanzamt Österreich, vom 18. Oktober 2019 betreffend Abweisung  des Antrages vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur  Familienbeihilfe für Hartmut Groebmair  ab Juli 2019,   Steuernummer 39-801/9564, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Leonhard Osskinat` | `Leonhard Osskinat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schreyvogelgasse 2V, 8262 Leithen, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)
- `Hartmut Groebmair` (person)
- `39-801/9564` (tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Esmeralda Fietze  in der Beschwerdesache Norbert Hummels,  Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich, über die Beschwerde vom 18. Mai 2022 gegen die Bescheide des Finanzamtes  Österreich vom 25. April 2022 betreffend Gebühren 2021 sowie Gebührenerhöhung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Norbert Hummels` | `Norbert Hummels` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Esmeralda Fietze` (person)
- `Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Charlotte Hirschmueller Silberhumerweg 2, 9163 Bodental, Österreich,  vertreten durch HR Danielle Schochert, Haßreidterstraße 75, 8831 Raiming, Österreich, über die Beschwerde vom  21. Dezember 2018 gegen die Bescheide des FA vom 28. September 2018 betreffend  Wiederaufnahme des Verfahren betreffend Einkommensteuer 2011 bis 2014,  Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014, Steuernummer  46-246/2967, zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide betreffend Wiederaufnahme des Verfahren  betreffend Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014  werden als unbegründet abgewiesen.

**False Positives:**

- `Charlotte Hirschmueller Silberhumerweg` — partial — gold is substring of pred: `Charlotte Hirschmueller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Charlotte Hirschmueller`(person)
- `Silberhumerweg 2, 9163 Bodental, Österreich`(address)
- `HR Danielle Schochert`(person)
- `Haßreidterstraße 75, 8831 Raiming, Österreich`(address)
- `46-246/2967`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Bettina Domigall` — partial — pred is substring of gold: `Bettina Domigall, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Mag. Susanne Haim`(person)
- `Mag Stefan Raab`(person)
- `Leopold Pichlbauer`(person)
- `Bettina Domigall, Bakk. iur.`(person)
- `Zickhöhe 66, 3361 Biberbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Tanja Grottenthaler`(person)

</details>

---

## `Names after 'von' (Family/Relation Context)` 🏆

**F1:** 0.020 | **Precision:** 0.889 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `bb3830e3`  
**Description:**
Captures names following 'von' in contexts like 'Kindesmutter von', 'Vater von', etc., ensuring the name is a person.

**Content:**
```
(?:Kindesmutter|Vater|Mutter|Sohn|Tochter|Ehefrau|Ehemann|Elternteil|Angehörige|Angehöriger)\s+(?:von\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.010 | 0.020 | 18 | 16 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 16 | 2 | 1598 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_13`)


II. Über die Beschwerde wurde erwogen:  1. Sachverhalt   Der Bf. bezog im Jahr 2019 für seinen Sohn Rudolf Kumpmeier, geboren am 30. September 1972,  Familienbeihilfe.

| Predicted | Gold |
|---|---|
| `Rudolf Kumpmeier` | `Rudolf Kumpmeier` |

**Missed by this rule (FN):**

- `30. September 1972` (date)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_44`)


Für den Sohn Rudolf Kumpmeier  hat der Bf. im Streitjahr 2019 Familienbeihilfe bezogen, sodass die  Anspruchsvoraussetzungen für die Gewährung des Familienbonus Plus erfüllt sind.

| Predicted | Gold |
|---|---|
| `Rudolf Kumpmeier` | `Rudolf Kumpmeier` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_19`)


Die Exfrau sei im Jänner 2020 ausgezogen und seither  bezahle der Beschwerdeführer Alimente für den Sohn Herbert Schaffarik.

| Predicted | Gold |
|---|---|
| `Herbert Schaffarik` | `Herbert Schaffarik` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_22`)


Festgestellt Sachverhalt   Der Beschwerdeführer ist Vater von OStR Priv.-Doz. Theodor Voelpel  und Herbert Schaffarik  und lebte dieser im Jahr  2020 bis zum 08. Jänner mit der Mutter der beiden Söhne, mit der der Beschwerdeführer auch  verheiratet war, sowie den beiden Kindern in einem gemeinsamen Haushalt. Am 08. Jänner zog  die Mutter zusammen mit dem Sohn Herbert Schaffarik  aus dem gemeinsamen Haushalt aus.

| Predicted | Gold |
|---|---|
| `Herbert Schaffarik` | `Herbert Schaffarik` |

**Missed by this rule (FN):**

- `OStR Priv.-Doz. Theodor Voelpel` (person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_25`)


außergerichtlichen Vereinbarung mit der Mutter sowie ab August infolge einer  Unterhaltsvereinbarung vor der Kinder- und Jugendhilfe des Magistrats Salzburg Unterhalt für  den bei der Mutter wohnhaften Sohn Herbert Schaffarik.

| Predicted | Gold |
|---|---|
| `Herbert Schaffarik` | `Herbert Schaffarik` |

**Missed by this rule (FN):**

- `Magistrats` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_104`)


Zum Unterhaltsabsetzbetrag  Nach dem festgestellten Sachverhalt hat der Beschwerdeführer in Bezug auf den Sohn  Herbert Schaffarik  ab Jänner 2020 monatlich Unterhalt gezahlt. Dem Beschwerdeführer steht  folglich für Monate Jänner bis Dezember der Unterhaltsabsetzbetrag in Höhe von EUR 29,20  monatlich zu. Da der Unterhaltsabsetzbetrag im Rahmen des bekämpften Bescheides keine  Berücksichtigung fand, musste dieser Umstand vom Bundesfinanzgericht bei der Änderung des  bekämpften Bescheides aufgegriffen werden.

| Predicted | Gold |
|---|---|
| `Herbert Schaffarik` | `Herbert Schaffarik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_109`)


Dem  Beschwerdeführer steht daher für den Zeitraum Jänner bis Dezember als  Familienbeihilfenberechtigter für diesen Sohn gem. § 33 Abs. 3a Z 3 lit. a EStG 1988 sowie auch  im Fall eines Zustehens eines Unterhaltsabsetzbetrages gem. § 33 Abs. 3a Z 3 lit b EStG 1988  der Familienbonus Plus zu.  Aber auch betreffend den Sohn Herbert Schaffarik  steht dem Beschwerdeführer gem. § 33 Abs. 3a Z  3 lit. b EStG 1988 der Familienbonus Plus für die Monate Jänner bis Dezember zu, da der  Beschwerdeführer in diesem Zeitraum Unterhalt für diesen Sohn geleistet hat und ihm  infolgedessen, wie bereits unter Punkt 2 dargestellt, für diesen Zeitraum der  Unterhaltsabsetzbetrag zusteht.

| Predicted | Gold |
|---|---|
| `Herbert Schaffarik` | `Herbert Schaffarik` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_11`)


In der Folge führte Sohn aus:  „Ich habe meinen Betrieb im Jahr 2011 von meinem Vater Quentin Schwartkopp  übernommen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_7`)


Die Bf brachte vor, dass ihre Tochter Heidemarie Fitzenreiter  während ihres Schulbesuches in Israel  nicht erwerbstätig und ledig gewesen sei, weshalb sie einen Unterhaltsanspruch gehabt habe.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_25`)


Weiters habe sich die  Tochter Heidemarie Fitzenreiter  aber auch im Beschwerdezeitraum in Israel und damit ständig im  Ausland aufgehalten.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_37`)


Auch die Bf gab in  einem von ihr ausgefüllten und am 22.06.2023 unterzeichneten Datenblatt zur Überprüfung  des Anspruches auf Familienbeihilfe an, dass ihre Tochter Heidemarie Fitzenreiter  ab 05.09.2022 bis  12.06.2023 am Neve College for Woman ein Seminar absolviert habe (Art der Ausbildung nach  Angabe der Bf: „Jeschiva for woman“).

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_69`)


§ 5 Abs 3 FLAG 1967 schließt einen  Familienbeihilfenanspruch in den hier unter anderem streitgegenständlichen Monaten  November 2022 bis Mai 2023 für die Tochter Heidemarie Fitzenreiter  aus, weshalb auch dahingestellt  bleiben kann, ob aufgrund des College-Besuches der Tochter der Bf in Israel in den Monaten  November 2022 bis Mai 2023 eine Berufsausbildung im Sinne des § 2 Abs 1 lit b FLAG 1967  vorgelegen ist.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_81`)


In der Beschwerde brachte die Bf vor, dass ihre Tochter Heidemarie Fitzenreiter  während ihres  Schulbesuches in Israel nicht erwerbstätig und ledig gewesen sei, weshalb sie einen  Unterhaltsanspruch gehabt habe.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_85`)


Im Vorlageantrag erläuterte die Bf wie folgt: Sie habe das Finanzamt mit Schreiben vom  20.09.2022 um Verlängerung der Familienbeihilfe für ihre Tochter Heidemarie Fitzenreiter  ersucht.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/146075.1`) (sent_id: `deanon_BFG_20260814_TEST/146075.1_36`)


Die Beschwerdeführerin bezog für ihre volljährige Tochter Delila Hollek, geboren am  TT.10.2000, im Zeitraum von September 2019 bis Februar 2023 Familienbeihilfe,  Kinderabsetzbeträge sowie die Geschwisterstaffel aufgrund des Schulbesuches an der  Handelsakademie für Berufstätige in Wien.

| Predicted | Gold |
|---|---|
| `Delila Hollek` | `Delila Hollek` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_18`)


Zum Ablauf der langwierigen Abgabe der Diplomarbeit meiner Tochter Luna Schaffrath, die  sehr wohl ernsthaft und sehr zielstrebig ihre Matura geschafft hat.

| Predicted | Gold |
|---|---|
| `Luna Schaffrath` | `Luna Schaffrath` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_14`)


Betreffend seinen Sohn Luigi Assenov, LLB, geboren am 23. Oktober 1983,  wurde die Familienbeihilfe mit Juni 2017 eingestellt.  Der jüngere Sohn, Rudolf Kumpmeier, hatte im Jahr 2019 das 18.

**False Positives:**

- `Luigi Assenov` — partial — pred is substring of gold: `Luigi Assenov, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Luigi Assenov, LLB`(person)
- `23. Oktober 1983`(date)
- `Rudolf Kumpmeier`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_42`)


Der Anspruch auf Familienbeihilfe für den Sohn Luigi Assenov, LLB  endete mit Juni 2017.

**False Positives:**

- `Luigi Assenov` — partial — pred is substring of gold: `Luigi Assenov, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Luigi Assenov, LLB`(person)

</details>

---

## `Names after 'Beschwerde des' (Genitive)` 🏆

**F1:** 0.028 | **Precision:** 0.885 | **Recall:** 0.014  

**Format:** `regex`  
**Rule ID:** `284fd772`  
**Description:**
Captures the name following 'Beschwerde des/der', excluding common non-person nouns, and handling split titles.

**Content:**
```
(?:Beschwerde\s+(?:des|der)\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?!\s+(?:Abgabepflichtigen|Verein|Gesellschaft|AG|mbH|GmbH|KG|UG|Stiftung|Beh\u00f6rde|Amt|Finanzamt|Gericht|Kommission|Ausschuss|Komitee|Firma|Unternehmen|Organisation|Institution|Partei|Bewegung|Bund|Land|Stadt|Gemeinde|Bezirk|Kreis|Region|Kanton|Kommune|Verband|Kammer|Institute|Institut|Forschung|Lehrstuhl|Klinik|Krankenhaus|Hochschule|Universit\u00e4t|Schule|Akademie|Zentrum|Institut|B\u00fcro|Praxis|Wohnung|Haus|Geb\u00e4ude|Grundst\u00fcck|Fl\u00e4che|Land|Gebiet|Territorium|Staat|Reich|Kaiserreich|Republik|Monarchie|Demokratie|Diktatur|Faschismus|Kommunismus|Sozialismus|Kapitalismus|Liberalismus|Konservatismus|Nationalismus|Internationalismus|Globalismus|Regionalismus|F\u00f6deralismus|Zentralismus|Autokratie|Oligarchie|Anarchie|Totalitarismus|Demokratie|Rechtsstaat|Verfassungsstaat|Sozialstaat|Wohlfahrtsstaat|Marktwirtschaft|Planwirtschaft|Mischwirtschaft|Sozialmarktwirtschaft|Freie Marktwirtschaft|Sozialistische Marktwirtschaft|Kapitalistische Marktwirtschaft|Neoliberale Marktwirtschaft|Sozialdemokratische Marktwirtschaft|Konservative Marktwirtschaft|Libert\u00e4re Marktwirtschaft|Anarchistische Marktwirtschaft|Faschistische Marktwirtschaft|Kommunistische Marktwirtschaft|Sozialistische Planwirtschaft|Kapitalistische Planwirtschaft|Neoliberale Planwirtschaft|Sozialdemokratische Planwirtschaft|Konservative Planwirtschaft|Libert\u00e4re Planwirtschaft|Anarchistische Planwirtschaft|Faschistische Planwirtschaft|Kommunistische Planwirtschaft|Sozialistische Mischwirtschaft|Kapitalistische Mischwirtschaft|Neoliberale Mischwirtschaft|Sozialdemokratische Mischwirtschaft|Konservative Mischwirtschaft|Libert\u00e4re Mischwirtschaft|Anarchistische Mischwirtschaft|Faschistische Mischwirtschaft|Kommunistische Mischwirtschaft|Sozialistische Marktwirtschaft|Kapitalistische Marktwirtschaft|Neoliberale Marktwirtschaft|Sozialdemokratische Marktwirtschaft|Konservative Marktwirtschaft|Libert\u00e4re Marktwirtschaft|Anarchistische Marktwirtschaft|Faschistische Marktwirtschaft|Kommunistische Marktwirtschaft|Sozialistische Planwirtschaft|Kapitalistische Planwirtschaft|Neoliberale Planwirtschaft|Sozialdemokratische Planwirtschaft|Konservative Planwirtschaft|Libert\u00e4re Planwirtschaft|Anarchistische Planwirtschaft|Faschistische Planwirtschaft|Kommunistische Planwirtschaft|Sozialistische Mischwirtschaft|Kapitalistische Mischwirtschaft|Neoliberale Mischwirtschaft|Sozialdemokratische Mischwirtschaft|Konservative Mischwirtschaft|Libert\u00e4re Mischwirtschaft|Anarchistische Mischwirtschaft|Faschistische Mischwirtschaft|Kommunistische Mischwirtschaft)(?=\s|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.885 | 0.014 | 0.028 | 26 | 23 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 3 | 1591 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Serge Pechert` | `Serge Pechert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Elisabeth Brunner` (person)
- `Texing 43, 3143 Oberloitzenberg, Österreich` (address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des Rocco Choudhury, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Rocco Choudhury` | `Rocco Choudhury` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wachtelgasse 7, 9543 Stadt, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde der  Florentin Blatner, Hetzerstraße 11, 4712 Armau, Österreich, vom 18. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 18. Dezember 2020, Zl. MA67/Zahl/2020, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Florentin Blatner` | `Florentin Blatner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Hetzerstraße 11, 4712 Armau, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt  Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_3`)


über die Beschwerde des Lukas Niedergesess, Staudenstraße 7, 3834 Eisenreichs, Österreich, Deutschland, vom 16. Februar 2021, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 13. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1 Parkometer- gesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Lukas Niedergesess` | `Lukas Niedergesess` |

**Missed by this rule (FN):**

- `Staudenstraße 7, 3834 Eisenreichs, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, über die Beschwerde der Bodo Saday, Alois Windisch-Straße 1, 5121 Hofweiden, Österreich, vom 14. Juli 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 28. Juni 2021, GZ. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Bodo Saday` | `Bodo Saday` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alois Windisch-Straße 1, 5121 Hofweiden, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde der Michael Klingsohr, Hochburg 78, 4363 Pabneukirchen, Österreich, vom 09. Dezember  2016 gegen den Bescheid des Magistrats der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

| Predicted | Gold |
|---|---|
| `Michael Klingsohr` | `Michael Klingsohr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Hochburg 78, 4363 Pabneukirchen, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die Beschwerde der Estelle Ivankovic, Heilhamer Weg 231, 2602 Schönau an der Triesting, Österreich, vom 27. Jänner 2022, gegen das Straferkenntnis der belangten Behörde, Magistrat der  Stadt Wien, als Abgabenstrafbehörde vom 3. Jänner 2022, Zahl MA67/Zahl/2021, betreffend  eine Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in der Fassung ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4  Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl. für  Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Estelle Ivankovic` | `Estelle Ivankovic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heilhamer Weg 231, 2602 Schönau an der Triesting, Österreich` (address)
- `Magistrat der  Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/136624.1`) (sent_id: `deanon_BFG_20260814_TEST/136624.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die Beschwerde der Heiko Cortnumme, Barbarasiedlung D/ 3, 9314 Garzern, Österreich, vertreten durch Vertreter, vom 11. Dezember 2017 gegen die Bescheide des  Finanzamtes Österreich, vormals Finanzamtes Bruck Eisenstadt Oberwart, vom 3. Oktober  2017 betreffend Körperschaftsteuer 2006 und 2007, vom 12. Oktober 2017 betreffend  Körperschaftsteuer 2008 sowie vom 16. November 2017 betreffend Körperschaftsteuer 2018,  Steuernummer 01-857/0717, nach der am 9. März 2022 in Hintere Zollamstsstraße 2b,  1030 Wien, durchgeführten mündlichen Verhandlung im Beisein der Schriftführerin R zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Heiko Cortnumme` | `Heiko Cortnumme` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Barbarasiedlung D/ 3, 9314 Garzern, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `01-857/0717` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Julia Reittinger, Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich, vertreten durch Annemarie Entschev-Kurzmann, Mariahilfer Straße  140 Tür 10, 1150 Wien, vom 25. November 2020, gegen den Bescheid des Finanzamtes  Österreich vom 10. November 2020 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe und des Erhöhungsbetrages ab März 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Julia Reittinger` | `Julia Reittinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich` (address)
- `Annemarie Entschev-Kurzmann` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde der  Zlatan Wetterling, Am Kochfeld 129, 4770 Oberndorf, Österreich, vom 21. November 2019, gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 8. November 2019 betreffend gemäß § 8a FLAG gekürzte  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Zlatan Wetterling` | `Zlatan Wetterling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Doktor` (person)
- `Am Kochfeld 129, 4770 Oberndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde des Jessica Tenbrink, Dornlandweg 6, 8354 Risola, Österreich, vom 29. August 2022, gegen den Bescheid des  Finanzamtes Österreich vom 17. August 2022, betreffend Abweisung des Antrages auf  Gewährung von Familienbeihilfe ab Mai 2022, zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jessica Tenbrink` | `Jessica Tenbrink` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Dornlandweg 6, 8354 Risola, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Cornelia Reifs,  Hub an der Mank 8, 9300 Draschelbach, Österreich, vom 25. Mai 2023, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 26. April  2023, GZ. MA67/Zahl/2022, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien  Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Cornelia Reifs` | `Cornelia Reifs` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hub an der Mank 8, 9300 Draschelbach, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch den Richter Mag. Christian Seywald über die  Beschwerde der Uwe Rossberg, Stadels 61, 8990 Reith, Österreich, vom 1. Februar 2024, gegen das Straferkenntnis  der belangten Behörde, Magistrat der Stadt Wien, als Abgabenstrafbehörde vom 24. Jänner  2024, GZ. MA67/GZ/2023, betreffend eine Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in der Fassung ABl. der Stadt  Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Uwe Rossberg` | `Uwe Rossberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Mag. Christian Seywald` (person)
- `Stadels 61, 8990 Reith, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt  Wien` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad über die Beschwerde des  Arthur Soyal, Josef-Prangl-Straße 16, 8342 Perlsdorf, Österreich, vom 23. Jänner 2024 gegen das Straferkenntnis des Magistrates  der Stadt Wien vom 27. Dezember 2023, Geschäftszahl MA67/111111/2023, betreffend  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung, ABl der Stadt  Wien 2005/51 in Verbindung mit § 4 Abs 1 Wiener Parkometergesetz 2006, LGBI für Wien  2006/9 in der Fassung LGBl für Wien 2012/24, nach Durchführung einer mündlichen  Verhandlung am 21. Mai 2024, im Beisein des Schriftführers AD Rudolf Keinberger, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs  1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Arthur Soyal` | `Arthur Soyal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Konrad` (person)
- `Josef-Prangl-Straße 16, 8342 Perlsdorf, Österreich` (address)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt  Wien` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Jeanne Pavlovitsch, Döbinggasse 9, 4153 Kirchbach, Österreich, vom 5. August 2024, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67 vom 31. Juli 2024, GZ. MA67/GZ/2024, mit  dem der Einspruch vom 12. Juni 2024 gegen die Strafverfügung vom 4. Juni 2024, mit  derselben Geschäftszahl, gemäß § 13 Abs. 3 AVG iVm § 24 VStG 1991 zurückgewiesen wurde,  zu Recht:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird der oben genannte, angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Döbinggasse 9, 4153 Kirchbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde der Helge Schilsong, Jheringgasse 45, 3950 Wielands, Österreich, vom 6. September 2024 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 3.  September 2024, GZ. MA67/GZ1/2024, mit dem der Einspruch vom 24. Juli 2024 gegen die  Strafverfügung vom 27. Mai 2024, GZ. MA67/GZ1/2024, gemäß § 49 Abs. 1 VStG 1991  zurückgewiesen wurde, zu Recht:    Der Beschwerde wird gemäß § 50 VwGVG Folge gegeben und der angefochtene  Zurückweisungsbescheid aufgehoben.

| Predicted | Gold |
|---|---|
| `Helge Schilsong` | `Helge Schilsong` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Jheringgasse 45, 3950 Wielands, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Felizitas Kobl, Zornberg 27, 4681 Watzing, Österreich, vom 10. August 2024 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 26. Juli 2024, GZ. MA67/GZ/2024, betreffend  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Verhandlung am 24. Oktober 2024 im Beisein des  Schriftführers SF, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 VStG von der Verhängung einer Strafe abgesehen und  dem Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit seines Verhaltens eine  Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Felizitas Kobl` | `Felizitas Kobl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Zornberg 27, 4681 Watzing, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)
- `Stadt  Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/146931.1`) (sent_id: `deanon_BFG_20260814_TEST/146931.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Simon Eylert  über die Beschwerde des Senta Orlovius,  Florianiweg 6, 2640 Schlagl, Österreich, vom 22. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  13. Februar 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021, ergangen  zur Steuernummer 31-279/5148, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Senta Orlovius` | `Senta Orlovius` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Simon Eylert` (person)
- `Florianiweg 6, 2640 Schlagl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `31-279/5148` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  der Jeffrey Heilmayr, Johann Holzmann-Straße 222, 4912 Ponneredt, Österreich, vom 20. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 15. März 2023, mit dem der Antrag auf Familienbeihilfe und  Erhöhungsbetrag  ab August 2022 abgewiesen wurde, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jeffrey Heilmayr` | `Jeffrey Heilmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Johann Holzmann-Straße 222, 4912 Ponneredt, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Sandro Stoeckicht  über die Beschwerde des Zeno Bauermann,  Oisreitl 3, 9570 Rappitsch, Österreich  vom 11. April 2025, gegen das Straferkenntnis der belangten Behörde  Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde, vom 31. März  2025, GZ. MA67/GZ1/2024, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:   I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Zeno Bauermann` | `Zeno Bauermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Sandro Stoeckicht` (person)
- `Oisreitl 3, 9570 Rappitsch, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Adriana Zwick, Via Monsano 359J, 3830 Nonndorf, Österreich, vom 24. April 2025 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 16. April 2025, GZ. MA67/GZ/2025, wegen einer  Verwaltungsübertretung nach § 2 in Verbindung mit § 4 Abs. 2 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Adriana Zwick` | `Adriana Zwick` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Via Monsano 359J, 3830 Nonndorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  der Adelheid Lokaizyk, Waldmeistergasse 162, 9241 Zettin, Österreich, vom 10. Juni 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. Juni 2021 betreffend Rückforderung von Familienbeihilfe- und  Kinderabsetzbeträgen für den Zeitraum Jänner 2020 bis Oktober 2020, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Adelheid Lokaizyk` | `Adelheid Lokaizyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Waldmeistergasse 162, 9241 Zettin, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der Cathleen Gröneweg, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Cathleen Gr` — partial — pred is substring of gold: `Cathleen Gröneweg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cathleen Gröneweg`(person)
- `Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich`(address)
- `Finanzamtes Klagenfurt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_193`)


Erkenntnis vom 01.April 2019, Zl. ir  Mit diesem Erkenntnis wies das Verwaltungsgericht eine Beschwerde des Finanzamtes  Klagenfurt gegen einen Bescheid der Bezirkshauptmannschaft G, mit dem ein  Verwaltungsstrafverfahren gegen Ä wegen des Verdachtes von Verwaltungsübertretungen  nach dem Arbeitsvertragsrechts – Anpassungsgesetz eingestellt worden ist, ab.

**False Positives:**

- `Finanzamtes  Klagenfurt` — partial — gold is substring of pred: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/141066.1`) (sent_id: `deanon_BFG_20260814_TEST/141066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Hon.-Prof. Dragan Neisemeyer  über die Beschwerde der Haendl Wind GmbH, Parseier 13, 4421 Pieslwang, Österreich, vertreten durch die Puntigam Wirtschaftstreuhand und  Steuerberatung GmbH, Hauptstraße 39, 8093 St. Peter am Ottersbach, vom 29.09.2020 gegen  den Bescheid des Finanzamtes Graz-Umgebung vom 11.03.2020 betreffend Umsatzsteuer 2017  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Haendl Wind Gmb` — partial — pred is substring of gold: `Haendl Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dragan Neisemeyer`(person)
- `Haendl Wind GmbH`(organisation)
- `Parseier 13, 4421 Pieslwang, Österreich`(address)
- `Puntigam Wirtschaftstreuhand und  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz`(organisation)

</details>

---

## `Names with Split Titles (e.g. Univ- Prof.)` 🏆

**F1:** 0.322 | **Precision:** 0.709 | **Recall:** 0.208  

**Format:** `regex`  
**Rule ID:** `de0eb9fb`  
**Description:**
Captures full title and name following legal titles including complex multi-word titles like 'Techn R', 'Univ.-Prof.in', 'Priv.-Doz.in', ensuring the full name is captured even with spaces in titles.

**Content:**
```
(?:Techn\s+R\s+|Techn\.\s*R\s+|Techn\.R\s+|Univ\.-?Prof\.(?:\.in)?\s+|Priv\.-?Doz\.(?:\.in)?\s+|Hon\.-?Prof\.(?:\.in)?\s+|Hon\.-?Prof\.|Dr\.(?:\s+Priv\.-Doz\.)?\s+|Dr\.in\s+|Mag\.(?:\s+Univ\.-Prof\.)?\s+|Mag\.a\s+|Ing\.|Bakk\.(?:\s+iur\.)?\s+|LLM\s+|BSc\s+|RA\.?\s+|StB\.?\s+|Gf-?\s+|\u00d6kR\s+|Dipl\.-Ing\.|RgR\s+|OStR\s+|HR\s+|Fr\.PhD\s+|VetR\s+|DDr\.|LL\.B\.(?:\s+LL\.M\.)?\s+|B\.iur\.(?:\s+r\.\s+nat\.)?\s+|i\.iur\.(?:\s+r\.\s+nat\.)?\s+|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?\s+|LL\.M\.(?:\s+LL\.B\.)?\s+|M\.B\.L\.|LL\.B\.|MBA\s+|MSc\s+|DI\s+|Dipl\.(?:\s+Kff\.)?\s+|StR\s+|KommR\s+|KzlR\s+)([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.709 | 0.208 | 0.322 | 474 | 336 | 138 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 336 | 138 | 1278 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Heinz Neuner` | `Dr. Heinz Neuner` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `N.N.` (person)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |
| `RgR Amalia Schuetzke` | `RgR Amalia Schuetzke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_60`)


Der Beschwerdeführer begründet die berufliche Notwendigkeit der Teilnahme an den  gegenständlichen Kursen mit der Erlangung von Kenntnissen und Fähigkeiten zur Anwendung  Hypnosystemischer Konzepte nach Dr. Gunther Schmidt und von Kommunikationsmethoden,  wie sie im Hypnotherapeutischen Bereich zur Anwendung kämen;

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_67`)


darüber hinaus habe  er sich bereits nach der Teilnahme am ersten von drei Kursen der „Kurzausbildung mit  Dr. Gunther Schmidt – Hypnosystemische Konzepte für Coaching, Team &  Organisationsentwicklung und Supervision“ im Herbst 2018 entschieden, sich im Laufe der Zeit  ein weiteres „Standbein“ aufzubauen, um die erworbenen Kenntnisse als  freiberuflicher/selbständiger Coach anzubieten.

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Mehmet Gessl` | `Dr. Mehmet Gessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donau-Elektro` (organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich` (address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

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
| `Mag. Damian Wiecher` | `Mag. Damian Wiecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow` (person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Gabriele Krafft` | `Dr. Gabriele Krafft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daniel Parys` (person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Li Schukardt` | `Priv.-Doz. Li Schukardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Buchholz` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Corbinian Friemuth` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Guntram Antepoth` (person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `70-875/4351` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_186`)


Sie legte ein Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für Neurologie und  Psychiatrie vor.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_194`)


von der Bf. vorgelegten Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für  Neurologie und Psychiatrie.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Finn van Aken, Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich, vertreten durch Mag. Musa Işlek, Achardgasse 6,  1210 Wien, über die Beschwerde vom 29. Juni 2018 gegen den Bescheid des Finanzamtes Wien  1/23 vom 28. Mai 2018 betreffend Umsatzsteuer 2016 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Dr. Adebiola Bayer` | `Dr. Adebiola Bayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finn van Aken` (person)
- `Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich` (address)
- `Mag. Musa Işlek` (organisation)
- `Finanzamtes Wien  1/23` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Ditzler` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominika Oehlerich, BEd` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Waldemar Faltermeir  in der Beschwerdesache  Elias Kendziorra,  Fernblick 3, 6410 Telfs, Österreich, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid des Finanzamt Waldviertel  vom 22. Mai 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 29-596/0625  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Waldemar Faltermeir` | `Dr. Waldemar Faltermeir` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Kendziorra` (person)
- `Fernblick 3, 6410 Telfs, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `29-596/0625` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_115`)


• Schreiben des Bezirksgerichtes Donaustadt vom 29. Juli 2013 (Verständigung gemäß §  126 AußStrG)  • Psychiatrisches Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9  Dem Ersteller des Gutachtens, Dr. Wolfgang Baischer, Facharzt für Psychiatrie und Neurologie  wurden folgende Befunde vorgelegt:  Psychiatrische Abteilung des SMZ-Ost, Aufenthalt vom 21. Oktober bis 5. November 2012:  "Chronisch-progrediente Encephalitis disseminata mit organischem Psychosyndrom, gemischte  schizoaffektive Störung.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Missed by this rule (FN):**

- `Universität Wien` (organisation)
- `Prof. Maida` (person)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_166`)


Dr. Wolfgang Baischer diagnostizierte beim Bf. im psychiatrischen Gutachten vom 21. Februar  2013 ein organisches Psychosyndrom bei Encephalitis disseminata (Anm.: multiple Sklerose)  und hielt dazu fest, dass diese degenerative neurologische Erkrankung im Sinne einer  Encephalitis disseminata (Multiple Sklerose) beim Untersuchten seit längerer Zeit bekannt sei.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Leonhard Bianchini, Stixendorf 463, 6361 Glantersberg, Österreich,  über die Beschwerde vom 20.03.2018, eingebracht am 22. März 2018, gegen den Bescheid des  Finanzamtes Klagenfurt vom 16.02.2018, zu Steuernummer 13-665/9571, mittels welchem  der Antrag auf Wiederaufnahme der Verfahren betreffend Einkommensteuer für die Jahre  2012 bis 2015 abgewiesen wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helga Woschank` | `Dr. Helga Woschank` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leonhard Bianchini` (person)
- `Stixendorf 463, 6361 Glantersberg, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `13-665/9571` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |
| `Hon.-Prof. Clemens Mooß` | `Hon.-Prof. Clemens Mooß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Burgschweiger` (person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Bernarda Egli, Moosenweg 38, 5630 Harbach, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 8. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernarda Egli` (person)
- `Moosenweg 38, 5630 Harbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Susette Volmari` (person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich` (address)
- `Magistrates der  Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sulamith Hördegen` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ing. Ludwig Taspinar, MA` (person)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |
| `Mag. Monika Schmalzl` | `Mag. Monika Schmalzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |
| `Mag. Thassilo Wedekinn` | `Mag. Thassilo Wedekinn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Dr.in Regina Manegold` | `Dr.in Regina Manegold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in KzlR Helge Erwied` (person)
- `Unterfeichten 5, 4055 Sipbach, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Techn R Volker Nissle, Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 11. Oktober 2016 betreffend Einkommensteuer 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |
| `Techn R Volker Nissle` | `Techn R Volker Nissle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Madeleine Göpffarth` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |
| `Dr. Franz Kandlhofer` | `Dr. Franz Kandlhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Sebastian Pfeiffer, LL.M.` (person)
- `Gerald Cuny-Kreuzer` (person)
- `Christina Tiebout` (person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Ing. Alexandra Ebermaier, MBA` (person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Paolo Reppert  in der Beschwerdesache des  Wendelin Pham, Kremstal Bundesstraße 6, 4682 Thalham, Österreich, über die Beschwerden 1.) vom 17.10.2019 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 15.10.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 sowie  2.) vom 4.5.2020 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3.4.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Paolo Reppert` | `Dr. Paolo Reppert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wendelin Pham` (person)
- `Kremstal Bundesstraße 6, 4682 Thalham, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hugo Pietzak` | `Priv.-Doz. Hugo Pietzak` |
| `Dr. Florens Weißer` | `Dr. Florens Weißer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Straubingerplatz 57, 4691 Römerberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `09-64-114/4837` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Dr.in Esra Schlink` | `Dr.in Esra Schlink` |
| `Dipl. Kff. Sibylle Wahlscheid` | `Dipl. Kff. Sibylle Wahlscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |
| `Mag. Sven Weichmann` | `Mag. Sven Weichmann` |
| `Mag. Kurt Kreith` | `Mag. Kurt Kreith` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_4`)


Die Beschwerdeführerin (Bf.) Dr. Judith Glazer wurde mit Bescheid des Finanzamtes Baden  Mödling vom 20.08.2020 zur Einkommensteuer 2018 veranlagt.

| Predicted | Gold |
|---|---|
| `Dr. Judith Glazer` | `Dr. Judith Glazer` |

**Missed by this rule (FN):**

- `Finanzamtes Baden  Mödling` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |
| `Dr. Christoph Ganahl` | `Dr. Christoph Ganahl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Untermeier` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |
| `Dr. Ashley Nagelschmidt` | `Dr. Ashley Nagelschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hollenbach 37, 4872 Unterthumberg, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `16-165/9893` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Moser` | `Mag. Wolfgang Moser` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Petra Port` (person)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Petra Port` (person)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

| Predicted | Gold |
|---|---|
| `Mag. Wladimir Beheim` | `Mag. Wladimir Beheim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bruno Rüttgers` (person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich` (address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG` (organisation)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Babette Bernett, Schmalzhofen 9, 8250 Riegersbach, Österreich, über die Beschwerde vom 17. September 2020 gegen den  Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt Österreich) vom 4. September  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerdevorentscheidung vom 24. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 wird gemäß § 279 Abs. 1 BAO ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Babette Bernett` (person)
- `Schmalzhofen 9, 8250 Riegersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Daniel Philip Pfau` | `Mag. Daniel Philip Pfau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in Julia Mundle` (person)
- `Leitersdorf 2, 9344 Psein, Österreich` (address)
- `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `23-019/8335` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingrid Dohrmaier` (person)
- `Daläus 14O, 2301 Wittau, Österreich` (address)
- `Korber & Partner WTH-Stb  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Finanzamtes Österreich` (organisation)
- `41-654/1190` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Edwin Teiwes` | `Univ.-Prof. Edwin Teiwes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Francois Distefano` (person)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-092/9347` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Carla Winterkorn, Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich, über die Beschwerde vom 17. April 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 19. März 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer 43-645/1612  zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Carla Winterkorn` (person)
- `Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `43-645/1612` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125219.1`) (sent_id: `deanon_BFG_20260814_TEST/125219.1_176`)


Zudem wurde vom Erstgutachter DI Bodo Meßmacher ausgeführt, dass die Kosten für den Umbau- und Sanierungsarbeiten zur Verwertung des Gebäudeteils in der Pf. von ihm mit 75.000 Euro geschätzt werden.

**False Positives:**

- `DI Bodo Meßmacher` — partial — gold is substring of pred: `Bodo Meßmacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bodo Meßmacher`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Dr. Kurt Bartold` — partial — pred is substring of gold: `Priv.-Doz. Dr. Kurt Bartold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Hemma Ramelow` — partial — pred is substring of gold: `Univ.-Prof.in Dr.in Hemma Ramelow`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_57`)


Sie ging zu KzlR Gregor Scholt, BA einem Chirurg der wollte ihr einen Nadel reinstecken, sie  wurde dort festgehalten.

**False Positives:**

- `KzlR Gregor Scholt` — partial — pred is substring of gold: `KzlR Gregor Scholt, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Gregor Scholt, BA`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

**False Positives:**

- `Mag.a Livia Korowski` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Livia Korowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Livia Korowski`(person)
- `Sven Mitterhuber`(person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

**False Positives:**

- `Mag. Elisabeth Brunner` — partial — pred is substring of gold: `MMag. Elisabeth Brunner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Elisabeth Brunner`(person)
- `Serge Pechert`(person)
- `Texing 43, 3143 Oberloitzenberg, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_111`)


Gutachten erstellt am 31.01.2017 von Dr.in Silvia Bauer  Gutachten vidiert am 31.01.2017 von Dr.in Renate Reininger"

**False Positives:**

- `Dr.in Silvia Bauer  Gutachten` — partial — gold is substring of pred: `Dr.in Silvia Bauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Silvia Bauer`(person)
- `Dr.in Renate Reininger`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)


Wenn der Sachwalter die Einvernahme von Prof. Maida als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der Neurologin Univ.Prof. Dr. Eva Maria Maida im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

**False Positives:**

- `Dr. Eva Maria Maida` — partial — pred is substring of gold: `Neurologin Univ.Prof. Dr. Eva Maria Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)
- `Bundesfinanzgericht`(organisation)
- `Neurologin Univ.Prof. Dr. Eva Maria Maida`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag.a Hilde Heidorn` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Hilde Heidorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `KzlR Helge Erwied` — partial — pred is substring of gold: `Dr.in KzlR Helge Erwied`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Regina Manegold`(person)
- `Dr.in KzlR Helge Erwied`(person)
- `Unterfeichten 5, 4055 Sipbach, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `Dr. Thomas Keppert` — partial — pred is substring of gold: `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Dr. Sebastian Pfeiffer` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer, LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Dr. Sebastian Pfeiffer, LL.M.`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dr. Franz Kandlhofer`(person)
- `Christina Tiebout`(person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich`(address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/132474.1`) (sent_id: `deanon_BFG_20260814_TEST/132474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Violetta Colberg  in der Beschwerdesache KzlR Kurt Bätzgen,  Alte Zeile 11, 4084 Sonnleiten, Österreich, gegen den Bescheid des FAF vom 10. Mai 2013 über die Festsetzung eines  Säumniszuschlages für die Umsatzsteuer 2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Violetta Colberg` — partial — pred is substring of gold: `Hon.-Prof.in Dr.in Violetta Colberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Violetta Colberg`(person)
- `KzlR Kurt Bätzgen`(person)
- `Alte Zeile 11, 4084 Sonnleiten, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/132622.1`) (sent_id: `deanon_BFG_20260814_TEST/132622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache RgR VetR Cassandra Sczech, Hainbuchen 119, 3423 Wördern, Österreich, betreffend Beschwerde vom 22. September 2020 gegen die Bescheide  2015/2016/2017/2018 des Finanzamtes Gänserndorf Mistelbach beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `VetR Cassandra Sczech` — partial — pred is substring of gold: `RgR VetR Cassandra Sczech`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `RgR VetR Cassandra Sczech`(person)
- `Hainbuchen 119, 3423 Wördern, Österreich`(address)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof. Kai Menrath` — partial — pred is substring of gold: `Univ.-Prof. Univ.-Prof. Kai Menrath`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

**False Positives:**

- `Dipl. Kff. Ingrid Klockgiesser` — partial — pred is substring of gold: `VetR Dipl. Kff. Ingrid Klockgiesser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `VetR Dipl. Kff. Ingrid Klockgiesser`(person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

**False Positives:**

- `Mag.a Heidrun Eifeler` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Heidrun Eifeler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler`(person)
- `Esra Luetje`(person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich`(address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

**False Positives:**

- `Dr.in Sieglinde Steinkaemper` — partial — pred is substring of gold: `Hon.-Prof.in Dr.in Sieglinde Steinkaemper`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper`(person)
- `Julian Gruening`(person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Janis Dührkopp`(person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

**False Positives:**

- `Dr. Schwab Wirtschaftstreuhand` — partial — pred is substring of gold: `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Alice Schöpfel`(person)
- `Walter Guggenmoos`(person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich`(address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`(organisation)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt Österreich`(organisation)
- `79-464/0427`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_6`)


Im Zuge der Arbeitnehmerveranlagungen 2011  und 2012 beantragte die Bf. die Berücksichtigung von Aufwendungen für eine Ausbildung zur  Dipl. Body Vitaltrainerin in der Höhe von EUR 7.061,81 (Jahr 2011) und EUR 3.348,18 (Jahr  2012) als Werbungskosten.

**False Positives:**

- `Dipl. Body Vitaltrainerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_8`)


Bei den Aufwendungen für den  Lehrgang zur Dipl. Body Vitaltrainerin handle es sich hierbei um Aufwendungen für  Bildungsmaßnahmen, die auch bei nicht berufstätigen Personen von allgemeinem Interesse  seien oder die grundsätzlich der privaten Lebensführung dienen würden.

**False Positives:**

- `Dipl. Body Vitaltrainerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_12`)


3. Die Bf. bekämpfte diese Bescheide mit Beschwerde vom 17.04.2015 und brachte dazu vor,  dass ihr erlerntes Wissen aus der Weiterbildung zur Dipl. Body Vitaltrainerin regelmäßig in  ihrem Arbeitsbereich auf der Intensivstation angewandt werde.

**False Positives:**

- `Dipl. Body Vitaltrainerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Single Word Names after 'Herrn' or 'Frau'` 🏆

**F1:** 0.045 | **Precision:** 0.603 | **Recall:** 0.024  

**Format:** `regex`  
**Rule ID:** `19a6a077`  
**Description:**
Captures single-word names following 'Herrn' or 'Frau' in contexts where the name is a surname only (e.g., 'Herrn Hus').

**Content:**
```
(?:Herrn|Frau)\s+([A-Z][a-z\u00df]+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.603 | 0.024 | 0.045 | 63 | 38 | 25 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 38 | 25 | 1576 |

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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_60`)


Auch gibt die Tante des Beschwerdeführers,Frau Freßdorf  an, dass sich  mit Beginn des Studiums zunehmend gegenüber seiner Umwelt verschloss und sich immer  4 von 21 Seite 5 von 21

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_63`)


Zur Untersuchung beim Bundessozialamt wurde der Beschwerdeführer von Frau Unverdroß  einer  Betreuerin der Einrichtung, in welcher der Beschwerdeführer betreut wird, begleitet.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Unverdroß` (person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_72`)


Bei der Erstellung des fachärztlichen Sachverständigengutachtens durch das Bundessozialamt  fanden weder der Befund der Stellungskommission noch die Aussagen von Frau Unverdroß  entsprechende Berücksichtigung.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_140`)


In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Der Rechtsanwalt verwies auf die Aufführungen in der Beschwerde sowie auf die beantragten  Zeugen, insbesondere auf die Tante des Beschwerdeführers (Bf.),Frau Freßdorf  die Aussagen zu dem  damaligen Gesundheitszustand des Bf. während seines Studiums treffen könne.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_200`)


Laut Sachwalter habe Frau Freßdorf (Tante des Bf.) erzählt, dass sich ihr Neffe mit Beginn des  Studiums zunehmend gegenüber seiner Umwelt verschlossen und sich immer mehr  zurückgezogen habe, was sich dadurch geäußert habe, dass er keinen Kontakt mit der Familie  haben wollte und auch gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_218`)


Lebensjahr (bzw. dem 25. Lebensjahr) eingetreten ist,  brachte Frau Freßdorf doch nur vor, dass sich ihr Neffe mit Beginn des Studiums zunehmend  gegenüber seiner Umwelt verschlossen und sich immer mehr zurückgezogen habe, was sich  dadurch geäußert habe, dass er keinen Kontakt mit der Familie haben wollte und auch  gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

| Predicted | Gold |
|---|---|
| `Ruckelshaußen` | `Ruckelshaußen` |

**Missed by this rule (FN):**

- `Dimitri Witkoski` (person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_45`)


Nach Antwort von Herrn Ruckelshaußen vom 04.08.2015 betreffend  „asymmetrische Arrondierung und Immo-Est-Befreiung“ kommt im wörtlichen Sinne die  Befreiungsbestimmung des § 30 Abs 2 Z 4 EStG immer für denjenigen zur Anwendung, bei dem  ein Grundstückstausch einen Flurbereinigungsvorgang darstellt. Wenn für einen Tauschpartner  eine Flurbereinigung gegeben ist (und auch ein Tausch und keine Veräußerung vorliegt - dh  keine Aufzahlungen über 50%), dann greift für diesen die Befreiung, wohingegen der andere  Tauschpartner steuerpflichtig ist.

| Predicted | Gold |
|---|---|
| `Ruckelshaußen` | `Ruckelshaußen` |

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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_39`)


Erst ein Telefonat zwischen Magistrat der Stadt Wien und Herrn Bodewein hat ergeben, dass es sich  um beim Anbringen vom 15. September 2021 um eine Beschwerde handeln solle.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_59`)


Für Herrn Bodewein geht hingegen die absolute Unzulässigkeit einer Revision gemäß § 25a Abs. 4  VwGG vor (siehe Rechtsmittelbelehrung).

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_23`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grund- lage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_74`)


So hatte Frau Thyssen erst vor wenigen  Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass der EU-Vertrag  jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grundlage der Nationa- lität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_26`)


Im Vorlageantrag wird ausgeführt:  „Herr B ist nach Angaben meines Mandanten erst im Sommer 2013 nach Österreich gekommen  und war ausschließlich für Herrn Mathusczyk tätig.

| Predicted | Gold |
|---|---|
| `Mathusczyk` | `Mathusczyk` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_47`)


Erst im Einspruch vom 18. März 2024 gegen die beiden Strafverfügungen vom 11. März  2024, GZ. 1) MA67/GZ1/2024 und 2) MA67/GZ2/2024, brachte der Bf. erstmals vor, dass das in  Rede stehende Fahrzeug zur jeweiligen Beanstandungszeit von Herrn Schwent gelenkt wurde.

| Predicted | Gold |
|---|---|
| `Schwent` | `Schwent` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung vom 4. Juni 2024, GZ. MA67/GZ/2024, lastete der Magistrat der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde Frau Manhardt an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 4. April 2024 um  12:24 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien, Helenengasse zwischen  Praterstern und Hedwiggasse rechts, abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_5`)


Demnach habe Frau Manhardt die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_9`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertetungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_39`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_66`)


Nach der Aktenlage wurde der Einspruch gegen die an Frau Manhardt ergangene  Strafverfügung vom Beschwerdeführer erhoben, eine Vollmacht wurde jedoch (trotz  Aufforderung durch die belangte Behörde) nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_21`)


Nach telefonischer Rücksprache mit Frau Lensen füge ich das ganze nochmals als  Anhang hinzu.“

| Predicted | Gold |
|---|---|
| `Lensen` | `Lensen` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_5`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_105`)


ln Ihrer Stellungnahme gaben Sie im Wesentlichen an, dass das Fahrzeug am Morgen dieses  Tages in der STRASSE-Hauptwohnsitz von Herrn Dr. YYY übernommen worden wäre und Ihnen  dieser mitgeteilt hätte, dass er einige Tage nach Ungarn fahren werde.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Prim` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_72`)


Am 26.1.2018 (am Tag danach) seien zwei Poststücke per Einschreiben mit den  Aufgabenummern RQ … 747 und 748 versendet worden, die von Herrn Mag. Sch. auf dem  Nachhauseweg beim Postamt W. aufgegeben worden seien.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Sch.`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_115`)


Es wurden einvernehmlich nicht nur Befunde beurteilt, sondern auch ausführliche persönliche  Gespräche mit Frau Mag. D (Neuropsychologisches Gutachten) und OA. Dr. G (Neuropädiaterin)  geführt.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. G`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_4`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 9. August 2021 wurde über Herrn Dipl.-Ing. Astrid Gänsl  ein  erster Säumniszuschlag (für einen Betrag an Umsatzsteuer 2015 von € 14.970,00) in Höhe von  € 299,40 festgesetzt, da die angeführte Abgabenschuldigkeit nicht bis 15. Februar 2016  entrichtet worden sei.

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Astrid Gänsl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)
- `Dipl.-Ing. Astrid Gänsl`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_35`)


Zusätzlich  sei der Beschwerdeführerin unbedingt empfohlen worden, die OP von Herrn Dr. B einem  anerkannten Schulterspezialisten ausführen zu lassen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_45`)


Als letzter  Versuch hätte sie auf Empfehlungen Herrn Dr. B, einen anerkannten Schulterspezialisten,  aufgesucht, welcher endlich nach einem langen Leidensweg die richtige Diagnose gestellt und  zu einer sofortigen Operation geraten hätte.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_58`)


Die streitgegenständliche Operation wurde schließlich in der Klinik Diakonissen Linz von Herrn  Dr. B durchgeführt (stationärer Aufenthalt von 15.5. bis 20.5.2019).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_56`)


Die von Herrn Ing. Priv.-Doz.in Linda Schleglmilch zu Punkt 4 und 5 gemachten Angaben stellen für die Betriebsprüfung keine  zu akzeptierenden Argumente dar.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. Priv.-Doz.in Linda Schleglmilch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Priv.-Doz.in Linda Schleglmilch`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_19`)


Die Überprüfung der durchgeführten Selbstberechnungen erfolgte dergestalt, als Herrn Dr. F  dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel einen Datenträger zur Verfügung  gestellt hat.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_26`)


Infolge sind von Herrn Dr. F Unterlagen - im Begleitschreiben als Gutachten bezeichnet sowie  Mietverträge - per Mail vorgelegt worden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_105`)


Dagegen erhob die Bf. fristgerecht Beschwerde und brachte unter Anführung der  gegenständlichen Geschäftszahl begründend (wörtlich) vor:  „Betrifft: Milderung der Strafe   Sehr geehrte Herr/Frau Frau,  ich habe Ihr Bescheid erhalten und bin gezwungen um eine Milderung anzusuchen.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_12`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_59`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_116`)


Das telefonische Vor - Aviso dieser Vorgangsweise wurde letzte Woche zwischen Dr. Kohlfürst  und Herrn Amtsdirektor V abgestimmt.

**False Positives:**

- `Amtsdirektor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Kohlfürst`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_14`)


Ziel der Bautätigkeit sei die Schaffung einer gemeinsamen  Wohnung für seine Familie, dh für seine Frau Prof. Engelbert Thuerrigl  verehelichte A, seine Kinder und für ihn  selbst, gewesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Engelbert Thuerrigl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Engelbert Thuerrigl`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)


Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn Jeanne Kraenzlin) getragen wird.

**False Positives:**

- `Jeanne` — partial — pred is substring of gold: `Jeanne Kraenzlin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeanne Kraenzlin`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_31`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_28`)


Im Zuge des Ermittlungsverfahrens wurde festgestellt, dass der aktuelle Hauptwohnsitz von  Herrn Sohn, geb. am 25.gggg.1981, seit 03.bbb.2013 in Adresse_Sohn, ist.“

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_108`)


Im erwähnten Straferkenntnis vom  7.11.2022 hat die belangte Behörde diese Ermittlungsergebnisse auch wiedergegeben und  dazu auszugsweise wie folgt ausgeführt:  „Ermittlungen ergaben, dass für Herrn Rudolf B kein Ausweis gemäß § 29b StVO ausgestellt  wurde.

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_110`)


……  Im Übrigen ist auch der lt. Anzeigeangaben im Fahrzeug nicht gut erkennbar hinter der  Windschutzscheibe eingelegte Parkausweis gemäß § 29b StVO, dessen Ausweisnummer  teilweise durch eine Postkarte verdeckt war, nicht für Herrn Rudolf B ausgestellt.“

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names with 'VetR' and similar standalone titles` 🏆

**F1:** 0.028 | **Precision:** 0.460 | **Recall:** 0.014  

**Format:** `regex`  
**Rule ID:** `e1aefbb2`  
**Description:**
Captures names immediately following specific standalone titles like 'VetR', 'Ing.', 'Bakk.' without requiring 'Herrn/Frau' prefix.

**Content:**
```
(?:VetR|Ing\.|Bakk\.|Dipl\.-Ing\.|RA\.|StB\.|MedR|KommR|OStR|HR|Fr\.PhD|KzlR|Techn\s+R)\s+([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.460 | 0.014 | 0.028 | 50 | 23 | 27 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 27 | 1591 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `MedR Francois Distefano` | `MedR Francois Distefano` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Edwin Teiwes` (person)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-092/9347` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dipl.-Ing. Jeanne Handke, Vornbacherweg 166, 5142 Weinberg, Österreich, über die Beschwerde vom 23. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 21. Juli 2021 betreffend Grunderwerbsteuer, Steuernummer 82-448/5450,  Erfassungsnummer 2017, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Jeanne Handke` | `Dipl.-Ing. Jeanne Handke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vornbacherweg 166, 5142 Weinberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `82-448/5450` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Stephanie Dauben  in der Beschwerdesache MedR Erhard Hauprich,  Wohnpark Ager 97, 8264 Obgrün, Österreich, über die Beschwerde vom 22. Juni 2020 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `MedR Erhard Hauprich` | `MedR Erhard Hauprich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Stephanie Dauben` (person)
- `Wohnpark Ager 97, 8264 Obgrün, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Ing. Nicoletta Papastergios,  Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich  über die Beschwerde vom 12. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 31. März 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 94-528/7027  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ing. Nicoletta Papastergios` | `Ing. Nicoletta Papastergios` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `94-528/7027` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/140490.1`) (sent_id: `deanon_BFG_20260814_TEST/140490.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Dipl.-Ing. Milena Panagiotoglou, KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich, über die Beschwerde vom 11. September 2022  gegen den Bescheid des Finanzamtes Österreich vom 6. September 2022 betreffend  Einkommensteuer 2017 (Arbeitnehmerveranlagung) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Milena Panagiotoglou` | `Dipl.-Ing. Milena Panagiotoglou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_26`)


Der einzige Gesellschafter, Ing. Leonie Veix,  wohnhaft in Polen, war von der Gründung im Jahr 2013 bis zur Löschung gemäß § 40 FBG  infolge Vermögenslosigkeit der Geschäftsführer der Firma.

| Predicted | Gold |
|---|---|
| `Ing. Leonie Veix` | `Ing. Leonie Veix` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vivian Gastell  in der Beschwerdesache Dipl.-Ing. Tosca Toussaint,  Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 25. Mai 2023 betreffend Abweisung des Antrags vom 6. Februar 2023 auf  Erstattung des Mehrkindzuschlages auf Grund der  Verhältnisse des Jahres 2022,  Steuernummer 82-564/6636, SV-Nr. Nr., zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Tosca Toussaint` | `Dipl.-Ing. Tosca Toussaint` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Vivian Gastell` (person)
- `Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `82-564/6636` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Vorsitzenden des Finanzstrafsenates 6008-6  Mag. Johann Fischerlehner in der Finanzstrafsache gegen Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich, wegen  der Finanzvergehen der Abgabenhinterziehungen gemäß § 33 Abs. 2a des Finanzstrafgesetzes  (FinStrG) über die Beschwerden der Beschuldigten vom 22.09.2023 und der Amtsbeauftragten  vom 09.10.2023 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung -  Team als Finanzstrafbehörde vom 14.07.2023 beschlossen:  Das angefochtene Erkenntnis des Spruchsenates vom 14.07.2023, Gz., Team wird gemäß § 161  Abs. 4 FinStrG aufgehoben und die Finanzstrafsache in ihrem gesamten Umfang an die  Finanzstrafbehörde zur neuerlichen Entscheidung zurückverwiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johann Fischerlehner` (person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_3`)


Begründung  Verfahrensgang:  Mit Beschluss des Bezirksgerichtes BG vom TT. Februar 2023 zu Aktenzeichen Az. wurde  betreffend Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  das Schuldenregulierungsverfahren eröffnet und  Dr. Harald POHLHAMMER, Herrenstraße 29/2.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)
- `Dr. Harald POHLHAMMER` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_5`)


Mit Vorladung vom 22. Juni 2023 zur mündlichen Verhandlung am 14.07.2023 um 08:30 Uhr  vor dem Spruchsenat des Amtes für Betrugsbekämpfung - Bereich Finanzstrafsachen - Team als  Finanzstrafbehörde wurde Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  als Beschuldigter geladen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Amtes für Betrugsbekämpfung` (organisation)
- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_7`)


Finanzstrafbehörde wurde die Fa. NB zu Handen Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  als  Nebenbeteiligte geladen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_9`)


Demnach hätte Herr Dipl.-Ing. Heinz Riechels  trotz Aufforderung des Masseverwalters die  Post nicht beim Masseverwalter abgeholt. Beigeschlossen wurden die Vorladung des  Beschuldigten Dipl.-Ing. Heinz Riechels  zur Spruchsenatsverhandlung (RSa Brief) sowie die Vorladung des  Nebenbeteiligten NB zur Spruchsenatsverhandlung (RSa Brief).

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_11`)


Festgehalten wurde, dass bei Aufruf der Sache weder der Beschuldigte Dipl.-Ing. Heinz Riechels  noch der  beschuldigte Verband NB erschienen sind.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_14`)


Der Senatsvorsitzende hat in einem Vorhalt vom 14.3.2025 die belangte Behörde aufgefordert,  binnen von vier Wochen ab Zustellung dieses Schreibens folgende Unterlagen vorzulegen:   Ladung der beschuldigten Parteien zur mündlichen Verhandlung am 14.07.2023 samt  Zustellnachweis   Auszug aus der Insolvenzdatei betreffend Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  Weiters wurde die belangte Behörde aufgefordert folgende Passage in der schriftlichen  Ausfertigung des angefochtenen Staferkenntnisses  (Seite 7) näher zu erläutern:  „Die Zustellung der Ladung ist ausgewiesen durch persönliche Übernahme per 27.06.2023.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_20`)


Unterschrift auf der gegenständlichen Beschwerde:  [...]  Zudem ist auf der Verständigung von der Hinterlegung eine Nachsendeadresse angeführt, die  jener des damaligen Insolvenzverwalters Dr. Pohlhammer des Dipl.-Ing. Heinz Riechels  entspricht.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Dr. Pohlhammer` (person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_22`)


Die Ladungen zur Spruchsenatsverhandlung an den Beschuldigten Dipl.-Ing. Heinz Riechels  und den  nebenbeteiligten Verband NB gingen It. Eingangsstempel auf den RSa Schreiben jeweils am  27. Juni 2023 beim Masseverwalter Dr. Pohlhammer ein.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Dr. Pohlhammer` (person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_23`)


Offensichtlich wurde seitens des Spruchsenats die Tatsache, dass die Zustellung der Ladung zur  Spruchsenatsverhandlung an Dipl.-Ing. Heinz Riechels  nachweislich mittels Nachsendeauftrag an den  Masseverwalter erfolgte (siehe Nachsendeadresse links unten im Zustellnachweis der Ladung  an Dipl.-Ing. Heinz Riechels), nicht berücksichtigt und wurde daher im Glauben, dass die Ladung rechtmäßig  an den Beschuldigten ausgefolgt worden sei und dieser Kenntnis vom Verhandlungstermin  erlangt habe, die Spruchsenatsverhandlung in Abwesenheit des Beschuldigten Dipl.-Ing. Heinz Riechels  durchgeführt.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_24`)


Mit E-Mail vom 19.07.2023 wurde der Spruchsenatsvorsitzende Mag. Lichtenegger über das  Schreiben des Insolvenzverwalters Dr. Pohlhammer betreffend die nicht abgeholten  Spruchsenats-Vorladungen informiert und ihm das Schreiben übermittelt.  Über die Beschwerde wurde erwogen:  Festgestellter Sachverhalt:  Aus den vorgelegten und nunmehr auf Grund des Vorhaltes des Senatsvorsitzenden ergänzten  Akten ergibt sich zweifelsfrei, dass die Ladungen zur mündlichen Verhandlung am 14.07.2023  um 08:30 Uhr vor dem Spruchsenat des Amtes für Betrugsbekämpfung - Bereich  Finanzstrafsachen - Team als Finanzstrafbehörde weder dem Beschuldigten Dipl.-Ing. Heinz Riechels  noch  3 von 5 Seite 4 von 5

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Mag. Lichtenegger` (person)
- `Dr. Pohlhammer` (person)
- `Amtes für Betrugsbekämpfung` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_26`)


Trotz Verfügung der eigenhändigen  Zustellung wurden die Poststücke an den damaligen Masseverwalter des Dipl.-Ing. Heinz Riechels  übermittelt und sind dem Beschuldigten und der Nebenbeteiligten auch tatsächlich nicht  zugekommen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_50`)


Im gegenständlichen Fall hat sich herausgestellt, dass die Ladungen zur mündlichen  Verhandlung am 14.07.2023 um 08:30 Uhr vor dem Spruchsenat des Amtes für  Betrugsbekämpfung - Bereich Finanzstrafsachen - Team als Finanzstrafbehörde weder dem  Beschuldigten Dipl.-Ing. Heinz Riechels  noch dem nebenbeteiligten Verband NB zugestellt wurden.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Amtes für  Betrugsbekämpfung` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

**False Positives:**

- `MedR Constantin Wiedewilt` — partial — pred is substring of gold: `VetR OMedR Constantin Wiedewilt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `VetR OMedR Constantin Wiedewilt`(person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich`(address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Ing. Ludwig Taspinar` — partial — pred is substring of gold: `KommR Ing. Ludwig Taspinar, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `KommR Ing. Ludwig Taspinar, MA`(person)
- `Alt Lenzing 13, 4076 Karling, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

**False Positives:**

- `Ing. Alexandra Ebermaier` — partial — pred is substring of gold: `StR Ing. Alexandra Ebermaier, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `StR Ing. Alexandra Ebermaier, MBA`(person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_8`)


Die Gesellschaftsanteile werden von Dipl. Ing.Ing. Bertram Hennlein und Dipl. Ing. B gehalten.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_9`)


Als  Geschäftsführer fungierte im Streitzeitraum Dipl. Ing.Ing. Bertram Hennlein  Im Zuge einer die Jahre 2015 bis 2019 umfassenden gemeinsamen Prüfung der Lohnabgaben  (GPLA) wurden folgende, nunmehr streitgegenständlichen Feststellungen getroffen:  1 von 17 Seite 2 von 17

**False Positives:**

- `Ing. Bertram Hennlein  Im Zuge` — positional overlap with gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_39`)


Ad Geschäftsführerbezug, Diäten und GSVG-Beiträge  Im Prüfungszeitraum sei Dipl. Ing.Ing. Bertram Hennlein als Geschäftsführer der Beschwerdeführerin und Dipl.  Ing. B als Prokurist tätig gewesen.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_42`)


Dipl. Ing. B sei täglich an den Standorten W sowie Z anwesend gewesen und habe sich operativ  um die Durchführung der Geschäftsführeragenden gekümmert, während Dipl. Ing.Ing. Bertram Hennlein in  diese Tätigkeiten so gut wie gar nicht eingebunden gewesen sei.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_45`)


Dipl. Ing.Ing. Bertram Hennlein sei nur selten an den Bürostandorten körperlich anwesend gewesen und habe  daher organisatorisch gar nicht die Durchführung der originären Tätigkeiten eines  Geschäftsführers übernehmen können.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_46`)


Die Entlohnung des Dipl. Ing.Ing. Bertram Hennlein betreffe daher  ausschließlich seine Tätigkeit für die oben angeführten Projekte, für die Grenzverhandlungen  und als Sachverständiger.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_57`)


Die operativen Tätigkeiten des Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein hätten in der  Abwicklung der Projekte, in Grenzverhandlungen und im Tätigwerden als Sachverständiger  bestanden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_60`)


In den Jahren 2014-2020 seien auch alle Jahresabschlüsse vom alleinigen  Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein unterzeichnet worden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_88`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.1. Bezüge des wesentlich beteiligten Gesellschafter-Geschäftsführers  Dipl. Ing.Ing. Bertram Hennlein ist zu 90% an der beschwerdeführenden Gesellschaft beteiligt und vertritt diese  seit 19.11.2010 selbständig als ihr Geschäftsführer.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing.Ing. Bertram Hennlein`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_91`)


Insgesamt flossen ihm in den  Streitjahren folgende Beträge zu:  2015 2016 2017 2018 2019  26.447,13 € 37.786,37 € 36.058,96 € 52.441,49 € 54.658,22 €  Dipl. Ing.Ing. Bertram Hennlein war für die Beschwerdeführerin einerseits als Sachverständiger tätig und  andererseits mit der Abwicklung des Projektgeschäftes (z.B. Semmering Basistunnel,  Bosrucktunnel, Sensorik-Anwendungen bei der ÖBB und ASFINAG) betraut.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)
- `ÖBB`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

**False Positives:**

- `MedR Milena Piechulik` — partial — pred is substring of gold: `OMedR Milena Piechulik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Brendon Spade`(person)
- `OMedR Milena Piechulik`(person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich`(address)
- `Walther Kendler`(person)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `16-827/1246`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140416.1`) (sent_id: `deanon_BFG_20260814_TEST/140416.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache OMedR Frauke Klutzuweit, Weberkogelstraße 114, 8632 Weichselboden, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 23. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 18. Februar 2021 betreffend Feststellung der Einkünfte § 188 BAO 2019 zu  Steuernummer 50-666/0525  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `MedR Frauke Klutzuweit` — partial — pred is substring of gold: `OMedR Frauke Klutzuweit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Frauke Klutzuweit`(person)
- `Weberkogelstraße 114, 8632 Weichselboden, Österreich`(address)
- `N & N Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `50-666/0525`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142258.1`) (sent_id: `deanon_BFG_20260814_TEST/142258.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache ÖkR OMedR Gregor Lauerhaas, Riegerl 15, 4343 Hofstetten, Österreich, betreffend Beschwerde vom 16. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 14. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021,   Steuernummer 51-218/3095, beschlossen:  Der Vorlageantrag vom 21. September 2023 wird gemäß 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO zurückgewiesen.

**False Positives:**

- `MedR Gregor Lauerhaas` — partial — pred is substring of gold: `ÖkR OMedR Gregor Lauerhaas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `ÖkR OMedR Gregor Lauerhaas`(person)
- `Riegerl 15, 4343 Hofstetten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `51-218/3095`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/142817.1`) (sent_id: `deanon_BFG_20260814_TEST/142817.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Blasina, die Richterin  Mag. Monika Ahorn sowie die fachkundigen Laienrichter Gerald Cuny-Kreuzer und Dipl. Ing.  Thomas Hrdinka in der Beschwerdesache Fabian Kohnke, Hammersdorfstraße 78, 4223 Lungitz, Österreich, vertreten durch Intercura  Treuhand- und Revisionsgesellschaft m.b.H., Bösendorferstraße 2, 1010 Wien, über die  Beschwerde vom 14. Dezember 2018 gegen die Bescheide des Finanzamtes Wien 1/23 vom  16. November 2018 betreffend Haftung Lohnsteuer, Festsetzung Dienstgeberbeitrag und  Zuschlag zum Dienstgeberbeitrag sowie Säumniszuschläge jeweils 2015 bis 2017  (Steuernummer 14-263/3594 ) nach Durchführung einer mündlichen Verhandlung am  21. November 2023 in Anwesenheit der Schriftführerin Asli Özdemir zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing.  Thomas Hrdinka` — partial — pred is substring of gold: `Dipl. Ing.  Thomas Hrdinka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Mag. Monika Ahorn`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dipl. Ing.  Thomas Hrdinka`(person)
- `Fabian Kohnke`(person)
- `Hammersdorfstraße 78, 4223 Lungitz, Österreich`(address)
- `Intercura  Treuhand- und Revisionsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `14-263/3594`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Rupert Wedell  in der Beschwerdesache OStR OMedR Rebecca Ehrmanntraut,  Museumplatz 27, 8241 Rohrbachschlag, Österreich, über die Beschwerden vom 10. Oktober 2017 gegen die Bescheide des  FA Baden Mödling  vom 27. Juni 2017 bzw. 10. Juli 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 bis 2015, Steuernummer 38-848/8801, zu Recht erkannt:  I. Den Beschwerden gegen die Bescheide betreffend Einkommensteuer für die Jahre 2012 bis  2015 wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `MedR Rebecca Ehrmanntraut` — partial — pred is substring of gold: `OStR OMedR Rebecca Ehrmanntraut`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Rupert Wedell`(person)
- `OStR OMedR Rebecca Ehrmanntraut`(person)
- `Museumplatz 27, 8241 Rohrbachschlag, Österreich`(address)
- `FA Baden Mödling`(organisation)
- `38-848/8801`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/143519.1`) (sent_id: `deanon_BFG_20260814_TEST/143519.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Jeannine Gondrom  betreffend den Antrag des OMedR Simon Pavlicsek, Fulateia 364, 9562 Spitzenbichl, Österreich,   auf Gewährung der Verfahrenshilfe gemäß § 292 BAO im Beschwerdeverfahren zum Bescheid  des Finanzamt Graz-Stadt  vom 06.06.2023 hinsichtlich Rückforderung von Kinderabsetzbetrag und  Familienbeihilfe für vier Kinder für den Zeitraum 09.2020 – 07.2022  beschlossen:  Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `MedR Simon Pavlicsek` — partial — pred is substring of gold: `OMedR Simon Pavlicsek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Jeannine Gondrom`(person)
- `OMedR Simon Pavlicsek`(person)
- `Fulateia 364, 9562 Spitzenbichl, Österreich`(address)
- `Finanzamt Graz-Stadt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Wolfgang  Weichselbraun` — partial — pred is substring of gold: `Dipl.Ing. Wolfgang  Weichselbraun`

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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/145343.1`) (sent_id: `deanon_BFG_20260814_TEST/145343.1_2`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_204`)


0 OMedR Emilia Kusmierz akupunktur 10 Fahrten bodenst FK 151,20  Ansicht FA:  Das Finanzamt beantragte nach Diskussion um die Führung der Fahrstrecke und die Länge der  einfachen Fahrtstrecke die Stattgabe.

**False Positives:**

- `MedR Emilia Kusmierz` — partial — pred is substring of gold: `OMedR Emilia Kusmierz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Emilia Kusmierz`(person)
- `Finanzamt`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_295`)


28.6.24.7 0,00 OMedR Emilia Kusmierz lOx Akupunktur zus.

**False Positives:**

- `MedR Emilia Kusmierz` — partial — pred is substring of gold: `OMedR Emilia Kusmierz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Emilia Kusmierz`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_323`)


maps eine Fahrtstrecke  von 65 km in Ansatz gebracht (wie schon die Fahrt zu OMedR Emilia Kusmierz.

**False Positives:**

- `MedR Emilia Kusmierz` — partial — pred is substring of gold: `OMedR Emilia Kusmierz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Emilia Kusmierz`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/146580.1`) (sent_id: `deanon_BFG_20260814_TEST/146580.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mikolaj Wegen  in der Beschwerdesache StR MedR Zeno Direk,  Alpenlandhof 5, 3124 Wetzlarn, Österreich, über die Beschwerde vom 28. November 2024 gegen den Bescheid des  Finanzamtes Österreich vom 15. November 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 18-441/3089  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `MedR Zeno Direk` — partial — pred is substring of gold: `StR MedR Zeno Direk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mikolaj Wegen`(person)
- `StR MedR Zeno Direk`(person)
- `Alpenlandhof 5, 3124 Wetzlarn, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `18-441/3089`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/147392.1`) (sent_id: `deanon_BFG_20260814_TEST/147392.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Sonja Stradner in der Beschwerdesache  MedR Silke Sommerbauer, MSc, TAL-Schieberstation 2, 2170 Wetzelsdorf, Österreich, vertreten durch GOBBS Steuer- und Unternehmensberatungs- GmbH,  Schubertstraße 3, 2100 Korneuburg, und FAS Network GmbH, Schubertstraße 3, 2100  Korneuburg, über die Beschwerde vom 8. April 2021 gegen den Haftungsbescheid des  Finanzamtes Österreich vom 19. Februar 2021 betreffend Lohnsteuer 2016, Steuernummer  72-745/5137, zu Recht erkannt:   I. Die Beschwerde gegen den Haftungsbescheid betreffend Lohnsteuer 2016 wird gemäß  § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `MedR Silke Sommerbauer` — partial — pred is substring of gold: `MedR Silke Sommerbauer, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Sonja Stradner`(person)
- `MedR Silke Sommerbauer, MSc`(person)
- `TAL-Schieberstation 2, 2170 Wetzelsdorf, Österreich`(address)
- `GOBBS Steuer- und Unternehmensberatungs- GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `72-745/5137`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/147392.1`) (sent_id: `deanon_BFG_20260814_TEST/147392.1_9`)


Dagegen brachte die MedR Silke Sommerbauer, MSc.

**False Positives:**

- `MedR Silke Sommerbauer` — partial — pred is substring of gold: `MedR Silke Sommerbauer, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MedR Silke Sommerbauer, MSc`(person)

</details>

---

## `Names after 'von' (General Context)` 

**F1:** 0.002 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `48220079`  
**Description:**
Captures the name following 'von' in broader legal contexts, handling split titles and ensuring full name capture.

**Content:**
```
(?:Befunden|Gutachten|Stellungnahme|Aussage|Schreiben|Einspruch|Antrag|Ansuchen|E-Mail|Mail|Bescheinigung|Bescheid|Verf\u00fcgung|Urteil|Entscheidung|Klage|Rechtsmittel|Vertretung|Anwalt|Rechtsanwalt|Notar|Gericht|Beh\u00f6rde|Amt|Finanzamt|Magistrat|Bundesfinanzgericht|Verwaltungsgericht|Verwaltungsstrafbeh\u00f6rde|VfGH|OGH|VwGH|BFG|Online\s+Wettprodukt|Liegenschaft|Zeitraum|Angaben|des|der)\s+(?:von\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn\s+R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.002 | 6 | 2 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 4 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_116`)


Laut vorgelegtem Gutachten von Nicola Peterhansel  Fachärztin für Psychiatrie, vom 7. Jänner 2019, leidet  der Bf. an einer Intelligenzminderung mit einer ausgeprägten Lese- und Rechenschwäche und  kann auf Grund des vorliegenden Krankheitsbildes weder Vertragsinhalte richtig erfassen,  11 von 13 Seite 12 von 13

| Predicted | Gold |
|---|---|
| `Nicola Peterhansel` | `Nicola Peterhansel` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_17`)


In der Folge wies der Magistrat der Stadt Wien den Einspruch von Pjotr Niessl  vom  10. September 2024 gegen die an M als Beschuldigten gerichtete Strafverfügung vom  3. September 2024 mit Bescheid vom 7. März 2025 gemäß § 13 Abs. 3 Allgemeines  Verwaltungsverfahrensgesetz 1991 (AVG) iVm § 24 Verwaltungsstrafgesetz 1991 (VStG) mit der  Begründung zurück, dass Pjotr Niessl  mit Schreiben vom 10. September 2024 im eigenen  Namen gegen die an M gerichtete Strafverfügung Einspruch erhoben habe.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_20`)


Nach den Angaben von Herrn Dr. F sollten auf diesem Datenträger alle notwendigen  Unterlagen gespeichert sein, welche für die ordnungsgemäße Selbstberechnung notwendig  gewesen sind (siehe dazu auch die Ausführungen in der Einleitung).

**False Positives:**

- `Herrn Dr` — positional overlap with gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_277`)


Die Angaben von Herrn Baumeister Y X werden nicht zur Sachverhaltsfeststellung  herangezogen, weil sie nach der hier vertretenen Auffassung nicht relevant sind und jedenfalls  unzuverlässig sind, wie auch im Detail in Abschnitt 14 dargestellt wird.

**False Positives:**

- `Herrn Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names after 'Bf,' (Comma separated)` 💣

**F1:** 0.001 | **Precision:** 0.012 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `8fd8f42b`  
**Description:**
Captures full title and name immediately following 'Bf,' or 'Bf.', handling missing spaces and ensuring valid name structure.

**Content:**
```
Bf[.,]\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s+|\s+r\.\s+nat\.)?|i\.iur\.(?:\s+|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s+|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)*(?:\s+(?:LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|BSc)?)?(?=\s|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.012 | 0.001 | 0.001 | 82 | 1 | 81 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 81 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_32`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf, Heidemarie Fitzenreiter (geboren am 5. März 1970), hat im November 2020  das 18.

| Predicted | Gold |
|---|---|
| `Heidemarie Fitzenreiter` | `Heidemarie Fitzenreiter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `5. März 1970` (date)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_27`)


Außerdem sei auf die persönlichen Verhältnisse und auf die wirtschaftliche Leistungsfähigkeit des Bf. Bedacht genommen (§ 23 Abs. 3 FinStrG) worden.

**False Positives:**

- `Bedacht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_17`)


Dagegen erhob die Bf. Beschwerde beim VwGH (Ra 2018/15/0121).

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_8`)


Mit Schriftsatz vom 23.4.2018, Postaufgabedatum laut Poststempel 24.4.2018, erhob der Bf.  Beschwerde gegen diesen Feststellungsbescheid.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_9`)


Dagegen erhob die Bf. Beschwerde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_115`)


Hinsichtlich der Rechnungen Nr. 005/16, Nr. 007/16 und Nr. 017/16, welche für  Generalplanerleistungen im Zusammenhang mit dem Neubau des Wohnheims ausgestellt  wurden, legte die Bf. Unterlagen vor, aus denen sich sowohl ergibt, dass die  Generalplanerleistungen von einem umsatzsteuerpflichtigen Unternehmer erbracht wurden,  als auch, dass die Bf. seit der Fertigstellung des Wohnheims deren einzelnen Einheiten mit  einer Größe von 24,70 m² bis 80,28 m² um EUR 317,96 bis EUR 809,45 netto pro Monat  zuzüglich Betriebskosten vermietet.

**False Positives:**

- `Unterlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_229`)


Nach dem Dafürhalten des BFG bedürfte es zwecks diesbezüglich konkreter Feststellungen  wohl der Bekanntgabe aller erforderlichen Daten durch den Bf. Bislang wurden seinerseits  lediglich die Aufzeichnungen über die "Heimfahrten Ö-D-Ö" zur Vorlage gebracht, woraus ua.  lediglich zu erahnen ist, dass es sich hiebei um Fahrten von A/XX nach D/XX und retour handeln  wird.

**False Positives:**

- `Bislang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_170`)


Damit kam es aber erst im Jahr  2013 zum Zufluss des Veräußerungspreises an den Bf.   Somit können die neu hervorgekommenen Tatsachen, die vom Finanzamt als  Wiederaufnahmsgründe herangezogen wurden, nicht zu einem geänderten  Einkommensteuerbescheid für 2012 führen.

**False Positives:**

- `Somit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_22`)


Gegen die Strafverfügung erhob der Bf. Einspruch und erklärte, das Schreiben vom 12.3.2019  nach Rückkehr von seinem Auslandsaufenthalt vorgefunden zu haben.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_134`)


Mit E-Mail vom 20.11.2019 brachte der Bf. Beschwerde gegen das Straferkenntnis ein,  beantragte die Durchführung einer mündlichen Verhandlung, die Aufhebung des  9 von 28 Seite 10 von 28

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_33`)


Die Revision der Bf. richtete sich gegen die Anwendbarkeit des § 25 Abs. 1 Z 1 lit b EStG 1988  auf die Tätigkeit der vier, nicht als Geschäftsführer tätigen, nicht wesentlich beteiligten,  Gesellschafter der Bf.  Gegen die Einbeziehung der Honorare der Gesellschafter-Geschäftsführerin in die  Bemessungsgrundlagen für den Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag und  Festsetzung der lohnabhängigen Abgaben für die Jahre 2010 – 2013 wurden keine Vorbringen  erstattet.

**False Positives:**

- `Gegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_22`)


Mit Schreiben vom 14. Februar 2020 und 21. Februar 2020 wurden dem Bf. Ablichtungen  von 3 am Tattag zur Tatzeit vom Meldungsleger aufgenommene Fotos gesandt.

**False Positives:**

- `Ablichtungen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_86`)


II. Das Bundesfinanzgericht hat erwogen:  Betreffend das Jahr 2016 erklärte der Bf. Folgendes (Abgabeninformationssystemabfragen):  Gesamtbetrag der Bemessungsgrundlagen des Veranlagungszeitraumes 2016 für Lieferungen  und sonstige Leistungen (ohne den nachstehend angeführten Eigenverbrauch) einschließlich  Anzahlungen (jeweils ohne Umsatzsteuer) … 0,00 €  Beilage: Ich bitte zukünftig um Beachtung, dass mir keinerlei Wohnungen mit  Umsatzsteuerpflicht unterliegen.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_88`)


1 Fahrt (deutscher Wohnsitz) (Wohnung in Wien) 740 km (und retour 740 km) á Pauschale  0,42 € 621,60 €, Maut / 10 Tages-Vignette 8,80 €  Verpflegungsmehraufwand 48,00 €, Übernachtungspauschale 104,00 € Anreise/Abreise  Portokosten 3,60 €, Telefonkosten 20,00 €  Betreffend das Jahr 2017 erklärte der Bf. Folgendes (Abgabeninformationssystemabfragen):  Gesamtbetrag der Bemessungsgrundlagen des Veranlagungszeitraumes 2017 für Lieferungen  und sonstige Leistungen (ohne den nachstehend angeführten Eigenverbrauch) einschließlich  Anzahlungen (jeweils ohne Umsatzsteuer) … 17.280,00 €  Einkünfte aus Vermietung und Verpachtung … -773.72 €.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_89`)


Betreffend das Jahr 2018 erklärte der Bf. Folgendes (Abgabeninformationssystemabfragen):   Gesamtbetrag der Bemessungsgrundlagen des Veranlagungszeitraumes 2018 für Lieferungen  und sonstige Leistungen (ohne den nachstehend angeführten Eigenverbrauch) einschließlich  Anzahlungen (jeweils ohne Umsatzsteuer) … 17.400,00 € *  Davon steuerfrei OHNE Vorsteuerabzug gemäß  a) § 6 Abs. 1 Z 9 lit. a (Grundstücksumsätze) -17.400,00 €  * Kaltmiete 1.200,00 € x 12 + Betriebskosten 250,00 € x 12 = 17.400,00 €  Einkünfte aus Vermietung und Verpachtung … 3.190,09 €  Einnahmen/Werbungskosten-Überschussrechnung:  Hausgeld/Garage 4.184,62, Abschreibung 8.936,56 €, BKA 282,73 €,  Werbungskosten 806,00 € *  * ident der Werbungskostenposition dieses Betrages im Jahr 2016  Gemäß § 6 Abs. 1 Z 27 UStG 1994 sind die Umsätze der Kleinunternehmer steuerfrei.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_97`)


Eine vom Meldungsleger erstellte Fotografie zeigt zum Teil den  Schriftzug „Firma“ an der Gebäudefassade und davor das abgestellte, beanstandete Kfz des Bf.  Daraus geht klar hervor, dass das besagte Kfz in jenem Abschnitt abgestellt wurde, der der  Guglgasse ONr. 1 zuzuordnen war.

**False Positives:**

- `Daraus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_116`)


Selbst bei  Unklarheit hätte der Bf. Erkundigungen einholen und bis zur Klärung  für die ordnungsgemäße  Entwertung von Parkscheinen sorgen müssen.

**False Positives:**

- `Erkundigungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_251`)


GF. 27/11: Ein österreichischer Unternehmer erbringt eine sonstige Leistung an einen  Dienstnehmer der Bf.  Rechtliche Beurteilung: Die Bf. ist nicht Leistungsempfänger und daher nicht zum  Vorsteuerabzug berechtigt.

**False Positives:**

- `Rechtliche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_27`)


In der Abgabenerklärung für 2019 setzte der Bf. Kosten der doppelten Haushaltsführung iHv.  € 4.575,72 an.

**False Positives:**

- `Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_21`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf, To (geb. am 1998), vollendete am 2016 das 18.

**False Positives:**

- `To` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_10`)


Mit Schriftsatz vom 22. März 2020 brachte der Bf. Beschwerde ein.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_45`)


Die Tochter des Bf, Frau (…), vollendete im Jahr 2014 bereits ihr 23.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_179`)


Damit liege die Haftung und das wirtschaftliche Risiko bei der Bf.  Weder die vertraglichen Grundlagen bzw. Abrechnungen noch die Aussagen bei den  Einvernahmen sprechen dafür, dass von den AN eigenständige und gewährleistungsfähige  Werke erbracht worden wären.

**False Positives:**

- `Weder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_31`)


Da sich der einzige Wohnsitz des Bf. im Jahr 2014 in Österreich befunden habe, habe  Österreich gem. Art. 4 Abs. 1 des Doppelbesteuerungsabkommens Österreich/Deutschland als  Ansässigkeitsstaat das Besteuerungsrecht auf das gesamte Welteinkommen des Bf.  Deutschland habe als Tätigkeitsstaat gem. Art. 15 Abs. 1 DBA Österreich/Deutschland anhand  der lokalen Auslegung des Arbeitnehmerbegriffes das Besteuerungsrecht auf die Einkünfte,  welche die Arbeitstage in Deutschland beträfen.

**False Positives:**

- `Deutschland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_18`)


Die Erstattungsverordnung komme folglich zur Anwendung, weshalb die Bf. Anspruch auf  Erstattung der an die inländischen Provider bezahlten Vorsteuern in voller Höhe habe.

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_60`)


Dieser Sachverhalt ergibt sich aus dem vorgelegten Verwaltungsakt und dem Vorbringen der  Bf.  Rechtsgrundlagen - Rechtliche Würdigung:  Gemäß § 1 Wiener Parkometerabgabeverordnung ist für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen (§ 25 StVO) eine Abgabe zu entrichten.

**False Positives:**

- `Rechtsgrundlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_474`)


Dass im gegenständlichen Besteuerungszeitraum von der Bf. Sportwetten und Ausspielungen  veranstaltet wurden, an der (auch) Spieler teilnahmen, die sich - körperlich – im Inland  aufhielten, wird auch von der Bf. nicht bestritten.

**False Positives:**

- `Sportwetten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_533`)


Die Bf. hat ihren Sitz in Gibraltar und besteht deshalb eine erhöhte  Mitwirkungspflicht der Bf.  Der Bf. war bekannt, dass das Finanzamt auf Grund des -nach der oa.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_563`)


3. Zu den unionsrechtlichen Einwänden der Bf.   Nach Artikel 267 AEUV entscheidet der EuGH im Wege der Vorabentscheidung über die  Auslegung der Verträge sowie über die Gültigkeit und die Auslegung der Handlungen der  Organe, Einrichtungen oder sonstigen Stellen der Union.

**False Positives:**

- `Nach Artikel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_614`)


Andernfalls ist der um den geltend gemachten Rabatt verminderte Einsatz in  Ansatz zu bringen.“  4.2 Ausgestaltung der BONI der Bf.  Es ist somit für die Frage der Einbeziehung der „Boni“ in die Bemessungsgrundlage die  jeweilige konkrete Ausgestaltung der Boni relevant.

**False Positives:**

- `Es` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/136107.1`) (sent_id: `deanon_BFG_20260814_TEST/136107.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über die Beschwerde  vom 17. September 2020 des Beschwerdeführers Klarissa Fuhljahn, Adr Bf, Steuernummer  21-178/1143, vertreten durch den mit Zustellvollmacht ausgewiesenen Martin Friedl, 4650  Lambach, Marktplatz 2 gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr (nunmehr  Finanzamt Österreich) vom 17. August 2020 betreffend Haftung für Lohnsteuer 2012 – 2017  sowie Festsetzung von Dienstgeberbeiträgen und Festsetzung von Zuschlägen zu den  Dienstgeberbeiträgen für die Jahre 2011 – 2017:  I)

**False Positives:**

- `Steuernummer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Klarissa Fuhljahn`(person)
- `21-178/1143`(tax_number)
- `Martin Friedl`(person)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_22`)


Weder in den Beschwerden noch in den Vorlageanträgen oder infolge des Schreibens des BFG  vom 2.3.2022 brachte der Bf. Argumente vor, dass ihm die Einkommensteuerbescheide 2017  und 2018 nicht rechtzeitig zugegangen seien bzw. er einen Verzicht auf die elektronische Form  der Zustellung nicht abgegeben habe.

**False Positives:**

- `Argumente` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_114`)


Zufolge der Bestätigung der Familienkasse Bauern-Süd bezog Betreuerin für den Bf. Kindergeld  in Deutschland und wurde dieses ab dem Monat April 2020 gemäß § 70 Abs. 2 dEStG  aufgehoben.

**False Positives:**

- `Kindergeld ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138698.1`) (sent_id: `deanon_BFG_20260814_TEST/138698.1_8`)


Rahmen eines Antrages nach § 295a BA0 die Kosten nachträglich berücksichtigt werden - siehe  dazu auch LStR 2002 Rz 385" (BFG-Akt AS 34 ff)  Mit Schreiben vom 20. Februar 2020 erhob die Bf. Beschwerde.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_701`)


Wohnung W 2 durch die Gattin des Bf. Zugleich wurde die Privatnutzung der Wohnung  eingeräumt.

**False Positives:**

- `Zugleich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_55`)


Mit Schreiben vom 21. Dezember 2020 teilte die Bf. Folgendes mit:   … ich kann ihnen nun den Ambulanzbefund des Landesklinikum Baden-Mödling zukommen  lassen.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_7`)


Mit Eingabe vom 5. Juni 2020 erhob der Bf. Beschwerde, in der er im Wesentlichen vorbringt,  die Indexierung der steuerlichen Begünstigungen sei diskriminierend und unionsrechtswidrig.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_23`)


Vienna GmbH sowie zwei von Frau an die Bf. gerichtete Schreiben vom 23.5.2017 und vom  10.8.2017 in denen diese bestätigt, von der Bf. Euro 13.000,00 und Euro 998,00 für die  Zahlungen der Modul University für das „2nd, 3rd und 4th Installment“ sowie für das „4th  Installment“ in bar erhalten zu haben, bei.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_213`)


Nachdem der Schwiegersohn des Bf, Hr. GM, in Österreich nie einen Wohnsitz oder Sitz hatte,  wäre es die Aufgabe des Bf gewesen, bei der Aufklärung mitzuwirken.

**False Positives:**

- `Hr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_416`)


Darin hat der Bf. Erwiderungen  und ergänzendes Vorbringen zu den Ausführungen in der Niederschrift vom 7.9.2015 getätigt,  26 von 33 Seite 27 von 33

**False Positives:**

- `Erwiderungen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/140125.1`) (sent_id: `deanon_BFG_20260814_TEST/140125.1_29`)


Wegen  Verletzung der Rechtsvorschriften des § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz wurden  über den Bf. Geldstrafen von je 60,00 € und für den Fall der Uneinbringlichkeit  Ersatzfreiheitsstrafen von je 14 Stunden verhängt.

**False Positives:**

- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/140320.1`) (sent_id: `deanon_BFG_20260814_TEST/140320.1_17`)


Beweiswürdigung:  Die getroffenen Feststellungen ergeben sich zweifelsfrei aus dem Steuerakt des Bf.  Die Feststellung, dass der Bf am 21.10.2022 den Einkommensteuerbescheid ausgelesen hat,  war aufgrund einer Mitteilung der Verfahrensbetreuung des Finanzamtes Österreich zu treffen.

**False Positives:**

- `Die Feststellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/140588.1`) (sent_id: `deanon_BFG_20260814_TEST/140588.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Lerchenfelderstraße 9, 4230 Burbach, Österreich, über die Beschwerde vom 16. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Anspruchszinsen (§ 205  BAO) 2015, Steuernummer 87-149/1701, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Lerchenfelderstraße` — partial — pred is substring of gold: `Lerchenfelderstraße 9, 4230 Burbach, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Lerchenfelderstraße 9, 4230 Burbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `87-149/1701`(tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_127`)


Auch mit dem Vorbringen in der Beschwerde vom 28. September 2021, wonach bereits im  Februar 2020 der Prüfungsabteilung mitgeteilt worden sei, der Bf. sei niemals im Service tätig  gewesen, habe über keinen Kellnerschlüssel verfügt, habe sich aufgrund eines Traktorunfalles  im August 2016 bis Mai 2017 im Krankenhaus befunden und sei danach an den Rollstuhl  gefesselt gewesen und habe sich erst später nur mühsam mit Krücken fortbewegen können,  und daher auszuschließen sei, dass dem Bf. Geldmittel zugeflossen seien, hat sich das  Finanzamt in der Beschwerdevorentscheidung vom 01.09.2022 nicht auseinandergesetzt.

**False Positives:**

- `Geldmittel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_129`)


Feststellungen und konkrete Ermittlungen dahingehend, ob bzw. in welcher Höhe dem Bf.  Geldmittel aus den Kalkulationsdifferenzen unter Mitberücksichtigung der seitens der  steuerlichen Vertretung aufgezeigten Einwände, wurden vom Finanzamt nicht getroffen.

**False Positives:**

- `Geldmittel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_157`)


Im Erkenntnis vom 28.05.2018, RV/7101269/2018, erwog das BFG: Im Zeitraum Juni 2011 bis  September 2011 bezog der Sohn der Bf. Arbeitslosengeld.

**False Positives:**

- `Arbeitslosengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/141354.1`) (sent_id: `deanon_BFG_20260814_TEST/141354.1_208`)


Selbst wenn man  dem Begehren des Bf. Folge gegeben hätte, wäre nicht ausgeschlossen, dass er im Laufe der  Jahre (bedeutend) mehr als die tatsächlichen ursprünglichen Anschaffungskosten abschreibt.

**False Positives:**

- `Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/141355.1`) (sent_id: `deanon_BFG_20260814_TEST/141355.1_205`)


dem Begehren des Bf. Folge gegeben hätte, wäre nicht ausgeschlossen, dass er im Laufe der  Jahre (bedeutend) mehr als die tatsächlichen ursprünglichen Anschaffungskosten abschreibt.

**False Positives:**

- `Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/141572.1`) (sent_id: `deanon_BFG_20260814_TEST/141572.1_46`)


8. Gegen die Beschwerdeentscheidung des BFG vom 16.4.2019, RV/1101048/2015, erhoben  sowohl das Finanzamt als auch der Bf. Revisionen an den Verwaltungsgerichtshof.

**False Positives:**

- `Revisionen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `Finanzamt`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_59`)


Nachdem eine für Dienstverhältnisse erforderliche Kontrollunterworfenheit oder  wirtschaftliche Abhängigkeit nicht gegeben und die Weisungsgebundenheit auf Grund des  vereinbarten und gelebten Vertragsverhältnisses nicht gegeben sei, diese sogar explizit  ausgeschlossen ist, könne ein Dienstverhältnis im Sinne des EStG keinesfalls vorliegen, so die  Bf.   Und weiter: „Der GPLA-Prüfer und die Finanzbehörde gehen davon aus, dass während der  oben genannten Zeit, in welcher Herr NR auch als Geschäftsführer im Firmenbuch eingetragen  war, dessen Bezüge zwingend als solche gem. § 22 Z 2 zweiter Teilstrich EStG anzusehen seien.

**False Positives:**

- `Und` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_43`)


Mit weiterem Schriftsatz vom 02.11.2023 erhob die Bf. Einwendungen gemäß § 87 Abs. 6 BAO  gegen das Protokoll über den Erörterungstermin und führte zur darin festgehaltenen  Außerstreitstellung im Zusammenhang mit der Überschreitung der „2%-Marge“ aus, dass sich  diese auf das Verhältnis zwischen den unter ein und derselben Projektnummer verbuchten  3 von 23 Seite 4 von 23

**False Positives:**

- `Einwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/143262.1`) (sent_id: `deanon_BFG_20260814_TEST/143262.1_7`)


Zudem  habe er am 1.7.2022 weitere 7.703 € an das FA mit Verrechnungsweisung für die ESt-VZ 2021  überwiesen (siehe Abgabenkonto des Bf, Buchungstag 5.7.2022).

**False Positives:**

- `Buchungstag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_320`)


Wir ergänzen im Folgenden die im Ermittlungsbericht des Finanzamtes auf Seite 4 von 5  enthaltene Aufstellung der steuerlichen Jahresergebnisse der Bf.   Laut Erstbescheid/Erklärung Kumuliertes Ergebnis  2006 -8.523,95   2007 -6.735,21 -15.259,16  2008 +4.247,16 -11.012,00  2009 -12.067,28 -23.079,28  2010 -11.234,95 -34.314,23  2011 -57.740,54 -92.054,77  2012 -102.049,70 -194.104,47  2013 -118.133,09 -312.237,56  2014 2.300,00 -309.937,45  2015 11.652,40 -298.285,05  2016 36.037,67 -262.247,38  2017 34.059,36 -228.188,02  2018 68.763,60 -159.424,42  2019 36.976,29 -122.448,13  2020 72.947,17 -49.500,96  Vorl.

**False Positives:**

- `Laut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/143588.1`) (sent_id: `deanon_BFG_20260814_TEST/143588.1_10`)


Gemäß Artikel 18 Abs. 1 des  Doppelbesteuerungsabkommens (DBA) Österreich/BRD komme Österreich als  Ansässigkeitsstaat das Besteuerungsrecht für die Firmenrente der Firma MH* zu.  Dagegen erhob der Bf. Beschwerde „bis die ausländischen Einkünfte geklärt sind.“

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_256`)


Es bestehe allerdings die  Besonderheit, dass gemäß § 72a der Bf. Stadtverfassung die Krankenanstalten und  Pflegeheime in einem A. zusammengefasst und quasi als „Unternehmung“ der Bf geführt  werden können.

**False Positives:**

- `Stadtverfassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_342`)


Zum A.:  Der A. sei gemäß § 72 der Bf. Stadtverfassung eine „Unternehmung“ der Bf.

**False Positives:**

- `Stadtverfassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/144140.1`) (sent_id: `deanon_BFG_20260814_TEST/144140.1_184`)


Es steht somit nur für die 4 Monate, in denen die Gattin des Bf. Anspruch auf die  Familienbeihilfe hatte, der Familienbonus Plus, in Höhe von (54,18*4) € 216,72 zu. Dieser  wurde bereits im angefochtenen Bescheid berücksichtigt.

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_108`)


Bereits in den Jahren davor – am 7. April 2021 sowie am  6. Mai 2022 – hatte die Bf. Meldungen gemäß § 5 WiEReG erstattet.

**False Positives:**

- `Meldungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/145402.1`) (sent_id: `deanon_BFG_20260814_TEST/145402.1_91`)


Die inländische (Wohn)Anschrift des Bf. Parasolstraße 27, 5163 Hiltenwiesen, Österreich  ist ident der Firmenanschrift des  Arbeitgebers des Bf.

**False Positives:**

- `Parasolstraße` — partial — pred is substring of gold: `Parasolstraße 27, 5163 Hiltenwiesen, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Parasolstraße 27, 5163 Hiltenwiesen, Österreich`(address)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_6`)


Dagegen erhob der Bf. Beschwerde mit der Begründung, dass sein Jahreseinkommen für das  Jahr 2022 Euro 34.675,28 betragen würde und er um Neuberechnung ersuche.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_110`)


Die im Verfahren vorgelegte Gleitzeitvereinbarung des Bf mit seinem Dienstgeber vom  August 2017 ließ ausreichend Spielraum für eine flexible Anpassung des Arbeitsbeginns bzw.  Arbeitsendes an die Fahrpläne des Regionalbusses 9999 durch den Bf. Auch an Arbeitstagen  mit Arbeitsbeginnzeiten zwischen 8:30 und 9:30 Uhr, die nach den Arbeitsaufzeichnungen des  Bf weitaus überwogen, standen nach einer regelmäßigen/überwiegenden Arbeitszeit von neun  Stunden zumutbare Busverbindungen zur Verfügung.

**False Positives:**

- `Auch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/145929.1`) (sent_id: `deanon_BFG_20260814_TEST/145929.1_12`)


Dagegen erhob der Bf. Beschwerde mit der Begründung, er habe im Oktober 2021 einen  großen Auftrag im Volumen von etwa 70% seines Umsatzes erhalten.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_19`)


In der Einkommensteuererklärung 2017 beantragte der Bf. Sonderausgaben in Höhe von  € 457,87, die erklärungsgemäß berücksichtigt wurden.

**False Positives:**

- `Sonderausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_161`)


Am 24.9.2003 wurde ein erhöhter Homocysteinwert festgestellt. Im Befund ist auch  festgehalten, dass der Bf. Augenblutungen hat.

**False Positives:**

- `Augenblutungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/146695.1`) (sent_id: `deanon_BFG_20260814_TEST/146695.1_56`)


Die  Familienbeihilfenbezieherin ist im vorliegenden Fall die Kindesmutter, die Frau des Bf. Der Bf.  selbst hatte im Jahr 2021 weder Anspruch auf den Unterhaltsabsetzbetrag, noch bezog er  Familienbeihilfe für seine beiden Stiefkinder.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_29`)


Tatsache sei, dass der  gegenständliche PKW der Marke Alfa Romeo Giulietta mit der FIN 000000 im Eigentum des  Vaters der Bf, Herr F stehe und auf diesen zugelassen sei.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_169`)


Der Vater der Bf, Herr F, geboren am XXXXX in Deutschland, ist in P wohnhaft.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_443`)


Nach den dargestellten Sachverhaltsfeststellungen ist dies  unzweifelhaft die Bf. Wie im Sachverhalt festgestellt und aus der Beweiswürdigung ersichtlich,  übt die Bf im streitgegenständlichen Zeitraum die Verfügungsgewalt aus, zumal sie bestimmt  wann sie nach Deutschland fährt bzw. wann sie mit dem Fahrzeug wohin fährt, wie lange sie an  welchem Ort bleibt und auch ein Teil der Kostentragung für Tankrechnungen und die  Jahresvignette in Österreich von der Bf getragen werden.

**False Positives:**

- `Wie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_453`)


Dies ist im gegenständlichen Fall  die Bf.  Wie in der Beweiswürdigung ausgeführt, konnte im gegenständlichen Fall jedoch bereits keine  Zuordnung zu einem „zweiten“ Standort außerhalb Österreichs erfolgen.

**False Positives:**

- `Wie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/147471.1`) (sent_id: `deanon_BFG_20260814_TEST/147471.1_198`)


Die Versicherung diente daher auf  Grund der dargestellten Vertragsgestaltung neben der behaupteten Darlehenssicherung in  nicht bloß geringfügigem Ausmaß auch wesentlichen anderen Zwecken, nämlich einer – aus  welchen Motiven auch immer intendierten - Absicherung der Darlehensnehmerin für den Fall  des Ablebens des Bf.  Wenn der Bf. im Beschwerdeschriftsatz vom 29.7.2019 vorbringt, dass sich das Original der  Polizze in seinen Händen befunden und A bei seinem Ableben daher kein Geld erhalten hätte,  so ist zu erwidern, dass sich dies aus der vorliegenden Polizze nicht ergibt.

**False Positives:**

- `Wenn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_29`)


Über das Vermögen der X GmbH wurde am 28.11.2016 vor dem LG für ZRS Graz zu GZ S das  Konkursverfahren eröffnet, in dem die Bf. Forderungen in Höhe von gesamt 513.875,98 Euro  anmeldete, wovon 448.875,98 Euro gerichtlich anerkannt wurden.

**False Positives:**

- `Forderungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `X GmbH`(organisation)
- `LG für ZRS Graz`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Hotterweg 4, 5142 Hitzging, Österreich, über die Beschwerde vom 27. Oktober 2023 gegen den  Bescheid des Finanzamtes Österreich vom 6. Oktober 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 47-043/9413, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Hotterweg` — partial — pred is substring of gold: `Hotterweg 4, 5142 Hitzging, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Hotterweg 4, 5142 Hitzging, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `47-043/9413`(tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/148480.1`) (sent_id: `deanon_BFG_20260814_TEST/148480.1_8`)


Entsprechend diesen Feststellungen wurde mit Festsetzungsbescheid vom 22.6.2015 für  verdeckte Ausschüttungen in Höhe von 1.256,15 € für das Jahr 2011, in Höhe von 17.980,50 €  für das Jahr 2012 und in Höhe von 3.765,81 € für das Jahr 2013, insgesamt somit 23.002,46 €  dem Bf. Kapitalertragsteuer vorgeschrieben.

**False Positives:**

- `Kapitalertragsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_179`)


Dem Erkenntnis des BFG vom 24.10.2022, RV/7102390/2021, lag folgender Sachverhalt  zugrunde:   Die im August 1999 geborene … ist die Tochter der Bf. Mutter und Tochter sind bulgarische  Staatsbürger und leben in Österreich.

**False Positives:**

- `Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_26`)


Am 3. April 2025 erhob der Bf. Einspruch gegen die Strafverfügung vom 27. März 2025 und  brachte nunmehr vor, das Fahrzeug sei zum gegenständlichen Zeitpunkt verborgt gewesen.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_86`)


Da auch in der Beschwerde gegen die Feststellung der Außenprüfung, dass die Rechnungen von  der Mackwart und Reinink Automotive GmbH an Bf. Scheinrechnungen sind, keine stichhaltigen Gegenargumente dargelegt  worden sind, werden die Daten aus Ihrer am 17.05.2017 eingebrachten  6 von 26 Seite 7 von 26

**False Positives:**

- `Scheinrechnungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mackwart und Reinink Automotive GmbH`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/149107.1`) (sent_id: `deanon_BFG_20260814_TEST/149107.1_27`)


Im Jahr 2021 trat die Bf. Anteile an der Zeidle Textil GmbH  ab und erzielte daraus einen  Veräußerungsgewinn in Höhe von EUR 993.000,00.

**False Positives:**

- `Anteile` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zeidle Textil GmbH`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/148999.1`) (sent_id: `deanon_BFG_20260814_TEST/148999.1_45`)


Im Jahr 2003 ließ die Bf. Holz schlägern, das sodann über Jahre getrocknet wurde.

**False Positives:**

- `Holz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/149302.1`) (sent_id: `deanon_BFG_20260814_TEST/149302.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache RA Mag. Dominik Maringer als Masseverwalter im Konkurs der  Verlassenschaft nach Bf, Salzburgerstraße 4, 4840 Vöcklabruck, über die Beschwerde vom  19. Jänner 2022 gegen die Bescheide des Finanzamtes Österreich vom 20. Dezember 2021  betreffend Einkommensteuer 2007 bis 2011, Steuernummer 23-567/1545, zu Recht  erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

**False Positives:**

- `Salzburgerstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `RA Mag. Dominik Maringer`(person)
- `Finanzamtes Österreich`(organisation)
- `23-567/1545`(tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/149302.1`) (sent_id: `deanon_BFG_20260814_TEST/149302.1_5`)


Zusätzlich ergeht der  BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache RA Mag. Dominik Maringer als Masseverwalter im Konkurs der  Verlassenschaft nach Bf, Salzburgerstraße 4, 4840 Vöcklabruck, betreffend Beschwerde vom  19. Jänner 2022 gegen die Bescheide des Finanzamtes Österreich vom 20. Dezember 2021  betreffend Anspruchszinsen (§ 205 BAO) 2007 bis 2011 und Wiederaufnahme der  Einkommensteuerverfahren 2007 bis 2011, Steuernummer 23-567/1545, beschlossen:   1 von 4 Seite 2 von 4

**False Positives:**

- `Salzburgerstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `RA Mag. Dominik Maringer`(person)
- `Finanzamtes Österreich`(organisation)
- `23-567/1545`(tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/149239.1`) (sent_id: `deanon_BFG_20260814_TEST/149239.1_55`)


II. Sachverhalt:  Die gesamte Familie AA (Bf, Gattin und vier Kinder, diese geb. in den Jahren 1996, 1998 und  2001) ist im Februar 2008 nach Neuseeland ausgewandert und hat dort ihren ständigen  Aufenthalt genommen (eigene Angaben;

**False Positives:**

- `Gattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/149610.1`) (sent_id: `deanon_BFG_20260814_TEST/149610.1_8`)


Außergewöhnliche Belastungen  c. Außergewöhnliche Belastungen mit Selbstbehalt € 1.538,40  Auf Ersuchen der belangten Behörde um Ergänzung vom 24.01.2025 (Eingangsstempel:  31.01.2025) teilte die Bf. Folgendes mit:  Ad a.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names after 'von' (Befunden/Gutachten)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `45258c48`  
**Description:**
Captures the name following 'von' in specific contexts using a capture group to exclude the context phrase.

**Content:**
```
(?:Befunden|Gutachten|Stellungnahme|Aussage|Schreiben|Einspruch|Antrag|Ansuchen|E-Mail|Mail|Bescheinigung|Bescheid|Verf\u00fcgung|Urteil|Entscheidung|Klage|Rechtsmittel|Vertretung|Anwalt|Rechtsanwalt|Notar|Gericht|Beh\u00f6rde|Amt|Finanzamt|Magistrat|Bundesfinanzgericht|Verwaltungsgericht|Verwaltungsstrafbeh\u00f6rde|VfGH|OGH|VwGH|BFG)\s+(?:von\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
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

## `Names after 'Arbeitsplatz des' (Contextual)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `494f2df2`  
**Description:**
Captures full title and name following 'Arbeitsplatz des' or 'Arbeitsplatz der', ensuring valid name structure.

**Content:**
```
(?:Arbeitsplatz\s+(?:des|der)\s+)(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)*(?:\s+(?:LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|BSc)?)?(?=\s|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 7 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_44`)


Im Schreiben vom  5.5.2014 bestätigt Ihr Arbeitgeber: ‚In der Regel ist der Arbeitsplatz der Unternehmensberater  direkt bei einem unserer Kunden‘.

**False Positives:**

- `Unternehmensberater ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_90`)


Im Schreiben vom 5.5.2014 bestätigt Ihr Arbeitgeber: „In der Regel ist der  Arbeitsplatz der Unternehmensberater direkt bei einem unserer Kunden.“

**False Positives:**

- `Unternehmensberater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_14`)


In der Beschwerde wird ausgeführt, dass der BF die Betrauung mit einem Arbeitsplatz der  Verwendungsgruppe „A“ anstrebe.

**False Positives:**

- `Verwendungsgruppe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_29`)


Mit 01.01.2015 wurde der BF nach Abschluss seines Studiums der Psychologie (Erwerb des  akademischen Grades BSc; arbeitspsychologisch orientierte Bachelorarbeit „Belastungen im  Einsatzdienst“) an der Universität mit einem Arbeitsplatz des Magistrates der  Verwendungsgruppe „B“ als Sicherheitsfachkraft betraut.

**False Positives:**

- `Magistrates` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_34`)


Der BF hat die Betrauung mit einem Arbeitsplatz der Verwendungsgruppe „A“ beim Magistrat  angestrebt.

**False Positives:**

- `Verwendungsgruppe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_38`)


Dem BF ist schließlich im Jahre 2021 auch ein Leitungsposten (Arbeitsplatz der  Verwendungsgruppe „A“) angeboten worden, und zwar stand eine Tätigkeit als  Arbeitspsychologe beim Magistrat im Raum.

**False Positives:**

- `Verwendungsgruppe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_248`)


Einkaufsmöglichkeiten sowie der Arbeitsplatz der Bf befinden sich in unmittelbarer und auch  mit dem Fahrrad erreichbarer Nähe zum Wohnort (Entfernung zur Arbeit beträgt rund 3 km;

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names after 'Herrn' or 'Frau' (Accusative/Dative)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c40bbb94`  
**Description:**
Captures full title and name following 'Herrn' or 'Frau', ensuring the name includes at least a first and last name (or title + first + last) to avoid partial matches.

**Content:**
```
(?:Herrn|Frau)\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
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

</details>

---

<details>
<summary>❌ False Negatives (934, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shirley Vostrovsky  in der Beschwerdesache **RgR Tanja Tihl, BSc**,  Kleindorf I 13, 4661 Deising, Österreich, über die Beschwerde vom 25. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 24. April 2023, Steuernummer 58-854/9841, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `RgR Tanja Tihl, BSc` (person)
- predicted in sentence: `RgR Tanja Tihl`

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)

Das Bundesfinanzgericht hat durch die Richterin **Mag. Anna Mechtler-Höger** in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

- missed: `Mag. Anna Mechtler-Höger` (person)
- predicted in sentence: `MedR Constantin Wiedewilt`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Priv.-Doz. Dr. Kurt Bartold**  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

- missed: `Priv.-Doz. Dr. Kurt Bartold` (person)
- predicted in sentence: `Dr. Kurt Bartold`

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter **Manfred Fiala** und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Manfred Fiala` (person)
- predicted in sentence: `Dr. Anna Radschek`, `Mag. Sonja Stradner`, `Ing. Wolfgang  Weichselbraun`, `Kira Lentze`

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter **Mag. Leander Hättrich**  in der Beschwerdesache Edith Grotehenn,  Karlhofstraße 20, 4212 Götschka, Österreich, vertreten durch Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Operngasse 6/4/9, 1010 Wien, gegen den Bescheid des FA Wien  4/5/10 vom 05.09.2009 betreffend Körperschaftsteuer 2006 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

- missed: `Mag. Leander Hättrich` (person)
- predicted in sentence: `Edith Grotehenn`

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die vorsitzende Richterin Mag. Aloisia Bergauer und die  beisitzende Richterin Mag. Andrea Ebner sowie die fachkundigen Laienrichter Mag. Johannes  Denk und **Friedrich Nagl** in der Beschwerdesache Dipl. Kfm. Rüdiger Schäffler, Anton-Dengler-Gasse 16, 8330 Krennach, Österreich, vertreten durch  BONAFIDE Treuhand- und Revisionsgesellschaft m.b.H., Berggasse 10, 1090 Wien, über die  Beschwerde vom 17. Oktober 2011 gegen die Bescheide des Finanzamtes Wien 12/13/14  Purkersdorf vom 11. Oktober 2011 betreffend Einkommensteuer für die Jahre 2006 bis 2009  nach Durchführung einer mündlichen Verhandlung beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

- missed: `Friedrich Nagl` (person)
- predicted in sentence: `Mag. Aloisia Bergauer`, `Mag. Andrea Ebner`, `Mag. Johannes  Denk`

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  **Timon Reinhertz**, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Timon Reinhertz` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_2`)

in der Verwaltungsstrafsache gegen  Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich, über die Beschwerde vom 8. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. März 2020, Geschäftszahl MA  67/196701206198/2019, uRecht erkannt:    I. **Detlev Griessmer**, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich  wird eine Ermahnung erteilt. Das Straferkenntnis wird aufgeho- ben.

- missed: `Detlev Griessmer` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_194`)

wurden Einkunftserzielung und Gewinnermittlung als Überschussrechnung laut  Liebhabereiverordnung für natürliche Personen und Gewinnermittlung für  Kapitalgesellschaften vermischt und jeweils der für die steuerpflichtige **Cathleen Kirchgässner**  nachteilige  Ansatz angeführt.“

- missed: `Cathleen Kirchgässner` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_385`)

Herr **Dr. YYY** arbeite in Gebieten, wo kein  Mobilfunknetz vorhanden sei.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden **Mag. Dieter Fröhlich**, den   Richter Mag. Christian Seywald, die fachkundigen Laienrichter Johannes Steiner und   Michael Kamper MSc über die Bescheidbeschwerde vom 24.07.2019 des Ulrike Ackermaier, Bakk. iur., Knödelhüttenstraße 12, 9184 Mühlbach, Österreich  vertreten durch Woditschka Steuerberatung GmbH, 2130 Mistelbach, Lanzendorfer  Hauptstraße 9/1, gegen die Umsatzsteuerbescheide für das Jahr 2017 und das Jahr 2018, vom  18.06.2019, des Finanzamtes Gänserndorf Mistelbach (nunmehr FA Österreich),  Steuernummer 75-013/8302, nach Durchführung einer mündlichen Verhandlung am 29.  Jänner 2024 in Anwesenheit des Schriftführers Dietmar Gratz  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Dieter Fröhlich` (person)
- predicted in sentence: `Mag. Christian Seywald`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_5`)

Mit Erinnerungsschreiben vom 6.11.2021 forderte das Finanzamt die **Herta Lindgens** (=  Beschwerdeführerin, Bf) dazu auf, die "Erstmeldung oder Meldung nach Fälligkeit der  jährlichen Überprüfung der wirtschaftlichen Eigentümer entsprechend den Bestimmungen des  § 5 Wirtschaftliche Eigentümer Registergesetz (WiEReG)" bis spätestens 28.12.2021  nachzuholen.

- missed: `Herta Lindgens` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/149107.1`) (sent_id: `deanon_BFG_20260814_TEST/149107.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Dr. Wiebke Peperkorn in der  Beschwerdesache Emilia Göpfardt, Hundsgrub 5, 4492 Rappersdorf, Österreich, vertreten durch **Mag. Dr. Walter Ganster**,  Hauptplatz 22, 9100 Völkermarkt, über die Beschwerde vom 6. Dezember 2023 gegen den  Bescheid des Finanzamtes Österreich vom 23. November 2023 betreffend Anspruchszinsen (§  205 BAO) 2021, Steuernummer 17-936/5215, zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

- missed: `Mag. Dr. Walter Ganster` (person)
- predicted in sentence: `Dr. Wiebke Peperkorn`, `Dr. Walter Ganster`

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)

Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr **Istvan  Melniczenko** (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

- missed: `Istvan  Melniczenko` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_149`)

Herr  **Dr. YYY** ist für Ärzte ohne Grenzen tätig.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Hon.-Prof. Wilfried Brokof**  in der Beschwerdesache Hademar Haßelbach, BSc,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Hon.-Prof. Wilfried Brokof` (person)
- predicted in sentence: `Hon.-Prof. Wilfried Brokof`, `Hademar Haßelbach`

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. in der Verwaltungsstrafsache gegen  **Pjotr Kristall**, Schöngrabenweg 12I, 4870 Mösendorf, Österreich, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs 2  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 6. September 2022,  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  22. August 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

- missed: `Pjotr Kristall` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, **Hermann**-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Hermann` (person)
- predicted in sentence: `Mag. Alexander Rimser`

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_3`)

Begründung  Aus den dem Gericht vorgelegten Unterlagen und dem elektronischen Akt ist ersichtlich, dass  die belangte Behörde (FA) am 6.3.2018 mittels Bescheid gemäß § 92 Abs. 1 lit. c BAO  feststellte, dass hinsichtlich des **Daniel Parys** (Beschwerdeführer, Bf.) im Zeitraum 2014 bis 2016  keine Unternehmereigenschaft vorlag.

- missed: `Daniel Parys` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_316`)

Mit Mail vom 26.8.2020 übermittelte die Richterin dem Bf. per Mail die Beweisfotos, das  Schreiben, welches der Magistrat an **Dr. YYY** gerichtet hatte, den Rückschein, die Niederschrift  über die mündliche Verhandlung und ein Schreiben, dessen Inhalt in der Folge wiedergegeben  wird:  "Anbei wird die Niederschrift der heutigen mündlichen Verhandlung übermittelt, in welcher die  Zeugin (das Organ der Parkraumüberwachung, welches die Anzeige gelegt hat, Frau ZEUGIN)  einvernommen wurde.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Andrea Müller-Dobler MBA MSc** in der  Verwaltungsstrafsache gegen Hademar Sachteleben, MSc, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

- missed: `Mag. Andrea Müller-Dobler MBA MSc` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_115`)

Es wurden einvernehmlich nicht nur Befunde beurteilt, sondern auch ausführliche persönliche  Gespräche mit Frau Mag. D (Neuropsychologisches Gutachten) und OA. **Dr. G** (Neuropädiaterin)  geführt.

- missed: `Dr. G` (person)
- predicted in sentence: `Mag`

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140189.1`) (sent_id: `deanon_BFG_20260814_TEST/140189.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Helena von Heyl**  in der Beschwerdesache des  Charlotte Buckenleib, Badeteich Bisamberg 32, 3500 Imbach, Österreich, vertreten durch StB, über die Beschwerde vom 26. Jänner 2022  gegen den Bescheid des Finanzamt Gmunden Vöcklabruck  vom 7. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Steuernummer 20-748/3811  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

- missed: `Hon.-Prof.in Helena von Heyl` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_22`)

Dieses Schreiben wird im Wesentlichen  von seinem Vater, **Quentin Schwartkopp**, bestätigt.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) **Siegfried Basyurt**, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

- missed: `Siegfried Basyurt` (person)
- predicted in sentence: `Bf`

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_39`)

Ergänzend wurde vom Finanzamt vorgebracht, dass sich **Mehmet Köprücü**  geweigert habe,  U/E Bescheide anzunehmen, sei keine unzulässige Einschränkung im Sinne des § 103 Abs 2  3 von 8 Seite 4 von 8

- missed: `Mehmet Köprücü` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Paolo Reppert  in der Beschwerdesache des  **Wendelin Pham**, Kremstal Bundesstraße 6, 4682 Thalham, Österreich, über die Beschwerden 1.) vom 17.10.2019 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 15.10.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 sowie  2.) vom 4.5.2020 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3.4.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

- missed: `Wendelin Pham` (person)
- predicted in sentence: `Dr. Paolo Reppert`

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Dr. Nicolaus Pomaroli MAS** in der  Beschwerdesache Techn R Miroslav Sängewald, Anton-Leb-Gasse 54, 4760 Bründl, Österreich, über die Beschwerde vom 23. Mai 2022 gegen  den Bescheid des Finanzamtes Österreich vom 18. Mai 2022 betreffend Familienbeihilfe 2022  zu Recht:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Dr. Nicolaus Pomaroli MAS` (person)
- predicted in sentence: `Dr. Nicolaus Pomaroli`

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/143519.1`) (sent_id: `deanon_BFG_20260814_TEST/143519.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Jeannine Gondrom  betreffend den Antrag des **OMedR Simon Pavlicsek**, Fulateia 364, 9562 Spitzenbichl, Österreich,   auf Gewährung der Verfahrenshilfe gemäß § 292 BAO im Beschwerdeverfahren zum Bescheid  des Finanzamt Graz-Stadt  vom 06.06.2023 hinsichtlich Rückforderung von Kinderabsetzbetrag und  Familienbeihilfe für vier Kinder für den Zeitraum 09.2020 – 07.2022  beschlossen:  Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

- missed: `OMedR Simon Pavlicsek` (person)
- predicted in sentence: `Dr.in Jeannine Gondrom`, `MedR Simon Pavlicsek`

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Danielle Merte  in der Beschwerdesache **Mag.a Susanne Groesche** Unternurpensalm 12, 5141 Moosdorf, Österreich  vertreten durch CONSULTATIO Steuerberatung GmbH & Co KG, Karl-Waldbrunner-Platz  1, 1210 Wien, über die Beschwerde vom 8. Juni 2015 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 7. Mai 2015 (jetzt Finanzamt für Großbetriebe), Steuernummer  76-369/9701, betreffend   1. Wiederaufnahme des Verfahrens zur Festsetzung der Energieabgabenvergütung für   A. 2005 – 2008,    Bäder 2005 – 2008,         Büchereien 2005 – 2008,  Bf. Kindergärten 2005 – 2008,      E. Stadion 2007,  B. Stadion 2005 – 2007,     C. Eishalle 2006, 2007,   D.Bad 2005 – 2007 und      F. Stadion 2006 und 2007  2.

- missed: `Mag.a Susanne Groesche` (person)
- predicted in sentence: `Dr.in Danielle Merte`, `Mag.a Susanne Groesche Unternurpensalm`

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_128`)

Dass die Kindesmutter den Anspruch auf die Ausgleichszahlung  hat (Art 67 VO (EU) 883/2004) und diesen mit dem Antrag vom 3.Jänner 2022 auch geltend  machte, ändert daran nichts (vgl. EuGH 22.10.2015, C-378/14 – Tomislaw **Trapkowski** und  VwGH 12.11.2019, Ra 2019/16/0133, je mwV).

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Merlin Morkam**  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

- missed: `Hon.-Prof.in Merlin Morkam` (person)
- predicted in sentence: `KzlR Jens Koudela`

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Jan Jürn  in der Beschwerdesache **Armin Klews, Bakk. art.**,  Lesach 119, 3071 Untergrafendorf, Österreich, über die Beschwerde vom 28. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 20. April 2022 betreffend Abweisung des Antrages auf Gewährung von  Familienbeihilfe ab Februar 2022 zur Steuernummer 51-609/6898  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Armin Klews, Bakk. art.` (person)
- predicted in sentence: `Armin Klews`

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142258.1`) (sent_id: `deanon_BFG_20260814_TEST/142258.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache **ÖkR OMedR Gregor Lauerhaas**, Riegerl 15, 4343 Hofstetten, Österreich, betreffend Beschwerde vom 16. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 14. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021,   Steuernummer 51-218/3095, beschlossen:  Der Vorlageantrag vom 21. September 2023 wird gemäß 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO zurückgewiesen.

- missed: `ÖkR OMedR Gregor Lauerhaas` (person)
- predicted in sentence: `MedR Gregor Lauerhaas`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Mag.a Waltraud Pantermühl**   in der Beschwerdesache der Kindsfater Telekom, Pirquethof 3, 8662 Lutschaun, Österreich, vertreten durch SIGNUM Treuhand  Steuerberatungs-GmbH, Rohrbach 25, 6850 Dornbirn,  betreffend den Bescheid des Finanzamt Graz-Stadt  vom 14. September 2021  hinsichtlich Zwangsstrafen 2021, Steuernummer 11-834/0873,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

- missed: `Mag.a Waltraud Pantermühl` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/147876.1`) (sent_id: `deanon_BFG_20260814_TEST/147876.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der **Yorick Lemgen**, Bürstenbachweg 2, 2295 Zwerndorf, Österreich, vertreten durch die Ernst & Young Steuerberatungsgesellschaft  m.b.H., Wagramer Straße 19, IZD-Tower (Postfach 89), 1220 Wien, über die Beschwerde vom  8. April 2025 gegen den Bescheid des Finanzamtes für Großbetriebe, Postfach 251, 1000 Wien,  vom 4. April 2025 betreffend die Festsetzung der Stabilitätsabgabe 2024 (Steuernummer xxx)  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Yorick Lemgen` (person)
- predicted in sentence: `Mag. Josef Ungericht`

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/148827.1`) (sent_id: `deanon_BFG_20260814_TEST/148827.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  **OSR Konstanze Dockweiler**, Hasenkogl 4, 3572 St. Leonhard am Hornerwald, Österreich, betreffend die am 2. August 2024 beim Finanzamt Österreich  eingelangte Beschwerde gegen die als „festgesetzte Säumniszuschläge für 2021“ bezeichneten  Bescheide beschlossen:  I.  Die Beschwerde gilt gem. § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

- missed: `OSR Konstanze Dockweiler` (person)
- predicted in sentence: `Mag. Erich Schwaiger`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_142`)

A. gab weiters an, dass er als einziger Gesellschafter und Geschäftsführer der X. d.o.o. in den Jahren 2012 und 2013 Seite 13 von 21 Rechnungen an **N.N.** ausgestellt hatte.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_377`)

Die Voraussetzungen für einen Abzug von Kosten des Herrn **M.** als außergewöhnliche  Belastung im Jahr 2018 liegen insgesamt nicht vor.

- missed: `M.` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Frauke Orsini**  in der Beschwerdesache Herbert Czarnezki,  Roacher Straße 40, 9241 Ragain, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 30. September 2019 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt  Österreich/FAÖ) vom 28. August 2019, Erf. Nr. Nr1,   betreffend  1. Festsetzung der Gebühren gemäß § 14 TP 2 Abs. 1 Z 1, TP 5 Abs. 1, TP 6 Abs. 1       und TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Der angefochtene Sammelbescheid wird abgeändert wie folgt:  1.

- missed: `Hon.-Prof.in Frauke Orsini` (person)
- predicted in sentence: `Herbert Czarnezki`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Priv.-Doz.in Caroline Reinwaldt**  in der Beschwerdesache Manuel Fortanz,  Zielgerade 30, 4950 Schwaig, Österreich, betreffend die Beschwerde vom 5. Juli 2017 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 9. Juni 2017 betreffend Umsatz- und Körperschaftsteuer 2010 bis 2015 sowie  Umsatzsteuerfestsetzung für die Zeiträume 01-03/2016, 04-06/201, 07-09/2016 und 10- 12/2016, Steuernummer , beschlossen:  Die Beschwerde wird als gegenstandslos geworden erklärt und das Verfahren eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `Priv.-Doz.in Caroline Reinwaldt` (person)
- predicted in sentence: `Manuel Fortanz`

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/143852.1`) (sent_id: `deanon_BFG_20260814_TEST/143852.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Albert Salzmann, die  Richterin Dr. Susanne Zankl sowie die fachkundigen Laienrichter Christine Höll und Dr. Rupert  Mayr in der Beschwerdesache **Ewald Lüttfrenk**, Triftgasse 9, 5145 Königsaich, Österreich, vertreten durch Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG, Forstamtsgasse 6, 5580 Tamsweg, über die  Beschwerde vom 30. März 2021 gegen die Bescheide des Finanzamtes Österreich vom  4. Februar 2020 betreffend Einkommensteuer 2014, 2015, 2016 und 2017 zur Steuernummer  55-257/7759  nach Durchführung einer mündlichen Verhandlung am 5. April 2023 in  Anwesenheit der Schriftführerin Premm Helene zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Ewald Lüttfrenk` (person)
- predicted in sentence: `Mag. Albert Salzmann`, `Dr. Susanne Zankl`, `Dr. Rupert  Mayr`

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter in der Beschwerdesache  **Prof.in Alma Siegers**, Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 11. August 2020 gegen den Bescheid des  Finanzamtes Österreich vom 22. Juli 2020 betreffend Einkommensteuer 2014, Steuernummer  37-792/2472, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Prof.in Alma Siegers` (person)
- predicted in sentence: `Dr. Judith Leodolter`

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin **Univ.-Prof.in Ada Forstner**  in der Beschwerdesache des  Elias von Wnuk-Lipinski, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Univ.-Prof.in Ada Forstner` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_10`)

Ebenso legte der Bf. die Heiratsurkunde, sowie eine seine Ehegattin **Katalin** betreffende  Bestätigung (E9) für das Jahr 2018 vor, aus welcher Einkünfte derselben in Höhe von  2.824.116,- HUF vor.

- missed: `Katalin` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_1`)

VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch den Richter **Mag. David Hell LL.B. LL.M.** in der Beschwerde- sache Geraldine Loeper, Bakk. techn., Südstraße 6, 6471 Leins, Österreich, zur Beschwerde vom 20. November 2023 gegen den  Bescheid des Finanzamtes Österreich vom 9. November 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 16-579/1693, mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde- vorentscheidung vom 15. Jänner 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2022 kein Vorlageantrag eingebracht.

- missed: `Mag. David Hell LL.B. LL.M.` (person)
- predicted in sentence: `Mag. David Hell`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_231`)

Der Kanzler informierte dabei  gemeinsam mit Gesundheitsminister Rudolf Anschober, dem steirischen Landeshauptmann  Hermann Schützenhöfer, dem Wiener Bürgermeister Michael Ludwig und **Univ.-Prof. Dr.  Oswald Wagner**, Vizerektor der Medizinischen Universität Wien und Leiter des klinischen  Institutes für Labormedizin, über die weitere Vorgehensweise in der Corona-Krise.

- missed: `Univ.-Prof. Dr.  Oswald Wagner` (person)
- predicted in sentence: `Dr.  Oswald Wagner`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_306`)

Wenn **Dr. YYY** nach Wien  kommt stelle ich ihm ein Kraftfahrzeug zur freien Verfügung.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Anna Mechtler-Höger** in der  Beschwerdesache Gotthard Kirchhoffs, Unterriese 2, 7432 Oberschützen, Österreich, vertreten durch WWV-GROUP  SteuerberatungsGmbH, Bahnhofstraße 4, 3950 Gmünd, über die Beschwerde vom  28. September 2021 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli 2021  betreffend Haftung für Lohnsteuer, Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  für die Jahre 2015 bis 2019, Steuernummer 19-927/9012, zu Recht erkannt:   I. Der Beschwerde gegen die Bescheide betreffend Festsetzung des Zuschlags zum  Dienstgeberbeitrag 2015 bis 2019 wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag. Anna Mechtler-Höger` (person)
- predicted in sentence: `Gotthard Kirchhoffs`

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_350`)

Der Ausweis wurde von **Dr. YYY** angebracht.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

</details>

---

