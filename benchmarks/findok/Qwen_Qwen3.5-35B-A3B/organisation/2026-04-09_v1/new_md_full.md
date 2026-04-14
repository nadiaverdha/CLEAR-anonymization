# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-14T17:01:44.585814

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config benchmarks/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-09_v1config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training examples | 1031 |
| Validation examples | 258 |
| Test examples | 788 |
| Train annotations | 1257 |
| Validation annotations | 325 |
| Test annotations | 3543 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 50 |
| Refinement iterations | 2 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | False |
| Enable Prune | False |
| Critic Interval | 0 |
| Audit Interval | 0 |
| Use GREX | True |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 79.7% |
| True Positives | 459 |
| False Positives | 321 |
| Micro Precision | 58.8% |
| Micro Recall | 84.4% |
| Micro F1 | 69.3% |
| Macro F1 | 69.3% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `specific_org_annemie_bott` | 9.8% | 100.0% | 5.1% | 28 | 28 | 0 |
| `specific_org_stadte_energie` | 1.5% | 100.0% | 0.7% | 4 | 4 | 0 |
| `specific_org_milan` | 18.7% | 100.0% | 10.3% | 56 | 56 | 0 |
| `specific_org_manfredo` | 4.0% | 100.0% | 2.0% | 11 | 11 | 0 |
| `specific_org_enns` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_steinfurt` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_gogel` | 1.1% | 100.0% | 0.6% | 3 | 3 | 0 |
| `specific_org_hoerup_ag` | 1.5% | 100.0% | 0.7% | 4 | 4 | 0 |
| `specific_org_bahrdt` | 2.5% | 100.0% | 1.3% | 7 | 7 | 0 |
| `specific_org_rnv` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_reinemut` | 7.1% | 100.0% | 3.7% | 20 | 20 | 0 |
| `specific_org_waldtouristik` | 1.8% | 100.0% | 0.9% | 5 | 5 | 0 |
| `specific_org_fa_salzburg` | 10.8% | 100.0% | 5.7% | 31 | 31 | 0 |
| `specific_org_fa_deutschlandsberg` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_keltrizor` | 1.8% | 100.0% | 0.9% | 5 | 5 | 0 |
| `specific_org_pastel` | 9.1% | 100.0% | 4.8% | 26 | 26 | 0 |
| `specific_org_leiss` | 4.7% | 100.0% | 2.4% | 13 | 13 | 0 |
| `specific_org_pfendtner` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_raiffeisen_hall` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_see_garttalder` | 1.1% | 100.0% | 0.6% | 3 | 3 | 0 |
| `specific_org_psomadakis` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_krolitzki` | 3.3% | 100.0% | 1.7% | 9 | 9 | 0 |
| `specific_org_okur` | 7.8% | 100.0% | 4.0% | 22 | 22 | 0 |
| `specific_org_klein_vorholt` | 1.5% | 100.0% | 0.7% | 4 | 4 | 0 |
| `specific_org_zumholte` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_dgcv_ecommerce` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_laskowsky` | 1.1% | 100.0% | 0.6% | 3 | 3 | 0 |
| `specific_org_kok_heberlein` | 4.3% | 100.0% | 2.2% | 12 | 12 | 0 |
| `specific_org_volkswien` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_donau_druck` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_gronemeier` | 2.5% | 100.0% | 1.3% | 7 | 7 | 0 |
| `specific_org_ugqq` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_wod_sicherheit` | 2.9% | 100.0% | 1.5% | 8 | 8 | 0 |
| `tax_office_finanzamt_grieskirchen` | 7.4% | 100.0% | 3.9% | 21 | 21 | 0 |
| `tax_office_finanzamt_schwechat` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_fa_purkersdorf` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_fa_vorarlberg` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `specific_org_fa_tirol_ost` | 1.8% | 100.0% | 0.9% | 5 | 5 | 0 |
| `specific_org_mur_alver` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_zoruniglanz` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `specific_org_luehrig_hundertmarck` | 1.1% | 100.0% | 0.6% | 3 | 3 | 0 |
| `specific_org_celikkanat_garten` | 8.1% | 100.0% | 4.2% | 23 | 23 | 0 |
| `tax_office_fa` | 23.0% | 80.2% | 13.4% | 91 | 73 | 18 |
| `specific_org_fa_judenburg` | 1.5% | 80.0% | 0.7% | 5 | 4 | 1 |
| `tax_office_fa_graz_stadt` | 1.5% | 80.0% | 0.7% | 5 | 4 | 1 |
| `specific_org_fa_waldviertel` | 0.4% | 50.0% | 0.2% | 2 | 1 | 1 |
| `company_gmbh_general` | 3.5% | 50.0% | 1.8% | 20 | 10 | 10 |
| `specific_org_fa_braunau_ried_schärding` | 0.4% | 50.0% | 0.2% | 2 | 1 | 1 |
| `tax_office_finanzamt` | 19.1% | 45.2% | 12.1% | 146 | 66 | 80 |
| `tax_office_finanzamt_graz_stadt` | 0.4% | 25.0% | 0.2% | 4 | 1 | 3 |
| `specific_org_fa_gmunden` | 0.4% | 20.0% | 0.2% | 5 | 1 | 4 |
| `specific_org_fa_baden` | 0.7% | 18.2% | 0.4% | 11 | 2 | 9 |
| `specific_org_fa_wien` | 0.4% | 16.7% | 0.2% | 6 | 1 | 5 |
| `company_ag_general` | 2.2% | 8.0% | 1.3% | 87 | 7 | 80 |
| `company_kg_general` | 2.1% | 5.5% | 1.3% | 127 | 7 | 120 |
| `specific_org_dias_telekom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_finanzen_tradonnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_traunluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_houdek` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_mur` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_klusner` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_schmeltz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_starker` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_yxtg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_logkeltal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_berwaldkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_waldtra` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_heimwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_wels` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_nowothnig` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_henken` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_roelfsen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_dorfcon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_depp` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_talkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_hebebrand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_wienerwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_bezirksgericht` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `specific_org_unterrecycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_talverwerk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_dufel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_gozcu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_chen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_lexkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_unibach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_noruniwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_kraftnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_waldver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_pastl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_hippach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_genburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_karnische` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_trafenfen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_gorius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_unter_donunisee` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_ruterborries` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_bankhaus_denzel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_bauermeister` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_hoch_synwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_sophie_wittmeir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_schoenfelder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_lexdon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_alal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_wien_waldnor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_vossbein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_event_sudkraftlex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_kqpc` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_sudver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_glanznorost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_west_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_maegerlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_planung_monuniost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_gartgart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_kraftver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_simek` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_dersteintri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_oina` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_gemke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_kornfelder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_sanitar` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_kasse_hyphen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_cervenka` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_lubomir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_textil_steingartlog` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_oberrecycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_osttechnik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_nord_kellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_maschinenbau_derwilsee` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_innluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_fensudlog` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_inn_monost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_sud_sudwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_kelgart_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_greiner_mai` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_technik_ostbachal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_traunlandwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_getraenke_nexdorfzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_zschieschank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_mullbrandt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_seenorder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_hudec_christian` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_nkah` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_olivier` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_hagdorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_istvan` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_paweltschik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_schneppensieper` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_touristik_wildon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_bawag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_lognex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_kira_hackbardt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_nordtraval` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_rosilius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_hochlebensmittel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_verdonlex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_bierwerth` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_bludszat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_office_fa_schwechat_gmunden` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_logseemon_metall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_mittelheizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_traun_digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_vahrenkamp` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_rion` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_dufel_technik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_raiffeisen_hyphen` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `specific_org_fuchsl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_wildorftra` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_orgbruckmonwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_sudversand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_logal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_norddaten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_org_dlcg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `specific_org_milan`

**F1:** 0.187 | **Precision:** 1.000 | **Recall:** 0.103  

**Format:** `regex`  
**Description:**
Matches 'Milan H\xe4ndlein'.

**Content:**
```
\bMilan\s+H\xe4ndlein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.103 | 0.187 | 56 | 56 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 0 | 484 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Verfahren wie folgt: 
 a) Sachverhalt und Verfahrensablauf bei der <<<Milan Händlein>>>, Str.Nr. 79-810/8442, BV 24: 
Das Unternehmen <<<Milan Händlein>>> ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... <<<Milan Händlein>>>, Str.Nr. 79-810/8442, BV 24: 
Das Unternehmen <<<Milan Händlein>>>  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen. ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... die Nachfolgejahre wurden folgende 
Umgründungsschritte bei <<<Milan Händlein>>>  durchgeführt: 
Auf Grundlage des Spaltungs- und Übernahmsvertrages ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die <<<Milan Händlein>>> 
mit Stichtag 31.12.2007 als übertragende Gesellschaft nach ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... Beratung  verschmolzen worden. 
Zum Stichtag 31.12.2008 ist die <<<Milan Händlein>>>  mit dem verbliebenen Vermögen entsprechend 
dem Umgründungsplan ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

</details>

---

## `specific_org_fa_salzburg`

**F1:** 0.108 | **Precision:** 1.000 | **Recall:** 0.057  

**Format:** `regex`  
**Description:**
Matches 'FA Salzburg-Stadt'.

**Content:**
```
\bFA\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.057 | 0.108 | 31 | 31 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 31 | 0 | 346 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... über die Beschwerde vom 13. Juli 2023 gegen den Bescheid des 
<<<FA Salzburg-Stadt>>>  vom 19. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 1**

```
... nicht zulässig. 
 
Entscheidungsgründe 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 in Großbritannien errichtete 
Gesellschaft ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
...
Unterhaltungsmedien und Wetten. Das Online Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Registrierungsadresse in Österreich mit 15. September 2019 
geschlossen. 
<<<FA Salzburg-Stadt>>>  ist für das Betreiben der Website, das Einrichten und die ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 2**

```
... über die Beschwerde vom 18. Mai 2021 gegen den Bescheid des <<<FA Salzburg-Stadt>>> 
vom 17. Mai 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

</details>

---

## `specific_org_annemie_bott`

**F1:** 0.098 | **Precision:** 1.000 | **Recall:** 0.051  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Annemie Bott'.

**Content:**
```
\bAnnemie\s+Bott\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.051 | 0.098 | 28 | 28 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 0 | 512 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Beschwerdesache  
1) PhD Marianne Yener  als Rechtsnachfolger der <<<Annemie Bott>>>,  Schäfergasse 5, 3613 Marbach an der Kleinen Krems, Österreich, ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (<<<Annemie Bott>>> 
St. Nr. 64-207/8107) und das Verfahren wiederaufgenommen. ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... wiederaufgenommen.  Bescheidadressaten waren 
sowohl das Gruppenmitglied <<<Annemie Bott>>>  als auch der Gruppenträger StadtEnergie Holding 
(28-587/0533). ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... Generalversammlungsbeschlusses vom 
19.08.2009 eine Abspaltung zur Aufnahme in die <<<Annemie Bott>>>  durch Übertragung des 
gesamten Betriebes (mit Ausnahme der ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... Positionen) erfolgt. Die Grönemeier&Hövelberndt E‑Commerce  und 
<<<Annemie Bott>>>  sind aufgrund der dargestellten Umgründungsschritte (partielle) ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

</details>

---

## `specific_org_pastel`

**F1:** 0.091 | **Precision:** 1.000 | **Recall:** 0.048  

**Format:** `regex`  
**Description:**
Matches 'Pastel Pharma'.

**Content:**
```
\bPastel\s+Pharma\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.048 | 0.091 | 26 | 26 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 0 | 155 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Dieter Fröhlich über die 
Bescheidbeschwerde vom 12.10.2017 der <<<Pastel Pharma>>>, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
... Bundesminister für Finanzen und führte 
dazu aus: 
„Die Firma <<<Pastel Pharma>>>  betreibt ein Wettbüro und schließt Wetten überwiegend über ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
... Forderungen bis zur 
Höhe des negativen Eigenkapitals verzichte. Die <<<Pastel Pharma>>>  ist zu 100% an der BB. mit Sitz in 
Curacao beteiligt. Die ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
... Appendix A dieser 
Unterlage ist eine vorläufige Lizenz auch der <<<Pastel Pharma>>>  Austria unter den Internetmarken 
(Internet-Plattformen) www.xx.com ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
...
Gesetzen von Curacao unterliegen und der Vertag zwischen der <<<Pastel Pharma>>>  Eood (mit Sitz in 
Bulgarien, Sofia) und dem Endkunden zustande ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

</details>

---

## `specific_org_celikkanat_garten`

**F1:** 0.081 | **Precision:** 1.000 | **Recall:** 0.042  

**Format:** `regex`  
**Description:**
Matches 'Celikkanat Garten' (without GmbH in this context).

**Content:**
```
\bCelikkanat\s+Garten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.042 | 0.081 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 246 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Ort,  
3. Okur Automotive  GmbH & Co KG, Straße3, Ort und 
4. <<<Celikkanat Garten>>>  GmbH & Co KG, Straße3, Ort, 
alle vertreten durch yy Wirtschaftstreuhand ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
... zzgl. Sonderbetriebsausgaben in Höhe von -€ 258.374,89), 
4. <<<Celikkanat Garten>>>  GmbH & Co KG: ein Betrag von -€ 1.527.464,40 (Verlustzuweisung ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
... Betrag von € 2.470.000,00 zu 
berücksichtigen sind) und 
4. <<<Celikkanat Garten>>>  GmbH & Co KG: € -1.387.500,00 (wobei bei der Veranlagung der ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
...
Verkehrswertzusammenschluss mit Buchwertfortführung gem. Art IV UmgrStG. 
 <<<Celikkanat Garten>>>  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 4. ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
... „Errichtung stille Gesellschaft“ - 
Okur Automotive  GmbH & Co KG und <<<Celikkanat Garten>>>  GmbH & Co KG 
 Zusammenschlussvertrag - Okur Automotive  ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `company_kg_general`

**F1:** 0.021 | **Precision:** 0.055 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches generic company names ending in 'KG', ensuring the name starts with a capitalized word and has at least one preceding word, excluding common non-entity prefixes.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)+\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.055 | 0.013 | 0.021 | 127 | 7 | 120 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 120 | 536 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Beschwerdeführer (kurz: Bf.) war im Jahr 2018 zu 60% an der <<<WOD Sicherheit KG>>>  und zu 33,33% an 
der Zumholte Verlag OG  beteiligt. Unternehmensgegenstand ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... stellte das Finanzamt die gemeinschaftlichen Einkünfte 2018 der 
<<<WOD Sicherheit KG>>>  mit 48.094,37 Euro und den auf die Beteiligung an der KG entfallenden ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
...
2018 ein, er habe die Einkünfte aus seiner Beteiligung an der <<<WOD Sicherheit KG>>>  im Jahr 2018 nicht 
mehr erhalten, weshalb dieser Anteil in ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... Zuflussprinzip zu beachten. Im Jahr 2018 seien ihm 
keine Einnahmen der <<<WOD Sicherheit KG>>>  zugeflossen, weswegen diese auch nicht der 
Einkommensteuer ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... erneut, die anteiligen 
Einkünfte von der Beteiligung an der <<<WOD Sicherheit KG>>>  2018 aus der Einkommensteuerfestsetzung 
auszunehmen.  
Am ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Schroateck 20, 8342 Ebersdorf, Österreich, vertreten durch <<<HD Steuerberater GmbH & Co KG>>>, Höchster 
Str. 51a, 6972 Fußach, über die Beschwerde vom 19. ...
```

FP: `HD Steuerberater GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Techn R Silke Altpeter` (person)
- `Schroateck 20, 8342 Ebersdorf, Österreich` (address)

**Example 1**

**False Positives:**

```
...
Verlustanteil von 3.111,10 € aus einer Beteiligung des IS an der <<<XY Holding GmbH & Co KG>>>, 
FN 777777a, StNr 77-777/7777a (nachfolgend XY- KG) enthalten, ...
```

FP: `XY Holding GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz.in Milena Cofala` (person)
- `Kira Junggunst` (person)
- `Kreuzbichlstraße 15k, 4890 Unterrain, Österreich` (address)
- `93-986/8725` (tax_number)
- `FA Klosterneuburg` (organisation)

**Example 2**

**False Positives:**

```
... Rittschein, Österreich, vertreten durch Copilot Unternehmens- und <<<Steuerberatungs 
GmbH & Co KG>>>, Littrowgasse 7, 1180 Wien, über folgende Beschwerden gegen ...
```

FP: `Steuerberatungs 
GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Karsten Busatis` (person)
- `Lungaweg 96, 8333 Breitenfeld an der Rittschein, Österreich` (address)
- `34-796/1007` (tax_number)
- `Karsten Busatis` (person)

**Example 3**

**False Positives:**

```
... Außerbergweg 6, 4451 Sand, Österreich, vertreten durch HLB Prüf-<<<Treuhand GmbH & Co KG>>>, Berggasse 16, 
1090 Wien, über die Beschwerde vom 3. November ...
```

FP: `Treuhand GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Dagobert Schimmack` (person)
- `Außerbergweg 6, 4451 Sand, Österreich` (address)
- `07-354/5950` (tax_number)

**Example 4**

**False Positives:**

```
... ob dieses Vorbringen den Tatsachen entspricht oder 
nicht.  
<<<Die WOD Sicherheit KG>>>  hat ihren Gewinn nach § 4 Abs. 3 EStG 1988 ermittelt. Wird ...
```

FP: `Die WOD Sicherheit KG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Hagen Jorkuweit` (person)
- `Priv.-Doz.in Catharina Tenner` (person)
- `Dr. Adolf Bastl` (person)
- `Mag. Andreas Pritzkat` (person)
- `PhD Marcel Kizilpinar, MSc` (person)
- `Hohen 73, 5133 Lohnsberg, Österreich` (address)
- `WOD Sicherheit KG` (organisation)
- `Zumholte Verlag OG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `Zumholte Verlag OG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)

</details>

---

## `company_ag_general`

**F1:** 0.022 | **Precision:** 0.080 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches generic company names ending in 'AG', ensuring the name starts with a capitalized word.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)*\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.080 | 0.013 | 0.022 | 87 | 7 | 80 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 80 | 537 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
...
gemäß § 41 Abs 1 Z 2 vor, weil sich die lohnsteuerpflichtigen <<<ZYJY Automotive AG>>>  GmbH sowie 
NYJ Event AG  GmbH zwar überschneiden würden, ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... sich die lohnsteuerpflichtigen ZYJY Automotive AG  GmbH sowie 
<<<NYJ Event AG>>>  GmbH zwar überschneiden würden, der Gesetzwortlaut verlange ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... Tatbestandsmerkmal des § 41 Abs 1 Z 12 vor. Im Zuge der 
Lohnverrechnung/<<<Kubzyk Elektro AG>>>  GmbH sei der ganze Familienbonus Plus ausbezahlt worden, 
...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... Arbeit-/Auftraggeber Betrag 
Lohnzettel 84(1) 01.01.-15.09. <<<Kubzyk Elektro AG>>>  GmbH € 17.356,99 
Meldung 3(2) 19.09.-02.10. Arbeitsmarktservice ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... Arbeitsmarktservice Österreich € 507,22 
Lohnzettel 84(1) 24.09.-31.12. <<<ZYJY Automotive AG>>>  GmbH € 1.058,79 
Lohnzettel 84(1) 03.10.-31.12. NYJ Event ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

**Example 1**

```
... zwischen der beschwerdeführenden Partei als Arbeitnehmer und der <<<Heimwil Transport AG>>>  als 
3 von 6
Seite 4 von 6 
 
 
Arbeitgeberin sowie den Angaben ...
```

| Predicted | Gold |
|---|---|
| `Heimwil Transport AG` | `Heimwil Transport AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Abschlusszahlung B 
Sachverhalt: 
Im WJ 2013/2014 wurden sämtliche vom <<<Konzern AG>>> gehaltenen Anteile an der OÖ. A AG (C) 
an deren Hauptgesellschafter ...
```

FP: `Konzern AG` (organisation)

```
... betreffende Gewinnverteilungsbeschluss kann durch den alleinigen <<<Gesellschafter AG>>> nach 
Feststellung der Bilanz B per 30.9.2014 erst Ende 2014 ...
```

FP: `Gesellschafter AG` (organisation)

```
... Juni 2014 bereits durchgeführt wurde. Im Übrigen waren diese <<<Zahlungen Seitens 
AG>>> jedenfalls zu leisten, auch wenn kein entsprechender Gewinn ...
```

FP: `Zahlungen Seitens 
AG` (organisation)

```
... Beteiligung. In wirtschaftlicher 
Betrachtungsweise wurde der <<<Erwerberin AG>>> zugestanden, diesen Restkaufpreis aus der dieser 
ausschließlich ...
```

FP: `Erwerberin AG` (organisation)

```
... übertragen wurde. Dieser 
bis dahin zukünftig der alleinigen <<<Gesellschafterin AG>>> zufließende Wertzuwachs der Beteiligung 
B sollte der Verkäuferin ...
```

FP: `Gesellschafterin AG` (organisation)

**✅ Gold Entities:**
- `Veronika Cuerten, Bakk. phil.` (person)
- `Schöglerstraße 1, 9612 Bach, Österreich` (address)

**Example 1**

**False Positives:**

```
... nach Rückkauf einer fondsgebundenen 
Lebensversicherung der X <<<Versicherungs AG>>> zum 01.05.2014 mit laufender gleichbleibender 
Prämienzahlung ...
```

FP: `Versicherungs AG` (organisation)

```
... Zuge des Ermittlungsverfahrens vor dem Finanzamt teilte die X <<<Lebensversicherungs AG>>> im 
Schreiben vom 29.12.2014 mit, dass es sich im gegenständlichen ...
```

FP: `Lebensversicherungs AG` (organisation)

```
... Tilgungsträger einer 
gleichlaufenden endfälligen Finanzierung bei der Y <<<Bank AG>>> zu deren Gunsten verpfändet 
worden. Durch die für den Kreditnehmer ...
```

FP: `Bank AG` (organisation)

```
... Vertragsbeginn in Höhe von 52.000 € beantragt. Lt. Angaben der X 
<<<Lebensversicherungs AG>>> handelt es sich deshalb nicht um laufende, im Wesentlichen ...
```

FP: `Lebensversicherungs AG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz.in Maria van Birgelen` (person)
- `Leif Bartheld` (person)
- `Arlenweg 4X, 5261 Haslau, Österreich` (address)

**Example 2**

**False Positives:**

```
... nur ein Viertel 
des Bezuges der X Österreich und jener der Y <<<Pensions AG>>> als ganzjähriger Bezug 
auszuscheiden. Es komme jedoch die ...
```

FP: `Pensions AG` (organisation)

```
... steuerpflichtige 
Einkünfte bezogen:  
Firmenkassenpension der Y <<<Pension AG>>> von 1.1. – 31.12.2019 
Berufsunfähigkeitspension PVA 1.2. – ...
```

FP: `Pension AG` (organisation)

```
...
Tarif zu versteuernde Bezüge: 
X 1.1. – 30.4.2019 17.416,52 
Y <<<Pension AG>>>  1.1. – 31.12.2019 2.688,00 
Pensionsversicherungsanstalt 28.11.2019 ...
```

FP: `Pension AG` (organisation)

```
... gegenständlichen Fall betrifft dies 
ausschließlich die Bezüge der Y <<<Pension AG>>>. Diese Bezüge von 2.688,00 Euro hat das Finanzamt 
bei Berechnung ...
```

FP: `Pension AG` (organisation)

```
... steuerfreien Arbeitslosengeldes) zuerst um die 
Bezüge der Y <<<Pension AG>>> und um den Jänner-Bezug der X zu vermindern und der verbleibende ...
```

FP: `Pension AG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz.in Franka Münchsmayer` (person)
- `Henriette Dempwolf` (person)
- `Hopfersbach 30, 4730 Lindbruck, Österreich` (address)
- `48-249/3886` (tax_number)
- `Henriette Dempwolf` (person)

**Example 3**

**False Positives:**

```
... Finanzamt mittels RSb versandt und von der 
Österreichischen <<<Post AG>>> der Bf. an ihrer Geschäftsanschrift am 4.3.2021 zugestellt. ...
```

FP: `Post AG` (organisation)

```
... ergibt 
sich aus dem zu den Akten liegenden Zustellnachweis der <<<Post AG>>> vom 4.3.2021. 
1 von 7
Seite 2 von 7 
 
 
Mit Schreiben vom ...
```

FP: `Post AG` (organisation)

**✅ Gold Entities:**
- `Laurentia Schnellert` (person)
- `Balzerlen 15l, 9334 Guttaringberg, Österreich` (address)

**Example 4**

**False Positives:**

```
... zustehe. Zusätzlich legte er eine Quittung der Österreichische <<<Post AG>>> vom 
11.11.2019 über einen per Einschreiben versendeten Brief ...
```

FP: `Post AG` (organisation)

```
... Quittung vom 11.11.2019 auch ein Schreiben der Österreichische <<<Post AG>>> vom 
24.2.2020 betreffend Nachforschung zur Aufgabenummer Nr. ...
```

FP: `Post AG` (organisation)

```
... Aufgabenummer 
Nr. mit dem vorgelegten Schreiben der Österreichische <<<Post AG>>> vom 24.2.2020 erbracht 
worden sei. Ob bzw. welche Dokumente/Unterlagen ...
```

FP: `Post AG` (organisation)

```
...
Beschwerde) mit dem vorgelegten Schreiben der Österreichische <<<Post AG>>> vom 24.2.2020 
gelungen sei. 
Das Bundesfinanzgericht teilt ...
```

FP: `Post AG` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof.in Mag.a Brunhild Stieglmaier` (person)
- `Bühelstauden 7, 4030 Linz, Österreich` (address)
- `40-192/1103` (tax_number)

