# RuleChef FinDok Benchmark - Rule Analysis- Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-09T13:17:27.727983

---

<details>
<summary> Configuration</summary>

| Parameter | Value |
|-----------|-------|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training examples | 1031 |
| Validation examples | 258 |
| Test examples | 1635 |
| Train annotations | 1257 |
| Validation annotations | 325 |
| Test annotations | 3429 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 50 |
| Refinement iterations | 2 |
| Seed | 42 |
| Agentic | False|
| Enable Critic | False |
| Enable Prune | False|
| Critic Interval | 0 |
| Audit Interval | 0|
| Use GREX | True |

</details>

---

<details>
<summary> Results</summary>

| Metric | Value |
|--------|-------|
| Accuracy (exact match) | 92.3% |
| No. of entities predicted | 369 |
| True Positives | 301 |
| False Positives | 68 |
| Micro Precision | 81.6% |
| Micro Recall | 74.3% |
| Micro F1 | 77.8% |
| Macro F1 | 77.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Matches |
|------|----|----------|--------|--------|
| `tax_office_fa` |22.3% | 98.1% | 12.6% | 52 |
| `company_gmbh_general` |16.3% | 74.0% | 9.1% | 50 |
| `tax_office_finanzamt` |15.0% | 72.3% | 8.4% | 47 |
| `company_ag_general` |8.8% | 67.9% | 4.7% | 28 |
| `specific_org_milan` |6.2% | 100.0% | 3.2% | 13 |
| `specific_org_houdek` |4.8% | 100.0% | 2.5% | 10 |
| `specific_org_fa_salzburg` |4.8% | 100.0% | 2.5% | 10 |
| `tax_office_finanzamt_grieskirchen` |4.8% | 100.0% | 2.5% | 10 |
| `specific_org_roelfsen` |3.4% | 100.0% | 1.7% | 7 |
| `specific_org_bezirksgericht` |2.9% | 100.0% | 1.5% | 6 |
| `specific_org_unterrecycling` |2.9% | 100.0% | 1.5% | 6 |
| `specific_org_pastl` |2.9% | 100.0% | 1.5% | 6 |
| `specific_org_annemie_bott` |2.4% | 100.0% | 1.2% | 5 |
| `specific_org_fa_deutschlandsberg` |2.4% | 100.0% | 1.2% | 5 |
| `specific_org_fa_waldviertel` |2.4% | 100.0% | 1.2% | 5 |
| `specific_org_kraftver` |2.4% | 100.0% | 1.2% | 5 |
| `company_kg_general` |2.2% | 12.2% | 1.2% | 41 |
| `specific_org_fa_gmunden` |2.0% | 100.0% | 1.0% | 4 |
| `specific_org_okur` |2.0% | 100.0% | 1.0% | 4 |
| `specific_org_gartgart` |2.0% | 100.0% | 1.0% | 4 |
| `tax_office_fa_graz_stadt` |2.0% | 100.0% | 1.0% | 4 |
| `specific_org_raiffeisen_hyphen` |1.9% | 66.7% | 1.0% | 6 |
| `specific_org_klusner` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_yxtg` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_nowothnig` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_reinemut` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_pastel` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_krolitzki` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_schoenfelder` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_event_sudkraftlex` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_kqpc` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_sanitar` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_verdonlex` |1.5% | 100.0% | 0.7% | 3 |
| `tax_office_fa_schwechat_gmunden` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_fa_purkersdorf` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_fa_tirol_ost` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_fa_braunau_ried_schärding` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_vahrenkamp` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_celikkanat_garten` |1.5% | 100.0% | 0.7% | 3 |
| `specific_org_fa_judenburg` |1.5% | 75.0% | 0.7% | 4 |
| `specific_org_stadte_energie` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_finanzen_tradonnex` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_schmeltz` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_raiffeisen_wienerwald` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_talverwerk` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_dufel` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_alal` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_nord_kellex` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_bierwerth` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_bludszat` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_traun_digital` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_dufel_technik` |1.0% | 100.0% | 0.5% | 2 |
| `specific_org_fa_wien` |1.0% | 66.7% | 0.5% | 3 |
| `specific_org_raiffeisen` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_mur` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_starker` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_enns` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_hoerup_ag` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_dorfcon` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_waldtouristik` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_chen` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_lexkel` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_leiss` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_klein_vorholt` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_dgcv_ecommerce` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_laskowsky` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_oberrecycling` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_innluftfahrt` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_inn_monost` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_zschieschank` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_mullbrandt` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_hudec_christian` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_gronemeier` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_ugqq` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_wod_sicherheit` |0.5% | 100.0% | 0.2% | 1 |
| `tax_office_finanzamt_schwechat` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_fa_vorarlberg` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_mittelheizung` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_fuchsl` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_dlcg` |0.5% | 100.0% | 0.2% | 1 |
| `specific_org_fa_baden` |0.5% | 50.0% | 0.2% | 2 |
| `tax_office_finanzamt_graz_stadt` |0.5% | 50.0% | 0.2% | 2 |
| `specific_org_dias_telekom` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_traunluftfahrt` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_manfredo` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_logkeltal` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_steinfurt` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_berwaldkel` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_waldtra` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_gogel` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_heimwald` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_bahrdt` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_raiffeisen_wels` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_henken` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_depp` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_talkel` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_hebebrand` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_rnv` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_gozcu` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_keltrizor` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_unibach` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_noruniwald` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_pfendtner` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_kraftnex` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_waldver` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_raiffeisen_hippach` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_raiffeisen_genburg` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_raiffeisen_hall` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_raiffeisen_karnische` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_see_garttalder` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_psomadakis` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_trafenfen` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_gorius` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_unter_donunisee` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_ruterborries` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_bankhaus_denzel` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_norconheim` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_bauermeister` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_hoch_synwil` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_sophie_wittmeir` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_lexdon` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_wien_waldnor` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_vossbein` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_sudver` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_glanznorost` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_west_luftfahrt` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_maegerlein` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_planung_monuniost` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_zumholte` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_simek` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_dersteintri` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_oina` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_gemke` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_kornfelder` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_raiffeisen_kasse_hyphen` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_cervenka` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_lubomir` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_textil_steingartlog` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_osttechnik` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_maschinenbau_derwilsee` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_fensudlog` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_sud_sudwil` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_kelgart_druck` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_greiner_mai` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_technik_ostbachal` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_traunlandwirtschaft` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_getraenke_nexdorfzor` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_kok_heberlein` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_seenorder` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_volkswien` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_donau_druck` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_nkah` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_olivier` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_hagdorn` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_istvan` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_paweltschik` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_schneppensieper` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_touristik_wildon` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_bawag` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_lognex` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_kira_hackbardt` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_nordtraval` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_rosilius` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_hochlebensmittel` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_yavasoglu` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_mur_alver` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_zoruniglanz` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_logseemon_metall` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_raiffeisen_rion` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_luehrig_hundertmarck` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_wildorftra` |0.0% | 0.0% | 0.0% | 0 |
| `specific_orgbruckmonwil` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_sudversand` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_logal` |0.0% | 0.0% | 0.0% | 0 |
| `specific_org_norddaten` |0.0% | 0.0% | 0.0% | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `specific_org_annemie_bott`

**F1:** 0.024 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Content:**
```
\bAnnemie\s+Bott\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.012 | 0.024 | 5 | 5 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 0 | 377 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 2**

```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 3**

```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 4**

```
64-207/8107, BV 24 : 
Beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott  gab es betreffend dem 
Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid 
Gruppenmitglied: 
21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010 
27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid 
Gruppenmitglied 2010 nach Betriebsprüfung  
27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 
20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010 
(Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung 
Rekultivierungskosten) 
19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt 
Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung 
Rekultivierungskosten) 
29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW) 
16.12.2013 Vorlage an BFG (damals noch UFS) 
17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete 
Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW) 
Betreffend des Rechtsvorgängers Milan Händlein  wurde das Erkenntnis des 
Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum 
Veranlagungsjahr 2007 erlassen.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 5**

```
zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom 
19.08.2009 eine Abspaltung zur Aufnahme in die Annemie Bott  durch Übertragung des 
gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und 
Übernahmsvertrages taxativ angeführten Positionen) erfolgt.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

</details>

<details>
<summary>❌ Missed (4)</summary>

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

- Missed: `FA Grieskirchen Wels` (organisation)


```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Milan Händlein` (organisation)


```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)

- Missed: `Milan Händlein` (organisation)


```
64-207/8107, BV 24 : 
Beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott  gab es betreffend dem 
Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid 
Gruppenmitglied: 
21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010 
27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid 
Gruppenmitglied 2010 nach Betriebsprüfung  
27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 
20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010 
(Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung 
Rekultivierungskosten) 
19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt 
Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung 
Rekultivierungskosten) 
29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW) 
16.12.2013 Vorlage an BFG (damals noch UFS) 
17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete 
Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW) 
Betreffend des Rechtsvorgängers Milan Händlein  wurde das Erkenntnis des 
Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum 
Veranlagungsjahr 2007 erlassen.
```

- Missed: `Milan Händlein` (organisation)


</details>

---

## `specific_org_stadte_energie`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bStadtEnergie\s+Holding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 254 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
III. Adressaten des Erkenntnisses: 
[...] 
Gruppenträger 28-587/0533 Dipl.-Ing. Angelika Bartholomai  als RNF der StadtEnergie Holding
```

| Prediction | Gold |
|------------|------|
| `StadtEnergie Holding` | `StadtEnergie Holding` |

**Example 2**

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

| Prediction | Gold |
|------------|------|
| `StadtEnergie Holding` | `StadtEnergie Holding` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

- Missed: `Laskowsky Umwelt` (organisation)


</details>

---

## `specific_org_raiffeisen`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+Stallhofen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 85 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Hierauf übermittelte der Beschwerdeführer ein Schreiben der Raiffeisenbank Stallhofen  vom 
24.2.2014, in welchem bestätigt wurde, dass er im Jahre 2013 € 4.377,00 an Kreditrückzahlung 
geleistet hat.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Stallhofen` | `Raiffeisenbank Stallhofen` |

</details>

---

## `specific_org_finanzen_tradonnex`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bFinanzen\s+Tradonnex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 249 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Dagegen erhob der Beschwerdeführer durch seinen steuerlichen Vertreter mit Schriftsatz vom 
23. Juni 2015 Beschwerde und beantragte, den Mietaufwand der Garagen (2011 bis 2013) und 
die Aufwendungen für Marken- und Musterschutzrechte (2012 und 2013) der Finanzen Tradonnex 
GmbH anzuerkennen, verdeckte Ausschüttungen nicht anzunehmen und dementsprechend 
keine Kapitalertragsteuer festzusetzen.
```

| Prediction | Gold |
|------------|------|
| `Finanzen Tradonnex` | `Finanzen Tradonnex` |

**Example 2**

```
Gegen dieses Erkenntnis erhob die Finanzen Tradonnex  GmbH außerordentliche Revision beim 
Verwaltungsgerichtshof.
```

| Prediction | Gold |
|------------|------|
| `Finanzen Tradonnex` | `Finanzen Tradonnex` |

</details>

---

## `specific_org_houdek`

**F1:** 0.048 | **Precision:** 1.000 | **Recall:** 0.025  

**Format:** `regex`  
**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.025 | 0.048 | 10 | 10 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 10 | 0 | 362 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2**

```
Die 
einzelnen Tankstellen der Houdek Maschinenbau  seien jeweils als eigenständige Teilbetriebe zu 
qualifizieren, für die jeweils gesondert der (Teilbetriebs)Gewinn zu ermitteln sei.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3**

```
Daraufhin wurde bei der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  das 
Jahr 2010 mit Bescheid vom 7.3.2016 wiederaufgenommen, ein neuer Feststellungsbescheid 
Gruppenmitglied erlassen und der Verlustvortrag um den strittigen Betrag (€ 665.812,12) 
erhöht.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4**

```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 5**

```
Bei den aus der Houdek Maschinenbau 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Roelfsen Versicherung  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Roelfsen Versicherung).
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

- Missed: `Roelfsen Versicherung` (organisation)

- Missed: `FA Wien 1/23` (organisation)

- Missed: `Roelfsen Versicherung` (organisation)


```
Daraufhin wurde bei der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  das 
Jahr 2010 mit Bescheid vom 7.3.2016 wiederaufgenommen, ein neuer Feststellungsbescheid 
Gruppenmitglied erlassen und der Verlustvortrag um den strittigen Betrag (€ 665.812,12) 
erhöht.
```

- Missed: `Roelfsen Versicherung` (organisation)


```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

- Missed: `Roelfsen Versicherung` (organisation)


```
Bei den aus der Houdek Maschinenbau 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Roelfsen Versicherung  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Roelfsen Versicherung).
```

- Missed: `Roelfsen Versicherung` (organisation)

- Missed: `Roelfsen Versicherung` (organisation)


```
Die Houdek Maschinenbau  habe daher jene Verluste, die den per 31.12.2007 auf die 
Schmeltz Luftfahrt  abgespaltenen Tankstellen zuzurechnen seien, vorrangig (und nicht wie von der 
BP vorgesehen nur aliquot) im Wege eines innerbetrieblichen Verlustausgleichs mit Gewinnen 
anderer Teilbetriebe ausgeglichen.
```

- Missed: `Schmeltz Luftfahrt` (organisation)


</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `company_kg_general`

**F1:** 0.022 | **Precision:** 0.122 | **Recall:** 0.012  

**Format:** `regex`  
**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)+\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.122 | 0.012 | 0.022 | 41 | 5 | 36 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 36 | 400 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Im Feststellungsverfahren der (damaligen) Schoenfelder Textil KG  wurde am 23. Oktober 2006 ein 
Feststellungsbescheid erlassen, fand im Jahr 2015 eine Betriebsprüfung statt und wurde am 18. 
Dezember 2015 das Feststellunsgsverfahren 2005 wiederaufgenommen und ein neuer 
Feststellungsbescheid erlassen.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

**Example 2**

```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 3**

```
Mit Erkenntnis vom 27. August 2024 gab das Bundesfinanzgericht ua. der Beschwerde gegen 
den Bescheid betreffend Wiederaufnahme des Feststellungsverfahren 2005 betreffend 
Schoenfelder Textil KG  statt und hob den Wiederaufnahmebescheid auf, da laut Mitteilung an das 
Bundesfinanzgericht vom Finanzamt neu angestellte Prognoserechungen ergeben hätten, dass 
die Rendite nach Steuern nicht doppelt so hoch wie vor Steuern liegen würde und somit kein 
Anwendungsfall des § 2 Abs. 2a EStG vorliege.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

**Example 4**

```
Die Beschwerde wendet sich somit mit Argumenten gegen den Einkommensteuerbescheid, die 
gegen den Bescheid über die Feststellung von Einkünften der WOD Sicherheit KG  gem. § 188 BAO vom 
20.1.2020 zu richten gewesen wären.
```

| Prediction | Gold |
|------------|------|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

**Example 5**

```
Im Feststellungsverfahren 2005 der Schoenfelder Textil KG  ergingen folgende Bescheide: 
23. Oktober 2006 Erlassung des Feststellungsbescheides 
18. Dezember 2015 Bescheid über die Wiederaufnahme des Feststellungsverfahrens 
   betreffend 2005 
18. Dezember 2015 Erlassung des neuen Feststellungebescheides 
27. August 2024 Erkenntnis des BFG, mit welchem der Beschwerde gegen die  
   Wiederaufnahme stattgegeben wird 
27. August 2024 Beschluss des BFG, mit welchem die Beschwerde gegen den  
   Feststellungsbescheid gegenstandslos erklärt wird.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Mit Ablauf des Stichtages 31. 
März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit 
Buchwertfortführung gem. Art IV UmgrStG. 
 Leiss Software  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober 2008 
gegründet.
```

- Missed: `Leiss Software` (organisation)


```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Süd Nortri  GmbH & Co KG 
und Hülsebusch + Breithaupt Versicherung  GmbH & Co KG angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung 
einer Beschwerde befugt ist, an den der den Gegenstand der Anfechtung bildende Bescheid 
ergangen ist.
```

- Missed: `Süd Nortri` (organisation)

- Missed: `Hülsebusch + Breithaupt Versicherung` (organisation)


```
Mit Ablauf des Stichtages 30. September 2008 erfolgte rückwirkend ein 
Verkehrswertzusammenschluss mit Buchwertfortführung gem. Art IV UmgrStG. 
 Okur Automotive  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 15. April 2009 
gegründet.
```

- Missed: `Okur Automotive` (organisation)


```
Celikkanat Garten  GmbH & Co KG: 
Aufstellung der Aufwendungen laut Gewinn und Verlustrechnung der Celikkanat Garten  GmbH & Co 
KG (atypisch stille Gesellschafterin) für das Jahr 2009: 
 € 
Initialisierungsaufwand 348,290,00 
Verkehrssteuern 24.030,00 
Lfd.
```

- Missed: `Celikkanat Garten` (organisation)

- Missed: `Celikkanat Garten` (organisation)


```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

- Missed: `Okur Automotive` (organisation)

- Missed: `Celikkanat Garten` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Mit Ablauf des Stichtages 31. 
März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit 
Buchwertfortführung gem. Art IV UmgrStG. 
 Leiss Software  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober 2008 
gegründet.
```

- FP: `Leiss Software  GmbH & Co KG` (organisation)


```
IM NAMEN DER REPUBLIK  
Das Bundesfinanzgericht hat durch den RichterM. in der Finanzstrafsache gegen Herrn 
Roland Sibbertsen, Reitenaustraße 4, 9500 Neufellach, Österreich, vertreten durch Schneider Rechtsanwalts KG, Rechte Bahnstraße 
10/19D, 1030 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung 
gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde der Beschuldigten 
vom 11. Dezember 2020 gegen den Zurückweisungsbescheid des Finanzamtes Wien 9/18/19 
Klosterneuburg als Finanzstrafbehörde vom 3. November 2020, Geschäftszahl FV-1, zu Recht 
erkannt: 
Die Beschwerde wird als unbegründet abgewiesen.
```

- FP: `Schneider Rechtsanwalts KG` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der 
Beschwerdesache Vera Lüerß, BA, Gewerbepark Hinterholz 3, 4974 Stött, Österreich, vertreten durch BKS Steuerberatung GmbH & Co 
KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, über die Beschwerde vom 
18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013 
betreffend Wiederaufnahme der Einkommensteuerverfahren 2003 bis 2010 sowie vom 
29.4.2013  betreffend Wiederaufnahme des Einkommensteuerverfahren 2011, Steuernummer 
***, zu Recht erkannt:  
Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- FP: `BKS Steuerberatung GmbH & Co 
KG` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der 
Beschwerdesache Ing. Miklos Novikova, Carl Lutz-Straße 44, 2225 Blumenthal, Österreich, vertreten durch BKS Steuerberatung GmbH & Co 
KG, Untere Hauptstraße 10, 3150 Wilhelmsburg, über die Beschwerde vom 14. Jänner 2019 
gegen den Haftungsbescheid des Finanzamtes Lilienfeld St. Pölten vom 17. Dezember 2018, 
Steuernummer 62-482/0330, Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- FP: `BKS Steuerberatung GmbH & Co 
KG` (organisation)


```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Süd Nortri  GmbH & Co KG 
und Hülsebusch + Breithaupt Versicherung  GmbH & Co KG angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung 
einer Beschwerde befugt ist, an den der den Gegenstand der Anfechtung bildende Bescheid 
ergangen ist.
```

- FP: `Nortri  GmbH & Co KG` (organisation)

- FP: `Breithaupt Versicherung  GmbH & Co KG` (organisation)


</details>

---

## `specific_org_fa_baden`

**F1:** 0.005 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Baden\s+M\xf6dling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.500 | 0.002 | 0.005 | 2 | 1 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 1 | 391 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Vitus Preimesser  in der Beschwerdesache Dipl.-Ing. Zdenko Faiss, 
Fützental 41, 2053 Jetzelsdorf, Österreich, über die Beschwerde vom 15.05.2019 gegen den Bescheid des seinerzeitigen 
Finanzamt Baden Mödling  vom 26.04.2019, betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2017, zu Recht erkannt: 
I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
IM NAMEN DER REPUBLI K 
Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden 
Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den 
Finanzstrafsachen gegen  
1. A B, [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich 
2. [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich 
3. [...]., Dr. Wagner-Gasse 35, 8700 Leoben, Österreich 
alle vertreten durch BKS Steuerberatungs GmbH W, Untere 
Hauptstraße 10, 3150 Wilhelmsburg 
wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des 
Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten 
Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates 
beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als 
Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des 
Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H., 
deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt: 
Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates 
aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den 
Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob 
fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der 
belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B 
Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.
```

- FP: `Finanzamt Baden Mödling` (organisation)


</details>

---

## `tax_office_finanzamt_graz_stadt`

