# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-15T07:47:29.934926

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-15/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training examples | 954 |
| Validation examples | 239 |
| Test examples | 96236 |
| Train annotations | 1165 |
| Validation annotations | 282 |
| Test annotations | 3536 |
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
| Accuracy (exact match) | 99.6% |
| True Positives | 209 |
| False Positives | 111 |
| Micro Precision | 65.3% |
| Micro Recall | 38.4% |
| Micro F1 | 48.4% |
| Macro F1 | 48.4% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `tax_authority_fa_salzburg` | 10.8% | 100.0% | 5.7% | 31 | 31 | 0 |
| `tax_authority_fa_vorarlberg` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `tax_authority_fa_amstetten` | 0.4% | 100.0% | 0.2% | 1 | 1 | 0 |
| `tax_authority_fa_tirol_ost` | 1.8% | 100.0% | 0.9% | 5 | 5 | 0 |
| `tax_authority_fa_linz` | 1.8% | 100.0% | 0.9% | 5 | 5 | 0 |
| `tax_authority_finanzamt_steiermark_mitte` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `tax_authority_fa_steiermark_mitte` | 1.5% | 100.0% | 0.7% | 4 | 4 | 0 |
| `tax_authority_fa_kirchdorf_perg_steyr` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `tax_authority_fa_deutschlandsberg_leibnitz_voitsberg` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `tax_authority_finanzamt_wien_8_16_17` | 1.8% | 100.0% | 0.9% | 5 | 5 | 0 |
| `tax_authority_fa_klagenfurt_st_veit_wolfsberg` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `tax_authority_fa_schwechat_gerasdorf` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `tax_authority_fa_freistadt_urbach` | 0.7% | 100.0% | 0.4% | 2 | 2 | 0 |
| `tax_authority_fa_extended_multiword` | 29.6% | 92.3% | 17.6% | 104 | 96 | 8 |
| `tax_authority_finanzamt_salzburg` | 11.7% | 87.2% | 6.2% | 39 | 34 | 5 |
| `tax_authority_fa_wien_8_16_17` | 1.1% | 60.0% | 0.6% | 5 | 3 | 2 |
| `tax_authority_finanzamt_extended` | 15.9% | 58.8% | 9.2% | 85 | 50 | 35 |
| `tax_authority_finanzamt_waldviertel` | 0.4% | 50.0% | 0.2% | 2 | 1 | 1 |
| `tax_authority_finanzamt_oststeiermark` | 0.4% | 50.0% | 0.2% | 2 | 1 | 1 |
| `tax_authority_finanzamt_salzburg_land` | 0.7% | 50.0% | 0.4% | 4 | 2 | 2 |
| `tax_authority_fa_salzburg_land` | 0.7% | 50.0% | 0.4% | 4 | 2 | 2 |
| `tax_authority_finanzamt_spittal_villach` | 0.4% | 50.0% | 0.2% | 2 | 1 | 1 |
| `tax_authority_finanzamtbruck_eisenstadt_oberwart` | 0.4% | 33.3% | 0.2% | 3 | 1 | 2 |
| `tax_authority_finanzamt_linz` | 1.1% | 30.0% | 0.6% | 10 | 3 | 7 |
| `tax_authority_finanzamt` | 4.7% | 29.8% | 2.6% | 47 | 14 | 33 |
| `tax_authority_finanzamt_graz_stadt` | 0.4% | 25.0% | 0.2% | 4 | 1 | 3 |
| `tax_authority_finanzamt_gmunden_vocklabruck` | 0.4% | 20.0% | 0.2% | 5 | 1 | 4 |
| `tax_authority_finanzamt_braunau_ried_schärding` | 0.4% | 7.1% | 0.2% | 14 | 1 | 13 |
| `bank_bawag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `court_bezirksgericht` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `specific_company_klusner` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_yxtg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_bierwerth` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mur` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_fensudlog` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `bank_raiffeisen_kasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_houdek` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dorfkraft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sudkraftlex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_kqpc` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_logkeltal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_innluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hudec` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_gartgart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_kraftver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_donau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_norkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_roelfsen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_unterrecycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_textil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_landeck` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `specific_company_hulsebusch` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_wien_waldnor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_bergplanung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_pastl_bachle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_gozcu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sudver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_glanznorost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_schmeltz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mittel_unisyn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_vahrenkamp` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_conwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hochlebensmittel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sanitar_talder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mittel_logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sud_lemkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rosilius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_geisselbrecht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_gmunden` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_innsbruck` | 0.0% | 0.0% | 0.0% | 14 | 0 | 14 |
| `tax_authority_finanzamt_landeck_reutte` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `tax_authority_finanzamt_niederoesterreich_mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_nord_kellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_dorfcon_verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_starker_beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_lexdon_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_alal_medien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_zimmerhackel_bau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_ober_lemostnor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_vennes_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_getranke_nexdorfzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_rheinmetall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_bludszat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_schiwick` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_verdonlex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_touristik_wildon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_innmarine` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_seyberth_kaben` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_waldver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_spittal_villach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_hoch_synwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_kornfelder_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_nordevent_gruppe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_maegerlein_logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_traun_aluni_institut` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_talverwerk_garten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_heimwald_forschung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_keldonbach_sicherheit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `bank_sparkasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_stefansky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_traunchemie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_ogem` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `bank_raiffeisen_stallhofen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_istvan_gerart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_depp_versand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_talpflege` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_chen_setzekorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_liu_rempis` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_logal_gruppe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_vianden_robotik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_willeckes_cloud` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_pergler_beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sudevent_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rhein_normonkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `bank_raiffeisen_hippach_hart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hinklein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dersyn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_scheibenzuber` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dongartcon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_zschieschank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mullbrandt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rpxf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_ostwilnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_niederoesterreichische_vorsorgekasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `bank_raiffeisen_mittleres_mostviertel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_butkus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_liefeith` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rheinbildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_waldtra` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dufel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_kelgart_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mittelheizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_trafenfen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_ostgart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_nord_willemtri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_traunlandwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_zfgq_pharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hempel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sudlandwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_bankhaus_denzel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_schoenfelder_textil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_bcol_event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_freimut_ohlroge` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_lognex_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_traun_digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_fwv_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_biletzki_emmert` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_amstetten_melk_scheibbs` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `specific_company_sudversand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_christofl_ki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_planung_monuniost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_valbruckzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_west_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_ruterborries` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dlcg_bildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sudgarten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_norddaten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_derwilsee` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_ostbachal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_kraftnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_nowothnig` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_cervenka` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_wacr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_gaebelt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_fatima_finkenbein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_nexdorf_metall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_stadt_logglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dammke_ki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mertznich_bau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_oststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `bank_raiffeisen_bankstelle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_logseemon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_unter_donunisee` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_baden_mödling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_gemke_gamper` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_enns_software` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_finanzen_tradonnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_berwaldkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_inn_monost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sud_nortri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_tritri_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dias_telekom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rheindigital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_landwirtschaft_zorfurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_slenzak_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_lexkel_vertrieb` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_blazickova_hepprich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_berend` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_unibach_getranke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_seenorderecommerce` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_marzell_versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_ober_chemie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_amundi` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_buhrfeindt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_unter_gartglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_nord_trinex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_wildorftra` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_henken` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_kreschmer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_nordtraval` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_traunluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_schneppensieper` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_monlogtri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_werkval` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `court_landesgericht` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `specific_company_nexkelkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_wenker` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_noruniwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_nkah` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hagdorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_paweltschik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_vossbein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mur_donwerk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_fuchsl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_olivier_bartha` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mittel_glanzval` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rheinverwerk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_grutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_oberrecycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_schickli_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_greiner_mai_event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_energie_synlexder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_oina_solar_institut` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sievens_automotive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_nord_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_ostgetränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `tax_authority_fa_salzburg`

**F1:** 0.108 | **Precision:** 1.000 | **Recall:** 0.057  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Salzburg-Stadt.

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

**Example 0** (doc_id: ``)

```
... über die Beschwerde vom 13. Juli 2023 gegen den Bescheid des 
<<<FA Salzburg-Stadt>>>  vom 19. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 1** (doc_id: ``)

```
Entscheidungsgründe 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 ...
```

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

**Example 2** (doc_id: ``)

```
Das Online Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, ...
```

```
... Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 3** (doc_id: ``)

```
<<<FA Salzburg-Stadt>>>  ist für das Betreiben der Website, das Einrichten und die ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 4** (doc_id: ``)

```
Als Folge 
davon wird <<<FA Salzburg-Stadt>>>  als Vermittlerin und KommR Ing. Roberta Gossling  als Buchmacherin ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

</details>

---

## `tax_authority_fa_extended_multiword`

**F1:** 0.296 | **Precision:** 0.923 | **Recall:** 0.176  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by multi-word locations including Braunau Ried Schärding

**Content:**
```
\bFA\s+(?:Braunau\s+Ried\s+Sch\u00e4rding|Judenburg\s+Liezen|Kirchdorf\s+Perg\s+Steyr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Spittal\s+Villach|Amstetten\s+Melk\s+Scheibbs|Gmunden\s+V\u00f6cklabruck|Wien\s+1/23|Wien\s+2/20/21/22|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Nieder\u00f6sterreich\s+Mitte|Schwechat\s+Gerasdorf|Tirol\s+Ost|Innsbruck|Steiermark\s+Mitte|Salzburg-Land|Vorarlberg|Landeck\s+Reutte|Graz-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Salzburg-Stadt|Waldviertel|Grieskirchen\s+Wels|Purkersdorf|Klosterneuburg|\u00d6sterreich\s+DS)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.923 | 0.176 | 0.296 | 104 | 96 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 96 | 8 | 447 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Lading, Österreich, vom 30. Juni 2021 gegen den Bescheid des 
<<<FA Wien 1/23>>>  vom 22. Juni 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: ``)

```
... ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle 
des <<<FA Klosterneuburg>>> ) vom 13. Dezember 2019 betreffend Einkommensteuer 2011 zu ...
```

| Predicted | Gold |
|---|---|
| `FA Klosterneuburg` | `FA Klosterneuburg` |

**Example 2** (doc_id: ``)

```
Im Wirtschaftsjahr 2007 ist gemäß der beim <<<FA Grieskirchen Wels>>>  eingereichten 
Körperschaftsteuererklärung 2007 ein steuerlicher ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 3** (doc_id: ``)

```
Mit Vorlagebericht vom 13.11.2013 hat das <<<FA Grieskirchen Wels>>> 
die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 4** (doc_id: ``)

```
... Linz, vom 27.01.2016, GZ 
RV/5101064/2013, wurde seitens des <<<FA Grieskirchen Wels>>>  in vollem Umfang im Zuge einer Amtsrevision 
angefochten.
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

</details>

---

## `tax_authority_finanzamt_salzburg`

**F1:** 0.117 | **Precision:** 0.872 | **Recall:** 0.062  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt' followed by Salzburg-Stadt.

**Content:**
```
\bFinanzamt\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.872 | 0.062 | 0.117 | 39 | 34 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 34 | 5 | 337 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
<<<Finanzamt Salzburg-Stadt>>>  betreibt Geschäfte in den Bereichen 
Unterhaltungsmedien und ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 1** (doc_id: ``)