</details>

---

## `tax_office_finanzamt`

**F1:** 0.191 | **Precision:** 0.452 | **Recall:** 0.121  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by specific known locations. Removed restrictive negative lookahead to allow 'vom' and dates.

**Content:**
```
\bFinanzamt\s+(?:Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Wien\s+8/16/17|Salzburg-Stadt|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Amstetten\s+Melk\s+Scheibbs|Steiermark\s+Mitte|\d+/?\d+|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Tirol\s+Ost|Nieder\xf6sterreich\s+Mitte|Grieskirchen\s+Wels|Linz|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Klosterneuburg|Salzburg-Land|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Purkersdorf|Vorarlberg|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Waldviertel|Oststeiermark|Spittal\s+Villach|Gmunden\s+V\xf6cklabruck|Wien\s+1/23|Wien\s+8/16/17|Steiermark\s+Mitte|Nieder\xf6sterreich\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Amstetten\s+Melk\s+Scheibbs|Grieskirchen\s+Wels|Gmunden\s+V\xf6cklabruck|Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Purkersdorf|Vorarlberg|Waldviertel|Oststeiermark|Spittal\s+Villach|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+8/16/17|Graz-Stadt|Salzburg-Stadt|Salzburg-Land|Judenburg\s+Liezen|Klosterneuburg|Freistadt\s+Rohrbach\s+Urfahr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)(?!\s+vom|\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.452 | 0.121 | 0.191 | 146 | 66 | 80 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 66 | 80 | 478 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
...
gegen den zur Steuernummer 28-115/0315  ergangenen Bescheid des <<<Finanzamt Deutschlandsberg Leibnitz Voitsberg>>> (FA) vom 
11. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Deutschlandsberg Leibnitz Voitsberg` | `Finanzamt Deutschlandsberg Leibnitz Voitsberg` |

**Example 1**

```
... folgt eine zahlenmäßige Darstellung)  
Am 26.04.2013 erließ das <<<Finanzamt Grieskirchen Wels>>>  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
...
RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des <<<Finanzamt Grieskirchen Wels>>>  gegenüber der 
mitbeteiligten Partei Annemie Bott (als partiellen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... eingereicht. 
Unmittelbar nachfolgend hat das BFG die Amtsrevision des <<<Finanzamt Grieskirchen Wels>>> (samt Veranlagungsakten 
sowie Auszügen aus dem Arbeitsbogen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die 
Amtsrevision des <<<Finanzamt Grieskirchen Wels>>>  als unbegründet abgewiesen. Der VwGH formulierte die 
9 von ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... betragsmäßig verbindlich wird. Begründend 
wurde deshalb durch das <<<Finanzamt Grieskirchen Wels>>>  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 2**

```
... Dr. Walter Ganster, Steuerberater in 9100 
Völkermarkt und <<<Finanzamt Schwechat Gerasdorf>>>  als Amtspartei und als Gesamtrechtsnachfolger des Finanzamtes ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Example 3**

```
... August 2017 
gegen den Bescheid des Finanzamtes F (nunmehr: <<<Finanzamt Klagenfurt St. Veit Wolfsberg>>>) vom 2. Juni 2017 betreffend 
Körperschaftsteuer 2016 zu Steuernummer ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | `Finanzamt Klagenfurt St. Veit Wolfsberg` |

**Example 4**

```
... Großbritannien errichtete 
Gesellschaft mit Sitz in Kranzing. <<<Finanzamt Salzburg-Stadt>>>  betreibt Geschäfte in den Bereichen 
Unterhaltungsmedien und ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
... erreichbar, welche unter anderem auch in Österreich verfügbar 
ist. <<<Finanzamt Salzburg-Stadt>>>  hält eine Wettlizenz des Vereinigten Königreichs. 
KommR Ing. ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
...
KommR Ing. Roberta Gossling  Limited ist eine im Jahr 2007 von <<<Finanzamt Salzburg-Stadt>>>  Ltd. gegründete Gesellschaft. Das 
Unternehmen ist in Großbritannien ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
...
Online Wettprodukte des Unternehmens waren unter der Website www.<<<Finanzamt Salzburg-Stadt>>> .com 
erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
... Wette auf den Ausgang der Lotterien erteilt der Teilnehmer <<<Finanzamt Salzburg-Stadt>>>  den 
Auftrag, die entsprechende Wette an KommR Ing. Roberta ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Einreichung der 
Umsatzsteuererklärung 2018 am 15.5.2019 beim <<<Finanzamt Graz-Stadt>>>, wurde die Frist für den 
Antrag auf Erstattung von Vorsteuern ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

```
... Anträge auf Erstattung von Vorsteuern zuständigen Behörde 
(<<<Finanzamt Graz-Stadt>>>) eingebracht. 
Weiters ist anzumerken, wenn die Behörde die ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

```
... 
Erstattung mittels amtlich vorgeschriebenem Vordruck beim <<<Finanzamt Graz-Stadt>>> zu 
beantragen. Der Antrag ist binnen sechs Monaten nach Ablauf ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

**✅ Gold Entities:**
- `Dr.in Constanze Peest` (person)
- `Linn Damianou` (person)
- `Fürnbergstraße 3, 4730 Steinparz, Österreich` (address)
- `Finanzamt Salzburg-Land` (organisation)
- `39-261/4216` (tax_number)

**Example 1**

**False Positives:**

```
... den 
Abweisungsbescheid des Finanzamtes Österreich (bisher <<<Finanzamt St. Johann Tamsweg Zell 
am See>>>) vom 6. August 2019 betreffend Familienbeihilfe für den Zeitraum ...
```

FP: `Finanzamt St. Johann Tamsweg Zell 
am See` (organisation)

**✅ Gold Entities:**
- `Heinrich Röskens` (person)
- `Kleinhofstraße 36, 2640 Pettenbach, Österreich` (address)

**Example 2**

**False Positives:**

```
... Gmunden“ gerichtete 
Vorlageantrag am 28. Dezember 2018 beim <<<Finanzamt Gmunden Vöcklabruck>>> einlangte, dieses 
Finanzamt jedoch sachlich und örtlich unzuständig ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

```
... Marxergasse 4, 4810 Gmunden“ und wurde 
am selben Tag beim <<<Finanzamt Gmunden Vöcklabruck>>> in Gmunden persönlich durch Einwurf in 
die „ Postbox“ der ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

```
... wurde der Vorlageantrag – zuständigkeitshalber - durch das <<<Finanzamt Gmunden 
Vöcklabruck>>> an das „Finanzamt für Gebühren und Verkehrsst. Marxerg. 4 1030 ...
```

FP: `Finanzamt Gmunden 
Vöcklabruck` (organisation)

```
... seinem sachlich und örtlich zuständigen Finanzamt (in dem 
Fall <<<Finanzamt Bruck Eisenstadt Oberwart>>>) fristwahrend abgeben. Soweit ihm Finanzonline 
7 von 10
Seite ...
```

FP: `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

```
... wird die Behörde im Adressfeld durch das weiterleitende Amt (<<<Finanzamt 
Gmunden Vöcklabruck>>>) selbst mit „Finanzamt für Gebühren u Verkehrsst“ bezeichnet. ...
```

FP: `Finanzamt 
Gmunden Vöcklabruck` (organisation)

**✅ Gold Entities:**
- `Ing. OMedR Albert Voulgaridou` (person)
- `Patriasdorfer Straße 4, 9634 Katlingberg, Österreich` (address)
- `07-334/2610` (tax_number)

**Example 3**

**False Positives:**

```
... hat. 
In der Zwischenzeit hat er sowohl der SVS als auch dem <<<Finanzamt Linz>>>, bei welchem er als 
beschränkt Steuerpflichtiger noch zu veranlagen ...
```

FP: `Finanzamt Linz` (organisation)

```
... veranlagen war, sämtliche Unterlagen übermittelt, jedoch 
ist es dem <<<Finanzamt Linz>>> nicht möglich, die zu Unrecht einbehaltene österreichische ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**
- `Viktoria Schreitmueller` (person)
- `Wolkersdorfer Weg 9q, 5223 Kuglberg, Österreich` (address)
- `18-890/9416` (tax_number)

**Example 4**

**False Positives:**

```
... 2020 gegen den Bescheid des 
Finanzamtes Österreich (vormals <<<Finanzamt Baden Mödling>>>) vom 13. November 2020 
betreffend Einkommensteuer 2015, Steuernummer ...
```

FP: `Finanzamt Baden Mödling` (organisation)

**✅ Gold Entities:**
- `Lara Pfeiferl` (person)
- `Obernbergerstraße 76, 8253 Schrimpf, Österreich` (address)
- `85-636/8182` (tax_number)

</details>

---

## `tax_office_fa`

**F1:** 0.230 | **Precision:** 0.802 | **Recall:** 0.134  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by specific known locations. Removed restrictive negative lookahead to allow 'vom' and dates.

**Content:**
```
\bFA\s+(?:Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Wien\s+8/16/17|Salzburg-Stadt|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Amstetten\s+Melk\s+Scheibbs|Steiermark\s+Mitte|\d+/?\d+|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Tirol\s+Ost|Nieder\xf6sterreich\s+Mitte|Grieskirchen\s+Wels|Linz|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Klosterneuburg|Salzburg-Land|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Purkersdorf|Vorarlberg|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Waldviertel|Oststeiermark|Spittal\s+Villach|Gmunden\s+V\xf6cklabruck|Wien\s+1/23|Wien\s+8/16/17|Steiermark\s+Mitte|Nieder\xf6sterreich\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Amstetten\s+Melk\s+Scheibbs|Grieskirchen\s+Wels|Gmunden\s+V\xf6cklabruck|Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Purkersdorf|Vorarlberg|Waldviertel|Oststeiermark|Spittal\s+Villach|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+8/16/17|Graz-Stadt|Salzburg-Stadt|Salzburg-Land|Judenburg\s+Liezen|Klosterneuburg|Freistadt\s+Rohrbach\s+Urfahr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)(?!\s+vom|\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.802 | 0.134 | 0.230 | 91 | 73 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 73 | 18 | 471 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle 
des <<<FA Klosterneuburg>>> ) vom 13. Dezember 2019 betreffend Einkommensteuer 2011 zu ...
```

| Predicted | Gold |
|---|---|
| `FA Klosterneuburg` | `FA Klosterneuburg` |

**Example 1**

```
... Milan Händlein. 
Im Wirtschaftsjahr 2007 ist gemäß der beim <<<FA Grieskirchen Wels>>>  eingereichten 
Körperschaftsteuererklärung 2007 ein steuerlicher ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... 31.05.2013 beigelegt). Mit Vorlagebericht vom 13.11.2013 hat das <<<FA Grieskirchen Wels>>> 
die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... Linz, vom 27.01.2016, GZ 
RV/5101064/2013, wurde seitens des <<<FA Grieskirchen Wels>>>  in vollem Umfang im Zuge einer Amtsrevision 
angefochten. ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des <<<FA Grieskirchen Wels>>>  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... 27.01.2016 für das Jahr 2007 (Rechtsvorgänger) 
wurde seitens des <<<FA Grieskirchen Wels>>>  mittels Amtsrevision bekämpft. Sollte der VwGH der Amtsrevision ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 2**

```
... die Beschwerde vom 
24. Jänner 2018 gegen den Bescheid des <<<FA Niederösterreich Mitte>>> (nunmehr Finanzamt Österreich) vom 
19. Dezember 2017, Steuernummer ...
```

| Predicted | Gold |
|---|---|
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Example 3**

```
... der Angelegenheit der Parteien 
Dagobert Hermkens (Bf) und <<<FA Klagenfurt St. Veit Wolfsberg>>>  als Amtspartei über die Beschwerde vom 7.2.2022     
     ...
```

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

**Example 4**

```
... nicht zulässig. 
 
Entscheidungsgründe 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 in Großbritannien errichtete 
Gesellschaft ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
...
Unterhaltungsmedien und Wetten. Das Online Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Registrierungsadresse in Österreich mit 15. September 2019 
geschlossen. 
<<<FA Salzburg-Stadt>>>  ist für das Betreiben der Website, das Einrichten und die ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
...
Rechtsmittelverfahren betreffend Rückabwicklung des Überrechnungsantrages beim <<<FA 08>>> 
abzuwarten und bis dorthin das gegenständliche Beschwerdeverfahren ...
```

FP: `FA 08` (organisation)

```
...
betreffend Rückabwicklung des Überrechnungsantrages m.W. nach beim <<<FA 08>>> bis dato nicht 
abgeschlossen ist, sodass nach wie vor der ...
```

FP: `FA 08` (organisation)

**✅ Gold Entities:**
- `35-039/2267` (tax_number)
- `35-039/2267` (tax_number)
- `35-039/2267` (tax_number)
- `35-039/2267` (tax_number)

**Example 1**

**False Positives:**

```
...
gesondert abgegolten.  
Auf den Vorlagebericht v.14.07.2015 zu <<<FA 46/2015>>>/002495 wird verwiesen. 
II. Das Bundesfinanzgericht hat erwogen: ...
```

FP: `FA 46/2015` (organisation)

**✅ Gold Entities:**
- `Prof. Hon.-Prof. ÖkR Detlev Leudert` (person)
- `Bungalowweg 8, 6741 Plazera, Österreich` (address)

**Example 2**

**False Positives:**

```
... Streitjahres zu gewähren: 
 
1.680 €…….168x10 Pendlerpauschale lt. <<<FA 
108>>>,30 €……10,83x10 Pendlereuro lt. FA 
 
Steuererklärung 2020 (Arbeitnehmerveranlagung): ...
```

FP: `FA 
108` (organisation)

**✅ Gold Entities:**
- `Mag. Rudolf Hawranek` (person)
- `Dagobert Hermkens` (person)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 3**

**False Positives:**

```
... 21.12.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (<<<FA 07>>>) die 
Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter ...
```

FP: `FA 07` (organisation)

**✅ Gold Entities:**
- `Dr.in Juliana Kleppel` (person)
- `HR Christian Styrnal` (person)
- `Babenbergersee I 18, 5524 Hallseiten, Österreich` (address)
- `60-008/3417` (tax_number)

**Example 4**

**False Positives:**

```
... September 2009 sowie vom 
14. Jänner 2013 gegen die Bescheide des <<<FA Salzburg-Land>>> (nunmehr Finanzamt Österreich) 
vom 18. Dezember 2012 betreffend ...
```

FP: `FA Salzburg-Land` (organisation)

**✅ Gold Entities:**
- `Irene Lachmann` (person)
- `Urbisweg 22, 4060 Sankt Isidor, Österreich` (address)
- `28-430/1410` (tax_number)
- `Urbisweg 22, 4060 Sankt Isidor, Österreich` (address)

</details>

---

## `company_gmbh_general`

**F1:** 0.035 | **Precision:** 0.500 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches generic company names ending in 'GMBH', ensuring the name starts with a capitalized word and has at least one preceding word, excluding common non-entity prefixes.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)+\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.018 | 0.035 | 20 | 10 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 10 | 298 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... „Küche“ wurde zunächst ausgeführt, dass zwei Rechnungen der „<<<Wiederspan Beratung GMBH>>>“ 
2 von 7
Seite 3 von 7 
 
 
keine Leistungsbeschreibung enthalte ...
```