**F1:** 0.005 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Graz-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.500 | 0.002 | 0.005 | 2 | 1 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 1 | 377 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Mit Bescheid des Finanzamt Graz-Stadt  vom 20.5.2022 wurde der begehrte 
Einkommensteuerbescheid 2020 erlassen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Graz-Stadt` | `Finanzamt Graz-Stadt` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- Missed: `InnLuftfahrt GMBH` (organisation)


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- FP: `Finanzamt Graz-Stadt` (organisation)


</details>

---

## `specific_org_fa_wien`

**F1:** 0.010 | **Precision:** 0.667 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.667 | 0.005 | 0.010 | 3 | 2 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 1 | 153 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Zusammenfassend kann festgehalten werden, dass vom Finanzamt Wien 1/23  bei der Argumentation 
generell übersehen worden ist, dass beim Verlustvortrag lediglich eine Bindung an die Höhe 
des im Körperschaftsteuerbescheid ausgewiesen Verlustes besteht.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 2**

```
Dr. Alexander Lamplmayr als gerichtlicher 
Erwachsenenvertreter, Landstraße 50, 4020 Linz,  über die Beschwerde der 
beschwerdeführenden Partei vom 25. Juni 2020 wegen behaupteter Verletzung der 
Entscheidungspflicht durch das Finanzamt Wien 1/23  betreffend die Anträge vom 3.5.2018 auf Zustellung 
des Bescheides vom 24.4.2018 betreffend Pfändung eines Kontos an die bestellte 
Sachwalterschaft (nunmehr: Erwachsenenvertretung), Rückzahlung der gepfändeten Beträge 
wegen rechtsunwirksamer Bescheidzustellung und daher rechtswidriger Kontopfändung, 
Gewährung der Akteneinsicht, in eventu auf Einstellung der Exekution und deren Aufschiebung 
bis zur Einstellung der Exekution sowie Rückzahlung der das Existenzminimum 
unterschreitenden gepfändeten Beträge, in eventu auf Aufhebung der Kontopfändung 
hinsichtlich des Teiles des bis zum nächsten Zahlungstermin notwendigen Unterhaltes in Höhe 
von 909,00 € und Rücküberweisung dieses Betrages, Steuernummer ***, beschlossen: 
a)
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Parteien des Ausgangsverfahrens am Bundesfinanzgericht RV/7103840/2015:  
Beschwerdeführerin: 
 Adriana Klimas 
 vertreten durch: Ernst & Young Steuerberatungsgesellschaft m.b.H., Wagramer 
Straße 19, 1220 Wien 
Belangte Behörde: 
 Finanzamt Wien 1/23, Marxergasse 4, 1030 Wien
```

- FP: `Finanzamt Wien 1/23` (organisation)


</details>

---

## `specific_org_raiffeisen_hyphen`

**F1:** 0.019 | **Precision:** 0.667 | **Recall:** 0.010  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+[A-Z][a-zA-Z]+(?:\s+-\s+[A-Z][a-zA-Z]+|\s+[A-Z][a-zA-Z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.667 | 0.010 | 0.019 | 6 | 4 | 2 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 2 | 315 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Am 27.12.2022 bezahlte die Raiffeisenbank Wienerwald  den Betrag von € 28.423,94 zuzüglich der 
gegenständlichen Pfändungsgebühr und Barauslagen (insg. sohin € 28.721,13) an die belangte 
Behörde, welche sodann die beiden anderen Forderungspfändungen einstellte.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 2**

```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Mittleres Mostviertel` | `Raiffeisenbank Mittleres Mostviertel` |

**Example 3**

```
Hierauf übermittelte der Beschwerdeführer ein Schreiben der Raiffeisenbank Stallhofen  vom 
24.2.2014, in welchem bestätigt wurde, dass er im Jahre 2013 € 4.377,00 an Kreditrückzahlung 
geleistet hat.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Stallhofen` | `Raiffeisenbank Stallhofen` |

**Example 4**

```
Darüber hinaus habe die belangte 
Behörde das Konto des Beschwerdeführers vor Weihnachten unrechtmäßig um den Betrag 
vom € 28.423,94 „ausgeplündert“ und zudem auf zwei Konten gleichzeitig zugegriffen, obwohl 
eines dieser Konten zwei Personen gemeinsam gehört und der Zugriff auf das andere Konto 
(bei der Raiffeisenbank Wienerwald) ausgereicht hätte, um die Forderung vollständig zu befriedigen.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Mit Bescheid des Zollamtes Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der Raiffeisenbank Wels Süd  mitgeteilt, dass der Bf Abgaben einschließlich Nebengebühren in Höhe von 
€ 63.917,32 schuldet.
```

- Missed: `Raiffeisenbank Wels Süd` (organisation)


```
Wegen eines Teilbetrages in Höhe von € 10.000,00 wurde die dem Bf 
gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem bezeichneten Girokonto zustehende 
Forderung gepfändet.
```

- Missed: `Raiffeisenbank Wels Süd` (organisation)


```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

- Missed: `Niederösterreichische Vorsorgekasse` (organisation)


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Mit Bescheid des Zollamtes Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der Raiffeisenbank Wels Süd  mitgeteilt, dass der Bf Abgaben einschließlich Nebengebühren in Höhe von 
€ 63.917,32 schuldet.
```

- FP: `Raiffeisenbank Wels` (organisation)


```
Wegen eines Teilbetrages in Höhe von € 10.000,00 wurde die dem Bf 
gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem bezeichneten Girokonto zustehende 
Forderung gepfändet.
```

- FP: `Raiffeisenbank Wels` (organisation)


</details>

---

</details>

---

<details>
<summary>📋 All Rules</summary>

## `tax_office_fa`

**F1:** 0.223 | **Precision:** 0.981 | **Recall:** 0.126  

**Format:** `regex`  
**Content:**
```
\bFA\s+(?:Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Wien\s+8/16/17|Salzburg-Stadt|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Amstetten\s+Melk\s+Scheibbs|Steiermark\s+Mitte|\d+/?\d+|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Tirol\s+Ost|Nieder\xf6sterreich\s+Mitte|Grieskirchen\s+Wels|Linz|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Klosterneuburg|Salzburg-Land|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Purkersdorf|Vorarlberg|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Waldviertel|Oststeiermark|Spittal\s+Villach|Gmunden\s+V\xf6cklabruck|Wien\s+1/23|Wien\s+8/16/17|Steiermark\s+Mitte|Nieder\xf6sterreich\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Amstetten\s+Melk\s+Scheibbs|Grieskirchen\s+Wels|Gmunden\s+V\xf6cklabruck|Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Purkersdorf|Vorarlberg|Waldviertel|Oststeiermark|Spittal\s+Villach|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+8/16/17|Graz-Stadt|Salzburg-Stadt|Salzburg-Land|Judenburg\s+Liezen|Klosterneuburg|Freistadt\s+Rohrbach\s+Urfahr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)(?!\s+vom|\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.981 | 0.126 | 0.223 | 52 | 51 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 51 | 1 | 352 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
 KommR Ing. Roberta Gossling  sei die Veranstalterin und FA Salzburg-Stadt  zumindest Vermittlerin der 
Ausspielungen.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 2**

```
Am 11.11.2022 
ging der gepfändete Betrag in Höhe von EUR 4.681,64 am Konto des FA Braunau Ried Schärding  ein und ist am 
Abgabenkonto des Beschwerdeführers verbucht.
```

| Prediction | Gold |
|------------|------|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Example 3**

```
BESCHLUSS 
Das Bundesfinanzgericht hat durch die Richterin Dr.in Leila Coutand  in der Beschwerdesache des 
Evelyn Kogelheide, Rechte Fischa-Promenade 64, 4812 Pinsdorfberg, Österreich  vertreten durch RA,  über die Beschwerde vom 20. November 2017 
gegen die Bescheide des FA Vorarlberg (nunmehr: Finanzamt Österreich) vom 19. Oktober 2015 
betreffend Einkommensteuer 2007 und 2008 zu Steuernummer 11-143/2882  beschlossen: 
I. Die Einkommensteuerbescheide für die Jahre 2007 und 2008 vom 19. Oktober 2015 
und die Beschwerdevorentscheidung vom 6. Feber 2018 werden gemäß § 278 Abs. 1 
BAO unter Zurückverweisung der Sache an die Abgabenbehörde aufgehoben.
```

| Prediction | Gold |
|------------|------|
| `FA Vorarlberg` | `FA Vorarlberg` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Andrea Trenka  in der Beschwerdesache Hademar Wischollek, 
St.Oswald - Rosennockstraße 25, 4343 Am Bühel, Österreich  vertreten durch Juri Marthiens, und Quentin Eichelmann, über die Beschwerden vom 10. 
Jänner 2018, 15. Jänner 2020, 10. Februar 2020, und 24. Februar 2020 gegen die Bescheide des 
FA Linz (nunmehr Finanzamt Österreich) zu Steuernummer 09-470/7083  betreffend 
Umsatz- und Körperschaftsteuer 2007, 2009 bis 2018 samt Wiederaufnahme dieser Verfahren 
betreffend die Jahre bis 2013 und Haftung für Kapitalertragsteuern 2009 bis 2017 
1.
```

| Prediction | Gold |
|------------|------|
| `FA Linz` | `FA Linz` |

**Example 5**

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

| Prediction | Gold |
|------------|------|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

</details>

<details>
<summary>❌ Missed (4)</summary>

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

- Missed: `Annemie Bott` (organisation)


```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

- Missed: `Roelfsen Versicherung` (organisation)

- Missed: `Houdek Maschinenbau` (organisation)

- Missed: `Roelfsen Versicherung` (organisation)


```
Im Rahmen der Beschwerde wurde – neben der Rechnung der Waldver E‑Commerce Systeme GMBH  und 
einem Schreiben des FA Salzburg-Land – eine Kopie des Behindertenpasses vom 10.06.2014 
übermittelt, aus der ein Grad der Behinderung von 50% sowie eine Gesundheitsschädigung 
gemäß § 2 Abs. 1 erster Teilstrich der VO 303/1996 hervorgeht.
```

- Missed: `Waldver E‑Commerce Systeme GMBH` (organisation)


```
Mit den gegenständlich angefochtenen Einkommensteuerbescheiden für die Jahre 2007 und 
2008 vom 5.9.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (FA 07) die 
Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter Berücksichtigung der 
Grundlagenbescheide vom 7.2.2011 betreffend Mitunternehmerschaft (atypisch stillen 
Beteiligung) an der TalVerverwerkGarten GMBH & atypisch stille Gesellschafter, St.nr. xx-xxx/xxxx 
(Beteiligung in den Streitjahren) fest.
```

- Missed: `TalVerverwerkGarten GMBH` (organisation)


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Mit den gegenständlich angefochtenen Einkommensteuerbescheiden für die Jahre 2007 und 
2008 vom 5.9.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (FA 07) die 
Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter Berücksichtigung der 
Grundlagenbescheide vom 7.2.2011 betreffend Mitunternehmerschaft (atypisch stillen 
Beteiligung) an der TalVerverwerkGarten GMBH & atypisch stille Gesellschafter, St.nr. xx-xxx/xxxx 
(Beteiligung in den Streitjahren) fest.
```

- FP: `FA 07` (organisation)


</details>

---

## `company_gmbh_general`

**F1:** 0.163 | **Precision:** 0.740 | **Recall:** 0.091  

**Format:** `regex`  
**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)+\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.740 | 0.091 | 0.163 | 50 | 37 | 13 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 37 | 13 | 365 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Mit Haftungsbescheid vom 7. April 2016 wurde der Bf. als ehemaliger Geschäftsführer für die 
aushaftende Abgabenschuld der OGEM Landwirtschaft GMBH  in Höhe von Euro 22.605,06 in Anspruch 
genommen.
```

| Prediction | Gold |
|------------|------|
| `OGEM Landwirtschaft GMBH` | `OGEM Landwirtschaft GMBH` |

**Example 2**

```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

**Example 3**

```
Auch in den von der Rhein Normonkel Manufaktur GMBH  an das Finanzamt 
übermittelten Lohnzettel, der den im Einkommensteuerbescheid 2014 vom 20.5.2015 
ausgewiesenen Einkünften aus nichtselbständiger Arbeit zugrunde liegt, hat der volle Pkw-
Sachbezug Eingang gefunden.
```

| Prediction | Gold |
|------------|------|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 4**

```
Soweit es den Mitarbeitern der Bludszat Maschinenbau GMBH  möglich war, haben diese auch Kontakt mit der 
MA 6 gehalten.
```

| Prediction | Gold |
|------------|------|
| `Bludszat Maschinenbau GMBH` | `Bludszat Maschinenbau GMBH` |

**Example 5**

```
Entscheidungsgründe 
I. Verfahrensgang 
Mit Bescheid vom 27. April 2016, der Beschwerdeführerin per Post zugegangen am 4. Mai 2016, 
setzte die belangte Behörde für den am 30. November 2015 zwischen der Beschwerdeführerin 
und der Verdonlex Automotive GMBH  unter Beitritt der Schiwick Finanzen AG  schriftlich geschlossenen Pachtvertrag 
gemäß § 33 TP 7 Abs 1 GebG  eine Gebühr im Betrag von 43.480, - Euro fest.
```

| Prediction | Gold |
|------------|------|
| `Verdonlex Automotive GMBH` | `Verdonlex Automotive GMBH` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

- Missed: `Kraftver-Gastronomie GMBH` (organisation)


```
Im Zeitraum 01.01.2019 – 27.04.2019 war die Bf. bei der Firma Kreschmer Recycling GMBH  im Inland 
beschäftigt.
```

- Missed: `Kreschmer Recycling GMBH` (organisation)


```
Entscheidungsgründe 
I. Verfahrensgang 
Mit Bescheid vom 27. April 2016, der Beschwerdeführerin per Post zugegangen am 4. Mai 2016, 
setzte die belangte Behörde für den am 30. November 2015 zwischen der Beschwerdeführerin 
und der Verdonlex Automotive GMBH  unter Beitritt der Schiwick Finanzen AG  schriftlich geschlossenen Pachtvertrag 
gemäß § 33 TP 7 Abs 1 GebG  eine Gebühr im Betrag von 43.480, - Euro fest.
```

- Missed: `Schiwick Finanzen AG` (organisation)


```
BESCHLUSS 
Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Priv.-Doz. Samir Bierdimpfl  in der Beschwerdesache Kraftver-Gastronomie GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, über den Vorlageantrag der Gartgart Dienstleistungen GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, vom 
18.9.2020 gegen die an die Kraftver-Gastronomie GMBH  ergangene Beschwerdevorentscheidung des 
Finanzamts Graz-Stadt vom 9.9.2020 betreffend Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO beschlossen: 
I. Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig 
zurückgewiesen.
```

- Missed: `Kraftver-Gastronomie GMBH` (organisation)

- Missed: `Kraftver-Gastronomie GMBH` (organisation)


```
Die UnterRecycling Services GMBH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen 
Berufenen, Herrn Valentina Riehmers, verhängten Geldstrafen von 5 x je € 510,00 und 2 x je € 520,00 
und die Verfahrenskosten in der Höhe von € 359,00 sowie für sonstige in Geld bemessene 
Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.
```

- Missed: `UnterRecycling Services GMBH` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Im Zeitraum 01.01.2019 – 27.04.2019 war die Bf. bei der Firma Kreschmer Recycling GMBH  im Inland 
beschäftigt.
```

- FP: `Firma Kreschmer Recycling GMBH` (organisation)


```
Die UnterRecycling Services GMBH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen 
Berufenen, Herrn Valentina Riehmers, verhängten Geldstrafen von 5 x je € 510,00 und 2 x je € 520,00 
und die Verfahrenskosten in der Höhe von € 359,00 sowie für sonstige in Geld bemessene 
Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.
```

- FP: `Die UnterRecycling Services GMBH` (organisation)


```
3. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im Juli 2020 vor 
der Liegenschaft in Rodelsbach 3, 4800 Lehen, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen 
Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür 
bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe 
entrichtet habe.
```

- FP: `Firma UnterRecycling Services GMBH` (organisation)


```
Das Bundesfinanzgericht wollte mit seiner Erledigung vom 14. Jänner 2019 die Beschwerde der 
Hudec&Christian Immobilien GMBH  betreffend die Feststellung von Einkünften gemäß § 188 BAO als 
unzulässig zurückweisen und damit mit Rechtskraftwirkung für alle am Feststellungsverfahren 
Beteiligten aussprechen, dass die vor ihm bekämpften Feststellungsbescheide nicht wirksam 
geworden waren.
```

- FP: `Christian Immobilien GMBH` (organisation)


```
BESCHLUSS 
Das Bundesfinanzgericht beschließt durch die Richterin Dr. Lisa Pucher in der Beschwerdesache 
Enns Werkal GMBH, Föhrenwald III 19, 3140 Pottenbrunn, Österreich, vertreten durch Geyer & Geyer Wirtschaftstreuhänder 
GmbH, Rudolf von Alt-Platz 1, 1030 Wien, über die Beschwerden der beschwerdeführenden 
Partei vom 07. August 2024 wegen behaupteter Verletzung der Entscheidungspflicht 
hinsichtlich nachfolgend angeführter Eingaben zu Steuernummer 04-382/0421:  
1) Beschwerde vom 27.03.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung eines ersten Säumniszuschlages vom 09.03.2023 
2) Beschwerde vom 11.05.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 11.04.2023 
3) Beschwerde vom 05.07.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 09.06.2023  
4) Beschwerde vom 08.08.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens vom 
19.07.2023 
5) Beschwerde vom 08.08.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 10.07.2023 
6) Beschwerde vom 31.08.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 09.08.2023 
7) Antrag vom 05.07.2023 auf Aufhebung des Bescheides über die Festsetzung von 
Nebengebühren gemäß § 299 BAO vom 09.05.2023 
8) Beschwerde vom 11.05.2023 gegen den Bescheid des Finanzamtes für Großbetriebe über 
die Festsetzung von ersten Säumniszuschlägen vom 09.01.2023
```

- FP: `Beschwerdesache 
Enns Werkal GMBH` (organisation)


</details>

---

## `tax_office_finanzamt`

**F1:** 0.150 | **Precision:** 0.723 | **Recall:** 0.084  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+(?:Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Wien\s+8/16/17|Salzburg-Stadt|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Amstetten\s+Melk\s+Scheibbs|Steiermark\s+Mitte|\d+/?\d+|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Tirol\s+Ost|Nieder\xf6sterreich\s+Mitte|Grieskirchen\s+Wels|Linz|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Klosterneuburg|Salzburg-Land|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Purkersdorf|Vorarlberg|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Waldviertel|Oststeiermark|Spittal\s+Villach|Gmunden\s+V\xf6cklabruck|Wien\s+1/23|Wien\s+8/16/17|Steiermark\s+Mitte|Nieder\xf6sterreich\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Amstetten\s+Melk\s+Scheibbs|Grieskirchen\s+Wels|Gmunden\s+V\xf6cklabruck|Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Purkersdorf|Vorarlberg|Waldviertel|Oststeiermark|Spittal\s+Villach|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+8/16/17|Graz-Stadt|Salzburg-Stadt|Salzburg-Land|Judenburg\s+Liezen|Klosterneuburg|Freistadt\s+Rohrbach\s+Urfahr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)(?!\s+vom|\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.723 | 0.084 | 0.150 | 47 | 34 | 13 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 34 | 13 | 364 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Das Bundesfinanzgericht hat durch den Richter Mag. Berthold Brodag  in der Beschwerdesache VetR Frauke Gibhardt, 
Trulitsch 43, 8832 Hinterburg, Österreich, vertreten durch Standfest & Partner Rechtsanwälte GmbH, Wallnerstraße 
4/5/MT 44, 1010 Wien, über die Beschwerde vom 27. Jänner 2017 gegen den Bescheid des 
Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt FA) vom 15. Dezember 2016 betreffend 
Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff Bundesabgabenordnung (BAO), 
Steuernummer St.Nr., beschlossen: 
 
I. Der angefochtene Bescheid vom 15. Dezember 2016 und die Beschwerdevorentscheidung 
vom 27. September 2018 werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache 
an die Abgabenbehörde aufgehoben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | `Finanzamt Klagenfurt St. Veit Wolfsberg` |

**Example 2**

```
Der Gewinn 
von Larissa Gmelich  bemesse sich ausschließlich anhand der Kommission, die an Finanzamt Judenburg Liezen 
verrechnet wird.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 3**

```
Das Bundesfinanzgericht hat durch den Richter Dr. Emmerich Vnucec  in der Beschwerdesache Aron Plotke, 
Oberschwarzerweg 2, 3553 Schiltern, Österreich, über die Beschwerde vom 23. Februar 2017 gegen den Bescheid des Finanzamt Grieskirchen Wels 
(nunmehr Finanzamt FA) vom 23. Jänner 2017 betreffend Haftungsinanspruchnahme gemäß 
§§ 9 iVm 80ff BAO, Steuernummer 50-942/3785, zu Recht erkannt:  
 
I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) teilweise Folge gegeben 
und die Haftung auf den Betrag von 4.986,13 Euro eingeschränkt.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 4**