```
<<<Finanzamt Salzburg-Stadt>>>  hält eine Wettlizenz des Vereinigten Königreichs.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 2** (doc_id: ``)

```
KommR Ing. Roberta Gossling  Limited ist eine im Jahr 2007 von <<<Finanzamt Salzburg-Stadt>>>  Ltd. gegründete Gesellschaft.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 3** (doc_id: ``)

```
<<<Finanzamt Salzburg-Stadt>>> .com 
erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 4** (doc_id: ``)

```
... Wette auf den Ausgang der Lotterien erteilt der Teilnehmer <<<Finanzamt Salzburg-Stadt>>>  den 
Auftrag, die entsprechende Wette an KommR Ing. Roberta ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Im Zuge einer Nachschau durch das <<<Finanzamt Salzburg-Stadt>>>, sowie in einer Niederschrift 
aufgenommen am 20.03.2013 wurde ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
...
Bisheriger Verfahrensverlauf: 
Mit Schreiben vom 29.10.2019 hat das <<<Finanzamt Salzburg-Stadt>>> die beschuldigte Partei (bP) 
gem § 83 Abs 2 FinStrG davon ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... insbesondere von Zeugeneinvernahmen am 
18.8.2020, hat das <<<Finanzamt Salzburg-Stadt>>> als Finanzstrafbehörde am 25.9.2020 eine 
Stellungnahme gem ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

```
...
Stellungnahme gem § 124 Abs 2 FinStrG an den Spruchsenat I beim <<<Finanzamt Salzburg-Stadt>>> 
übermittelt.
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
In dieser Stellungnahme teilte das <<<Finanzamt Salzburg-Stadt>>> als Finanzstrafbehörde mit, dass 
nach dessen Ansicht gegen ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**
- `DDr.in Kerstin Tittrich, BA` (person)

</details>

---

## `tax_authority_finanzamt_extended`

**F1:** 0.159 | **Precision:** 0.588 | **Recall:** 0.092  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities starting with 'Finanzamt' followed by specific known locations including Vorarlberg, Freistadt Rohrbach Urfahr, Deutschlandsberg Leibnitz Voitsberg, Tirol Ost, Grieskirchen Wels, Schwechat Gerasdorf, Klagenfurt St. Veit Wolfsberg.

**Content:**
```
\bFinanzamt\s+(?:St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Purkersdorf|Lilienfeld\s+St\.\s+P\u00f6lten|Judenburg\s+Liezen|Neunkirchen\s+Wr\.\s+Neustadt|Klosterneuburg|Wien\s+1/23|Wien\s+2/20/21/22|Kirchdorf\s+Perg\s+Steyr|Baden\s+M\u00f6dling|\u00d6sterreich\s+DS|Vorarlberg|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Grieskirchen\s+Wels|Schwechat\s+Gerasdorf|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.588 | 0.092 | 0.159 | 85 | 50 | 35 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 50 | 35 | 492 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
...
gegen den zur Steuernummer 28-115/0315  ergangenen Bescheid des <<<Finanzamt Deutschlandsberg Leibnitz Voitsberg>>> (FA) vom 
11. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Deutschlandsberg Leibnitz Voitsberg` | `Finanzamt Deutschlandsberg Leibnitz Voitsberg` |

**Example 1** (doc_id: ``)

```
über die Beschwerden vom 29. März 2019 gegen den Bescheid des <<<Finanzamt Grieskirchen Wels>>>  vom 29. Jänner 
2019 betreffend Wiederaufnahme § 303 BAO / ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 2** (doc_id: ``)

```
Am 26.04.2013 erließ das <<<Finanzamt Grieskirchen Wels>>>  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 3** (doc_id: ``)

```
...
RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des <<<Finanzamt Grieskirchen Wels>>>  gegenüber der 
mitbeteiligten Partei Annemie Bott (als partiellen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 4** (doc_id: ``)

```
Unmittelbar nachfolgend hat das BFG die Amtsrevision des <<<Finanzamt Grieskirchen Wels>>> (samt Veranlagungsakten 
sowie Auszügen aus dem Arbeitsbogen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

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

**Example 1** (doc_id: ``)

**False Positives:**

```
Mit Beschwerdevorentscheidungen vom 17. Februar 2020 wies das <<<Finanzamt Lilienfeld 
St. Pölten>>> die Beschwerden gegen die Einkommensteuerbescheide für 2017 ...
```

FP: `Finanzamt Lilienfeld 
St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Demnach sei die Sendung am 12.11.2019 an das <<<Finanzamt Lilienfeld St. Pölten>>> zugestellt und 
von einem Mitarbeiter übernommen worden.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Mit Vorlagebericht vom 5. Mai 2020 legte das <<<Finanzamt Lilienfeld St. Pölten>>> die Beschwerde 
dem Bundesfinanzgericht zur Entscheidung vor.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
für die Jahre 2001 bis 2003 wurde vom <<<Finanzamt Neunkirchen Wr. 
Neustadt>>> zu Eingangsrechnungen der geprüften Gesellschaften festgestellt, ...
```

FP: `Finanzamt Neunkirchen Wr. 
Neustadt` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt`

**F1:** 0.047 | **Precision:** 0.298 | **Recall:** 0.026  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities starting with 'Finanzamt' followed by specific known locations or multi-word locations including abbreviations like 'St.'

**Content:**
```
\bFinanzamt\s+(?:St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Purkersdorf|Lilienfeld\s+St\.\s+Pölten|Judenburg\s+Liezen|Neunkirchen\s+Wr\.\s+Neustadt|Klosterneuburg|Wien\s+1/23|Wien\s+2/20/21/22|Kirchdorf\s+Perg\s+Steyr|Baden\s+Mödling|Österreich\s+DS)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.298 | 0.026 | 0.047 | 47 | 14 | 33 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 33 | 367 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Erkenntnis BFG 6.5.2019, RV/7101631/2016, 
verwiesen, welches vom <<<Finanzamt Wien 2/20/21/22>>>  hinsichtlich des zweiten Beschwerdepunktes 
„III.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Example 1** (doc_id: ``)

```
... Beschwerde vom 5. Dezember 2022 gegen den 
Abweisungsbescheid des <<<Finanzamt Judenburg Liezen>>>  vom 25. November 2022 betreffend Aufhebung des 
Einkommensteuerbescheides ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 2** (doc_id: ``)

```
... Wiedergut, Steuerberaterin in 9500 Villach, 
gegen die Bescheide des <<<Finanzamt Baden Mödling>>>  vom 23.1.2014 (Gesamtrechtsnachfolger Finanzamt für 
Großbetriebe) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

**Example 3** (doc_id: ``)

```
... Beschwerde vom 27. September 2018 gegen den Haftungsbescheid 
des <<<Finanzamt Purkersdorf>>>  vom 11. Juli 2018 zu Recht erkannt:  
I. Der Beschwerde wird ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Purkersdorf` | `Finanzamt Purkersdorf` |

**Example 4** (doc_id: ``)

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

**Example 0** (doc_id: ``)

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

**Example 1** (doc_id: ``)

**False Positives:**

```
Mit Beschwerdevorentscheidungen vom 17. Februar 2020 wies das <<<Finanzamt Lilienfeld 
St. Pölten>>> die Beschwerden gegen die Einkommensteuerbescheide für 2017 ...
```

FP: `Finanzamt Lilienfeld 
St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Demnach sei die Sendung am 12.11.2019 an das <<<Finanzamt Lilienfeld St. Pölten>>> zugestellt und 
von einem Mitarbeiter übernommen worden.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Mit Vorlagebericht vom 5. Mai 2020 legte das <<<Finanzamt Lilienfeld St. Pölten>>> die Beschwerde 
dem Bundesfinanzgericht zur Entscheidung vor.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
für die Jahre 2001 bis 2003 wurde vom <<<Finanzamt Neunkirchen Wr. 
Neustadt>>> zu Eingangsrechnungen der geprüften Gesellschaften festgestellt, ...
```

FP: `Finanzamt Neunkirchen Wr. 
Neustadt` (organisation)

**✅ Gold Entities:**

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `tax_authority_finanzamt_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt' followed by Innsbruck.

**Content:**
```
\bFinanzamt\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 14 | 198 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... 2007 erfolgte nach Durchführung einer 
Außenprüfung durch das <<<Finanzamt Innsbruck>>>.
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... das Formular Beih 38 über Auftrag des Antragstellers 
an das <<<Finanzamt Innsbruck>>> übermittelt.
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Beweis: Arbeitgeberbescheinigung 
Das <<<Finanzamt Innsbruck>>> hat den Antrag des Antragstellers vollständig zurückgewiesen ...
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
... behaupteter Verletzung 
der Entscheidungspflicht durch das <<<Finanzamt Innsbruck>>> betreffend Arbeitnehmerveranlagung 
2022 beschlossen: 
I. Die ...
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Ludwig Elwardt` (person)
- `Frieda Aumund` (person)
- `Kirchbergerberg 79, 4676 Rakesing, Österreich` (address)

**Example 4** (doc_id: ``)

**False Positives:**

```
... 2020 gegen das Erkenntnis des Spruchsenates beim 
damaligen <<<Finanzamt Innsbruck>>> als Finanzstrafbehörde vom 18. Juni 2020, Geschäftszahlen 
...
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**
- `Esra Rashid` (person)
- `Pannaschgasse 2O, 8643 Kindberg, Österreich` (address)
- `Isabel Clements` (person)
- `Isabel Clements` (person)
- `Mona Tommeschat` (person)

</details>

---

## `tax_authority_finanzamt_braunau_ried_schärding`

**F1:** 0.004 | **Precision:** 0.071 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Finanzamt Braunau Ried Schärding.

**Content:**
```
\bFinanzamt\s+Braunau\s+Ried\s+Schärding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.071 | 0.002 | 0.004 | 14 | 1 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 13 | 83 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... über die 
Beschwerde vom 15. Juni 2020 gegen den Bescheid des <<<Finanzamt Braunau Ried Schärding>>>  vom 20. Mai 2020 
betreffend Feststellung von Einkünften gemäß ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Braunau Ried Schärding` | `Finanzamt Braunau Ried Schärding` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Mit Beschwerdevorentscheidung vom 12. März 2014 wies das <<<Finanzamt Braunau Ried 
Schärding>>> die Beschwerde als unbegründet ab.
```

FP: `Finanzamt Braunau Ried 
Schärding` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
Mit Vorlagebericht vom 16. Mai 2014 legte das <<<Finanzamt Braunau Ried Schärding>>> die 
Beschwerde dem Bundesfinanzgericht zur Entscheidung vor ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... vom 23.11.2015 
1) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
10.11.2015, über die Festsetzung der Kraftfahrzeugsteuer ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

```
... Monate 07-12/2014, 
2) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
10.11.2015, über die Festsetzung der Kraftfahrzeugsteuer ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

```
... vom 14.11.2016 
3) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
15.09.2016 über die Festsetzung der Normverbrauchsabgabe ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

