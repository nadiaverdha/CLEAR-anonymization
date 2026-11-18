# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-18T11:13:15.384847

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
| Accuracy (exact match) | 98.8% |
| True Positives | 944 |
| False Positives | 323 |
| False Negatives | 670 |
| Total Gold Entities | 1614 |
| Micro Precision | 74.5% |
| Micro Recall | 58.5% |
| Micro F1 | 65.5% |
| Macro F1 | 65.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `salutation_herr_frau` | 6.6% | 94.8% | 3.4% | 58 | 55 | 3 |
| `beschwerdesache_name` | 28.3% | 92.2% | 16.7% | 293 | 270 | 23 |
| `academic_titles` | 49.1% | 78.8% | 35.7% | 731 | 576 | 155 |
| `genitive_name_no_title` | 3.3% | 32.9% | 1.7% | 85 | 28 | 57 |
| `represented_by` | 1.7% | 17.9% | 0.9% | 78 | 14 | 64 |
| `role_anchor_name` | 0.1% | 7.7% | 0.1% | 13 | 1 | 12 |
| `initial_only_name` | 0.0% | 0.0% | 0.0% | 9 | 0 | 9 |
| `standalone_name_after_role` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `salutation_herr_frau` 🏆

**F1:** 0.066 | **Precision:** 0.948 | **Recall:** 0.034  

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
| 0.948 | 0.034 | 0.066 | 58 | 55 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 55 | 3 | 1559 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_36`)


Im Ermittlungsverfahren wurde bekannt gegeben, dass das Fahrzeug Herrn Vera Schliephacke  überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_40`)


Sie werden daher unter Hinweis auf Ihre Mitwirkungspﬂicht im Verwaltungsstrafverfahren,  binnen zwei Wochen ab Zustellung dieses Schreibens, aufgefordert, bekannt zu geben, wie  lange sich Herr Vera Schliephacke in Wien aufgehalten, wo er gewohnt hat und zu welchem Zweck  ihm das verfahrensgegenständliche Fahrzeug überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_108`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 01/2006  Herr Heinz Herper  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:    Die Unfähigkeit sich selbst den Unterhalt zu verschaffen ist ab 1/2006 belegbar da ab diesem  Zeitpunkt höhergradige körperliche Beeinträchtigungen vorhanden sind;

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

| Predicted | Gold |
|---|---|
| `Dimitri Witkoski` | `Dimitri Witkoski` |

**Missed by this rule (FN):**

- `Ruckelshaußen` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Waldviertel als Finanzstrafbehörde vom 12. November  2020, SpS, Strafnummer, wurde Herr Petra Port, geb. am 1980, schuldig erkannt, er habe im  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_14`)


Herr Julia Reittinger  ist voraussichtlich dauernd außerstande sich selbst den Unterhalt zu  verschaffen: NEIN

| Predicted | Gold |
|---|---|
| `Julia Reittinger` | `Julia Reittinger` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

| Predicted | Gold |
|---|---|
| `Franziska Fitzmann` | `Franziska Fitzmann` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr Katharina Bauckholt (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Katharina Bauckholt` | `Katharina Bauckholt` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_17`)


Im Gegenteil war es so, daß  die Touristik Werkvalbach GmbH die fälligen Gebäudemieten, welche an Herrn Jeanne Kraenzlin  zu zahlen gewesen  wären, nicht bedienen konnte.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Missed by this rule (FN):**

- `Touristik Werkvalbach GmbH` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_54`)


Der Verzicht wurde somit vom steuerlichen  Vertreter - auch im Namen von Herrn Jeanne Kraenzlin - abgegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)


Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn Jeanne Kraenzlin) getragen wird.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)


Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr Istvan  Melniczenko (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Istvan  Melniczenko` | `Istvan  Melniczenko` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_4`)


Dass der Geschäftsführer der GmbH, Herr Nadine Millradt, dies bestreite, sei ihm bekannt und  derzeit Gegenstand mehrerer Verfahren.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_7`)


Herr Nadine Millradt  schulde ihm noch ausstehende Gehälter.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_12`)


Sollte Herr Nadine Millradt  die Vorsteuer zum Abzug gebracht haben, müsse sie von ihm zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_24`)


In der Begründung wird dazu ausgeführt:  „Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 8,4 Liter  Alkohol unter Abfindung, wobei diese Menge als "Hausbrand" steuerfrei belassen werden  sollte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_25`)


Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 15 Liter  Alkohol unter Abfindung, wobei diese Mengen als "Hausbrand" ebenfalls steuerfrei belassen  werden sollte.“

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_32`)


Im Bescheid II vom 20.2.2019 wurde für Herrn Quentin Schwartkopp, Adresse_Bf., gemäß § 8 Abs. 1 Z 2  AlkStG iVm. § 201 Abs. 1 und Abs. 2 Z 3 der Bundesabgabenordnung (BAO) die Alkoholsteuer  für 2016 in Höhe von € 280,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_33`)


In der Begründung wurde ausgeführt: „Nach dem Auszug "Abfrage  Abfindungsberechtigte/Person" vom 31.08.2018 des Zollamtes Innsbruck war Herr Quentin Schwartkopp  jedenfalls als Abfindungsberechtigter ausgewiesen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_34`)


Im Rahmen des Ermittlungsverfahrens wurde festgestellt, dass Herr Quentin Schwartkopp, belegt durch  den Übergabevertrag, GZ xxx vom 17.mt.2011 — mit Wirkung vom 01.mt.2011 — das  landwirtschaftliche Anwesen in Betriebssitz, an seinen Sohn Sohn, übergeben hat.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_37`)


Mit Schreiben des Zollamtes Innsbruck vom 14.01.2019, GZ 800000/thrhtr, wurde Herr  Quentin Schwartkopp  zur Abgabe einer Stellungnahme gemäß § 115 BAO eingeladen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_38`)


Mit Schreiben vom  29.01.2019 gab Herr Quentin Schwartkopp  an, dass er nach Übergabe seines Hofes an seinen Sohn Sohn  mit diesem mündlich vereinbart habe, dass er die Obstveredelung weiterhin als  Fruchtgenussberechtigter betreiben dürfe.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_41`)


Überdies hätte Herr Quentin Schwartkopp  auch  vor der Übertragung des land- und forstwirtschaftlichen Betriebes die Freimenge für Herrn  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

| Predicted | Gold |
|---|---|
| `Dominik Barfusz` | `Dominik Barfusz` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)


Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der Engelbert Schefe  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Engelbert Schefe` (person)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_34`)


Herr Corvin Billmaier  hat die Ausgaben getragen und bezahlt und Ausgaben sind bei jenem  abzugsfähig, der sie bezahlt hat und nicht bei jenem, den sie betroffen hätten.

| Predicted | Gold |
|---|---|
| `Corvin Billmaier` | `Corvin Billmaier` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Gudrun Joehnk` | `Gudrun Joehnk` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_8`)


Begründung  Verlauf des Verfahrens  Mit Straferkenntnis vom 27. Dezember 2023, GZ MA67/111111/2023, hat der Magistrat der  Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Arthur Soyal (in weiterer Folge:  Beschwerdeführer) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt, indem er  das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen W-6789 (A) am 4. August  2023 um 11:10 Uhr in einer gebührenpflichtigen Kurzparkzone in 1160 Wien, Hasnerstraße  129, abgestellt habe, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Arthur Soyal` | `Arthur Soyal` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_8`)


Mit an die Magistratsabteilung 67 gesendeter E-Mail vom 12. Juni 2024 erstattete Herr  Jeanne Pavlovitsch (in der Folge: Beschwerdeführer) eine von der belangten Behörde als Einspruch  gegen die Strafverfügung vom 4. Juni 2024 gewertete Eingabe.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/146473.1`) (sent_id: `deanon_BFG_20260814_TEST/146473.1_3`)


Begründung  Am 22.03.2024 erließ das Finanzamt für Frau Günter Salfetter, Beschwerdeführerin, einen  Einkommensteuerbescheid (Arbeitnehmerveranlagung) für das Jahr 2023.

| Predicted | Gold |
|---|---|
| `Günter Salfetter` | `Günter Salfetter` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_16`)


Der E-Mail vom 5. Februar 2025 war folgende Vollmacht beigelegt:   „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024 , wohnt Adr1, den  Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt  Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte Akzeptieren Sie das  Einspruch.“

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_31`)


Mit E-Mail vom 5. Februar 2025 übermittelte der Beschwerdeführer ein Schreiben des M mit  folgendem Inhalt: „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024,  wohnt Adr1, den Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu  Magistrat der Stadt Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte  Akzeptieren Sie das Einspruch“.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_44`)


Der belangten Behörde ist zwar zuzustimmen, dass die schriftliche Vollmacht mit  5. Februar 2025 datiert und somit erst nach der Verfahrenshandlung (Erhebung des  Einspruches) vom 10. September 2024 errichtet wurde, die Behörde lässt hierbei jedoch außer  Betracht, dass es sich sowohl bei dem Beschwerdeführer als auch bei dem Vollmachtgeber um  Personen mit offenkundig mangelnden Sprachkenntnissen handelt. Aus der gewählten  Ausdrucksweise lässt sich nach Ansicht des Bundesfinanzgerichts jedoch ableiten, dass der  Beschwerdeführer bereits vor der Verschriftlichung der Vollmacht, nämlich bereits im  Zeitpunkt der Setzung der Verfahrenshandlung am 10. September 2024 mündlich von M zur  Erhebung eines Einspruches gegen die Strafverfügung bevollmächtigt war (Arg: „[…] Herrn  Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt Wien  Magistratsabteilung 67 schicken […]“).

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_14`)


Herr Kaspar Sadowski  führt ab 1.1.2018 den Betrieb „Unternehmensberatung" - der zuvor von der **  GMBH geführt wurde - nun mehr als Einzelunternehmung Kaspar Sadowski  weiter.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_16`)


Es wurde in diesem Zusammenhang auch die einschlägige  Gewerbeberechtigung bei Herrn Kaspar Sadowski  wieder als aktiv gemeldet.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_20`)


Da Herr Kaspar Sadowski  immer  Alleingesellschafter der ** GMBH war, ist der Übergang des Verlustvortrages mit 100 %  vorzunehmen.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_3`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_31`)


Das Finanzamt hat dazu folgende Stellungnahme abgegeben:  „Der Mehmet Köprücü  gab am 20.04.2022 seine Vollmacht für das Haftungsverfahren  Evamaria Watenphul  bekannt und beschrieb sie wortwörtlich so:  Haftungsbescheide je vom 23.03.2022  Und:  In der außen bezeichneten Finanzsache haben die Beschwerdeführer … Evamaria Watenphul, … als  ehemalige Geschäftsführer der Özyilmaz Recycling GmbH., Herrn Mehmet Köprücü  Vollmacht erteilt,  wobei sich der gefertigte Anwalt auf diesem ihm erteilte Vollmacht beruft.

**False Positives:**

- `Mehmet Köprücü  Vollmacht` — similar text (different position): `Mehmet Köprücü`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Mehmet Köprücü`(person)
- `Evamaria Watenphul`(person)
- `Evamaria Watenphul`(person)
- `Özyilmaz Recycling GmbH.`(organisation)
- `Mehmet Köprücü`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

**False Positives:**

- `Manhardt  Adresse` — partial — gold is substring of pred: `Manhardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Manhardt`(person)

</details>

---

## `beschwerdesache_name` 🏆