```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 5**

```
Die Säumnisbeschwerden waren daher schon deshalb zurückzuweisen, da am 8. Februar 2021 
das Finanzamt Innsbruck  nicht mehr existierte und somit keine Säumnis dieses Finanzamtes vorliegen 
konnte (ebenso BFG vom 1.2.2021, RS/5100003/2021).
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Innsbruck` | `Finanzamt Innsbruck` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- Missed: `InnLuftfahrt GMBH` (organisation)


```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Annemie Bott` (organisation)

- Missed: `Milan Händlein` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Linn Pelzner  in der Beschwerdesache der 
Alal-Medien, Dichtlstraße 32, 4656 Windberg, Österreich  vertreten durch Vertreter-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999-99-999/9999 (M- GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt 
Dienststelle des Finanzamt Gmunden Vöcklabruck) vom 5. November 2019 betreffend Heranziehung als 
Gemeinschuldnerin für „Umsatzsteuerveranlagungen und div.
```

- Missed: `Alal-Medien` (organisation)


```
Mit Bescheid vom 25. April 2019 hat das Finanzamt Salzburg-Stadt gegenüber Gökdemir Landwirtschaft AG  eine 
Geldforderung in Höhe von insgesamt € 4.225,30 gemäß § 65 AbgEO gepfändet, weil der Bf 
angeblich beschränkt pfändbare Forderungen aus einem Arbeitsverhältnis oder sonstige 
Bezüge im Sinne des § 290a EO gegen diese zustehen.
```

- Missed: `Gökdemir Landwirtschaft AG` (organisation)


```
Das Bundesfinanzgericht hat durch den Richter Dr. Gisbert Rischmüller  in der Angelegenheit der Parteien 
Ludger Flickschuh (Beschwerdeführerin), vertreten durch die Kienberger Steuerberatungs GmbH, 
9020 Klagenfurt und Finanzamt Österreich (Amtspartei) als Gesamtrechtsnachfolger des 
Finanzamt St. Johann Tamsweg Zell am See  über die Beschwerden vom 17.12.2015       
        gegen die Bescheide des FA St. Johann Tamsweg Zell am See  vom 17.11.2015 betreffend Umsatzsteuer 2012 und 
2013        
zu Recht erkannt: 
Ad Beschwerde gegen den Bescheid betreffend Umsatzsteuer 2012: 
Der bekämpfte Bescheid wird abgeändert.
```

- Missed: `FA St. Johann Tamsweg Zell am See` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- FP: `Finanzamt Graz-Stadt` (organisation)


```
Kff. Finn Jonigk, Arthur-Krupp-Straße 27, 9655 Moos, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH & 
Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 16. Februar 2018 gegen 
den Bescheid  
a. vom 17. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 sowie  
b. vom 18. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, beide 
erlassen vom Finanzamt Spittal Villach, Steuernummer 46-794/1326, zu Recht erkannt:  
I. Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO 
als unbegründet abgewiesen.
```

- FP: `Finanzamt Spittal Villach` (organisation)


```
Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der 
Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische 
Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur 
Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit 
1 von 20
Seite 2 von 20
```

- FP: `Finanzamt Innsbruck` (organisation)


```
In dieser Stellungnahme teilte das Finanzamt Salzburg-Stadt als Finanzstrafbehörde mit, dass 
nach dessen Ansicht gegen die bP der begründete Verdacht bestehe, dass diese 
Finanzvergehen der Abgabenhinterziehung gem § 33 Abs 1 FinstrG sowie 
Finanzordnungswidrigkeiten gem § 51 Abs 1 lit a FinStrG, jeweils im og Umfang, begangen 
habe, wobei DDr.in Kerstin Tittrich, BA  als steuerlicher Vertreter der bP dazu beigetragen habe, dass die 
bP die Abgabenhinterziehung betreffend Umsatzsteuer 2016 iHv € 58.333,33 begehen konnte.
```

- FP: `Finanzamt Salzburg-Stadt` (organisation)


```
Sachverhalt 
1.1 
Margarete Mroß, BSc  als Beschwerdeführer wurde vom Finanzamt Innsbruck als Wohnsitzfinanzamt 
Familienbeihilfe für die Kinder E …, D …, C … und A … seit dem Jahr 2012 und laufend gewährt.
```

- FP: `Finanzamt Innsbruck` (organisation)


</details>

---

## `company_ag_general`

**F1:** 0.088 | **Precision:** 0.679 | **Recall:** 0.047  

**Format:** `regex`  
**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)*\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.679 | 0.047 | 0.088 | 28 | 19 | 9 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 19 | 9 | 382 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Über die grundsätzliche Streitfrage, ob die erhaltenen Vertreterentschädigungen von 
Hausbesorgern, die im Dienstverhältnis zu MittelHeizung Werke AG  stehen, als „durchlaufende Posten“ bzw. 
„Auslagenersätze iSd § 26 Z 2 EStG 1988“ oder als steuerpflichtiger Arbeitslohn zu behandeln 
sind, hat das Bundesfinanzgericht mit Erkenntnis vom 17.11.2022, RV/7100193/2021 
entschieden und weder „durchlaufende Posten“ noch „Auslagenersätze“ erkannt.
```

| Prediction | Gold |
|------------|------|
| `MittelHeizung Werke AG` | `MittelHeizung Werke AG` |

**Example 2**

```
Das Finanzamt erließ erklärungsgemäß einen Einkommensteuerbescheid für das Jahr 2014, in 
dem Einkünfte aus nichtselbständiger Arbeit aufgrund folgender Lohnzettel enthalten waren: 
Bezugszeitraum: 1.1.2014 bis 21.02.2014, Bezugsauszahlende Stelle: Berend Energie AG 
Bezugszeitraum: 1.1.2014 bis 31.12.2014, Bezugsauszahlende Stelle: Valida Plus   
Bezugszeitraum: 02.05.2014 bis 31.12.2014, Bezugsauszahlende Stelle: Blazickova & Hepprich Energie AG  
In diesem Kalenderjahr bezog der BF noch in folgenden Zeiträumen Leistungen des 
Arbeitsmarktservice Österreich (AMS): 
22.02.2014 bis 09.06.2014 
10.06.2014 bis 30.06.2014 
01.07.2014 bis 09.09.2014 
1 von 8
Seite 2 von 8
```

| Prediction | Gold |
|------------|------|
| `Berend Energie AG` | `Berend Energie AG` |
| `Blazickova & Hepprich Energie AG` | `Blazickova & Hepprich Energie AG` |

**Example 3**

```
Vor diesem Hintergrund kann die in der im Beschwerdefall vereinbarte Bedingun g der 
Inanspruchnahme der Schiwick Finanzen AG , „ dass der Pächter trotz schriftlicher Aufforderung und 
Fristsetzung von 4 Wochen seinen Verpflichtungen aus dem Vertrag nicht nachkommt “, nicht 
5 von 7
Seite 6 von 7
```

| Prediction | Gold |
|------------|------|
| `Schiwick Finanzen AG` | `Schiwick Finanzen AG` |

**Example 4**

```
Entscheidungsgründe 
I. Verfahrensgang 
Mit Bescheid vom 27. April 2016, der Beschwerdeführerin per Post zugegangen am 4. Mai 2016, 
setzte die belangte Behörde für den am 30. November 2015 zwischen der Beschwerdeführerin 
und der Verdonlex Automotive GMBH  unter Beitritt der Schiwick Finanzen AG  schriftlich geschlossenen Pachtvertrag 
gemäß § 33 TP 7 Abs 1 GebG  eine Gebühr im Betrag von 43.480, - Euro fest.
```

| Prediction | Gold |
|------------|------|
| `Schiwick Finanzen AG` | `Schiwick Finanzen AG` |

**Example 5**

```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

| Prediction | Gold |
|------------|------|
| `Schiwick Finanzen AG` | `Schiwick Finanzen AG` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Festgestellter Sachverhalt  
Im Jahr 2016 war die beschwerdeführende Partei beim Unternehmen Logbach-Bildung AG  als Key 
Account Manager / Business Development Manager – Angestellter tätig.
```

- Missed: `Logbach-Bildung AG` (organisation)


```
Entscheidungsgründe 
I. Verfahrensgang 
Mit Bescheid vom 27. April 2016, der Beschwerdeführerin per Post zugegangen am 4. Mai 2016, 
setzte die belangte Behörde für den am 30. November 2015 zwischen der Beschwerdeführerin 
und der Verdonlex Automotive GMBH  unter Beitritt der Schiwick Finanzen AG  schriftlich geschlossenen Pachtvertrag 
gemäß § 33 TP 7 Abs 1 GebG  eine Gebühr im Betrag von 43.480, - Euro fest.
```

- Missed: `Verdonlex Automotive GMBH` (organisation)


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- Missed: `Verdonlex Automotive GMBH` (organisation)


```
Er stand ganzjährig in einem 
Dienstverhältnis zur Hörup Gastronomie AG.
```

- Missed: `Hörup Gastronomie AG` (organisation)


```
Kz 245): 
 
Donau Furtkraftwald AG  1.1.2017 - 31.12.2017 € 4.915,96 
Schoebel Getränke AG  1.1.2017 - 21.4.2017 € 4.466,60 
Donber AG  10.4.2017 - 10.4.2017 € 36,35 
Tal-Lebensmittel Gruppe AG  22.4.2017 - 30.6.2017 € 3.348,55 
Brucktraval AG  1.7.2017 - 31.12.2017 € 6.588,48
```

- Missed: `Schoebel Getränke AG` (organisation)

- Missed: `Tal-Lebensmittel Gruppe AG` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Festgestellter Sachverhalt  
Im Jahr 2016 war die beschwerdeführende Partei beim Unternehmen Logbach-Bildung AG  als Key 
Account Manager / Business Development Manager – Angestellter tätig.
```

- FP: `Bildung AG` (organisation)


```
Der in den Verwaltungsakten enthaltenen Beschwerdevoretscheidung vom 23.1.2019, die 
nachweislich am 6.2.2019 zugestellt wurde (siehe Übernahmebestätigung der Österreichische 
Post AG), ist zu entnehmen, dass über die Beschwerde des Herrn Jörg Kosolek  wegen 
Kommunalsteuer und Dienstgeberabgabe abgesprochen werden sollte.
```

- FP: `Post AG` (organisation)


```
Er stand ganzjährig in einem 
Dienstverhältnis zur Hörup Gastronomie AG.
```

- FP: `Gastronomie AG` (organisation)


```
Kz 245): 
 
Donau Furtkraftwald AG  1.1.2017 - 31.12.2017 € 4.915,96 
Schoebel Getränke AG  1.1.2017 - 21.4.2017 € 4.466,60 
Donber AG  10.4.2017 - 10.4.2017 € 36,35 
Tal-Lebensmittel Gruppe AG  22.4.2017 - 30.6.2017 € 3.348,55 
Brucktraval AG  1.7.2017 - 31.12.2017 € 6.588,48
```

- FP: `Lebensmittel Gruppe AG` (organisation)


```
Die 
Feststellungen zur beruflichen Tätigkeit des Beschwerdeführers, zu den konkreten Einsatzorten 
und zu den von seinem Arbeitgeber geleisteten Kostenersätzen gründen sich auf das Schreiben 
der Cervenka&Neunübel Telekom AG  vom 9.6.2016 sowie die mit diesem Schreiben übermittelten Beilagen 
(„Dienstnehmerkalender“ und „Baustellenbesetzung“).
```

- FP: `Telekom AG` (organisation)


</details>

---

## `specific_org_milan`

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Content:**
```
\bMilan\s+H\xe4ndlein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.032 | 0.062 | 13 | 13 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 13 | 0 | 313 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Der Sachverhalt ergibt sich bisherigen Verfahren wie folgt: 
 a) Sachverhalt und Verfahrensablauf bei der Milan Händlein, Str.Nr.
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

**Example 2**

```
im Ergebnis hat sich auf Ebene der Milan Händlein  ein Verlust in Höhe von EUR 3.632.188,29 
ergeben, welcher vorgetragen wurde und erstmals im Jahr 2010 auf Ebene der 
Rechtsnachfolgerin in der Feststellungserklärung Gruppenmitglied weise geltend gemacht 
werden konnte.
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

**Example 3**

```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

**Example 4**

```
Verluste 
verbleibende 
Teilbetriebe 
Milan Händlein: 
-3.606.018,18 74,89 %
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

**Example 5**

```
2010 teil Im Zuge der in den Jahren 2011 bis 2013 bei der Milan Händlein 
erfolgten Außenprüfung betreffend Jahre 2007 und 2008 hat diesen Sachverhalt einer 
Überprüfung unterzogen und die bisherige Verlustverrechnung als unzutreffend beurteilt.
```

| Prediction | Gold |
|------------|------|
| `Milan Händlein` | `Milan Händlein` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Annemie Bott` (organisation)


```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Annemie Bott` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)


```
64-207/8107, BV 24 : 
Beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott  gab es betreffend dem 
Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid 
Gruppenmitglied: 
21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010 
27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid 
Gruppenmitglied 2010 nach Betriebsprüfung  
27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 
20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010 
(Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung 
Rekultivierungskosten) 
19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt 
Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung 
Rekultivierungskosten) 
29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW) 
16.12.2013 Vorlage an BFG (damals noch UFS) 
17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete 
Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW) 
Betreffend des Rechtsvorgängers Milan Händlein  wurde das Erkenntnis des 
Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum 
Veranlagungsjahr 2007 erlassen.
```

- Missed: `Annemie Bott` (organisation)


</details>

---

## `specific_org_houdek`

**F1:** 0.048 | **Precision:** 1.000 | **Recall:** 0.025  

**Format:** `regex`  
**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.025 | 0.048 | 10 | 10 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 10 | 0 | 362 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2**

```
Die 
einzelnen Tankstellen der Houdek Maschinenbau  seien jeweils als eigenständige Teilbetriebe zu 
qualifizieren, für die jeweils gesondert der (Teilbetriebs)Gewinn zu ermitteln sei.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3**

```
Daraufhin wurde bei der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  das 
Jahr 2010 mit Bescheid vom 7.3.2016 wiederaufgenommen, ein neuer Feststellungsbescheid 
Gruppenmitglied erlassen und der Verlustvortrag um den strittigen Betrag (€ 665.812,12) 
erhöht.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4**

```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 5**

```
Bei den aus der Houdek Maschinenbau 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Roelfsen Versicherung  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Roelfsen Versicherung).
```

| Prediction | Gold |
|------------|------|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

- Missed: `Roelfsen Versicherung` (organisation)

- Missed: `FA Wien 1/23` (organisation)

- Missed: `Roelfsen Versicherung` (organisation)


```
Daraufhin wurde bei der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  das 
Jahr 2010 mit Bescheid vom 7.3.2016 wiederaufgenommen, ein neuer Feststellungsbescheid 
Gruppenmitglied erlassen und der Verlustvortrag um den strittigen Betrag (€ 665.812,12) 
erhöht.
```

- Missed: `Roelfsen Versicherung` (organisation)


```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

- Missed: `Roelfsen Versicherung` (organisation)


```
Bei den aus der Houdek Maschinenbau 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Roelfsen Versicherung  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Roelfsen Versicherung).
```

- Missed: `Roelfsen Versicherung` (organisation)

- Missed: `Roelfsen Versicherung` (organisation)


```
Die Houdek Maschinenbau  habe daher jene Verluste, die den per 31.12.2007 auf die 
Schmeltz Luftfahrt  abgespaltenen Tankstellen zuzurechnen seien, vorrangig (und nicht wie von der 
BP vorgesehen nur aliquot) im Wege eines innerbetrieblichen Verlustausgleichs mit Gewinnen 
anderer Teilbetriebe ausgeglichen.
```

- Missed: `Schmeltz Luftfahrt` (organisation)


</details>

---

## `specific_org_fa_salzburg`

**F1:** 0.048 | **Precision:** 1.000 | **Recall:** 0.025  

**Format:** `regex`  
**Content:**
```
\bFA\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.025 | 0.048 | 10 | 10 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 10 | 0 | 393 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
 KommR Ing. Roberta Gossling  sei die Veranstalterin und FA Salzburg-Stadt  zumindest Vermittlerin der 
Ausspielungen.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Ludwig Widermann  in der Beschwerdesache Gisbert Delarue, 
Schöpferstraße 129, 5232 Gumping, Österreich, vertreten durch Dr. Michael Kotschnigg, Stadlauer Straße 39/I/Top12, 1220 
Wien, über die Beschwerde vom 13. Februar 2023 gegen den Bescheid über die Festsetzung 
von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens des FA Salzburg-Stadt  vom 
11. Jänner 2023 zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 3**

```
Kfm. Heinz Pavlos, 
Am Schenkenbichl 1, 4775 Oberpramau, Österreich, gegen die von der belangten Behörde FA Salzburg-Stadt, nunmehr Finanzamt 
Österreich, am 18. Dezember 2019 ausgefertigten Bescheide betreffend Einkommensteuer für 
die Jahre 2014 bis 2018 zu Recht erkannt: 
I. Die angefochtenen Bescheide werden gemäß § 279 BAO abgeändert.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 4**

```
IM NAMEN DER REPUBLIK  
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Priv.-Doz. Wolfgang Matschaj  in der Beschwerdesache Ing. Tristan Frommholz, 
Am Vierkanthof 7, 2115 Ernstbrunn, Österreich, vertreten durch Halbwachs Schmitt & Partner STB, Mariahilfer Straße 126/24, 
1070 Wien, über die Beschwerde gegen den Bescheid des FA Salzburg-Stadt  vom 12. März 2013, 
betreffend Körperschaftsteuer 2011 zu Recht erkannt:  
Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 5**

```
Hierbei beauftragt der Spielteilnehmer FA Salzburg-Stadt  mit Abgabe von Tipps bei 
KommR Ing. Roberta Gossling  namens der Spielergemeinschaft mit der Erbringung der in den AGB von FA Salzburg-Stadt 
unter Ziffer 5 genannten Serviceleistungen.
```

| Prediction | Gold |
|------------|------|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

</details>

---

## `tax_office_finanzamt_grieskirchen`

**F1:** 0.048 | **Precision:** 1.000 | **Recall:** 0.025  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Grieskirchen\s+Wels\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.025 | 0.048 | 10 | 10 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 10 | 0 | 327 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Das Bundesfinanzgericht hat durch den Richter Dr. Emmerich Vnucec  in der Beschwerdesache Aron Plotke, 
Oberschwarzerweg 2, 3553 Schiltern, Österreich, über die Beschwerde vom 23. Februar 2017 gegen den Bescheid des Finanzamt Grieskirchen Wels 
(nunmehr Finanzamt FA) vom 23. Jänner 2017 betreffend Haftungsinanspruchnahme gemäß 
§§ 9 iVm 80ff BAO, Steuernummer 50-942/3785, zu Recht erkannt:  
 
I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) teilweise Folge gegeben 
und die Haftung auf den Betrag von 4.986,13 Euro eingeschränkt.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 2**

```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 3**

```
Hierbei beauftragt der Spielteilnehmer Finanzamt Grieskirchen Wels  mit Abgabe von Tipps bei 
Noel Klasson  namens der Spielergemeinschaft mit der Erbringung der in den AGB von Finanzamt Grieskirchen Wels 
unter Ziffer 5 genannten Serviceleistungen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 4**

```
über die Beschwerden vom 29. März 2019 gegen den Bescheid des Finanzamt Grieskirchen Wels  vom 29. Jänner 
2019 betreffend Wiederaufnahme § 303 BAO /  KSt 2010 Steuernummer 64-207/8107  zu 
Recht erkannt:  
I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 5**

```
Im Übrigen führte die Beschwerdeführerin aus, dass Finanzamt Grieskirchen Wels  selbst keinen 
Einfluss auf die Wettquoten habe.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Annemie Bott` (organisation)

- Missed: `Milan Händlein` (organisation)


```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Annemie Bott` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)

- Missed: `Milan Händlein` (organisation)


</details>

---

## `specific_org_roelfsen`

**F1:** 0.034 | **Precision:** 1.000 | **Recall:** 0.017  

**Format:** `regex`  
**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.017 | 0.034 | 7 | 7 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 7 | 0 | 365 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2**

```
Daraufhin wurde bei der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  das 
Jahr 2010 mit Bescheid vom 7.3.2016 wiederaufgenommen, ein neuer Feststellungsbescheid 
Gruppenmitglied erlassen und der Verlustvortrag um den strittigen Betrag (€ 665.812,12) 
erhöht.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3**

```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4**

```
Bei den aus der Houdek Maschinenbau 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Roelfsen Versicherung  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Roelfsen Versicherung).
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 5**

```
Kff. Sandra Khartchenko (FN ***) ist die Rechtsnachfolgerin der Roelfsen Versicherung.
```

| Prediction | Gold |
|------------|------|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

<details>
<summary>❌ Missed (4)</summary>

```
Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der 
Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des 
Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann, 
wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum 
Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.
```

- Missed: `FA Wien 1/23` (organisation)

- Missed: `Houdek Maschinenbau` (organisation)


```
Daraufhin wurde bei der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  das 
Jahr 2010 mit Bescheid vom 7.3.2016 wiederaufgenommen, ein neuer Feststellungsbescheid 
Gruppenmitglied erlassen und der Verlustvortrag um den strittigen Betrag (€ 665.812,12) 
erhöht.
```