```
... Normverbrauchsabgabe 04/2014, 
4) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
15.09.2016 über die Festsetzung der Kraftfahrzeugsteuer ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**
- `RgR Alessia Nikoleizik` (person)
- `Lassingrotte 6, 3970 Spital, Österreich` (address)

**Example 3** (doc_id: ``)

**False Positives:**

```
Am 9. April 2009 erließ das <<<Finanzamt Braunau Ried Schärding>>> einen Bescheid über die 
Feststellung von Einkünften aus Vermietung ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
Am 9. November 2009 erließ das <<<Finanzamt Braunau Ried Schärding>>> einen Bescheid über die 
Feststellung von Einkünften aus Vermietung ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_linz`

**F1:** 0.011 | **Precision:** 0.300 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches Finanzamt Linz

**Content:**
```
\bFinanzamt\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.300 | 0.006 | 0.011 | 10 | 3 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 7 | 309 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... betreffend die Beschwerde vom 26. Mai 2023 gegen den Bescheid des 
<<<Finanzamt Linz>>>  vom 27. April 2023 über die Abweisung einer Nachsicht von ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Example 1** (doc_id: ``)

```
... Österreich, über die Beschwerde vom 6.Mai 2022 gegen den Bescheid des <<<Finanzamt Linz>>>  vom 
12. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Example 2** (doc_id: ``)

```
... Beschwerde vom 27. Jänner 2020 gegen 
den die Bescheide des <<<Finanzamt Linz>>>  vom 7. Oktober 2019 betreffend Anspruchszinsen (§ 205 
BAO) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
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

**Example 1** (doc_id: ``)

**False Positives:**

```
... BAO für 
2018 (Wirtschaftsjahr 01.02.2017 - 31.01.2018) beim <<<Finanzamt Linz>>> elektronisch eingereicht.
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Der Sachverhalt wird durch das <<<Finanzamt Linz>>> wie folgt als erwiesen angenommen (der als 
erwiesen angenommene ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Für das <<<Finanzamt Linz>>> ist es als erwiesen anzunehmen, dass die Gewinnverteilung des ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
Es ist daher für das <<<Finanzamt Linz>>> als erwiesen anzunehmen, dass nach der Anteilsabtretung 
von ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `bank_bawag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches BAWAG P.S.K. Wohnbaubank specifically.

**Content:**
```
\bBAWAG\s+P\.S\.K\.\s+Wohnbaubank
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_klusner`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Klusner&Päffgen Bildung GMBH.

**Content:**
```
\bKlusner&Päffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_yxtg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name YXTG Maschinenbau.

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

## `specific_company_bierwerth`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Bierwerth.

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

## `specific_company_mur`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Mur Ververzor Betriebe.

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

</details>

---

<details>
<summary>📋 All Rules</summary>

## `tax_authority_fa_extended_multiword`

**F1:** 0.296 | **Precision:** 0.923 | **Recall:** 0.176  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by multi-word locations including Braunau Ried Schärding

**Content:**
```
\bFA\s+(?:Braunau\s+Ried\s+Sch\u00e4rding|Judenburg\s+Liezen|Kirchdorf\s+Perg\s+Steyr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Spittal\s+Villach|Amstetten\s+Melk\s+Scheibbs|Gmunden\s+V\u00f6cklabruck|Wien\s+1/23|Wien\s+2/20/21/22|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Nieder\u00f6sterreich\s+Mitte|Schwechat\s+Gerasdorf|Tirol\s+Ost|Innsbruck|Steiermark\s+Mitte|Salzburg-Land|Vorarlberg|Landeck\s+Reutte|Graz-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Salzburg-Stadt|Waldviertel|Grieskirchen\s+Wels|Purkersdorf|Klosterneuburg|\u00d6sterreich\s+DS)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.923 | 0.176 | 0.296 | 104 | 96 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 96 | 8 | 447 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Lading, Österreich, vom 30. Juni 2021 gegen den Bescheid des 
<<<FA Wien 1/23>>>  vom 22. Juni 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: ``)

```
... ergangenen Bescheid des Finanzamtes X (jetzt Dienststelle 
des <<<FA Klosterneuburg>>> ) vom 13. Dezember 2019 betreffend Einkommensteuer 2011 zu ...
```

| Predicted | Gold |
|---|---|
| `FA Klosterneuburg` | `FA Klosterneuburg` |

**Example 2** (doc_id: ``)

```
Im Wirtschaftsjahr 2007 ist gemäß der beim <<<FA Grieskirchen Wels>>>  eingereichten 
Körperschaftsteuererklärung 2007 ein steuerlicher ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 3** (doc_id: ``)

```
Mit Vorlagebericht vom 13.11.2013 hat das <<<FA Grieskirchen Wels>>> 
die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) ...
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

**Example 4** (doc_id: ``)

```
... Linz, vom 27.01.2016, GZ 
RV/5101064/2013, wurde seitens des <<<FA Grieskirchen Wels>>>  in vollem Umfang im Zuge einer Amtsrevision 
angefochten.
```

| Predicted | Gold |
|---|---|
| `FA Grieskirchen Wels` | `FA Grieskirchen Wels` |

</details>

---

## `tax_authority_finanzamt_extended`

**F1:** 0.159 | **Precision:** 0.588 | **Recall:** 0.092  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities starting with 'Finanzamt' followed by specific known locations including Vorarlberg, Freistadt Rohrbach Urfahr, Deutschlandsberg Leibnitz Voitsberg, Tirol Ost, Grieskirchen Wels, Schwechat Gerasdorf, Klagenfurt St. Veit Wolfsberg.

**Content:**
```
\bFinanzamt\s+(?:St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Purkersdorf|Lilienfeld\s+St\.\s+P\u00f6lten|Judenburg\s+Liezen|Neunkirchen\s+Wr\.\s+Neustadt|Klosterneuburg|Wien\s+1/23|Wien\s+2/20/21/22|Kirchdorf\s+Perg\s+Steyr|Baden\s+M\u00f6dling|\u00d6sterreich\s+DS|Vorarlberg|Freistadt\s+Rohrbach\s+Urfahr|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Grieskirchen\s+Wels|Schwechat\s+Gerasdorf|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.588 | 0.092 | 0.159 | 85 | 50 | 35 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 50 | 35 | 492 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
...
gegen den zur Steuernummer 28-115/0315  ergangenen Bescheid des <<<Finanzamt Deutschlandsberg Leibnitz Voitsberg>>> (FA) vom 
11. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Deutschlandsberg Leibnitz Voitsberg` | `Finanzamt Deutschlandsberg Leibnitz Voitsberg` |

**Example 1** (doc_id: ``)

```
über die Beschwerden vom 29. März 2019 gegen den Bescheid des <<<Finanzamt Grieskirchen Wels>>>  vom 29. Jänner 
2019 betreffend Wiederaufnahme § 303 BAO / ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 2** (doc_id: ``)

```
Am 26.04.2013 erließ das <<<Finanzamt Grieskirchen Wels>>>  nach Durchführung der Außenprüfung je einen 
Körperschaftsteuerbescheid ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 3** (doc_id: ``)