**F1:** 0.283 | **Precision:** 0.922 | **Recall:** 0.167  

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
| 0.922 | 0.167 | 0.283 | 293 | 270 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 270 | 23 | 1344 |

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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karina Ditzler` | `Karina Ditzler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Cornelia Özgür` | `Cornelia Özgür` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Fabienne Kattner` (person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich` (address)
- `Thomas Krampl` (person)
- `Finanzamtes für Gebühren` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dominika Oehlerich, BEd` | `Dominika Oehlerich, BEd` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Ebner` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Simone Zemanek, MSc` | `Simone Zemanek, MSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `15-763/9594` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Gorecki` | `Wieland Gorecki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

| Predicted | Gold |
|---|---|
| `Bruno Rüttgers` | `Bruno Rüttgers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wladimir Beheim` (person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich` (address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG` (organisation)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Babette Bernett, Schmalzhofen 9, 8250 Riegersbach, Österreich, über die Beschwerde vom 17. September 2020 gegen den  Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt Österreich) vom 4. September  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerdevorentscheidung vom 24. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 wird gemäß § 279 Abs. 1 BAO ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Babette Bernett` | `Babette Bernett` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Schmalzhofen 9, 8250 Riegersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Janis Dührkopp` | `Janis Dührkopp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Thomas Leitner` (person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Björn Stover, Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich, vertreten durch ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH, Landungsplatz 5, 4864  Attersee/Attersee, über die Beschwerde vom 14. September 2021 gegen die Bescheide des  Finanzamtes Österreich vom 23. August 2021 betreffend die Festsetzung von  Verspätungszuschlägen für die Monate 12/2020, 01/2021 und 03-05/2021, Steuernummer  57-952/0912, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Björn Stover` | `Björn Stover` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich` (address)
- `ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `57-952/0912` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/136300.1`) (sent_id: `deanon_BFG_20260814_TEST/136300.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Susanne Türner, Viehdorfer Straße 25, 9853 Burgwiese, Österreich, gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg  Tulln vom 25. November 2011 betreffend Körperschaftsteuer und Umsatzsteuer 2007,  Steuernummer 16-353/9813  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susanne Türner` | `Susanne Türner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Viehdorfer Straße 25, 9853 Burgwiese, Österreich` (address)
- `Finanzamtes` (organisation)
- `16-353/9813` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Patrick Hübben  in der Beschwerdesache Alice Rüde,  Auhub 26, 9560 Kraß, Österreich, vertreten durch BDO Steiermark GmbH Wtp u Stb, Schubertstraße 62, 8010  Graz, über die Beschwerde vom 18. März 2019 gegen den Bescheid des FA Tirol Ost  vom  26. Februar 2019 betreffend Abweisung eines Zahlungserleichterungsansuchens zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alice Rüde` | `Alice Rüde` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Patrick Hübben` (person)
- `Auhub 26, 9560 Kraß, Österreich` (address)
- `BDO Steiermark GmbH Wtp` (organisation)
- `FA Tirol Ost` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Lewis Fröhner, Feldgasse, Rattersdorf 6, 6731 Boden, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 25. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lewis Fröhner` | `Lewis Fröhner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Feldgasse, Rattersdorf 6, 6731 Boden, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Marion Schlesing  in der Beschwerdesache des  Dimitri Seewaldt, Sonnblickweg 22, 4263 Elmberg, Österreich, über die Beschwerde vom 15. November 2018 gegen den Bescheid  des FA Judenburg Liezen (jetzt Dienststelle des Finanzamtes Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zur Steuernummer 93-757/0582  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dimitri Seewaldt` | `Dimitri Seewaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Marion Schlesing` (person)
- `Sonnblickweg 22, 4263 Elmberg, Österreich` (address)
- `FA Judenburg Liezen` (organisation)
- `Finanzamtes Österreich` (organisation)
- `93-757/0582` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dora Grobstich  in der Beschwerdesache Raul Türkkan,  Schachener Straße 122J, 3643 Nonnersdorf, Österreich, über die Beschwerde vom 10. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 4. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 24-623/5745  zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Raul Türkkan` | `Raul Türkkan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dora Grobstich` (person)
- `Schachener Straße 122J, 3643 Nonnersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `24-623/5745` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


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

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


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

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Gruenleitner Event` — type mismatch — same span as gold: `Gruenleitner Event`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Waltraud Pantermühl   in der Beschwerdesache der Kindsfater Telekom, Pirquethof 3, 8662 Lutschaun, Österreich, vertreten durch SIGNUM Treuhand  Steuerberatungs-GmbH, Rohrbach 25, 6850 Dornbirn,  betreffend den Bescheid des Finanzamt Graz-Stadt  vom 14. September 2021  hinsichtlich Zwangsstrafen 2021, Steuernummer 11-834/0873,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Kindsfater Telekom` — type mismatch — same span as gold: `Kindsfater Telekom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Waltraud Pantermühl`(person)
- `Kindsfater Telekom`(organisation)
- `Pirquethof 3, 8662 Lutschaun, Österreich`(address)
- `SIGNUM Treuhand  Steuerberatungs-GmbH`(organisation)
- `Finanzamt Graz-Stadt`(organisation)
- `11-834/0873`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rut Schattel  in der Beschwerdesache des  Stanley Wachenschwanz, Bakk. rer. nat. Bf1-Adr***RA über die Beschwerde vom 19. Oktober 2016 gegen die Bescheide  des Finanzamtes X vom 28. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2012 und 2013 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Stanley Wachenschwanz` — partial — pred is substring of gold: `Stanley Wachenschwanz, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rut Schattel`(person)
- `Stanley Wachenschwanz, Bakk. rer. nat.`(person)
- `Finanzamtes`(organisation)

</details>

---

## `academic_titles` 🏆

**F1:** 0.491 | **Precision:** 0.788 | **Recall:** 0.357  

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
| 0.788 | 0.357 | 0.491 | 731 | 576 | 155 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 576 | 155 | 1038 |

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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ophelia Dutschka` | `Hon.-Prof.in Ophelia Dutschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_60`)


Der Beschwerdeführer begründet die berufliche Notwendigkeit der Teilnahme an den  gegenständlichen Kursen mit der Erlangung von Kenntnissen und Fähigkeiten zur Anwendung  Hypnosystemischer Konzepte nach Dr. Gunther Schmidt und von Kommunikationsmethoden,  wie sie im Hypnotherapeutischen Bereich zur Anwendung kämen;

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_67`)


darüber hinaus habe  er sich bereits nach der Teilnahme am ersten von drei Kursen der „Kurzausbildung mit  Dr. Gunther Schmidt – Hypnosystemische Konzepte für Coaching, Team &  Organisationsentwicklung und Supervision“ im Herbst 2018 entschieden, sich im Laufe der Zeit  ein weiteres „Standbein“ aufzubauen, um die erworbenen Kenntnisse als  freiberuflicher/selbständiger Coach anzubieten.

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dr. Kurt Bartold` | `Priv.-Doz. Dr. Kurt Bartold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gruenleitner Event` (organisation)
- `Finanzamtes  Graz-Stadt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Cassandra Witzenhause` | `Univ.-Prof.in Cassandra Witzenhause` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hedwig Mackiewicz` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Damian Wiecher` | `Mag. Damian Wiecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow` (person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Li Schukardt` | `Priv.-Doz. Li Schukardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Buchholz` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Corbinian Friemuth` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |
| `Techn R Lilia Schöpcke` | `Techn R Lilia Schöpcke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_24`)


Seit 2013 habe sie die Invaliditätspension gehabt und jetzt habe sie Rehabgeld  Ledig, lebt alleine, kein Kinder  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  zur Untersuchung mitgebrachte Befunde:  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013:  Dg.: emotional instabile Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30.11.- 01.12.2015:  Dg.: ängstlich agitiertes paranoides Zustandsbild bei narzisstisch emotional instabiler  Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012:  Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012:  Dg.: posttraumatische Belastungsstörung, Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013 posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  2 von 18 Seite 3 von 18

| Predicted | Gold |
|---|---|
| `Dr. Mairinger` | `Dr. Mairinger` |
| `Dr. Schlapschi` | `Dr. Schlapschi` |
| `Dr. Nöllner` | `Dr. Nöllner` |
| `Dr. Mersch` | `Dr. Mersch` |

**Missed by this rule (FN):**

- `Psych Rehab Hollenburg` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_25`)


Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung   Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  Untersuchungsbefund:  Allgemeinzustand: 34 jährige in gutem AZ  Ernährungszustand: gut  Größe: 158,00 cm Gewicht: 50,00 kg    Status (Kopf / Fußschema) - Fachstatus:  Stand und Gang: unauffällig  Sprache und Sprechen: unauffällig  Gesamtmobilität - Gangbild:  kommt frei gehend alleine zur Untersuchung, wurde von Bekannten hergebracht  Führerschein: nein  Psycho(patho)logischer Status:  Kooperativ und freundlich, gut auskunftsfähig, bewußtseinsklar, voll orientiert, leichtes  kognitiv- mnestisches Defizit, Gedankenductus: geordnet, kohärent; logorrhoisch, an  bestimmten Dankzielen haftend, Konzentration reduziert und Antrieb eher angehoben,  Stimmungslage depressiv, weinerlich, kaum afflzierbar;

| Predicted | Gold |
|---|---|
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_50`)


Dr. Omasits sei in Pension.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_66`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_68`)


Cipralex und Psychotherapie  Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  emotional instabile Persönlichkeitsstörung mit histrionischen Zügen   Gutachten zur Gewährung der Invaliditätspension 12.04.2016,   Dr. Omasits (Psychiatrie): paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP  auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |
| `Dr. Omasits` | `Dr. Omasits` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_149`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_151`)


Cipralex und Psychotherapie   Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  9 von 18 Seite 10 von 18

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_152`)


emotional instabile Persönlichkeitsstörung mit histrionischen Zügen  Gutachten zur Gewährung der Invaliditätspension 12.04.2016, Dr. Omasits (Psychiatrie):  paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_155`)


LK Baden, Psychiatrie, 16.11.2012: Anpassungsstörung, Vd. a. Persönlichkeitsstörung  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013: Dg.: emotional instabile  Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30 11- 01 12 2015: Dg.: ängstlich agitiertes paranoides  Zustandsbild bei narzisstisch emotional instabiler Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012: Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012: Dg.: posttraumatische Belastungsstörung,  Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013: posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018: posttraumatische  Belastungsstörung, Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  mitgebrachter Befund:  PSD Wr. Neustadt 09/2019: Diagnosen: PTSD, komb.

| Predicted | Gold |
|---|---|
| `Dr. Mairinger` | `Dr. Mairinger` |
| `Dr. Schlapschi` | `Dr. Schlapschi` |
| `Dr. Nöllner` | `Dr. Nöllner` |
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |

**Missed by this rule (FN):**

- `Psych Rehab Hollenburg` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_186`)


Sie legte ein Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für Neurologie und  Psychiatrie vor.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_194`)


von der Bf. vorgelegten Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für  Neurologie und Psychiatrie.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Mag.a Livia Korowski` | `Priv.-Doz.in Mag.a Livia Korowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Mitterhuber` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Ditzler` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Linn Förstle` | `Hon.-Prof. Linn Förstle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich` (address)
- `Finanzamtes` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |
| `Techn R Tosca Häfeli` | `Techn R Tosca Häfeli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_11`)


Mit Strafverfügung vom 12.3.2019 lastete der Magistrat der Stadt Wien, Magistratsabteilung  67, Techn R Tosca Häfeli, in der Folge kurz mit Bf. bezeichnet, folgende Verwaltungsübertretung an:  "1. Datum/Zeit:  06.06.2018, 09:29 Uhr   Ort:   TATORT   betroffenes Fahrzeug: KENNZ (A)   Abstellen des Fahrzeuges, ohne für seine Kennzeichnung mit einem für den   Beanstandungszeitpunkt gültigen Parknachweis (Parkschein, Tages- oder   Wochenpauschalkarte) gesorgt zu haben, da der im Fahrzeug angebrachte   Parkausweis für Behinderte gemäß § 29b der StVO kein Original war.

| Predicted | Gold |
|---|---|
| `Techn R Tosca Häfeli` | `Techn R Tosca Häfeli` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung  67` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Daisy Hoopt` | `Univ.-Prof.in Daisy Hoopt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in StR DDr.in Reneé Plein` (person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `VetR OMedR Constantin Wiedewilt` | `VetR OMedR Constantin Wiedewilt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich` (address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominika Oehlerich, BEd` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_85`)


Behandlungen / Medikamente / Hilfsmittel: Efectin 225mg, Inkotan 15mg, Lasix 40mg,  Pantoprazol 20mg, PK-Merz, Pregabalin 75mg 2x1, Sirdalud 4mg 2x1, Zyprexa 2,5mg 1-2-4-0,  Copaxone Inj.lösung, etc.; FÄ-Betreuung bei Dr. Fux alle 6 Wochen.

| Predicted | Gold |
|---|---|
| `Dr. Fux` | `Dr. Fux` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_115`)


• Schreiben des Bezirksgerichtes Donaustadt vom 29. Juli 2013 (Verständigung gemäß §  126 AußStrG)  • Psychiatrisches Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9  Dem Ersteller des Gutachtens, Dr. Wolfgang Baischer, Facharzt für Psychiatrie und Neurologie  wurden folgende Befunde vorgelegt:  Psychiatrische Abteilung des SMZ-Ost, Aufenthalt vom 21. Oktober bis 5. November 2012:  "Chronisch-progrediente Encephalitis disseminata mit organischem Psychosyndrom, gemischte  schizoaffektive Störung.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Missed by this rule (FN):**

- `Universität Wien` (organisation)
- `Prof. Maida` (person)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_166`)


Dr. Wolfgang Baischer diagnostizierte beim Bf. im psychiatrischen Gutachten vom 21. Februar  2013 ein organisches Psychosyndrom bei Encephalitis disseminata (Anm.: multiple Sklerose)  und hielt dazu fest, dass diese degenerative neurologische Erkrankung im Sinne einer  Encephalitis disseminata (Multiple Sklerose) beim Untersuchten seit längerer Zeit bekannt sei.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_207`)


Das Gutachten von Prof. Maida datiert mit 2. März  2009, das BASB-Gutachten  vom 29. September 2009, die Befunde/Arztbriefe der  Psychiatrischen Abteilung des SMZ-Ost aus 2012 und das Gutachten von Dr. Baischer vom 21.  Februar 2013.

| Predicted | Gold |
|---|---|
| `Dr. Baischer` | `Dr. Baischer` |

**Missed by this rule (FN):**

- `Prof. Maida` (person)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `StR Mag. Dirk Bröders` | `StR Mag. Dirk Bröders` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `77-629/3506` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Schraders` | `Univ.-Prof.in Anastasia Schraders` |
| `KommR Serge Salameh` | `KommR Serge Salameh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Caroline Schröer` | `Mag.a Caroline Schröer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Beha` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/131086.1`) (sent_id: `deanon_BFG_20260814_TEST/131086.1_2`)


in der Beschwerdesache PhD KommR Louisa Mühle, Waltersdorferstraße 9, 5310 Scharfling, Österreich, vertreten durch N & N Steuerberatungsgesellschaft m.b.H., Schubertstraße 68, 8010  Graz, über die Beschwerde vom 6. Dezember 2017 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 6. November 2017 betreffend  1.

| Predicted | Gold |
|---|---|
| `PhD KommR Louisa Mühle` | `PhD KommR Louisa Mühle` |

**Missed by this rule (FN):**

- `Waltersdorferstraße 9, 5310 Scharfling, Österreich` (address)
- `N & N Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ing. Ludwig Taspinar, MA` (person)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |
| `Mag. Monika Schmalzl` | `Mag. Monika Schmalzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |
| `Mag. Thassilo Wedekinn` | `Mag. Thassilo Wedekinn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich` (address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_19`)


Als Auftragnehmer fungierten - laut den  vorliegenden Eingangsrechnungen – die Firma1 GmbH, die Firma2 GmbH & CoKG, die Firma3  GmbH & CoKG, die PhD Mag. Heinrich Hambücher  und die Firma4 GmbH. Die Firma1 GmbH habe sich bei der  Leistungserbringung diverser Subunternehmer bedient, die wiederum in einem Naheverhältnis  zum Kommanditisten bzw. Komplementär der Rechtsvorgängerin & CoKG gestanden seien.

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Missed by this rule (FN):**

- `Firma2 GmbH & CoKG` (organisation)
- `Firma3  GmbH & CoKG` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_37`)


Nachdem die Rechtsvorgängerin & CoKG infolge Anwachsung der Gesellschaftsanteile nach §  142 UGB an die PhD Mag. Heinrich Hambücher  mit Wirksamkeit zum xx.xx.xxxx im Firmenbuch gelöscht worden  war, teilte die steuerliche Vertretung am 11.02.2020 mit, dass zur Rechtsnachfolgerin ein  aufrechtes Bevollmächtigungsverhältnis bestehe.

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_75`)


ihr  Geschäftsanteil wurde von der PhD Mag. Heinrich Hambücher (FN xxxxxx) übernommen;

| Predicted | Gold |
|---|---|
| `PhD Mag. Heinrich Hambücher` | `PhD Mag. Heinrich Hambücher` |

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

**False Positives:**

- `Mag. Pichle` — partial — pred is substring of gold: `ECA Mag. Pichler & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Lehwaldt`(person)
- `Waltraud Hinterlandt`(person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich`(address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lewis Rzehula`(person)
- `Neustädterstraße 3, 9560 Wabl, Österreich`(address)
- `43-839/6567`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Dr` — partial — pred is substring of gold: `Univ.-Prof.in Dr.in Hemma Ramelow`

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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`
- `Mag. Robert Bitsche` — partial — pred is substring of gold: `RA Mag. Robert Bitsche`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Roxana Dellner`(person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich`(address)
- `RA Mag. Robert Bitsche`(person)
- `Magistrats der Stadt Wien`(organisation)
- `88-034/0292`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Günter Gopfauf`(person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich`(address)
- `Finanzamtes Salzburg – Stadt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

**False Positives:**

- `StR DDr.in Rene` — partial — pred is substring of gold: `Prof.in StR DDr.in Reneé Plein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Daisy Hoopt`(person)
- `Prof.in StR DDr.in Reneé Plein`(person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_16`)


Nachdem binnen der zweiwöchigen Frist (§ 2 Abs. 2 Wiener Parkometergesetz 2006) keine  Lenkerauskunft erteilt wurde, lastete der Magistrat der Stadt Wien, MA 67, Prof.in StR DDr.in Reneé Plein  (Beschwerdeführer, kurz: Bf.) als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin des näher bezeichneten Fahrzeuges mit Strafverfügung vom 25. März  2020, MA67/456/2020, an, dass er dem ordnungsgemäß zugestellten  Lenkerauskunftsersuchen der MA 67 vom 23. Jänner 2020 innerhalb von zwei Wochen ab  Zustellung nicht entsprochen habe.

**False Positives:**

- `StR DDr.in Rene` — partial — pred is substring of gold: `Prof.in StR DDr.in Reneé Plein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Prof.in StR DDr.in Reneé Plein`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `VetR OMedR Constantin Wiedewilt`(person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich`(address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Heinz Herper`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_71`)


Dr. Maida, Neurologie- und Psychiatriefachärztin.

**False Positives:**

- `Dr. Maida` — partial — pred is substring of gold: `Dr. Maida,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Maida,`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_89`)


Lebt  seit 2005 in teilbetreuter intensiver WG/Verein B. Seit ca. 2012 von Dr. Hofer-Zeni  besachwaltet.

**False Positives:**