| Predicted | Gold |
|---|---|
| `Wiederspan Beratung GMBH` | `Wiederspan Beratung GMBH` |

**Example 1**

```
... Gesellschafter) der mit Gesellschaftsvertrag 
vom 30.04.1979 gegründeten <<<Gumpold Technik GMBH>>> (in der Folge: GmbH). Geschäftsgegenstand der 
GmbH war der ...
```

| Predicted | Gold |
|---|---|
| `Gumpold Technik GMBH` | `Gumpold Technik GMBH` |

**Example 2**

```
... Beschwerdesache relevant – 
mit der Bersud Möbel GMBH (vormals <<<Unter Heimdorf GMBH>>>; im Folgenden: Y GmbH). 
Sowohl bei der Beschwerdeführerin ...
```

| Predicted | Gold |
|---|---|
| `Unter Heimdorf GMBH` | `Unter Heimdorf GMBH` |

**Example 3**

```
... bezog die Bf Einkünfte aus nichtselbständiger Arbeit bei der <<<Technik Valseekel GMBH>>> (nach Berücksichtigung des Pauschbetrages für Werbungskosten ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

```
... bezog die Bf Einkünfte aus 
nichtselbständiger Arbeit bei der <<<Technik Valseekel GMBH>>> (nach Berücksichtigung des Pauschbetrages 
für Werbungskosten ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

```
...
nichtselbständiger Arbeit. Sie war in genannten Jahren bei der <<<Technik Valseekel GMBH>>>  als 
4 von 9
Seite 5 von 9 
 
 
Arbeitnehmerin tätig und von ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

```
... Österreich an. 
2. Beweiswürdigung 
Das Dienstverhältnis der Bf zur <<<Technik Valseekel GMBH>>>  sowie das Bestehen des Wohnsitzes und 
Mittelpunktes der Lebensinteressen ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

**Example 4**

```
... ist, ob der Beschwerdeführer (Bf.) infolge der Insolvenz der <<<Luehrig + Hundertmarck Holz GMBH>>> 
(Primärschuldnerin) als ehemaliger Geschäftsführer für die ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

```
... ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der <<<Luehrig + Hundertmarck Holz GMBH>>>  in Höhe von Euro 396.769,30 in 
Anspruch genommen. 
Dagegen ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

```
... Oktober 2014, sowie ab 18. Dezember 2014 
Geschäftsführer der <<<Luehrig + Hundertmarck Holz GMBH>>> (Primärschuldnerin). 
Mit Beschluss des Landesgerichts Wr. ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Bundesfinanzgericht beschließt durch die Richterin Dr. Lisa Pucher in der <<<Beschwerdesache 
Enns Werkal GMBH>>>, Föhrenwald III 19, 3140 Pottenbrunn, Österreich, vertreten ...
```

FP: `Beschwerdesache 
Enns Werkal GMBH` (organisation)

```
... Bundes-Verfassungsgesetz 
(B-VG) nicht zulässig. 
Begründung 
<<<Die Enns Werkal GMBH>>>  hat mit Eingabe vom 07.08.2024 gemäß § 284 Abs 1 BAO 
Säumnisbeschwerden ...
```

FP: `Die Enns Werkal GMBH` (organisation)

**✅ Gold Entities:**
- `Enns Werkal GMBH` (organisation)
- `Föhrenwald III 19, 3140 Pottenbrunn, Österreich` (address)
- `04-382/0421` (tax_number)
- `Enns Werkal GMBH` (organisation)

**Example 1**

**False Positives:**

```
...
Der Bf. war im Beschwerdezeitraum durchgehend bei der Klein-<<<Vorholt KI GMBH>>>  angestellt. Im 
Vorjahr 2022 war der Bf. zunächst bis einschließlich ...
```

FP: `Vorholt KI GMBH` (organisation)

```
... 2022 war der Bf. zunächst bis einschließlich August bei der <<<Firma Gogel Daten GMBH>>> 
beschäftigt. Ab September 2022 begann sein Dienstverhältnis ...
```

FP: `Firma Gogel Daten GMBH` (organisation)

```
... Feststellung, wonach der Bf. im Jahr 2022 zunächst bei der <<<Firma Gogel Daten GMBH>>>  und im 
Folgenden bei der Klein-Vorholt KI GMBH  beschäftigt ...
```

FP: `Firma Gogel Daten GMBH` (organisation)

```
... der Firma Gogel Daten GMBH  und im 
Folgenden bei der Klein-<<<Vorholt KI GMBH>>>  beschäftigt war, ergibt sich einerseits aus dem vom Bf. mit ...
```

FP: `Vorholt KI GMBH` (organisation)

```
...
Dass der Bf. im Beschwerdezeitraum durchgehend bei der Klein-<<<Vorholt KI GMBH>>>  angestellt war, 
ergibt sich aus dem an das Finanzamt übermittelten ...
```

FP: `Vorholt KI GMBH` (organisation)

**✅ Gold Entities:**
- `Sophie Zekalla` (person)
- `Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich` (address)
- `71-479/6461` (tax_number)
- `Klein-Vorholt KI GMBH` (organisation)
- `Gogel Daten GMBH` (organisation)
- `Gogel Daten GMBH` (organisation)
- `Klein-Vorholt KI GMBH` (organisation)
- `Klein-Vorholt KI GMBH` (organisation)
- `AT91 2020 2243 9978 8478` (account)
- `Gogel Daten GMBH` (organisation)
- `Klein-Vorholt KI GMBH` (organisation)

**Example 2**

**False Positives:**

```
...
Elmira Gunder  als Masseverwalter im Insolvenzverfahren der Inn-<<<Recycling Institut GMBH>>>, Wolfgerstraße 5, 8223 Buchberg bei Herberstein, Österreich ...
```

FP: `Recycling Institut GMBH` (organisation)

**✅ Gold Entities:**
- `Dr. Torsten Wieskemper` (person)
- `Elmira Gunder` (person)
- `Inn-Recycling Institut GMBH` (organisation)
- `Wolfgerstraße 5, 8223 Buchberg bei Herberstein, Österreich` (address)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `specific_org_dias_telekom`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'DIAS Telekom Institut'.

**Content:**
```
\bDIAS\s+Telekom\s+Institut\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Raiffeisenbank Stallhofen'.

**Content:**
```
\bRaiffeisenbank\s+Stallhofen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_finanzen_tradonnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzen Tradonnex'.

**Content:**
```
\bFinanzen\s+Tradonnex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'TraunLuftfahrt Solutions'.

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

## `specific_org_houdek`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Houdek Maschinenbau'.

**Content:**
```
\bHoudek\s+Maschinenbau\b
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

## `tax_office_fa`

**F1:** 0.230 | **Precision:** 0.802 | **Recall:** 0.134  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by specific known locations. Removed restrictive negative lookahead to allow 'vom' and dates.

**Content:**
```
\bFA\s+(?:Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Wien\s+8/16/17|Salzburg-Stadt|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Amstetten\s+Melk\s+Scheibbs|Steiermark\s+Mitte|\d+/?\d+|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Tirol\s+Ost|Nieder\xf6sterreich\s+Mitte|Grieskirchen\s+Wels|Linz|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Klosterneuburg|Salzburg-Land|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Purkersdorf|Vorarlberg|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Waldviertel|Oststeiermark|Spittal\s+Villach|Gmunden\s+V\xf6cklabruck|Wien\s+1/23|Wien\s+8/16/17|Steiermark\s+Mitte|Nieder\xf6sterreich\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Amstetten\s+Melk\s+Scheibbs|Grieskirchen\s+Wels|Gmunden\s+V\xf6cklabruck|Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Purkersdorf|Vorarlberg|Waldviertel|Oststeiermark|Spittal\s+Villach|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+8/16/17|Graz-Stadt|Salzburg-Stadt|Salzburg-Land|Judenburg\s+Liezen|Klosterneuburg|Freistadt\s+Rohrbach\s+Urfahr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)(?!\s+vom|\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.802 | 0.134 | 0.230 | 91 | 73 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 73 | 18 | 471 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle 
des <<<FA Klosterneuburg>>> ) vom 13. Dezember 2019 betreffend Einkommensteuer 2011 zu ...
```

| Predicted | Gold |
|---|---|
| `FA Klosterneuburg` | `FA Klosterneuburg` |

**Example 1**

```
... Milan Händlein. 
Im Wirtschaftsjahr 2007 ist gemäß der beim <<<FA Grieskirchen Wels>>>  eingereichten 
Körperschaftsteuererklärung 2007 ein steuerlicher ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... 31.05.2013 beigelegt). Mit Vorlagebericht vom 13.11.2013 hat das <<<FA Grieskirchen Wels>>> 
die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... Linz, vom 27.01.2016, GZ 
RV/5101064/2013, wurde seitens des <<<FA Grieskirchen Wels>>>  in vollem Umfang im Zuge einer Amtsrevision 
angefochten. ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... beim 
Rechtsvorgänger für das Jahr 2007, wurde seitens des <<<FA Grieskirchen Wels>>>  am 07.03.2016 das 
Veranlagungsjahr 2010 beim gegenständlichen ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

```
... 27.01.2016 für das Jahr 2007 (Rechtsvorgänger) 
wurde seitens des <<<FA Grieskirchen Wels>>>  mittels Amtsrevision bekämpft. Sollte der VwGH der Amtsrevision ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 2**

```
... die Beschwerde vom 
24. Jänner 2018 gegen den Bescheid des <<<FA Niederösterreich Mitte>>> (nunmehr Finanzamt Österreich) vom 
19. Dezember 2017, Steuernummer ...
```

| Predicted | Gold |
|---|---|
| `FA Niederösterreich Mitte` | `FA Niederösterreich Mitte` |

**Example 3**

```
... der Angelegenheit der Parteien 
Dagobert Hermkens (Bf) und <<<FA Klagenfurt St. Veit Wolfsberg>>>  als Amtspartei über die Beschwerde vom 7.2.2022     
     ...
```

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

**Example 4**

```
... nicht zulässig. 
 
Entscheidungsgründe 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 in Großbritannien errichtete 
Gesellschaft ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
...
Unterhaltungsmedien und Wetten. Das Online Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Registrierungsadresse in Österreich mit 15. September 2019 
geschlossen. 
<<<FA Salzburg-Stadt>>>  ist für das Betreiben der Website, das Einrichten und die ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
...
Rechtsmittelverfahren betreffend Rückabwicklung des Überrechnungsantrages beim <<<FA 08>>> 
abzuwarten und bis dorthin das gegenständliche Beschwerdeverfahren ...
```

FP: `FA 08` (organisation)

```
...
betreffend Rückabwicklung des Überrechnungsantrages m.W. nach beim <<<FA 08>>> bis dato nicht 
abgeschlossen ist, sodass nach wie vor der ...
```

FP: `FA 08` (organisation)

**✅ Gold Entities:**
- `35-039/2267` (tax_number)
- `35-039/2267` (tax_number)
- `35-039/2267` (tax_number)
- `35-039/2267` (tax_number)

**Example 1**

**False Positives:**

```
...
gesondert abgegolten.  
Auf den Vorlagebericht v.14.07.2015 zu <<<FA 46/2015>>>/002495 wird verwiesen. 
II. Das Bundesfinanzgericht hat erwogen: ...
```

FP: `FA 46/2015` (organisation)

**✅ Gold Entities:**
- `Prof. Hon.-Prof. ÖkR Detlev Leudert` (person)
- `Bungalowweg 8, 6741 Plazera, Österreich` (address)

**Example 2**

**False Positives:**

```
... Streitjahres zu gewähren: 
 
1.680 €…….168x10 Pendlerpauschale lt. <<<FA 
108>>>,30 €……10,83x10 Pendlereuro lt. FA 
 
Steuererklärung 2020 (Arbeitnehmerveranlagung): ...
```

FP: `FA 
108` (organisation)

**✅ Gold Entities:**
- `Mag. Rudolf Hawranek` (person)
- `Dagobert Hermkens` (person)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 3**

**False Positives:**

```
... 21.12.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (<<<FA 07>>>) die 
Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter ...
```

FP: `FA 07` (organisation)

**✅ Gold Entities:**
- `Dr.in Juliana Kleppel` (person)
- `HR Christian Styrnal` (person)
- `Babenbergersee I 18, 5524 Hallseiten, Österreich` (address)
- `60-008/3417` (tax_number)

**Example 4**

**False Positives:**

```
... September 2009 sowie vom 
14. Jänner 2013 gegen die Bescheide des <<<FA Salzburg-Land>>> (nunmehr Finanzamt Österreich) 
vom 18. Dezember 2012 betreffend ...
```

FP: `FA Salzburg-Land` (organisation)

**✅ Gold Entities:**
- `Irene Lachmann` (person)
- `Urbisweg 22, 4060 Sankt Isidor, Österreich` (address)
- `28-430/1410` (tax_number)
- `Urbisweg 22, 4060 Sankt Isidor, Österreich` (address)

</details>

---

## `tax_office_finanzamt`

**F1:** 0.191 | **Precision:** 0.452 | **Recall:** 0.121  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by specific known locations. Removed restrictive negative lookahead to allow 'vom' and dates.

**Content:**
```
\bFinanzamt\s+(?:Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Wien\s+8/16/17|Salzburg-Stadt|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Amstetten\s+Melk\s+Scheibbs|Steiermark\s+Mitte|\d+/?\d+|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Tirol\s+Ost|Nieder\xf6sterreich\s+Mitte|Grieskirchen\s+Wels|Linz|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Klosterneuburg|Salzburg-Land|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Purkersdorf|Vorarlberg|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Waldviertel|Oststeiermark|Spittal\s+Villach|Gmunden\s+V\xf6cklabruck|Wien\s+1/23|Wien\s+8/16/17|Steiermark\s+Mitte|Nieder\xf6sterreich\s+Mitte|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Amstetten\s+Melk\s+Scheibbs|Grieskirchen\s+Wels|Gmunden\s+V\xf6cklabruck|Schwechat\s+Gerasdorf|Baden\s+M\xf6dling|Purkersdorf|Vorarlberg|Waldviertel|Oststeiermark|Spittal\s+Villach|Innsbruck|Braunau\s+Ried\s+Sch\xe4rding|Landeck\s+Reutte|Kirchdorf\s+Perg\s+Steyr|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+8/16/17|Graz-Stadt|Salzburg-Stadt|Salzburg-Land|Judenburg\s+Liezen|Klosterneuburg|Freistadt\s+Rohrbach\s+Urfahr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)(?!\s+vom|\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.452 | 0.121 | 0.191 | 146 | 66 | 80 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 66 | 80 | 478 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
...
gegen den zur Steuernummer 28-115/0315  ergangenen Bescheid des <<<Finanzamt Deutschlandsberg Leibnitz Voitsberg>>> (FA) vom 
11. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Deutschlandsberg Leibnitz Voitsberg` | `Finanzamt Deutschlandsberg Leibnitz Voitsberg` |

**Example 1**

```
... folgt eine zahlenmäßige Darstellung)  
Am 26.04.2013 erließ das <<<Finanzamt Grieskirchen Wels>>>  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
...
RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des <<<Finanzamt Grieskirchen Wels>>>  gegenüber der 
mitbeteiligten Partei Annemie Bott (als partiellen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... eingereicht. 
Unmittelbar nachfolgend hat das BFG die Amtsrevision des <<<Finanzamt Grieskirchen Wels>>> (samt Veranlagungsakten 
sowie Auszügen aus dem Arbeitsbogen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die 
Amtsrevision des <<<Finanzamt Grieskirchen Wels>>>  als unbegründet abgewiesen. Der VwGH formulierte die 
9 von ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... betragsmäßig verbindlich wird. Begründend 
wurde deshalb durch das <<<Finanzamt Grieskirchen Wels>>>  im Sachbescheid Feststellungsbescheid Gruppenmitglied 
2010 ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 2**

```
... Dr. Walter Ganster, Steuerberater in 9100 
Völkermarkt und <<<Finanzamt Schwechat Gerasdorf>>>  als Amtspartei und als Gesamtrechtsnachfolger des Finanzamtes ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Example 3**

```
... August 2017 
gegen den Bescheid des Finanzamtes F (nunmehr: <<<Finanzamt Klagenfurt St. Veit Wolfsberg>>>) vom 2. Juni 2017 betreffend 
Körperschaftsteuer 2016 zu Steuernummer ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | `Finanzamt Klagenfurt St. Veit Wolfsberg` |

**Example 4**

```
... Großbritannien errichtete 
Gesellschaft mit Sitz in Kranzing. <<<Finanzamt Salzburg-Stadt>>>  betreibt Geschäfte in den Bereichen 
Unterhaltungsmedien und ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
... erreichbar, welche unter anderem auch in Österreich verfügbar 
ist. <<<Finanzamt Salzburg-Stadt>>>  hält eine Wettlizenz des Vereinigten Königreichs. 
KommR Ing. ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
...
KommR Ing. Roberta Gossling  Limited ist eine im Jahr 2007 von <<<Finanzamt Salzburg-Stadt>>>  Ltd. gegründete Gesellschaft. Das 
Unternehmen ist in Großbritannien ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
...
Online Wettprodukte des Unternehmens waren unter der Website www.<<<Finanzamt Salzburg-Stadt>>> .com 
erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

```
... Wette auf den Ausgang der Lotterien erteilt der Teilnehmer <<<Finanzamt Salzburg-Stadt>>>  den 
Auftrag, die entsprechende Wette an KommR Ing. Roberta ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Einreichung der 
Umsatzsteuererklärung 2018 am 15.5.2019 beim <<<Finanzamt Graz-Stadt>>>, wurde die Frist für den 
Antrag auf Erstattung von Vorsteuern ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

```
... Anträge auf Erstattung von Vorsteuern zuständigen Behörde 
(<<<Finanzamt Graz-Stadt>>>) eingebracht. 
Weiters ist anzumerken, wenn die Behörde die ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

```
... 
Erstattung mittels amtlich vorgeschriebenem Vordruck beim <<<Finanzamt Graz-Stadt>>> zu 
beantragen. Der Antrag ist binnen sechs Monaten nach Ablauf ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

**✅ Gold Entities:**
- `Dr.in Constanze Peest` (person)
- `Linn Damianou` (person)
- `Fürnbergstraße 3, 4730 Steinparz, Österreich` (address)
- `Finanzamt Salzburg-Land` (organisation)
- `39-261/4216` (tax_number)

**Example 1**

**False Positives:**

```
... den 
Abweisungsbescheid des Finanzamtes Österreich (bisher <<<Finanzamt St. Johann Tamsweg Zell 
am See>>>) vom 6. August 2019 betreffend Familienbeihilfe für den Zeitraum ...
```

FP: `Finanzamt St. Johann Tamsweg Zell 
am See` (organisation)

**✅ Gold Entities:**
- `Heinrich Röskens` (person)
- `Kleinhofstraße 36, 2640 Pettenbach, Österreich` (address)

**Example 2**

**False Positives:**

```
... Gmunden“ gerichtete 
Vorlageantrag am 28. Dezember 2018 beim <<<Finanzamt Gmunden Vöcklabruck>>> einlangte, dieses 
Finanzamt jedoch sachlich und örtlich unzuständig ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

```
... Marxergasse 4, 4810 Gmunden“ und wurde 
am selben Tag beim <<<Finanzamt Gmunden Vöcklabruck>>> in Gmunden persönlich durch Einwurf in 
die „ Postbox“ der ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

```
... wurde der Vorlageantrag – zuständigkeitshalber - durch das <<<Finanzamt Gmunden 
Vöcklabruck>>> an das „Finanzamt für Gebühren und Verkehrsst. Marxerg. 4 1030 ...
```

FP: `Finanzamt Gmunden 
Vöcklabruck` (organisation)

```
... seinem sachlich und örtlich zuständigen Finanzamt (in dem 
Fall <<<Finanzamt Bruck Eisenstadt Oberwart>>>) fristwahrend abgeben. Soweit ihm Finanzonline 
7 von 10
Seite ...
```

FP: `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

```
... wird die Behörde im Adressfeld durch das weiterleitende Amt (<<<Finanzamt 
Gmunden Vöcklabruck>>>) selbst mit „Finanzamt für Gebühren u Verkehrsst“ bezeichnet. ...
```

FP: `Finanzamt 
Gmunden Vöcklabruck` (organisation)

**✅ Gold Entities:**
- `Ing. OMedR Albert Voulgaridou` (person)
- `Patriasdorfer Straße 4, 9634 Katlingberg, Österreich` (address)
- `07-334/2610` (tax_number)

**Example 3**

**False Positives:**

```
... hat. 
In der Zwischenzeit hat er sowohl der SVS als auch dem <<<Finanzamt Linz>>>, bei welchem er als 
beschränkt Steuerpflichtiger noch zu veranlagen ...
```

FP: `Finanzamt Linz` (organisation)

```
... veranlagen war, sämtliche Unterlagen übermittelt, jedoch 
ist es dem <<<Finanzamt Linz>>> nicht möglich, die zu Unrecht einbehaltene österreichische ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**
- `Viktoria Schreitmueller` (person)
- `Wolkersdorfer Weg 9q, 5223 Kuglberg, Österreich` (address)
- `18-890/9416` (tax_number)

**Example 4**

**False Positives:**

```
... 2020 gegen den Bescheid des 
Finanzamtes Österreich (vormals <<<Finanzamt Baden Mödling>>>) vom 13. November 2020 
betreffend Einkommensteuer 2015, Steuernummer ...
```

FP: `Finanzamt Baden Mödling` (organisation)

**✅ Gold Entities:**
- `Lara Pfeiferl` (person)
- `Obernbergerstraße 76, 8253 Schrimpf, Österreich` (address)
- `85-636/8182` (tax_number)

</details>

---

## `specific_org_milan`

**F1:** 0.187 | **Precision:** 1.000 | **Recall:** 0.103  

**Format:** `regex`  
**Description:**
Matches 'Milan H\xe4ndlein'.

**Content:**
```
\bMilan\s+H\xe4ndlein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.103 | 0.187 | 56 | 56 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 0 | 484 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Verfahren wie folgt: 
 a) Sachverhalt und Verfahrensablauf bei der <<<Milan Händlein>>>, Str.Nr. 79-810/8442, BV 24: 