- Missed: `Houdek Maschinenbau` (organisation)


```
Im Beschwerdeverfahren gegen den Körperschaftsteuerbescheid 2007 hat das 
Bundesfinanzgericht (BFG 27.1.2016, RV/5101064/2013) der Beschwerde stattgegeben und 
den Verlust der Roelfsen Versicherung  als partieller Rechtsnachfolger der Houdek Maschinenbau  von € -
2.966.376,17 auf € -3.632.188,28 erhöht.
```

- Missed: `Houdek Maschinenbau` (organisation)


```
Bei den aus der Houdek Maschinenbau 
stammenden Verlustvorträgen handelt es sich um Außergruppenverluste, sodass grundsätzlich 
nur eine Verrechnung mit positiven Einkünften der Roelfsen Versicherung  im Jahr 2010 möglich ist (vgl. 
E-Mail des steuerlichen Vertreters vom 04.02.2016 betreffend steuerlicher Auswirkung des 
BFG- Erkenntnisses vom 27.01.2016, GZ RV/5101064/2013 auf das Jahr 2010 bei der 
Roelfsen Versicherung).
```

- Missed: `Houdek Maschinenbau` (organisation)


</details>

---

## `specific_org_bezirksgericht`

**F1:** 0.029 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `regex`  
**Content:**
```
\bBezirksgericht\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.015 | 0.029 | 6 | 6 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 6 | 0 | 382 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Dies würde der 
Berechnungsmethode des BG Bezirksgericht Silz  entsprechen, das sowohl auf Seiten des 
Unterhaltsbedarfes wie auch auf Seiten des geleisteten Unterhalts eine Berechnung über den 
gesamten Zeitraum (Juni 2017 bis Februar 2023) angestellt hat.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 2**

```
Ich habe inzwischen auch noch 
einen letztinstanzlichen Beschluss des LG Innsbruck, der den bereits 2 x vorgelegten Beschluss des 
Bezirksgerichtes Bezirksgericht Silz  vom 16.03.2023 bestätigt: Es liegt gerichtlich geprüft keinerlei 
Unterhaltsverletzung vor!
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 3**

```
Die Summe 
entspricht jener, die auch das BG Bezirksgericht Silz  errechnet hat.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 4**

```
Das Geburtsdatum der minderjährigen Tochter sowie die Feststellung, dass gegenüber dem 
Beschwerdeführer kein Unterhaltstitel besteht, ergibt sich aus dem Beschluss des BG 
Bezirksgericht Silz  vom 03.02.2023 bzw. dem Vorbringen des Beschwerdeführers.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 5**

```
Mit Eingabe vom 24.04.2023 wurde seitens des Beschwerdeführers im Wesentlichen 
ausgeführt, dass im fraglichen Beschluss des BG Bezirksgericht Silz  kein Unterhaltsanspruch von 
EUR 320,00 festgestellt worden sei.
```

| Prediction | Gold |
|------------|------|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Ich habe inzwischen auch noch 
einen letztinstanzlichen Beschluss des LG Innsbruck, der den bereits 2 x vorgelegten Beschluss des 
Bezirksgerichtes Bezirksgericht Silz  vom 16.03.2023 bestätigt: Es liegt gerichtlich geprüft keinerlei 
Unterhaltsverletzung vor!
```

- Missed: `LG Innsbruck` (organisation)


</details>

---

## `specific_org_unterrecycling`

**F1:** 0.029 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `regex`  
**Content:**
```
\bUnterRecycling\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.015 | 0.029 | 6 | 6 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 6 | 0 | 296 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Die UnterRecycling Services GMBH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen 
Berufenen, Herrn Valentina Riehmers, verhängten Geldstrafen von 5 x je € 510,00 und 2 x je € 520,00 
und die Verfahrenskosten in der Höhe von € 359,00 sowie für sonstige in Geld bemessene 
Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.
```

| Prediction | Gold |
|------------|------|
| `UnterRecycling Services GMBH` | `UnterRecycling Services GMBH` |

**Example 2**

```
3. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im Juli 2020 vor 
der Liegenschaft in Rodelsbach 3, 4800 Lehen, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen 
Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür 
bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe 
entrichtet habe.
```

| Prediction | Gold |
|------------|------|
| `UnterRecycling Services GMBH` | `UnterRecycling Services GMBH` |

**Example 3**

```
4. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im Juli 2020 vor 
der Liegenschaft in Felleishof 4, 9556 Lebmach, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen 
Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein Gerüst im 
Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er hiefür bis zum 
12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet 
3 von 11
Seite 4 von 11
```

| Prediction | Gold |
|------------|------|
| `UnterRecycling Services GMBH` | `UnterRecycling Services GMBH` |

**Example 4**

```
Entscheidungsgründe 
I. Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen 
vom 3. Februar 2022, GZ. MA6/206000003074/2020, wurde Valentina Riehmers (in weiterer Folge: 
Beschuldigter) für schuldig befunden,  
1. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im April 2020 vor 
der Liegenschaft in Felleishof 4, 9556 Lebmach, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen 
Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein Gerüst im 
Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er hiefür bis zum 
12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet 
habe.
```

| Prediction | Gold |
|------------|------|
| `UnterRecycling Services GMBH` | `UnterRecycling Services GMBH` |

**Example 5**

```
V. Gemäß § 9 Abs. 7 VStG haftet die UnterRecycling Services GMBH  über die nunmehr verhängten 
Geldstrafen, sonstige in Geld bemessene Unrechtsfolgen und die Verfahrenskosten zur 
ungeteilten Hand.
```

| Prediction | Gold |
|------------|------|
| `UnterRecycling Services GMBH` | `UnterRecycling Services GMBH` |

</details>

---

## `specific_org_pastl`

**F1:** 0.029 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `regex`  
**Content:**
```
\bPastl\+B\xe4chle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.015 | 0.029 | 6 | 6 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 6 | 0 | 374 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Gemäß dem § 185 Abs. 1 lit. a FinStrG hat die Firma Pastl+Bächle Handel  die Kosten des Verfahrens in 
Höhe von € 500,-- zu ersetzen.
```

| Prediction | Gold |
|------------|------|
| `Pastl+Bächle Handel` | `Pastl+Bächle Handel` |

**Example 2**

```
Zu den Oldtimern und Garagierungskosten halten wir fest, dass auf Grund des 
Firmenwortlautes (Pastl+Bächle Handel = Besitz/Vermögen), der aufrechten Gewerbeberechtigung und 
des Unternehmensgegenstandes u.a. auch der Handel mit Fahrzeugen beabsichtigt war.
```

| Prediction | Gold |
|------------|------|
| `Pastl+Bächle Handel` | `Pastl+Bächle Handel` |

**Example 3**

```
Festgestellt wird, dass ebenfalls die bereits bei 
der Firma Pastl+Bächle Handel  angeführten nicht abzugsfähigen Ausgaben, wie PA-PKW, ÖBB-
Reisegutscheine, Fachliteratur, Reisespesen, sonstige Gebühren und Abgaben und auch 
Werbeaufwand, für die Jahre 2013 und 2014 unrichtiger Weise gewinnmindernd behandelt 
wurden.
```

| Prediction | Gold |
|------------|------|
| `Pastl+Bächle Handel` | `Pastl+Bächle Handel` |

**Example 4**

```
Die ursprüngliche B GmbH wurde 1993 gegründet und 2013 in Pastl+Bächle Handel  umbenannt.
```

| Prediction | Gold |
|------------|------|
| `Pastl+Bächle Handel` | `Pastl+Bächle Handel` |

**Example 5**

```
Mit o.a. Erkenntnis wurde der belangte Verband Pastl+Bächle Handel  gemäß § 34 Abs 1 FinStrG mit einer 
Geldstrafe von EUR 7.000,00 zzgl. Kostenersatz von EUR 500,00 bestraft.
```

| Prediction | Gold |
|------------|------|
| `Pastl+Bächle Handel` | `Pastl+Bächle Handel` |

</details>

---

## `specific_org_annemie_bott`

**F1:** 0.024 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Content:**
```
\bAnnemie\s+Bott\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.012 | 0.024 | 5 | 5 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 0 | 377 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 2**

```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 3**

```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 4**

```
64-207/8107, BV 24 : 
Beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott  gab es betreffend dem 
Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid 
Gruppenmitglied: 
21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010 
27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid 
Gruppenmitglied 2010 nach Betriebsprüfung  
27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 
20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010 
(Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung 
Rekultivierungskosten) 
19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt 
Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung 
Rekultivierungskosten) 
29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW) 
16.12.2013 Vorlage an BFG (damals noch UFS) 
17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete 
Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW) 
Betreffend des Rechtsvorgängers Milan Händlein  wurde das Erkenntnis des 
Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum 
Veranlagungsjahr 2007 erlassen.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

**Example 5**

```
zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom 
19.08.2009 eine Abspaltung zur Aufnahme in die Annemie Bott  durch Übertragung des 
gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und 
Übernahmsvertrages taxativ angeführten Positionen) erfolgt.
```

| Prediction | Gold |
|------------|------|
| `Annemie Bott` | `Annemie Bott` |

</details>

<details>
<summary>❌ Missed (4)</summary>

```
Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Grieskirchen Wels  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott 
hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO 
wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da 
11 von 39
Seite 12 von 39
```

- Missed: `FA Grieskirchen Wels` (organisation)


```
Begründend 
wurde deshalb durch das Finanzamt Grieskirchen Wels  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ 
RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Annemie Bott  als RNF der 
Milan Händlein  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR 
1.047.673,40 ergibt.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Milan Händlein` (organisation)


```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Krolitzki Beratung` (organisation)

- Missed: `Milan Händlein` (organisation)


```
64-207/8107, BV 24 : 
Beim gegenständlichen partiellen Rechtsnachfolger Annemie Bott  gab es betreffend dem 
Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid 
Gruppenmitglied: 
21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010 
27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid 
Gruppenmitglied 2010 nach Betriebsprüfung  
27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 
20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010 
(Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung 
Rekultivierungskosten) 
19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt 
Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung 
Rekultivierungskosten) 
29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW) 
16.12.2013 Vorlage an BFG (damals noch UFS) 
17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete 
Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW) 
Betreffend des Rechtsvorgängers Milan Händlein  wurde das Erkenntnis des 
Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum 
Veranlagungsjahr 2007 erlassen.
```

- Missed: `Milan Händlein` (organisation)


</details>

---

## `specific_org_fa_deutschlandsberg`

**F1:** 0.024 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Content:**
```
\bFA\s+Deutschlandsberg\s+Leibnitz\s+Voitsberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.012 | 0.024 | 5 | 5 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 0 | 330 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Das Finanzamt legte die Beschwerde am 11.8.2021 dem 
Bundesfinanzgericht vor und ergänzte sein Vorbringen am 17.6.2021 dahin, „dass seitens des 
FA Deutschlandsberg Leibnitz Voitsberg … im gegenständlichen Beschwerdefall weder das Bestehen eines 
Familienbeihilfenanspruches in Österreich dem Grunde nach für T, geboren am x.x.2008 
bestritten wird noch sonstige Einwände gegen die beantragte Berücksichtigung des 
Familienbonus Plus beim Beschwerdeführer bestehen.“
```

| Prediction | Gold |
|------------|------|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Manuela Dietmannsberger  in der Beschwerdesache Valerian Goerlitz, 
Rechbergerstraße 12, 2604 Eggendorf, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die 
Beschwerde vom 17. April 2019 gegen die Bescheide des FA Deutschlandsberg Leibnitz Voitsberg  vom 11. März 2019  
1) über die Festsetzung eines zweiten Säumniszuschlages in Höhe von 87,69 € und 
2) über die Festsetzung eines dritten Säumniszuschlages in Höhe von 87,68 € 
Steuernummer 87-782/3154  zu Recht erkannt:  
Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Priv.-Doz.in Dr.in Pamela Gscheidt  in der Beschwerdesache der 
Kudla&Kühnel Solar, Josef-Schlesinger-Straße 22, 9330 Rabenstein, Österreich, über die Beschwerde vom 6. August 2021 gegen den Bescheid des 
FA Deutschlandsberg Leibnitz Voitsberg  vom 5. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 
zu Steuernummer 49-615/4779  zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eugenia Theimer  in der Beschwerdesache OStR Engelbert Ennulat, 
Ehrendorfer Wald 8, 2625 Guntrams, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte 
GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 7. Februar 2024 
gegen den Bescheid des FA Deutschlandsberg Leibnitz Voitsberg  vom 10. Jänner 2024 betreffend Abweisung eines Antrages 
auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum 
01.12.2022 bis 30.06.2023, Steuernummer 46-323/9363, zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

**Example 5**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Dr. Kevin Griepekoven  in der Beschwerdesache Moritz Danielek, 
Ulricusstraße 7, 6951 Lingenau, Österreich, über die Beschwerde vom 15. Jänner 2015 gegen die Bescheides des 
Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: FA Deutschlandsberg Leibnitz Voitsberg), jeweils  vom 11. Dezember 
2014 betreffend  
 Säumniszuschlag im Zusammenhang mit Lohnsteuer 2007; 
 Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2007; 
 Säumniszuschlag im Zusammenhang mit Lohnsteuer 2008; 
 Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2008; 
 Säumniszuschlag im Zusammenhang mit Lohnsteuer 2009; 
 Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2009; 
 Säumniszuschlag im Zusammenhang mit Lohnsteuer 2010, 
jeweils zur Steuernummer 84-350/7355  zu Recht erkannt:  
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Priv.-Doz.in Dr.in Pamela Gscheidt  in der Beschwerdesache der 
Kudla&Kühnel Solar, Josef-Schlesinger-Straße 22, 9330 Rabenstein, Österreich, über die Beschwerde vom 6. August 2021 gegen den Bescheid des 
FA Deutschlandsberg Leibnitz Voitsberg  vom 5. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 
zu Steuernummer 49-615/4779  zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- Missed: `Kudla&Kühnel Solar` (organisation)


</details>

---

## `specific_org_fa_waldviertel`

**F1:** 0.024 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Content:**
```
\bFA\s+Waldviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.012 | 0.024 | 5 | 5 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 0 | 353 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Nicht im Gemeinschaftsgebiet ansässige Unternehmer haben die Vorsteuererstattung laut § 3a 
der Erstattungsverordnung BGBl 279/1995 in der jeweiligen Fassung mittels amtlich 
vorgeschriebenen Vordruckes beim FA Waldviertel  zu beantragen.
```

| Prediction | Gold |
|------------|------|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Gertrude Schonefeld  in der Beschwerdesache des 
Fabienne Stegerwald, Almmeisterweg 31, 4212 Traidendorf, Österreich, über die Beschwerde vom 2.März 2023, eingebracht am 6. März 
2023, gegen den Bescheid des FA Waldviertel  vom 7. März 2023 betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2022 zur Steuernummer 51-026/1591  zu Recht erkannt:  
I. Der angefochtene Bescheid wird abgeändert.
```

| Prediction | Gold |
|------------|------|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag.a Anita Müller  in der Beschwerdesache des 
Siegbert Koeberer, Obermayrstraße 19, 5270 Mauerkirchen, Österreich, vertreten durch Rechtsanwälte, über die Beschwerde vom 
31.8.2015 gegen den Haftungsbescheid des FA Waldviertel  vom 29.7.2015 zu Recht erkannt:  
I. Der Beschwerde wird teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 4**

```
IM NAMEN DER REPUBLIK  
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Isolde Bölster  in der Beschwerdesache 
Larissa Eisenacker, Bakk. techn., Dietenmühle 3, 6723 Blons, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH 
Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  
über die Beschwerden vom 8. Mai 2015 gegen die Bescheide des Finanzamt Waldviertel  vom 2. April 2015, 
betreffend Wiederaufnahme des Verfahrens zur Vorsteuererstattung 2009, 2010 und 2011 
sowie die Bescheide des Finanzamt Waldviertel  vom 2. April 2015 betreffend Vorsteuererstattung 2009, 
2010, 2011, 2012 und 2013, die Beschwerde vom 9. September 2015 gegen den Bescheid des 
FA Waldviertel  vom 11. August 2015, betreffend Vorsteuererstattung 2014 und die Beschwerde 
vom 7. September 2016 gegen den Bescheid des FA Waldviertel  vom 6. Juli 2016, betreffend 
Vorsteuererstattung 2015 nach Durchführung einer mündlichen Verhandlung am 4. April 2022 
zu Recht erkannt:  
I. Die Bescheide vom 2. April 2015 betreffend Wiederaufnahme des Verfahrens zur 
Vorsteuererstattung 2009, 2010 und 2011 werden - ersatzlos - aufgehoben.
```

| Prediction | Gold |
|------------|------|
| `FA Waldviertel` | `FA Waldviertel` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
IM NAMEN DER REPUBLIK  
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Isolde Bölster  in der Beschwerdesache 
Larissa Eisenacker, Bakk. techn., Dietenmühle 3, 6723 Blons, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH 
Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  
über die Beschwerden vom 8. Mai 2015 gegen die Bescheide des Finanzamt Waldviertel  vom 2. April 2015, 
betreffend Wiederaufnahme des Verfahrens zur Vorsteuererstattung 2009, 2010 und 2011 
sowie die Bescheide des Finanzamt Waldviertel  vom 2. April 2015 betreffend Vorsteuererstattung 2009, 
2010, 2011, 2012 und 2013, die Beschwerde vom 9. September 2015 gegen den Bescheid des 
FA Waldviertel  vom 11. August 2015, betreffend Vorsteuererstattung 2014 und die Beschwerde 
vom 7. September 2016 gegen den Bescheid des FA Waldviertel  vom 6. Juli 2016, betreffend 
Vorsteuererstattung 2015 nach Durchführung einer mündlichen Verhandlung am 4. April 2022 
zu Recht erkannt:  
I. Die Bescheide vom 2. April 2015 betreffend Wiederaufnahme des Verfahrens zur 
Vorsteuererstattung 2009, 2010 und 2011 werden - ersatzlos - aufgehoben.
```

- Missed: `Finanzamt Waldviertel` (organisation)

- Missed: `Finanzamt Waldviertel` (organisation)


</details>

---

## `specific_org_kraftver`

**F1:** 0.024 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Content:**
```
\bKraftver-Gastronomie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.012 | 0.024 | 5 | 5 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 0 | 382 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

| Prediction | Gold |
|------------|------|
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 2**

```
BESCHLUSS 
Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Priv.-Doz. Samir Bierdimpfl  in der Beschwerdesache Kraftver-Gastronomie GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, über den Vorlageantrag der Gartgart Dienstleistungen GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, vom 
18.9.2020 gegen die an die Kraftver-Gastronomie GMBH  ergangene Beschwerdevorentscheidung des 
Finanzamts Graz-Stadt vom 9.9.2020 betreffend Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO beschlossen: 
I. Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig 
zurückgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 3**

```
In den Akten finden sich überdies keinerlei Hinweise darauf, 
dass ein Vorlageantrag unter der FinanzOnline-Teilnehmeridentifikation der Kraftver-Gastronomie GMBH 
gestellt worden wäre.
```

| Prediction | Gold |
|------------|------|
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

**Example 4**

```
Begründung 
1. Verfahrensgang/festgestellter Sachverhalt: 
Mit Erinnerungsschreiben vom 11.1.2020 forderte das Finanzamt die Kraftver-Gastronomie GMBH  dazu auf, 
die Meldung der wirtschaftlichen Eigentümer gemäß § 5 WiEReG bis spätestens 21.4.2020 
nachzuholen.
```

| Prediction | Gold |
|------------|------|
| `Kraftver-Gastronomie GMBH` | `Kraftver-Gastronomie GMBH` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

- Missed: `Gartgart Dienstleistungen GMBH` (organisation)


```
BESCHLUSS 
Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Priv.-Doz. Samir Bierdimpfl  in der Beschwerdesache Kraftver-Gastronomie GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, über den Vorlageantrag der Gartgart Dienstleistungen GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, vom 
18.9.2020 gegen die an die Kraftver-Gastronomie GMBH  ergangene Beschwerdevorentscheidung des 
Finanzamts Graz-Stadt vom 9.9.2020 betreffend Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO beschlossen: 
I. Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig 
zurückgewiesen.
```

- Missed: `Gartgart Dienstleistungen GMBH` (organisation)


</details>

---

## `company_kg_general`

**F1:** 0.022 | **Precision:** 0.122 | **Recall:** 0.012  

**Format:** `regex`  
**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)+\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.122 | 0.012 | 0.022 | 41 | 5 | 36 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 5 | 36 | 400 |

</details>

<details>
<summary>✅ Worked (5)</summary>

**Example 1**

```
Im Feststellungsverfahren der (damaligen) Schoenfelder Textil KG  wurde am 23. Oktober 2006 ein 
Feststellungsbescheid erlassen, fand im Jahr 2015 eine Betriebsprüfung statt und wurde am 18. 
Dezember 2015 das Feststellunsgsverfahren 2005 wiederaufgenommen und ein neuer 
Feststellungsbescheid erlassen.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