- `Dr. Hofer` — partial — pred is substring of gold: `Dr. Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hofer-Zeni`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von Dr. Thomas Hofer-Zeni vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`
- `Dr. Thomas Hofer` — similar text (different position): `Dr. Thomas Hofer-Zeni`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamt`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_149`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Der Bf. wohnt seit 18. Dezember 2006 in Im Mühlfeld 20n, 3205 Weinburg, Österreich /52, Verein B. Der Verein betreut  Erwachsene, Unterstützungsform: teilbetreut intensiv.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)


Wenn der Sachwalter die Einvernahme von Prof. Maida als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der Neurologin Univ.Prof. Dr. Eva Maria Maida im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

**False Positives:**

- `Dr. Eva Maria Maida` — partial — pred is substring of gold: `Neurologin Univ.Prof. Dr. Eva Maria Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)
- `Bundesfinanzgericht`(organisation)
- `Neurologin Univ.Prof. Dr. Eva Maria Maida`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Mag. Dirk Bröders`(person)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `77-629/3506`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Hartwig Simonson`(person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Daisy Große` — partial — pred is substring of gold: `Hon.-Prof.in Daisy Große-Bölting`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

**False Positives:**

- `KommR Ing. Ludwig Taspinar` — partial — pred is substring of gold: `KommR Ing. Ludwig Taspinar, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `KommR Ing. Ludwig Taspinar, MA`(person)
- `Alt Lenzing 13, 4076 Karling, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131857.1`) (sent_id: `deanon_BFG_20260814_TEST/131857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterD in der Beschwerdesache VetR Eduard van den Berge, Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich, über die Beschwerde vom 6. Juni 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 31. Mai 2019 betreffend Rückforderung Familienbeihilfe und  Kinderabsetzbetrag für September 2018 bis Mai 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `VetR Eduard` — partial — pred is substring of gold: `VetR Eduard van den Berge`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Eduard van den Berge`(person)
- `Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

**False Positives:**

- `Mag. Andrea Müller` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Shoshana Döllmann`(person)
- `U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_26`)


Die Bf. legte dem Vorlageantrag zum Nachweis der rechtzeitigen Einreichung der Beschwerde  ein als Beschwerde bezeichnetes Schreiben vom 25.01.2018 versehen mit einer Klebevignette  der österreichischen Post mit dem Aufdruck „R Einschreiben“ und der   Nr.: „RQ 40 412 744 0 AT“ in Kopie bei.

**False Positives:**

- `R Einschreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `genitive_name_no_title` 🏆

**F1:** 0.033 | **Precision:** 0.329 | **Recall:** 0.017  

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
| 0.329 | 0.017 | 0.033 | 85 | 28 | 57 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 28 | 57 | 1586 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

| Predicted | Gold |
|---|---|
| `Günter Gopfauf` | `Günter Gopfauf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Maria-Luise Wohlmayr` (person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich` (address)
- `Finanzamtes Salzburg – Stadt` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der Cathleen Gröneweg, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Cathleen Gröneweg` | `Cathleen Gröneweg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Shoshana Döllmann` | `Shoshana Döllmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des Rocco Choudhury, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Rocco Choudhury` | `Rocco Choudhury` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wachtelgasse 7, 9543 Stadt, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_3`)


über die Beschwerde des Lukas Niedergesess, Staudenstraße 7, 3834 Eisenreichs, Österreich, Deutschland, vom 16. Februar 2021, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 13. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1 Parkometer- gesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Lukas Niedergesess` | `Lukas Niedergesess` |

**Missed by this rule (FN):**

- `Staudenstraße 7, 3834 Eisenreichs, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_2`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde der Michael Klingsohr, Hochburg 78, 4363 Pabneukirchen, Österreich, vom 09. Dezember  2016 gegen den Bescheid des Magistrats der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

| Predicted | Gold |
|---|---|
| `Michael Klingsohr` | `Michael Klingsohr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Hochburg 78, 4363 Pabneukirchen, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/135913.1`) (sent_id: `deanon_BFG_20260814_TEST/135913.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/136624.1`) (sent_id: `deanon_BFG_20260814_TEST/136624.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde der  Zlatan Wetterling, Am Kochfeld 129, 4770 Oberndorf, Österreich, vom 21. November 2019, gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 8. November 2019 betreffend gemäß § 8a FLAG gekürzte  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Zlatan Wetterling` | `Zlatan Wetterling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Doktor` (person)
- `Am Kochfeld 129, 4770 Oberndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140663.1`) (sent_id: `deanon_BFG_20260814_TEST/140663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde des Jessica Tenbrink, Dornlandweg 6, 8354 Risola, Österreich, vom 29. August 2022, gegen den Bescheid des  Finanzamtes Österreich vom 17. August 2022, betreffend Abweisung des Antrages auf  Gewährung von Familienbeihilfe ab Mai 2022, zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jessica Tenbrink` | `Jessica Tenbrink` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Dornlandweg 6, 8354 Risola, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/141690.1`) (sent_id: `deanon_BFG_20260814_TEST/141690.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Konrad über die Beschwerde  des Wilhelm Möncher, Hernalser Gürtel 1, 3192 Furthof, Österreich, vom 4. Juli 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26. Juni 2023, GZ.  MA67/Zahl/2023, wegen einer Verwaltungsübertretung gemäß § 5 Abs 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen  und das angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Wilhelm Möncher` | `Wilhelm Möncher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Konrad` (person)
- `Hernalser Gürtel 1, 3192 Furthof, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/143969.1`) (sent_id: `deanon_BFG_20260814_TEST/143969.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/144910.1`) (sent_id: `deanon_BFG_20260814_TEST/144910.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Maria Daniel über die Beschwerde der Diana Wüste,Schönangerweg 35, 4925 Gumpling, Österreich, vertreten durch Ing. Mag. Dr. Roland Erwin Hansely, Mahlerstraße 13 Tür 3,  1010 Wien, wegen behaupteter rechtswidriger Ausübung verwaltungsbehördlicher Befehls-  und Zwangsgewalt durch Organe des Zollamtes Österreich am 19.11.2023 durch Ausübung  psychischen Zwangs den Beschluss:   Die Maßnahmenbeschwerde vom 19.12.2023 wird als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Diana Wüste` | `Diana Wüste` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Maria Daniel` (person)
- `Schönangerweg 35, 4925 Gumpling, Österreich` (address)
- `Ing. Mag. Dr. Roland Erwin Hansely` (person)
- `Zollamtes Österreich` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Jeanne Pavlovitsch, Döbinggasse 9, 4153 Kirchbach, Österreich, vom 5. August 2024, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67 vom 31. Juli 2024, GZ. MA67/GZ/2024, mit  dem der Einspruch vom 12. Juni 2024 gegen die Strafverfügung vom 4. Juni 2024, mit  derselben Geschäftszahl, gemäß § 13 Abs. 3 AVG iVm § 24 VStG 1991 zurückgewiesen wurde,  zu Recht:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird der oben genannte, angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Döbinggasse 9, 4153 Kirchbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde der Helge Schilsong, Jheringgasse 45, 3950 Wielands, Österreich, vom 6. September 2024 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 3.  September 2024, GZ. MA67/GZ1/2024, mit dem der Einspruch vom 24. Juli 2024 gegen die  Strafverfügung vom 27. Mai 2024, GZ. MA67/GZ1/2024, gemäß § 49 Abs. 1 VStG 1991  zurückgewiesen wurde, zu Recht:    Der Beschwerde wird gemäß § 50 VwGVG Folge gegeben und der angefochtene  Zurückweisungsbescheid aufgehoben.

| Predicted | Gold |
|---|---|
| `Helge Schilsong` | `Helge Schilsong` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Jheringgasse 45, 3950 Wielands, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146931.1`) (sent_id: `deanon_BFG_20260814_TEST/146931.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  der Jeffrey Heilmayr, Johann Holzmann-Straße 222, 4912 Ponneredt, Österreich, vom 20. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 15. März 2023, mit dem der Antrag auf Familienbeihilfe und  Erhöhungsbetrag  ab August 2022 abgewiesen wurde, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jeffrey Heilmayr` | `Jeffrey Heilmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Johann Holzmann-Straße 222, 4912 Ponneredt, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_1`)


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

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_15`)


Enthält ein Bescheid die Ankündigung, dass noch  eine Begründung zum Bescheid ergehen wird, so wird die Beschwerdefrist nicht vor  Bekanntgabe der fehlenden Begründung oder der Mitteilung, dass die Ankündigung als  gegenstandslos zu betrachten ist, in Lauf gesetzt.

**False Positives:**

- `Ankündigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Hedwig Mackiewicz`(person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Finanzamt Wien` — partial — pred is substring of gold: `Finanzamt Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Guntram Antepoth`(person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `70-875/4351`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Finn van Aken, Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich, vertreten durch Mag. Musa Işlek, Achardgasse 6,  1210 Wien, über die Beschwerde vom 29. Juni 2018 gegen den Bescheid des Finanzamtes Wien  1/23 vom 28. Mai 2018 betreffend Umsatzsteuer 2016 zu Recht:   1.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Adebiola Bayer`(person)
- `Finn van Aken`(person)
- `Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich`(address)
- `Mag. Musa Işlek`(organisation)
- `Finanzamtes Wien  1/23`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Laetitia Kuban, Karawankenplatz 8, 8046 Graz, Österreich, über die Beschwerde vom 16. Dezember 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 14. November 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für das Kind x in den Zeiträumen vom 01.07.2018 bis zum 30.09.2018  sowie vom 01.07.2019 bis zum 30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Laetitia Kuban`(person)
- `Karawankenplatz 8, 8046 Graz, Österreich`(address)
- `Finanzamtes  Wien 2/20/21/22`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_33`)


Es wäre  Sache des Abgabepflichtigen, zumutbar und zu erwarten gewesen, bei seinem Vertreter, die  Zahlung des bereits erlegten Geldes zu veranlassen.

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_29`)


Es sei Sache des Beschuldigten, initiativ alles  darzulegen, was seiner Entlastung dienen könne.

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_50`)


Im Fall eines Ungehorsamsdelikts sei es Sache des Beschuldigten, initiativ alles darzulegen, was  seiner Entlastung dienen könne.

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Heinz Herper`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der Cathleen Gröneweg, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Klagenfurt` — type mismatch — same span as gold: `Finanzamtes Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cathleen Gröneweg`(person)
- `Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich`(address)
- `Finanzamtes Klagenfurt`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19  Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_116`)


Es ist daher Sache des Steuerpflichtigen, die ausschließliche oder ganz  überwiegend berufliche Verwendung aufzuzeigen (vgl. Baldauf in Jakom, EStG, 2017, § 20 Rz  90).

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_80`)


Nach der Judikatur des Verwaltungsgerichtshofes ist es Sache der Behörde, die einzelnen  Beweismittel nach ihrer Zweckdienlichkeit für die Erfüllung der Pflicht der Behörde zur  Ermittlung der materiellen Wahrheit unter Berücksichtigung der nach Lage des Falles  gebotenen Zweckmäßigkeit und Verfahrensökonomie auszuwählen.

**False Positives:**

- `Behörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/131857.1`) (sent_id: `deanon_BFG_20260814_TEST/131857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterD in der Beschwerdesache VetR Eduard van den Berge, Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich, über die Beschwerde vom 6. Juni 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 31. Mai 2019 betreffend Rückforderung Familienbeihilfe und  Kinderabsetzbetrag für September 2018 bis Mai 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Eduard van den Berge`(person)
- `Franz-Sauer-Platz 5, 4710 Wackersbuch, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_80`)


Enthält ein Bescheid die Ankündigung,  dass noch eine Begründung zum Bescheid ergehen wird, so wird die Beschwerdefrist nicht vor  Bekanntgabe der fehlenden Begründung oder der Mitteilung, dass die Ankündigung als  5 von 8 Seite 6 von 8

**False Positives:**

- `Ankündigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache OSR Juliette Franzisi, Spitzesed 172, 4673 Baumgarting, Österreich, über die Beschwerde vom 17. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 17. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 47-760/2078  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Juliette Franzisi`(person)
- `Spitzesed 172, 4673 Baumgarting, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)
- `47-760/2078`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_14`)


Enthält ein Bescheid die Ankündigung, dass noch  eine Begründung zum Bescheid ergehen wird, so wird die Beschwerdefrist nicht vor  Bekanntgabe der fehlenden Begründung oder der Mitteilung, dass die Ankündigung als  gegenstandslos zu betrachten ist, in Lauf gesetzt.

**False Positives:**

- `Ankündigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  8/16/17`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Marcel Rac`(person)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich`(address)
- `Finanzamtes Wien  8/16/17`(organisation)
- `42-508/7924`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_37`)


Erst 2019 wurde von Ihnen der Bescheid des Landes 0Ö über die Flurbereinigung vorgelegt.

**False Positives:**

- `Landes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — similar text (different position): `Finanzamtes Wien 2/20/21/22`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Janis Dührkopp`(person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniel Philip Pfau`(person)
- `Prof.in Julia Mundle`(person)
- `Leitersdorf 2, 9344 Psein, Österreich`(address)
- `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `23-019/8335`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_25`)


Enthält ein Bescheid die Ankündigung, dass noch  eine Begründung zum Bescheid ergehen wird, so wird die Beschwerdefrist nicht vor  Bekanntgabe der fehlenden Begründung oder der Mitteilung, dass die Ankündigung als  gegenstandslos zu betrachten ist, in Lauf gesetzt.

**False Positives:**

- `Ankündigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Desiree Ince`(person)
- `Geigergasse 49, 5324 Hintersee, Österreich`(address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-822/3731`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Juri Siebgen`(person)
- `Josef Maurergasse 2, 5424 Riedl, Österreich`(address)
- `MITTEREGGER Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `35-670/1415`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Klaus Krupok  in der Beschwerdesache Ernst Eschenbrenner,  Irenental 58, 4871 Tiefenbach, Österreich, über die Beschwerde vom 11. August 2016 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich)vom 13. Juli  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 Steuernummer  80-953/9265  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Klaus Krupok`(person)
- `Ernst Eschenbrenner`(person)
- `Irenental 58, 4871 Tiefenbach, Österreich`(address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `80-953/9265`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_21`)


Enthält ein Bescheid die  Ankündigung, dass noch eine Begründung zum Bescheid ergehen wird, so wird die  Berufungsfrist nicht vor Bekanntgabe der fehlenden Begründung oder der Mitteilung, dass die  Ankündigung als gegenstandslos zu betrachten ist, in Lauf gesetzt.

**False Positives:**

- `Ankündigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Engelbert Voglsang  in der Beschwerdesache DDr.in Magdalena Holtzbecher, Bakk. rer. nat.,  Kefergutstraße 149, 5152 Dorfbeuern, Österreich, über die Beschwerde vom 29.3.2020 gegen den Bescheid des Finanzamtes  Wien 1/23 vom 12.3.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) für das  Jahr 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Engelbert Voglsang`(person)
- `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`(person)
- `Kefergutstraße 149, 5152 Dorfbeuern, Österreich`(address)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/137477.1`) (sent_id: `deanon_BFG_20260814_TEST/137477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Alva Danell, Robert Lieben-Promenade 68, 5251 Thalheim, Österreich, vertreten durch Nikolaus WP GmbH Rnf. ÖBUG KG, St Veitg 8, 1130  Wien, über die Beschwerde vom 6. März 2014 gegen den Bescheid des Finanzamtes Wien  9/18/19 Klosterneuburg vom 10. Februar 2014 betreffend Einkommensteuer 2012  Steuernummer 48-595/6877  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Stefan Pipal`(person)
- `Alva Danell`(person)
- `Robert Lieben-Promenade 68, 5251 Thalheim, Österreich`(address)
- `Nikolaus WP GmbH Rnf. ÖBUG KG`(organisation)
- `Finanzamtes Wien  9/18/19 Klosterneuburg`(organisation)
- `48-595/6877`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_31`)


Als Sache des Beschwerdeverfahrens, somit als Prozessgegenstand des  verwaltungsgerichtlichen Verfahrens, ist jene Angelegenheit anzusehen, die den Inhalt des  Spruches des Bescheides der belangten Behörde gebildet hat (vgl. für viele etwa VwGH  10.11.2015, Ro 2015/19/0001, oder VwGH 29.01.2015, 2012/15/0030).

**False Positives:**