Das Unternehmen <<<Milan Händlein>>> ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... <<<Milan Händlein>>>, Str.Nr. 79-810/8442, BV 24: 
Das Unternehmen <<<Milan Händlein>>>  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen. ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... die Nachfolgejahre wurden folgende 
Umgründungsschritte bei <<<Milan Händlein>>>  durchgeführt: 
Auf Grundlage des Spaltungs- und Übernahmsvertrages ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die <<<Milan Händlein>>> 
mit Stichtag 31.12.2007 als übertragende Gesellschaft nach ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

```
... Beratung  verschmolzen worden. 
Zum Stichtag 31.12.2008 ist die <<<Milan Händlein>>>  mit dem verbliebenen Vermögen entsprechend 
dem Umgründungsplan ...
```

| Predicted | Gold |
|---|---|
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |
| `Milan Händlein` | `Milan Händlein` |

</details>

---

## `specific_org_fa_salzburg`

**F1:** 0.108 | **Precision:** 1.000 | **Recall:** 0.057  

**Format:** `regex`  
**Description:**
Matches 'FA Salzburg-Stadt'.

**Content:**
```
\bFA\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.057 | 0.108 | 31 | 31 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 31 | 0 | 346 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... über die Beschwerde vom 13. Juli 2023 gegen den Bescheid des 
<<<FA Salzburg-Stadt>>>  vom 19. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 1**

```
... nicht zulässig. 
 
Entscheidungsgründe 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 in Großbritannien errichtete 
Gesellschaft ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
...
Unterhaltungsmedien und Wetten. Das Online Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

```
... Registrierungsadresse in Österreich mit 15. September 2019 
geschlossen. 
<<<FA Salzburg-Stadt>>>  ist für das Betreiben der Website, das Einrichten und die ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 2**

```
... über die Beschwerde vom 18. Mai 2021 gegen den Bescheid des <<<FA Salzburg-Stadt>>> 
vom 17. Mai 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

</details>

---

## `specific_org_annemie_bott`

**F1:** 0.098 | **Precision:** 1.000 | **Recall:** 0.051  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Annemie Bott'.

**Content:**
```
\bAnnemie\s+Bott\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.051 | 0.098 | 28 | 28 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 0 | 512 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Beschwerdesache  
1) PhD Marianne Yener  als Rechtsnachfolger der <<<Annemie Bott>>>,  Schäfergasse 5, 3613 Marbach an der Kleinen Krems, Österreich, ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (<<<Annemie Bott>>> 
St. Nr. 64-207/8107) und das Verfahren wiederaufgenommen. ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... wiederaufgenommen.  Bescheidadressaten waren 
sowohl das Gruppenmitglied <<<Annemie Bott>>>  als auch der Gruppenträger StadtEnergie Holding 
(28-587/0533). ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... Generalversammlungsbeschlusses vom 
19.08.2009 eine Abspaltung zur Aufnahme in die <<<Annemie Bott>>>  durch Übertragung des 
gesamten Betriebes (mit Ausnahme der ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

```
... Positionen) erfolgt. Die Grönemeier&Hövelberndt E‑Commerce  und 
<<<Annemie Bott>>>  sind aufgrund der dargestellten Umgründungsschritte (partielle) ...
```

| Predicted | Gold |
|---|---|
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |
| `Annemie Bott` | `Annemie Bott` |

</details>

---

## `specific_org_pastel`

**F1:** 0.091 | **Precision:** 1.000 | **Recall:** 0.048  

**Format:** `regex`  
**Description:**
Matches 'Pastel Pharma'.

**Content:**
```
\bPastel\s+Pharma\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.048 | 0.091 | 26 | 26 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 0 | 155 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Dieter Fröhlich über die 
Bescheidbeschwerde vom 12.10.2017 der <<<Pastel Pharma>>>, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
... Bundesminister für Finanzen und führte 
dazu aus: 
„Die Firma <<<Pastel Pharma>>>  betreibt ein Wettbüro und schließt Wetten überwiegend über ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
... Forderungen bis zur 
Höhe des negativen Eigenkapitals verzichte. Die <<<Pastel Pharma>>>  ist zu 100% an der BB. mit Sitz in 
Curacao beteiligt. Die ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
... Appendix A dieser 
Unterlage ist eine vorläufige Lizenz auch der <<<Pastel Pharma>>>  Austria unter den Internetmarken 
(Internet-Plattformen) www.xx.com ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

```
...
Gesetzen von Curacao unterliegen und der Vertag zwischen der <<<Pastel Pharma>>>  Eood (mit Sitz in 
Bulgarien, Sofia) und dem Endkunden zustande ...
```

| Predicted | Gold |
|---|---|
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |
| `Pastel Pharma` | `Pastel Pharma` |

</details>

---

## `specific_org_celikkanat_garten`

**F1:** 0.081 | **Precision:** 1.000 | **Recall:** 0.042  

**Format:** `regex`  
**Description:**
Matches 'Celikkanat Garten' (without GmbH in this context).

**Content:**
```
\bCelikkanat\s+Garten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.042 | 0.081 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 246 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Ort,  
3. Okur Automotive  GmbH & Co KG, Straße3, Ort und 
4. <<<Celikkanat Garten>>>  GmbH & Co KG, Straße3, Ort, 
alle vertreten durch yy Wirtschaftstreuhand ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
... zzgl. Sonderbetriebsausgaben in Höhe von -€ 258.374,89), 
4. <<<Celikkanat Garten>>>  GmbH & Co KG: ein Betrag von -€ 1.527.464,40 (Verlustzuweisung ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
... Betrag von € 2.470.000,00 zu 
berücksichtigen sind) und 
4. <<<Celikkanat Garten>>>  GmbH & Co KG: € -1.387.500,00 (wobei bei der Veranlagung der ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
...
Verkehrswertzusammenschluss mit Buchwertfortführung gem. Art IV UmgrStG. 
 <<<Celikkanat Garten>>>  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 4. ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

```
... „Errichtung stille Gesellschaft“ - 
Okur Automotive  GmbH & Co KG und <<<Celikkanat Garten>>>  GmbH & Co KG 
 Zusammenschlussvertrag - Okur Automotive  ...