```
...
RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des <<<Finanzamt Grieskirchen Wels>>>  gegenüber der 
mitbeteiligten Partei Annemie Bott (als partiellen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

**Example 4** (doc_id: ``)

```
Unmittelbar nachfolgend hat das BFG die Amtsrevision des <<<Finanzamt Grieskirchen Wels>>> (samt Veranlagungsakten 
sowie Auszügen aus dem Arbeitsbogen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Grieskirchen Wels` | `Finanzamt Grieskirchen Wels` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

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

**Example 1** (doc_id: ``)

**False Positives:**

```
Mit Beschwerdevorentscheidungen vom 17. Februar 2020 wies das <<<Finanzamt Lilienfeld 
St. Pölten>>> die Beschwerden gegen die Einkommensteuerbescheide für 2017 ...
```

FP: `Finanzamt Lilienfeld 
St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Demnach sei die Sendung am 12.11.2019 an das <<<Finanzamt Lilienfeld St. Pölten>>> zugestellt und 
von einem Mitarbeiter übernommen worden.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Mit Vorlagebericht vom 5. Mai 2020 legte das <<<Finanzamt Lilienfeld St. Pölten>>> die Beschwerde 
dem Bundesfinanzgericht zur Entscheidung vor.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
für die Jahre 2001 bis 2003 wurde vom <<<Finanzamt Neunkirchen Wr. 
Neustadt>>> zu Eingangsrechnungen der geprüften Gesellschaften festgestellt, ...
```

FP: `Finanzamt Neunkirchen Wr. 
Neustadt` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_salzburg`

**F1:** 0.117 | **Precision:** 0.872 | **Recall:** 0.062  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt' followed by Salzburg-Stadt.

**Content:**
```
\bFinanzamt\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.872 | 0.062 | 0.117 | 39 | 34 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 34 | 5 | 337 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
<<<Finanzamt Salzburg-Stadt>>>  betreibt Geschäfte in den Bereichen 
Unterhaltungsmedien und ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 1** (doc_id: ``)

```
<<<Finanzamt Salzburg-Stadt>>>  hält eine Wettlizenz des Vereinigten Königreichs.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 2** (doc_id: ``)

```
KommR Ing. Roberta Gossling  Limited ist eine im Jahr 2007 von <<<Finanzamt Salzburg-Stadt>>>  Ltd. gegründete Gesellschaft.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 3** (doc_id: ``)

```
<<<Finanzamt Salzburg-Stadt>>> .com 
erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

**Example 4** (doc_id: ``)

```
... Wette auf den Ausgang der Lotterien erteilt der Teilnehmer <<<Finanzamt Salzburg-Stadt>>>  den 
Auftrag, die entsprechende Wette an KommR Ing. Roberta ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Stadt` | `Finanzamt Salzburg-Stadt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Im Zuge einer Nachschau durch das <<<Finanzamt Salzburg-Stadt>>>, sowie in einer Niederschrift 
aufgenommen am 20.03.2013 wurde ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
...
Bisheriger Verfahrensverlauf: 
Mit Schreiben vom 29.10.2019 hat das <<<Finanzamt Salzburg-Stadt>>> die beschuldigte Partei (bP) 
gem § 83 Abs 2 FinStrG davon ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... insbesondere von Zeugeneinvernahmen am 
18.8.2020, hat das <<<Finanzamt Salzburg-Stadt>>> als Finanzstrafbehörde am 25.9.2020 eine 
Stellungnahme gem ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

```
...
Stellungnahme gem § 124 Abs 2 FinStrG an den Spruchsenat I beim <<<Finanzamt Salzburg-Stadt>>> 
übermittelt.
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
In dieser Stellungnahme teilte das <<<Finanzamt Salzburg-Stadt>>> als Finanzstrafbehörde mit, dass 
nach dessen Ansicht gegen ...
```

FP: `Finanzamt Salzburg-Stadt` (organisation)

**✅ Gold Entities:**
- `DDr.in Kerstin Tittrich, BA` (person)

</details>

---

## `tax_authority_fa_salzburg`

**F1:** 0.108 | **Precision:** 1.000 | **Recall:** 0.057  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Salzburg-Stadt.

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

**Example 0** (doc_id: ``)

```
... über die Beschwerde vom 13. Juli 2023 gegen den Bescheid des 
<<<FA Salzburg-Stadt>>>  vom 19. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 1** (doc_id: ``)

```
Entscheidungsgründe 
I. Verfahrensgang 
<<<FA Salzburg-Stadt>>>  Ltd. (im Folgenden „<<<FA Salzburg-Stadt>>>“) ist eine im Jahr 1999 ...
```

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

**Example 2** (doc_id: ``)

```
Das Online Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, ...
```

```
... Wettprodukt von <<<FA Salzburg-Stadt>>>  ist unter der 
Website www.<<<FA Salzburg-Stadt>>> .com erreichbar, welche unter anderem auch in Österreich verfügbar ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 3** (doc_id: ``)

```
<<<FA Salzburg-Stadt>>>  ist für das Betreiben der Website, das Einrichten und die ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

**Example 4** (doc_id: ``)

```
Als Folge 
davon wird <<<FA Salzburg-Stadt>>>  als Vermittlerin und KommR Ing. Roberta Gossling  als Buchmacherin ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Stadt` | `FA Salzburg-Stadt` |

</details>

---

## `tax_authority_finanzamt`

**F1:** 0.047 | **Precision:** 0.298 | **Recall:** 0.026  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities starting with 'Finanzamt' followed by specific known locations or multi-word locations including abbreviations like 'St.'

**Content:**
```
\bFinanzamt\s+(?:St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Purkersdorf|Lilienfeld\s+St\.\s+Pölten|Judenburg\s+Liezen|Neunkirchen\s+Wr\.\s+Neustadt|Klosterneuburg|Wien\s+1/23|Wien\s+2/20/21/22|Kirchdorf\s+Perg\s+Steyr|Baden\s+Mödling|Österreich\s+DS)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.298 | 0.026 | 0.047 | 47 | 14 | 33 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 33 | 367 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Erkenntnis BFG 6.5.2019, RV/7101631/2016, 
verwiesen, welches vom <<<Finanzamt Wien 2/20/21/22>>>  hinsichtlich des zweiten Beschwerdepunktes 
„III.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 2/20/21/22` | `Finanzamt Wien 2/20/21/22` |

**Example 1** (doc_id: ``)

```
... Beschwerde vom 5. Dezember 2022 gegen den 
Abweisungsbescheid des <<<Finanzamt Judenburg Liezen>>>  vom 25. November 2022 betreffend Aufhebung des 
Einkommensteuerbescheides ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Judenburg Liezen` | `Finanzamt Judenburg Liezen` |

**Example 2** (doc_id: ``)

```
... Wiedergut, Steuerberaterin in 9500 Villach, 
gegen die Bescheide des <<<Finanzamt Baden Mödling>>>  vom 23.1.2014 (Gesamtrechtsnachfolger Finanzamt für 
Großbetriebe) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Baden Mödling` | `Finanzamt Baden Mödling` |

**Example 3** (doc_id: ``)

```
... Beschwerde vom 27. September 2018 gegen den Haftungsbescheid 
des <<<Finanzamt Purkersdorf>>>  vom 11. Juli 2018 zu Recht erkannt:  
I. Der Beschwerde wird ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Purkersdorf` | `Finanzamt Purkersdorf` |

**Example 4** (doc_id: ``)

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

**Example 0** (doc_id: ``)

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

**Example 1** (doc_id: ``)

**False Positives:**

```
Mit Beschwerdevorentscheidungen vom 17. Februar 2020 wies das <<<Finanzamt Lilienfeld 
St. Pölten>>> die Beschwerden gegen die Einkommensteuerbescheide für 2017 ...
```

FP: `Finanzamt Lilienfeld 
St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Demnach sei die Sendung am 12.11.2019 an das <<<Finanzamt Lilienfeld St. Pölten>>> zugestellt und 
von einem Mitarbeiter übernommen worden.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Mit Vorlagebericht vom 5. Mai 2020 legte das <<<Finanzamt Lilienfeld St. Pölten>>> die Beschwerde 
dem Bundesfinanzgericht zur Entscheidung vor.
```

FP: `Finanzamt Lilienfeld St. Pölten` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
für die Jahre 2001 bis 2003 wurde vom <<<Finanzamt Neunkirchen Wr. 
Neustadt>>> zu Eingangsrechnungen der geprüften Gesellschaften festgestellt, ...
```

FP: `Finanzamt Neunkirchen Wr. 
Neustadt` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_fa_tirol_ost`

**F1:** 0.018 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Tirol Ost.

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

**Example 0** (doc_id: ``)

```
... betreffend Beschwerde 
vom 06.07.2007 gegen die Bescheide des <<<FA Tirol Ost>>>  vom 13.09.2011 und 14.09.2011 
beschlossen: 
Der Vorlageantrag ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 1** (doc_id: ``)

```
... Parteien 
Isidor Ollerdißen (Beschwerdeführer), Stadt1, und <<<FA Tirol Ost>>>  als Amtspartei und als 
Gesamtrechtsnachfolger des Finanzamtes ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 2** (doc_id: ``)

```
... September 
2012 für Nachname 1 R und Nachname 1 A seien nun beim <<<FA Tirol Ost>>>  eingebracht worden.
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 3** (doc_id: ``)

```
...
16.Oktober 2015 ausgefertigten Bescheid der belangten Behörde <<<FA Tirol Ost>>>, nunmehr 
Finanzamt Tirol Ost, betreffend Einkommensteuer für ...
```

| Predicted | Gold |
|---|---|
| `FA Tirol Ost` | `FA Tirol Ost` |

**Example 4** (doc_id: ``)

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

## `tax_authority_fa_linz`

**F1:** 0.018 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches FA Linz

**Content:**
```
\bFA\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.018 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 144 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... betreffend die Beschwerde vom 26. Mai 2023 gegen 
den Bescheid des <<<FA Linz>>>  vom 27. April 2023 über die Abweisung einer Nachsicht von ...
```

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Example 1** (doc_id: ``)

```
... einer vorgelegten Rechnung vom 30.9.2010 geht hervor, dass die <<<FA Linz>>>  eine Prüfung 
Treppenaufzug zu einem Gesamtbetrag von 102,00 ...
```

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Example 2** (doc_id: ``)

```
... einer vorgelegten Rechnung vom 13.9.2012 geht hervor, dass die <<<FA Linz>>>  eine Prüfung 
des Treppenaufzugs zu einem Gesamtbetrag von ...
```

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Example 3** (doc_id: ``)

```
... Februar 2020, und 24. Februar 2020 gegen die Bescheide des 
<<<FA Linz>>> (nunmehr Finanzamt Österreich) zu Steuernummer 09-470/7083 ...
```

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

**Example 4** (doc_id: ``)

```
... die Beschwerde vom 13. August 2024 gegen den 
Bescheid des <<<FA Linz>>>  vom 8. August 2024 betreffend Aufhebung § 299 BAO / Sonstige ...
```

| Predicted | Gold |
|---|---|
| `FA Linz` | `FA Linz` |

</details>

---

## `tax_authority_finanzamt_wien_8_16_17`

**F1:** 0.018 | **Precision:** 1.000 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches Finanzamt Wien 8/16/17

**Content:**
```
\bFinanzamt\s+Wien\s+8/16/17\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.009 | 0.018 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 279 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
...
über die Beschwerde vom 8. August 2023 gegen den Bescheid des <<<Finanzamt Wien 8/16/17>>>  vom 27. Juli 2023 
zu Steuernummer 45-760/3996  betreffend ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Example 1** (doc_id: ``)

```
... Sulztal, Österreich, vom 5. Dezember 2022 gegen den Bescheid des 
<<<Finanzamt Wien 8/16/17>>>  vom 10. November 2022 betreffend Zahlungserleichterungen § ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Example 2** (doc_id: ``)

```
Die steuerliche Vertretung führte aus, dass 
mit Bescheid des <<<Finanzamt Wien 8/16/17>>>  vom 23.07.2021 dem Beschwerdeführer eine COVID-19-
1 von 9
...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Example 3** (doc_id: ``)

```
Dieser Antrag wurde an das <<<Finanzamt Wien 8/16/17>>>  weitergeleitet.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

**Example 4** (doc_id: ``)

```
... Soziales und Behindertenwesen 
(Sozialministeriumservice) dem <<<Finanzamt Wien 8/16/17>>>  durch eine Bescheinigung auf Grund eines ärztlichen 
Sachverständigengutachtens ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 8/16/17` | `Finanzamt Wien 8/16/17` |

</details>

---

## `tax_authority_fa_steiermark_mitte`

**F1:** 0.015 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches FA Steiermark Mitte

**Content:**
```
\bFA\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.015 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 132 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Abgabenbehörde eingelangt am 15. Juli 2019, gegen den Bescheid des <<<FA Steiermark Mitte>>> (jetzt 
Dienststelle des Finanzamtes Österreich) vom 6. Juni ...
```

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Example 1** (doc_id: ``)

```
... über die Beschwerden vom 17. Mai 2016 gegen die Bescheide des <<<FA Steiermark Mitte>>> 
vom 11. April 2016 betreffend ersten Säumniszuschlag 2016 ...
```

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Example 2** (doc_id: ``)

```
Nach telefonischer Rucksprache 
mit Frau FA beim <<<FA Steiermark Mitte>>>  hat Frau STB1 die bereits am 26.02.2014 mittels eingeschriebenen ...
```

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

**Example 3** (doc_id: ``)

```
... gegen den zur Steuernummer 45-988/6339  ergangenen Bescheid des <<<FA Steiermark Mitte>>>  vom 
10. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `FA Steiermark Mitte` | `FA Steiermark Mitte` |

</details>

---

## `tax_authority_fa_wien_8_16_17`

**F1:** 0.011 | **Precision:** 0.600 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authority 'FA Wien 8/16/17'.

**Content:**
```
\bFA\s+Wien\s+8/16/17\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.600 | 0.006 | 0.011 | 5 | 3 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 2 | 182 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Matschek 
Steuerberatungsgesellschaft mbH, 9020 Klagenfurt und <<<FA Wien 8/16/17>>>  als Amtspartei über die 
Beschwerde vom 11.5.2021      
  ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 8/16/17` | `FA Wien 8/16/17` |

**Example 1** (doc_id: ``)

```
... die Beschwerde vom 17. Jänner 2025 gegen die Bescheide des <<<FA Wien 8/16/17>>> 
jeweils vom 7. Jänner 2025 über die Abweisung des Antrages ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 8/16/17` | `FA Wien 8/16/17` |

**Example 2** (doc_id: ``)

```
...
Übermittlung des gesamten ärztlichen Sachverständigengutachtens an das <<<FA Wien 8/16/17>>>  hat nicht 
zu erfolgen.
```

| Predicted | Gold |
|---|---|
| `FA Wien 8/16/17` | `FA Wien 8/16/17` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... der Revisionswerberin vom 28.10.2003 gegen die Bescheide des <<<FA Wien 
8/16/17>>> vom 22.08.2003, betreffend Festsetzung Umsatzsteuer 10-11/2002, ...
```

FP: `FA Wien 
8/16/17` (organisation)

```
... Umsatzsteuer 7/2003, sowie gemäß § 253 BAO gegen die Bescheide des <<<FA Wien 
8/16/17>>> vom 05.10.2005 betreffend Umsatzsteuer 2002 und 2003 abgewiesen ...
```

FP: `FA Wien 
8/16/17` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_linz`

**F1:** 0.011 | **Precision:** 0.300 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches Finanzamt Linz

**Content:**
```
\bFinanzamt\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.300 | 0.006 | 0.011 | 10 | 3 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 7 | 309 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... betreffend die Beschwerde vom 26. Mai 2023 gegen den Bescheid des 
<<<Finanzamt Linz>>>  vom 27. April 2023 über die Abweisung einer Nachsicht von ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Example 1** (doc_id: ``)

```
... Österreich, über die Beschwerde vom 6.Mai 2022 gegen den Bescheid des <<<Finanzamt Linz>>>  vom 
12. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

**Example 2** (doc_id: ``)

```
... Beschwerde vom 27. Jänner 2020 gegen 
den die Bescheide des <<<Finanzamt Linz>>>  vom 7. Oktober 2019 betreffend Anspruchszinsen (§ 205 
BAO) ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Linz` | `Finanzamt Linz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
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

**Example 1** (doc_id: ``)

**False Positives:**

```
... BAO für 
2018 (Wirtschaftsjahr 01.02.2017 - 31.01.2018) beim <<<Finanzamt Linz>>> elektronisch eingereicht.
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Der Sachverhalt wird durch das <<<Finanzamt Linz>>> wie folgt als erwiesen angenommen (der als 
erwiesen angenommene ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Für das <<<Finanzamt Linz>>> ist es als erwiesen anzunehmen, dass die Gewinnverteilung des ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
Es ist daher für das <<<Finanzamt Linz>>> als erwiesen anzunehmen, dass nach der Anteilsabtretung 
von ...
```

FP: `Finanzamt Linz` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_fa_vorarlberg`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Vorarlberg.

**Content:**
```
\bFA\s+Vorarlberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 195 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... 3420 Kritzendorf, vom 15. Mai 2017 gegen die 
Bescheide des <<<FA Vorarlberg>>>  vom 14. Oktober 2016, 16. Oktober 2016, 22. Oktober 2016 sowie ...
```

| Predicted | Gold |
|---|---|
| `FA Vorarlberg` | `FA Vorarlberg` |

**Example 1** (doc_id: ``)

```
... die Beschwerde vom 28. Februar 2019 gegen die Bescheide 
des <<<FA Vorarlberg>>>  vom 30. Jänner 2019, 20-231/9124, betreffend Umsatz- und 
...
```

| Predicted | Gold |
|---|---|
| `FA Vorarlberg` | `FA Vorarlberg` |

</details>

---

## `tax_authority_finanzamt_steiermark_mitte`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches Finanzamt Steiermark Mitte.

**Content:**
```
\bFinanzamt\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 289 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... über die Beschwerde vom 30. März 2015 gegen den Bescheid des <<<Finanzamt Steiermark Mitte>>> 
vom 6. März 2015 betreffend Einkommensteuer 2013 zu Recht ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Steiermark Mitte` | `Finanzamt Steiermark Mitte` |

**Example 1** (doc_id: ``)

```
... gegen den zu Steuernummer 58-619/3976 
ergangenen Bescheid des <<<Finanzamt Steiermark Mitte>>>  vom 9. März 2023 betreffend Festsetzung Umsatzsteuer 1-
11/2022 ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Steiermark Mitte` | `Finanzamt Steiermark Mitte` |

</details>

---

## `tax_authority_fa_kirchdorf_perg_steyr`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches FA Kirchdorf Perg Steyr

**Content:**
```
\bFA\s+Kirchdorf\s+Perg\s+Steyr\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 304 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... die Beschwerde vom 13. September 2021 gegen den Bescheid des 
<<<FA Kirchdorf Perg Steyr>>>  vom 19. August 2021 betreffend Festsetzung von Gebühren und ...
```

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Example 1** (doc_id: ``)

```
... über die Beschwerde vom 17. März 2016 gegen den Bescheid des <<<FA Kirchdorf Perg Steyr>>> 
vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige ...
```

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

</details>

---

## `tax_authority_fa_deutschlandsberg_leibnitz_voitsberg`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches FA Deutschlandsberg Leibnitz Voitsberg

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

**Example 0** (doc_id: ``)

```
... die Beschwerde vom 7. Februar 2024 
gegen den Bescheid des <<<FA Deutschlandsberg Leibnitz Voitsberg>>>  vom 10. Jänner 2024 betreffend Abweisung eines Antrages 
auf ...
```

| Predicted | Gold |
|---|---|
| `FA Deutschlandsberg Leibnitz Voitsberg` | `FA Deutschlandsberg Leibnitz Voitsberg` |

**Example 1** (doc_id: ``)

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

## `tax_authority_fa_klagenfurt_st_veit_wolfsberg`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authority 'FA Klagenfurt St. Veit Wolfsberg'

**Content:**
```
\bFA\s+Klagenfurt\s+St\.\s+Veit\s+Wolfsberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 372 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... der Angelegenheit der Parteien 
Dagobert Hermkens (Bf) und <<<FA Klagenfurt St. Veit Wolfsberg>>>  als Amtspartei über die Beschwerde vom 7.2.2022     
     ...
```

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

**Example 1** (doc_id: ``)

```
... die Beschwerde vom 21. Februar 2022 gegen die Bescheide des <<<FA Klagenfurt St. Veit Wolfsberg>>>  vom 
5. November 2021, betreffend Umsatzsteuer 2018 - 2020 ...
```

| Predicted | Gold |
|---|---|
| `FA Klagenfurt St. Veit Wolfsberg` | `FA Klagenfurt St. Veit Wolfsberg` |

</details>

---

## `tax_authority_fa_schwechat_gerasdorf`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authority 'FA Schwechat Gerasdorf'

**Content:**
```
\bFA\s+Schwechat\s+Gerasdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 94 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... die Beschwerde vom 3. Oktober 2021 gegen die Bescheide 
des <<<FA Schwechat Gerasdorf>>>  jeweils vom 29. September 2021 betreffend Einkommensteuer ...
```

| Predicted | Gold |
|---|---|
| `FA Schwechat Gerasdorf` | `FA Schwechat Gerasdorf` |

**Example 1** (doc_id: ``)

```
... die Beschwerde vom 12. November 2019 gegen den Bescheid des 
<<<FA Schwechat Gerasdorf>>>  vom 9. Oktober 2019 betreffend die Festsetzung von ersten ...
```

| Predicted | Gold |
|---|---|
| `FA Schwechat Gerasdorf` | `FA Schwechat Gerasdorf` |

</details>

---

## `tax_authority_fa_freistadt_urbach`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Freistadt Rohrbach Urfahr.

**Content:**
```
\bFA\s+Freistadt\s+Rohrbach\s+Urfahr\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.007 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 378 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... die Beschwerde vom 21. Jänner 2009 gegen die Bescheide des 
<<<FA Freistadt Rohrbach Urfahr>>>  vom 27. November 2008 betreffend Umsatzsteuer 2006 und 2007 ...
```

| Predicted | Gold |
|---|---|
| `FA Freistadt Rohrbach Urfahr` | `FA Freistadt Rohrbach Urfahr` |

**Example 1** (doc_id: ``)

```
... die zur Steuernummer 93-042/2361  ergangenen Bescheide des 
<<<FA Freistadt Rohrbach Urfahr>>> (jetzt Dienststelle des Finanzamtes Österreich) vom 21.August ...
```

| Predicted | Gold |
|---|---|
| `FA Freistadt Rohrbach Urfahr` | `FA Freistadt Rohrbach Urfahr` |

</details>

---

## `tax_authority_finanzamt_salzburg_land`

**F1:** 0.007 | **Precision:** 0.500 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches Finanzamt Salzburg-Land

**Content:**
```
\bFinanzamt\s+Salzburg\-Land\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.004 | 0.007 | 4 | 2 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 2 | 542 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... die Beschwerde vom 29.7.2019 gegen den Bescheid des (nunmehr) <<<Finanzamt Salzburg-Land>>> 
vom 11. Juli 2019 betreffend Umsatzsteuer 2018 Steuernummer ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

**Example 1** (doc_id: ``)

```
... über die Beschwerde vom 31. Juli 2018 gegen den Bescheid des <<<Finanzamt Salzburg-Land>>>  vom 
28. Juni 2018 betreffend Haftungsinanspruchnahme gemäß ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Salzburg-Land` | `Finanzamt Salzburg-Land` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Entscheidungsgründe 
I. Verfahrensgang 
Das <<<Finanzamt Salzburg-Land>>> hat gegenüber Lubomir Näger, Bakk. phil. (nachstehend mit „Bf“ ...
```

FP: `Finanzamt Salzburg-Land` (organisation)

**✅ Gold Entities:**
- `Lubomir Näger, Bakk. phil.` (person)

**Example 1** (doc_id: ``)

**False Positives:**

```
... den Abweisungsbescheid 
des Finanzamtes Österreich (bisher <<<Finanzamt Salzburg-Land>>>) vom 24. Oktober 2019 
betreffend Zuerkennung der Familienbeihilfe ...
```

FP: `Finanzamt Salzburg-Land` (organisation)

**✅ Gold Entities:**
- `Ingrid Raemaekers` (person)
- `Am Lindenkreuz 6, 2620 Lindgrub, Österreich` (address)

</details>

---

## `tax_authority_fa_salzburg_land`

**F1:** 0.007 | **Precision:** 0.500 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authority 'FA Salzburg-Land'

**Content:**
```
\bFA\s+Salzburg\-Land\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.004 | 0.007 | 4 | 2 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 2 | 310 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... die Beschwerde vom 28. Februar 2017 gegen die Bescheide des 
<<<FA Salzburg-Land>>>  vom 25. Jänner 2017 betreffend Einkommensteuer 2014 und Einkommensteuer ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Land` | `FA Salzburg-Land` |

**Example 1** (doc_id: ``)

```
...
über die Beschwerde vom 20. Juli 2021 gegen den Bescheid des <<<FA Salzburg-Land>>>  vom 14. Juli 2021, 
Steuernummer 67-659/6836, betreffend Festsetzung ...
```

| Predicted | Gold |
|---|---|
| `FA Salzburg-Land` | `FA Salzburg-Land` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

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

**Example 1** (doc_id: ``)

**False Positives:**

```
In den gegenständlichen Beschwerdeverfahren, das vom <<<FA Salzburg-Land>>> dem BFG vorgelegt 
worden waren, ist somit ab 01.01.2021 das ...
```

FP: `FA Salzburg-Land` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_fa_amstetten`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Amstetten Melk Scheibbs.

**Content:**
```
\bFA\s+Amstetten\s+Melk\s+Scheibbs\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 62 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
...
betreffend Beschwerde vom 8. März 2019 gegen den Bescheid des <<<FA Amstetten Melk Scheibbs>>>  vom 9. Juli 2018, 
Steuernummer 04-171/2066, betreffend Vorsteuererstattung ...
```

| Predicted | Gold |
|---|---|
| `FA Amstetten Melk Scheibbs` | `FA Amstetten Melk Scheibbs` |

</details>

---

## `tax_authority_finanzamt_waldviertel`

**F1:** 0.004 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt' followed by Waldviertel.

**Content:**
```
\bFinanzamt\s+Waldviertel\b
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

**Example 0** (doc_id: ``)

```
... vertreten 
durch STB1, über die Beschwerde gegen den Bescheid des <<<Finanzamt Waldviertel>>>  vom 5. Februar 2019 
betreffend Zwangsstrafe nach § 16 WiEReG ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Waldviertel` | `Finanzamt Waldviertel` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
...
 Vorausgegangenes Verfahren: 
Am 4. Februar 2020 hatte das <<<Finanzamt Waldviertel>>> folgenden Bescheid an die Bf. erlassen:  
Abweisungsbescheid ...
```

FP: `Finanzamt Waldviertel` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_oststeiermark`

**F1:** 0.004 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Finanzamt Oststeiermark

**Content:**
```
\bFinanzamt\s+Oststeiermark\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.002 | 0.004 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 286 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... über die Beschwerde vom 1. August 2019 gegen den Bescheid des <<<Finanzamt Oststeiermark>>> 
vom 17. Juli 2019 betreffend Abweisung eines Antrages auf ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Oststeiermark` | `Finanzamt Oststeiermark` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Daher wurde die Prüfung vom <<<Finanzamt 
Oststeiermark>>> durchgeführt und nicht vom Finanzamt für den 9/18/19 Bezirk.
```

FP: `Finanzamt 
Oststeiermark` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_spittal_villach`

**F1:** 0.004 | **Precision:** 0.500 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt Spittal Villach'.

**Content:**
```
\bFinanzamt\s+Spittal\s+Villach\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.002 | 0.004 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 265 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Wirtschaftstreuhand Gesellschaft mbH, Straße2, Ort, 
gegen den Bescheid des <<<Finanzamt Spittal Villach>>> (nunmehr Finanzamt Österreich, § 323 b BAO) vom 29. 
November ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Spittal Villach` | `Finanzamt Spittal Villach` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... 2019 gegen 
den Bescheid des Finanzamtes Österreich (vormals <<<Finanzamt Spittal Villach>>>) vom 19. Juli 2019 
betreffend Feststellung der Einkünfte § ...
```

FP: `Finanzamt Spittal Villach` (organisation)

**✅ Gold Entities:**
- `HR Manfred Leymann` (person)
- `Thomas-Münzer-Gasse 19, 5133 Bitzlthal, Österreich` (address)
- `65-622/1704` (tax_number)

</details>

---

## `tax_authority_finanzamtbruck_eisenstadt_oberwart`

**F1:** 0.004 | **Precision:** 0.333 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Finanzamt Bruck Eisenstadt Oberwart

**Content:**
```
\bFinanzamt\s+Bruck\s+Eisenstadt\s+Oberwart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.002 | 0.004 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 374 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... die zur Steuernummer 58-793/8116  ergangenen Bescheide des <<<Finanzamt Bruck Eisenstadt Oberwart>>>  vom 
15. Juli 2015 betreffend Umsatzsteuerfestsetzung für ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Bruck Eisenstadt Oberwart` | `Finanzamt Bruck Eisenstadt Oberwart` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... seinem sachlich und örtlich zuständigen Finanzamt (in dem 
Fall <<<Finanzamt Bruck Eisenstadt Oberwart>>>) fristwahrend abgeben.
```

FP: `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
Das <<<Finanzamt Bruck Eisenstadt Oberwart>>> kann über Antrag eines abkommensberechtigten 
Arbeitskräfteüberlassungsunternehmens ...
```

FP: `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_graz_stadt`

**F1:** 0.004 | **Precision:** 0.250 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt' followed by Graz-Stadt.

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
| `organisation` | 1 | 3 | 542 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

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

**Example 0** (doc_id: ``)

**False Positives:**

```
... Einreichung der 
Umsatzsteuererklärung 2018 am 15.5.2019 beim <<<Finanzamt Graz-Stadt>>>, wurde die Frist für den 
Antrag auf Erstattung von Vorsteuern ...
```

FP: `Finanzamt Graz-Stadt` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... Anträge auf Erstattung von Vorsteuern zuständigen Behörde 
(<<<Finanzamt Graz-Stadt>>>) eingebracht.
```

FP: `Finanzamt Graz-Stadt` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... 
Erstattung mittels amtlich vorgeschriebenem Vordruck beim <<<Finanzamt Graz-Stadt>>> zu 
beantragen.
```

FP: `Finanzamt Graz-Stadt` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_gmunden_vocklabruck`

**F1:** 0.004 | **Precision:** 0.200 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Finanzamt Gmunden Vöcklabruck

**Content:**
```
\bFinanzamt\s+Gmunden\s+Vöcklabruck\b
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

**Example 0** (doc_id: ``)

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

**Example 0** (doc_id: ``)

**False Positives:**

```
... Gmunden“ gerichtete 
Vorlageantrag am 28. Dezember 2018 beim <<<Finanzamt Gmunden Vöcklabruck>>> einlangte, dieses 
Finanzamt jedoch sachlich und örtlich unzuständig ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... Marxergasse 4, 4810 Gmunden“ und wurde 
am selben Tag beim <<<Finanzamt Gmunden Vöcklabruck>>> in Gmunden persönlich durch Einwurf in 
die „ Postbox“ der ...
```

FP: `Finanzamt Gmunden Vöcklabruck` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... wurde der Vorlageantrag – zuständigkeitshalber - durch das <<<Finanzamt Gmunden 
Vöcklabruck>>> an das „Finanzamt für Gebühren und Verkehrsst.
```

FP: `Finanzamt Gmunden 
Vöcklabruck` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
... wird die Behörde im Adressfeld durch das weiterleitende Amt (<<<Finanzamt 
Gmunden Vöcklabruck>>>) selbst mit „Finanzamt für Gebühren u Verkehrsst“ bezeichnet.
```

FP: `Finanzamt 
Gmunden Vöcklabruck` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_braunau_ried_schärding`

**F1:** 0.004 | **Precision:** 0.071 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Finanzamt Braunau Ried Schärding.

**Content:**
```
\bFinanzamt\s+Braunau\s+Ried\s+Schärding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.071 | 0.002 | 0.004 | 14 | 1 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 13 | 83 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... über die 
Beschwerde vom 15. Juni 2020 gegen den Bescheid des <<<Finanzamt Braunau Ried Schärding>>>  vom 20. Mai 2020 
betreffend Feststellung von Einkünften gemäß ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Braunau Ried Schärding` | `Finanzamt Braunau Ried Schärding` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Mit Beschwerdevorentscheidung vom 12. März 2014 wies das <<<Finanzamt Braunau Ried 
Schärding>>> die Beschwerde als unbegründet ab.
```

FP: `Finanzamt Braunau Ried 
Schärding` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
Mit Vorlagebericht vom 16. Mai 2014 legte das <<<Finanzamt Braunau Ried Schärding>>> die 
Beschwerde dem Bundesfinanzgericht zur Entscheidung vor ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... vom 23.11.2015 
1) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
10.11.2015, über die Festsetzung der Kraftfahrzeugsteuer ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

```
... Monate 07-12/2014, 
2) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
10.11.2015, über die Festsetzung der Kraftfahrzeugsteuer ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

```
... vom 14.11.2016 
3) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
15.09.2016 über die Festsetzung der Normverbrauchsabgabe ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