- `Beschwerdeverfahrens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Leonhard Osskinat, Schreyvogelgasse 2V, 8262 Leithen, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid des Finanzamtes  Baden Mödling, nunmehr Finanzamt Österreich, vom 18. Oktober 2019 betreffend Abweisung  des Antrages vom 3. September 2019 auf Gewährung des Erhöhungsbetrages zur  Familienbeihilfe für Hartmut Groebmair  ab Juli 2019,   Steuernummer 39-801/9564, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Baden Mödling` — type mismatch — same span as gold: `Finanzamtes  Baden Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Leonhard Osskinat`(person)
- `Schreyvogelgasse 2V, 8262 Leithen, Österreich`(address)
- `Finanzamtes  Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)
- `Hartmut Groebmair`(person)
- `39-801/9564`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_2`)


Die Beschwerde vom 28.12.2020 gegen die Bescheide des Finanzamtes Österreich je  vom 27.11.2020 bezüglich Wiederaufnahme der Verfahren die Einkommensteuer  2014-2018 betreffend gilt gemäß § 278 Abs. 1 lit. b BAO als zurückgenommen.

**False Positives:**

- `Einkommensteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_17`)


Mit Bescheiden jeweils datierend mit 27.11.2020 wurden einerseits die Verfahren die  Einkommensteuer 2014-2018 betreffend gemäß § 303 Abs. 1 BAO wiederaufgenommen und  gleichzeitig neue Sachbescheide erlassen;

**False Positives:**

- `Einkommensteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19  Klosterneuburg`
- `Finanzamtes Wien` — similar text (different position): `Finanzamtes Wien 9/18/19  Klosterneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Brendon Spade`(person)
- `OMedR Milena Piechulik`(person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich`(address)
- `Walther Kendler`(person)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `16-827/1246`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alva Volgenandt  in der Beschwerdesache Pawel Smock,  Kongreßbad 9, 6811 Göfis, Österreich, vertreten durch Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH, Geusaugasse 39 Tür 8, 1030 Wien, 1.) über die Beschwerde vom 28.02.2014 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 27.01.2014 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2.) über die Beschwerde vom  28.07.2014 gegen den Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom  30.06.2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012, Steuernummer  20-852/2672, nach der am 19.10.2022 durchgeführten mündlichen Verhandlung zu Recht  erkannt:     I. Die Beschwerden werden als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`
- `Finanzamtes Wien` — similar text (different position): `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Alva Volgenandt`(person)
- `Pawel Smock`(person)
- `Kongreßbad 9, 6811 Göfis, Österreich`(address)
- `Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `20-852/2672`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Andreas Domingo  in der Beschwerdesache Univ.-Prof.in KzlR Tiffany Nowakowsky,  Thumastraße 13, 5201 Brunn, Österreich, vertreten durch "ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, St.-Veit-Gasse 8, 1130 Wien, über die  Beschwerde vom 14. April 2020 gegen den Bescheid des Finanzamtes Wien 1/23 vom 2. März  2020 betreffend die Abweisung eines Zahlungserleichterungsansuchens, Steuernummer  75-144/0441, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Andreas Domingo`(person)
- `Univ.-Prof.in KzlR Tiffany Nowakowsky`(person)
- `Thumastraße 13, 5201 Brunn, Österreich`(address)
- `DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `75-144/0441`(tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_6`)


Mit Bescheid des Finanzamtes Wien 1/23 vom 2. März 2020 wurde das Ansuchen um  Bewilligung einer Zahlungserleichterung mit der Begründung abgewiesen, dass keine  erhebliche Härte erblickt werden könne.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 1/23`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 1/23`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_55`)


„Unterlaufen im Verfahren der Zustellung Mängel, so gilt die Zustellung als in dem Zeitpunkt  dennoch bewirkt, in dem das Dokument dem Empfänger tatsächlich zugekommen ist.“

**False Positives:**

- `Zustellung Mängel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/140202.1`) (sent_id: `deanon_BFG_20260814_TEST/140202.1_4`)


In der Folge erhob der Bf. mit Eingabe vom 22. Mai 2015 gegen vorgenannte Bescheide eine  Beschwerde des Inhalts, dass in Anbetracht, des Vorliegens der Hauptwohnsitzbefreiung nach  § 30 Abs. 1 Z 1 lit. a EStG 1998 weder Einkommensteuer noch darauf basierenden  Anspruchszinsen festzusetzen seien.

**False Positives:**

- `Inhalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/140311.1`) (sent_id: `deanon_BFG_20260814_TEST/140311.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Reinhard Milschlag  in der Beschwerdesache Melanie Guidi,  Scheatlers Wies 27, 3633 Dorfstadt, Österreich, über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 5. Juni 2019 betreffend die Bewilligung einer Zahlungserleichterung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Reinhard Milschlag`(person)
- `Melanie Guidi`(person)
- `Scheatlers Wies 27, 3633 Dorfstadt, Österreich`(address)
- `Finanzamtes  Wien 4/5/10`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/140311.1`) (sent_id: `deanon_BFG_20260814_TEST/140311.1_5`)


Mit Bescheid des Finanzamtes Wien 4/5/10 vom 5. Juni 2019 wurde das Ansuchen um  Bewilligung einer Zahlungserleichterung mit der Begründung abgewiesen, das Ansuchen  enthalte keine Begründung.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 4/5/10`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/140320.1`) (sent_id: `deanon_BFG_20260814_TEST/140320.1_20`)


Enthält ein Bescheid die  Ankündigung, dass noch eine Begründung zum Bescheid ergehen wird, so wird die  Beschwerdefrist nicht vor Bekanntgabe der fehlenden Begründung oder der Mitteilung, dass  die Ankündigung als gegenstandslos zu betrachten ist, in Lauf gesetzt.

**False Positives:**

- `Ankündigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/140554.1`) (sent_id: `deanon_BFG_20260814_TEST/140554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Beschwerdesache Rinaldo Steckenmesser, Karl Hagl-Straße 8, 4903 Starling, Österreich, über die Beschwerde vom 3. Juni 2019 gegen  den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 2. Mai 2019 betreffend die  Festsetzung von Zwangsstrafen 2019, Steuernummer 76-764/5431, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karoline Windsteig`(person)
- `Rinaldo Steckenmesser`(person)
- `Karl Hagl-Straße 8, 4903 Starling, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `76-764/5431`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/141066.1`) (sent_id: `deanon_BFG_20260814_TEST/141066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Hon.-Prof. Dragan Neisemeyer  über die Beschwerde der Haendl Wind GmbH, Parseier 13, 4421 Pieslwang, Österreich, vertreten durch die Puntigam Wirtschaftstreuhand und  Steuerberatung GmbH, Hauptstraße 39, 8093 St. Peter am Ottersbach, vom 29.09.2020 gegen  den Bescheid des Finanzamtes Graz-Umgebung vom 11.03.2020 betreffend Umsatzsteuer 2017  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Haendl Wind` — partial — pred is substring of gold: `Haendl Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dragan Neisemeyer`(person)
- `Haendl Wind GmbH`(organisation)
- `Parseier 13, 4421 Pieslwang, Österreich`(address)
- `Puntigam Wirtschaftstreuhand und  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/141392.1`) (sent_id: `deanon_BFG_20260814_TEST/141392.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Michaela Ondracsek, Arnsdorfer Straße 153, 4881 Kronberg, Österreich, über die Beschwerde vom 11. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 30. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-938/6957  zu Recht erkannt:   I.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Michaela Ondracsek`(person)
- `Arnsdorfer Straße 153, 4881 Kronberg, Österreich`(address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `92-938/6957`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_59`)


Unterlaufen im Verfahren der Zustellung Mängel, so gilt die Zustellung gemäß § 7 Abs 1  Zustellgesetz als in dem Zeitpunkt dennoch bewirkt, in dem das Dokument dem Empfänger  tatsächlich zugekommen ist.

**False Positives:**

- `Zustellung Mängel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_27`)


Die Beschwerdevorentscheidung wurde an den steuerlichen Vertreter mit RSb Brief  nachweislich am 22.7.2022 zugestellt.  Der steuerliche Vertreter der Bf. brachte am 1.8.2022 fristgerecht einen Vorlageantrag gemäß  § 264 BAO ein, beantragte die Abhaltung einer mündlichen Verhandlung und führte ergänzend  folgendes aus:  „Strittig ist im gegenständlichen Verfahren die Frage, ob die 28.10.2021 ausgestellte  Erinnerung zur Meldung der wirtschaftlichen Eigentümer gemäß § 5 Wirtschaftliche Eigentümer  Register Gesetz und die in diesem Schreiben unter Androhung einer Zwangsstrafe angekündigte  Nachmeldefrist ordnungsgemäß zugestellt wurde.

**False Positives:**

- `Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Beschwerdesache Heinrich Rzeppa, LLM, Toulagasse 1, 8111 Straßengel, Österreich, vertreten durch Dr. Martin Weiser, Landstraßer  Hauptstraße 60, 1030 Wien, über die Beschwerde vom 04. März 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 31. Jänner 2019 betreffend Umsatzsteuer 2016, Steuernummer  52-580/0972  beschlossen:  I. Die Parteien werden gem. § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Verwaltungsgerichts noch eine Beschwerdevorentscheidung zu erlassen ist.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 4/5/10`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karoline Windsteig`(person)
- `Heinrich Rzeppa, LLM`(person)
- `Toulagasse 1, 8111 Straßengel, Österreich`(address)
- `Dr. Martin Weiser`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `52-580/0972`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_15`)


Der Bescheid des Finanzamtes, mit dem der Umsatzsteuerjahresbescheides 2016 vom  19.07.2018 aufgehoben wurde, wurde ordnungsgemäß am 28.01.2019 zugestellt und ist in  Rechtskraft erwachsen.

**False Positives:**

- `Finanzamtes` — type mismatch — same span as gold: `Finanzamtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_31`)


Es sei Sache des Beschuldigten,  initiativ alles darzulegen, was seiner Entlastung dienen könne.

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/146621.1`) (sent_id: `deanon_BFG_20260814_TEST/146621.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Werner Holtmeier, In der Scheibe 3N, 4722 Ratzling, Österreich, vertreten durch EASYTAX Steuerberatungsgesellschaft mbH,  Veithgasse 6, 1030 Wien, über die Beschwerde vom 12. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf (nunmehr Finanzamt Österreich)  vom 9. Dezember 2019 betreffend Säumniszuschlag 2019 Steuernummer 11-505/9535  zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Lisa Fries`(person)
- `Werner Holtmeier`(person)
- `In der Scheibe 3N, 4722 Ratzling, Österreich`(address)
- `EASYTAX Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `11-505/9535`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/146646.1`) (sent_id: `deanon_BFG_20260814_TEST/146646.1_60`)


Die Feststellungen zur Minderung der Erwerbsfähigkeit von 70% und der zugrundeliegenden  Erkrankung sind durch den Bescheid des Landesinvalidenamtes, den Behindertenpass, den  Parkausweis und die Vorbringen der Bf. hinreichend dokumentiert.

**False Positives:**

- `Landesinvalidenamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_45`)


Das Finanzamt folgte den Feststellungen der Betriebsprüfung und erließ nach  Wiederaufnahme der Verfahren die Körperschaftsteuerbescheide 2014, 2015, 2016 (jeweils  vom 25.03.2019), die Umsatzsteuerbescheide 2014, 2015, 2016 (jeweils vom 25.03.2019), die  Bescheide über die Festsetzung von Umsatzsteuer 12/2017 und 12/2018 vom jeweils  25.03.2019, sowie die Haftungsbescheide Kapitalertragsteuer 01/2014, 12/2014, 12/2015,  12/2016 und 12/2017 vom jeweils 21.03.2019.

**False Positives:**

- `Körperschaftsteuerbescheide` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/147657.1`) (sent_id: `deanon_BFG_20260814_TEST/147657.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hemma Fieber  in der Beschwerdesache Eleonore Isenhardt,  Bachwiesenstraße 12, 6401 Inzing, Österreich, vertreten durch TPA Regio Steuerberatung GmbH, Schwedengasse 2, 3500  Krems/Donau, über die Beschwerde vom 22. Mai 2019 gegen den Bescheid des Finanzamtes  Wien 12/13/14 Purkersdorf vom 6. Mai 2019 betreffend die Wiederaufnahme des Verfahrens  gem § 303 Abs 1 BAO hinsichtlich der Einkommensteuer 2010 zu Steuernummer  94-874/0419  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes  Wien` — partial — pred is substring of gold: `Finanzamtes  Wien 12/13/14 Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hemma Fieber`(person)
- `Eleonore Isenhardt`(person)
- `Bachwiesenstraße 12, 6401 Inzing, Österreich`(address)
- `TPA Regio Steuerberatung GmbH`(organisation)
- `Finanzamtes  Wien 12/13/14 Purkersdorf`(organisation)
- `94-874/0419`(tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/148480.1`) (sent_id: `deanon_BFG_20260814_TEST/148480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Reinhold Jonasius, Johann Tagwerker-Straße 17, 5760 Pabing, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, über die Beschwerde vom 28.08.2015 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 22. Juni 2015  betreffend Festsetzung der Kapitalertragsteuer 2011 – 2013, Steuernummer 81-937/8981  nach Durchführung einer mündlichen Verhandlung am 31. Jänner 2025 zu Recht erkannt:   I. Der Beschwerde wird als teilweise Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien  3/6/7/11/15`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Reinhold Jonasius`(person)
- `Johann Tagwerker-Straße 17, 5760 Pabing, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)
- `Finanzamt Österreich`(organisation)
- `81-937/8981`(tax_number)

</details>

---

## `represented_by` 🏆

**F1:** 0.017 | **Precision:** 0.179 | **Recall:** 0.009  

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
| 0.179 | 0.009 | 0.017 | 78 | 14 | 64 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 14 | 64 | 1600 |

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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Florian Rouse  in der Beschwerdesache Evamaria Watenphul,  Allhartsbergerstraße 47, 8142 Kasten, Österreich, vertreten durch Mehmet Köprücü, Puchheimgasse 14, 6234 Brandenberg, Österreich, betreffend Beschwerde  vom 21. September 2022 gegen den Haftungsbescheid des Finanzamtes Österreich vom  6. September 2022, 83-456/1644, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mehmet Köprücü` | `Mehmet Köprücü` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Univ.-Prof. Florian Rouse` (person)
- `Evamaria Watenphul` (person)
- `Allhartsbergerstraße 47, 8142 Kasten, Österreich` (address)
- `Puchheimgasse 14, 6234 Brandenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-456/1644` (tax_number)

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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/147296.1`) (sent_id: `deanon_BFG_20260814_TEST/147296.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_51`)


Daraus folgt, dass der Einspruch gegen die Strafverfügung vom 3. September 2024 des M,  vertreten durch Pjotr Niessl, wieder unerledigt ist und die belangte Behörde darüber zu  entscheiden hat.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/148979.1`) (sent_id: `deanon_BFG_20260814_TEST/148979.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/149201.1`) (sent_id: `deanon_BFG_20260814_TEST/149201.1_2`)


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