**Example 2**

```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

**Example 3**

```
Mit Erkenntnis vom 27. August 2024 gab das Bundesfinanzgericht ua. der Beschwerde gegen 
den Bescheid betreffend Wiederaufnahme des Feststellungsverfahren 2005 betreffend 
Schoenfelder Textil KG  statt und hob den Wiederaufnahmebescheid auf, da laut Mitteilung an das 
Bundesfinanzgericht vom Finanzamt neu angestellte Prognoserechungen ergeben hätten, dass 
die Rendite nach Steuern nicht doppelt so hoch wie vor Steuern liegen würde und somit kein 
Anwendungsfall des § 2 Abs. 2a EStG vorliege.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

**Example 4**

```
Die Beschwerde wendet sich somit mit Argumenten gegen den Einkommensteuerbescheid, die 
gegen den Bescheid über die Feststellung von Einkünften der WOD Sicherheit KG  gem. § 188 BAO vom 
20.1.2020 zu richten gewesen wären.
```

| Prediction | Gold |
|------------|------|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

**Example 5**

```
Im Feststellungsverfahren 2005 der Schoenfelder Textil KG  ergingen folgende Bescheide: 
23. Oktober 2006 Erlassung des Feststellungsbescheides 
18. Dezember 2015 Bescheid über die Wiederaufnahme des Feststellungsverfahrens 
   betreffend 2005 
18. Dezember 2015 Erlassung des neuen Feststellungebescheides 
27. August 2024 Erkenntnis des BFG, mit welchem der Beschwerde gegen die  
   Wiederaufnahme stattgegeben wird 
27. August 2024 Beschluss des BFG, mit welchem die Beschwerde gegen den  
   Feststellungsbescheid gegenstandslos erklärt wird.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

</details>

<details>
<summary>❌ Missed (5)</summary>

```
Mit Ablauf des Stichtages 31. 
März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit 
Buchwertfortführung gem. Art IV UmgrStG. 
 Leiss Software  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober 2008 
gegründet.
```

- Missed: `Leiss Software` (organisation)


```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Süd Nortri  GmbH & Co KG 
und Hülsebusch + Breithaupt Versicherung  GmbH & Co KG angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung 
einer Beschwerde befugt ist, an den der den Gegenstand der Anfechtung bildende Bescheid 
ergangen ist.
```

- Missed: `Süd Nortri` (organisation)

- Missed: `Hülsebusch + Breithaupt Versicherung` (organisation)


```
Mit Ablauf des Stichtages 30. September 2008 erfolgte rückwirkend ein 
Verkehrswertzusammenschluss mit Buchwertfortführung gem. Art IV UmgrStG. 
 Okur Automotive  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 15. April 2009 
gegründet.
```

- Missed: `Okur Automotive` (organisation)


```
Celikkanat Garten  GmbH & Co KG: 
Aufstellung der Aufwendungen laut Gewinn und Verlustrechnung der Celikkanat Garten  GmbH & Co 
KG (atypisch stille Gesellschafterin) für das Jahr 2009: 
 € 
Initialisierungsaufwand 348,290,00 
Verkehrssteuern 24.030,00 
Lfd.
```

- Missed: `Celikkanat Garten` (organisation)

- Missed: `Celikkanat Garten` (organisation)


```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

- Missed: `Okur Automotive` (organisation)

- Missed: `Celikkanat Garten` (organisation)


</details>

<details>
<summary>⚠️ False Positives (5)</summary>

```
Mit Ablauf des Stichtages 31. 
März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit 
Buchwertfortführung gem. Art IV UmgrStG. 
 Leiss Software  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober 2008 
gegründet.
```

- FP: `Leiss Software  GmbH & Co KG` (organisation)


```
IM NAMEN DER REPUBLIK  
Das Bundesfinanzgericht hat durch den RichterM. in der Finanzstrafsache gegen Herrn 
Roland Sibbertsen, Reitenaustraße 4, 9500 Neufellach, Österreich, vertreten durch Schneider Rechtsanwalts KG, Rechte Bahnstraße 
10/19D, 1030 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung 
gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde der Beschuldigten 
vom 11. Dezember 2020 gegen den Zurückweisungsbescheid des Finanzamtes Wien 9/18/19 
Klosterneuburg als Finanzstrafbehörde vom 3. November 2020, Geschäftszahl FV-1, zu Recht 
erkannt: 
Die Beschwerde wird als unbegründet abgewiesen.
```

- FP: `Schneider Rechtsanwalts KG` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der 
Beschwerdesache Vera Lüerß, BA, Gewerbepark Hinterholz 3, 4974 Stött, Österreich, vertreten durch BKS Steuerberatung GmbH & Co 
KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, über die Beschwerde vom 
18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013 
betreffend Wiederaufnahme der Einkommensteuerverfahren 2003 bis 2010 sowie vom 
29.4.2013  betreffend Wiederaufnahme des Einkommensteuerverfahren 2011, Steuernummer 
***, zu Recht erkannt:  
Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

- FP: `BKS Steuerberatung GmbH & Co 
KG` (organisation)


```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der 
Beschwerdesache Ing. Miklos Novikova, Carl Lutz-Straße 44, 2225 Blumenthal, Österreich, vertreten durch BKS Steuerberatung GmbH & Co 
KG, Untere Hauptstraße 10, 3150 Wilhelmsburg, über die Beschwerde vom 14. Jänner 2019 
gegen den Haftungsbescheid des Finanzamtes Lilienfeld St. Pölten vom 17. Dezember 2018, 
Steuernummer 62-482/0330, Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

- FP: `BKS Steuerberatung GmbH & Co 
KG` (organisation)


```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Süd Nortri  GmbH & Co KG 
und Hülsebusch + Breithaupt Versicherung  GmbH & Co KG angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung 
einer Beschwerde befugt ist, an den der den Gegenstand der Anfechtung bildende Bescheid 
ergangen ist.
```

- FP: `Nortri  GmbH & Co KG` (organisation)

- FP: `Breithaupt Versicherung  GmbH & Co KG` (organisation)


</details>

---

## `specific_org_fa_gmunden`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Gmunden\s+V\xf6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.010 | 0.020 | 4 | 4 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 0 | 302 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Linn Pelzner  in der Beschwerdesache der 
Alal-Medien, Dichtlstraße 32, 4656 Windberg, Österreich  vertreten durch Vertreter-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999-99-999/9999 (M- GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt 
Dienststelle des Finanzamt Gmunden Vöcklabruck) vom 5. November 2019 betreffend Heranziehung als 
Gemeinschuldnerin für „Umsatzsteuerveranlagungen und div.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Gmunden Vöcklabruck` | `Finanzamt Gmunden Vöcklabruck` |

**Example 2**

```
Das Bundesfinanzgericht hat durch den Richter Mag. Aron Sperle  in der Angelegenheit der Parteien 
Gottfried Schwärzl (Beschwerdeführerin), vertreten durch Frau Mag. Martina Elsner, 9020 Klagenfurt 
und Finanzamt Österreich als Amtspartei und als Gesamtrechtsnachfolger des Finanzamt Gmunden Vöcklabruck  über 
die Beschwerde vom 1.2.2020 gegen den Bescheid des Finanzamtes vom 27.1.2020 betreffend 
Abweisung des Antrages vom 4.10.2019 auf Aufhebung des Einkommensteuerbescheides 2018 
vom 10.7.2019 und über die Beschwerde vom 8.5.2020 gegen die Beschwerdevorentscheidung 
vom 26.3.2020 
beschlossen: 
Die Beschwerde vom 8.5.2020 gegen die Beschwerdevorentscheidung vom 26.3.2020 wird 
zurückgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Gmunden Vöcklabruck` | `Finanzamt Gmunden Vöcklabruck` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alexandra Halbmeyer  in der Beschwerdesache des 
Dragan Cayci, Ronklerbrunnen 5, 3860 Haslau, Österreich, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des 
Finanzamt Gmunden Vöcklabruck  vom 11. Jänner 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 
2017 zu Recht erkannt:  
 
Die Beschwerde wird als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Gmunden Vöcklabruck` | `Finanzamt Gmunden Vöcklabruck` |

**Example 4**

```
Die Ehefrau des BF hat laut Feststellungen des Finanzamt Gmunden Vöcklabruck  im Kalenderjahr 2022 ganzjährig 
Familienbeihilfe für die genannten Kinder bezogen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Gmunden Vöcklabruck` | `Finanzamt Gmunden Vöcklabruck` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Linn Pelzner  in der Beschwerdesache der 
Alal-Medien, Dichtlstraße 32, 4656 Windberg, Österreich  vertreten durch Vertreter-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999-99-999/9999 (M- GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt 
Dienststelle des Finanzamt Gmunden Vöcklabruck) vom 5. November 2019 betreffend Heranziehung als 
Gemeinschuldnerin für „Umsatzsteuerveranlagungen und div.
```

- Missed: `Alal-Medien` (organisation)


</details>

---

## `specific_org_okur`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Content:**
```
\bOkur\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.010 | 0.020 | 4 | 4 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 0 | 357 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Mit Ablauf des Stichtages 30. September 2008 erfolgte rückwirkend ein 
Verkehrswertzusammenschluss mit Buchwertfortführung gem. Art IV UmgrStG. 
 Okur Automotive  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 15. April 2009 
gegründet.
```

| Prediction | Gold |
|------------|------|
| `Okur Automotive` | `Okur Automotive` |

**Example 2**

```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

| Prediction | Gold |
|------------|------|
| `Okur Automotive` | `Okur Automotive` |

**Example 3**

```
Okur Automotive  GmbH & Co KG: 
Aufstellung der Aufwendungen laut Gewinn und Verlustrechnung der Okur Automotive  GmbH & Co 
KG (atypisch stille Gesellschafterin) für das Jahr 2009: 
 € 
Initialisierungsaufwand 870.000,00 
Verkehrssteuern 60.010,00 
Lfd.
```

| Prediction | Gold |
|------------|------|
| `Okur Automotive` | `Okur Automotive` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

- Missed: `Celikkanat Garten` (organisation)


</details>

---

## `specific_org_gartgart`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Content:**
```
\bGartgart\s+Dienstleistungen\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.010 | 0.020 | 4 | 4 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 0 | 383 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

**Example 2**

```
BESCHLUSS 
Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Priv.-Doz. Samir Bierdimpfl  in der Beschwerdesache Kraftver-Gastronomie GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, über den Vorlageantrag der Gartgart Dienstleistungen GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, vom 
18.9.2020 gegen die an die Kraftver-Gastronomie GMBH  ergangene Beschwerdevorentscheidung des 
Finanzamts Graz-Stadt vom 9.9.2020 betreffend Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO beschlossen: 
I. Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig 
zurückgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

**Example 3**

```
Denn der Vorlageantrag wurde über FinanzOnline unter der FinanzOnline-
Teilnehmeridentifikation der Gartgart Dienstleistungen GMBH  eingebracht.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

**Example 4**

```
Und dies trifft im 
vorliegenden Fall eben auf die Gartgart Dienstleistungen GMBH  zu.
```

| Prediction | Gold |
|------------|------|
| `Gartgart Dienstleistungen GMBH` | `Gartgart Dienstleistungen GMBH` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Weder in der 
FinanzOnline-Eingabe selbst noch in dem der FinanzOnline-Eingabe angefügten Schreiben 
finden sich Hinweise darauf, dass die Gartgart Dienstleistungen GMBH  den Vorlageantrag im Namen der Kraftver-Gastronomie GMBH  gestellt hätte.
```

- Missed: `Kraftver-Gastronomie GMBH` (organisation)


```
BESCHLUSS 
Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Priv.-Doz. Samir Bierdimpfl  in der Beschwerdesache Kraftver-Gastronomie GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, über den Vorlageantrag der Gartgart Dienstleistungen GMBH, Neurieder Gasse 61, 4144 Dittmannsdorf, Österreich, vom 
18.9.2020 gegen die an die Kraftver-Gastronomie GMBH  ergangene Beschwerdevorentscheidung des 
Finanzamts Graz-Stadt vom 9.9.2020 betreffend Zwangsstrafe gemäß § 16 WiEReG iVm § 111 
BAO beschlossen: 
I. Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig 
zurückgewiesen.
```

- Missed: `Kraftver-Gastronomie GMBH` (organisation)

- Missed: `Kraftver-Gastronomie GMBH` (organisation)


</details>

---

## `tax_office_fa_graz_stadt`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Content:**
```
\bFA\s+Graz-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.010 | 0.020 | 4 | 4 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 0 | 291 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Das Bundesfinanzgericht beschließt durch den Richter Mag. Benedikt Volge  in der Beschwerdesache 
Karlheinz Bremmenkamp, Hoferfeldweg 2, 9300 Steinbrücken, Österreich, vertreten durch Rechtsanwalt Ing. Mag. Hamza Ovacin, Stadtstraße 
33, 6850 Dornbirn betreffend Beschwerde vom 18. Februar 2022 gegen die Bescheide des 
FA Graz-Stadt  vom 14. Dezember 2021 betreffend Körperschaftsteuer 2016, Körperschaftsteuer 
2017, Körperschaftsteuer 2018, Körperschaftsteuer 2019, Umsatzsteuer 2017, Umsatzsteuer 
2018 und Umsatzsteuer 2019, Steuernummer 53-335/9713 : 
I. Der Vorlageantrag wird gem § 278 Abs 1 lit a BAO iVm § 264 Abs 4 lit e BAO als unzulässig 
zurückgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Rut Eschenröder  in der Beschwerdesache Jean Mavros, 
Inning Betriebsgebiet I 11, 9100 Ratschitschach, Österreich, über die Beschwerde vom 23. Juni 2019 gegen die Bescheide des FA Graz-Stadt 
vom 23. Mai 2019 bzw. 19.08.2019 betreffend Umsatz- und Einkommensteuer 2017, 
Anspruchszinsen (§ 205 BAO) 2017, Verspätungszuschlag 2017 sowie Einkommensteuer-
Vorauszahlungen 2019, Steuernummer 77-563/3206, 
I. zu Recht erkannt: 
1.
```

| Prediction | Gold |
|------------|------|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 3**

```
Aus einer 
vorgelegten Rechnung vom 26.8.2010 geht hervor, dass die FA Graz-Stadt  eine Wartung des 
Treppenlifts zu einem Gesamtbetrag von 260,40 Euro durchgeführt hat.
```

| Prediction | Gold |
|------------|------|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 4**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait, 
St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des 
FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an 
Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum 
November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

</details>

---

## `specific_org_raiffeisen_hyphen`

**F1:** 0.019 | **Precision:** 0.667 | **Recall:** 0.010  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+[A-Z][a-zA-Z]+(?:\s+-\s+[A-Z][a-zA-Z]+|\s+[A-Z][a-zA-Z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.667 | 0.010 | 0.019 | 6 | 4 | 2 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 4 | 2 | 315 |

</details>

<details>
<summary>✅ Worked (4)</summary>

**Example 1**

```
Am 27.12.2022 bezahlte die Raiffeisenbank Wienerwald  den Betrag von € 28.423,94 zuzüglich der 
gegenständlichen Pfändungsgebühr und Barauslagen (insg. sohin € 28.721,13) an die belangte 
Behörde, welche sodann die beiden anderen Forderungspfändungen einstellte.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 2**

```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Mittleres Mostviertel` | `Raiffeisenbank Mittleres Mostviertel` |

**Example 3**

```
Hierauf übermittelte der Beschwerdeführer ein Schreiben der Raiffeisenbank Stallhofen  vom 
24.2.2014, in welchem bestätigt wurde, dass er im Jahre 2013 € 4.377,00 an Kreditrückzahlung 
geleistet hat.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Stallhofen` | `Raiffeisenbank Stallhofen` |

**Example 4**

```
Darüber hinaus habe die belangte 
Behörde das Konto des Beschwerdeführers vor Weihnachten unrechtmäßig um den Betrag 
vom € 28.423,94 „ausgeplündert“ und zudem auf zwei Konten gleichzeitig zugegriffen, obwohl 
eines dieser Konten zwei Personen gemeinsam gehört und der Zugriff auf das andere Konto 
(bei der Raiffeisenbank Wienerwald) ausgereicht hätte, um die Forderung vollständig zu befriedigen.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

</details>

<details>
<summary>❌ Missed (3)</summary>

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Mit Bescheid des Zollamtes Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der Raiffeisenbank Wels Süd  mitgeteilt, dass der Bf Abgaben einschließlich Nebengebühren in Höhe von 
€ 63.917,32 schuldet.
```

- Missed: `Raiffeisenbank Wels Süd` (organisation)


```
Wegen eines Teilbetrages in Höhe von € 10.000,00 wurde die dem Bf 
gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem bezeichneten Girokonto zustehende 
Forderung gepfändet.
```

- Missed: `Raiffeisenbank Wels Süd` (organisation)


```
Dazu ist auch noch zu berücksichtigen, dass die gesamte Bezahlung, obwohl auf allen vom Bf 
über diesen Kaufvertrag erstellten Rechnungen ausschließlich eine Kontonummer bei der 
Niederösterreichische Vorsorgekasse  angegeben war, über das Treuhandkonto des Bf bei der Raiffeisenbank Mittleres Mostviertel  erfolgt ist, 
die Rückzahlung durch eine für derartige Maßnahmen wohl mehr als unüblichen Barabhebung 
erfolgt sein soll.
```

- Missed: `Niederösterreichische Vorsorgekasse` (organisation)


</details>

<details>
<summary>⚠️ False Positives (2)</summary>

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Mit Bescheid des Zollamtes Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der Raiffeisenbank Wels Süd  mitgeteilt, dass der Bf Abgaben einschließlich Nebengebühren in Höhe von 
€ 63.917,32 schuldet.
```

- FP: `Raiffeisenbank Wels` (organisation)


```
Wegen eines Teilbetrages in Höhe von € 10.000,00 wurde die dem Bf 
gegen die Raiffeisenbank Wels Süd  wegen des Guthabens auf einem bezeichneten Girokonto zustehende 
Forderung gepfändet.
```

- FP: `Raiffeisenbank Wels` (organisation)


</details>

---

## `specific_org_klusner`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bKlusner&P\xe4ffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 401 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Vor dieser Eintragung verfügte die Bf im 
beschwerdegegenständlichen Zeitraum über keinen Anteil an der Klusner&Päffgen Bildung GMBH.
```

| Prediction | Gold |
|------------|------|
| `Klusner&Päffgen Bildung GMBH` | `Klusner&Päffgen Bildung GMBH` |

**Example 2**

```
Mit Einbringungsakt vom 26.9.2017 abgeschlossen zwischen der Bf und der Privatstiftung 
erklärten die Parteien unter Punkt 1.1, dass die Privatstiftung einen Teil ihres Anteils an der 
Klusner&Päffgen Bildung GMBH, der einer zur Gänze einbezahlten Stammeinlage von ATS 765.000 bzw. 51% 
des gesamten Stammkapitals entspricht, zum Stichtag des 31.12.2016 in die Bf einbringt.
```

| Prediction | Gold |
|------------|------|
| `Klusner&Päffgen Bildung GMBH` | `Klusner&Päffgen Bildung GMBH` |

**Example 3**

```
Im Gegensatz zu einem 
nachträglichen Eintritt einer Körperschaft iSd § 9 Abs 9 TS 3 KStG wurde auch bereits ein 
Antrag auf die Aufnahme der Klusner&Päffgen Bildung GMBH  in die Gruppe gestellt (Antrag vom 12.10.2017).
```

| Prediction | Gold |
|------------|------|
| `Klusner&Päffgen Bildung GMBH` | `Klusner&Päffgen Bildung GMBH` |

</details>

---

## `specific_org_yxtg`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bYXTG\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 330 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Die Voraussetzungen zur Inanspruchnahme der 
steuerlichen Begünstigung werden von der YXTG Maschinenbau  erfüllt: 
• Die Stromerzeugung stellt den ausschließlichen Betriebsgegenstand des Unternehmens dar.
```

| Prediction | Gold |
|------------|------|
| `YXTG Maschinenbau` | `YXTG Maschinenbau` |

**Example 2**

```
Die 
Stadtwerke X verpflichten sich, die von der YXTG Maschinenbau  erzeugte und in das öffentliche Netz 
eingespeiste elektrische Energie im gelieferten Umfang zur vereinbarten Vergütung 
abzunehmen.
```

| Prediction | Gold |
|------------|------|
| `YXTG Maschinenbau` | `YXTG Maschinenbau` |

**Example 3**

```
Der „Rahmenvertrag betreffend die gemeinsame Errichtung und des Betriebes des 
Wasserkatfwerks Y“ vom 26.8.2013 wurde zwischen der Gemeinde Y, der Stadtgemeinde X, 
der A GmbH, der A Privatstiftung und der YXTG Maschinenbau  abgeschlossen.
```

| Prediction | Gold |
|------------|------|
| `YXTG Maschinenbau` | `YXTG Maschinenbau` |

</details>

---

## `specific_org_nowothnig`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bNowothnig\s+Wind\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 239 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Die Firma 
Nowothnig Wind  trägt zum gemeinsamen Projekt durch die Errichtung der geplanten Wohnanlage 
bei.
```