```
... Normverbrauchsabgabe 04/2014, 
4) gegen den Bescheid der belangten Behörde <<<Finanzamt Braunau Ried Schärding>>> vom 
15.09.2016 über die Festsetzung der Kraftfahrzeugsteuer ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**
- `RgR Alessia Nikoleizik` (person)
- `Lassingrotte 6, 3970 Spital, Österreich` (address)

**Example 3** (doc_id: ``)

**False Positives:**

```
Am 9. April 2009 erließ das <<<Finanzamt Braunau Ried Schärding>>> einen Bescheid über die 
Feststellung von Einkünften aus Vermietung ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
Am 9. November 2009 erließ das <<<Finanzamt Braunau Ried Schärding>>> einen Bescheid über die 
Feststellung von Einkünften aus Vermietung ...
```

FP: `Finanzamt Braunau Ried Schärding` (organisation)

**✅ Gold Entities:**

</details>

---

## `bank_bawag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches BAWAG P.S.K. Wohnbaubank specifically.

**Content:**
```
\bBAWAG\s+P\.S\.K\.\s+Wohnbaubank
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `court_bezirksgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Bezirksgericht followed by location.

**Content:**
```
\bBezirksgericht\s+[A-Z][a-zäöüß]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Mit weiterem 
Beschluss vom 04.03.2005 ordnete das <<<Bezirksgericht Gericht>>> die Schätzung dieser 
Liegenschaft durch den allgemein beeideten ...
```