- `Steuerberatungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rabel` — partial — pred is substring of gold: `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Ophelia Dutschka`(person)
- `Diepolding 3, 3754 Trabenreith, Österreich`(address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Kulmburg` — partial — pred is substring of gold: `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mehmet Gessl`(person)
- `Donau-Elektro`(organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich`(address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

**False Positives:**

- `Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Livia Korowski`(person)
- `Sven Mitterhuber`(person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

**False Positives:**

- `Gosteco Goworek` — partial — pred is substring of gold: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Elisabeth Brunner`(person)
- `Serge Pechert`(person)
- `Texing 43, 3143 Oberloitzenberg, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Heinz Neuböck Wthrd` — partial — pred is substring of gold: `Heinz Neuböck Wthrd GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Bernhart Steuerberatungs` — partial — pred is substring of gold: `Bernhart Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Eckert Fries Carter Rechtsanwälte` — partial — pred is substring of gold: `Eckert Fries Carter Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Anneliese Wäsche`(person)
- `Gernot Kirchenmayer`(person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich`(address)
- `Eckert Fries Carter Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Holzinger` — partial — pred is substring of gold: `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck`(person)
- `Felizitas Johanesson`(person)
- `Aspangweg 17, 9781 Gailberg, Österreich`(address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `48-504/5908`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Deloitte Tax  Wirtschaftsprüfungs` — partial — pred is substring of gold: `Deloitte Tax  Wirtschaftsprüfungs GmbH`

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

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

**False Positives:**

- `Proxauf Meyer Zeilinger Rechtsanwälte` — partial — pred is substring of gold: `Proxauf Meyer Zeilinger Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Andrea Helbok`(person)
- `Lydia Rehnen`(person)
- `Roßbergl 5, 4923 Gunzing, Österreich`(address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH`(organisation)
- `Finanzamtes  Innsbruck`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Böhm` — partial — pred is substring of gold: `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

**False Positives:**

- `Astoria Wirtschaftstreuhand` — partial — pred is substring of gold: `Astoria Wirtschaftstreuhand GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler`(person)
- `Esra Luetje`(person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich`(address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kastler Wirtschaftstreuhand` — partial — pred is substring of gold: `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lisa Lindnau`(person)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich`(address)
- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `35-287/7417`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

**False Positives:**

- `Burka Vitek Moser  Rechtsanwälte` — type mismatch — same span as gold: `Burka Vitek Moser  Rechtsanwälte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes`(organisation)
- `Petra Port`(person)
- `Konventweg 36, 4613 Unterholz, Österreich`(address)
- `Burka Vitek Moser  Rechtsanwälte`(organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Mag. Wolfgang Moser`(person)
- `Petra Port`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

**False Positives:**

- `Deloitte Tax Wirtschaftsprüfungs` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper`(person)
- `Julian Gruening`(person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hopmeier Wagner Kirnbauer  Rechtsanwälte` — partial — pred is substring of gold: `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniel Philip Pfau`(person)
- `Prof.in Julia Mundle`(person)
- `Leitersdorf 2, 9344 Psein, Österreich`(address)
- `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `23-019/8335`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Korber` — partial — pred is substring of gold: `Korber & Partner WTH-Stb  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Ingrid Dohrmaier`(person)
- `Daläus 14O, 2301 Wittau, Österreich`(address)
- `Korber & Partner WTH-Stb  GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf`(organisation)
- `Finanzamtes Österreich`(organisation)
- `41-654/1190`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Gutwirth Consulting Steuerberatungs` — partial — pred is substring of gold: `Gutwirth Consulting Steuerberatungs GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Prof.in Jeanne Sohns`(person)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich`(address)
- `Gutwirth Consulting Steuerberatungs GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

**False Positives:**

- `Obf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Wieland Starnberg`(person)
- `Ing. Linus Feyerherdt`(person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich`(address)
- `Christina Hildegard Stowasser`(person)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `Finanzamtes Österreich`(organisation)
- `98-011/6615`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/136624.1`) (sent_id: `deanon_BFG_20260814_TEST/136624.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die Beschwerde der Heiko Cortnumme, Barbarasiedlung D/ 3, 9314 Garzern, Österreich, vertreten durch Vertreter, vom 11. Dezember 2017 gegen die Bescheide des  Finanzamtes Österreich, vormals Finanzamtes Bruck Eisenstadt Oberwart, vom 3. Oktober  2017 betreffend Körperschaftsteuer 2006 und 2007, vom 12. Oktober 2017 betreffend  Körperschaftsteuer 2008 sowie vom 16. November 2017 betreffend Körperschaftsteuer 2018,  Steuernummer 01-857/0717, nach der am 9. März 2022 in Hintere Zollamstsstraße 2b,  1030 Wien, durchgeführten mündlichen Verhandlung im Beisein der Schriftführerin R zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Heiko Cortnumme`(person)
- `Barbarasiedlung D/ 3, 9314 Garzern, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `01-857/0717`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Techn R Edwin Lamken, Steindl 32, 4076 Lengau, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse 17,  1030 Wien, wegen Verletzung der Entscheidungspflicht betreffend die Beschwerde gegen den  Bescheid des Finanzamtes Österreich vom 29.07.2009 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Umsatzsteuer 2006 der Gammersbach&Pelstring Telekom GmbH  Steuernummer 53-479/4428  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm § 284 Abs. 7 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Caroline Toifl Rechtsanwalt` — partial — pred is substring of gold: `Caroline Toifl Rechtsanwalt GmbH`

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

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Causa Wirtschaftstreuhand` — partial — pred is substring of gold: `Causa Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Frederik von Gruber`(person)
- `Laila Klimenkow`(person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich`(address)
- `Causa Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Heike Lohoff, Odescalchigasse 154, 4264 Lichtenau, Österreich, vertreten durch Vertreter, AdrVertreter, über die Beschwerde vom 15. Juli 2015 gegen  den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr:  Finanzamt Österreich) vom 6. Juli 2015 betreffend Grunderwerbsteuer, Steuernummer  77-421/3532, Erfassungsnummer 10-2012, nach Durchführung von mündlichen  Verhandlungen am 13.10.2021 und 10.08.2022 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Heike Lohoff`(person)
- `Odescalchigasse 154, 4264 Lichtenau, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)
- `77-421/3532`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner als Vorsitzende, den  Richter Mag. Dieter Ortner sowie die fachkundigen Laienrichter Mag. Reinhard Krassnig und  Komm. Rat Max Stechauner in der Beschwerdesache Dirk Ambrose, Herrnberg 22, 5152 Schönberg, Österreich, vertreten  durch Kohlfürst, Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH, St. Veiter Ring  1A, 9020 Klagenfurt/Wörthersee, und Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerde vom 20. Dezember 2017 gegen den Bescheid des Finanzamtes  Klagenfurt (nunmehr Finanzamt Österreich) vom 23. November 2017 mit dem ein Antrag  gemäß § 303 Abs. 1 BAO vom 27. Februar 2017 auf Wiederaufnahme des Verfahrens  betreffend Einkommensteuer 2002, Steuernummer 21-063/4049, abgewiesen worden ist,  nach Durchführung einer mündlichen Verhandlung am 10. August 2022 in Anwesenheit der  Schriftführerin FOI Alexandra Dumpelnik zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Kohlfürst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Elisabeth Hafner`(person)
- `Mag. Dieter Ortner`(person)
- `Mag. Reinhard Krassnig`(person)
- `Komm. Rat Max Stechauner`(person)
- `Dirk Ambrose`(person)
- `Herrnberg 22, 5152 Schönberg, Österreich`(address)
- `Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `21-063/4049`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  Simone Philipzig, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hofer Leitinger Steuerberatung` — partial — pred is substring of gold: `Hofer Leitinger Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Philippa Beßerdich`(person)
- `Simone Philipzig`(person)
- `Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich`(address)
- `Hofer Leitinger Steuerberatung GmbH`(organisation)
- `FA Kirchdorf Perg Steyr`(organisation)
- `59-060/2086`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Bettina Füsslin  in der Beschwerdesache Univ.-Prof.in Anastasia Sebott,  Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich, vertreten durch Mag. jur.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Bettina Füsslin`(person)
- `Univ.-Prof.in Anastasia Sebott`(person)
- `Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Olivia Severien  in der Beschwerdesache  Denis Öztopal, Weidenbachstraße 3, 5131 Pimbach, Österreich, vertreten durch Pschera Steuerberatung GmbH, Gösser Straße 60,  8700 Leoben, über die Beschwerde vom 20. November 2013 gegen die zur Steuernummer 68- 060/6613 ergangenen Bescheide des Finanzamt Salzburg-Stadt (nun Dienststelle des Finanzamtes Österreich)  vom 22. Oktober 2013 betreffend Umsatz- und Einkommensteuer 2000  – 2010 zu Recht  erkannt:   I. Die Berufung/Beschwerde vom 20. Nov.

**False Positives:**

- `Pschera Steuerberatung` — partial — pred is substring of gold: `Pschera Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Olivia Severien`(person)
- `Denis Öztopal`(person)
- `Weidenbachstraße 3, 5131 Pimbach, Österreich`(address)
- `Pschera Steuerberatung GmbH`(organisation)
- `Finanzamt Salzburg-Stadt`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Olivia Rodenbach  in der Beschwerdesache Veit Dworatzeck,  Zehentberg 7, 4060 Rufling, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  24. Mai 2011 gegen den Bescheid des Finanzamtes Österreich vom 19. April 2011 betreffend  Einkommensteuer 2009 Steuernummer 82-692/9441  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Kanzlei Kiffmann` — partial — pred is substring of gold: `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Olivia Rodenbach`(person)
- `Veit Dworatzeck`(person)
- `Zehentberg 7, 4060 Rufling, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)
- `82-692/9441`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Imre Zeitner  in der Beschwerdesache des  Daisy Schlimme, Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich, vertreten durch Henning & Partner Steuerberatung GmbH,  Brockmanngasse 75, 8010 Graz, sowie durch Dr. Michael Kotschnigg, Franzensbrückenstraße 5,  1020 Wien, über die Beschwerde vom 15. Jänner 2016 gegen die Bescheide des Finanzamtes  Graz-Umgebung (nunmehr: Finanzamt Österreich) vom 9. Dezember 2015 betreffend   1) Wiederaufnahme der Verfahren hinsichtlich Umsatzsteuer 2009 bis 2011 sowie  2) Einkommensteuer und Umsatzsteuer je 2009 bis 2014   den BESCHLUSS gefasst:   I. Die angefochtenen Bescheide (sowie die bezüglichen Beschwerdevorentscheidungen)  werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an die Abgabenbehörde  aufgehoben.

**False Positives:**

- `Henning` — partial — pred is substring of gold: `Henning & Partner Steuerberatung GmbH`

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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hofer Leitinger Steuerberatung` — partial — pred is substring of gold: `Hofer Leitinger Steuerberatung  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Schrettl Herbert` — partial — pred is substring of gold: `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter Mag.a  Patricia Kathan-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin Isabella  Alexandra Längle in der Finanzstrafsache gegen VetR Vivian Hirtel, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

**False Positives:**

- `Dr` — similar text (different position): `Isabella  Alexandra Längle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Mag. Josef Ungericht`(person)
- `Mag. Armin Treichl`(person)
- `Mag.a  Patricia Kathan`(person)
- `Mag. Norbert Metzler`(person)
- `Isabella  Alexandra Längle`(person)
- `VetR Vivian Hirtel`(person)
- `Litzlberger Straße 14, 8530 Kresbach, Österreich`(address)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/140846.1`) (sent_id: `deanon_BFG_20260814_TEST/140846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Janosch Herr  in der Beschwerdesache des  René Schiekel, MSc, Auf der Kröß 1, 2151 Altmanns, Österreich, vertreten durch Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH, Gartenaugasse 3, 3500 Krems/Donau, über die Beschwerde vom 11. Juni 2019 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Sacha Katzensteiner Blauensteiner Rechtsanwälte` — partial — pred is substring of gold: `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Janosch Herr`(person)
- `René Schiekel, MSc`(person)
- `Auf der Kröß 1, 2151 Altmanns, Österreich`(address)
- `Sacha Katzensteiner Blauensteiner Rechtsanwälte  GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/141265.1`) (sent_id: `deanon_BFG_20260814_TEST/141265.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Revisionssache  Bertram Tienemann, Jura-Soyfer-Gasse 5, 8461 Ehrenhausen, Österreich  vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über den Antrag des  Revisionswerbers vom 20. April 2023, der Revision vom 20. April 2023 gegen das Erkenntnis  des Bundesfinanzgerichtes vom 6. Dezember 2022, RV/7103133/2013, betreffend  Einkommensteuer 2007 erhobenen außerordentlichen Revision aufschiebende Wirkung  zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Bertram Tienemann`(person)
- `Jura-Soyfer-Gasse 5, 8461 Ehrenhausen, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/141757.1`) (sent_id: `deanon_BFG_20260814_TEST/141757.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1, die weitere Richterin R2 und die  fachkundigen Laienrichterinnen R3 und R4 in der Beschwerdesache des Achmed Nann, Johann Neydhart-Weg 16h, 4151 Dobretshofen, Österreich, vertreten durch Wirtschaftstreuhand Tirol Steuerberatungsgesellschaft m.b.H & Co  KG, Rennweg 18, 6020 Innsbruck, über die Beschwerde vom 24. Mai 2017 gegen die Bescheide  des FA Klosterneuburg  vom 26. April 2017 betreffend Umsatzsteuer 2011, Einkommensteuer 2011 und  Anspruchszinsen 2011 zu Steuernummer 03-768/0502  in der mündlichen Verhandlung am  1. August 2023 S zu Recht erkannt:   I. Die Beschwerde gegen den Umsatzsteuerbescheid 2011 wird als unbegründet  abgewiesen.

**False Positives:**

- `Wirtschaftstreuhand Tirol` — partial — pred is substring of gold: `Wirtschaftstreuhand Tirol Steuerberatungsgesellschaft m.b.H & Co  KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Achmed Nann`(person)
- `Johann Neydhart-Weg 16h, 4151 Dobretshofen, Österreich`(address)
- `Wirtschaftstreuhand Tirol Steuerberatungsgesellschaft m.b.H & Co  KG`(organisation)
- `FA Klosterneuburg`(organisation)
- `03-768/0502`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/141952.1`) (sent_id: `deanon_BFG_20260814_TEST/141952.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Niklas Dankwarth, Schüttaustraße 10, 9753 Raggnitz, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse  17, 1030 Wien, über die Beschwerde vom 24. September 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. August 2020 betreffend Einkommensteuer 2018  Steuernummer 01-612/4118  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Caroline Toifl Rechtsanwalt` — partial — pred is substring of gold: `Caroline Toifl Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Niklas Dankwarth`(person)
- `Schüttaustraße 10, 9753 Raggnitz, Österreich`(address)
- `Caroline Toifl Rechtsanwalt GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `01-612/4118`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/142112.1`) (sent_id: `deanon_BFG_20260814_TEST/142112.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Martin C. WITTMANN in der  Beschwerdesache Chen Thiergarten, Recyclingstraße 4z, 9911 Vergein, Österreich, vertreten durch Lang & Partner Steuerberatung  GmbH & Co KG, Kapfenstein 123, 8353 Kapfenstein, über die Beschwerde der  beschwerdeführenden Partei vom 17. Juli 2023 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Bescheidaufhebung gem § 299 BAO vom 30. Dezember 2022 hinsichtlich der Bescheide  Umsatzsteuer 2019 und Feststellung von Einkünften gemäß § 188 BAO 2019, jeweils vom 7.  Jänner 2022, Steuernummer 91-654/5089  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Lang` — partial — pred is substring of gold: `Lang & Partner Steuerberatung  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Martin C. WITTMANN`(person)
- `Chen Thiergarten`(person)
- `Recyclingstraße 4z, 9911 Vergein, Österreich`(address)
- `Lang & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamt Österreich`(organisation)
- `91-654/5089`(tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter als Vorsitzende, die  Richterin Mag. Andrea Proidl als beisitzende Richterin sowie Mag. Martin Saringer und Mag.  Harald  Zeller als fachkundige Laienrichter in der Beschwerdesache Priv.-Doz.in Diana Pöppel, Spitalbergweg 20, 4775 Wagholming, Österreich,  vertreten durch Baldinger & Partner Unternehmens- und Steuerberatung GmbH, Ferrogasse  35, 1180 Wien, über die Beschwerde vom 9. September 2017 gegen die Bescheide des  Finanzamtes Wien 4/5/10 vom 17. Juli 2017 betreffend Umsatzsteuer 2010-2016,  Steuernummer 56-661/5349, nach Durchführung einer mündlichen Verhandlung am 9. Juni  2023 in Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Baldinger` — partial — pred is substring of gold: `Baldinger & Partner Unternehmens- und Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Judith Leodolter`(person)
- `Mag. Andrea Proidl`(person)
- `Mag. Martin Saringer`(person)
- `Mag.  Harald  Zeller`(person)
- `Priv.-Doz.in Diana Pöppel`(person)
- `Spitalbergweg 20, 4775 Wagholming, Österreich`(address)
- `Baldinger & Partner Unternehmens- und Steuerberatung GmbH`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)
- `56-661/5349`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Arnold Ulmke, Mazellegasse 14, 2870 Stübegg, Österreich, vertreten durch Steuerberatung, Adresse Steuerberatung, über die Beschwerde vom  17. November 2014 gegen die Bescheide des Finanzamtes St. Johann Tamsweg Zell am See  vom 20. Oktober 2014 betreffend Dienstgeberbeitrag 2009 - 2012 und Zuschlag zum  Dienstgeberbeitrag 2009 - 2012, Steuernummer 26-962/7724  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberatung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Arnold Ulmke`(person)
- `Mazellegasse 14, 2870 Stübegg, Österreich`(address)
- `Finanzamtes St. Johann Tamsweg Zell`(organisation)
- `26-962/7724`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. VN. NN., die Richterin Dr.in  Ri.N. sowie die fachkundigen Laienrichter Lena Pahlmann und Ch,Nn. in der Beschwerdesache  Esra Voskuhle, Brandstetterweg 76k, 4682 Buchet, Österreich, vertreten durch Beratungs GmbH, Str.x, plz Stadt, über die  Beschwerde vom 26. Juni 2019 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich Dienststelle  Sonderzuständigkeiten) vom 27. Mai 2019 betreffend Gebühren gemäß § 33 TP 20  Gebührengesetz (GebG) 1957 nach Durchführung einer mündlichen Verhandlung am  12. Oktober 2023 in Anwesenheit des Beschwerdeführers und dessen Ehegattin A.N.G und der  Schriftführerin Vn. Nn1 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Beratungs` — partial — pred is substring of gold: `Beratungs GmbH`

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

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/142998.1`) (sent_id: `deanon_BFG_20260814_TEST/142998.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Evelyn Schlessing, Koksbatteriestraße 7, 9560 Bichl, Österreich  vertreten durch Univ.Prof.i.R. Dr. Josef Werndl,  über die Beschwerde vom 27. Dezember 2022 gegen den Bescheid des Finanzamtes Österreich  vom 15. Dezember 2022 betreffend Einkommensteuer 2021 zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.Prof.i.R. Dr. Josef Werndl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Evelyn Schlessing`(person)
- `Koksbatteriestraße 7, 9560 Bichl, Österreich`(address)
- `Univ.Prof.i.R. Dr. Josef Werndl`(person)
- `Finanzamtes Österreich`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/143628.1`) (sent_id: `deanon_BFG_20260814_TEST/143628.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Dieter Fröhlich, den   Richter Mag. Christian Seywald, die fachkundigen Laienrichter Johannes Steiner und   Michael Kamper MSc über die Bescheidbeschwerde vom 24.07.2019 des Ulrike Ackermaier, Bakk. iur., Knödelhüttenstraße 12, 9184 Mühlbach, Österreich  vertreten durch Woditschka Steuerberatung GmbH, 2130 Mistelbach, Lanzendorfer  Hauptstraße 9/1, gegen die Umsatzsteuerbescheide für das Jahr 2017 und das Jahr 2018, vom  18.06.2019, des Finanzamtes Gänserndorf Mistelbach (nunmehr FA Österreich),  Steuernummer 75-013/8302, nach Durchführung einer mündlichen Verhandlung am 29.  Jänner 2024 in Anwesenheit des Schriftführers Dietmar Gratz  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Woditschka Steuerberatung` — partial — pred is substring of gold: `Woditschka Steuerberatung GmbH`

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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/143793.1`) (sent_id: `deanon_BFG_20260814_TEST/143793.1_2`)


Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache   DDr. OStR Ernst Brücklmaier, Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich  vertreten durch Beste & Partner Steuerberatung GmbH,  Perlhofgasse 2/2/8, 2372 Gießhübl, betreffend Beschwerde vom 20. September 2021 gegen  die Bescheide des Finanzamtes für Großbetriebe vom 2. September 2021 betreffend  Wiederaufnahme § 303 BAO Körperschaftsteuer der Jahre 2014-2016 sowie Wiederaufnahme  Körperschaftsteuer für das Jahr 2018, Steuernummer 87-802/5730  beschlossen:  Die Beschwerde wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Beste` — partial — pred is substring of gold: `Beste & Partner Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `DDr. OStR Ernst Brücklmaier`(person)
- `Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich`(address)
- `Beste & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `87-802/5730`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/143852.1`) (sent_id: `deanon_BFG_20260814_TEST/143852.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Albert Salzmann, die  Richterin Dr. Susanne Zankl sowie die fachkundigen Laienrichter Christine Höll und Dr. Rupert  Mayr in der Beschwerdesache Ewald Lüttfrenk, Triftgasse 9, 5145 Königsaich, Österreich, vertreten durch Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG, Forstamtsgasse 6, 5580 Tamsweg, über die  Beschwerde vom 30. März 2021 gegen die Bescheide des Finanzamtes Österreich vom  4. Februar 2020 betreffend Einkommensteuer 2014, 2015, 2016 und 2017 zur Steuernummer  55-257/7759  nach Durchführung einer mündlichen Verhandlung am 5. April 2023 in  Anwesenheit der Schriftführerin Premm Helene zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Etschbacher` — partial — pred is substring of gold: `Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Dr. Susanne Zankl`(person)
- `Christine Höll`(person)
- `Dr. Rupert  Mayr`(person)
- `Ewald Lüttfrenk`(person)
- `Triftgasse 9, 5145 Königsaich, Österreich`(address)
- `Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `55-257/7759`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

**False Positives:**

- `Prof` — similar text (different position): `Mag. Hon.-Prof. Denis Hoffjan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Denis Hoffjan`(person)
- `Hon.-Prof.in Ariadne Iwanowsky`(person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich`(address)
- `Prof. Yorick Frühbis`(person)
- `Finanzamt Österreich`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden A und die Richterin   Priv.-Doz.in Annkathrin Czesielski  sowie die fachkundigen Laienrichter B und C in der Beschwerdesache Prof.in Esra Konwischer,  Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 11. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 25. Juli 2016, ErfNr u.a., betreffend   1. Festsetzung der Gebühren gemäß § 14 TP 6 Abs. 2 Z 1, TP 2 Abs. 1 Z 1, TP 5 Abs. 1 und        TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Die Beschwerde wird insgesamt als unbegründet abgewiesen.

**False Positives:**

- `Zachmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Annkathrin Czesielski`(person)
- `Prof.in Esra Konwischer`(person)
- `Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jessica Buddeus  in der Beschwerdesache Heidemarie Helwig,  Schmittengasse 288, 3160 Maierhöfen, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 7. Februar 2024  gegen den Bescheid des FA Purkersdorf  vom 10. Jänner 2024 betreffend Abweisung eines Antrages  auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum  01.12.2022 bis 30.06.2023, Steuernummer 81-530/8966, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Jessica Buddeus`(person)
- `Heidemarie Helwig`(person)
- `Schmittengasse 288, 3160 Maierhöfen, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH`(organisation)
- `FA Purkersdorf`(organisation)
- `81-530/8966`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sabrina Ternes  in der Beschwerdesache Sheila Szikorra,  Brennersee 10, 9555 St. Gandolf, Österreich, vertreten durch Auxiliaris Steuerberatung GmbH, Grazer Straße 12, 8480  Mureck, über die Beschwerde vom 11. Jänner 2019 gegen den Bescheid des Finanzamtes  Klagenfurt vom 17. Dezember 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Steuernummer 67-828/8052  zu Recht erkannt:   I. Gemäß § 279 BAO wird die Beschwerde als unbegründet abgewiesen und wird der  angefochtene Bescheid abgeändert.

**False Positives:**

- `Auxiliaris Steuerberatung` — partial — pred is substring of gold: `Auxiliaris Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Sabrina Ternes`(person)
- `Sheila Szikorra`(person)
- `Brennersee 10, 9555 St. Gandolf, Österreich`(address)
- `Auxiliaris Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `67-828/8052`(tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/145014.1`) (sent_id: `deanon_BFG_20260814_TEST/145014.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ilse Leners  in der Beschwerdesache Herta Lindgens,  Ruth-Drexel-Weg 7, 4691 Schlatt, Österreich, vertreten durch Markl Rechtsanwälte OG, Schmerlingstraße 2, 6020 Innsbruck,  über die Beschwerde vom 20. Jänner 2022 gegen den Bescheid des Finanzamtes Österreich  vom 5. Jänner 2022, Str. Nr. X1, betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO   zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Markl Rechtsanwälte` — partial — pred is substring of gold: `Markl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ilse Leners`(person)
- `Herta Lindgens`(person)
- `Ruth-Drexel-Weg 7, 4691 Schlatt, Österreich`(address)
- `Markl Rechtsanwälte OG`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Woditschka  Steuerberatung` — partial — pred is substring of gold: `Woditschka  Steuerberatung GmbH`

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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/145955.1`) (sent_id: `deanon_BFG_20260814_TEST/145955.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Anita Volkermann, Bieleweg 10, 4263 Spörbichl, Österreich, vertreten durch Hallas & Partner, Praterstraße  38, 1020 Wien, über die Beschwerde vom 28. Dezember 2012 gegen die Bescheide des  Finanzamts Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom 30. November  2012 betreffend Einkommensteuer 2002 und 2004, Steuernummer 90-565/3892, zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hallas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Anita Volkermann`(person)
- `Bieleweg 10, 4263 Spörbichl, Österreich`(address)
- `Finanzamts Wien 9/18/19`(organisation)
- `Finanzamt Österreich`(organisation)
- `90-565/3892`(tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/145764.1`) (sent_id: `deanon_BFG_20260814_TEST/145764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Thassilo Wetekam, Moosen 81, 4926 Kleinbach, Österreich, vertreten durch Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die  Beschwerde vom 12. Juni 2024 gegen den Bescheid des Finanzamtes für Großbetriebe vom  13. Mai 2024 betreffend Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum  1. Juli 2023 bis 31. Dezember 2023, Steuernummer 89-352/4267, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Ebner`(person)
- `Thassilo Wetekam`(person)
- `Moosen 81, 4926 Kleinbach, Österreich`(address)
- `Zacherl Schallaböck Proksch  Manak Kraft Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `89-352/4267`(tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der Univ.-Prof. Julian Czernitzki, Faßlergasse 78L-80, 9612 Dellach, Österreich, vertreten durch Schneider Wirtschaftsprüfung und  Steuerberatung GmbH, 6845 Hohenems, Nibelungenstraße 19, über die Beschwerde vom  19.04.2019 gegen die Körperschaftsteuerbescheide 2014, 2015, 2016, gegen die  Umsatzsteuerbescheide 2014, 2015, 2016 (alle Bescheide vom 25.03.2019), gegen die  Bescheide über die Festsetzung von Umsatzsteuer für 12/2017 und 12/2018 vom jeweils  25.03.2019 (Umsatzsteuerbescheid 2017 vom 22.05.2020 und Umsatzsteuerbescheid 2018  vom 17.10.2023), sowie gegen die Haftungsbescheide Kapitalertragsteuer 01/2014, 12/2014,  12/2015, 12/2016 und 12/2017 (Bescheide jeweils vom 21.03.2019), zu Recht erkannt:  I. Der Beschwerde gegen die Körperschaftsteuerbescheide 2015 und 2016, die  Umsatzsteuerbescheide 2015, 2016, 2017 und 2018 wird Folge gegeben.

**False Positives:**

- `Schneider` — partial — pred is substring of gold: `Schneider Wirtschaftsprüfung und  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Univ.-Prof. Julian Czernitzki`(person)
- `Faßlergasse 78L-80, 9612 Dellach, Österreich`(address)
- `Schneider Wirtschaftsprüfung und  Steuerberatung GmbH`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frauke Orsini  in der Beschwerdesache Herbert Czarnezki,  Roacher Straße 40, 9241 Ragain, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 30. September 2019 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt  Österreich/FAÖ) vom 28. August 2019, Erf. Nr. Nr1,   betreffend  1. Festsetzung der Gebühren gemäß § 14 TP 2 Abs. 1 Z 1, TP 5 Abs. 1, TP 6 Abs. 1       und TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Der angefochtene Sammelbescheid wird abgeändert wie folgt:  1.

**False Positives:**

- `Zachmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Frauke Orsini`(person)
- `Herbert Czarnezki`(person)
- `Roacher Straße 40, 9241 Ragain, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt  Österreich/FAÖ`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/148199.1`) (sent_id: `deanon_BFG_20260814_TEST/148199.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Siegbert Anweiler  in der Beschwerdesache Thomas Harasymir,  Gerlosstraße 32, 4694 Aurachkirchen, Österreich, vertreten durch Südsteirische Steuerberatung GmbH, Hauptplatz 7, 8430  Leibnitz, zur Beschwerde vom 4.11.2024 gegen die Bescheide des Finanzamtes für  Großbetriebe vom 10.9.2024 betreffend Feststellung von Einkünften gemäß § 188 BAO für die  Jahre 2021 und 2022 beschlossen:  I. Die Beschwerde wird an das vorlegende Finanzamt für Großbetriebe weiter- bzw  rückgeleitet.

**False Positives:**

- `Südsteirische Steuerberatung` — partial — pred is substring of gold: `Südsteirische Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegbert Anweiler`(person)
- `Thomas Harasymir`(person)
- `Gerlosstraße 32, 4694 Aurachkirchen, Österreich`(address)
- `Südsteirische Steuerberatung GmbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `Finanzamt für Großbetriebe`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hildegard Nüßgens  in der Beschwerdesache Charles Dormayr,  SET-Straße 22, 4382 Sarmingstein, Österreich, vertreten durch Christandl & Partner Rechtsanwälte, Mag. Heinz Bauer,  Elisabethstraße 50b, 8010 Graz, über die Beschwerde vom  13. Jänner 2020 gegen den  Bescheid des Finanzamtes Österreich vom  11. Dezember 2019 betreffend Grunderwerbsteuer  27.02.2019 Steuernummer 59-652/7687  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Christandl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hildegard Nüßgens`(person)
- `Charles Dormayr`(person)
- `SET-Straße 22, 4382 Sarmingstein, Österreich`(address)
- `Mag. Heinz Bauer`(person)
- `Finanzamtes Österreich`(organisation)
- `59-652/7687`(tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/148480.1`) (sent_id: `deanon_BFG_20260814_TEST/148480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Reinhold Jonasius, Johann Tagwerker-Straße 17, 5760 Pabing, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, über die Beschwerde vom 28.08.2015 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 22. Juni 2015  betreffend Festsetzung der Kapitalertragsteuer 2011 – 2013, Steuernummer 81-937/8981  nach Durchführung einer mündlichen Verhandlung am 31. Jänner 2025 zu Recht erkannt:   I. Der Beschwerde wird als teilweise Folge gegeben.

**False Positives:**

- `Gosteco Goworek` — partial — pred is substring of gold: `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Reinhold Jonasius`(person)
- `Johann Tagwerker-Straße 17, 5760 Pabing, Österreich`(address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH`(organisation)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)
- `Finanzamt Österreich`(organisation)
- `81-937/8981`(tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/148995.1`) (sent_id: `deanon_BFG_20260814_TEST/148995.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/149239.1`) (sent_id: `deanon_BFG_20260814_TEST/149239.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Lukas Mlnarik  in der Beschwerdesache Mathilda Neuteifl,  Adr, vertreten durch Steuerberater, über die Beschwerde vom 9.4.2015 (gem. § 248 BAO)  gegen den Bescheid des Finanzamtes Innsbruck (nunmehr Finanzamt Österreich/FAÖ) vom  12.12.2014 betreffend die Rückforderung von Familienbeihilfe und Kinderabsetzbetrag für den  Zeitraum 01/2009 bis 11/2014, SV-Nr, nach Durchführung einer mündlichen Verhandlung zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Lukas Mlnarik`(person)
- `Mathilda Neuteifl`(person)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt Österreich/FAÖ`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/149829.1`) (sent_id: `deanon_BFG_20260814_TEST/149829.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Lothar Kriwet, Gaugen 11, 9150 Draurain, Österreich, vertreten durch Spiss Steuerberatung GmbH,  Timmlerweg 16, 6580 St. Anton am Arlberg, über die Beschwerde vom 31. Oktober 2025 gegen  die Bescheide des Finanzamtes Österreich vom 15. Oktober 2025 betreffend   1. Verzinsung gemäß § 16 COFAG-NoAG (Fixkostenzuschuss I),  2.

**False Positives:**

- `Spiss Steuerberatung` — partial — pred is substring of gold: `Spiss Steuerberatung GmbH`

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

## `role_anchor_name` 💣

**F1:** 0.001 | **Precision:** 0.077 | **Recall:** 0.001  

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
| 0.077 | 0.001 | 0.001 | 13 | 1 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 12 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Tanja Grottenthaler` | `Tanja Grottenthaler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Mag. Susanne Haim` (person)
- `Mag Stefan Raab` (person)
- `Leopold Pichlbauer` (person)
- `Bettina Domigall, Bakk. iur.` (person)
- `Zickhöhe 66, 3361 Biberbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_21`)


In der Berufung (nunmehr Beschwerde) wendet die Beschwerdeführerin im Wesentlichen ein,  der Geschäftsführer der Beschwerdeführerin, dem die verdeckte Ausschüttung von der  Betriebsprüfung zugerechnet worden sei, sei nicht auch Gesellschafter der  Beschwerdeführerin.

**False Positives:**

- `Beschwerdeführerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_143`)


Danach sind Vertreter Personen, die im Außendienst  zum Zwecke der Anbahnung und des Abschlusses von Geschäften und zur Kundenbetreuung  tätig sind (vgl. zB VwGH 31.5.2017, Ro 2015/13/0009).

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_54`)


Ermittlungen durch das Bundesfinanzgericht  In dem Bemühen, Klarheit für alle beim Bundesfinanzgericht anhängigen Fälle zu gewinnen,  welche die steuerliche Behandlung von als Einmalbetrag ausbezahlten Freizügigkeitsleistungen  (sowie Hinterlassenenleistungen) österreichischer Grenzgänger/innen zum Gegenstand haben,  wandten sich die Richterinnen und Richter des Bundesfinanzgerichtes, Außenstelle Feldkirch,  mit einem amtswegigen Ermittlungsersuchen an die nachstehenden liechtensteinischen (3)  und Schweizer (5) offiziellen Stellen:  Finanzmarktaufsicht Liechtenstein FMA  Liechtensteinischer Pensionskassenverband LLB  Liechtensteinischer Versicherungsverband LVV (hat sich für unzuständig erklärt).

**False Positives:**

- `Bundesfinanzgerichtes` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135522.1`) (sent_id: `deanon_BFG_20260814_TEST/135522.1_71`)


Wie unter Z. 1 ausgeführt, gibt es aber kaum noch Anbieter von  Freizügigkeitspolicen und unseres Wissens ist es bei keinem Anbieter möglich, die  Altersleistungen in Rentenform zu beziehen.“  C. Ergänzende Ermittlungen durch die Abgabenbehörde  Ein Vertreter der Abgabenbehörde, dem das BFG seine Ermittlungsergebnisse zur  Stellungnahme zugeleitet hatte, wandte sich in der Folge mit nachstehenden Fragen ergänzend  an insgesamt 33 liechtensteinische und schweizerische Versicherungsunternehmen,  einschließlich schweizerischer Versicherungsunternehmen die in Liechtenstein im  grenzüberschreitenden Dienstleistungsverkehr zugelassen sind:  7 von 13 Seite 8 von 13

**False Positives:**

- `Abgabenbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_23`)


Mehmet Köprücü  sei entgegen den Angaben im Vorlagebericht des Finanzamtes nicht der  steuerliche Vertreter des Bf, sondern nur eingeschränkt für das Beschwerdeverfahren  beauftragt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mehmet Köprücü`(person)
- `Finanzamtes`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_31`)


Das Finanzamt hat dazu folgende Stellungnahme abgegeben:  „Der Mehmet Köprücü  gab am 20.04.2022 seine Vollmacht für das Haftungsverfahren  Evamaria Watenphul  bekannt und beschrieb sie wortwörtlich so:  Haftungsbescheide je vom 23.03.2022  Und:  In der außen bezeichneten Finanzsache haben die Beschwerdeführer … Evamaria Watenphul, … als  ehemalige Geschäftsführer der Özyilmaz Recycling GmbH., Herrn Mehmet Köprücü  Vollmacht erteilt,  wobei sich der gefertigte Anwalt auf diesem ihm erteilte Vollmacht beruft.

**False Positives:**

- `Özyilmaz Recycling` — partial — pred is substring of gold: `Özyilmaz Recycling GmbH.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Mehmet Köprücü`(person)
- `Evamaria Watenphul`(person)
- `Evamaria Watenphul`(person)
- `Özyilmaz Recycling GmbH.`(organisation)
- `Mehmet Köprücü`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_1`)


BESCHLUSS  Der Vorsitzende des Finanzstrafsenates Wien 2 des Bundesfinanzgerichtes Mag. Gerhard  Groschedl hat in der Finanzstrafsache gegen   1.

**False Positives:**

- `Finanzstrafsenates Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Mag. Gerhard  Groschedl`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/145306.1`) (sent_id: `deanon_BFG_20260814_TEST/145306.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Vorsitzenden Richter Ri 1, den beisitzenden Richter Ri 2  und die fachkundigen Laienrichter Laienri 1 und Laienri 2 in der Beschwerdesache Herbert Koppen,  Reingrubstraße 15, 4615 Lehen, Österreich, vertreten durch Dr. Felix Karl Vogl Rechtsanwalt GmbH, Bahnhofstraße 34/12,  6780 Schruns, betreffend Beschwerde vom 31. März 2020 gegen den Bescheide des Zollamtes  Feldkirch Wolfurt vom 2. März 2020 betreffend Einfuhrabgaben (GZ_angef. Bescheid) in der  am 1.7.2024 stattgefundenen Sitzung beschlossen:  Der angefochtene Bescheid wird gemäß § 278 BAO unter Zurückverweisung der Sache an die  Abgabenbehörde hinsichtlich der NO und Y9 aufgehoben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`
- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Herbert Koppen`(person)
- `Reingrubstraße 15, 4615 Lehen, Österreich`(address)
- `Dr. Felix Karl Vogl Rechtsanwalt GmbH`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_298`)