| Prediction | Gold |
|------------|------|
| `Nowothnig Wind` | `Nowothnig Wind` |

**Example 2**

```
Aus den jeweiligen Verkaufserlösen soll zunächst Herr A den Grundanteil im Ausmaß von 
Euro 6.650,- pro Quadratmeter vom Käufer erhalten, der Rest des Verkaufserlöses wird der 
Nowothnig Wind  zur Abdeckung der Baukosten zur Verfügung gestellt werden.
```

| Prediction | Gold |
|------------|------|
| `Nowothnig Wind` | `Nowothnig Wind` |

**Example 3**

```
Aus den 
Errichtungskosten der Gebäude wurden von der Firma Nowothnig Wind  Vorsteuern geltend gemacht.
```

| Prediction | Gold |
|------------|------|
| `Nowothnig Wind` | `Nowothnig Wind` |

</details>

---

## `specific_org_reinemut`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bReinemut\s+\+\s+Smoch\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 244 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Kostenentscheidung 
Die Verfahrenskosten in Höhe von € 500,00 für den Beschuldigten und € 350,00 für den 
belangten Verband Reinemut + Smoch Handel  gründen sich auf § 185 Abs. 1 lit. a FinStrG, wonach pauschal ein 
Kostenersatz im Ausmaß von 10% der verhängten Geldstrafe, maximal aber ein Betrag von 
€ 500,00 festzusetzen ist.
```

| Prediction | Gold |
|------------|------|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 2**

```
Aus diesem Schreiben ergibt sich, dass „im Namen und im Auftrag unserer oben genannten 
Mandantschaft“, nämlich der Reinemut + Smoch Handel, lediglich Informationen über nicht gemeldete 
Umsatzsteuervoranmeldungen für die Zeiträume 01/2021-09/2022 an das Finanzamt berichtet 
wurden.
```

| Prediction | Gold |
|------------|------|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 3**

```
Am 18.7.2023 wurde gegen OSR Jan Passerschroer, MA  und gegen die Firma Reinemut + Smoch Handel  eine Strafverfügung 
erlassen.
```

| Prediction | Gold |
|------------|------|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

</details>

---

## `specific_org_pastel`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bPastel\s+Pharma\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 85 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Laut Appendix A dieser 
Unterlage ist eine vorläufige Lizenz auch der Pastel Pharma  Austria unter den Internetmarken 
(Internet-Plattformen) www.xx.com und www.1x1.gr für Sport-, Casino- und Pokerprodukte 
erteilt worden.
```

| Prediction | Gold |
|------------|------|
| `Pastel Pharma` | `Pastel Pharma` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die 
Bescheidbeschwerde vom 12.10.2017 der Pastel Pharma, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra 
GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des 
Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF-
010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf 
Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,  
zu Recht erkannt: 
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Pastel Pharma` | `Pastel Pharma` |

**Example 3**

```
Aus den auf der Internetplatform von www.goalbetint.com ausgewiesenen Wettbedingungen 
(insb. Punkt 36 und 39) ergibt sich, dass die abgeschlossenen Wettvereinbarungen dem 
Gesetzen von Curacao unterliegen und der Vertag zwischen der Pastel Pharma  Eood (mit Sitz in 
Bulgarien, Sofia) und dem Endkunden zustande kommt (Abfrage April 2017).
```

| Prediction | Gold |
|------------|------|
| `Pastel Pharma` | `Pastel Pharma` |

</details>

---

## `specific_org_krolitzki`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bKrolitzki\s+Beratung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 200 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
(Der Körperschaftsteuerbescheid 2007 des partiellen 
Gesamtrechtsnachfolgers Krolitzki Beratung  vom 26.04.2013, wo Einkünfte aus Gewerbebetrieb 
von € -665.812,12 festgesteilt wurden, erwuchs in Rechtskraft).
```

| Prediction | Gold |
|------------|------|
| `Krolitzki Beratung` | `Krolitzki Beratung` |

**Example 2**

```
Der Körperschaftsteuerbescheid 2007 des partiellen Rechtsnachfolgers Krolitzki Beratung  mit 
Einkünften aus Gewerbebetrieb in Höhe von € -665.812,12 erwuchs in Rechtskraft.
```

| Prediction | Gold |
|------------|------|
| `Krolitzki Beratung` | `Krolitzki Beratung` |

**Example 3**

```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Prediction | Gold |
|------------|------|
| `Krolitzki Beratung` | `Krolitzki Beratung` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Annemie Bott` (organisation)

- Missed: `Grönemeier&Hövelberndt E‑Commerce` (organisation)

- Missed: `Milan Händlein` (organisation)


</details>

---

## `specific_org_schoenfelder`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bSchoenfelder\s+Textil\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 376 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Im Feststellungsverfahren der (damaligen) Schoenfelder Textil KG  wurde am 23. Oktober 2006 ein 
Feststellungsbescheid erlassen, fand im Jahr 2015 eine Betriebsprüfung statt und wurde am 18. 
Dezember 2015 das Feststellunsgsverfahren 2005 wiederaufgenommen und ein neuer 
Feststellungsbescheid erlassen.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

**Example 2**

```
Mit Erkenntnis vom 27. August 2024 gab das Bundesfinanzgericht ua. der Beschwerde gegen 
den Bescheid betreffend Wiederaufnahme des Feststellungsverfahren 2005 betreffend 
Schoenfelder Textil KG  statt und hob den Wiederaufnahmebescheid auf, da laut Mitteilung an das 
Bundesfinanzgericht vom Finanzamt neu angestellte Prognoserechungen ergeben hätten, dass 
die Rendite nach Steuern nicht doppelt so hoch wie vor Steuern liegen würde und somit kein 
Anwendungsfall des § 2 Abs. 2a EStG vorliege.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

**Example 3**

```
Im Feststellungsverfahren 2005 der Schoenfelder Textil KG  ergingen folgende Bescheide: 
23. Oktober 2006 Erlassung des Feststellungsbescheides 
18. Dezember 2015 Bescheid über die Wiederaufnahme des Feststellungsverfahrens 
   betreffend 2005 
18. Dezember 2015 Erlassung des neuen Feststellungebescheides 
27. August 2024 Erkenntnis des BFG, mit welchem der Beschwerde gegen die  
   Wiederaufnahme stattgegeben wird 
27. August 2024 Beschluss des BFG, mit welchem die Beschwerde gegen den  
   Feststellungsbescheid gegenstandslos erklärt wird.
```

| Prediction | Gold |
|------------|------|
| `Schoenfelder Textil KG` | `Schoenfelder Textil KG` |

</details>

---

## `specific_org_event_sudkraftlex`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 224 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses 
Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein 
Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.
```

| Prediction | Gold |
|------------|------|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2**

```
Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer 
der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.
```

| Prediction | Gold |
|------------|------|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3**

```
Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im 
Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH 
bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der 
Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).
```

| Prediction | Gold |
|------------|------|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer 
der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.
```

- Missed: `KQPC Versand GMBH` (organisation)


```
Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im 
Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH 
bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der 
Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).
```

- Missed: `KQPC Versand GMBH` (organisation)


</details>

---

## `specific_org_kqpc`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 258 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Damit entfällt auch die 
Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.
```

| Prediction | Gold |
|------------|------|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2**

```
Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer 
der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.
```

| Prediction | Gold |
|------------|------|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3**

```
Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im 
Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH 
bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der 
Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).
```

| Prediction | Gold |
|------------|------|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer 
der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.
```

- Missed: `Event Sudkraftlex GMBH` (organisation)


```
Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im 
Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH 
bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der 
Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).
```

- Missed: `Event Sudkraftlex GMBH` (organisation)


</details>

---

## `specific_org_sanitar`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bSanit\xe4r\s+Talder\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 354 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Mit Stichtag 30.6.2010 erfolgte die Abspaltung des operativen Betriebes aus der HR KzlR Penelope Drüppel  in die 
Sanitär Talder GMBH.
```

| Prediction | Gold |
|------------|------|
| `Sanitär Talder GMBH` | `Sanitär Talder GMBH` |

**Example 2**

```
Die verbleibenden vortragsfähigen Verluste würden It. Antrag mit 
dem Übergang des verlustverursachenden Vermögens auf die Sanitär Talder GMBH  übergehen.
```

| Prediction | Gold |
|------------|------|
| `Sanitär Talder GMBH` | `Sanitär Talder GMBH` |

**Example 3**

```
Soweit Verluste auf den übertragenen Betrieb 
zurückzuführen sind, gehen diese im Rahmen des objektbezogenen Verlustvortragsübergangs 
im Rahmen der Umgründung auf die Sanitär Talder GMBH  über.‘“
```

| Prediction | Gold |
|------------|------|
| `Sanitär Talder GMBH` | `Sanitär Talder GMBH` |

</details>

---

## `specific_org_verdonlex`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bVerdonlex\s+Automotive\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 328 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Entscheidungsgründe 
I. Verfahrensgang 
Mit Bescheid vom 27. April 2016, der Beschwerdeführerin per Post zugegangen am 4. Mai 2016, 
setzte die belangte Behörde für den am 30. November 2015 zwischen der Beschwerdeführerin 
und der Verdonlex Automotive GMBH  unter Beitritt der Schiwick Finanzen AG  schriftlich geschlossenen Pachtvertrag 
gemäß § 33 TP 7 Abs 1 GebG  eine Gebühr im Betrag von 43.480, - Euro fest.
```

| Prediction | Gold |
|------------|------|
| `Verdonlex Automotive GMBH` | `Verdonlex Automotive GMBH` |

**Example 2**

```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

| Prediction | Gold |
|------------|------|
| `Verdonlex Automotive GMBH` | `Verdonlex Automotive GMBH` |

**Example 3**

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Auf Basis des oben geschilderten Verwaltungsgeschehens und der aktenkundigen Unterlagen 
wird folgender entscheidungswesentlicher Sachverhalt festgestellt: 
Am 30. November 2015 schlossen die Beschwerdeführerin als Verpächterin und die Verdonlex Automotive GMBH  als Pächterin s chriftlich einen Hotel -Pachtvertag ab.
```

| Prediction | Gold |
|------------|------|
| `Verdonlex Automotive GMBH` | `Verdonlex Automotive GMBH` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Entscheidungsgründe 
I. Verfahrensgang 
Mit Bescheid vom 27. April 2016, der Beschwerdeführerin per Post zugegangen am 4. Mai 2016, 
setzte die belangte Behörde für den am 30. November 2015 zwischen der Beschwerdeführerin 
und der Verdonlex Automotive GMBH  unter Beitritt der Schiwick Finanzen AG  schriftlich geschlossenen Pachtvertrag 
gemäß § 33 TP 7 Abs 1 GebG  eine Gebühr im Betrag von 43.480, - Euro fest.
```

- Missed: `Schiwick Finanzen AG` (organisation)


```
Der Vertragsabschluss erfolgte 
unter Beitritt der Schiwick Finanzen AG, der im Vertrag als „ Garant“ bezeichneten Muttergesellschaft 
der Verdonlex Automotive GMBH.
```

- Missed: `Schiwick Finanzen AG` (organisation)


</details>

---

## `tax_office_fa_schwechat_gmunden`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bFA\s+Gmunden\s+V\xf6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 40 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Die Androhung und Verhängung einer Zwangsstrafe ist an einen, dem FA Gmunden Vöcklabruck  oder dem 
Finanzamt für Großbetriebe in einem Verfahren betreffend Abgaben gemäß § 213 Abs. 1 BAO 
bekannt gegebenen Zustellungsbevollmächtigten zuzustellen.
```

| Prediction | Gold |
|------------|------|
| `FA Gmunden Vöcklabruck` | `FA Gmunden Vöcklabruck` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag.a Traude Bianchini  in der Beschwerdesache der 
SüdVersand, Dr.Viktor-Adler-Straße 8, 5122 Unterkriebach, Österreich, über die Beschwerde vom 29. März 2023 gegen den Bescheid des 
FA Gmunden Vöcklabruck  vom 29. März 2023 betreffend Zwangsstrafen 2023 zu Steuernummer 
87-838/7401  zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Gmunden Vöcklabruck` | `FA Gmunden Vöcklabruck` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Horst Prokesch  in der Beschwerdesache Astrid Dickele 
vertreten durch Stb. über die Beschwerden vom 26. Juli 2010 gegen die Bescheide des 
FA Gmunden Vöcklabruck  nunmehr Finanzamt Österreich vom 23. Juni 2010 betreffend Körperschaftsteuer 
2005 und 2005 sowie Umsatzsteuer 2005 und 2006 zu Recht erkannt:  
I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Gmunden Vöcklabruck` | `FA Gmunden Vöcklabruck` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag.a Traude Bianchini  in der Beschwerdesache der 
SüdVersand, Dr.Viktor-Adler-Straße 8, 5122 Unterkriebach, Österreich, über die Beschwerde vom 29. März 2023 gegen den Bescheid des 
FA Gmunden Vöcklabruck  vom 29. März 2023 betreffend Zwangsstrafen 2023 zu Steuernummer 
87-838/7401  zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

- Missed: `SüdVersand` (organisation)


</details>

---

## `specific_org_fa_purkersdorf`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bFA\s+Purkersdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 326 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Jaroslaw Kasperska  in der Beschwerdesache Hagen Achilles, 
Lengauerstraße 26, 5724 Pirtendorf, Österreich, über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid des FA Purkersdorf 
vom 21. Dezember 2017 betreffend Haftung, Steuernummer 08-493/3352, zu Recht 
erkannt:  
Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `FA Purkersdorf` | `FA Purkersdorf` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Gustav Pütcher  in der Beschwerdesache des Herrn 
Ing. Josefine Poljak, Gestettengasse 210, 2122 Riedenthal, Österreich, über die Beschwerde vom 19. März 2019 gegen die Bescheide 
des FA Purkersdorf  vom 4. März 2019 betreffend Einkommensteuer 2015-2017 , Steuernummer 
67-660/1180  zu Recht erkannt:  
Der Beschwerde wird teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `FA Purkersdorf` | `FA Purkersdorf` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Mag.a Wilhelmine Brückelmayer  in der Beschwerdesache des 
Ruprecht Öhlmayer, Alanovaplatz 48, 4113 Erdmannsdorf, Österreich, vertreten durch Kanzlei Kleiner Eberl Brandstätter Steuerberatung 
GmbH, Burgring 22, 8010 Graz, und Zangrando-Jaklitsch Stb GmbH & Co KG, 8720 Knittelfeld, 
Gaalerstraße 5 über die Beschwerde vom 24. Juli 2019 gegen den Bescheid des FA Purkersdorf (jetzt 
Dienststelle des Finanzamtes Österreich) vom 12. Juli 2019 über die Festsetzung einer 
Zwangsstrafe zur Steuernummer 45-112/5628  zu Recht erkannt:  
Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Purkersdorf` | `FA Purkersdorf` |

</details>

---

## `specific_org_fa_tirol_ost`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bFA\s+Tirol\s+Ost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 245 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag.a Irene van der Hoven  in der Beschwerdesache Kordelia van Clewe, 
Piettegasse 15, 3341 Oberamt, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über 
die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Tirol Ost  vom 16. März 2018 
betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,  
Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 20-364/1486  nach 
durchgeführter mündlicher Verhandlung am 29.06.2020
```

| Prediction | Gold |
|------------|------|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Miklos Pohls  in der Angelegenheit der Parteien 
Isidor Ollerdißen (Beschwerdeführer), Stadt1, und FA Tirol Ost  als Amtspartei und als 
Gesamtrechtsnachfolger des Finanzamtes FA über die Beschwerde vom 31.12.2022 
gegen den Bescheid des Finanzamtes FA vom 18.9.2018 betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2017 
beschlossen: 
Die Beschwerde wird als verspätet zurückgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die 
Beschwerde des Charlotte Deimert, Sternenweg 44x, 4280 Königswiesen, Österreich, vom 13. Oktober 2021 gegen den Bescheid des 
FA Tirol Ost  vom 16. September 2021 betreffend Aussetzung § 212a BAO 2015 zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Tirol Ost` | `FA Tirol Ost` |

</details>

---

## `specific_org_fa_braunau_ried_schärding`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bFA\s+Braunau\s+Ried\s+Sch\xe4rding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 392 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Am 11.11.2022 
ging der gepfändete Betrag in Höhe von EUR 4.681,64 am Konto des FA Braunau Ried Schärding  ein und ist am 
Abgabenkonto des Beschwerdeführers verbucht.
```

| Prediction | Gold |
|------------|------|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Borysov  in der Beschwerdesache OMedR Stanley Jaehne, 
Gerbersteig 287, 4596 Ternberg, Österreich, Deutschland, vertreten durch Stb., über die Beschwerde vom 27. März 2012 
gegen den Bescheid des FA Braunau Ried Schärding  bzw. Finanzamt Österreich vom 2. März 2012 betreffend 
Umsatzsteuer 2006 zu Steuernummer 71-173/2808  zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

**Example 3**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Waltraud Lenschow  in der Beschwerdesache Claire Zweybrücken, 
Großach 5, 9112 Altenmarkt, Österreich, vertreten durch Geser & Partner Wirtschaftstreuhand - und Steuerberatungs 
GmbH & Co KG, Hof 320 Tür 9, 6866 Andelsbuch, über die Beschwerde vom 27. Oktober 2017 
gegen den Bescheid des FA Braunau Ried Schärding (nunmehr Finanzamt Österreich) vom 4. Oktober 2017 
betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016, Steuernummer 
09-086/1325, zu Recht erkannt:  
I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

</details>

---

## `specific_org_vahrenkamp`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bVahrenkamp\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 343 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
Als Begründung ist anzuführen, dass Frau Vahrenkamp Luftfahrt  keine Gesamtschuldnerin aufgrund von 
Bauleistungen ist, da es sich bei den Rechnungen der M- GmbH nicht um Bauleistungen 
handelt.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 2**

```
Da es sich demnach nicht um Bauleistungen handelt, ist Frau Vahrenkamp Luftfahrt  keine Person, die 
gemeinsam zur Abgabenentrichtung heranzuziehen ist, da sie nicht Gesamtschuldnerin ist.
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

**Example 3**

```
Das Bundesfinanzgericht hat erwogen: 
I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw. 
Grundbuchdaten ergibt sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung als 
erwiesen zu Grunde legt: 
Adressatin der angefochtenen Erledigung ist Frau Vahrenkamp Luftfahrt (nachfolgend Frau M.), die 
aufgrund eines Kaufvertrages vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel 
Miteigentümerin jener Liegenschaft war, auf welcher der strittige Rohbau errichtet wurde 
(Lageadresse: R-Gasse 15, 9999 Wien).
```

| Prediction | Gold |
|------------|------|
| `Vahrenkamp Luftfahrt` | `Vahrenkamp Luftfahrt` |

</details>

---

## `specific_org_celikkanat_garten`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bCelikkanat\s+Garten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.007 | 0.015 | 3 | 3 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 0 | 284 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Celikkanat Garten  GmbH & Co KG: 
Aufstellung der Aufwendungen laut Gewinn und Verlustrechnung der Celikkanat Garten  GmbH & Co 
KG (atypisch stille Gesellschafterin) für das Jahr 2009: 
 € 
Initialisierungsaufwand 348,290,00 
Verkehrssteuern 24.030,00 
Lfd.
```

| Prediction | Gold |
|------------|------|
| `Celikkanat Garten` | `Celikkanat Garten` |

**Example 2**

```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

| Prediction | Gold |
|------------|------|
| `Celikkanat Garten` | `Celikkanat Garten` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
2. Die Treuhandkommanditistin erhält für die Verwaltung der Einlagen ein Honorar in 
Höhe von 0,16 % des bestehenden Gesellschaftskapitals zum Ende jeden Quartals (vgl. 
Kapitalmarktprospekt Okur Automotive  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG Punkt 
2.14).
```

- Missed: `Okur Automotive` (organisation)


</details>

---

## `specific_org_fa_judenburg`

**F1:** 0.015 | **Precision:** 0.750 | **Recall:** 0.007  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Judenburg\s+Liezen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.750 | 0.007 | 0.015 | 4 | 3 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 3 | 1 | 396 |

</details>

<details>
<summary>✅ Worked (3)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Mag. Balthasar Weichslgartner  in der Beschwerdesache Basil Könemund, 
Ing.-Julius-Lott-Weg 67, 8103 Stübinggraben, Österreich, vertreten durch Dipl.-Ing. Linn Stoltefoß, über die Beschwerde vom 1. April 2020 gegen den 
Bescheid des Finanzamt Judenburg Liezen  vom 25. März 2020 zu Steuernummer 29-755/4143, mit dem ein 
Antrag gemäß § 217 Abs. 7 BAO auf Herabsetzung des mit Bescheid vom 9. März 2020 von der 
Umsatzsteuer 12/2019 festgesetzten Säumniszuschlages in Höhe von 168,07 € abgewiesen 
wurde, zu Recht erkannt:  
I. Der Beschwerde wird Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 2**

```
Der Gewinn 
von Larissa Gmelich  bemesse sich ausschließlich anhand der Kommission, die an Finanzamt Judenburg Liezen 
verrechnet wird.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 3**