FP: `Bezirksgericht Gericht` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
Das Versteigerungsverfahren vor dem <<<Bezirksgericht Gericht>>> wurde infolge des vorgenannten 
Vertrages mit Beschluss vom ...
```

FP: `Bezirksgericht Gericht` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_company_klusner`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Klusner&Päffgen Bildung GMBH.

**Content:**
```
\bKlusner&Päffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_yxtg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name YXTG Maschinenbau.

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

## `specific_company_bierwerth`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Bierwerth.

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

## `specific_company_mur`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Mur Ververzor Betriebe.

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

## `specific_company_fensudlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Fensudlog GMBH.

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

## `bank_raiffeisen_kasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenkasse entities including specific regions.

**Content:**
```
\bRaiffeisenkasse\s+[A-Z][a-zA-Z\-\u00e4\u00f6\u00fc\u00df]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_houdek`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Houdek Maschinenbau.

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

## `specific_company_dorfkraft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Dorfkraft-Sanitär AG.

**Content:**
```
\bDorfkraft-Sanit\u00e4r\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_sudkraftlex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Event Sudkraftlex GMBH.

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

## `specific_company_kqpc`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name KQPC Versand GMBH.

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

## `specific_company_logkeltal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Logkeltal Marine.

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

## `specific_company_innluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name InnLuftfahrt GMBH.

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

## `specific_company_hudec`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Hudec&Christian Immobilien GMBH.

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

## `specific_company_gartgart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Gartgart Dienstleistungen GMBH.

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

## `specific_company_kraftver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Kraftver-Gastronomie GMBH.

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

## `specific_company_donau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Donau Furtkraftwald AG.

**Content:**
```
\bDonau\s+Furtkraftwald\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_norkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Norkel-Software GMBH.

**Content:**
```
\bNorkel-Software\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_roelfsen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Roelfsen Versicherung.

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

## `specific_company_unterrecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name UnterRecycling Services GMBH.

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

## `specific_company_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Textil Steingartlog.

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