Befragt durch den Vertreter der Abgabenbehörde, welcher der Bf vorhält, dass sie den  Mittelpunkt in Österreich habe und nicht wisse ob sie sich überwiegend in Österreich aufhalte.

**False Positives:**

- `Abgabenbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_301`)


Befragt in der mündlichen Verhandlung durch den Vertreter der Abgabenbehörde, ob der  Lebensgefährte (Vater der Kinder) wenn sie in Deutschland gewesen ist, dieser alleine in  Österreich war, gibt die Bf an: „Ja er war teilweise in Österreich und teilweise im Ausland  arbeiten.

**False Positives:**

- `Abgabenbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/148601.1`) (sent_id: `deanon_BFG_20260814_TEST/148601.1_121`)


Voraussetzungen für die Haftung gemäß § 9 Abs. 1 BAO sind die Stellung als Vertreter der  Gesellschaft, eine Abgabenforderung gegen den Vertretenen, die Uneinbringlichkeit dieser  Abgabenforderung, eine abgabenrechtliche Pflichtverletzung des Vertreters und dessen  Verschulden an dieser Pflichtverletzung sowie die Ursächlichkeit der Pflichtverletzung für die  Uneinbringlichkeit.

**False Positives:**

- `Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
| 0.000 | 0.000 | 0.000 | 9 | 0 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 9 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_91`)