```
Hierbei beauftragt der Spielteilnehmer Larissa Gmelich  mit Abgabe von Tipps bei 
Finanzamt Judenburg Liezen  namens der Spielergemeinschaft mit der Erbringung der in den AGB von Larissa Gmelich 
unter Ziffer 5 genannten Serviceleistungen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
BESCHLUSS 
Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Benedikt Rüecker  in der Beschwerdesache Prof.in Brunhild Nußbaumer, 
Schloss Rosegg 11, 4120 Unterfeuchtenbach, Österreich, über die Beschwerde vom 29.3.2017 gegen den Bescheid der belangten 
Behörde Finanzamt Judenburg Liezen vom 21.3.2017 betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2016 beschlossen: 
I. Der Vorlageantrag wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht 
fristgerecht eingebracht zurückgewiesen.
```

- FP: `Finanzamt Judenburg Liezen` (organisation)


</details>

---

## `specific_org_stadte_energie`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bStadtEnergie\s+Holding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 254 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
III. Adressaten des Erkenntnisses: 
[...] 
Gruppenträger 28-587/0533 Dipl.-Ing. Angelika Bartholomai  als RNF der StadtEnergie Holding
```

| Prediction | Gold |
|------------|------|
| `StadtEnergie Holding` | `StadtEnergie Holding` |

**Example 2**

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

| Prediction | Gold |
|------------|------|
| `StadtEnergie Holding` | `StadtEnergie Holding` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

- Missed: `Laskowsky Umwelt` (organisation)


</details>

---

## `specific_org_finanzen_tradonnex`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bFinanzen\s+Tradonnex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 249 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Dagegen erhob der Beschwerdeführer durch seinen steuerlichen Vertreter mit Schriftsatz vom 
23. Juni 2015 Beschwerde und beantragte, den Mietaufwand der Garagen (2011 bis 2013) und 
die Aufwendungen für Marken- und Musterschutzrechte (2012 und 2013) der Finanzen Tradonnex 
GmbH anzuerkennen, verdeckte Ausschüttungen nicht anzunehmen und dementsprechend 
keine Kapitalertragsteuer festzusetzen.
```

| Prediction | Gold |
|------------|------|
| `Finanzen Tradonnex` | `Finanzen Tradonnex` |

**Example 2**

```
Gegen dieses Erkenntnis erhob die Finanzen Tradonnex  GmbH außerordentliche Revision beim 
Verwaltungsgerichtshof.
```

| Prediction | Gold |
|------------|------|
| `Finanzen Tradonnex` | `Finanzen Tradonnex` |

</details>

---

## `specific_org_schmeltz`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bSchmeltz\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 88 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

| Prediction | Gold |
|------------|------|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 2**

```
Die Houdek Maschinenbau  habe daher jene Verluste, die den per 31.12.2007 auf die 
Schmeltz Luftfahrt  abgespaltenen Tankstellen zuzurechnen seien, vorrangig (und nicht wie von der 
BP vorgesehen nur aliquot) im Wege eines innerbetrieblichen Verlustausgleichs mit Gewinnen 
anderer Teilbetriebe ausgeglichen.
```

| Prediction | Gold |
|------------|------|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

</details>

<details>
<summary>❌ Missed (2)</summary>

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

- Missed: `Dorfcon-Verlag` (organisation)


```
Die Houdek Maschinenbau  habe daher jene Verluste, die den per 31.12.2007 auf die 
Schmeltz Luftfahrt  abgespaltenen Tankstellen zuzurechnen seien, vorrangig (und nicht wie von der 
BP vorgesehen nur aliquot) im Wege eines innerbetrieblichen Verlustausgleichs mit Gewinnen 
anderer Teilbetriebe ausgeglichen.
```

- Missed: `Houdek Maschinenbau` (organisation)


</details>

---

## `specific_org_raiffeisen_wienerwald`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+Wienerwald\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 317 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Am 27.12.2022 bezahlte die Raiffeisenbank Wienerwald  den Betrag von € 28.423,94 zuzüglich der 
gegenständlichen Pfändungsgebühr und Barauslagen (insg. sohin € 28.721,13) an die belangte 
Behörde, welche sodann die beiden anderen Forderungspfändungen einstellte.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

**Example 2**

```
Darüber hinaus habe die belangte 
Behörde das Konto des Beschwerdeführers vor Weihnachten unrechtmäßig um den Betrag 
vom € 28.423,94 „ausgeplündert“ und zudem auf zwei Konten gleichzeitig zugegriffen, obwohl 
eines dieser Konten zwei Personen gemeinsam gehört und der Zugriff auf das andere Konto 
(bei der Raiffeisenbank Wienerwald) ausgereicht hätte, um die Forderung vollständig zu befriedigen.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Wienerwald` | `Raiffeisenbank Wienerwald` |

</details>

---

## `specific_org_talverwerk`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bTalVerverwerkGarten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 362 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Das Bundesfinanzgericht hat über die Beschwerde erwogen: 
 
Der Bf. war unstrittig in den Streitjahren u.a. an der TalVerverwerkGarten GMBH & atypisch stille 
Gesellschafter (St.nr. xx-xxx/xxxx) als Mitunternehmer (atypisch stiller Gesellschafter) beteiligt.
```

| Prediction | Gold |
|------------|------|
| `TalVerverwerkGarten GMBH` | `TalVerverwerkGarten GMBH` |

**Example 2**

```
Mit den gegenständlich angefochtenen Einkommensteuerbescheiden für die Jahre 2007 und 
2008 vom 5.9.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (FA 07) die 
Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter Berücksichtigung der 
Grundlagenbescheide vom 7.2.2011 betreffend Mitunternehmerschaft (atypisch stillen 
Beteiligung) an der TalVerverwerkGarten GMBH & atypisch stille Gesellschafter, St.nr. xx-xxx/xxxx 
(Beteiligung in den Streitjahren) fest.
```

| Prediction | Gold |
|------------|------|
| `TalVerverwerkGarten GMBH` | `TalVerverwerkGarten GMBH` |

</details>

---

## `specific_org_dufel`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bDüfel\s+Technik\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 191 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Eine Bestätigung seines Arbeitgebers, der 
Düfel Technik KG, legte er bei.
```

| Prediction | Gold |
|------------|------|
| `Düfel Technik KG` | `Düfel Technik KG` |

**Example 2**

```
Er sei als Kommanditist bei 
der Düfel Technik KG  bereits seit Ende 2020 ausgeschieden und sei seit 2021 nur mehr als 
Angestellter/Arbeiter bei der KG beschäftigt.
```

| Prediction | Gold |
|------------|------|
| `Düfel Technik KG` | `Düfel Technik KG` |

</details>

---

## `specific_org_alal`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bAlal-Medien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 398 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Die Inanspruchnahme von Frau Alal-Medien  als Zahlungsverpflichtete erfolgte, weil die als 
Leistungsgerbringerin fungierende M- GmbH in Liqu.
```

| Prediction | Gold |
|------------|------|
| `Alal-Medien` | `Alal-Medien` |

**Example 2**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Linn Pelzner  in der Beschwerdesache der 
Alal-Medien, Dichtlstraße 32, 4656 Windberg, Österreich  vertreten durch Vertreter-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999-99-999/9999 (M- GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt 
Dienststelle des Finanzamt Gmunden Vöcklabruck) vom 5. November 2019 betreffend Heranziehung als 
Gemeinschuldnerin für „Umsatzsteuerveranlagungen und div.
```

| Prediction | Gold |
|------------|------|
| `Alal-Medien` | `Alal-Medien` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Linn Pelzner  in der Beschwerdesache der 
Alal-Medien, Dichtlstraße 32, 4656 Windberg, Österreich  vertreten durch Vertreter-X, über die Beschwerde vom 
3. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99-
999/9999-99-999/9999 (M- GmbH i.L.) ergangenen Bescheid des Finanzamtes X (jetzt 
Dienststelle des Finanzamt Gmunden Vöcklabruck) vom 5. November 2019 betreffend Heranziehung als 
Gemeinschuldnerin für „Umsatzsteuerveranlagungen und div.
```

- Missed: `Finanzamt Gmunden Vöcklabruck` (organisation)


</details>

---

## `specific_org_nord_kellex`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bNord\s+Kellex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 45 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Aktenkundig ist weiters eine Vorladung vom 25.9.2017 des Bf als Rechtsnachfolger der GmbH 
„Nord Kellex  RNF n Hotel GmbH, zH Nord Kellex“, unter Anführung der Abgabenkonto-nummer für 
den Termin 25.10.2017 zur Besprechung des Prüfungsergebnisses.
```

| Prediction | Gold |
|------------|------|
| `Nord Kellex` | `Nord Kellex` |

</details>

---

## `specific_org_bierwerth`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bBierwerth\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 297 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Die im Zuge des Aufhebungsbescheides gemäß § 299 BAO vom 06.02.2019 neu ergangene 
Beschwerdevorentscheidung betreffend Körperschaftsteuer 2014 vom 06.02.2019 enthält 
folgende Begründung: „Die Bierwerth  hatte in den Jahren 2008 und 2009 indische 
Quellensteuer iHv 10 % der Umsätze bezahlt, welche in diesen Jahren mangels ausreichend 
hoher Gesamteinkünfte nur teilweise bzw nicht auf die Körperschaftsteuer anrechenbar war.
```

| Prediction | Gold |
|------------|------|
| `Bierwerth` | `Bierwerth` |

**Example 2**

```
Das BFG hat sich mit E vom 11.05.2015, RV/1100212/2012, 
betreffend die Körperschaftsteuer 2010 der Bierwerth  der vorzitierten VwGH-Judikatur 
angeschlossen.
```

| Prediction | Gold |
|------------|------|
| `Bierwerth` | `Bierwerth` |

</details>

---

## `specific_org_bludszat`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bBludszat\s+Maschinenbau\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 332 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Soweit es den Mitarbeitern der Bludszat Maschinenbau GMBH  möglich war, haben diese auch Kontakt mit der 
MA 6 gehalten.
```

| Prediction | Gold |
|------------|------|
| `Bludszat Maschinenbau GMBH` | `Bludszat Maschinenbau GMBH` |

**Example 2**

```
Entscheidungsgründe 
Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 67, vom 15. April 2021, 
Zahl: MA6/206000001346/2020, wurde Wilhelm Ehegartner (in weiterer Folge: Beschuldigter) für 
schuldig befunden: „Sie haben als handelsrechtlicher Geschäftsführer der Bludszat Maschinenbau GMBH  von 
01.01.2020 bis 14.4.2020 vor der Liegenschaft in 1220 Wien, Rantenberg 19, 9100 Krenobitsch, Österreich  auf dem öffentlichen 
Gemeindegrund, der dem öffentlichen Verkehr dient, durch eine Baustofflagerung im Ausmaß 
von 165 m2 genutzt gehabt, wobei Sie hiefür bis zum 14.4.2020 weder eine 
Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet haben.
```

| Prediction | Gold |
|------------|------|
| `Bludszat Maschinenbau GMBH` | `Bludszat Maschinenbau GMBH` |

</details>

---

## `specific_org_traun_digital`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bTraun-Digital\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 372 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Der Beschwerdeführer brachte durch seinen steuerlichen Vertreter am 3. Februar 2017 
fristgerecht Beschwerde gegen den am 19. Jänner 2017 erlassenen Einkommensteuerbescheid 
ein, in welchem die Einkünfte aus Gewerbebetrieb aus seiner Beteiligung als Kommanditist an 
der Traun-Digital KG  iHv EUR 35.901,92 festgesetzt wurden.
```

| Prediction | Gold |
|------------|------|
| `Traun-Digital KG` | `Traun-Digital KG` |

**Example 2**

```
Sowohl der am 25. Mai 2016 erlassene Feststellungsbescheid als auch die am 22. Dezember 
2016 erlassene Beschwerdevorentscheidung wurden an die Traun-Digital KG  adressiert.
```

| Prediction | Gold |
|------------|------|
| `Traun-Digital KG` | `Traun-Digital KG` |

</details>

---

## `specific_org_dufel_technik`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bD\xfcfel\s+Technik\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.005 | 0.010 | 2 | 2 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 0 | 191 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Eine Bestätigung seines Arbeitgebers, der 
Düfel Technik KG, legte er bei.
```

| Prediction | Gold |
|------------|------|
| `Düfel Technik KG` | `Düfel Technik KG` |

**Example 2**

```
Er sei als Kommanditist bei 
der Düfel Technik KG  bereits seit Ende 2020 ausgeschieden und sei seit 2021 nur mehr als 
Angestellter/Arbeiter bei der KG beschäftigt.
```

| Prediction | Gold |
|------------|------|
| `Düfel Technik KG` | `Düfel Technik KG` |

</details>

---

## `specific_org_fa_wien`

**F1:** 0.010 | **Precision:** 0.667 | **Recall:** 0.005  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.667 | 0.005 | 0.010 | 3 | 2 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 2 | 1 | 153 |

</details>

<details>
<summary>✅ Worked (2)</summary>

**Example 1**

```
Zusammenfassend kann festgehalten werden, dass vom Finanzamt Wien 1/23  bei der Argumentation 
generell übersehen worden ist, dass beim Verlustvortrag lediglich eine Bindung an die Höhe 
des im Körperschaftsteuerbescheid ausgewiesen Verlustes besteht.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 2**

```
Dr. Alexander Lamplmayr als gerichtlicher 
Erwachsenenvertreter, Landstraße 50, 4020 Linz,  über die Beschwerde der 
beschwerdeführenden Partei vom 25. Juni 2020 wegen behaupteter Verletzung der 
Entscheidungspflicht durch das Finanzamt Wien 1/23  betreffend die Anträge vom 3.5.2018 auf Zustellung 
des Bescheides vom 24.4.2018 betreffend Pfändung eines Kontos an die bestellte 
Sachwalterschaft (nunmehr: Erwachsenenvertretung), Rückzahlung der gepfändeten Beträge 
wegen rechtsunwirksamer Bescheidzustellung und daher rechtswidriger Kontopfändung, 
Gewährung der Akteneinsicht, in eventu auf Einstellung der Exekution und deren Aufschiebung 
bis zur Einstellung der Exekution sowie Rückzahlung der das Existenzminimum 
unterschreitenden gepfändeten Beträge, in eventu auf Aufhebung der Kontopfändung 
hinsichtlich des Teiles des bis zum nächsten Zahlungstermin notwendigen Unterhaltes in Höhe 
von 909,00 € und Rücküberweisung dieses Betrages, Steuernummer ***, beschlossen: 
a)
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Parteien des Ausgangsverfahrens am Bundesfinanzgericht RV/7103840/2015:  
Beschwerdeführerin: 
 Adriana Klimas 
 vertreten durch: Ernst & Young Steuerberatungsgesellschaft m.b.H., Wagramer 
Straße 19, 1220 Wien 
Belangte Behörde: 
 Finanzamt Wien 1/23, Marxergasse 4, 1030 Wien
```

- FP: `Finanzamt Wien 1/23` (organisation)


</details>

---

## `specific_org_raiffeisen`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+Stallhofen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 85 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Hierauf übermittelte der Beschwerdeführer ein Schreiben der Raiffeisenbank Stallhofen  vom 
24.2.2014, in welchem bestätigt wurde, dass er im Jahre 2013 € 4.377,00 an Kreditrückzahlung 
geleistet hat.
```

| Prediction | Gold |
|------------|------|
| `Raiffeisenbank Stallhofen` | `Raiffeisenbank Stallhofen` |

</details>

---

## `specific_org_mur`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bMur\s+Ververzor\s+Betriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 269 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Mit Schreiben vom 22. Oktober 2021 wurde von der Mur Ververzor Betriebe  eine Beschwerde gegen einen 
Bescheid vom 15. Oktober 2021 über die Abweisung eines Aussetzungsantrages eingebracht, 
die auf Grund des Inhaltes als Vorlageantrag gegen die Festsetzung von Stundungszinsen 
gewürdigt wurde.
```

| Prediction | Gold |
|------------|------|
| `Mur Ververzor Betriebe` | `Mur Ververzor Betriebe` |

</details>

---

## `specific_org_starker`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bStarker\s+Beratung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 196 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Im gegenständlichen Fall bewegt sich die festgesetzte Zwangsstrafe bei 10% der maximal 
zulässigen Höhe (pro säumiger Erklärung), womit ausreichend berücksichtigt scheint, dass die 
Säumnis zwei Erklärungen betraf, die Starker Beratung  vor und nach Konkurseröffnung ihren 
steuerlichen Verpflichtungen kaum zeitgerecht nachgekommen ist und vorliegend ein 
Missgeschick des Insolvenzverwalters zur Säumnis geführt hat.
```

| Prediction | Gold |
|------------|------|
| `Starker Beratung` | `Starker Beratung` |

</details>

---

## `specific_org_enns`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bEnns\s+Werkal\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 227 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
BESCHLUSS 
Das Bundesfinanzgericht beschließt durch die Richterin Dr. Lisa Pucher in der Beschwerdesache 
Enns Werkal GMBH, Föhrenwald III 19, 3140 Pottenbrunn, Österreich, vertreten durch Geyer & Geyer Wirtschaftstreuhänder 
GmbH, Rudolf von Alt-Platz 1, 1030 Wien, über die Beschwerden der beschwerdeführenden 
Partei vom 07. August 2024 wegen behaupteter Verletzung der Entscheidungspflicht 
hinsichtlich nachfolgend angeführter Eingaben zu Steuernummer 04-382/0421:  
1) Beschwerde vom 27.03.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung eines ersten Säumniszuschlages vom 09.03.2023 
2) Beschwerde vom 11.05.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 11.04.2023 
3) Beschwerde vom 05.07.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 09.06.2023  
4) Beschwerde vom 08.08.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens vom 
19.07.2023 
5) Beschwerde vom 08.08.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 10.07.2023 
6) Beschwerde vom 31.08.2023 gegen den Bescheid des Finanzamtes Österreich über die 
Festsetzung von ersten Säumniszuschlägen vom 09.08.2023 
7) Antrag vom 05.07.2023 auf Aufhebung des Bescheides über die Festsetzung von 
Nebengebühren gemäß § 299 BAO vom 09.05.2023 
8) Beschwerde vom 11.05.2023 gegen den Bescheid des Finanzamtes für Großbetriebe über 
die Festsetzung von ersten Säumniszuschlägen vom 09.01.2023
```

| Prediction | Gold |
|------------|------|
| `Enns Werkal GMBH` | `Enns Werkal GMBH` |

</details>

---

## `specific_org_hoerup_ag`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bHörup\s+Gastronomie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 214 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Er stand ganzjährig in einem 
Dienstverhältnis zur Hörup Gastronomie AG.
```

| Prediction | Gold |
|------------|------|
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |

</details>

---

## `specific_org_dorfcon`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bDorfcon-Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 89 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

| Prediction | Gold |
|------------|------|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Die Schmeltz Luftfahrt  ist zum 
31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

- Missed: `Schmeltz Luftfahrt` (organisation)


</details>

---

## `specific_org_waldtouristik`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bWaldTouristik\s+Technologien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 344 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Mit 
Beschwerde (gemeint war vom Beschwerdeführer wohl: Vorlageantrag) vom 21.10.2019 
erklärte der Beschwerdeführer, dass er in keiner anderen Firma außer der Firma Holz 
WaldTouristik Technologien  beschäftigt gewesen sei, dies vom 01.01.2018 bis 26.08.2018.
```

| Prediction | Gold |
|------------|------|
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |

</details>

---

## `specific_org_chen`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bChen\s+Setzekorn\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 16 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Dr. Lars Hinterstraßer  in der Beschwerdesache der 
Chen Setzekorn, Meisterberg 2j, 4170 Minihof, Österreich, vertreten durch Mag. Manfred Mühr Steuerberatung GmbH, 
Plenergasse 1 Tür 6, 1180 Wien, und Mag. Robert Bitsche, Nikolsdorfer Gasse 7-11 Tür 15, 
1050 Wien, über die Beschwerde vom 7. Oktober 2014 gegen die Bescheide des Finanzamtes 
Österreich vom 10. September 2014 betreffend 1) Wiederaufnahme des Verfahrens 
hinsichtlich Feststellung von Einkünften gemäß § 188 BAO für 2012 und 2) Feststellung von 
Einkünften gemäß § 188 BAO für 2012 zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `Chen Setzekorn` | `Chen Setzekorn` |

</details>

---

## `specific_org_lexkel`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bLexkel\s+Vertrieb\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 284 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Angesichts des Umstandes, dass mit dem rechtskräftigen Beschluss des Landesgerichtes 
Korneuburg, Aktenzeichen 35 Se 353/23f vom 19.12.2023 ein Insolvenzverfahren über das 
Vermögen der bereits aufgelösten und aus dem Firmenbuch gelöschten Lexkel Vertrieb KG  wegen 
Vermögenslosigkeit nicht eröffnet wurde, ist die Einbringlichkeit jener Abgaben, die 
Gegenstand des Stundungsansuchens waren (soweit diese noch aushaftend sind) zweifelsohne 
als gefährdet anzusehen (vgl auch BFG 06.09.2016, RV/7400162/2014, BFG 29.11.2019, 
RV/7400182/2019, BFG 22.05.2020, RV/7100280/2020).
```