## `tax_authority_fa_landeck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Landeck Reutte.

**Content:**
```
\bFA\s+Landeck\s+Reutte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 44 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... 2020/15/0085-10 über die 
Beschwerden gegen die Bescheide des <<<FA Landeck Reutte>>> vom 24. November 2008 betreffend 
Umsatzsteuer 2007, vom 21. ...
```

FP: `FA Landeck Reutte` (organisation)

**✅ Gold Entities:**
- `Lee Guthe` (person)
- `Olympiastraße 16, 3800 Scheideldorf, Österreich` (address)

</details>

---

## `specific_company_hulsebusch`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Hülsebusch + Breithaupt Versicherung.

**Content:**
```
\bH\u00fclsebusch\s+\+\s+Breithaupt\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_wien_waldnor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Wien Waldnor KG (excluding suffix if already present in specific rule, but here we match the full name).

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

## `specific_company_bergplanung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name BergPlanung, including when followed by GmbH & CoKG.

**Content:**
```
\bBergPlanung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Pastl+Bächle Handel.

**Content:**
```
\bPastl\+B\u00e4chle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_gozcu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Gözcü Getränke.

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

## `specific_company_sudver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Sudver Handel Services GMBH.

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

## `specific_company_glanznorost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Glanznorost Institut GMBH.

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

## `specific_company_schmeltz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Schmeltz Luftfahrt.

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

## `specific_company_mittel_unisyn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Mittel Unisyn GMBH.

**Content:**
```
\bMittel\s+Unisyn\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_vahrenkamp`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Vahrenkamp Luftfahrt.

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

## `specific_company_conwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Conwil-Marine.

**Content:**
```
\bConwil-Marine\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hochlebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name HochLebensmittel Holding GMBH.

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

## `specific_company_sanitar_talder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Sanitär Talder GMBH.

**Content:**
```
\bSanitär\s+Talder\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_mittel_logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Mittel-Logistik.

**Content:**
```
\bMittel-Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_sud_lemkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Süd Lemkel.

**Content:**
```
\bSüd\s+Lemkel\b
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
Matches the specific company name Rosilius Pflege AG.

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
Matches the specific company name Yavasoglu Analyse AG.

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

## `specific_company_geisselbrecht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Geißelbrecht Garten.

**Content:**
```
\bGeißelbrecht\s+Garten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_gmunden`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Gmunden Vöcklabruck.

**Content:**
```
\bFA\s+Gmunden\s+Vöcklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_finanzamt_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt' followed by Innsbruck.

**Content:**
```
\bFinanzamt\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 14 | 198 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... 2007 erfolgte nach Durchführung einer 
Außenprüfung durch das <<<Finanzamt Innsbruck>>>.
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... das Formular Beih 38 über Auftrag des Antragstellers 
an das <<<Finanzamt Innsbruck>>> übermittelt.
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Beweis: Arbeitgeberbescheinigung 
Das <<<Finanzamt Innsbruck>>> hat den Antrag des Antragstellers vollständig zurückgewiesen ...
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
... behaupteter Verletzung 
der Entscheidungspflicht durch das <<<Finanzamt Innsbruck>>> betreffend Arbeitnehmerveranlagung 
2022 beschlossen: 
I. Die ...
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**
- `Priv.-Doz. Ludwig Elwardt` (person)
- `Frieda Aumund` (person)
- `Kirchbergerberg 79, 4676 Rakesing, Österreich` (address)

**Example 4** (doc_id: ``)

**False Positives:**

```
... 2020 gegen das Erkenntnis des Spruchsenates beim 
damaligen <<<Finanzamt Innsbruck>>> als Finanzstrafbehörde vom 18. Juni 2020, Geschäftszahlen 
...
```

FP: `Finanzamt Innsbruck` (organisation)

**✅ Gold Entities:**
- `Esra Rashid` (person)
- `Pannaschgasse 2O, 8643 Kindberg, Österreich` (address)
- `Isabel Clements` (person)
- `Isabel Clements` (person)
- `Mona Tommeschat` (person)

</details>

---

## `tax_authority_finanzamt_landeck_reutte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities 'Finanzamt' followed by Landeck Reutte.

**Content:**
```
\bFinanzamt\s+Landeck\s+Reutte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 3 | 51 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Nach Abschluss 
der Außenprüfung wurden vom <<<Finanzamt Landeck Reutte>>> am 26.4.2018 Haftungsbescheide 
(Einkommensteuer gemäß § 99 ...
```

FP: `Finanzamt Landeck Reutte` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... gemäß § 99 
EStG 1988) nach Durchführung einer GPLA-Prüfung vom <<<Finanzamt Landeck Reutte>>> erlassen 
und gegen diese Bescheide Beschwerden erhoben.
```

FP: `Finanzamt Landeck Reutte` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... bedeutet zwar, dass ein Organ des Finanzamtes Innsbruck für das 
<<<Finanzamt Landeck Reutte>>> tätig werden darf, jedoch nicht, dass das Finanzamt Innsbruck ...
```

FP: `Finanzamt Landeck Reutte` (organisation)

**✅ Gold Entities:**

</details>

---

## `tax_authority_finanzamt_niederoesterreich_mitte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt Niederösterreich Mitte

**Content:**
```
\bFinanzamt\s+Niederösterreich\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_nord_kellex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Nord Kellex

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

## `generic_company_dorfcon_verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Dorfcon-Verlag

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

## `generic_company_starker_beratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Starker Beratung

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

## `generic_company_lexdon_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Lexdon IT

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

## `generic_company_alal_medien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Alal-Medien

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

## `generic_company_zimmerhackel_bau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Zimmerhackel Bau

**Content:**
```
\bZimmerhackel\s+Bau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_ober_lemostnor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Ober Lemostnor AG

**Content:**
```
\bOber\s+Lemostnor\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_vennes_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Vennes Recycling AG

**Content:**
```
\bVennes\s+Recycling\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_getranke_nexdorfzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Getränke Nexdorfzor GMBH

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

## `generic_company_rheinmetall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches RheinMetall Technologien GMBH

**Content:**
```
\bRheinMetall\s+Technologien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_bludszat`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Bludszat Maschinenbau GMBH

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

## `generic_company_schiwick`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Schiwick Finanzen AG

**Content:**
```
\bSchiwick\s+Finanzen\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_verdonlex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Verdonlex Automotive GMBH

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

## `specific_company_touristik_wildon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Touristik Wildon.

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

## `specific_company_innmarine`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name InnMarine GMBH.

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

## `specific_company_seyberth_kaben`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Seyberth + Kaben Getränke AG.

**Content:**
```
\bSeyberth\s+\+\s+Kaben\s+Getränke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_waldver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Waldver E‑Commerce Systeme GMBH.

**Content:**
```
\bWaldver\s+E‑Commerce\s+Systeme\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_spittal_villach`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches FA Spittal Villach

**Content:**
```
\bFA\s+Spittal\s+Villach\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_hoch_synwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Hoch Synwil

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

## `generic_company_kornfelder_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Kornfelder Recycling

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

## `generic_company_nordevent_gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches NordEvent Gruppe

**Content:**
```
\bNordEvent\s+Gruppe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_maegerlein_logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Mägerlein Logistik

**Content:**
```
\bMägerlein\s+Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_traun_aluni_institut`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Traun Aluni Institut GMBH

**Content:**
```
\bTraun\s+Aluni\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_talverwerk_garten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches TalVerverwerkGarten GMBH

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

## `generic_company_heimwald_forschung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Heimwald-Forschung GMBH

**Content:**
```
\bHeimwald\-Forschung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_keldonbach_sicherheit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Keldonbach Sicherheit GMBH

**Content:**
```
\bKeldonbach\s+Sicherheit\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `bank_sparkasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Sparkasse entities including specific locations.

**Content:**
```
\bSparkasse\s+[A-Z][a-zA-Z\-\u00e4\u00f6\u00fc\u00df]+
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
Matches the specific company name Stefansky Bau GMBH.

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

## `specific_company_traunchemie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name TraunChemie GMBH.

**Content:**
```
\bTraunChemie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_ogem`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name OGEM Landwirtschaft GMBH.

**Content:**
```
\bOGEM\s+Landwirtschaft\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `bank_raiffeisen_stallhofen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenbank Stallhofen.

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

## `specific_company_istvan_gerart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Istvan Gerart.

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

## `specific_company_depp_versand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Depp Versand.

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

## `specific_company_talpflege`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name TalPflege.

**Content:**
```
\bTalPflege\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_chen_setzekorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Chen Setzekorn.

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

## `specific_company_liu_rempis`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Liu Rempis.

**Content:**
```
\bLiu\s+Rempis\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_logal_gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Logal Gruppe.

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

## `specific_company_vianden_robotik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Vianden Robotik GMBH.

**Content:**
```
\bVianden\s+Robotik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_willeckes_cloud`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Willeckes Cloud GMBH.

**Content:**
```
\bWilleckes\s+Cloud\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_pergler_beratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Pergler Beratung GMBH.

**Content:**
```
\bPergler\s+Beratung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_sudevent_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name SüdEvent AG.

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

## `specific_company_rhein_normonkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Rhein Normonkel Manufaktur GMBH.

**Content:**
```
\bRhein\s+Normonkel\s+Manufaktur\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `bank_raiffeisen_hippach_hart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenbank Hippach-Hart.

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

## `specific_company_hinklein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Hinklein.

**Content:**
```
\bHinklein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authority 'FA Innsbruck'

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

## `specific_company_dersyn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Dersyn Immobilien GMBH

**Content:**
```
\bDersyn\s+Immobilien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_scheibenzuber`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Scheibenzuber Textil

**Content:**
```
\bScheibenzuber\s+Textil\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_dongartcon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Dongartcon-Landwirtschaft GMBH

**Content:**
```
\bDongartcon-Landwirtschaft\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_zschieschank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Zschieschank&Heeß Transport GMBH

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

## `specific_company_mullbrandt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Müllbrandt u. Worthmeier Digital GMBH

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

## `specific_company_rpxf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name RPXF Immobilien

**Content:**
```
\bRPXF\s+Immobilien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_ostwilnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name OstWilnexLogistik AG

**Content:**
```
\bOstWilnexLogistik\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_niederoesterreichische_vorsorgekasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Niederösterreichische Vorsorgekasse

**Content:**
```
\bNiederösterreichische\s+Vorsorgekasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `bank_raiffeisen_mittleres_mostviertel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific bank name Raiffeisenbank Mittleres Mostviertel

**Content:**
```
\bRaiffeisenbank\s+Mittleres\s+Mostviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_butkus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Butkus Metall

**Content:**
```
\bButkus\s+Metall\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_liefeith`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Liefeith Immobilien.

**Content:**
```
\bLiefeith\s+Immobilien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_rheinbildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name RheinBildung.

**Content:**
```
\bRheinBildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_waldtra`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Waldtra-Sicherheit.

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

## `specific_company_dufel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Düfel Technik KG.

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

## `specific_company_kelgart_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Kelgart-Druck.

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

## `specific_company_mittelheizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name MittelHeizung Werke AG.

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