Es ist sohin evident, dass die Gründung der X., mit der das ganze Jahr 2011 ‚ keinerlei Geschäftsbeziehung gegeben war, nicht "ausschließlich über meinen Wunsch und um Scheinrechnungen zu legen", (erst) am 01.03.2012 (s. NS über die Schlussbesprechung) erfolgte.

**False Positives:**

- `X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139580.1`) (sent_id: `deanon_BFG_20260814_TEST/139580.1_69`)


Hinsichtlich der Ausführungen der beisitzenden Richterin, wonach das vorangeführte  Unternehmen nicht, wie vom steuerlichen Vertreter erwähnt, eine Subfirma von C sei, sondern  eine solche von der B., gab der steuerliche Vertreter bekannt, dass er keine Infos hinsichtlich  dieses Unternehmens habe.

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_277`)


(„Frau DM wohnte in den geprüften Jahren immer im  Ausland…“) oder S. 8ff.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_29`)


Hier wurde in der Selbstanzeige die Vermutung geäußert, daß die  Kalkulationsdifferenzen durch die B., welche dem Lokal angeschlossen war und Zugang zu den  Getränkevorräten im Keller hatte, der Grund für die Kalkulationsabweichungen im restlichen  Jahr 2017 und 2018 war.

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_162`)


Infolgedessen betrug die effektive  Mehrwertsteuerbelastung von B. 46 % (vgl. Rz. 13 des Urteils des EuGH v. 7.7.2022, B, C- 696/20, hier: 40%).

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_430`)


Hinsichtlich der drei weitere Bereiche des A., nämlich IT-Bereich, Wäschereien und  Generaldirektion, welche von der Außenprüfung zusätzlich als drei eigene Betriebe  gewerblicher Art angenommen wurden, sei insbesondere nicht nachvollziehbar, dass die  Generaldirektion als eigener Betrieb gewerblicher Art bestehen solle.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_109`)


P. erzielte bei der D. 11.532 € bzw. bei der Bf.:   D. Univ.-Prof. Julian Czernitzki  Arbeitsmarktservice gesamt Einkommen It. ESt- Bescheid  2014 11.532 € 4.200 €  15.732 € 15.540,66 €  2015  5.656 € 1.407 € 7.063 € 5.200,71 €  2016  5.941 €  5.941 € 5.486,10 €  Die Gegenüberstellung verdeutlicht, dass P. über keine ausreichen Einkünfte, die eine  durchschnittliche Lebensführung erfordert, verfügte, sehr wohl aber G.. Gerade dieser Aspekt  zeigt auf, dass in wirtschaftlicher Betrachtungsweise der in der Beschwerde erstmals  vorgetragene Einwand, die Entnahmen zum Verrechnungskonto „P.“ seien G. zuzurechnen,  auch deshalb unglaubwürdig ist, weil (trotz diesbezüglicher Anfrage) nicht aufgeklärt worden  ist, welche konkrete Verwendung die Gelder bei G. gefunden haben sollten.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof. Julian Czernitzki`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_36`)


Es seien auf ihrem Konto keine Eingänge der  Beihilfe, sondern auf dem Konto von S., der zu diesem Zeitpunkt 2019 bis 2020 in Wien  wohnhaft gewesen sei und dort auch studiert habe, bis zum heutigen Datum.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_70`)


Es  seien auf ihrem Konto keine Eingänge der Beihilfe, sondern auf dem Konto von S., der zu  diesem Zeitpunkt 2019 bis 2020 in Wien wohnhaft gewesen sei und dort auch studiert habe,  bis zum heutigen Datum.

**False Positives:**

- `S.` — no gold match — likely missing annotation

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
| `person` | 0 | 0 | 1614 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (670, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_240`)

Bekannt sei, dass **Dipl.Ing. Dr. H** mehrere Gutachten erstellt habe.

- missed: `Dipl.Ing. Dr. H` (person)
- predicted in sentence: `Ing. Dr`

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_99`)

Im Urteil vom 26.10.2010, C-97/09, **Schmelz**, erwog der EuGH:  Nach alledem erweist es sich, dass beim gegenwärtigen Stand der Entwicklung der  Mehrwertsteuerregelung das Ziel, die Wirksamkeit der Steueraufsicht im Hinblick auf die  Bekämpfung von Steuerhinterziehungen, Steuerumgehungen und etwaigen Missbräuchen zu  gewährleisten, und das Ziel der Kleinunternehmerregelung, mit der die Wettbewerbsfähigkeit  der Kleinunternehmen gestärkt werden soll, es zum einen rechtfertigen, dass die  Anwendbarkeit der Mehrwertsteuerbefreiung auf die Tätigkeiten der Kleinunternehmen  beschränkt wird, die im Hoheitsgebiet des Mitgliedstaats, in dem die Mehrwertsteuer  geschuldet wird, ansässig sind, und zum anderen, dass der zu berücksichtigende Jahresumsatz  derjenige ist, der in dem Mitgliedstaat erzielt wird, in dem das Unternehmen ansässig ist.

- missed: `Schmelz` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_14`)

Frau **Basyurt** wurde darauf hingewiesen, dass der Pkw innerhalb der nächsten 3 Wochen in  Österreich angemeldet wird;

- missed: `Basyurt` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch **Mag. András Péter Radics**, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. András Péter Radics` (person)
- predicted in sentence: `Dr. Astrid Binder`, `Nadine Tomczack`, `Mag. Andr`

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_5`)

Die belangte Behörde stellte am 18. März 2016 mit Einheitswertbescheid zum 1.1.2014,  Hauptfeststellung mit Wirksamkeit ab 1.1.2015, den Einheitswert für den Grundbesitz des  Beschwerdeführers **Siegfried Beyazit** (in der Folge als Bf bezeichnet) Adresse fest, der jeweils im  Hälfteeigentum des Bf und seiner Gattin steht.

- missed: `Siegfried Beyazit` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_43`)

Zur Berechnung der Bemessungsgrundlage der Glückspielabgabe enthält die Selbstanzeige  folgende Ausführungen:  „Berechnung Glückspielabgabe Casino Spiele  Für die Berechnung der Bemessungsgrundlage der Glücksspielabgabe gemäß § 57 Abs 2 GSpG  für den gegenständlichen Zeitraum wurden Bruttospieleinnahmen berücksichtigt, die von  Kunden erzielt wurden, die bei der Registrierung auf der Website https**://www.Oswald Rübberdt** .com  „Österreich“ aus einem Drop-Down Menü als Wohnsitzland ausgewählt und eine  österreichische Registrierungsadresse angegeben haben.

- missed: `://www.Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., **Gerald Cuny-Kreuzer** sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

- missed: `Gerald Cuny-Kreuzer` (person)
- predicted in sentence: `Dr. Hans Blasina`, `Dr. Sebastian Pfeiffer, LL.M`, `Dr. Franz Kandlhofer`, `Christina Tiebout`, `Deloitte Tax  Wirtschaftsprüfungs`

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_200`)

Laut Sachwalter habe Frau **Freßdorf** (Tante des Bf.) erzählt, dass sich ihr Neffe mit Beginn des  Studiums zunehmend gegenüber seiner Umwelt verschlossen und sich immer mehr  zurückgezogen habe, was sich dadurch geäußert habe, dass er keinen Kontakt mit der Familie  haben wollte und auch gemeinsamen Familienaktivitäten ferngeblieben sei.

- missed: `Freßdorf` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_57`)

Sachverhalt   Unbeschränkt haftender Gesellschafter der Beschwerde führenden **Uwe Dörfl**  ist die W GmbH.  Als Kommanditisten sind die XX Immobilien Holding GmbH und die A-Finanzvermittlung GmbH  beteiligt.

- missed: `Uwe Dörfl` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_72`)