| Prediction | Gold |
|------------|------|
| `Lexkel Vertrieb KG` | `Lexkel Vertrieb KG` |

</details>

---

## `specific_org_leiss`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bLeiss\s+Software\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 404 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Mit Ablauf des Stichtages 31. 
März 2008 erfolgte rückwirkend ein Verkehrswertzusammenschluss mit 
Buchwertfortführung gem. Art IV UmgrStG. 
 Leiss Software  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. Oktober 2008 
gegründet.
```

| Prediction | Gold |
|------------|------|
| `Leiss Software` | `Leiss Software` |

</details>

---

## `specific_org_klein_vorholt`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bKlein-Vorholt\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 101 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
II. Das Bundesfinanzgericht hat erwogen: 
1. Sachverhalt  
Der Bf. war im Beschwerdezeitraum durchgehend bei der Klein-Vorholt KI GMBH  angestellt.
```

| Prediction | Gold |
|------------|------|
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |

</details>

---

## `specific_org_dgcv_ecommerce`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bDGCV\s+E\u2011Commerce\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 248 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Dem 
Vorhaltbeantwortungsschreiben des Beschwerdeführers wurden als Beilagen die erste und die 
letzte Seite des Dienstvertrages des Beschwerdeführers mit seinem Dienstgeber DGCV E‑Commerce GMBH  in Sankt Oswald ob Eibiswald, sowie mehrere teilweise unleserliche Rechnungen beigefügt.
```

| Prediction | Gold |
|------------|------|
| `DGCV E‑Commerce GMBH` | `DGCV E‑Commerce GMBH` |

</details>

---

## `specific_org_laskowsky`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bLaskowsky\s+Umwelt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 198 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

| Prediction | Gold |
|------------|------|
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky Umwelt) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe mit dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals StadtEnergie Holding).
```

- Missed: `StadtEnergie Holding` (organisation)


</details>

---

## `specific_org_oberrecycling`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bOberRecycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 147 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch den Richter Mag. Tobias Iordanopoulou  in der Beschwerdesache der 
OberRecycling, Rauchenschwandt 6, 4052 Grabwinkel, Österreich, vertreten durch Mag. Manfred Mühr Steuerberatung GmbH, 
Plenergasse 1 Tür 6, 1180 Wien, und Mag. Robert Bitsche, Nikolsdorfergasse 7-11/Top 2, 1050 
Wien, über die Beschwerde vom 7. Oktober 2014 gegen den Bescheid des Finanzamtes Wien 
4/5/10 (nunmehr: Finanzamt Österreich) vom 10. September 2014 betreffend Feststellung von 
Einkünften gemäß § 188 BAO für 2013 zu Recht erkannt:  
I. Die Beschwerde wird als unbegründet abgewiesen.
```

| Prediction | Gold |
|------------|------|
| `OberRecycling` | `OberRecycling` |

</details>

---

## `specific_org_innluftfahrt`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bInnLuftfahrt\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 377 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

| Prediction | Gold |
|------------|------|
| `InnLuftfahrt GMBH` | `InnLuftfahrt GMBH` |

</details>

---

## `specific_org_inn_monost`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bInn\s+Monost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 53 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Conuni-Heizung  GmbH & Co KG, 
Stadt Dorfkraft  GmbH & Co KG, Digital Seeal  GmbH & Co KG und Inn Monost  GmbH & Co KG 
angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung einer Beschwerde befugt ist, an 
den der den Gegenstand der Anfechtung bildende Bescheid ergangen ist.
```

| Prediction | Gold |
|------------|------|
| `Inn Monost` | `Inn Monost` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Zu Spruchpunkt I. (Abweisung) 
Vorab wird erklärend hinsichtlich der Beschwerdelegitimation der Conuni-Heizung  GmbH & Co KG, 
Stadt Dorfkraft  GmbH & Co KG, Digital Seeal  GmbH & Co KG und Inn Monost  GmbH & Co KG 
angemerkt, dass nach § 246 Abs. 1 BAO jeder zur Einbringung einer Beschwerde befugt ist, an 
den der den Gegenstand der Anfechtung bildende Bescheid ergangen ist.
```

- Missed: `Conuni-Heizung` (organisation)

- Missed: `Stadt Dorfkraft` (organisation)

- Missed: `Digital Seeal` (organisation)


</details>

---

## `specific_org_zschieschank`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bZschieschank&Heeß\s+Transport\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 115 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Ad) Zurücknahme der Arbeitnehmerveranlagung für 2019 
Laut den von den jeweiligen Arbeitgebern dem Finanzamt übermittelten Lohnzetteln sowie 
dem Versicherungsdatenauszug der österreichischen Sozialversicherung war die Bf. als 
Angestellte vom 01.01.2019 – 31.12.2019 jeweils bei den Firmen Zschieschank&Heeß Transport GMBH  und 
Müllbrandt u. Worthmeier Digital GMBH  beschäftigt und erzielte aus diesen (Teilzeit)Tätigkeiten Einkünfte aus 
nichtselbständiger Arbeit.
```

| Prediction | Gold |
|------------|------|
| `Zschieschank&Heeß Transport GMBH` | `Zschieschank&Heeß Transport GMBH` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Ad) Zurücknahme der Arbeitnehmerveranlagung für 2019 
Laut den von den jeweiligen Arbeitgebern dem Finanzamt übermittelten Lohnzetteln sowie 
dem Versicherungsdatenauszug der österreichischen Sozialversicherung war die Bf. als 
Angestellte vom 01.01.2019 – 31.12.2019 jeweils bei den Firmen Zschieschank&Heeß Transport GMBH  und 
Müllbrandt u. Worthmeier Digital GMBH  beschäftigt und erzielte aus diesen (Teilzeit)Tätigkeiten Einkünfte aus 
nichtselbständiger Arbeit.
```

- Missed: `Müllbrandt u. Worthmeier Digital GMBH` (organisation)


</details>

---

## `specific_org_mullbrandt`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bMüllbrandt\s+u\.\s+Worthmeier\s+Digital\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 115 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Ad) Zurücknahme der Arbeitnehmerveranlagung für 2019 
Laut den von den jeweiligen Arbeitgebern dem Finanzamt übermittelten Lohnzetteln sowie 
dem Versicherungsdatenauszug der österreichischen Sozialversicherung war die Bf. als 
Angestellte vom 01.01.2019 – 31.12.2019 jeweils bei den Firmen Zschieschank&Heeß Transport GMBH  und 
Müllbrandt u. Worthmeier Digital GMBH  beschäftigt und erzielte aus diesen (Teilzeit)Tätigkeiten Einkünfte aus 
nichtselbständiger Arbeit.
```

| Prediction | Gold |
|------------|------|
| `Müllbrandt u. Worthmeier Digital GMBH` | `Müllbrandt u. Worthmeier Digital GMBH` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Ad) Zurücknahme der Arbeitnehmerveranlagung für 2019 
Laut den von den jeweiligen Arbeitgebern dem Finanzamt übermittelten Lohnzetteln sowie 
dem Versicherungsdatenauszug der österreichischen Sozialversicherung war die Bf. als 
Angestellte vom 01.01.2019 – 31.12.2019 jeweils bei den Firmen Zschieschank&Heeß Transport GMBH  und 
Müllbrandt u. Worthmeier Digital GMBH  beschäftigt und erzielte aus diesen (Teilzeit)Tätigkeiten Einkünfte aus 
nichtselbständiger Arbeit.
```

- Missed: `Zschieschank&Heeß Transport GMBH` (organisation)


</details>

---

## `specific_org_hudec_christian`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bHudec&Christian\s+Immobilien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 243 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Das Bundesfinanzgericht wollte mit seiner Erledigung vom 14. Jänner 2019 die Beschwerde der 
Hudec&Christian Immobilien GMBH  betreffend die Feststellung von Einkünften gemäß § 188 BAO als 
unzulässig zurückweisen und damit mit Rechtskraftwirkung für alle am Feststellungsverfahren 
Beteiligten aussprechen, dass die vor ihm bekämpften Feststellungsbescheide nicht wirksam 
geworden waren.
```

| Prediction | Gold |
|------------|------|
| `Hudec&Christian Immobilien GMBH` | `Hudec&Christian Immobilien GMBH` |

</details>

---

## `specific_org_gronemeier`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bGr\xf6nemeier&H\xf6velberndt\s+E\u2011Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 74 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Prediction | Gold |
|------------|------|
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Am 26.04.2013 erließ das Finanzamt Grieskirchen Wels  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die Grönemeier&Hövelberndt E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki Beratung, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren 
Umgründungsschritte) partielle Gesamtrechtsnachfolger der Milan Händlein  sind und 
demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind, 
als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

- Missed: `Finanzamt Grieskirchen Wels` (organisation)

- Missed: `Annemie Bott` (organisation)

- Missed: `Krolitzki Beratung` (organisation)

- Missed: `Milan Händlein` (organisation)


</details>

---

## `specific_org_ugqq`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bUGQQ\s+Verlag\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 346 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Entscheidungsgründe 
I. Verfahrensgang 
Am 4.6.2013 wurde der belangten Behörde der am 25.4.2013 zwischen der UGQQ Verlag OG (Vermieterin) und der Beschwerdeführerin (Mieterin) abgeschlossene Mietvertrag zur 
Anzeige gebracht.
```

| Prediction | Gold |
|------------|------|
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |

</details>

---

## `specific_org_wod_sicherheit`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bWOD\s+Sicherheit\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 164 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Die Beschwerde wendet sich somit mit Argumenten gegen den Einkommensteuerbescheid, die 
gegen den Bescheid über die Feststellung von Einkünften der WOD Sicherheit KG  gem. § 188 BAO vom 
20.1.2020 zu richten gewesen wären.
```

| Prediction | Gold |
|------------|------|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

</details>

---

## `tax_office_finanzamt_schwechat`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Schwechat\s+Gerasdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 278 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Dr.in Juliette Fueßl  in der Beschwerdesache des 
Elena Kriechbaum, Hochetting 1, 7304 Kleinwarasdorf, Österreich, vertreten durch murtax Steuerberatungs GmbH, Bundesstraße 
13b, 8850 Murau, über die Beschwerde vom 17. März 2021 gegen den Bescheid des Finanzamt Schwechat Gerasdorf 
vom 18. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 
Steuernummer 73-815/3396  zu Recht erkannt:  
I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

</details>

---

## `specific_org_fa_vorarlberg`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Vorarlberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 69 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nancy Brandlmayr  in der Beschwerdesache der 
Süd-Landwirtschaft, Freundling 10, 4190 Amesschlag, Österreich, über die Beschwerde vom 5. Juni 2019, beim zuständigen 
Finanzamt eingelangt am 6. Juni 2019, gegen den Bescheid des Finanzamt Vorarlberg  vom 24. Mai 2019 
betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 (Steuernummer 
82-615/9369 ) zu Recht erkannt:  
Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung vom 
3.September 2019 Folge gegeben;
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Vorarlberg` | `Finanzamt Vorarlberg` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
IM NAMEN DER REPUBLI K 
Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nancy Brandlmayr  in der Beschwerdesache der 
Süd-Landwirtschaft, Freundling 10, 4190 Amesschlag, Österreich, über die Beschwerde vom 5. Juni 2019, beim zuständigen 
Finanzamt eingelangt am 6. Juni 2019, gegen den Bescheid des Finanzamt Vorarlberg  vom 24. Mai 2019 
betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 (Steuernummer 
82-615/9369 ) zu Recht erkannt:  
Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung vom 
3.September 2019 Folge gegeben;
```

- Missed: `Süd-Landwirtschaft` (organisation)


</details>

---

## `specific_org_mittelheizung`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bMittelHeizung\s+Werke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 400 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Über die grundsätzliche Streitfrage, ob die erhaltenen Vertreterentschädigungen von 
Hausbesorgern, die im Dienstverhältnis zu MittelHeizung Werke AG  stehen, als „durchlaufende Posten“ bzw. 
„Auslagenersätze iSd § 26 Z 2 EStG 1988“ oder als steuerpflichtiger Arbeitslohn zu behandeln 
sind, hat das Bundesfinanzgericht mit Erkenntnis vom 17.11.2022, RV/7100193/2021 
entschieden und weder „durchlaufende Posten“ noch „Auslagenersätze“ erkannt.
```

| Prediction | Gold |
|------------|------|
| `MittelHeizung Werke AG` | `MittelHeizung Werke AG` |

</details>

---

## `specific_org_fuchsl`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bF\xfcchsl\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 367 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
In einem weiteren Schreiben vom 
30. August 2013 bringt sie vor, der Beschwerdeführer habe im Jahr 2006 die zu 100% in seinem 
Eigentum stehende Füchsl Touristik GMBH  in eine Einzelfirma umgewandelt.
```

| Prediction | Gold |
|------------|------|
| `Füchsl Touristik GMBH` | `Füchsl Touristik GMBH` |

</details>

---

## `specific_org_dlcg`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bDLCG\s+Bildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 1.000 | 0.002 | 0.005 | 1 | 1 | 0 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 0 | 276 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Des Weiteren wurde keineswegs behauptet, Frau DLCG Bildung  hätte sich „ausreichend 
Informationen" verschafft.
```

| Prediction | Gold |
|------------|------|
| `DLCG Bildung` | `DLCG Bildung` |

</details>

---

## `specific_org_fa_baden`

**F1:** 0.005 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Baden\s+M\xf6dling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.500 | 0.002 | 0.005 | 2 | 1 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 1 | 391 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Vitus Preimesser  in der Beschwerdesache Dipl.-Ing. Zdenko Faiss, 
Fützental 41, 2053 Jetzelsdorf, Österreich, über die Beschwerde vom 15.05.2019 gegen den Bescheid des seinerzeitigen 
Finanzamt Baden Mödling  vom 26.04.2019, betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) 2017, zu Recht erkannt: 
I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
IM NAMEN DER REPUBLI K 
Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden 
Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den 
Finanzstrafsachen gegen  
1. A B, [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich 
2. [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich 
3. [...]., Dr. Wagner-Gasse 35, 8700 Leoben, Österreich 
alle vertreten durch BKS Steuerberatungs GmbH W, Untere 
Hauptstraße 10, 3150 Wilhelmsburg 
wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des 
Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten 
Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates 
beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als 
Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des 
Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H., 
deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt: 
Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates 
aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den 
Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob 
fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der 
belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B 
Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.
```

- FP: `Finanzamt Baden Mödling` (organisation)


</details>

---

## `tax_office_finanzamt_graz_stadt`

**F1:** 0.005 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Content:**
```
\bFinanzamt\s+Graz-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.500 | 0.002 | 0.005 | 2 | 1 | 1 

**Per-Class Breakdown**

| Class | TP | FP | FN |
|-------|----|----|----|
| `organisation` | 1 | 1 | 377 |

</details>

<details>
<summary>✅ Worked (1)</summary>

**Example 1**

```
Mit Bescheid des Finanzamt Graz-Stadt  vom 20.5.2022 wurde der begehrte 
Einkommensteuerbescheid 2020 erlassen.
```

| Prediction | Gold |
|------------|------|
| `Finanzamt Graz-Stadt` | `Finanzamt Graz-Stadt` |

</details>

<details>
<summary>❌ Missed (1)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- Missed: `InnLuftfahrt GMBH` (organisation)


</details>

<details>
<summary>⚠️ False Positives (1)</summary>

```
Mit Haftungsbescheid vom 11.12.2014 zog das Finanzamt Graz-Stadt die InnLuftfahrt GMBH 
gemäß § 82 EStG 1988 zur Haftung für den Lohnsteuermehrbetrag 2009 heran.
```

- FP: `Finanzamt Graz-Stadt` (organisation)


</details>

---

## `specific_org_dias_telekom`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bDIAS\s+Telekom\s+Institut\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bTraunLuftfahrt\s+Solutions\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_manfredo`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bManfredo\s+Herrschmann\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_logkeltal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bLogkeltal\s+Marine\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_steinfurt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSteinfurtglanz-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_berwaldkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bBerwaldkel-M\xf6bel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_waldtra`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bWaldtra-Sicherheit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_gogel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bGogel\s+Daten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_heimwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bHeimwald-Forschung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_bahrdt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bBahrdt\s+Digital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_raiffeisen_wels`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+Wels\s+S\xfc\xdfer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_henken`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bHenken\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_depp`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bDepp\s+Versand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_talkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bTalkel-Versand\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_hebebrand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bHebebrand\s+Recycling\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_rnv`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRNV\s+Digital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_gozcu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bGözcü\s+Getränke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_keltrizor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bKeltrizor\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_unibach`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bUnibach-Getränke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_noruniwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bNoruniwald-Technik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_pfendtner`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bPfendtner\s+Textil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_kraftnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bKraftnex\s+Technologien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_waldver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bWaldver\s+E-Commerce\s+Systeme\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_raiffeisen_hippach`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+Hippach-Hart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_raiffeisen_genburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+genburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_raiffeisen_hall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRaiffeisen\s+Rionalbank\s+Hall\s+in\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_raiffeisen_karnische`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_see_garttalder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSee\s+Garttalder\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_psomadakis`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bPsomadakis\s+Touristik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_trafenfen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bTrafenfen\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_gorius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bGorius\s+und\s+Ziegann\s+Event\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_unter_donunisee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bUnter\s+Donunisee\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_ruterborries`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRüterborries\+Friderich\s+Möbel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_bankhaus_denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bBankhaus\s+Denzel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bNorconheim\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_bauermeister`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bBauermeister\s+Getränke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_hoch_synwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bHoch\s+Synwil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_sophie_wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSophie\s+Wittmeir\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_lexdon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bLexdon\s+IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_wien_waldnor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bWien\s+Waldnor\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_vossbein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bVossbein\s+Lebensmittel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_sudver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSudver\s+Handel\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_glanznorost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bGlanznorost\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_west_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bWest-Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_maegerlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bM\xe4gerlein\s+Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_planung_monuniost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bPlanung\s+Monuniost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_zumholte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bZumholte\s+Verlag\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_simek`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSimek\s+Daten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_dersteintri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bDersteintri-Versicherung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_oina`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bOINA\s+Solar\s+Institut\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_gemke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bGemke\+Gamper\s+Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_kornfelder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bKornfelder\s+Recycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_raiffeisen_kasse_hyphen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenkasse\s+[A-Z][a-zA-Z]+(?:\s+-\s+[A-Z][a-zA-Z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_cervenka`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bCervenka&Neun\xfc\xbbel\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_lubomir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bLubomir\s+Merschmeyer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_textil_steingartlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bTextil\s+Steingartlog\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_osttechnik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bOstTechnik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_maschinenbau_derwilsee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bMaschinenbau\s+Derwilsee\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_fensudlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bFensudlog\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_sud_sudwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSüd\s+Sudwil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_kelgart_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bKelgart-Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_greiner_mai`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bGreiner-Mai\s+Event\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_technik_ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bTechnik\s+Ostbachal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_traunlandwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bTraunLandwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_getraenke_nexdorfzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bGetränke\s+Nexdorfzor\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_kok_heberlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bKök\s+&\s+Heberlein\s+Bau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_seenorder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSeeNorderE\u2011Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_volkswien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bVOLKSBANK\s+WIEN\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_donau_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bDonau-Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_nkah`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bNKAH\s+Luftfahrt\s+Vertrieb\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_olivier`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bOlivier\s+u\.\s+Bartha\s+Recycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_hagdorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bHagdorn\s+Robotik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_istvan`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bIstvan\s+Gerart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_paweltschik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bPaweltschik\s+Telekom\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_schneppensieper`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bSchneppensieper\s+&\s+B\xfc\x9ftbrunne\s+Touristik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_touristik_wildon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bTouristik\s+Wildon\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_bawag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bBAWAG\s+P\.S\.K\.\s+Wohnbaubank\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_lognex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bLognex-IT\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_kira_hackbardt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bKira\s+Hackbardt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_nordtraval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bNordTravalUmwelt\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRosilius\s+Pflege\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_hochlebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bHochLebensmittel\s+Holding\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bYavasoglu\s+Analyse\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_mur_alver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_zoruniglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bZoruniglanz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_logseemon_metall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bLogseemon-Metall\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_raiffeisen_rion`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bRaiffeisenbank\s+Rion\s+V\xf6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_luehrig_hundertmarck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bLuehrig\s+\+\s+Hundertmarck\s+Holz\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_wildorftra`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bWildorftra\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_orgbruckmonwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bBruckmonwil\s+Digital\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bS\xfc\xd6rt\s+Versand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_logal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bLogal\s+Gruppe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

## `specific_org_norddaten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Content:**
```
\bNordDaten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Matches | TP | FP 
|-----------|--------|----|---------|----|----
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 

</details>

---

</details>

---