```

| Predicted | Gold |
|---|---|
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |
| `Celikkanat Garten` | `Celikkanat Garten` |

</details>

---

## `specific_org_okur`

**F1:** 0.078 | **Precision:** 1.000 | **Recall:** 0.040  

**Format:** `regex`  
**Description:**
Matches 'Okur Automotive'.

**Content:**
```
\bOkur\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.040 | 0.078 | 22 | 22 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 22 | 0 | 247 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Straße3, Ort, 
2. Leiss Software  GmbH & Co KG, Straße3, Ort,  
3. <<<Okur Automotive>>>  GmbH & Co KG, Straße3, Ort und 
4. Celikkanat Garten  GmbH ...
```

| Predicted | Gold |
|---|---|
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |

```
... in 
Höhe von -€ 3.552,80),  
2 von 31
Seite 3 von 31 
 
 
3. <<<Okur Automotive>>>  GmbH & Co KG:  ein Betrag von -€ 2.728.374,89 (Verlustzuweisung ...
```

| Predicted | Gold |
|---|---|
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |

```
... Betrieb) im Betrag von € 86.861,84 zu berücksichtigen 
sind), 
3. <<<Okur Automotive>>>  GmbH & Co KG:  € -2.470.000,00 (wobei bei der Veranlagung ...
```

| Predicted | Gold |
|---|---|
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |

```
...
Verkehrswertzusammenschluss mit Buchwertfortführung gem. Art IV UmgrStG. 
 <<<Okur Automotive>>>  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 15. ...
```

| Predicted | Gold |
|---|---|
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |

```
... Zusammenschlussvertrag – „Errichtung stille Gesellschaft“ - 
<<<Okur Automotive>>>  GmbH & Co KG und Celikkanat Garten  GmbH & Co KG 
 Zusammenschlussvertrag ...
```

| Predicted | Gold |
|---|---|
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |
| `Okur Automotive` | `Okur Automotive` |

</details>

---

## `tax_office_finanzamt_grieskirchen`

**F1:** 0.074 | **Precision:** 1.000 | **Recall:** 0.039  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Grieskirchen Wels'.

**Content:**
```
\bFinanzamt\s+Grieskirchen\s+Wels\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.039 | 0.074 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 0 | 519 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
...
über die Beschwerden vom 29. März 2019 gegen den Bescheid des <<<Finanzamt Grieskirchen Wels>>>  vom 29. Jänner 
2019 betreffend Wiederaufnahme § 303 BAO / ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... folgt eine zahlenmäßige Darstellung)  
Am 26.04.2013 erließ das <<<Finanzamt Grieskirchen Wels>>>  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
...
RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des <<<Finanzamt Grieskirchen Wels>>>  gegenüber der 
mitbeteiligten Partei Annemie Bott (als partiellen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... eingereicht. 
Unmittelbar nachfolgend hat das BFG die Amtsrevision des <<<Finanzamt Grieskirchen Wels>>> (samt Veranlagungsakten 
sowie Auszügen aus dem Arbeitsbogen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

```
... 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die 
Amtsrevision des <<<Finanzamt Grieskirchen Wels>>>  als unbegründet abgewiesen. Der VwGH formulierte die 
9 von ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 1**

```
... die Beschwerde vom 23. Februar 2017 gegen den Bescheid des <<<Finanzamt Grieskirchen Wels>>> 
(nunmehr Finanzamt FA) vom 23. Jänner 2017 betreffend Haftungsinanspruchnahme ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 2**

```
... vorgelegten Rechnung vom 31.3.2013 geht hervor, dass von der <<<Finanzamt Grieskirchen Wels>>>  eine 
Wartung des Treppenlifts zu einem Gesamtbetrag von 283,20 ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 3**

```
...
Bundes-Verfassungsgesetz (B-VG) nicht zulässig.  
Begründung 
Mit Bescheid des <<<Finanzamt Grieskirchen Wels>>>  vom 5. Februar 2021 wurde zur Steuernummer 57-862/6163 
der ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

</details>

---

## `specific_org_reinemut`

**F1:** 0.071 | **Precision:** 1.000 | **Recall:** 0.037  

**Format:** `regex`  
**Description:**
Matches 'Reinemut + Smoch Handel'.

**Content:**
```
\bReinemut\s+\+\s+Smoch\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.037 | 0.071 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 13 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich 
2. <<<Reinemut + Smoch Handel>>>, Zachariasweg 4K, 3250 Wieselburg, Österreich  
beide vertreten ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

```
... 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der 
<<<Reinemut + Smoch Handel>>>  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

```
... des Verdachts einer Verkürzung an 
Umsatzsteuer 7/2019 der <<<Reinemut + Smoch Handel>>>  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren 
wird ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

```
... §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt. 
Über die <<<Reinemut + Smoch Handel>>>  wird gemäß §§ 28a Abs. 2 und 33 Abs. 5 FinStrG iVm §§ 3-5 ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

```
... Angelegenheiten verantwortliche Geschäftsführer der Firma 
<<<Reinemut + Smoch Handel>>>, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

</details>

---

## `specific_org_leiss`

**F1:** 0.047 | **Precision:** 1.000 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches 'Leiss Software' which appears without GmbH in the text.

**Content:**
```
\bLeiss\s+Software\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.024 | 0.047 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 256 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Gesellschafterinnen 
1. Kök & Heberlein Bau  GmbH & Co KG, Straße3, Ort, 
2. <<<Leiss Software>>>  GmbH & Co KG, Straße3, Ort,  
3. Okur Automotive  GmbH & Co ...
```

| Predicted | Gold |
|---|---|
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |

```
... 10.828,20 (Sonderbetriebsausgaben in 
Höhe von -€ 10.828,20), 
2. <<<Leiss Software>>>  GmbH & Co KG: ein Betrag von -€ 3.552,80 (Sonderbetriebsausgaben ...
```

| Predicted | Gold |
|---|---|
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |

```
...
zugerechnet: 
1. Kök & Heberlein Bau  GmbH & Co KG: € 0,00, 
2. <<<Leiss Software>>>  GmbH & Co KG: € -86.861,84 (wobei bei der Veranlagung der ...
```

| Predicted | Gold |
|---|---|
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |

```
... Verkehrswertzusammenschluss mit 
Buchwertfortführung gem. Art IV UmgrStG. 
 <<<Leiss Software>>>  GmbH & Co KG: Die Bf. wurde mit Gesellschaftsvertrag vom 24. ...
```

| Predicted | Gold |
|---|---|
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |

```
... verpflichtet, ein Kapitalkonto aufzufüllen. 
 Zusammenschlussvertrag – <<<Leiss Software>>>  GmbH & Co KG: 
Zu den Ausführungen zum rückwirkend errichteten ...
```

| Predicted | Gold |
|---|---|
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |
| `Leiss Software` | `Leiss Software` |

</details>

---

## `specific_org_kok_heberlein`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Matches 'Kök & Heberlein Bau'.

**Content:**
```
\bKök\s+&\s+Heberlein\s+Bau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 0 | 257 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... die Beschwerden der atypisch stillen Gesellschafterinnen 
1. <<<Kök & Heberlein Bau>>>  GmbH & Co KG, Straße3, Ort, 
2. Leiss Software  GmbH & Co ...
```

| Predicted | Gold |
|---|---|
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |

```
... 2009 vom 9. Dezember 2010 
folgende Einkünfte zugerechnet: 
1. <<<Kök & Heberlein Bau>>>  GmbH & Co KG: ein Betrag von -€ 10.828,20 (Sonderbetriebsausgaben ...
```

| Predicted | Gold |
|---|---|
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |

```
... atypisch stillen Gesellschafterinnen wie folgt 
zugerechnet: 
1. <<<Kök & Heberlein Bau>>>  GmbH & Co KG: € 0,00, 
2. Leiss Software  GmbH & Co KG: € ...
```

| Predicted | Gold |
|---|---|
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |

```
... -beziehungen – Verträge – Verlustzuweisung 
Zu den Bf.: 
 <<<Kök & Heberlein Bau>>>  GmbH & Co KG: Die stille Gesellschafterin wurde mit Gesellschaftsvertrag ...
```

| Predicted | Gold |
|---|---|
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |

```
...
Gesellschafterinnen folgende Sonderbetriebsausgaben in Abzug gebracht. 
1. <<<Kök & Heberlein Bau>>>  GmbH & Co KG: -€ 10.828,30 
2. Leiss Software  GmbH & Co KG: ...
```

| Predicted | Gold |
|---|---|
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |
| `Kök & Heberlein Bau` | `Kök & Heberlein Bau` |

</details>

---

## `specific_org_manfredo`

**F1:** 0.040 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Manfredo Herrschmann'.

**Content:**
```
\bManfredo\s+Herrschmann\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.020 | 0.040 | 11 | 11 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 0 | 529 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Vermögen, bestehend aus 11 einzeln 
benannten Tankstellen, auf die <<<Manfredo Herrschmann>>>  übertragen. Die <<<Manfredo Herrschmann>>>  ist zum 
31.10.2010 ...
```

| Predicted | Gold |
|---|---|
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |

```
... Tankstellen, auf die <<<Manfredo Herrschmann>>>  übertragen. Die <<<Manfredo Herrschmann>>>  ist zum 
31.10.2010 als übertragende Gesellschaft mit Krolitzki ...
```

| Predicted | Gold |
|---|---|
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |

```
... Beratung  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der <<<Manfredo Herrschmann>>> (partielle) 
Gesamtrechtsnachfolgerin der Milan Händlein. 
...
```

| Predicted | Gold |
|---|---|
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |

```
...
 
216.864,04 
 
4 von 39
Seite 5 von 39 
 
 
Teilbetriebe 
<<<Manfredo Herrschmann>>>:  
Verluste 
geschlossene 
Teilbetriebe 
Milan Händlein:  
...
```

| Predicted | Gold |
|---|---|
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |

```
... -4.815.241,29  1.183.053,01 
 
 Abgespaltene 
Tankstellen 
<<<Manfredo Herrschmann>>>
**  
Geschlossene 
Tankstellen 
Milan Händlein 
Verkaufte 
...
```

| Predicted | Gold |
|---|---|
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |
| `Manfredo Herrschmann` | `Manfredo Herrschmann` |

</details>

---

## `company_gmbh_general`

**F1:** 0.035 | **Precision:** 0.500 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches generic company names ending in 'GMBH', ensuring the name starts with a capitalized word and has at least one preceding word, excluding common non-entity prefixes.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)+\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.018 | 0.035 | 20 | 10 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 10 | 298 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... „Küche“ wurde zunächst ausgeführt, dass zwei Rechnungen der „<<<Wiederspan Beratung GMBH>>>“ 
2 von 7
Seite 3 von 7 
 
 
keine Leistungsbeschreibung enthalte ...
```

| Predicted | Gold |
|---|---|
| `Wiederspan Beratung GMBH` | `Wiederspan Beratung GMBH` |

**Example 1**

```
... Gesellschafter) der mit Gesellschaftsvertrag 
vom 30.04.1979 gegründeten <<<Gumpold Technik GMBH>>> (in der Folge: GmbH). Geschäftsgegenstand der 
GmbH war der ...
```

| Predicted | Gold |
|---|---|
| `Gumpold Technik GMBH` | `Gumpold Technik GMBH` |

**Example 2**

```
... Beschwerdesache relevant – 
mit der Bersud Möbel GMBH (vormals <<<Unter Heimdorf GMBH>>>; im Folgenden: Y GmbH). 
Sowohl bei der Beschwerdeführerin ...
```

| Predicted | Gold |
|---|---|
| `Unter Heimdorf GMBH` | `Unter Heimdorf GMBH` |

**Example 3**

```
... bezog die Bf Einkünfte aus nichtselbständiger Arbeit bei der <<<Technik Valseekel GMBH>>> (nach Berücksichtigung des Pauschbetrages für Werbungskosten ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

```
... bezog die Bf Einkünfte aus 
nichtselbständiger Arbeit bei der <<<Technik Valseekel GMBH>>> (nach Berücksichtigung des Pauschbetrages 
für Werbungskosten ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

```
...
nichtselbständiger Arbeit. Sie war in genannten Jahren bei der <<<Technik Valseekel GMBH>>>  als 
4 von 9
Seite 5 von 9 
 
 
Arbeitnehmerin tätig und von ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

```
... Österreich an. 
2. Beweiswürdigung 
Das Dienstverhältnis der Bf zur <<<Technik Valseekel GMBH>>>  sowie das Bestehen des Wohnsitzes und 
Mittelpunktes der Lebensinteressen ...
```

| Predicted | Gold |
|---|---|
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |
| `Technik Valseekel GMBH` | `Technik Valseekel GMBH` |

**Example 4**

```
... ist, ob der Beschwerdeführer (Bf.) infolge der Insolvenz der <<<Luehrig + Hundertmarck Holz GMBH>>> 
(Primärschuldnerin) als ehemaliger Geschäftsführer für die ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

```
... ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der <<<Luehrig + Hundertmarck Holz GMBH>>>  in Höhe von Euro 396.769,30 in 
Anspruch genommen. 
Dagegen ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

```
... Oktober 2014, sowie ab 18. Dezember 2014 
Geschäftsführer der <<<Luehrig + Hundertmarck Holz GMBH>>> (Primärschuldnerin). 
Mit Beschluss des Landesgerichts Wr. ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Bundesfinanzgericht beschließt durch die Richterin Dr. Lisa Pucher in der <<<Beschwerdesache 
Enns Werkal GMBH>>>, Föhrenwald III 19, 3140 Pottenbrunn, Österreich, vertreten ...
```

FP: `Beschwerdesache 
Enns Werkal GMBH` (organisation)

```
... Bundes-Verfassungsgesetz 
(B-VG) nicht zulässig. 
Begründung 
<<<Die Enns Werkal GMBH>>>  hat mit Eingabe vom 07.08.2024 gemäß § 284 Abs 1 BAO 
Säumnisbeschwerden ...
```

FP: `Die Enns Werkal GMBH` (organisation)

**✅ Gold Entities:**
- `Enns Werkal GMBH` (organisation)
- `Föhrenwald III 19, 3140 Pottenbrunn, Österreich` (address)
- `04-382/0421` (tax_number)
- `Enns Werkal GMBH` (organisation)

**Example 1**

**False Positives:**

```
...
Der Bf. war im Beschwerdezeitraum durchgehend bei der Klein-<<<Vorholt KI GMBH>>>  angestellt. Im 
Vorjahr 2022 war der Bf. zunächst bis einschließlich ...
```

FP: `Vorholt KI GMBH` (organisation)

```
... 2022 war der Bf. zunächst bis einschließlich August bei der <<<Firma Gogel Daten GMBH>>> 
beschäftigt. Ab September 2022 begann sein Dienstverhältnis ...
```

FP: `Firma Gogel Daten GMBH` (organisation)

```
... Feststellung, wonach der Bf. im Jahr 2022 zunächst bei der <<<Firma Gogel Daten GMBH>>>  und im 
Folgenden bei der Klein-Vorholt KI GMBH  beschäftigt ...
```

FP: `Firma Gogel Daten GMBH` (organisation)

```
... der Firma Gogel Daten GMBH  und im 
Folgenden bei der Klein-<<<Vorholt KI GMBH>>>  beschäftigt war, ergibt sich einerseits aus dem vom Bf. mit ...
```

FP: `Vorholt KI GMBH` (organisation)

```
...
Dass der Bf. im Beschwerdezeitraum durchgehend bei der Klein-<<<Vorholt KI GMBH>>>  angestellt war, 
ergibt sich aus dem an das Finanzamt übermittelten ...
```

FP: `Vorholt KI GMBH` (organisation)

**✅ Gold Entities:**
- `Sophie Zekalla` (person)
- `Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich` (address)
- `71-479/6461` (tax_number)
- `Klein-Vorholt KI GMBH` (organisation)
- `Gogel Daten GMBH` (organisation)
- `Gogel Daten GMBH` (organisation)
- `Klein-Vorholt KI GMBH` (organisation)
- `Klein-Vorholt KI GMBH` (organisation)
- `AT91 2020 2243 9978 8478` (account)
- `Gogel Daten GMBH` (organisation)
- `Klein-Vorholt KI GMBH` (organisation)

**Example 2**

**False Positives:**

```
...
Elmira Gunder  als Masseverwalter im Insolvenzverfahren der Inn-<<<Recycling Institut GMBH>>>, Wolfgerstraße 5, 8223 Buchberg bei Herberstein, Österreich ...
```

FP: `Recycling Institut GMBH` (organisation)

**✅ Gold Entities:**
- `Dr. Torsten Wieskemper` (person)
- `Elmira Gunder` (person)
- `Inn-Recycling Institut GMBH` (organisation)
- `Wolfgerstraße 5, 8223 Buchberg bei Herberstein, Österreich` (address)

</details>

---

## `specific_org_krolitzki`

**F1:** 0.033 | **Precision:** 1.000 | **Recall:** 0.017  

**Format:** `regex`  
**Description:**
Matches 'Krolitzki Beratung'.

**Content:**
```
\bKrolitzki\s+Beratung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.017 | 0.033 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 531 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Herrschmann  ist zum 
31.10.2010 als übertragende Gesellschaft mit <<<Krolitzki Beratung>>>  verschmolzen worden. 
Zum Stichtag 31.12.2008 ist die Milan ...
```

| Predicted | Gold |
|---|---|
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |

```
... der Milan Händlein  verbliebende Vermögen betroffen ist. Die <<<Krolitzki Beratung>>>  ist 
auf Grund der Verschmelzung zum 31.10.2010 mit der Manfredo ...
```

| Predicted | Gold |
|---|---|
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |

```
... E‑Commerce 
und einen Körperschaftsteuerbescheid 2007 an die <<<Krolitzki Beratung>>>, da diese Gesellschaften auf 
Grund der Abspaltung der 11 Tankstellen ...
```

| Predicted | Gold |
|---|---|
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |

```
... Finanzamt den erzielten 
Verlust 2007 zwischen Annemie Bott  und <<<Krolitzki Beratung>>>  grundsätzlich entsprechend der 
Zuordnung der Einkünfte zu ...
```

| Predicted | Gold |
|---|---|
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |

```
... Betriebsprüfung ermittelte Verlust wäre 
daher zwischen Annemie Bott  und <<<Krolitzki Beratung>>>  wie folgt aliquot (unter Außerachtlassung 
einer geringfügigen ...
```

| Predicted | Gold |
|---|---|
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |
| `Krolitzki Beratung` | `Krolitzki Beratung` |

</details>

---

## `specific_org_wod_sicherheit`

**F1:** 0.029 | **Precision:** 1.000 | **Recall:** 0.015  

**Format:** `regex`  
**Description:**
Matches 'WOD Sicherheit KG'.

**Content:**
```
\bWOD\s+Sicherheit\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.015 | 0.029 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 297 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Beschwerdeführer (kurz: Bf.) war im Jahr 2018 zu 60% an der <<<WOD Sicherheit KG>>>  und zu 33,33% an 
der Zumholte Verlag OG  beteiligt. Unternehmensgegenstand ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... stellte das Finanzamt die gemeinschaftlichen Einkünfte 2018 der 
<<<WOD Sicherheit KG>>>  mit 48.094,37 Euro und den auf die Beteiligung an der KG entfallenden ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
...
2018 ein, er habe die Einkünfte aus seiner Beteiligung an der <<<WOD Sicherheit KG>>>  im Jahr 2018 nicht 
mehr erhalten, weshalb dieser Anteil in ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... Zuflussprinzip zu beachten. Im Jahr 2018 seien ihm 
keine Einnahmen der <<<WOD Sicherheit KG>>>  zugeflossen, weswegen diese auch nicht der 
Einkommensteuer ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... erneut, die anteiligen 
Einkünfte von der Beteiligung an der <<<WOD Sicherheit KG>>>  2018 aus der Einkommensteuerfestsetzung 
auszunehmen.  
Am ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

</details>

---

## `specific_org_bahrdt`

**F1:** 0.025 | **Precision:** 1.000 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches 'Bahrdt Digital'.

**Content:**
```
\bBahrdt\s+Digital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.013 | 0.025 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 105 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... selbstständiger Tätigkeit als Gesellschaftsgeschäftsführer der Fa. 
<<<Bahrdt Digital>>> (im Folgenden GmbH-Gesellschaft) abweichend von der 
1 von ...
```

| Predicted | Gold |
|---|---|
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |

```
...
1988 (mit einer Gesellschaftsbeteiligung vom 55%) für die Fa. <<<Bahrdt Digital>>>  aus und erzielte 
damit (unstrittig) Einkünfte aus selbstständiger ...
```

| Predicted | Gold |
|---|---|
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |

```
... aktenkundigem Umlaufbeschluss vom 29.02.2016 zwischen dem Bf 
und der <<<Bahrdt Digital>>>  festgehalten, bezahlte die <<<Bahrdt Digital>>>  dem Bf überdies ...
```

| Predicted | Gold |
|---|---|
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |

```
... dem Bf 
und der <<<Bahrdt Digital>>>  festgehalten, bezahlte die <<<Bahrdt Digital>>>  dem Bf überdies seine für 2014 
geschuldeten Sozialversicherungsbeiträge ...
```

| Predicted | Gold |
|---|---|
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |

```
... Sozialversicherungsbeiträge iHv. EUR. 17.679,27, in-dem die <<<Bahrdt Digital>>>  die 
Sozialversicherungsbeiträge anhand vier (etwa vierteljährlich) ...
```

| Predicted | Gold |
|---|---|
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |
| `Bahrdt Digital` | `Bahrdt Digital` |

</details>

---

## `specific_org_gronemeier`

**F1:** 0.025 | **Precision:** 1.000 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches 'Grönemeier&Hövelberndt E‑Commerce' with em-dash.

**Content:**
```
\bGr\xf6nemeier&H\xf6velberndt\s+E\u2011Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.013 | 0.025 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 533 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... übertragende Gesellschaft (neben anderen Gesellschaften) mit der 
<<<Grönemeier&Hövelberndt E‑Commerce>>>  als übernehmende Gesellschaft verschmolzen worden. Im stichtagsgleichen ...
```

| Predicted | Gold |
|---|---|
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |

```
...
Übernahmsvertrages taxativ angeführten Positionen) erfolgt. Die <<<Grönemeier&Hövelberndt E‑Commerce>>>  und 
Annemie Bott  sind aufgrund der dargestellten Umgründungsschritte ...
```

| Predicted | Gold |
|---|---|
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |

```
...
Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Annemie Bott, die <<<Grönemeier&Hövelberndt E‑Commerce>>> 
und einen Körperschaftsteuerbescheid 2007 an die Krolitzki ...
```

| Predicted | Gold |
|---|---|
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |

```
... verbleibenden 
Teilbetrieben bzw. Vermögen zuzuordnen sind. Der <<<Grönemeier&Hövelberndt E‑Commerce>>>  als weiterem partiellen 
Gesamtrechtsnachfolger wurde ein ...
```

| Predicted | Gold |
|---|---|
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |

```
... Rechtsmeinung des Beschwerdeführers geteilt, wonach der bei der 
<<<Grönemeier&Hövelberndt E‑Commerce>>>  im Jahr 2007 insgesamt entstandene Verlust nach Vornahme des ...
```

| Predicted | Gold |
|---|---|
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |
| `Grönemeier&Hövelberndt E‑Commerce` | `Grönemeier&Hövelberndt E‑Commerce` |

</details>

---

## `company_ag_general`

**F1:** 0.022 | **Precision:** 0.080 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches generic company names ending in 'AG', ensuring the name starts with a capitalized word.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)*\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.080 | 0.013 | 0.022 | 87 | 7 | 80 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 80 | 537 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
...
gemäß § 41 Abs 1 Z 2 vor, weil sich die lohnsteuerpflichtigen <<<ZYJY Automotive AG>>>  GmbH sowie 
NYJ Event AG  GmbH zwar überschneiden würden, ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... sich die lohnsteuerpflichtigen ZYJY Automotive AG  GmbH sowie 
<<<NYJ Event AG>>>  GmbH zwar überschneiden würden, der Gesetzwortlaut verlange ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... Tatbestandsmerkmal des § 41 Abs 1 Z 12 vor. Im Zuge der 
Lohnverrechnung/<<<Kubzyk Elektro AG>>>  GmbH sei der ganze Familienbonus Plus ausbezahlt worden, 
...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... Arbeit-/Auftraggeber Betrag 
Lohnzettel 84(1) 01.01.-15.09. <<<Kubzyk Elektro AG>>>  GmbH € 17.356,99 
Meldung 3(2) 19.09.-02.10. Arbeitsmarktservice ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

```
... Arbeitsmarktservice Österreich € 507,22 
Lohnzettel 84(1) 24.09.-31.12. <<<ZYJY Automotive AG>>>  GmbH € 1.058,79 
Lohnzettel 84(1) 03.10.-31.12. NYJ Event ...
```

| Predicted | Gold |
|---|---|
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |
| `NYJ Event AG` | `NYJ Event AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `Kubzyk Elektro AG` | `Kubzyk Elektro AG` |
| `ZYJY Automotive AG` | `ZYJY Automotive AG` |

**Example 1**

```
... zwischen der beschwerdeführenden Partei als Arbeitnehmer und der <<<Heimwil Transport AG>>>  als 
3 von 6
Seite 4 von 6 
 
 
Arbeitgeberin sowie den Angaben ...
```

| Predicted | Gold |
|---|---|
| `Heimwil Transport AG` | `Heimwil Transport AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Abschlusszahlung B 
Sachverhalt: 
Im WJ 2013/2014 wurden sämtliche vom <<<Konzern AG>>> gehaltenen Anteile an der OÖ. A AG (C) 
an deren Hauptgesellschafter ...
```

FP: `Konzern AG` (organisation)

```
... betreffende Gewinnverteilungsbeschluss kann durch den alleinigen <<<Gesellschafter AG>>> nach 
Feststellung der Bilanz B per 30.9.2014 erst Ende 2014 ...
```

FP: `Gesellschafter AG` (organisation)

```
... Juni 2014 bereits durchgeführt wurde. Im Übrigen waren diese <<<Zahlungen Seitens 
AG>>> jedenfalls zu leisten, auch wenn kein entsprechender Gewinn ...
```

FP: `Zahlungen Seitens 
AG` (organisation)

```
... Beteiligung. In wirtschaftlicher 
Betrachtungsweise wurde der <<<Erwerberin AG>>> zugestanden, diesen Restkaufpreis aus der dieser 
ausschließlich ...
```

FP: `Erwerberin AG` (organisation)

```
... übertragen wurde. Dieser 
bis dahin zukünftig der alleinigen <<<Gesellschafterin AG>>> zufließende Wertzuwachs der Beteiligung 
B sollte der Verkäuferin ...
```

FP: `Gesellschafterin AG` (organisation)

**✅ Gold Entities:**
- `Veronika Cuerten, Bakk. phil.` (person)
- `Schöglerstraße 1, 9612 Bach, Österreich` (address)

**Example 1**

**False Positives:**

```
... nach Rückkauf einer fondsgebundenen 
Lebensversicherung der X <<<Versicherungs AG>>> zum 01.05.2014 mit laufender gleichbleibender 
Prämienzahlung ...
```

FP: `Versicherungs AG` (organisation)

```
... Zuge des Ermittlungsverfahrens vor dem Finanzamt teilte die X <<<Lebensversicherungs AG>>> im 
Schreiben vom 29.12.2014 mit, dass es sich im gegenständlichen ...
```

FP: `Lebensversicherungs AG` (organisation)

```
... Tilgungsträger einer 
gleichlaufenden endfälligen Finanzierung bei der Y <<<Bank AG>>> zu deren Gunsten verpfändet 
worden. Durch die für den Kreditnehmer ...
```

FP: `Bank AG` (organisation)

```
... Vertragsbeginn in Höhe von 52.000 € beantragt. Lt. Angaben der X 
<<<Lebensversicherungs AG>>> handelt es sich deshalb nicht um laufende, im Wesentlichen ...
```

FP: `Lebensversicherungs AG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz.in Maria van Birgelen` (person)
- `Leif Bartheld` (person)
- `Arlenweg 4X, 5261 Haslau, Österreich` (address)

**Example 2**

**False Positives:**

```
... nur ein Viertel 
des Bezuges der X Österreich und jener der Y <<<Pensions AG>>> als ganzjähriger Bezug 
auszuscheiden. Es komme jedoch die ...
```

FP: `Pensions AG` (organisation)

```
... steuerpflichtige 
Einkünfte bezogen:  
Firmenkassenpension der Y <<<Pension AG>>> von 1.1. – 31.12.2019 
Berufsunfähigkeitspension PVA 1.2. – ...
```

FP: `Pension AG` (organisation)

```
...
Tarif zu versteuernde Bezüge: 
X 1.1. – 30.4.2019 17.416,52 
Y <<<Pension AG>>>  1.1. – 31.12.2019 2.688,00 
Pensionsversicherungsanstalt 28.11.2019 ...
```

FP: `Pension AG` (organisation)

```
... gegenständlichen Fall betrifft dies 
ausschließlich die Bezüge der Y <<<Pension AG>>>. Diese Bezüge von 2.688,00 Euro hat das Finanzamt 
bei Berechnung ...
```

FP: `Pension AG` (organisation)

```
... steuerfreien Arbeitslosengeldes) zuerst um die 
Bezüge der Y <<<Pension AG>>> und um den Jänner-Bezug der X zu vermindern und der verbleibende ...
```

FP: `Pension AG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz.in Franka Münchsmayer` (person)
- `Henriette Dempwolf` (person)
- `Hopfersbach 30, 4730 Lindbruck, Österreich` (address)
- `48-249/3886` (tax_number)
- `Henriette Dempwolf` (person)

**Example 3**

**False Positives:**

```
... Finanzamt mittels RSb versandt und von der 
Österreichischen <<<Post AG>>> der Bf. an ihrer Geschäftsanschrift am 4.3.2021 zugestellt. ...
```

FP: `Post AG` (organisation)

```
... ergibt 
sich aus dem zu den Akten liegenden Zustellnachweis der <<<Post AG>>> vom 4.3.2021. 
1 von 7
Seite 2 von 7 
 
 
Mit Schreiben vom ...
```

FP: `Post AG` (organisation)

**✅ Gold Entities:**
- `Laurentia Schnellert` (person)
- `Balzerlen 15l, 9334 Guttaringberg, Österreich` (address)

**Example 4**

**False Positives:**

```
... zustehe. Zusätzlich legte er eine Quittung der Österreichische <<<Post AG>>> vom 
11.11.2019 über einen per Einschreiben versendeten Brief ...
```

FP: `Post AG` (organisation)

```
... Quittung vom 11.11.2019 auch ein Schreiben der Österreichische <<<Post AG>>> vom 
24.2.2020 betreffend Nachforschung zur Aufgabenummer Nr. ...
```

FP: `Post AG` (organisation)

```
... Aufgabenummer 
Nr. mit dem vorgelegten Schreiben der Österreichische <<<Post AG>>> vom 24.2.2020 erbracht 
worden sei. Ob bzw. welche Dokumente/Unterlagen ...
```

FP: `Post AG` (organisation)

```
...
Beschwerde) mit dem vorgelegten Schreiben der Österreichische <<<Post AG>>> vom 24.2.2020 
gelungen sei. 
Das Bundesfinanzgericht teilt ...
```

FP: `Post AG` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof.in Mag.a Brunhild Stieglmaier` (person)
- `Bühelstauden 7, 4030 Linz, Österreich` (address)
- `40-192/1103` (tax_number)

</details>

---

## `company_kg_general`

**F1:** 0.021 | **Precision:** 0.055 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches generic company names ending in 'KG', ensuring the name starts with a capitalized word and has at least one preceding word, excluding common non-entity prefixes.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+|\s+-\s+[A-Z][a-zA-Z]+|\s+&\s+[A-Z][a-zA-Z]+|\s+\+\s+[A-Z][a-zA-Z]+)+\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.055 | 0.013 | 0.021 | 127 | 7 | 120 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 120 | 536 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Beschwerdeführer (kurz: Bf.) war im Jahr 2018 zu 60% an der <<<WOD Sicherheit KG>>>  und zu 33,33% an 
der Zumholte Verlag OG  beteiligt. Unternehmensgegenstand ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... stellte das Finanzamt die gemeinschaftlichen Einkünfte 2018 der 
<<<WOD Sicherheit KG>>>  mit 48.094,37 Euro und den auf die Beteiligung an der KG entfallenden ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
...
2018 ein, er habe die Einkünfte aus seiner Beteiligung an der <<<WOD Sicherheit KG>>>  im Jahr 2018 nicht 
mehr erhalten, weshalb dieser Anteil in ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... Zuflussprinzip zu beachten. Im Jahr 2018 seien ihm 
keine Einnahmen der <<<WOD Sicherheit KG>>>  zugeflossen, weswegen diese auch nicht der 
Einkommensteuer ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

```
... erneut, die anteiligen 
Einkünfte von der Beteiligung an der <<<WOD Sicherheit KG>>>  2018 aus der Einkommensteuerfestsetzung 
auszunehmen.  
Am ...
```

| Predicted | Gold |
|---|---|
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |
| `WOD Sicherheit KG` | `WOD Sicherheit KG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Schroateck 20, 8342 Ebersdorf, Österreich, vertreten durch <<<HD Steuerberater GmbH & Co KG>>>, Höchster 
Str. 51a, 6972 Fußach, über die Beschwerde vom 19. ...
```

FP: `HD Steuerberater GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Techn R Silke Altpeter` (person)
- `Schroateck 20, 8342 Ebersdorf, Österreich` (address)

**Example 1**

**False Positives:**

```
...
Verlustanteil von 3.111,10 € aus einer Beteiligung des IS an der <<<XY Holding GmbH & Co KG>>>, 
FN 777777a, StNr 77-777/7777a (nachfolgend XY- KG) enthalten, ...
```

FP: `XY Holding GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz.in Milena Cofala` (person)
- `Kira Junggunst` (person)
- `Kreuzbichlstraße 15k, 4890 Unterrain, Österreich` (address)
- `93-986/8725` (tax_number)
- `FA Klosterneuburg` (organisation)

**Example 2**

**False Positives:**

```
... Rittschein, Österreich, vertreten durch Copilot Unternehmens- und <<<Steuerberatungs 
GmbH & Co KG>>>, Littrowgasse 7, 1180 Wien, über folgende Beschwerden gegen ...
```

FP: `Steuerberatungs 
GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Karsten Busatis` (person)
- `Lungaweg 96, 8333 Breitenfeld an der Rittschein, Österreich` (address)
- `34-796/1007` (tax_number)
- `Karsten Busatis` (person)

**Example 3**

**False Positives:**

```
... Außerbergweg 6, 4451 Sand, Österreich, vertreten durch HLB Prüf-<<<Treuhand GmbH & Co KG>>>, Berggasse 16, 
1090 Wien, über die Beschwerde vom 3. November ...
```

FP: `Treuhand GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Dagobert Schimmack` (person)
- `Außerbergweg 6, 4451 Sand, Österreich` (address)
- `07-354/5950` (tax_number)

**Example 4**

**False Positives:**

```
... ob dieses Vorbringen den Tatsachen entspricht oder 
nicht.  
<<<Die WOD Sicherheit KG>>>  hat ihren Gewinn nach § 4 Abs. 3 EStG 1988 ermittelt. Wird ...
```

FP: `Die WOD Sicherheit KG` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Hagen Jorkuweit` (person)
- `Priv.-Doz.in Catharina Tenner` (person)
- `Dr. Adolf Bastl` (person)
- `Mag. Andreas Pritzkat` (person)
- `PhD Marcel Kizilpinar, MSc` (person)
- `Hohen 73, 5133 Lohnsberg, Österreich` (address)
- `WOD Sicherheit KG` (organisation)
- `Zumholte Verlag OG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `Zumholte Verlag OG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)
- `WOD Sicherheit KG` (organisation)

</details>

---

## `specific_org_waldtouristik`

**F1:** 0.018 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'WaldTouristik Technologien'.

**Content:**
```
\bWaldTouristik\s+Technologien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.018 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 35 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Beschwerdeführer, dass er in keiner anderen Firma außer der Firma Holz 
<<<WaldTouristik Technologien>>>  beschäftigt gewesen sei, dies vom 01.01.2018 bis 26.08.2018. ...
```

| Predicted | Gold |
|---|---|
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |

```
... Beschwerdeführer vom 27.8.2018 bis 21.12.2018 bei der Firma 
<<<WaldTouristik Technologien>>>  in Österreich als Forstarbeiter beschäftigt gewesen. Aus den ...
```

| Predicted | Gold |
|---|---|
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |

```
... Österreich  gehabt habe. Als Unterkunftgeber sei die Firma Holz 
<<<WaldTouristik Technologien>>>  GmbH registriert gewesen. Dem Finanzamt lägen keine weiteren ...
```

| Predicted | Gold |
|---|---|
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |

```
... Arbeitgeber im Zeitraum 27.08.2018 bis 21.12.2018 fungierte die Holz 
<<<WaldTouristik Technologien>>>  GmbH. Der Beschwerdeführer hat für den streitgegenständlichen ...
```

| Predicted | Gold |
|---|---|
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |

```
... dass der Beschwerdeführer ausschließlich bei der Firma Holz <<<WaldTouristik Technologien>>> 
gearbeitet habe. Aus dem Gesamtzusammenhang ist das Begehren ...
```

| Predicted | Gold |
|---|---|
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |
| `WaldTouristik Technologien` | `WaldTouristik Technologien` |

</details>

---

## `specific_org_keltrizor`

**F1:** 0.018 | **Precision:** 1.000 | **Recall:** 0.009  

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
| 1.000 | 0.009 | 0.018 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 125 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... durch den Richter Mag. Peter Bilger in der Beschwerdesache 
<<<Keltrizor Handel>>>, Sterzinger Weg 11, 3902 Schoberdorf, Österreich, über die ...
```

| Predicted | Gold |
|---|---|
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |

```
...
aufgelösten sowie am 6. Juli 2022 im Firmenbuch gelöschten <<<Keltrizor Handel>>>  KG. Kommanditistin 
mit einer Beteiligung in Höhe von 45% ...
```

| Predicted | Gold |
|---|---|
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |

```
... 
Die rechtswidrigen vorläufigen Feststellungsbescheide der <<<Keltrizor Handel>>>  KG für die Jahre 2011 
und 2012 seien im Jahr 2013 zugestellt ...
```

| Predicted | Gold |
|---|---|
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |

```
... für die Erlassung 
endgültiger Einkommensteuerbescheide an <<<Keltrizor Handel>>>  und Shakira von Dittrich  bereits mit 
Ablauf des Jahres 2013 ...
```

| Predicted | Gold |
|---|---|
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |

```
... 23.11.2020, Ra 2019/15/0152).  
Der Einwand gegen die an die <<<Keltrizor Handel>>>  KG gerichteten Feststellungsbescheide 2011 bis 2016, 
diese ...
```

| Predicted | Gold |
|---|---|
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |
| `Keltrizor Handel` | `Keltrizor Handel` |

</details>

---

## `specific_org_fa_tirol_ost`

**F1:** 0.018 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'FA Tirol Ost'.

**Content:**
```
\bFA\s+Tirol\s+Ost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.018 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 304 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... betreffend Beschwerde 
vom 06.07.2007 gegen die Bescheide des <<<FA Tirol Ost>>>  vom 13.09.2011 und 14.09.2011 
beschlossen: 
Der Vorlageantrag ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 1**

```
... Parteien 
Isidor Ollerdißen (Beschwerdeführer), Stadt1, und <<<FA Tirol Ost>>>  als Amtspartei und als 
Gesamtrechtsnachfolger des Finanzamtes ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 2**

```
... September 
2012 für Nachname 1 R und Nachname 1 A seien nun beim <<<FA Tirol Ost>>>  eingebracht worden. Der 
Anspruch auf Kinderfreibeträge und ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 3**

```
...
16.Oktober 2015 ausgefertigten Bescheid der belangten Behörde <<<FA Tirol Ost>>>, nunmehr 
Finanzamt Tirol Ost, betreffend Einkommensteuer für ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 4**

```
... 
die Beschwerde vom 20. April 2018 gegen die Bescheide des <<<FA Tirol Ost>>>  vom 16. März 2018 
betreffend Wiederaufnahme des Verfahrens ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

</details>

---

## `specific_org_stadte_energie`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches the specific entity 'StadtEnergie Holding'.

**Content:**
```
\bStadtEnergie\s+Holding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.015 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 536 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
...
2) Dipl.-Ing. Angelika Bartholomai  als Rechtsnachfolger der <<<StadtEnergie Holding>>>, Außerbofa 5-8, 2264 Jedenspeigen, Österreich, vertreten durch ...
```

| Predicted | Gold |
|---|---|
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |

```
...
Gruppenträger 28-587/0533 Dipl.-Ing. Angelika Bartholomai  als RNF der <<<StadtEnergie Holding>>> 
 
 
1 von 39
Seite 2 von 39 
 
 
1. Entscheidungsgründe 
I. ...
```

| Predicted | Gold |
|---|---|
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |

```
... das Gruppenmitglied Annemie Bott  als auch der Gruppenträger <<<StadtEnergie Holding>>> 
(28-587/0533). Begründend wurde ausgeführt: „Die Wiederaufnahme ...
```

| Predicted | Gold |
|---|---|
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |

```
... dem Gruppenträger Dipl.-Ing. Angelika Bartholomai (vormals <<<StadtEnergie Holding>>>). 
Die PhD Marianne Yener (im Beschwerdezeitraum Laskowsky ...
```

| Predicted | Gold |
|---|---|
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |
| `StadtEnergie Holding` | `StadtEnergie Holding` |

</details>

---

## `specific_org_hoerup_ag`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Hörup Gastronomie AG'.

**Content:**
```
\bHörup\s+Gastronomie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.015 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 66 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Einkünfte. Er stand ganzjährig in einem 
Dienstverhältnis zur <<<Hörup Gastronomie AG>>>. Dienstverhältnisse zu anderen Arbeitgebern bestanden nicht. ...
```

| Predicted | Gold |
|---|---|
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |

```
... Dienstverhältnisse zu anderen Arbeitgebern bestanden nicht. 
Die <<<Hörup Gastronomie AG>>>  berücksichtigte im Rahmen der Lohnverrechnung weder Freibeträge ...
```

| Predicted | Gold |
|---|---|
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |

```
... ein 
Pendlerpauschale. An Absetzbeträgen wurden seitens der <<<Hörup Gastronomie AG>>>  im Rahmen der 
Lohnverrechnung (nur) der „normale“ (dh nicht ...
```

| Predicted | Gold |
|---|---|
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |

```
... geborene Tochter des Bf) berücksichtigt. Der Bf 
erhielt von der <<<Hörup Gastronomie AG>>>  keinen Kinderbetreuungszuschuss iSd § 3 Abs 1 Z 13 lit b EStG ...
```

| Predicted | Gold |
|---|---|
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |
| `Hörup Gastronomie AG` | `Hörup Gastronomie AG` |

</details>

---

## `specific_org_klein_vorholt`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

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
| 1.000 | 0.007 | 0.015 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 272 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Sachverhalt  
Der Bf. war im Beschwerdezeitraum durchgehend bei der <<<Klein-Vorholt KI GMBH>>>  angestellt. Im 
Vorjahr 2022 war der Bf. zunächst bis einschließlich ...
```

| Predicted | Gold |
|---|---|
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |

```
... zunächst bei der Firma Gogel Daten GMBH  und im 
Folgenden bei der <<<Klein-Vorholt KI GMBH>>>  beschäftigt war, ergibt sich einerseits aus dem vom Bf. mit ...
```

| Predicted | Gold |
|---|---|
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |

```
... daraus.   
Dass der Bf. im Beschwerdezeitraum durchgehend bei der <<<Klein-Vorholt KI GMBH>>>  angestellt war, 
ergibt sich aus dem an das Finanzamt übermittelten ...
```

| Predicted | Gold |
|---|---|
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |

```
...
Dienstverhältnisse bei den Firmen Gogel Daten GMBH  und im Folgenden bei der <<<Klein-Vorholt KI GMBH>>> 
einbehalten und geleistet wurden.  
3 von 6
Seite 4 von 6 ...
```

| Predicted | Gold |
|---|---|
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |
| `Klein-Vorholt KI GMBH` | `Klein-Vorholt KI GMBH` |

</details>

---

## `specific_org_fa_judenburg`

**F1:** 0.015 | **Precision:** 0.800 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Judenburg Liezen'.

**Content:**
```
\bFinanzamt\s+Judenburg\s+Liezen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.007 | 0.015 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 1 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Beschwerde vom 5. Dezember 2022 gegen den 
Abweisungsbescheid des <<<Finanzamt Judenburg Liezen>>>  vom 25. November 2022 betreffend Aufhebung des 
Einkommensteuerbescheides ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 1**

```
...
über die Beschwerde vom 16. Mai 2022 gegen den Bescheid des <<<Finanzamt Judenburg Liezen>>>  vom 28. Februar 
2022 betreffend Wiedereinsetzung der Frist ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 2**

```
... über die Beschwerde vom 25. Juli 2019 gegen den Bescheid des <<<Finanzamt Judenburg Liezen>>>  vom 
17. Juli 2019 betreffend Abweisung eines Antrages auf ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 3**

```
... über die Beschwerde vom 1. April 2020 gegen den 
Bescheid des <<<Finanzamt Judenburg Liezen>>>  vom 25. März 2020 zu Steuernummer 29-755/4143, mit dem ein ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Beschwerde vom 29.3.2017 gegen den Bescheid der belangten 
Behörde <<<Finanzamt Judenburg Liezen>>> vom 21.3.2017 betreffend Einkommensteuer 
(Arbeitnehmerveranlagung) ...
```

FP: `Finanzamt Judenburg Liezen` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Benedikt Rüecker` (person)
- `Prof.in Brunhild Nußbaumer` (person)
- `Schloss Rosegg 11, 4120 Unterfeuchtenbach, Österreich` (address)

</details>

---

## `tax_office_fa_graz_stadt`

**F1:** 0.015 | **Precision:** 0.800 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'FA Graz-Stadt'.

**Content:**
```
\bFA\s+Graz-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.007 | 0.015 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 1 | 374 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... über die Beschwerde vom 23. Juni 2019 gegen die Bescheide des <<<FA Graz-Stadt>>> 
vom 23. Mai 2019 bzw. 19.08.2019 betreffend Umsatz- und Einkommensteuer ...
```

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 1**

```
... einer 
vorgelegten Rechnung vom 26.8.2010 geht hervor, dass die <<<FA Graz-Stadt>>>  eine Wartung des 
Treppenlifts zu einem Gesamtbetrag von 260,40 ...
```

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 2**

```
... über die Beschwerde vom 2. August 2021 gegen den Bescheid des <<<FA Graz-Stadt>>> 
vom 27. Juli 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 3**

```
... betreffend Beschwerde vom 18. Februar 2022 gegen die Bescheide des 
<<<FA Graz-Stadt>>>  vom 14. Dezember 2021 betreffend Körperschaftsteuer 2016, ...
```

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... hat für 
sämtliche Zeiträume eine Umsatzsteuererklärung beim <<<FA Graz-Stadt>>> abzugeben. Auf die 
Niederschrift wird verwiesen. 
Tz. 8 Vorsteuer: ...
```

FP: `FA Graz-Stadt` (organisation)

**✅ Gold Entities:**
- `KommR Zeno Henricy` (person)
- `Kaplan Herzlik Straße 2, 4962 Gundholling, Österreich` (address)
- `89-403/3092` (tax_number)

</details>

---

## `specific_org_gogel`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

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
| 1.000 | 0.006 | 0.011 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 273 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... war der Bf. zunächst bis einschließlich August bei der Firma <<<Gogel Daten GMBH>>> 
beschäftigt. Ab September 2022 begann sein Dienstverhältnis ...
```

| Predicted | Gold |
|---|---|
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |

```
... Feststellung, wonach der Bf. im Jahr 2022 zunächst bei der Firma <<<Gogel Daten GMBH>>>  und im 
Folgenden bei der Klein-Vorholt KI GMBH  beschäftigt ...
```

| Predicted | Gold |
|---|---|
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |

```
... diesem Jahr bestandenen 
Dienstverhältnisse bei den Firmen <<<Gogel Daten GMBH>>>  und im Folgenden bei der Klein-Vorholt KI GMBH 
einbehalten ...
```

| Predicted | Gold |
|---|---|
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |
| `Gogel Daten GMBH` | `Gogel Daten GMBH` |

</details>

---

## `specific_org_see_garttalder`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'See Garttalder'.

**Content:**
```
\bSee\s+Garttalder\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 59 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... deutschen Steuerberaters: 
Wirtschaftlicher Eigentümer der <<<See Garttalder>>>  ist als oberste Konzernmutter die KM. Die 
Gesellschaft ist ...
```

| Predicted | Gold |
|---|---|
| `See Garttalder` | `See Garttalder` |
| `See Garttalder` | `See Garttalder` |
| `See Garttalder` | `See Garttalder` |

```
... der Geschäftsführung die österreichische GmbH, in dem Fall <<<See Garttalder>>> 
eingeben sollen und den österreichischen Geschäftsführer als ...
```

| Predicted | Gold |
|---|---|
| `See Garttalder` | `See Garttalder` |
| `See Garttalder` | `See Garttalder` |
| `See Garttalder` | `See Garttalder` |

```
... den deutscehn Steuerberater der 
Muttergesellschaft der Firma <<<See Garttalder>>>  gebeten und doch die Identität und die Daten der 
Vorstände ...
```

| Predicted | Gold |
|---|---|
| `See Garttalder` | `See Garttalder` |
| `See Garttalder` | `See Garttalder` |
| `See Garttalder` | `See Garttalder` |

</details>

---

## `specific_org_laskowsky`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'Laskowsky Umwelt'.

**Content:**
```
\bLaskowsky\s+Umwelt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 537 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... abzuweisen.“ 
Ein Firmenbuchauszug vom 9.7.2024 ergab, dass die <<<Laskowsky Umwelt>>>  seit 15.5.2024 aufgrund 
einer Neufassung des Gesellschaftsvertrages ...
```

| Predicted | Gold |
|---|---|
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |

```
... Annemie Bott.  
Die PhD Marianne Yener (im Beschwerdezeitraum <<<Laskowsky Umwelt>>>) war im Jahr 2010 Gruppenmittglied 
der Unternehmensgruppe ...
```

| Predicted | Gold |
|---|---|
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |

```
... StadtEnergie Holding). 
Die PhD Marianne Yener (im Beschwerdezeitraum <<<Laskowsky Umwelt>>>) ist als Rechtsnachfolgerin der 
Annemie Bott  auch partielle ...
```

| Predicted | Gold |
|---|---|
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |
| `Laskowsky Umwelt` | `Laskowsky Umwelt` |

</details>

---

## `specific_org_luehrig_hundertmarck`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'Luehrig + Hundertmarck Holz GMBH'.

**Content:**
```
\bLuehrig\s+\+\s+Hundertmarck\s+Holz\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 101 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... ist, ob der Beschwerdeführer (Bf.) infolge der Insolvenz der <<<Luehrig + Hundertmarck Holz GMBH>>> 
(Primärschuldnerin) als ehemaliger Geschäftsführer für die ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

```
... ehemaliger Geschäftsführer 
für die aushaftende Abgabenschuld der <<<Luehrig + Hundertmarck Holz GMBH>>>  in Höhe von Euro 396.769,30 in 
Anspruch genommen. 
Dagegen ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

```
... Oktober 2014, sowie ab 18. Dezember 2014 
Geschäftsführer der <<<Luehrig + Hundertmarck Holz GMBH>>> (Primärschuldnerin). 
Mit Beschluss des Landesgerichts Wr. ...
```

| Predicted | Gold |
|---|---|
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |
| `Luehrig + Hundertmarck Holz GMBH` | `Luehrig + Hundertmarck Holz GMBH` |

</details>

---

## `specific_org_enns`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Enns Werkal GMBH'.

**Content:**
```
\bEnns\s+Werkal\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 284 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... durch die Richterin Dr. Lisa Pucher in der Beschwerdesache 
<<<Enns Werkal GMBH>>>, Föhrenwald III 19, 3140 Pottenbrunn, Österreich, vertreten ...
```

| Predicted | Gold |
|---|---|
| `Enns Werkal GMBH` | `Enns Werkal GMBH` |
| `Enns Werkal GMBH` | `Enns Werkal GMBH` |

```
... Bundes-Verfassungsgesetz 
(B-VG) nicht zulässig. 
Begründung 
Die <<<Enns Werkal GMBH>>>  hat mit Eingabe vom 07.08.2024 gemäß § 284 Abs 1 BAO 
Säumnisbeschwerden ...
```

| Predicted | Gold |
|---|---|
| `Enns Werkal GMBH` | `Enns Werkal GMBH` |
| `Enns Werkal GMBH` | `Enns Werkal GMBH` |

</details>

---

## `specific_org_fa_deutschlandsberg`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'FA Deutschlandsberg Leibnitz Voitsberg'.

**Content:**
```
\bFA\s+Deutschlandsberg\s+Leibnitz\s+Voitsberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 82 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... die Beschwerde vom 7. Februar 2024 
gegen den Bescheid des <<<FA Deutschlandsberg Leibnitz Voitsberg>>>  vom 10. Jänner 2024 betreffend Abweisung eines Antrages 
auf ...
```

| Predicted | Gold |
|---|---|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

**Example 1**

```
... Bescheides des 
Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: <<<FA Deutschlandsberg Leibnitz Voitsberg>>>), jeweils  vom 11. Dezember 
2014 betreffend  
 Säumniszuschlag ...
```

| Predicted | Gold |
|---|---|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

</details>

---

## `specific_org_zumholte`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Zumholte Verlag OG'.

**Content:**
```
\bZumholte\s+Verlag\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 303 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... 2018 zu 60% an der WOD Sicherheit KG  und zu 33,33% an 
der <<<Zumholte Verlag OG>>>  beteiligt. Unternehmensgegenstand der beiden Gesellschaften ...
```

| Predicted | Gold |
|---|---|
| `Zumholte Verlag OG` | `Zumholte Verlag OG` |
| `Zumholte Verlag OG` | `Zumholte Verlag OG` |

```
... 5.3.2020 stellte es die gemeinschaftlichen Einkünfte 2018 der <<<Zumholte Verlag OG>>> 
mit 427.541,96 Euro und den auf die Beteiligung an der OG ...
```

| Predicted | Gold |
|---|---|
| `Zumholte Verlag OG` | `Zumholte Verlag OG` |
| `Zumholte Verlag OG` | `Zumholte Verlag OG` |

</details>

---

## `specific_org_dgcv_ecommerce`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'DGCV E‑Commerce GMBH' with em-dash.

**Content:**
```
\bDGCV\s+E\u2011Commerce\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 90 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Dienstvertrages des Beschwerdeführers mit seinem Dienstgeber <<<DGCV E‑Commerce GMBH>>>  in Sankt Oswald ob Eibiswald, sowie mehrere teilweise unleserliche ...
```

| Predicted | Gold |
|---|---|
| `DGCV E‑Commerce GMBH` | `DGCV E‑Commerce GMBH` |
| `DGCV E‑Commerce GMBH` | `DGCV E‑Commerce GMBH` |

```
... Monaten befristetes nichtselbständiges 
Dienstverhältnis bei <<<DGCV E‑Commerce GMBH>>>  in Sankt Oswald ob Eibiswald. Ab 01.05.2020 mietete der 
Beschwerdeführer ...
```

| Predicted | Gold |
|---|---|
| `DGCV E‑Commerce GMBH` | `DGCV E‑Commerce GMBH` |
| `DGCV E‑Commerce GMBH` | `DGCV E‑Commerce GMBH` |

</details>

---

## `specific_org_volkswien`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'VOLKSBANK WIEN'.

**Content:**
```
\bVOLKSBANK\s+WIEN\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 182 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... von 1.8.1975 bis zu ihrer Pensionierung am 31.12.2013 in der 
<<<VOLKSBANK WIEN>>>  als Beraterin von kleinen und mittleren Unternehmen beschäftigt. ...
```

| Predicted | Gold |
|---|---|
| `VOLKSBANK WIEN` | `VOLKSBANK WIEN` |
| `VOLKSBANK WIEN` | `VOLKSBANK WIEN` |

```
... 359 Abs. 1 StPO schuldig 
gesprochen, der Privatbeteiligten <<<VOLKSBANK WIEN>>>  binnen 14 Tagen 312.651,66 € samt 4 % Zinsen 
seit 9.10.2017 ...
```

| Predicted | Gold |
|---|---|
| `VOLKSBANK WIEN` | `VOLKSBANK WIEN` |
| `VOLKSBANK WIEN` | `VOLKSBANK WIEN` |

</details>

---

## `specific_org_ugqq`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'UGQQ Verlag OG'.

**Content:**
```
\bUGQQ\s+Verlag\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 5 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... 4.6.2013 wurde der belangten Behörde der am 25.4.2013 zwischen der <<<UGQQ Verlag OG>>> (Vermieterin) und der Beschwerdeführerin (Mieterin) abgeschlossene ...
```

| Predicted | Gold |
|---|---|
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |

```
... vorliegendem Mietvertrag, unterzeichnet am 25.4.2013, werden von der <<<UGQQ Verlag OG>>>  als Vermieterin Geschäftsräumlichkeiten im Ausmaß von etwa ...
```

| Predicted | Gold |
|---|---|
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |
| `UGQQ Verlag OG` | `UGQQ Verlag OG` |

</details>

---

## `tax_office_finanzamt_schwechat`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Schwechat Gerasdorf'.

**Content:**
```
\bFinanzamt\s+Schwechat\s+Gerasdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 379 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Dr. Walter Ganster, Steuerberater in 9100 
Völkermarkt und <<<Finanzamt Schwechat Gerasdorf>>>  als Amtspartei und als Gesamtrechtsnachfolger des Finanzamtes ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

**Example 1**

```
... die Beschwerde vom 31. Dezember 2012 gegen den Bescheid des 
<<<Finanzamt Schwechat Gerasdorf>>> (nunmehr Finanzamt FA) vom 27. November 2012 betreffend Körperschaftsteuer ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Schwechat Gerasdorf` | `Finanzamt Schwechat Gerasdorf` |

</details>

---

## `specific_org_fa_vorarlberg`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Vorarlberg'.

**Content:**
```
\bFinanzamt\s+Vorarlberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 120 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... betreffend Beschwerde vom 13. November 2023 gegen den 
Bescheid des <<<Finanzamt Vorarlberg>>>  vom 24. Oktober 2023 betreffend Haftungsbescheid / Sonstige ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Vorarlberg` | `Finanzamt Vorarlberg` |

**Example 1**

```
... über die Beschwerde vom 7. Mai 2018 gegen den Bescheid des <<<Finanzamt Vorarlberg>>>  vom 
20. April 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Vorarlberg` | `Finanzamt Vorarlberg` |

</details>

---

## `specific_org_fa_baden`

**F1:** 0.007 | **Precision:** 0.182 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Baden Mödling'.

**Content:**
```
\bFinanzamt\s+Baden\s+M\xf6dling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.182 | 0.004 | 0.007 | 11 | 2 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 9 | 281 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Wiedergut, Steuerberaterin in 9500 Villach, 
gegen die Bescheide des <<<Finanzamt Baden Mödling>>>  vom 23.1.2014 (Gesamtrechtsnachfolger Finanzamt für 
Großbetriebe) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

**Example 1**

```
... die Beschwerde vom 16. Oktober 2023 gegen den Bescheid des <<<Finanzamt Baden Mödling>>> 
vom 13. September 2023 betreffend die Zurückweisung eines ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... 2020 gegen den Bescheid des 
Finanzamtes Österreich (vormals <<<Finanzamt Baden Mödling>>>) vom 13. November 2020 
betreffend Einkommensteuer 2015, Steuernummer ...
```

FP: `Finanzamt Baden Mödling` (organisation)

**✅ Gold Entities:**
- `Lara Pfeiferl` (person)
- `Obernbergerstraße 76, 8253 Schrimpf, Österreich` (address)
- `85-636/8182` (tax_number)

**Example 1**

**False Positives:**

```
... gründet den festgestellten Sachverhalt auf den Inhalt der vom 
<<<Finanzamt Baden Mödling>>> vorgelegten Verwaltungsakten. Der festgestellte Sachverhalt ...
```

FP: `Finanzamt Baden Mödling` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Jasmin van der Beck` (person)
- `OMedR Josefine Weyler` (person)
- `Mariensiedlung 4, 6672 Haller, Österreich` (address)

**Example 2**

**False Positives:**

```
... übermittelt.  
4 von 13
Seite 5 von 13 
 
 
Vom vormals zuständigen <<<Finanzamt Baden Mödling>>> wurden im beschwerdegegenständlichen 
Zeitraum folgende Umsatzsteuer(erst)bescheide ...
```

FP: `Finanzamt Baden Mödling` (organisation)

**✅ Gold Entities:**
- `Camilla Oberholzner` (person)
- `Camilla Oberholzner` (person)

**Example 3**

**False Positives:**

```
... I (Zurückweisung) 
1. Sachverhalt 
Am 20.03.2015 wurden vom <<<Finanzamt Baden Mödling>>> die Umsatzsteuerbescheide 2011 und 
2012 erlassen. 
Dagegen ...
```

FP: `Finanzamt Baden Mödling` (organisation)

**✅ Gold Entities:**
- `Traude Schellscheid` (person)
- `Heidenreichring 11, 6123 Umlberg, Österreich` (address)
- `50-793/3376` (tax_number)

**Example 4**

**False Positives:**

```
... wurde am 7.08.2015 die geforderte Ansässigkeitsbescheidung beim <<<Finanzamt 
Baden Mödling>>> eingeholt und der Lufthansa übermittelt. Aus der Kontrollmitteilung ...
```

FP: `Finanzamt 
Baden Mödling` (organisation)

**✅ Gold Entities:**
- `Brigitte Vosbein` (person)
- `16-601/9943` (tax_number)
- `Weißpyhra 96, 5722 Gaisbichl, Österreich` (address)

</details>

---

## `specific_org_steinfurt`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Steinfurtglanz-Landwirtschaft'.

**Content:**
```
\bSteinfurtglanz-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 71 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Richter Mag. Silvester Kissel  in der Beschwerdesache der 
<<<Steinfurtglanz-Landwirtschaft>>>, An der Westumfahrung 142, 5300 Hallwang, Österreich  betreffend ...
```

| Predicted | Gold |
|---|---|
| `Steinfurtglanz-Landwirtschaft` | `Steinfurtglanz-Landwirtschaft` |

</details>

---

## `specific_org_rnv`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'RNV Digital'.

**Content:**
```
\bRNV\s+Digital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 10 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Univ.-Prof.in Gwendolin Lindlein  in der Beschwerdesache der 
<<<RNV Digital>>>, vertreten durch Steuerberater X, über die Beschwerde vom 27. ...
```

| Predicted | Gold |
|---|---|
| `RNV Digital` | `RNV Digital` |

</details>

---

## `specific_org_pfendtner`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Pfendtner Textil'.

**Content:**
```
\bPfendtner\s+Textil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 82 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Richterin Univ.-Prof.in Xenia Goedeker  in der Beschwerdesache der 
<<<Pfendtner Textil>>>, Fallenberg 13, 4932 Ramerding, Österreich, vertreten durch ...
```

| Predicted | Gold |
|---|---|
| `Pfendtner Textil` | `Pfendtner Textil` |

</details>

---

## `specific_org_raiffeisen_hall`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisen Rionalbank Hall in Tirol'.

**Content:**
```
\bRaiffeisen\s+Rionalbank\s+Hall\s+in\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 186 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... brutto. Die Finanzierung erfolgte über ein Leasing mit der 
<<<Raiffeisen Rionalbank Hall in Tirol>>>. Die Eckdaten des Leasings stellen sich folgendermaßen dar: ...
```

| Predicted | Gold |
|---|---|
| `Raiffeisen Rionalbank Hall in Tirol` | `Raiffeisen Rionalbank Hall in Tirol` |

</details>

---

## `specific_org_psomadakis`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Psomadakis Touristik'.

**Content:**
```
\bPsomadakis\s+Touristik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 191 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Richterin Dr.in Emma Stranghöhner  in der Beschwerdesache der 
<<<Psomadakis Touristik>>>, Andreas-Rainer-Weg 13, 9111 Mittertrixen, Österreich, über ...
```

| Predicted | Gold |
|---|---|
| `Psomadakis Touristik` | `Psomadakis Touristik` |

</details>

---

## `specific_org_donau_druck`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Donau-Druck'.

**Content:**
```
\bDonau-Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 141 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Richterin Univ.-Prof.in Alice Carolus  in der Beschwerdesache der 
<<<Donau-Druck>>>, Oberweg 20, 2493 Lichtenwörth, Österreich, über die Beschwerde ...
```

| Predicted | Gold |
|---|---|
| `Donau-Druck` | `Donau-Druck` |

</details>

---

## `specific_org_fa_purkersdorf`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'FA Purkersdorf'.

**Content:**
```
\bFA\s+Purkersdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 87 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... die Beschwerden vom 12. März 2024 
gegen die Bescheide des <<<FA Purkersdorf>>>  vom 12. Februar 2024 betreffend Umsatzsteuer 2020 und 
betreffend ...
```

| Predicted | Gold |
|---|---|
| `FA Purkersdorf` | `FA Purkersdorf` |

</details>

---

## `specific_org_mur_alver`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Mur Alver OG'.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 307 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... nicht der Bf als Empfänger aufscheine und eine 
Rechnung der „<<<Mur Alver OG>>>“ Leuchten aus dem Luxussegment anführe. Diese seien daher 
...
```

| Predicted | Gold |
|---|---|
| `Mur Alver OG` | `Mur Alver OG` |

</details>

---

## `specific_org_zoruniglanz`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Zoruniglanz'.

**Content:**
```
\bZoruniglanz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 7 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... Richter Priv.-Doz. Patrick Szymonski  in der Beschwerdesache der 
<<<Zoruniglanz>>>, Nadelbach 22, 3812 Sieghartsles, Österreich, betreffend Beschwerde ...
```

| Predicted | Gold |
|---|---|
| `Zoruniglanz` | `Zoruniglanz` |

</details>

---

## `specific_org_fa_waldviertel`

**F1:** 0.004 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'FA Waldviertel'.

**Content:**
```
\bFA\s+Waldviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.002 | 0.004 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 83 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... über die Beschwerde vom 
21. März 2023 gegen den Bescheid des <<<FA Waldviertel>>>  vom 17. Februar 2023 betreffend Nachsicht § 
236 BAO 2023 ...
```

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... 14. Juni 2021:  
Mit Abweisungsbescheid vom 04.02.2020 des <<<FA Waldviertel>>> wurde Familienbeihilfe für die 
das Kind … (Nachname die Bf.) ...
```

FP: `FA Waldviertel` (organisation)

**✅ Gold Entities:**
- `Yelec Träubel` (person)
- `Pelargonienweg 13, 4063 Rudelsdorf, Österreich` (address)
- `Karin Steilen` (person)
- `41-392/0377` (tax_number)
- `4756010962` (social_security_number)

</details>

---

## `specific_org_fa_braunau_ried_schärding`

**F1:** 0.004 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'FA Braunau Ried Schärding'.

**Content:**
```
\bFA\s+Braunau\s+Ried\s+Sch\xe4rding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.002 | 0.004 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 184 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... über die Beschwerde vom 27. März 2012 
gegen den Bescheid des <<<FA Braunau Ried Schärding>>>  bzw. Finanzamt Österreich vom 2. März 2012 betreffend 
Umsatzsteuer ...
```

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... über die Beschwerde vom 12. Juni 2012 gegen den Bescheid des <<<FA Braunau Ried 
Schärding>>> vom 9. Mai 2012 betreffend Einkommensteuer 2006 Steuernummer ...
```

FP: `FA Braunau Ried 
Schärding` (organisation)

**✅ Gold Entities:**
- `Ing. Felizia Stammschroer` (person)
- `Lötz 10, 5340 Winkl, Österreich` (address)
- `86-740/0703` (tax_number)

</details>

---

## `tax_office_finanzamt_graz_stadt`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Graz-Stadt'.

**Content:**
```
\bFinanzamt\s+Graz-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.002 | 0.004 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 3 | 543 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... die Beschwerde vom 22. Jänner 2018 gegen den Bescheid 
des <<<Finanzamt Graz-Stadt>>>  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:  ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Graz-Stadt` | `Finanzamt Graz-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Einreichung der 
Umsatzsteuererklärung 2018 am 15.5.2019 beim <<<Finanzamt Graz-Stadt>>>, wurde die Frist für den 
Antrag auf Erstattung von Vorsteuern ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

```
... Anträge auf Erstattung von Vorsteuern zuständigen Behörde 
(<<<Finanzamt Graz-Stadt>>>) eingebracht. 
Weiters ist anzumerken, wenn die Behörde die ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

```
... 
Erstattung mittels amtlich vorgeschriebenem Vordruck beim <<<Finanzamt Graz-Stadt>>> zu 
beantragen. Der Antrag ist binnen sechs Monaten nach Ablauf ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

**✅ Gold Entities:**
- `Dr.in Constanze Peest` (person)
- `Linn Damianou` (person)
- `Fürnbergstraße 3, 4730 Steinparz, Österreich` (address)
- `Finanzamt Salzburg-Land` (organisation)
- `39-261/4216` (tax_number)

</details>

---

## `specific_org_fa_gmunden`

**F1:** 0.004 | **Precision:** 0.200 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Gmunden Vöcklabruck'.

**Content:**
```
\bFinanzamt\s+Gmunden\s+V\xf6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.200 | 0.002 | 0.004 | 5 | 1 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 4 | 374 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des 
<<<Finanzamt Gmunden Vöcklabruck>>>  vom 11. Jänner 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Gmunden Vöcklabruck` | `Finanzamt Gmunden Vöcklabruck` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Gmunden“ gerichtete 
Vorlageantrag am 28. Dezember 2018 beim <<<Finanzamt Gmunden Vöcklabruck>>> einlangte, dieses 
Finanzamt jedoch sachlich und örtlich unzuständig ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

```
... Marxergasse 4, 4810 Gmunden“ und wurde 
am selben Tag beim <<<Finanzamt Gmunden Vöcklabruck>>> in Gmunden persönlich durch Einwurf in 
die „ Postbox“ der ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

```
... wurde der Vorlageantrag – zuständigkeitshalber - durch das <<<Finanzamt Gmunden 
Vöcklabruck>>> an das „Finanzamt für Gebühren und Verkehrsst. Marxerg. 4 1030 ...
```

FP: `Finanzamt Gmunden 
Vöcklabruck` (organisation)

```
... wird die Behörde im Adressfeld durch das weiterleitende Amt (<<<Finanzamt 
Gmunden Vöcklabruck>>>) selbst mit „Finanzamt für Gebühren u Verkehrsst“ bezeichnet. ...
```

FP: `Finanzamt 
Gmunden Vöcklabruck` (organisation)

**✅ Gold Entities:**
- `Ing. OMedR Albert Voulgaridou` (person)
- `Patriasdorfer Straße 4, 9634 Katlingberg, Österreich` (address)
- `07-334/2610` (tax_number)

</details>

---

## `specific_org_fa_wien`

**F1:** 0.004 | **Precision:** 0.167 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Wien 1/23'.

**Content:**
```
\bFinanzamt\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.002 | 0.004 | 6 | 1 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 5 | 191 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0**

```
... die Beschwerde vom 18. September 2020 gegen den Bescheid des 
<<<Finanzamt Wien 1/23>>>  vom 24. August 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... und 2007 vom 3.7.2009 des Finanzamtes Österreich 
(ehemals <<<Finanzamt Wien 1/23>>>) richtet, zu Recht erkannt:  
I. Der Beschwerde, insoweit sich ...
```

FP: `Finanzamt Wien 1/23` (organisation)

**✅ Gold Entities:**
- `Dietrich Mägerlein` (person)
- `Mitterfeld 2, 4813 Gmundnerberg, Österreich` (address)

**Example 1**

**False Positives:**

```
... Die weitere Begründung lautet auszugsweise wie folgt: 
„Das <<<Finanzamt Wien 1/23>>> hat datiert mit 16. August 2017 eine Beschwerdevorentscheidung ...
```

FP: `Finanzamt Wien 1/23` (organisation)

**✅ Gold Entities:**
- `Leander Neimeyer` (person)
- `Farchat 2, 4064 Mitterbachham, Österreich` (address)
- `75-448/9858` (tax_number)
- `Leander Neimeyer` (person)
- `Naaß Elektro GMBH` (organisation)
- `Bersud Möbel GMBH` (organisation)
- `Unter Heimdorf GMBH` (organisation)

**Example 2**

**False Positives:**

```
...
Bisheriger Verfahrensgang 
Mit Bescheid vom 9.12.2016 erließ das <<<Finanzamt Wien 1/23>>> einen (Sammel-)Bescheid über 
die Festsetzung von ersten Säumniszuschlägen ...
```

FP: `Finanzamt Wien 1/23` (organisation)

```
... könne. 
Mit Beschwerdevorentscheidung vom 19.1.2017 wies das <<<Finanzamt Wien 1/23>>> die 
Beschwerde als unbegründet ab und führte als Begründung ...
```

FP: `Finanzamt Wien 1/23` (organisation)

**✅ Gold Entities:**
- `Peter Wöst` (person)
- `47-984/7521` (tax_number)

**Example 3**

**False Positives:**

```
... für jedes Finanzamt mit 
Sitz in Wien, ausgenommen für das <<<Finanzamt Wien 1/23>>>; 
 2. die Organe des Finanzamts Lilienfeld St. Pölten für jedes ...
```

FP: `Finanzamt Wien 1/23` (organisation)

**✅ Gold Entities:**
- `Dr. Helmut Swionteck` (person)
- `MedR Univ.-Prof. Georg Schevalje` (person)
- `Opitzgasse 59, 4752 Achleiten, Österreich` (address)
- `Linus Schoeppe` (person)

</details>

---

## `specific_org_dias_telekom`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'DIAS Telekom Institut'.

**Content:**
```
\bDIAS\s+Telekom\s+Institut\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Raiffeisenbank Stallhofen'.

**Content:**
```
\bRaiffeisenbank\s+Stallhofen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_finanzen_tradonnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzen Tradonnex'.

**Content:**
```
\bFinanzen\s+Tradonnex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'TraunLuftfahrt Solutions'.

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

## `specific_org_houdek`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Houdek Maschinenbau'.

**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_mur`

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

## `specific_org_klusner`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Klusner&P\xe4ffgen Bildung GMBH'.

**Content:**
```
\bKlusner&P\xe4ffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_schmeltz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schmeltz Luftfahrt'.

**Content:**
```
\bSchmeltz\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_starker`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Starker Beratung'.

**Content:**
```
\bStarker\s+Beratung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_yxtg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'YXTG Maschinenbau'.

**Content:**
```
\bYXTG\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_logkeltal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Logkeltal Marine'.

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

## `specific_org_berwaldkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Berwaldkel-M\xf6bel AG'.

**Content:**
```
\bBerwaldkel-M\xf6bel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_waldtra`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Waldtra-Sicherheit'.

**Content:**
```
\bWaldtra-Sicherheit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_heimwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Heimwald-Forschung GMBH'.

**Content:**
```
\bHeimwald-Forschung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_wels`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Wels Süd'.

**Content:**
```
\bRaiffeisenbank\s+Wels\s+S\xfc\xdfer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_nowothnig`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Nowothnig Wind'.

**Content:**
```
\bNowothnig\s+Wind\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_henken`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Henken'.

**Content:**
```
\bHenken\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_roelfsen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Roelfsen Versicherung'.

**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_dorfcon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Dorfcon-Verlag'.

**Content:**
```
\bDorfcon-Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_depp`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Depp Versand'.

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

## `specific_org_talkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Talkel-Versand AG'.

**Content:**
```
\bTalkel-Versand\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_hebebrand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hebebrand Recycling AG'.

**Content:**
```
\bHebebrand\s+Recycling\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_wienerwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Wienerwald'.

**Content:**
```
\bRaiffeisenbank\s+Wienerwald\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_bezirksgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht' followed by a location, avoiding duplication.

**Content:**
```
\bBezirksgericht\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 5 | 312 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... an derselben Adresse gemeldet. Mit 9.7.2019 wurde dies vom <<<Bezirksgericht ORT>>> 
bestätigt, auch wenn der Vater in diesem Beschluss ebenso ...
```

FP: `Bezirksgericht ORT` (organisation)

**✅ Gold Entities:**
- `OSR MedR Chen Bruckmayr` (person)
- `Überfeld/Sonnenweg 44, 4691 Schlatt, Österreich` (address)
- `OSR MedR Chen Bruckmayr` (person)
- `OSR MedR Chen Bruckmayr` (person)

**Example 1**

**False Positives:**

```
... (AZ-2, AS 7). Mit weiterem 
Beschluss vom 04.03.2005 ordnete das <<<Bezirksgericht Gericht>>> die Schätzung dieser 
Liegenschaft durch den allgemein beeideten ...
```

FP: `Bezirksgericht Gericht` (organisation)

```
... der Übergabe fehlten. 
Das Versteigerungsverfahren vor dem <<<Bezirksgericht Gericht>>> wurde infolge des vorgenannten 
Vertrages mit Beschluss vom ...
```

FP: `Bezirksgericht Gericht` (organisation)

**✅ Gold Entities:**
- `Esmeralda Halbgebauer` (person)
- `Akazienplatz 349, 9634 Rauth, Österreich` (address)

**Example 2**

**False Positives:**

```
... der 
Beschwerdeführer an, dass ein Abschöpfungsverfahren beim <<<Bezirksgericht BG>>> seit Oktober 
2017 anhängig sei. Die angemeldeten Forderungen ...
```

FP: `Bezirksgericht BG` (organisation)

```
...
festgehalten und insbesondere das Abschöpfungsverfahren beim <<<Bezirksgericht BG>>> 
berücksichtigt. Zudem wurde berücksichtigt, dass der Beschwerdeführer ...
```

FP: `Bezirksgericht BG` (organisation)

**✅ Gold Entities:**
- `KommR Vera Schnetger` (person)
- `St.-Antonius-Straße 3, 3123 Doppel, Österreich` (address)
- `KommR Vera Schnetger` (person)
- `KommR Vera Schnetger` (person)
- `KommR Vera Schnetger` (person)
- `KommR Vera Schnetger` (person)
- `KommR Vera Schnetger` (person)

</details>

---

## `specific_org_unterrecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'UnterRecycling Services GMBH'.

**Content:**
```
\bUnterRecycling\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_talverwerk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'TalVerverwerkGarten GMBH'.

**Content:**
```
\bTalVerverwerkGarten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_dufel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Düfel Technik KG'.

**Content:**
```
\bDüfel\s+Technik\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_gozcu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gözcü Getränke'.

**Content:**
```
\bGözcü\s+Getränke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_chen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Chen Setzekorn'.

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

## `specific_org_lexkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lexkel Vertrieb KG'.

**Content:**
```
\bLexkel\s+Vertrieb\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_unibach`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Unibach-Getränke AG'.

**Content:**
```
\bUnibach-Getränke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_noruniwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Noruniwald-Technik'.

**Content:**
```
\bNoruniwald-Technik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_kraftnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kraftnex Technologien GMBH'.

**Content:**
```
\bKraftnex\s+Technologien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_waldver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Waldver E-Commerce Systeme GMBH'.

**Content:**
```
\bWaldver\s+E-Commerce\s+Systeme\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_pastl`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Pastl+Bächle Handel'.

**Content:**
```
\bPastl\+B\xe4chle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_hippach`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Hippach-Hart'.

**Content:**
```
\bRaiffeisenbank\s+Hippach-Hart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_genburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank genburg'.

**Content:**
```
\bRaiffeisenbank\s+genburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_karnische`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Karnische Rion Bankstelle St.Stefan'.

**Content:**
```
\bRaiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_trafenfen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Trafenfen Automotive'.

**Content:**
```
\bTrafenfen\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_gorius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gorius und Ziegann Event GMBH'.

**Content:**
```
\bGorius\s+und\s+Ziegann\s+Event\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_unter_donunisee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Unter Donunisee AG'.

**Content:**
```
\bUnter\s+Donunisee\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_ruterborries`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Rüterborries+Friderich Möbel'.

**Content:**
```
\bRüterborries\+Friderich\s+Möbel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_bankhaus_denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bankhaus Denzel'.

**Content:**
```
\bBankhaus\s+Denzel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Norconheim'.

**Content:**
```
\bNorconheim\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_bauermeister`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bauermeister Getränke'.

**Content:**
```
\bBauermeister\s+Getränke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_hoch_synwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hoch Synwil'.

**Content:**
```
\bHoch\s+Synwil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_sophie_wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sophie Wittmeir'.

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

## `specific_org_schoenfelder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schoenfelder Textil KG'.

**Content:**
```
\bSchoenfelder\s+Textil\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_lexdon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lexdon IT'.

**Content:**
```
\bLexdon\s+IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_alal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Alal-Medien'.

**Content:**
```
\bAlal-Medien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_wien_waldnor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wien Waldnor KG'.

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

## `specific_org_vossbein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Vossbein Lebensmittel'.

**Content:**
```
\bVossbein\s+Lebensmittel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_event_sudkraftlex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Event Sudkraftlex GMBH'.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_kqpc`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'KQPC Versand GMBH'.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_sudver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sudver Handel Services GMBH'.

**Content:**
```
\bSudver\s+Handel\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_glanznorost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Glanznorost Institut GMBH'.

**Content:**
```
\bGlanznorost\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_west_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'West-Luftfahrt'.

**Content:**
```
\bWest-Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_maegerlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mägerlein Logistik'.

**Content:**
```
\bM\xe4gerlein\s+Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_planung_monuniost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Planung Monuniost'.

**Content:**
```
\bPlanung\s+Monuniost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_gartgart`

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

## `specific_org_kraftver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kraftver-Gastronomie GMBH'.

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

## `specific_org_simek`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Simek Daten GMBH'.

**Content:**
```
\bSimek\s+Daten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_dersteintri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Dersteintri-Versicherung GMBH'.

**Content:**
```
\bDersteintri-Versicherung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_oina`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'OINA Solar Institut'.

**Content:**
```
\bOINA\s+Solar\s+Institut\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_gemke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gemke+Gamper Logistik'.

**Content:**
```
\bGemke\+Gamper\s+Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_kornfelder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kornfelder Recycling'.

**Content:**
```
\bKornfelder\s+Recycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_sanitar`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sanitär Talder GMBH'.

**Content:**
```
\bSanit\xe4r\s+Talder\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_kasse_hyphen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenkasse' followed by hyphenated locations like 'Retz-Pulkautal'.

**Content:**
```
\bRaiffeisenkasse\s+[A-Z][a-zA-Z]+(?:\s+-\s+[A-Z][a-zA-Z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_cervenka`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Cervenka&Neunübel Telekom AG'.

**Content:**
```
\bCervenka&Neun\xfc\xbbel\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_lubomir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lubomir Merschmeyer' as an organization (Gruppenträger).

**Content:**
```
\bLubomir\s+Merschmeyer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_textil_steingartlog`

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

## `specific_org_oberrecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'OberRecycling'.

**Content:**
```
\bOberRecycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_osttechnik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'OstTechnik'.

**Content:**
```
\bOstTechnik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_nord_kellex`

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

## `specific_org_maschinenbau_derwilsee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Maschinenbau Derwilsee'.

**Content:**
```
\bMaschinenbau\s+Derwilsee\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_innluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'InnLuftfahrt GMBH'.

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

## `specific_org_fensudlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fensudlog GMBH'.

**Content:**
```
\bFensudlog\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_inn_monost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Inn Monost'.

**Content:**
```
\bInn\s+Monost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_sud_sudwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Süd Sudwil'.

**Content:**
```
\bSüd\s+Sudwil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_kelgart_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kelgart-Druck'.

**Content:**
```
\bKelgart-Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_greiner_mai`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Greiner-Mai Event'.

**Content:**
```
\bGreiner-Mai\s+Event\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_technik_ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Technik Ostbachal'.

**Content:**
```
\bTechnik\s+Ostbachal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_traunlandwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'TraunLandwirtschaft'.

**Content:**
```
\bTraunLandwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_getraenke_nexdorfzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Getränke Nexdorfzor GMBH'.

**Content:**
```
\bGetränke\s+Nexdorfzor\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_zschieschank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Zschieschank&Heeß Transport GMBH'.

**Content:**
```
\bZschieschank&Heeß\s+Transport\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_mullbrandt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Müllbrandt u. Worthmeier Digital GMBH'.

**Content:**
```
\bMüllbrandt\s+u\.\s+Worthmeier\s+Digital\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_seenorder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SeeNorderE‑Commerce' with em-dash.

**Content:**
```
\bSeeNorderE\u2011Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_hudec_christian`

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

## `specific_org_nkah`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'NKAH Luftfahrt Vertrieb'.

**Content:**
```
\bNKAH\s+Luftfahrt\s+Vertrieb\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_olivier`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Olivier u. Bartha Recycling'.

**Content:**
```
\bOlivier\s+u\.\s+Bartha\s+Recycling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_hagdorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hagdorn Robotik'.

**Content:**
```
\bHagdorn\s+Robotik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_istvan`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Istvan Gerart'.

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

## `specific_org_paweltschik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Paweltschik Telekom GMBH'.

**Content:**
```
\bPaweltschik\s+Telekom\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_schneppensieper`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schneppensieper & Bültbrunne Touristik'.

**Content:**
```
\bSchneppensieper\s+&\s+B\xfc\x9ftbrunne\s+Touristik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_touristik_wildon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Touristik Wildon'.

**Content:**
```
\bTouristik\s+Wildon\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_bawag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BAWAG P.S.K. Wohnbaubank'.

**Content:**
```
\bBAWAG\s+P\.S\.K\.\s+Wohnbaubank\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_lognex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lognex-IT AG' specifically to avoid partial matches.

**Content:**
```
\bLognex-IT\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_kira_hackbardt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kira Hackbardt' as an organization (Gruppenträger).

**Content:**
```
\bKira\s+Hackbardt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_nordtraval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'NordTravalUmwelt AG'.

**Content:**
```
\bNordTravalUmwelt\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Rosilius Pflege AG'.

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

## `specific_org_hochlebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'HochLebensmittel Holding GMBH'.

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

## `specific_org_verdonlex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Verdonlex Automotive GMBH'.

**Content:**
```
\bVerdonlex\s+Automotive\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Yavasoglu Analyse AG'.

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

## `specific_org_bierwerth`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bierwerth' as an organization (Gruppenträger).

**Content:**
```
\bBierwerth\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_bludszat`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bludszat Maschinenbau GMBH'.

**Content:**
```
\bBludszat\s+Maschinenbau\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_office_fa_schwechat_gmunden`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Gmunden Vöcklabruck' (specific failure case).

**Content:**
```
\bFA\s+Gmunden\s+V\xf6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_logseemon_metall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Logseemon-Metall AG'.

**Content:**
```
\bLogseemon-Metall\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_mittelheizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'MittelHeizung Werke AG'.

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

## `specific_org_traun_digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Traun-Digital KG'.

**Content:**
```
\bTraun-Digital\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_vahrenkamp`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Vahrenkamp Luftfahrt'.

**Content:**
```
\bVahrenkamp\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_rion`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Rion Vöcklabruck'.

**Content:**
```
\bRaiffeisenbank\s+Rion\s+V\xf6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_dufel_technik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Düfel Technik KG'.

**Content:**
```
\bD\xfcfel\s+Technik\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_raiffeisen_hyphen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank' followed by hyphenated locations like 'Süd-Weststeiermark' or 'Rion Vöcklabruck'.

**Content:**
```
\bRaiffeisenbank\s+[A-Z][a-zA-Z]+(?:\s+-\s+[A-Z][a-zA-Z]+|\s+[A-Z][a-zA-Z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 51 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0**

**False Positives:**

```
... Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der <<<Raiffeisenbank Wels>>> Süd  mitgeteilt, dass der Beschwerdeführer (Bf) Abgaben einschließlich ...
```

FP: `Raiffeisenbank Wels` (organisation)

```
... Teilbetrages in Höhe von 
€ 10.000,00 wird die dem Bf gegen die <<<Raiffeisenbank Wels>>> Süd  wegen des Guthabens auf einem 
bezeichneten Girokonto ...
```

FP: `Raiffeisenbank Wels` (organisation)

```
...
bezeichneten Girokonto zustehende Forderung gepfändet. Der <<<Raiffeisenbank Wels>>> Süd  wurde, soweit die 
Forderung gepfändet ist, verboten, ...
```

FP: `Raiffeisenbank Wels` (organisation)

```
... Österreich vom 10. Juni 2021, Zl. 700000/05154/29/2012, wurde 
der <<<Raiffeisenbank Wels>>> Süd  mitgeteilt, dass der Bf Abgaben einschließlich Nebengebühren ...
```

FP: `Raiffeisenbank Wels` (organisation)

```
... Teilbetrages in Höhe von € 10.000,00 wurde die dem Bf 
gegen die <<<Raiffeisenbank Wels>>> Süd  wegen des Guthabens auf einem bezeichneten Girokonto zustehende ...
```

FP: `Raiffeisenbank Wels` (organisation)

**✅ Gold Entities:**
- `Mag. Dario Dyckhoff` (person)
- `Melanie Fjodorov` (person)
- `Daumegasse 17, 9330 Silberegg, Österreich` (address)
- `Raiffeisenbank Wels Süd` (organisation)
- `Raiffeisenbank Wels Süd` (organisation)
- `Raiffeisenbank Wels Süd` (organisation)
- `Raiffeisenbank Wels Süd` (organisation)
- `Raiffeisenbank Wels Süd` (organisation)
- `Raiffeisenbank Wels Süd` (organisation)

</details>

---

## `specific_org_fuchsl`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Füchsl Touristik GMBH'.

**Content:**
```
\bF\xfcchsl\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_wildorftra`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wildorftra KI GMBH'.

**Content:**
```
\bWildorftra\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_orgbruckmonwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bruckmonwil Digital GMBH'.

**Content:**
```
\bBruckmonwil\s+Digital\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SüdVersand' specifically to avoid partial matches.

**Content:**
```
\bS\xfc\xd6rt\s+Versand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_logal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Logal Gruppe' specifically.

**Content:**
```
\bLogal\s+Gruppe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_norddaten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'NordDaten' specifically.

**Content:**
```
\bNordDaten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_org_dlcg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DLCG Bildung' specifically.

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

</details>

---