## `specific_company_trafenfen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Trafenfen Automotive.

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

## `specific_company_ostgart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Ostgart AG.

**Content:**
```
\bOstgart\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_nord_willemtri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Nord Willemtri KG.

**Content:**
```
\bNord\s+Willemtri\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_traunlandwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name TraunLandwirtschaft.

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

## `specific_company_zfgq_pharma`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name ZFGQ Pharma GMBH.

**Content:**
```
\bZFGQ\s+Pharma\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hempel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Hempel Heizung GMBH.

**Content:**
```
\bHempel\s+Heizung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_sudlandwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Süd-Landwirtschaft.

**Content:**
```
\bSüd-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_bankhaus_denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Bankhaus Denzel.

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

## `specific_company_schoenfelder_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Schoenfelder Textil KG.

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

## `specific_company_bcol_event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches BCOL Event AG

**Content:**
```
\bBCOL\s+Event\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_freimut_ohlroge`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Freimut+Ohlroge Analyse AG

**Content:**
```
\bFreimut\+Ohlroge\s+Analyse\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_lognex_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Lognex-IT AG

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

## `specific_company_traun_digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Traun-Digital KG

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

## `specific_company_fwv_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches FWV Luftfahrt GMBH

**Content:**
```
\bFWV\s+Luftfahrt\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_biletzki_emmert`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Biletzki&Emmert Medien GMBH

**Content:**
```
\bBiletzki&Emmert\s+Medien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_finanzamt_amstetten_melk_scheibbs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt Amstetten Melk Scheibbs.

**Content:**
```
\bFinanzamt\s+Amstetten\s+Melk\s+Scheibbs\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 4 | 78 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Mit Bescheid vom 18. April 2018 setzt das <<<Finanzamt Amstetten Melk Scheibbs>>> die 
Einkommensteuer für das Jahr 2017 unter Berücksichtigung ...
```

FP: `Finanzamt Amstetten Melk Scheibbs` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... Aufwendungen für Fachliteratur in 
Höhe von EUR 256,12 wurden vom <<<Finanzamt Amstetten Melk Scheibbs>>> hingegen nicht 
anerkannt.
```

FP: `Finanzamt Amstetten Melk Scheibbs` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Das <<<Finanzamt Amstetten Melk Scheibbs>>> gab diesem Antrag vom 26. April 2018 auf Aufhebung 
des Einkommensteuerbescheids ...
```

FP: `Finanzamt Amstetten Melk Scheibbs` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Im Rahmen dieser Festsetzung 
berücksichtigte das <<<Finanzamt Amstetten Melk Scheibbs>>> die geltend gemachten Aus-, 
Fortbildungs-, Umschulungskosten ...
```

FP: `Finanzamt Amstetten Melk Scheibbs` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name SüdVersand.

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

## `specific_company_norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Norconheim.

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

## `specific_company_christofl_ki`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Christöfl KI.

**Content:**
```
\bChrist\u00f6fl\s+KI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_planung_monuniost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Planung Monuniost.

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

## `specific_company_valbruckzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Valbruckzor-Energie.

**Content:**
```
\bValbruckzor-Energie\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_west_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name West-Luftfahrt.

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

## `specific_company_ruterborries`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Rüterborries+Friderich Möbel.

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

## `specific_company_dlcg_bildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name DLCG Bildung.

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

## `specific_company_sudgarten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name SüdGarten GMBH.

**Content:**
```
\bSüdGarten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_norddaten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name NordDaten.

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

## `specific_company_derwilsee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Maschinenbau Derwilsee.

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

## `specific_company_ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Technik Ostbachal.

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

## `specific_company_kraftnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Kraftnex Technologien GMBH.

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

## `specific_company_nowothnig`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Nowothnig Wind.

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

## `specific_company_cervenka`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Cervenka&Neunübel Telekom AG.

**Content:**
```
\bCervenka&Neunübel\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_wacr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name WACR Möbel Planung AG.

**Content:**
```
\bWACR\s+Möbel\s+Planung\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_gaebelt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Gäbelt.

**Content:**
```
\bGäbelt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_fatima_finkenbein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Fatima Finkenbein.

**Content:**
```
\bFatima\s+Finkenbein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_nexdorf_metall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Nexdorf-Metall.

**Content:**
```
\bNexdorf-Metall\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_stadt_logglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Stadt Logglanz.

**Content:**
```
\bStadt\s+Logglanz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_dammke_ki`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Dammke KI GMBH.

**Content:**
```
\bDammke\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_mertznich_bau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Mertznich Bau GMBH.

**Content:**
```
\bMertznich\s+Bau\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_oststeiermark`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by Oststeiermark.

**Content:**
```
\bFA\s+Oststeiermark\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `bank_raiffeisen_bankstelle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenbank entities including 'Bankstelle' suffixes to capture full name.

**Content:**
```
\bRaiffeisenbank\s+(?:Karnische\s+Rion\s+Bankstelle\s+St\.Stefan|genburg|S\u00fcd-Weststeiermark|Wienerwald|Stallhofen|Hippach-Hart|Mittleres\s+Mostviertel)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_logseemon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Logseemon-Metall AG.

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

## `specific_company_unter_donunisee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Unter Donunisee AG.

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

## `tax_authority_fa_baden_mödling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authority 'FA Baden Mödling'.

**Content:**
```
\bFA\s+Baden\s+Mödling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_gemke_gamper`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Gemke+Gamper Logistik.

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

## `specific_company_enns_software`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Enns-Software.

**Content:**
```
\bEnns-Software\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_finanzen_tradonnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Finanzen Tradonnex.

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

## `specific_company_berwaldkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Berwaldkel-Möbel AG.

**Content:**
```
\bBerwaldkel-Möbel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_inn_monost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Inn Monost.

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

## `specific_company_sud_nortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Süd Nortri.

**Content:**
```
\bSüd\s+Nortri\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_tritri_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Tritri-IT.

**Content:**
```
\bTritri-IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_dias_telekom`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name DIAS Telekom Institut.

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

## `specific_company_rheindigital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name RheinDigital.

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

## `specific_company_landwirtschaft_zorfurt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Landwirtschaft Zorfurt GMBH.

**Content:**
```
\bLandwirtschaft\s+Zorfurt\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_slenzak_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Slenzak IT GMBH.

**Content:**
```
\bSlenzak\s+IT\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_lexkel_vertrieb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Lexkel Vertrieb KG.

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

## `specific_company_blazickova_hepprich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Blazickova & Hepprich Energie AG.

**Content:**
```
\bBlazickova\s+&\s+Hepprich\s+Energie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_berend`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Berend Energie AG.

**Content:**
```
\bBerend\s+Energie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_unibach_getranke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Unibach-Getränke AG.

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

## `specific_company_seenorderecommerce`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name SeeNorderE‑Commerce.

**Content:**
```
\bSeeNorderE‑Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_marzell_versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Marzell Versicherung GMBH.

**Content:**
```
\bMarzell\s+Versicherung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_ober_chemie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Ober-Chemie GMBH.

**Content:**
```
\bOber-Chemie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_amundi`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Amundi Austria GmbH.

**Content:**
```
\bAmundi\s+Austria\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_buhrfeindt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Buhrfeindt Lebensmittel GMBH.

**Content:**
```
\bBuhrfeindt\s+Lebensmittel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_unter_gartglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Unter Gartglanz GMBH.

**Content:**
```
\bUnter\s+Gartglanz\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_nord_trinex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Nord Trinex GMBH.

**Content:**
```
\bNord\s+Trinex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_wildorftra`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Wildorftra KI GMBH.

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

## `specific_company_henken`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Henken.

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

## `specific_company_kreschmer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Kreschmer Recycling GMBH.

**Content:**
```
\bKreschmer\s+Recycling\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_nordtraval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name NordTravalUmwelt AG.

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

## `specific_company_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name TraunLuftfahrt Solutions.

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

## `specific_company_schneppensieper`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Schneppensieper & Bülbrunne Touristik.

**Content:**
```
\bSchneppensieper\s+&\s+Bülbrunne\s+Touristik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_monlogtri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Monlogtri-Analyse GMBH.

**Content:**
```
\bMonlogtri-Analyse\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_werkval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Werkval-Medien GMBH.

**Content:**
```
\bWerkval-Medien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `court_landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Landesgericht followed by location.

**Content:**
```
\bLandesgericht\s+[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 4 | 373 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
andererseits wurde beim <<<Landesgericht Ort>>> der 
dort gegen die Bf. geführte Akt zu abcd (wegen §§ 146, ...
```

FP: `Landesgericht Ort` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... den Jahren 2005 bis 2008) im Finanzstrafverfahren vor dem 
<<<Landesgericht Ort>>>1 (siehe Urteil v. 1.12.2010, Zl12; oben Pkt. I.8.) ist ua. ...
```

FP: `Landesgericht Ort` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
... aber auch die Gründung der BC GmbH, FN 99999, eingetragen im <<<Landesgericht 
Leoben>>>, zu sehen.
```

FP: `Landesgericht 
Leoben` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Im Strafverfahren vor dem <<<Landesgericht Stadt>>>-A hat XY selbst ausgesagt, dass er glaubte 
selbst über 12.000 ...
```

FP: `Landesgericht Stadt` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_company_nexkelkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Nexkelkel AG.

**Content:**
```
\bNexkelkel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_wenker`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Wenker Bau GMBH.

**Content:**
```
\bWenker\s+Bau\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_noruniwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Noruniwald-Technik.

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

## `specific_company_nkah`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name NKAH Luftfahrt Vertrieb.

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

## `specific_company_hagdorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Hagdorn Robotik.

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

## `specific_company_paweltschik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Paweltschik Telekom GMBH.

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

## `specific_company_vossbein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Vossbein Lebensmittel.

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

## `specific_company_mur_donwerk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Mur Donwerk GMBH.

**Content:**
```
\bMur\s+Donwerk\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_fuchsl`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Füchsl Touristik GMBH.

**Content:**
```
\bFüchsl\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_olivier_bartha`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Olivier u. Bartha Recycling.

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

## `specific_company_mittel_glanzval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Mittel Glanzval Consulting AG.

**Content:**
```
\bMittel\s+Glanzval\s+Consulting\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_rheinverwerk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name RheinVerwerkderElektro AG.

**Content:**
```
\bRheinVerwerkderElektro\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_grutz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Grütz Druck AG.

**Content:**
```
\bGrütz\s+Druck\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_oberrecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name OberRecycling.

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

## `specific_company_schickli_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Schickli Luftfahrt.

**Content:**
```
\bSchickli\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_greiner_mai_event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Greiner-Mai Event.

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

## `specific_company_energie_synlexder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Energie Synlexder.

**Content:**
```
\bEnergie\s+Synlexder\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_oina_solar_institut`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name OINA Solar Institut.

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

## `specific_company_sievens_automotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Sievens Automotive GMBH.

**Content:**
```
\bSievens\s+Automotive\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_nord_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Nord-Druck GMBH.

**Content:**
```
\bNord-Druck\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_ostgetränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name OstGetränke GMBH.

**Content:**
```
\bOstGetränke\s+GMBH\b
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