Bei der Erstellung des fachärztlichen Sachverständigengutachtens durch das Bundessozialamt  fanden weder der Befund der Stellungskommission noch die Aussagen von Frau **Unverdroß**  entsprechende Berücksichtigung.

- missed: `Unverdroß` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_16`)

Behandlung(en) / Medikamente / Hilfsmittel:  keine Therapie  Sozialanamnese:  bis Oktober sei er von PVA arbeitsunfähig geschrieben worden, neue Untersuchung hätten  noch nicht stattgefunden   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Befunde nachgereicht.:   Einladung für Untersuchung nach dem Behinderteneinstellungsgesetz am 11.05:21 um 16 Uhr  Ordination **Dr. Dok1**  PVA GA DR.

- missed: `Dr. Dok1` (person)
- predicted in sentence: `Dr. Dok`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/141832.1`) (sent_id: `deanon_BFG_20260814_TEST/141832.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr.in Li Lübkemann**  in der   Beschwerdesache Theobald Tormöllen, Am Hora 38, 9554 Trenk, Österreich, vertreten durch Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 2. September 2016 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 24. August 2016, ErfNr, betreffend Grunderwerbsteuer im  fortgesetzten Verfahren   zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Dr.in Li Lübkemann` (person)
- predicted in sentence: `Theobald Tormöllen`

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des **OSR Corbinian Friemuth**,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `OSR Corbinian Friemuth` (person)
- predicted in sentence: `Mag. Alexander Rimser`

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Dr.in Hemma Ramelow**  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Univ.-Prof.in Dr.in Hemma Ramelow` (person)
- predicted in sentence: `Univ.-Prof.in Dr`, `Mag. Damian Wiecher`, `Finanzamt Wien`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_95`)

2.3.2009, **Prof. Maida**: Gehen einiger Schritte nur mit Hilfe möglich.

- missed: `Prof. Maida` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_61`)

Darüber hinaus spreche  beispielsweise Sektionschef **Univ.-Prof. DDr. Gunter Mayr** in RdW 6/2016, S. 419 ff, von den im  „Gewinn" veröffentlichten Grundstückswerten als tauglichen Bewertungsmaßstab für Grund  und Boden.

- missed: `Univ.-Prof. DDr. Gunter Mayr` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_126`)

Weitere Ermittlungen des FA   In der Folge führte das FA eine Nachschau durch, im Zuge derer die steuerliche Vertretung der  Bf. dem FA detaillierte Daten für den gegenständlichen Zeitraum übermittelte (Datei mit der  Bezeichnung „191003**_Oswald Rübberdt**  GSA_WET 2012-2016.xlsx.“)  8 von 48 Seite 9 von 48

- missed: `_Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)

Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die **Engelbert Schefe**, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

- missed: `Engelbert Schefe` (person)
- predicted in sentence: `Dieter Avemaria`

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_23`)

Mit E-Mail vom 21. März 2025 erhob **Pjotr Niessl**  fristgerecht Beschwerde gegen den  Zurückweisungsbescheid vom 7. März 2025 und brachte Folgendes vor:  „Wie im Telefon besprochen, ich möchte hiermit offiziell eine Beschwerde gegen die Ablehnung  unserer Vollmacht einreichen.

- missed: `Pjotr Niessl` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)

- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau **Basyurt** tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

- missed: `Basyurt` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/146075.1`) (sent_id: `deanon_BFG_20260814_TEST/146075.1_26`)

**Delila Hollek**  habe sich die  Option allerdings offengehalten die Ausbildung zu einem späteren Zeitpunkt fortzusetzen.

- missed: `Delila Hollek` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache **Prof.in Julia Mundle**, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Prof.in Julia Mundle` (person)
- predicted in sentence: `Mag. Daniel Philip Pfau`, `Hopmeier Wagner Kirnbauer  Rechtsanwälte`, `Finanzamtes Wien`

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_6`)

Zudem fasst das Bundesfinanzgericht durch den Richter Mag. Michael Gleiss in der  Beschwerdesache Sibylle Thalhofer, Fabriksgelände 6, 4923 Mitterberg, Österreich  vertreten durch **Mag. Hans Gerald Rainer- Harbach**, Burgplatz 6 Tür 3, 9800 Spittal an der Drau, über die Beschwerde vom 25. Juli 2013  gegen den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 25. Juni 2013 betreffend Einkommensteuer 2006, den   Beschluss:  IV. Die Beschwerde wird gemäß § 261 Abs 2 BAO als gegenstandslos erklärt.

- missed: `Mag. Hans Gerald Rainer- Harbach` (person)
- predicted in sentence: `Mag. Michael Gleiss`, `Sibylle Thalhofer`, `Mag. Hans Gerald Rainer`

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/141732.1`) (sent_id: `deanon_BFG_20260814_TEST/141732.1_34`)

Diese amtswegig neu angelegte, zweite Steuernummer wurde weder dem steuerlichen  Vertreter noch der **Ulrich Büldmöller**  bekannt gegeben.

- missed: `Ulrich Büldmöller` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_12`)

Entscheidungsgründe  I. Verfahrensablauf  Selbstanzeige, Selbstberechnungen und Anträge nach § 201 BAO   Mit Schriftsätzen vom 21.12.2016 erstattete **Oswald Rübberdt**  Limited (die nunmehrige  Beschwerdeführerin, kurz Bf.)

- missed: `Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. VN. NN., die Richterin **Dr.in  Ri.N.** sowie die fachkundigen Laienrichter Lena Pahlmann und Ch,Nn. in der Beschwerdesache  Esra Voskuhle, Brandstetterweg 76k, 4682 Buchet, Österreich, vertreten durch Beratungs GmbH, Str.x, plz Stadt, über die  Beschwerde vom 26. Juni 2019 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich Dienststelle  Sonderzuständigkeiten) vom 27. Mai 2019 betreffend Gebühren gemäß § 33 TP 20  Gebührengesetz (GebG) 1957 nach Durchführung einer mündlichen Verhandlung am  12. Oktober 2023 in Anwesenheit des Beschwerdeführers und dessen Ehegattin A.N.G und der  Schriftführerin Vn. Nn1 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Dr.in  Ri.N.` (person)
- predicted in sentence: `Esra Voskuhle`, `Beratungs`

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_8`)

S. wurde am 23. November 2021 (Nachuntersuchung) von **Dr.in Dok1** untersucht und folgendes  Gutachten erstellt:  Anamnese:  VGA, 08/2016:  kombinierter Entwicklungsrückstand mit Intelligenzminderung – 50%   1 von 16 Seite 2 von 16

- missed: `Dr.in Dok1` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_9`)

Als  Geschäftsführer fungierte im Streitzeitraum Dipl. **Ing.Ing. Bertram Hennlein**  Im Zuge einer die Jahre 2015 bis 2019 umfassenden gemeinsamen Prüfung der Lohnabgaben  (GPLA) wurden folgende, nunmehr streitgegenständlichen Feststellungen getroffen:  1 von 17 Seite 2 von 17

- missed: `Ing.Ing. Bertram Hennlein` (person)
- predicted in sentence: `Ing. Bertram Hennlein  Im Zuge`

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_142`)

A. gab weiters an, dass er als einziger Gesellschafter und Geschäftsführer der X. d.o.o. in den Jahren 2012 und 2013 Seite 13 von 21 Rechnungen an **N.N.** ausgestellt hatte.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache **Dipl. Kff. Sibylle Wahlscheid**,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

- missed: `Dipl. Kff. Sibylle Wahlscheid` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/139553.1`) (sent_id: `deanon_BFG_20260814_TEST/139553.1_14`)

Betreffend seinen Sohn Luigi Assenov, LLB, geboren am 23. Oktober 1983,  wurde die Familienbeihilfe mit Juni 2017 eingestellt.  Der jüngere Sohn, **Rudolf Kumpmeier**, hatte im Jahr 2019 das 18.

- missed: `Rudolf Kumpmeier` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_10`)

Ebenso legte der Bf. die Heiratsurkunde, sowie eine seine Ehegattin **Katalin** betreffende  Bestätigung (E9) für das Jahr 2018 vor, aus welcher Einkünfte derselben in Höhe von  2.824.116,- HUF vor.

- missed: `Katalin` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_59`)

Für Herrn **Bodewein** geht hingegen die absolute Unzulässigkeit einer Revision gemäß § 25a Abs. 4  VwGG vor (siehe Rechtsmittelbelehrung).

- missed: `Bodewein` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Günter Möhlenfeld  in Vertretung des verhinderten  Richters Hon.-Prof. Kaspar Frantzius  in der Verwaltungsstrafsache gegen **Elias Schwabeland**, Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 22. November  2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom  15. November 2021, GZ. MA67/Zahl/2021, nach Durchführung einer mündlichen Verhandlung  am 19. Dezember 2022, in Anwesenheit des Beschuldigten und der Schriftführerin IP, jedoch in  entschuldigter Abwesenheit einer Vertreterin/eines Vertreters der belangten Behörde, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis  aufgehoben und das Verfahren eingestellt.  Gemäß § 52 Abs. 8 VwGVG hat die beschwerdeführende Partei keinen Beitrag zu den Kosten  des Beschwerdeverfahrens zu entrichten.

- missed: `Elias Schwabeland` (person)
- predicted in sentence: `Hon.-Prof. Günter Möhlenfeld`, `Hon.-Prof. Kaspar Frantzius`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_92`)

Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  1.12.1980, ärztlicher Befund der Stellungskommission Wien: Nervosität, Asthenie, **M.**  Scheuermann.

- missed: `M.` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_52`)

Im Vorlagebericht vom 13.01.2023 hat das Finanzamt folgende Stellungnahme angeführt:   „Im Vorlageantrag wird ausgeführt, dass der Verzicht nicht gegenüber Hr. **Jeanne Kraenzlin**  gilt, da  dieser nicht persönlich unterzeichnet hat und somit nicht auf sein Rechtsmittel in Bezug auf die  Festsetzung der Kapitalertragsteuern aus den Zeiträumen 2015 bis 2018 verzichtet.

- missed: `Jeanne Kraenzlin` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)

Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von **Dr. Thomas Hofer-Zeni** vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

- missed: `Dr. Thomas Hofer-Zeni` (person)
- predicted in sentence: `Dr. Thomas Hofer`, `Dr. Thomas Hofer`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_19`)

Die Exfrau sei im Jänner 2020 ausgezogen und seither  bezahle der Beschwerdeführer Alimente für den Sohn **Herbert Schaffarik**.

- missed: `Herbert Schaffarik` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. David Hell LL.B. LL.M.** in der  Beschwerdesache DDr. Ali Franzel, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Mag. David Hell LL.B. LL.M.` (person)
- predicted in sentence: `Mag. David Hell`

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/148199.1`) (sent_id: `deanon_BFG_20260814_TEST/148199.1_7`)

Diese Bescheide sind  jeweils an die **Thomas Harasymir**  zu Handen Frau HR Martha Heiwolt  gerichtet und wurden an letztere zugestellt.  Sie enthalten jeweils folgenden Hinweis: „Dieser Bescheid wirkt gegen alle Beteiligten, denen  im Spruch Einkünfte zugerechnet bzw. nicht zugerechnet werden (§ 191 Abs. 3 BAO).

- missed: `Thomas Harasymir` (person)
- predicted in sentence: `HR Martha Heiwolt`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_12`)

Betreuungsverfahren **Heinrich Gröppert–** FÄ für Psychiatrie, 01/2019

- missed: `Heinrich Gröppert–` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_7`)

Im Februar 2015 wurde die Finanzpolizei seitens der Landespolizeidirektion zum "Verdacht  einer Übertretung nach § 82 Abs. 8 KFG" durch **Sven Mitterhuber** (= Beschwerdeführer, Bf)  verständigt und ua.

- missed: `Sven Mitterhuber` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/142998.1`) (sent_id: `deanon_BFG_20260814_TEST/142998.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag.Dr. Thomas Leitner** in der  Beschwerdesache Evelyn Schlessing, Koksbatteriestraße 7, 9560 Bichl, Österreich  vertreten durch Univ.Prof.i.R. Dr. Josef Werndl,  über die Beschwerde vom 27. Dezember 2022 gegen den Bescheid des Finanzamtes Österreich  vom 15. Dezember 2022 betreffend Einkommensteuer 2021 zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

- missed: `Mag.Dr. Thomas Leitner` (person)
- predicted in sentence: `Dr. Thomas Leitner`, `Evelyn Schlessing`, `Univ`, `Dr. Josef Werndl`

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_151`)

II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Bf. ist die **Cathleen Kirchgässner**  mit dem ursprünglichen Sitz in der politischer Gemeinde öOrt2 (nunmehr  öOrt3, Änderung eingetragen im Firmenbuch am 22.11.2023), die am 05.02.2008 im  Firmenbuch mit dem Geschäftszweig Handel mit Waren aller Art neu eingetragen wurde.

- missed: `Cathleen Kirchgässner` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache **Eleonore Sawadzki, Bakk. art.**, Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

- missed: `Eleonore Sawadzki, Bakk. art.` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer`, `Eleonore Sawadzki`

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/140622.1`) (sent_id: `deanon_BFG_20260814_TEST/140622.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache **Bodo Adamovic, Bakk. phil.**, Gantschenbergstraße 24, 4204 Affenberg, Österreich, betreffend Beschwerde vom 22. Mai 2015 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 27. April 2015 betreffend Einkommensteuer 2012  Steuernummer 49-425/9978  beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

- missed: `Bodo Adamovic, Bakk. phil.` (person)
- predicted in sentence: `Bodo Adamovic`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_16`)

Nachdem binnen der zweiwöchigen Frist (§ 2 Abs. 2 Wiener Parkometergesetz 2006) keine  Lenkerauskunft erteilt wurde, lastete der Magistrat der Stadt Wien, MA 67, **Prof.in StR DDr.in Reneé Plein**  (Beschwerdeführer, kurz: Bf.) als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin des näher bezeichneten Fahrzeuges mit Strafverfügung vom 25. März  2020, MA67/456/2020, an, dass er dem ordnungsgemäß zugestellten  Lenkerauskunftsersuchen der MA 67 vom 23. Jänner 2020 innerhalb von zwei Wochen ab  Zustellung nicht entsprochen habe.

- missed: `Prof.in StR DDr.in Reneé Plein` (person)
- predicted in sentence: `StR DDr.in Rene`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_66`)

Nach der Aktenlage wurde der Einspruch gegen die an Frau **Manhardt** ergangene  Strafverfügung vom Beschwerdeführer erhoben, eine Vollmacht wurde jedoch (trotz  Aufforderung durch die belangte Behörde) nicht vorgelegt.

- missed: `Manhardt` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_40`)

Bei den vorgelegten Unterlagen handelt es sich einerseits um Mietverträge und andererseits  um Schreiben des Herrn DI J **M.**

- missed: `M.` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/148797.1`) (sent_id: `deanon_BFG_20260814_TEST/148797.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Birgitt Koran über den Antrag des  **Stephanie Luippold**, Straße IX 48, 4153 Eschernhof, Österreich, vom 7. Mai 2025 auf Verfahrenshilfe (Beigebung eines  Verteidigers) für ein Beschwerdeverfahren gegen eine Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA 32, vom 15. April 2025, GZ.  MA67/GZ1/2024, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Beschlusses des Bundesfinanzgerichtes vom 4. Februar 2025, GZ.  RV/GZ2/2025, beschlossen:  I. Der Antrag auf Verfahrenshilfe (Beigebung eines Verfahrenshilfeverteidigers) wird  abgewiesen.

- missed: `Stephanie Luippold` (person)
- predicted in sentence: `Dr. Birgitt Koran`

</details>

---

