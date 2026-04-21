# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-21T16:59:00.492193

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-21_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 385 |
| Validation documents | 97 |
| Test documents | 108 |
| Train sentences | 2327 |
| Validation sentences | 218 |
| Test sentences | 12077 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 50 |
| Refinement iterations | 5 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | False |
| Enable Prune | False |
| Critic Interval | 0 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 30 |
| Refine per batch | 1 |
| Manually annotated examples | 1304 |
| First batch with manual data | 34 |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 90.4% |
| True Positives | 1379 |
| False Positives | 1123 |
| Micro Precision | 55.1% |
| Micro Recall | 79.1% |
| Micro F1 | 65.0% |
| Macro F1 | 65.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `specific_fa_st_johann` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `specific_fa_braunau` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_fa_braunau_ried_schärding` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_finanzamt_landeck_reutte` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_kqpc_versand` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `specific_event_sudkraftlex` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `specific_sudver_handel` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_glanznorost` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_finanzamt_waldviertel` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_roelfsen_versicherung` | 3.6% | 100.0% | 1.8% | 32 | 32 | 0 |
| `specific_lubomir_merschmeyer` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `specific_schmeltz_luftfahrt` | 1.3% | 100.0% | 0.6% | 11 | 11 | 0 |
| `specific_houdek_maschinenbau` | 6.2% | 100.0% | 3.2% | 56 | 56 | 0 |
| `specific_lexdon_it` | 0.8% | 100.0% | 0.4% | 7 | 7 | 0 |
| `specific_dorfcon_verlag` | 1.0% | 100.0% | 0.5% | 9 | 9 | 0 |
| `specific_fa_wien_1_23` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `specific_tritri_it` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_gozcu_getranke` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `specific_finanzamt_wien_1_23` | 2.2% | 100.0% | 1.1% | 19 | 19 | 0 |
| `specific_mag_ghesla` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_finanzamt_wien_klosterneuburg` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `specific_mur_alver_og` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_ams_osterreich` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_landespolizeidirketion_tirol` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_musikhochschule_wien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_konservatorium_wien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_wiener_philharmoniker` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_finanzamt_neunkirchen_wr` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_inet_internet_service` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `specific_inet_system` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_ufs_bfg` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_how_to_spend_it` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_landespolizeidirektion_wien` | 0.9% | 100.0% | 0.5% | 8 | 8 | 0 |
| `specific_garanta_versicherungsag` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_sivananda_yoga` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_da_deutsche_allgemeine` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_geschenkartikel_gmbh` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_aved_cosmetic` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_yoga_vidya_gmbh` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_universitaet_st_gallen` | 0.8% | 100.0% | 0.4% | 7 | 7 | 0 |
| `specific_magistrat_klagenfurt` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_tschurtschenthaler_walder_fister` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_berwaldkel_mobel_ag` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `specific_immobilienbuero_mandl` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_bundesministeriums_fuer_inneres` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_bundesministeriums_fuer_finanzen` | 0.9% | 100.0% | 0.5% | 8 | 8 | 0 |
| `specific_fag` | 2.6% | 100.0% | 1.3% | 23 | 23 | 0 |
| `specific_faoe` | 4.6% | 100.0% | 2.4% | 41 | 41 | 0 |
| `specific_finanzamt_fur_grossbetriebe` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_deloitte_tax` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `specific_schule_grillenreith` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `specific_bankhaus_denzel` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `specific_cervenka_neunubel_telekom_ag` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_finanzamt_wien_3_6_7_11_15_schwechat_gerasdorf` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_easo` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_bmi` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `specific_kriminalpolizei_oesterreich` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_bm_fuer_inneres` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_flughafen_munchen` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `specific_european_frontex_genitive` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_hla_tourismus` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_hlf_krems` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_universitat_wien` | 2.0% | 100.0% | 1.0% | 18 | 18 | 0 |
| `specific_hallas_partner_wirtschaftspruefung` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_bezirksgericht_purkersdorf` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_university_of_bristol` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `specific_england_org` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_grazer_treuhand_gmbh_partner_kg` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_finanzamts_graz_stadt` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_rhein_normonkel_manufaktur_gmbh` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `specific_fa_waldviertel` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `specific_merkur_treuhand_steuerberatung` | 1.1% | 100.0% | 0.6% | 10 | 10 | 0 |
| `specific_schabetsberger_steuerberatung` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `specific_ufs_salzburg` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_verwaltungsgericht_wien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_steuerberater_metzler` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_finanzamt_innsbruck` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_ikea` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_obi` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_leiner` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_möbelix` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_mömax` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_ottode` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_xxxlutz` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_quelleat` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_seneCura_laurentius_park_bludenz` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `specific_krankenpflegevereins_bludenz` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_finanzamt_wien_1_23_genitive` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `specific_innmarine_gmbh` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_lenfeld_leys_sonderegger` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_universitaet_innsbruck` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_raiffeisenbank_karnische_rion` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `specific_x_gmbh` | 2.2% | 100.0% | 1.1% | 19 | 19 | 0 |
| `specific_ogk` | 4.5% | 100.0% | 2.3% | 40 | 40 | 0 |
| `specific_bundesministerin_fuer_finanzen` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_bdo_austria_gmbh_wp_u_stbges` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_leitnerleitner_gmbh_wirtschaftspruefer_und_steuerberater` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_betriebspruefung_gmbh` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_x_gmbh_hyphen` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `specific_finanzamt_osterreich` | 7.3% | 98.5% | 3.8% | 67 | 66 | 1 |
| `generic_company_gmbh` | 2.4% | 91.3% | 1.2% | 23 | 21 | 2 |
| `specific_wirtschaftsuniversitat_wien` | 2.9% | 89.7% | 1.5% | 29 | 26 | 3 |
| `specific_finanzamt_osterreich_nominative` | 4.7% | 89.4% | 2.4% | 47 | 42 | 5 |
| `specific_magistrat_wien_extended` | 4.6% | 85.4% | 2.4% | 48 | 41 | 7 |
| `specific_suva` | 5.8% | 81.2% | 3.0% | 64 | 52 | 12 |
| `specific_jku_linz` | 1.8% | 76.2% | 0.9% | 21 | 16 | 5 |
| `specific_pva_svs_svb` | 0.6% | 71.4% | 0.3% | 7 | 5 | 2 |
| `specific_bmf` | 0.8% | 58.3% | 0.4% | 12 | 7 | 5 |
| `specific_bundesfinanzgericht` | 25.1% | 43.4% | 17.7% | 709 | 308 | 401 |
| `specific_verwaltungsgerichtshof` | 18.6% | 42.3% | 11.9% | 492 | 208 | 284 |
| `specific_frontex` | 0.9% | 42.1% | 0.5% | 19 | 8 | 11 |
| `specific_ams` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `specific_bfh` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `specific_amtes_fuer_betrugsbekampfung` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `specific_bundesministers_fuer_finanzen` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `specific_verfassungsgerichtshof` | 0.7% | 27.3% | 0.3% | 22 | 6 | 16 |
| `specific_magistratsabteilung_67` | 0.5% | 26.7% | 0.2% | 15 | 4 | 11 |
| `specific_jku_wu_abbreviations` | 1.0% | 22.5% | 0.5% | 40 | 9 | 31 |
| `specific_bfg_genitive` | 0.2% | 22.2% | 0.1% | 9 | 2 | 7 |
| `specific_bfg` | 3.3% | 21.8% | 1.8% | 142 | 31 | 111 |
| `specific_oecd` | 0.1% | 20.0% | 0.1% | 5 | 1 | 4 |
| `specific_ufs` | 0.6% | 18.5% | 0.3% | 27 | 5 | 22 |
| `specific_pensionsversicherungsanstalt` | 0.2% | 15.4% | 0.1% | 13 | 2 | 11 |
| `specific_vwgh` | 1.8% | 11.8% | 1.0% | 144 | 17 | 127 |
| `specific_vfgh` | 0.1% | 2.6% | 0.1% | 39 | 1 | 38 |
| `specific_company_pastl_bachle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_textil_steingartlog` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bauermeister_getränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_sophie_wittmeir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_starker_beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_ugqq_verlag_og` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_tal_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_nord_trinex_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_trafenfen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_oppert_elektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_hagdorn_robotik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_planung_monuniost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_raiffeisenbank_stallhofen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_nordevent_gruppe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bezirksgericht_zell` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_donau_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_greiner_mai_event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_waldtra_sicherheit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_mur_ververzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_wod_sicherheit_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_zumholte_verlag_og` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_strohsack_und_dresbeimdieke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_kudla_kuehnel_solar` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_salzburg_land` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_norkel_software_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_rpxf_immobilien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_klagenfurt_sv_w` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_mauriczat_medien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_sudevent_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_zyjy_automotive_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_nyj_event_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_kubzyk_elektro_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_baden_modling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_schwechat_gerasdorf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_wien_2_20_21_22` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_freistadt_urbahr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_valbruckzor_energie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_technik_ostbachal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_deutschlandsberg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_salzburg_stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_klusner_paffgen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_tschermack_pharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_rosilius_pflege` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_yavasoglu_analyse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_gmunden_vocklabruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_ruterborries_fridrich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_dgcv_ecommerce` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_nkah_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_unter_donunisee` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_lognex_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_sudgarten_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_wien_waldnor_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_naass_elektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bersud_möbel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_unter_heimdorf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_yxtg_maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_mittel_logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_alessi_event_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bludszat_maschinenbau_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_stadt_logglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_judenburg_liezen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_oststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fabruck_eisenstadt_oberwart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_amstetten_melk_scheibbs` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_dias_telekom_institut` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_rheindigital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_zoruniglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_chen_setzekorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_conwil_marine` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_paweltschik_telekom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_basdas_pharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_tirol_ost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_tirol_ost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bezirksgericht_silz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_lg_innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_landesgericht_innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_west_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_annemie_bott` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_stadte_energie_holding` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_milan_haendlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_manfredo_herrschmann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_krolitzki_beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_gronemeier_hovelberndt_ecommerce` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_keltrizor_handel_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_volkbank_wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_elender_cloud` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_sünramm_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_süd_sudwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_südversand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_gäbelt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_steinfurtglanz_landwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_ennsbildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_ostwilnexlogistik_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_mur_donwerk_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_dlcg_bildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bahrdt_digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_wildorftra_ki_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specificbruckmonwil_digital_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_sud_nortri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_hulsebusch_breithaupt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_logal_gruppe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_enns_werkal_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_lexkel_vertrieb_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_kornfelder_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fuchsl_touristik_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_magerlein_logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_dongartcon_landwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bezirksgericht_neunkirchen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_traun_aluni_institut` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_monlogtri_analyse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_unter_gartglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_niederosterreich_mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_niederosterreich_mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_baden_modling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_blazickova_hepprich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_mittelheizung_werke_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_traun_digital_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_mertznich_bau_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_gernot_hirschkorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_hinklein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_huberswoboda` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_unterrecycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_osterreichische_gesellschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bm_fuer_finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_obufug_rule` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bks_steuerberatung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fachhochschule_karnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fh_karnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_sozialversicherung_bauern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `specific_bmf_arbeit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_imre_schaffer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_steiermark_mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_vorarlberg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_landeck_reutte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_oststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_salzburg_stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamtbruck_eisenstadt_oberwart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_company_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzen_tradonnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_lg_zrs_wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bundesministeriums_fuer_justiz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_karl_franzens_universitat_graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_klosterneuburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_kings_school_worcester` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_fa_kirchdorf_perg_steyr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_osterreich_dst12` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_saxinger_chalupsky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_mittel_unisyn_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_ober_lemostnor_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_vennes_recycling_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_baers_walterscheidt_handel_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_b_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_a_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_hausverwaltung_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_finanzamt_hollabrunn_korneuburg_tulln` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bfg_aussenstelle_linz` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `specific_bfg_aussenstelle_linz_paren` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_psd_wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_psycho_wagner_spital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bundesamt_soziales` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `specific_london_film_academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_bundeskanzleramtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `specific_houdek_maschinenbau`

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Houdek Maschinenbau'.

**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.032 | 0.062 | 56 | 56 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 0 | 1481 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_17`)

```
Der Sachverhalt ergibt sich bisherigen Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der Houdek Maschinenbau, Str.Nr.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_18`)

```
95-002/7970, BV 24:  Das Unternehmen Houdek Maschinenbau  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)

```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)

```
Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)

```
Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.
```

```
Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `specific_faoe`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'FAÖ' (Finanzamt Österreich).

**Content:**
```
\bFAÖ\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.024 | 0.046 | 41 | 41 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 41 | 0 | 1514 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)

```
Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)

```
Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)

```
Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_11`)

```
Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_12`)

```
Mit Beschwerdevorentscheidungen vom 17.7.2025 wies das FAÖ die Beschwerden sowohl  gegen den Umsatzsteuerbescheid 2022 vom 5.11.2024, als auch jene das Jahr 2023 betreffend  vom 26.5.2025, als unbegründet ab.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

</details>

---

## `specific_ogk`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1700 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)

```
Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)

```
Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)

```
Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)

```
Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)

```
Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `specific_roelfsen_versicherung`

**F1:** 0.036 | **Precision:** 1.000 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches 'Roelfsen Versicherung'

**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.018 | 0.036 | 32 | 32 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 32 | 0 | 1515 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)

```
Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)

```
Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)

```
Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_24`)

```
zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die Roelfsen Versicherung  durch Übertragung des  gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und  Übernahmsvertrages taxativ angeführten Positionen) erfolgt.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

---

## `specific_fag`

**F1:** 0.026 | **Precision:** 1.000 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'FAG' (Finanzamt für Großbetriebe).

**Content:**
```
\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.013 | 0.026 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 1027 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)

```
Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_5`)

```
Das FAG erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides  2022 vom 8.9.2023 und verband diese mit dem ebenfalls vom selben Tag datierenden  Sachbescheid.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_7`)

```
Am 5.11.2024 hob das FAG den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § 299 BAO auf und erließ einen neuen Jahresbescheid.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_8`)

```
Weiters hob das FAG am  26.5.2025 den Umsatzsteuerbescheid des Jahres 2023 gemäß § 299 BAO auf und verband  1 von 5 Seite 2 von 5
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_10`)

```
Dagegen wurde von der Bf. am 16.6.2025 Beschwerde, eingebracht beim FAG, erhoben.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `specific_bundesfinanzgericht`

**F1:** 0.251 | **Precision:** 0.434 | **Recall:** 0.177  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive forms 'Bundesfinanzgerichtes' and 'Bundesfinanzgerichts' but excludes 'Bundesfinanzgerichts, Außenstelle Linz'.

**Content:**
```
\bBundesfinanzgericht(?:es|s)?\b(?!\s*,\s*Außenstelle\s+Linz)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.434 | 0.177 | 0.251 | 709 | 308 | 401 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 308 | 401 | 1435 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_210`)

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_226`)

```
Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_227`)

```
Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_236`)

```
Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)

**False Positives:**

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_210`)

**False Positives:**

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_226`)

**False Positives:**

```
Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_227`)

**False Positives:**

```
Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `USA` (country)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_236`)

**False Positives:**

```
Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_verwaltungsgerichtshof`

**F1:** 0.186 | **Precision:** 0.423 | **Recall:** 0.119  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.119 | 0.186 | 492 | 208 | 284 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 208 | 284 | 1533 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)

```
II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)

```
Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)

```
Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)

```
Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**

```
II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.
```

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**

```
Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**

```
Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**

```
Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_vwgh`

**F1:** 0.018 | **Precision:** 0.118 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof) but excludes citation contexts like '(VwGH ...', hyphenated compounds, and genitive forms handled separately.

**Content:**
```
\bVwGH\b(?!\s*\()(?![\s,]*\d)(?!-\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.118 | 0.010 | 0.018 | 144 | 17 | 127 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 17 | 127 | 1707 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)

```
Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).
```

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_125`)

```
Die Rechtsfolgen im beschwerdegegenständlichen Fall ergeben sich unmittelbar aus den  anzuwendenden, vom Wortlaut her eindeutigen gesetzlichen Bestimmungen und wurde im  Übrigen der ständigen Rechtsprechung des VwGH gefolgt.
```

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)

**False Positives:**

```
Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_38`)

**False Positives:**

```
Für die Wirksamkeit einer Prozesserklärung ist das Erklärte maßgebend, nicht das Gewollte (vgl  zB VwGH vom 28.2.2008, 2006/16/0129).
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_39`)

**False Positives:**

```
Das Erklärte ist allerdings der Auslegung zugänglich  (vgl. zB VwGH vom 29.7.2010, 2009/15/0152).
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_41`)

**False Positives:**

```
hierbei kommt es  darauf an, wie die Erklärung unter Berücksichtigung der konkreten gesetzlichen Regelung, des  Verfahrenszweckes und der der Behörde vorliegenden Aktenlage objektiv verstanden werden  muss (zB VwGH vom 20.3.2014, 2010/15/0195, VwGH 30.1.2015, Ra 2014/17/0025)
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_42`)

**False Positives:**

```
Ist der Inhalt eines Anbringens eindeutig, ist eine davon abweichende, nach außen auch  andeutungsweise nicht zum Ausdruck kommende Absicht des Einschreiters nicht maßgeblich  (vgl. zB VwGH vom 24.6.2009, 2007/15/0041)
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_bfg`

**F1:** 0.033 | **Precision:** 0.218 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BFG' (Bundesfinanzgericht) but excludes citation contexts like '(BFG ...', hyphenated compounds, and genitive forms handled separately.

**Content:**
```
\bBFG\b(?!\s*\()(?![\s,]*\d)(?!-\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.218 | 0.018 | 0.033 | 142 | 31 | 111 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 31 | 111 | 1698 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_101`)

```
Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_103`)

```
Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_135`)

```
Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_147`)

```
Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_148`)

```
Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_101`)

**False Positives:**

```
Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_103`)

**False Positives:**

```
Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_135`)

**False Positives:**

```
Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_147`)

**False Positives:**

```
Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_148`)

**False Positives:**

```
Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_vfgh`

**F1:** 0.001 | **Precision:** 0.026 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VfGH' (Verfassungsgerichtshof) but excludes citation contexts like '(VfGH ...'.

**Content:**
```
\bVfGH\b(?!\s*\()
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.026 | 0.001 | 0.001 | 39 | 1 | 38 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 38 | 1439 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_32`)

```
Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.
```

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**

```
Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_157`)

**False Positives:**

```
Der VfGH hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_159`)

**False Positives:**

```
Dem genannten VfGH-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung aus dem Jahr 1984 gab die zuständige FLD der Berufung einer  Gesellschafterin gegen die einheitliche und gesonderte Gewinnfeststellung in der Form statt,  dass die im Erstbescheid bei der Gesellschafterin zur Gänze als Gewinnanteil behandelte  Ablösezahlung mit 2/3 zu aktivieren und auf 6 Jahre verteilt abzuschreiben war.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_162`)

**False Positives:**

```
Der VfGH bejahte die Anwendbarkeit des Vorfragentatbestandes.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**

```
Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `specific_company_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Pastl+Bächle Handel' which contains a plus sign and lacks a standard suffix.

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

## `specific_textil_steingartlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Textil Steingartlog'.

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

## `specific_bauermeister_getränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bauermeister Getränke'.

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

## `specific_sophie_wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sophie Wittmeir'.

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

## `specific_starker_beratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Starker Beratung'.

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

</details>

---

<details>
<summary>📋 All Rules</summary>

## `specific_bundesfinanzgericht`

**F1:** 0.251 | **Precision:** 0.434 | **Recall:** 0.177  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht' and its genitive forms 'Bundesfinanzgerichtes' and 'Bundesfinanzgerichts' but excludes 'Bundesfinanzgerichts, Außenstelle Linz'.

**Content:**
```
\bBundesfinanzgericht(?:es|s)?\b(?!\s*,\s*Außenstelle\s+Linz)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.434 | 0.177 | 0.251 | 709 | 308 | 401 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 308 | 401 | 1435 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_210`)

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_226`)

```
Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_227`)

```
Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_236`)

```
Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)

**False Positives:**

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_210`)

**False Positives:**

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im Antrag vom 7.6.2022 beantragte der Bf. die Gewährung einer Nachsicht in Höhe von  37.221,- €.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_226`)

**False Positives:**

```
Beweiswürdigung  Das Bundesfinanzgericht geht in freier Beweiswürdigung vom oben geschilderten Sachverhalt  aus, der im Übrigen im Akteninhalt Deckung findet und von den Verfahrensparteien auch nicht  in Abrede gestellt wurde.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_227`)

**False Positives:**

```
Ergänzend wird festgehalten, dass das Bundesfinanzgericht die  Aussage, wonach die in der Erstaussage im Zuge der GPLA-Prüfung gemachte Angabe, dass die  angegebenen Dienstnehmer zur Ausführung von Tätigkeiten in die USA geschickt wurden, ein  höherer Wahrheitsgehalt als den später im Rahmen dieses Rechtsmittelverfahrens gemachten  Aussagen beizumessen ist, denn es entspricht der Lebenserfahrung, dass die später getätigten  Aussagen den eigenen, hier für den Bf. günstigeren, Rechtsstandpunkt zu untermauern  versuchen.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**
- `USA` (country)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_236`)

**False Positives:**

```
Grundsätzlich schließt sich das Bundesfinanzgericht den Ausführungen in der BVE an,  ergänzend wird betont, dass eine vom Gesetz geforderte Unbilligkeit eine sachliche oder eine  persönliche sein kann.
```

FP: `Bundesfinanzgericht` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_verwaltungsgerichtshof`

**F1:** 0.186 | **Precision:** 0.423 | **Recall:** 0.119  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.119 | 0.186 | 492 | 208 | 284 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 208 | 284 | 1533 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)

```
II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)

```
Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)

```
Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)

```
Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**

```
II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.
```

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**

```
Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**

```
Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**

```
Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_finanzamt_osterreich`

**F1:** 0.073 | **Precision:** 0.985 | **Recall:** 0.038  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and its genitive form 'Finanzamtes Österreich'.

**Content:**
```
\bFinanzamtes?\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.985 | 0.038 | 0.073 | 67 | 66 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 66 | 1 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) ( sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)

```
BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1_1`)

```
BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Agatha Vesper, Albersdorfweg 21, 4973 Rabenfurt, Österreich, betreffend Beschwerde vom 9. Juli 2024 gegen den Bescheid des  Finanzamtes Österreich vom 17. Juni 2024 betreffend Abweisung des Antrages vom  31. Jänner 2024 auf den Erhöhungsbetrag zur Familienbeihilfe ab Jänner 2024, Steuernummer  58-042/7990 (SVNR 6155 130467), beschlossen:   Der Vorlageantrag vom 20. November 2024 wird gemäß § 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht  zurückgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Linda Abdulla  in der Beschwerdesache Merlin Jespersen, LLB,  Graf-Hoyos-Weg 5, 9313 Fiming, Österreich, über die Beschwerde vom 17. Dezember 2019 gegen die Bescheide des  Finanzamtes Österreich vom 16. Dezember 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 bis 2018 zu Steuernummer 37-035/4368  zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_1`)

**False Positives:**

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

FP: `Finanzamtes  Österreich` (organisation)

**✅ Gold Entities:**
- `Dr.in Estelle Niederholz` (person)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

</details>

---

## `specific_houdek_maschinenbau`

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Houdek Maschinenbau'.

**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.032 | 0.062 | 56 | 56 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 0 | 1481 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_17`)

```
Der Sachverhalt ergibt sich bisherigen Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der Houdek Maschinenbau, Str.Nr.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_18`)

```
95-002/7970, BV 24:  Das Unternehmen Houdek Maschinenbau  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)

```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)

```
Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)

```
Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.
```

```
Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `specific_suva`

**F1:** 0.058 | **Precision:** 0.812 | **Recall:** 0.030  

**Format:** `regex`  
**Description:**
Matches 'Schweizerischen Unfallversicherungsanstalt (SUVA)' with flexible whitespace and 'SUVA' alone.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)|\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.812 | 0.030 | 0.058 | 64 | 52 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 52 | 12 | 933 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_8`)

```
Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.
```

| Predicted | Gold |
|---|---|
| `Schweizerischen Unfallversicherungsanstalt (SUVA)` | `Schweizerischen Unfallversicherungsanstalt (SUVA)` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_11`)

```
Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_12`)

```
Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_13`)

```
3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_14`)

```
4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)

**False Positives:**

```
10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;
```

FP: `SUVA` (organisation)

```
10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)

**False Positives:**

```
 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_44`)

**False Positives:**

```
Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_58`)

**False Positives:**

```
In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_63`)

**False Positives:**

```
Rechtliche Beurteilung  2.1. SUVA-Invalidenrente  Gemäß § 3 Abs. 1 Z 4 lit. c EStG 1988 sind Geldleistungen aus einer gesetzlichen Unfallversor- gung sowie dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen ge- setzlichen Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspricht,  steuerbefreit.
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_finanzamt_osterreich_nominative`

**F1:** 0.047 | **Precision:** 0.894 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' specifically to ensure nominative form is caught.

**Content:**
```
\bFinanzamt\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.894 | 0.024 | 0.047 | 47 | 42 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 5 | 1639 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Niklas Bußjann  in der Beschwerdesache ÖkR ÖkR Jonas Sternekicker,  Mühlbach 2, 4851 Fischhamering, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 15. Mai 2025  zu Steuernummer 98-117/5180  ausgefertigten Bescheid betreffend Einkommensteuer für  das Jahr 2024 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_50`)

**False Positives:**

```
Aufgrund dieses Sicherstellungsauftrages pfändete sie mit Bescheid  (Zahlungsverbot) vom 3.4.2024, adressiert an das Finanzamt Österreich (DST12), Dr. Adolf  Schärf Platz 2,1220 Wien, das der Beschwerdeführerin gegenüber dem Finanzamt Österreich  (DST12) zustehende Guthaben auf Steuernummer 01-186/7053.
```

FP: `Finanzamt Österreich` (organisation)

```
Aufgrund dieses Sicherstellungsauftrages pfändete sie mit Bescheid  (Zahlungsverbot) vom 3.4.2024, adressiert an das Finanzamt Österreich (DST12), Dr. Adolf  Schärf Platz 2,1220 Wien, das der Beschwerdeführerin gegenüber dem Finanzamt Österreich  (DST12) zustehende Guthaben auf Steuernummer 01-186/7053.
```

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)
- `Dr. Adolf  Schärf Platz 2,1220 Wien` (address)
- `Finanzamt Österreich  (DST12)` (organisation)
- `01-186/7053` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_52`)

**False Positives:**

```
Am  3.4.2024 wurde der Pfändungsbescheid (Zahlungsverbot) vom 3.4.2024 durch persönliche  Übernahme auch an das Finanzamt Österreich (DST12) zugestellt.
```

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_65`)

**False Positives:**

```
Die  Feststellungen zum Vorhalt betreffend den Umfang der Vollmacht gründen sich auf das  Schreiben der belangten Behörde vom 4.4.2024 und die hierauf ergangene Eingabe der  Beschwerdeführerin vom 16.4.2024 (beides von der Beschwerdeführerin vorgelegt), die  Feststellung zur Zustellung des Pfändungsbescheides an das Finanzamt Österreich (DST12) auf  die diesbezüglich von der belangten Behörde vorgelegte, mit einer Übernahmebestätigung  versehene Bescheidausfertigung (ebenfalls im Verfahren RV/702183/2024).
```

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_125`)

**False Positives:**

```
Damit fehlt dem Pfändungsbescheid vom 3.4.2024, der - anders als der  Sicherstellungsauftrag - durch die Zustellung an das Finanzamt Österreich (DST12) rechtlich  existent geworden ist (vgl. VwGH 9.6.2017, Ra 2017/02/0060), der Titel (vgl. VwGH 10.5.2010,  2009/16/0102;
```

FP: `Finanzamt Österreich` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich (DST12)` (organisation)

</details>

---

## `specific_faoe`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'FAÖ' (Finanzamt Österreich).

**Content:**
```
\bFAÖ\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.024 | 0.046 | 41 | 41 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 41 | 0 | 1514 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)

```
Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)

```
Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)

```
Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_11`)

```
Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_12`)

```
Mit Beschwerdevorentscheidungen vom 17.7.2025 wies das FAÖ die Beschwerden sowohl  gegen den Umsatzsteuerbescheid 2022 vom 5.11.2024, als auch jene das Jahr 2023 betreffend  vom 26.5.2025, als unbegründet ab.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

</details>

---

## `specific_magistrat_wien_extended`

**F1:** 0.046 | **Precision:** 0.854 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien' including genitive 'Magistrats', 'Magistrates', and department variants like ', MA 67', 'MA67', 'Magistratsabteilung 67' with flexible spacing.

**Content:**
```
\bMagistrat(?:es|s)?\s+der\s+Stadt\s+Wien(?:\s*,\s*Magistratsabteilung\s+67|\s*,\s*MA\s*67|\s+Magistratsabteilung\s+67)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.854 | 0.024 | 0.046 | 48 | 41 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 41 | 7 | 1566 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)

```
III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_8`)

```
Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte die Firma Firma, AdrFirma, als  Zulassungsbesitzerin des in Rede stehenden Fahrzeuges mit Schreiben vom 17. Juni 2025, GZ.  MA67/GZ/2025, zur Lenkerauskunft gemäß § 2 Wiener Parkometergesetz 2006 binnen einer  Frist von zwei Wochen ab Zustellung des Schreibens auf (Lenkererhebung).
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)

```
In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)

```
Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.
```

```
Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)

**False Positives:**

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)
```

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)

**False Positives:**

```
Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.
```

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)

**False Positives:**

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)
```

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)

**False Positives:**

```
Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.
```

FP: `Magistrats der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)

**False Positives:**

```
BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.
```

FP: `Magistrates der Stadt Wien` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

</details>

---

## `specific_ogk`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1700 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)

```
Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)

```
Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)

```
Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)

```
Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)

```
Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `specific_roelfsen_versicherung`

**F1:** 0.036 | **Precision:** 1.000 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches 'Roelfsen Versicherung'

**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.018 | 0.036 | 32 | 32 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 32 | 0 | 1515 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)

```
Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)

```
Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)

```
Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_24`)

```
zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die Roelfsen Versicherung  durch Übertragung des  gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und  Übernahmsvertrages taxativ angeführten Positionen) erfolgt.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

---

## `specific_bfg`

**F1:** 0.033 | **Precision:** 0.218 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BFG' (Bundesfinanzgericht) but excludes citation contexts like '(BFG ...', hyphenated compounds, and genitive forms handled separately.

**Content:**
```
\bBFG\b(?!\s*\()(?![\s,]*\d)(?!-\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.218 | 0.018 | 0.033 | 142 | 31 | 111 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 31 | 111 | 1698 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_101`)

```
Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_103`)

```
Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_135`)

```
Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_147`)

```
Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_148`)

```
Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.
```

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_101`)

**False Positives:**

```
Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_103`)

**False Positives:**

```
Nach dem abweisenden Erkenntnis des BFG vom 31.03.2022 (RV/2100724/2019) brachte man  am 07.06.2022 einen Antrag auf Nachsicht gem. § 236 BAO über EUR 65.475,86 ein.
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_135`)

**False Positives:**

```
Im Übrigen kommt es auf das tatsächliche Einsehen in die Databox (zB. auch Öffnen, Lesen,  oder Ausdrucken eines Bescheides) nicht an (vgl. BFG vom 11.5.2016, RV/7104423/2014).
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_147`)

**False Positives:**

```
Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits unmissverständlich dargelegt hat,  sind die Abgabenbescheide auch rechtskonform erlassen worden.
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_148`)

**False Positives:**

```
Zur Einbringung des Einzelunternehmens in die GmbH  Wie das BFG vom 31.03.2022, RV/2100724/2019, bereits klargestellt hat, gilt die GmbH nicht  als Gesamtrechtsnachfolgerin des Einzelunternehmens.
```

FP: `BFG` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_wirtschaftsuniversitat_wien`

**F1:** 0.029 | **Precision:** 0.897 | **Recall:** 0.015  

**Format:** `regex`  
**Description:**
Matches 'Wirtschaftsuniversität Wien' and its abbreviation 'WU Wien'.

**Content:**
```
\b(?:Wirtschaftsuniversit\u00e4t\s+Wien|WU\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.897 | 0.015 | 0.029 | 29 | 26 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 26 | 3 | 1649 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_6`)

```
Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_47`)

```
Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_74`)

```
Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_135`)

```
Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_6`)

```
Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**

```
2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]
```

FP: `Wirtschaftsuniversität Wien` (organisation)

```
2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]
```

FP: `WU Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**

```
Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.
```

FP: `Wirtschaftsuniversität Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

</details>

---

## `specific_fag`

**F1:** 0.026 | **Precision:** 1.000 | **Recall:** 0.013  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'FAG' (Finanzamt für Großbetriebe).

**Content:**
```
\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.013 | 0.026 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 1027 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)

```
Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_5`)

```
Das FAG erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides  2022 vom 8.9.2023 und verband diese mit dem ebenfalls vom selben Tag datierenden  Sachbescheid.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_7`)

```
Am 5.11.2024 hob das FAG den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § 299 BAO auf und erließ einen neuen Jahresbescheid.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_8`)

```
Weiters hob das FAG am  26.5.2025 den Umsatzsteuerbescheid des Jahres 2023 gemäß § 299 BAO auf und verband  1 von 5 Seite 2 von 5
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_10`)

```
Dagegen wurde von der Bf. am 16.6.2025 Beschwerde, eingebracht beim FAG, erhoben.
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

</details>

---

## `generic_company_gmbh`

**F1:** 0.024 | **Precision:** 0.913 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches generic company patterns like 'Name Industry GMBH' including Steuerberatung.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*)\s+(Lebensmittel|Beratung|Handel|Versand|Dienstleistung|Technik|Elektro|Möbel|Maschinenbau|Software|Digital|Logistik|Immobilien|Versicherung|Pharma|Medien|Verlag|Institut|Bau|Touristik|Recycling|Energie|Cloud|Analyse|Transport|Service|Produktion|Entwicklung|Planung|Konstruktion|Fertigung|Herstellung|Vertrieb|Marketing|Consulting|Engineering|Architecture|Design|Construction|Management|Finance|Accounting|Legal|Tax|Audit|Insurance|Banking|Investment|Real\s+Estate|Property|Development|Holding|Group|Corp|Inc|Ltd|AG|KG|GmbH|UG|OHG|GbR|PartG|WEG|Steuerberatung)\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.913 | 0.012 | 0.024 | 23 | 21 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 2 | 1582 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)

```
Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)

```
Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)

```
In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)

```
Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_18`)

```
Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)

**False Positives:**

```
Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

FP: `Die KQPC Versand GMBH` (organisation)

**✅ Gold Entities:**
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)
- `Event Sudkraftlex GMBH` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)

**False Positives:**

```
Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

FP: `Die KQPC Versand GMBH` (organisation)

**✅ Gold Entities:**
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)
- `Event Sudkraftlex GMBH` (organisation)

</details>

---

## `specific_kqpc_versand`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific entity 'KQPC Versand GMBH'.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)

```
Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)

```
Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)

```
In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)

```
Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)

```
Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

## `specific_event_sudkraftlex`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Event Sudkraftlex GMBH'.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1579 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)

```
Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)

```
Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)

```
Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)

```
Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_20`)

```
Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `specific_fa_wien_1_23`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'FA Wien 1/23'.

**Content:**
```
\bFA\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1500 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_27`)

```
Im Wirtschaftsjahr 2007 ist gemäß der beim FA Wien 1/23  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84  Tankstellen erzielt worden.
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)

```
Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)

```
Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_75`)

```
Das BFG hat der Beschwerde stattgegeben (Entscheidung vom 27.01.2016, GZ  RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des FA Wien 1/23  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung (als partiellen Gesamtrechtsnachfolger der Houdek Maschinenbau)  abgeändert.
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)

```
Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

</details>

---

## `specific_finanzamt_wien_1_23`

**F1:** 0.022 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Wien 1/23'.

**Content:**
```
\bFinanzamt\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.022 | 19 | 19 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 0 | 1524 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_3`)

```
über die Beschwerden vom 29. März 2019 gegen den Bescheid des Finanzamt Wien 1/23  vom 29. Jänner  2019 betreffend Wiederaufnahme § 303 BAO /  KSt 2010 Steuernummer 85-900/3590  zu  Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_102`)

```
Unmittelbar nachfolgend hat das BFG die Amtsrevision des Finanzamt Wien 1/23 (samt Veranlagungsakten  sowie Auszügen aus dem Arbeitsbogen der Betriebsprüfung) dem VwGH unter der Zahl Ro  2016/15/0010 zur Entscheidung vorgelegt.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_111`)

```
Mittels VwGH-Entscheidung vom 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die  Amtsrevision des Finanzamt Wien 1/23  als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_135`)

```
Begründend  wurde deshalb durch das Finanzamt Wien 1/23  im Sachbescheid Feststellungsbescheid Gruppenmitglied  2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ  RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Roelfsen Versicherung  als RNF der  Houdek Maschinenbau  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR  1.047.673,40 ergibt.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_137`)

```
Die BFG- Entscheidung RV/5101064/2013 vom 27.01.2016 für das Jahr 2007 (Rechtsvorgänger) wurde  seitens des Finanzamt Wien 1/23  mittels Amtsrevision bekämpft.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

</details>

---

## `specific_x_gmbh`

**F1:** 0.022 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific entity 'X GmbH' which is a placeholder for a company name.

**Content:**
```
\bX\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.022 | 19 | 19 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 0 | 1452 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_113`)

```
Streitfrage wie folgt „Strittig ist, ob für Zwecke der Anwendung des § 35 UmgrStG den  abgespaltenen Tankstellen (Teilbetrieben) zurechnende Verluste 2007 von EUR -882.676,16  vorrangig mit Gewinnen 2007 von der X GmbH verbliebenen Tankstellen (Teilbetrieben) in  Höhe von EUR 1.183.053,01 verrechnet werden (so die Mitbeteiligte) oder ob dies nicht der  Fall ist (so das Finanzamt).
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_114`)

```
In Streit steht also letztlich, weicher Teil des Jahresverlustes 2007  der X GmbH in Anbetracht des § 35 UmgrStG von der X GmbH in den auf das Jahr 2007  folgenden Jahren als Verlustvortrag iSd § 8 Abs. 4 Z 2 KStG 1988 geltend gemacht werden  kann".
```

```
In Streit steht also letztlich, weicher Teil des Jahresverlustes 2007  der X GmbH in Anbetracht des § 35 UmgrStG von der X GmbH in den auf das Jahr 2007  folgenden Jahren als Verlustvortrag iSd § 8 Abs. 4 Z 2 KStG 1988 geltend gemacht werden  kann".
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_121`)

```
Für den Revisionsfall folge daraus: Die X GmbH habe - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen sei.
```

```
Für den Revisionsfall folge daraus: Die X GmbH habe - unter Berücksichtigung der unstrittigen  Feststellungen des Prüfers - im Jahr 2007 einen Gesamtverlust von 3,632.188,29 EUR erzielt,  der für Zwecke des Verlustvortrages in nachfolgenden Veranlagungsjahren gemäß § 35  UmgrStG iVm § 21 UmgrStG entsprechend dem Verursachungszusammenhang auf die bei der  X GmbH verbliebenen und auf die im Wege einer Spaltung auf die R GmbH übergegangenen  Tankstellen aufzuteilen sei.
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_123`)

```
Entscheidend sei allerdings, dass im Veranlagungsjahr 2007 die Spaltung noch nicht erfolgt sei  und der gesamte Verlust des Veranlagungsjahres 2007 von 3,632.188,29 EUR durch die X  GmbH erzielt worden sei.
```

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_124`)

```
Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39
```

```
Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

</details>

---

## `specific_universitat_wien`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches 'Universität Wien' and 'Universität in Wien'.

**Content:**
```
\bUniversität\s+(?:in\s+)?Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.010 | 0.020 | 18 | 18 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 1658 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)

```
T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)

```
Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)

```
Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)

```
Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_3`)

```
Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) bezog für ihre Tochter T., geb. am 2002, von Oktober 2020  (Beginn des Bachelorstudiums Lehramt mit den Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der Universität Wien) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `specific_jku_linz`

**F1:** 0.018 | **Precision:** 0.762 | **Recall:** 0.009  

**Format:** `regex`  
**Description:**
Matches 'Johannes Kepler Universität Linz' and its abbreviation 'JKU Linz'.

**Content:**
```
\b(?:Johannes\s+Kepler\s+Universit\u00e4t\s+Linz|JKU\s+Linz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.762 | 0.009 | 0.018 | 21 | 16 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 16 | 5 | 627 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)

```
angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).
```

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |
| `JKU Linz` | `JKU Linz` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)

```
 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)

```
8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16
```

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)

```
01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

FP: `Johannes Kepler Universität Linz` (organisation)

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)

**False Positives:**

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.
```

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**

```
Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.
```

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_98`)

**False Positives:**

```
Die belangte Behörde bringt vor, dass von den abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der JKU Linz angerechnet wurden.
```

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `specific_vwgh`

**F1:** 0.018 | **Precision:** 0.118 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof) but excludes citation contexts like '(VwGH ...', hyphenated compounds, and genitive forms handled separately.

**Content:**
```
\bVwGH\b(?!\s*\()(?![\s,]*\d)(?!-\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.118 | 0.010 | 0.018 | 144 | 17 | 127 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 17 | 127 | 1707 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)

```
Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).
```

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_125`)

```
Die Rechtsfolgen im beschwerdegegenständlichen Fall ergeben sich unmittelbar aus den  anzuwendenden, vom Wortlaut her eindeutigen gesetzlichen Bestimmungen und wurde im  Übrigen der ständigen Rechtsprechung des VwGH gefolgt.
```

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)

**False Positives:**

```
Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_38`)

**False Positives:**

```
Für die Wirksamkeit einer Prozesserklärung ist das Erklärte maßgebend, nicht das Gewollte (vgl  zB VwGH vom 28.2.2008, 2006/16/0129).
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_39`)

**False Positives:**

```
Das Erklärte ist allerdings der Auslegung zugänglich  (vgl. zB VwGH vom 29.7.2010, 2009/15/0152).
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_41`)

**False Positives:**

```
hierbei kommt es  darauf an, wie die Erklärung unter Berücksichtigung der konkreten gesetzlichen Regelung, des  Verfahrenszweckes und der der Behörde vorliegenden Aktenlage objektiv verstanden werden  muss (zB VwGH vom 20.3.2014, 2010/15/0195, VwGH 30.1.2015, Ra 2014/17/0025)
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_42`)

**False Positives:**

```
Ist der Inhalt eines Anbringens eindeutig, ist eine davon abweichende, nach außen auch  andeutungsweise nicht zum Ausdruck kommende Absicht des Einschreiters nicht maßgeblich  (vgl. zB VwGH vom 24.6.2009, 2007/15/0041)
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_schmeltz_luftfahrt`

**F1:** 0.013 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Schmeltz Luftfahrt'.

**Content:**
```
\bSchmeltz\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.013 | 11 | 11 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 0 | 1524 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)

```
Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_21`)

```
Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)

```
Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_49`)

```
Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_54`)

```
Abgespaltene  Tankstellen  Schmeltz Luftfahrt **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

</details>

---

## `specific_merkur_treuhand_steuerberatung`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'Merkur Treuhand Steuerberatung GmbH' handling potential line breaks or extra spaces.

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 0 | 25 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Hartwig Boehler  in der Beschwerdesache DDr.in Josepha de Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch Merkur Treuhand Steuerberatung GmbH, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom 16. Mai 2024 gegen den Bescheid des Finanzamtes  Österreich vom 13. Mai 2024 betreffend Abrechnung gem. § 216 BAO Steuernummer  01-186/7053  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und festgestellt, dass die  Umbuchung des per 3.4.2024 auf dem Abgabenkonto der Beschwerdeführerin bestehenden  Guthabens i.H.v. € 166.146,40 auf Finanzverwahrnisse unrichtig war.
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_43`)

```
B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.
```

```
B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_44`)

```
Weiters wurde  der Merkur Treuhand Steuerberatung GmbH darin die Vollmacht „zum Empfang von  Schriftstücken, insbesondere der Abgabenbehörden, welche nunmehr ausschließlich dem  Bevollmächtigten zuzustellen sind“ erteilt und mitgeteilt, dass durch die vorliegende Vollmacht  „noch etwa beim Finanzamt erliegende vorhergehende Vollmachten außer Kraft gesetzt“  werden.
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_45`)

```
Im (Begleit-) Schreiben vom 13.3.2024 führt die Merkur Treuhand Steuerberatung  GmbH aus, dass die Vollmacht als „Spezialvollmacht für das laufende Verfahren betreffend  Umsatzsteuer und NOVA sowie das Finanzstrafverfahren“ erteilt wurde.
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung  GmbH` | `Merkur Treuhand Steuerberatung  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)

```
Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

</details>

---

## `specific_dorfcon_verlag`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Dorfcon-Verlag'.

**Content:**
```
\bDorfcon-Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.010 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 1523 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_21`)

```
Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)

```
Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)

```
Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_32`)

```
Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_45`)

```
Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

</details>

---

## `specific_jku_wu_abbreviations`

**F1:** 0.010 | **Precision:** 0.225 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches bare abbreviations 'JKU' and 'WU' for universities.

**Content:**
```
\b(?:JKU|WU)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.225 | 0.005 | 0.010 | 40 | 9 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 31 | 632 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)

```
Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_41`)

```
Siehe Internetseite JKU und WU  Karriereaussichten!
```

```
Siehe Internetseite JKU und WU  Karriereaussichten!
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |
| `WU` | `WU` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)

```
Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)

```
 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.
```

```
 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)

```
https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.
```

```
https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**

```
2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)

**False Positives:**

```
 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

FP: `JKU` (organisation)

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

FP: `JKU` (organisation)

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

FP: `WU` (organisation)

```
 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)

**False Positives:**

```
 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `JKU Linz` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)

**False Positives:**

```
5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `specific_landespolizeidirektion_wien`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirektion Wien'.

**Content:**
```
\bLandespolizeidirektion\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.009 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 1125 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_7`)

```
Entscheidungsgründe  Verfahrensgang:  Das Abstellen des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A)  wurde von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien  (A118) am 18. April 2025 um 11:07 Uhr in 1120 Wien, Meidlinger Hauptstraße 67,  beanstandet, da ein gültiger Parkschein fehlte.
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_19`)

```
In dem Schreiben vom 18. August 2025 wurde zum Ergebnis der Beweisaufnahme angeführt:  „Aus der Organstrafverfügung, welche von einem Organ des Parkraumüberwachungsorgans  der Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung gelegt wurde,  ergibt sich, dass das Fahrzeug der Marke Marke mit dem behördlichen Kennzeichen 123 am  18.04.2025 um 11:07 Uhr in 1120 Wien, Meidlinger Hauptstraße 67, in einer  gebührenpflichtigen Kurzparkzone abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_7`)

```
Entscheidungsgründe  Das mehrspurige Kraftfahrzeug, mit dem behördlichen Kennzeichen W-Kennz. (A) wurde vom  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 07. Mai 2025  um 11:59 Uhr in der gebührenpflichtigen Kurzparkzone in 1050 Wien, Bacherplatz gegenüber  14, beanstandet, da es zur Beanstandungszeit ohne gültigen Parkschein abgestellt war.
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_55`)

```
Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_57`)

```
Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `specific_bundesministeriums_fuer_finanzen`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium für Finanzen' and its genitive form 'Bundesministeriums für Finanzen'.

**Content:**
```
\bBundesministerium(?:s)?\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.009 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 1320 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1_43`)

```
Nach Auskunft des Bundesministeriums für Finanzen in gleichgelagerten Fällen ist der im  Signaturblock angegebene Tag im Allgemeinen jener Tag, an welchem der Bescheid in die  Databox eingebracht wurde, weil diese Einbringung in der Regel innerhalb einer Stunde ab  Erstellung der Amtssignatur erfolgt.
```

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Finanzen` | `Bundesministeriums für Finanzen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_42`)

```
Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG und der österreichischen Wohnadresse Bf-Adr Ö und der Zeitdauer der Benutzung  eines Massenbeförderungsmittels gründen sich auf eine vom Bundesfinanzgericht  durchgeführte Berechnung mit dem von Bundesministerium für Finanzen im Internet zur  Verfügung gestellten Pendlerrechner.
```

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_91`)

```
Gemäß § 3 Abs 1 Pendlerverordnung ist für die Beurteilung, ob die Benützung eines  Massenbeförderungsmittels zumutbar oder unzumutbar ist, für Verhältnisse innerhalb  Österreichs der vom Bundesministerium für Finanzen im Internet zur Verfügung gestellte  Pendlerrechner zu verwenden.
```

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_92`)

```
Das Bundesfinanzgericht führte im Zuge seiner Entscheidungsfindung eine Berechnung mit  dem vom Bundesministerium für Finanzen im Internet zur Verfügung gestellten  Pendlerrechner durch.
```

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_68`)

```
Am 11. Juli 2025 richtete das Bundesfinanzgericht ein Amtshilfeersuchen an das  Bundesministerium für Finanzen.
```

| Predicted | Gold |
|---|---|
| `Bundesministerium für Finanzen` | `Bundesministerium für Finanzen` |

</details>

---

## `specific_frontex`

**F1:** 0.009 | **Precision:** 0.421 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'Frontex'.

**Content:**
```
\bFrontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.421 | 0.005 | 0.009 | 19 | 8 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 11 | 241 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_6`)

```
Über Aufforderung der belangten Behörde gliederte der Bf. die Reisekosten wie folgt auf:  Einsätze für die Grenzschutzagentur Frontex: versteuerte Taggelder  Einsatz im Jahr 2018 als Frontex-Beamter in  Sardinien (I) vom 04.06.
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_62`)

```
Werbungskosten die in Zusammenhang mit Frontex, EASO, ... Einsätzen stehen, dürfen daher in  solchen Fällen nicht berücksichtigt werden.
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_74`)

```
Da mit den von der  Besteuerung ausgenommenen Taggelder in Zusammenhang mit dem Kurzzeiteinsatz für  Frontex auch die laut Reisekosten-Beilage gesondert beantragten Kilometer-/ und Taggeld iHv  355,15 € abgerechnet wurden steht eine weitere pauschalierte Vergütung nicht zu, daher  wurden mit Beschwerdevorentscheidung vom 13.12.2021 alle in Zusammenhang mit dem  Frontex-Einsatz stehenden weiteren Werbungskosten nicht berücksichtigt.“
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_76`)

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer (Bf.) ist Polizist und wurde gemäß § 39a BDG in der Zeit 26. Februar 2025  an Frontex entsendet und war im Auslandseinsatz in Sizilien.
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)

```
Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_6`)

**False Positives:**

```
Über Aufforderung der belangten Behörde gliederte der Bf. die Reisekosten wie folgt auf:  Einsätze für die Grenzschutzagentur Frontex: versteuerte Taggelder  Einsatz im Jahr 2018 als Frontex-Beamter in  Sardinien (I) vom 04.06.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Frontex` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_10`)

**False Positives:**

```
Einsatz im Jahr 2019 als Frontex-Beamter in  Sizilien (I) vom 16.07.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_25`)

**False Positives:**

```
Frontex-Einsatz: Anreise  zumFlugh.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_28`)

**False Positives:**

```
Frontex-Einsatz in Sizilien  (Trapani) 31 x Frühstück a'  5,85   181,35  181,35  18.08.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Trapani` (city)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_43`)

**False Positives:**

```
Zur Reisezulage:  Im Kalenderjahr 2019 war ich einmal für die Organisation "Europäische Grenzschutzagentur  Frontex" in Trapani auf der Insel Silzilien (I) tätig.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Europäische Grenzschutzagentur  Frontex` (organisation)
- `Trapani` (city)

</details>

---

## `specific_lexdon_it`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lexdon IT'.

**Content:**
```
\bLexdon\s+IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 1523 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)

```
Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)

```
Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)

```
Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_31`)

```
Der Lexdon IT  als weiterem partiellen  Gesamtrechtsnachfolger wurde ein Körperschaftsteuerbescheid 2007 zugestellt, der einen  Ergebnisanteil von Null mangels Übergang von verlustverursachenden Vermögen auswies.
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_98`)

```
Im Ergebnis hat das BFG die Rechtsmeinung des Beschwerdeführers geteilt, wonach der bei der  Lexdon IT  im Jahr 2007 insgesamt entstandene Verlust nach Vornahme des  innerbetrieblichen Verlustausgleichs ausschließlich im Zusammenhang mit den übrigen bei der  Houdek Maschinenbau  verbliebenen Tankstellen verbleibt, sodass dieser Verlust zur Gänze zu  negativen Einkünften und infolge dessen zu vortragsfähigen Verlusten führt (vgl. Seite 3 der  Beschwerde vom 31.5.2013 inklusive Gutachten von Univ.-Prof. Dr. Tina Ehrke-Rabel, welches  als integrierender Bestandteil der Beschwerde 31.05.2013 anzusehen ist).
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

</details>

---

## `specific_universitaet_st_gallen`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Universität in St. Gallen' and 'Universität St. Gallen'.

**Content:**
```
\bUniversität\s+(?:in\s+)?St\.\s+Gallen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 250 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_24`)

```
Das Finanzamt erließ eine abweisende Beschwerdevorentscheidung, dies mit folgender  Begründung:   Ihr Sohn P…, geboren am … .2000 studiert seit dem Wintersemester 2020/21 an der Universität  in St. Gallen in der Schweiz, das Studium wird ernsthaft und zielstrebig betrieben.
```

| Predicted | Gold |
|---|---|
| `Universität  in St. Gallen` | `Universität  in St. Gallen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_45`)

```
Der Vorlageantrag wurde erhoben wie folgt:   Hinsichtlich der Begründung meines Begehrens und der beantragten Änderungen verweise ich  auf meine Beschwerde vom 29.7.2023 und auf die Stellungnahme vom 13.10.2023 bzw.  möchte diese ergänzen wie folgt:   Mein Sohn P… (geb. … .00) hat von 2020 bis 2023 erfolgreich an der Universität St. Gallen  studiert.
```

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_50`)

```
Insbesondere im Studium hatte sich die Corona-Pandemie für Studierende der Universität St.  Gallen zu Gunsten der Ortsunabhängigkeit der Studierenden ausgewirkt.
```

| Predicted | Gold |
|---|---|
| `Universität St.  Gallen` | `Universität St.  Gallen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_53`)

```
Außerdem besteht  an der Universität St. Gallen (unabhängig der Pandemie Situation) keine Anwesenheitspflicht.
```

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_68`)

```
Der Sohn P… ist seit dem Herbstsemester 2020 für  das Studium der Betriebswirtschaftslehre an der Universität St. Gallen (HSG) in der Schweiz  inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

</details>

---

## `specific_bmf`

**F1:** 0.008 | **Precision:** 0.583 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BMF' (Bundesministerium für Finanzen).

**Content:**
```
\bBMF\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.583 | 0.004 | 0.008 | 12 | 7 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 5 | 1673 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_24`)

```
Abrufbar auf der  Website des BMF unter Formulare) kann auch für ausländische Arbeitgeber  ausgefüllt werden.
```

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_101`)

```
Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).
```

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_65`)

```
Mangels gesetzlicher Vorgaben, aufgrund der diesbezüglichen  VwGH-Rechtsprechung und nach Ansicht des BMF sei es dem Steuerpflichtigen freigestellt, in  welcher Reihenfolge er den innerbetrieblichen Verlustausgleich vornehme, dh. wie er die  positiven Ergebnisse einzelner Teilbetriebe mit den negativen Ergebnissen anderer Teilbetriebe  saldiere, sodass der Steuerpflichtige die für ihn günstigste Form des Verlustausgleichs wählen  könne.
```

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_8`)

```
Mit  Eingaben vom 8. und 9. August 2023 ergänzte der BF den Antrag dahingehend, dass die  Meldung tatsächlich zunächst noch nicht erfolgt, sondern nur in FOn gespeichert worden sei,  da ein auf Seiten des BMF liegendes technisches Problem die Einbringung verhindere.
```

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_101`)

```
Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).
```

| Predicted | Gold |
|---|---|
| `BMF` | `BMF` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_101`)

**False Positives:**

```
Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).
```

FP: `BMF` (organisation)

**✅ Gold Entities:**
- `BMF` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_86`)

**False Positives:**

```
BMF, AÖF 2006/128, Abschn 5; UFS 24.8.2009, RV/0430-L/04;
```

FP: `BMF` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_98`)

**False Positives:**

```
BFG  9.1.2019, RV/3100898/2018),   die persönlichen, insbesondere die wirtschaftlichen Verhältnisse des  Abgabepflichtigen (BMF, AÖF 2006/128, Abschn 4; BFG 14.8.2017,  RV/7102275/2017).
```

FP: `BMF` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_100`)

**False Positives:**

```
BMF, AÖF 2006/128, Abschn 4).
```

FP: `BMF` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_101`)

**False Positives:**

```
Es sind daher alle Semester aus den  vorherigen Studien, in denen eine Fortsetzungsmeldung vorgelegen ist und für die  Familienbeihilfe bezogen wurde, in Bezug auf die Wartezeit bis zur Wiedergewährung der  Familienbeihilfe für das neue Studium heranzuziehen (vgl. Erlass des BMF vom 05.10.2010,  BMF-110900/0003-IV/2/2010).
```

FP: `BMF` (organisation)

**✅ Gold Entities:**
- `BMF` (organisation)

</details>

---

## `specific_inet_internet_service`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'INET Internet Service GmbH' specifically to avoid partial matches.

**Content:**
```
\bINET\s+Internet\s+Service\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 111 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_6`)

```
Entscheidungsgründe  Laut den Feststellungsbescheiden des Finanzamts Neunkirchen Wiener Neustadt vom  9.11.2011 für die Jahre 2001 bis 2003 und Nichtfeststellungsbescheid für das Jahr 2004  betreffend INET Internet Service GmbH und Mitges.
```

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_13`)

```
Mit den gegenständlich angefochtenen Einkommensteuerbescheiden für die Jahre 2001 bis  2003 vom 21.12.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (FA 07) die  Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter Berücksichtigung der  Grundlagenbescheide vom 9.11.2011 betreffend Mitunternehmerschaft (atypisch stillen  Beteiligung) an der INET Internet Service GmbH und Mitges., St.nr.: ***, (Beteiligung in den  Streitjahren) fest.
```

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_31`)

```
Der Bf. war unstrittig in den Streitjahren an der INET Internet Service GmbH und Mitges.
```

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_75`)

```
Im Zuge von Wiederholungsprüfungen gem. § 99 FinStrG u.a. bei der INET Internet Service  GmbH und Mitges.
```

| Predicted | Gold |
|---|---|
| `INET Internet Service  GmbH` | `INET Internet Service  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_83`)

```
Im Jahr 2008 wurde am 30.1.2008 ein Bescheid gemäß § 293b BAO betreffend das  Feststellungsverfahren der INET Internet Service GmbH und atypisch Stille erlassen, mit  welchem die Feststellungsbescheide für 2001 und 2002, beide vom 22.3.2006, abgeändert  wurden.
```

| Predicted | Gold |
|---|---|
| `INET Internet Service GmbH` | `INET Internet Service GmbH` |

</details>

---

## `specific_schule_grillenreith`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the various forms of the school name 'Schule für allgemeine Gesundheits- und Krankenpflege Grillenreith' and its variants.

**Content:**
```
\bSchule\s+f\u00fcr\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+(?:am\s+LKH\s+)?Grillenreith|Gesundheits\-\s+und\s+Krankenpflege\-Schule\s+am\s+LKH\s+Grillenreith|Schule\s+f\u00fcr\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+in\s+Grillenreith
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 789 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_6`)

```
2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.
```

| Predicted | Gold |
|---|---|
| `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` | `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_10`)

```
Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.
```

| Predicted | Gold |
|---|---|
| `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` | `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_13`)

```
4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.
```

| Predicted | Gold |
|---|---|
| `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` | `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_20`)

```
Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.
```

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_26`)

```
Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.
```

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` |

</details>

---

## `specific_flughafen_munchen`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Flughafen München' and 'Flughafen  München' (with double space).

**Content:**
```
\bFlughafen\s+(?:München|Muenchen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 231 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)

```
Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.
```

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_83`)

```
Der Bf. macht Werbungskosten geltend, die im Zusammenhang mit dem Auslandseinsatz  stehen und zwar Frühstückskosten iHv € 181,35, sowie An- und Rückreisekosten zum Flughafen  München iHv € 173,80.
```

| Predicted | Gold |
|---|---|
| `Flughafen  München` | `Flughafen  München` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)

```
Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.
```

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_127`)

```
II. Zu den Frühstücks- und Reisekosten:  In Streit steht die Rechtsfrage, ob pauschale Frühstückskosten sowie die An- und  Rückreisekosten zum Flughafen München als Werbungskosten im Zusammenhang mit der  Auslandstätigkeit des Bw., für die er eine steuerfreie Auslandszulage iSd § 21 Gehaltsgesetz  erhalten hat, zu berücksichtigen sind.
```

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_139`)

```
Die Kosten für die Fahrt  zwischen Wohnort und Flughafen München, die der Bf. mit dem eigenen PKW zurückgelegt  hat, wurden nicht ersetzt.
```

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

</details>

---

## `specific_university_of_bristol`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'University of Bristol'.

**Content:**
```
\bUniversity\s+of\s+Bristol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 663 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_26`)

```
Die Tochter studiert an der University of Bristol bis voraussichtlich Juli 2023.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_30`)

```
Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_66`)

```
Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_67`)

```
2…7 is studying for a Chemistry (BSc) full time at the University of Bristol.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_68`)

```
Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

</details>

---

## `specific_schabetsberger_steuerberatung`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Schabetsberger Steuerberatung GmbH'.

**Content:**
```
\bSchabetsberger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 20 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_51`)

```
Beide Bescheide (der an das  Finanzamt Österreich adressierte Pfändungsescheid vom 3.4.2024 ergänzt um die Anmerkung  „Ausfertigung für den Abgabenschuldner“) wurden der Beschwerdeführerin am 5.4.2024 zu  Handen der Schabetsberger Steuerberatung GmbH, Fischerstiege 9, 1010 Wien, zugestellt.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)

```
Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_63`)

```
Die Feststellungen zum Sicherstellungsauftrag vom 20.3.2024 und zum Pfändungsbescheid  vom 3.4.2024 gründen sich auf eine Einsichtnahme in den Akt RV/702183/2024 des  Bundesfinanzgerichtes (dort bekämpft die Beschwerdeführerin den Pfändungsbescheid vom  3.4.2024), insbesondere auf den Zustellnachweis (Rückschein) zum Sicherstellungsauftrag vom  20.3.2024 und zum Pfändungsbescheid vom 3.4.2024, worin ein Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der Schabetsberger Steuerberatung GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, sowie auf das Schreiben der  Merkur Treuhand Steuerberatung GmbH vom 13.3.2024 und die damit übermittelte Vollmacht  vom 11.3.2024.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_108`)

```
Gleichzeitig wurden alle bis dahin beim  Finanzamt erliegenden Vollmachten (daher auch eine allfällige Zustellvollmacht der  Schabetsberger Steuerberatung GmbH) aufgelöst.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_114`)

```
Die Zustellung an die Schabetsberger  Steuerberatung GmbH war unwirksam.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger  Steuerberatung GmbH` | `Schabetsberger  Steuerberatung GmbH` |

</details>

---

## `specific_verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 0.273 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive forms 'Verfassungsgerichtshofes' and 'Verfassungsgerichtshofs'.

**Content:**
```
\bVerfassungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.273 | 0.003 | 0.007 | 22 | 6 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 16 | 1577 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)

```
die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)

```
Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149708.1`) ( sent_id: `findok-manually-annotated_TRAIN/149708.1_2`)

```
Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)

```
Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)

```
Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**

```
Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_172`)

**False Positives:**

```
Der Verfassungsgerichtshof ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein  derartiger Fall, nämlich wenn eine Entscheidung derselben Behörde für einen früheren  Steuerzeitraum, die sich in der rechtlichen Würdigung des Sachverhaltes direkt auf einen  (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt, in gleicher Weise behandelt  werden muss, wie der Fall der Vorfrage;
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**

```
Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_293`)

**False Positives:**

```
2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;
```

FP: `Verfassungsgerichtshofes` (organisation)

```
2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_295`)

**False Positives:**

```
Im der  zitierten Entscheidung des Verfassungsgerichtshofes zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher Aktivierung eine beantragte Wiederaufnahme für die Folgejahre  zwecks Berücksichtigung der AfA vorzunehmen ist.
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_rhein_normonkel_manufaktur_gmbh`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Rhein Normonkel Manufaktur GMBH'.

**Content:**
```
\bRhein\s+Normonkel\s+Manufaktur\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 431 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_32`)

```
Der ehemalige Arbeitgeber unseres Klienten, die Firma Rhein Normonkel Manufaktur GMBH, hat ihren Sitz in  4331  Wien, Elmbachweg (siehe aktenkundigen Lohnzettel).
```

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_69`)

```
II. Über die Beschwerde wurde erwogen:  1. Festgestellter Sachverhalt:  Der Bf war im Streitjahr für die in Wien ansässige Rhein Normonkel Manufaktur GMBH, einem Marktführer im  institutionellen Hygienebereich, als Außendienstmitarbeiter (Vertreter) nichtselbständig tätig.
```

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_70`)

```
Im Rahmen dieses Dienstverhältnisses wurde dem Bf von der Rhein Normonkel Manufaktur GMBH  ein Dienstwagen  der Marke Skoda Octavia zur Verfügung gestellt, welchen der Bf auch für Privatfahrten nutzte.
```

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_71`)

```
Die Rhein Normonkel Manufaktur GMBH  setzte in der laufenden Lohnverrechnung den vollen Pkw-Sachbezug iHv  332,06 Euro monatlich an.
```

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_72`)

```
Auch in den von der Rhein Normonkel Manufaktur GMBH  an das Finanzamt  übermittelten Lohnzettel, der den im Einkommensteuerbescheid 2014 vom 20.5.2015  ausgewiesenen Einkünften aus nichtselbständiger Arbeit zugrunde liegt, hat der volle Pkw- Sachbezug Eingang gefunden.
```

| Predicted | Gold |
|---|---|
| `Rhein Normonkel Manufaktur GMBH` | `Rhein Normonkel Manufaktur GMBH` |

</details>

---

## `specific_raiffeisenbank_karnische_rion`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Karnische Rion Bankstelle St.Stefan' with flexible whitespace to handle double spaces.

**Content:**
```
\bRaiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 991 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_13`)

```
Die belangte Behörde forderte den Beschwerdeführer mit Schreiben vom 08.11.2022 auf,  Nachweise zu erbringen, die belegen, dass dieser nicht Kontoinhaber des Kontos mit der  AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  sei.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_36`)

```
Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis  zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der  Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_39`)

```
Der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  wurde der Bescheid vom 10.10.2022 zugestellt und aufgetragen, die  gepfändeten Forderungen nicht mehr an den Abgabenschuldiger auszuzahlen.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_41`)

```
Der Beschwerdeführer ist Kontoinhaber des Kontos mit der AT78 2024 1897 7421 2903  bei der  Raiffeisenbank Karnische Rion  Bankstelle St.Stefan.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_45`)

```
Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend  Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

</details>

---

## `specific_pva_svs_svb`

**F1:** 0.006 | **Precision:** 0.714 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches abbreviations 'PVA' and 'SVS/SVB' in context of social security.

**Content:**
```
\b(?:PVA|SVS/SVB)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.714 | 0.003 | 0.006 | 7 | 5 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 2 | 1321 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_10`)

```
In ihrer Beantwortung vom 27.11.2019 gab die Bf an, dass die nicht vom Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der PVA einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) erhalten würde.
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_13`)

```
Dazu wurden von der Bf Bestätigungen der PVA, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten für Nervenheilkunde vorgelegt.
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_63`)

```
Davon wurde ein Selbstbetrag von der PVA direkt  an den Kostenträger zur teilweisen Deckung der Verpflegungskosten iHv 1.086,53 Euro  überwiesen.
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_64`)

```
Der Restbetrag (lt Verständigung über die Leistungshöhe zum 01.01.2017 der PVA  war dies ein Betrag von ca 200,00 bis 230,00 Euro) verblieb bei der Mutter der Bf als  „Taschengeld“.
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_80`)

```
2. Beweiswürdigung  Der Sachverhalt ist grundsätzlich unstrittig und ergibt sich als solcher aus dem Akt,  insbesondere den angeführten Aktenteilen wie den Bestätigungen der PVA, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_11`)

**False Positives:**

```
Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).
```

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)
- `SENECURA` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_12`)

**False Positives:**

```
Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.
```

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)

</details>

---

## `specific_ufs`

**F1:** 0.006 | **Precision:** 0.185 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'UFS' only when not followed by 'Salzburg' or part of 'UFS/BFG'.

**Content:**
```
\bUFS\b(?!\s+Salzburg)(?!/BFG)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.185 | 0.003 | 0.006 | 27 | 5 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 22 | 1478 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)

```
Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.
```

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)

```
85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.
```

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_141`)

```
19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)   29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)   16.12.2013 Vorlage an BFG (damals noch UFS)   17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  07.03.2016 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010   07.03.2016 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010 (Erhöhung des  Verlustvortrages infolge BFG-Erkenntnis RV/5101064/2013)
```

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_68`)

```
1.13. Gemäß § 323 Abs. 38 BAO sind die am 31.12.2013 beim UFS als Abgabenbehörde zweiter  Instanz anhängigen Berufungen vom Bundesfinanzgericht (BFG) als Beschwerden im Sinn des  Art. 130 Abs. 1 B-VG zu erledigen.
```

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_19`)

```
Die Berufung bzw. Beschwerde gegen die strittigen Einkommensteuerbescheide wurde ohne  Erlassung einer Berufungsvorentscheidung (nunmehr Beschwerdevorentscheidung) an den  damaligen UFS (nunmehr: BFG) vorgelegt.
```

| Predicted | Gold |
|---|---|
| `UFS` | `UFS` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_64`)

**False Positives:**

```
UFS 27.11.2007, RV/0087-L/07).
```

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_78`)

**False Positives:**

```
UFS 18.2.2010, RV/0098-L/06;
```

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_82`)

**False Positives:**

```
BFG 9.1.2019, RV/3100898/2018),   die Höhe des durch die verspätete Einreichung der Abgabenerklärung erzielten  finanziellen Vorteils (vgl UFS 21.10.2003, RV/0234-G/02, FJ 2004, 77;
```

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_86`)

**False Positives:**

```
BMF, AÖF 2006/128, Abschn 5; UFS 24.8.2009, RV/0430-L/04;
```

FP: `UFS` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_93`)

**False Positives:**

```
UFS 27.11.2007, RV/0087-L/07;
```

FP: `UFS` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_fa_st_johann`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA St. Johann Tamsweg Zell am See'.

**Content:**
```
\bFA\s+St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 1627 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.
```

| Predicted | Gold |
|---|---|
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |
| `FA St. Johann Tamsweg Zell am See` | `FA St. Johann Tamsweg Zell am See` |

</details>

---

## `specific_lubomir_merschmeyer`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Lubomir Merschmeyer'

**Content:**
```
\bLubomir\s+Merschmeyer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 1543 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)

```
Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)

```
Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_419`)

```
Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum Gözcü Getränke) war im Jahr 2010 Gruppenmittglied  der Unternehmensgruppe mit dem Gruppenträger Magdalena Diegmueller, LLB (vormals Lubomir Merschmeyer).
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

</details>

---

## `specific_finanzamt_wien_klosterneuburg`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Wien 9/18/19 Klosterneuburg' and its genitive form.

**Content:**
```
\bFinanzamt(?:es)?\s+Wien\s+9/18/19\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 1159 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)

```
Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138410.1`) ( sent_id: `findok-manually-annotated_TRAIN/138410.1_2`)

```
Gerald Erwin Ehgartner in der  Beschwerdesache Prof.in Klara Dolejsch, vertreten durch die Prof.in Tamara Simanek, über die Beschwerde vom 2.  November 2020 gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr  zuständig: Finanzamt Österreich) vom 9. September 2020 betreffend Abweisung des Antrags  auf Wiedereinsetzung in den vorigen Stand gemäß § 308 BAO zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)

```
BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_13`)

```
Mit den gegenständlich angefochtenen Einkommensteuerbescheiden für die Jahre 2001 bis  2003 vom 21.12.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (FA 07) die  Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter Berücksichtigung der  Grundlagenbescheide vom 9.11.2011 betreffend Mitunternehmerschaft (atypisch stillen  Beteiligung) an der INET Internet Service GmbH und Mitges., St.nr.: ***, (Beteiligung in den  Streitjahren) fest.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

</details>

---

## `specific_berwaldkel_mobel_ag`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Berwaldkel-Möbel AG'.

**Content:**
```
\bBerwaldkel-Möbel\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 717 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_5`)

```
Das Pendlerpauschale war bereits vom Arbeitgeber Berwaldkel-Möbel AG  berücksichtigt worden, hatte  aber dort wegen der Geringfügigkeit der Einkünfte bei der Berechnung der Lohnsteuer keine  Auswirkung.
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_7`)

```
Es wurden daher auch im Einkommensteuerbescheid 2016 vom 27.02.2017 bei der  Berechnung des Einkommens und der Einkommensteuer die bereits um das Pendlerpauschale  in Höhe von 1.476,00 € gekürzten Einkünfte bei der Fa. Berwaldkel-Möbel AG  in Ansatz gebracht.
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_16`)

```
Beigelegt war eine Bestätigung der Firma Berwaldkel-Möbel AG  vom 09.03.2021, wonach die Beschwerdeführerin das Pendlerpauschale beantragt hätte, es  aber von der Firma nicht berücksichtigt habe werden können, da das Einkommen nicht  lohnsteuerpflichtig sei.
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_27`)

```
Gleichzeitig wurde in Punkt 2) des Ergänzungsersuchens ausführlich dargestellt, dass das  Pendlerpauschale in den Einkommensteuerbescheiden 2016, 2017 und 2018 dadurch  Berücksichtigung gefunden habe, dass die vom Arbeitgeber Berwaldkel-Möbel AG  übermittelten Einkünfte  schon um das Pendlerpauschale gekürzt worden waren.
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

</details>

---

## `specific_bankhaus_denzel`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Bankhaus Denzel' which was missing from the rules.

**Content:**
```
\bBankhaus\s+Denzel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 877 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_11`)

```
für Wohnraumschaffung, das Pendlerpauschale und die Kosten für doppelte Haushaltsführung  und Familienheimfahrten näher zu erläutern und zu belegen, übermittelte der  Beschwerdeführer eine Reihe von Urkunden, darunter ein Kreditantrag an die Bankhaus Denzel  vom 7.9.2000, einen Kfz-Zulassungsschein und eine Auflistung der Fahrten vom  Familienwohnsitz in Ungarn nach Wien und zurück sowie der Fahrten von seinem Quartier in  Wien zum jeweiligen Arbeitsort und zurück.
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_50`)

```
Zu den  Kosten der Wohnraumschaffung bzw. -sanierung legte er nochmals die bereits übermittelten  Kreditunterlagen aus dem Jahr 2000 sowie ein Schreiben der Bankhaus Denzel  vom 26.3.2015 vor,  worin ihm mitgeteilt wird, dass auf dem Kreditkonto ein Saldo i.H.v. € 23.904,50 (inkl. Zinsen  sowie Anwalts- und Gerichtskosten) unberichtigt aushaftet und er aufgefordert wird, die  monatlichen Einzahlungen i.H.v. € 200,00 ab sofort auf dieses Kreditkonto vorzunehmen.
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_73`)

```
Im Jahr 2000 nahm der Beschwerdeführer einen Kredit über ATS 300.000,00 bei der  Bankhaus Denzel  zum Zwecke eines Hausbaues in Ungarn auf.
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_90`)

```
Die Feststellungen zum Kredit ergeben sich aus den vom Beschwerdeführer vorgelegten  Unterlagen, nämlich dem Kreditantrag vom 7.9.2000, der Selbstauskunft vom 31.8.2001 und  dem Schreiben der Bankhaus Denzel  vom 26.3.2015.
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

</details>

---

## `specific_bmi`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BMI' (Bundesministerium für Inneres).

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 237 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_66`)

```
Mit Schriftsatz vom 07. Jänner 2022 stellte der Bf. einen Vorlageantrag in welchem er  zusätzlich zu dem Vorbringen in der Beschwerde noch angibt, dass eine weitere Möglichkeit für  die steuerfreie Berücksichtigung der € 2.114,80 ein berichtigter Lohnzettel des BMI wäre.
```

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)

```
Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.
```

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)

```
Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.
```

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_93`)

```
Dem Erkenntnis des  Verwaltungsgerichtshofes vom 4. November 2020, Ra 2020/16/0039-6, liegt die  Grundausbildungsverordnung-Exekutivdienst BMI des Bundesministers für Inneres, BGBl. II  vom 12. Juni 2017, zu Grunde.
```

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

</details>

---

## `specific_finanzamt_wien_1_23_genitive`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Wien 1/23' (genitive form).

**Content:**
```
\bFinanzamtes\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 1355 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

</details>

---

## `specific_magistratsabteilung_67`

**F1:** 0.005 | **Precision:** 0.267 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Magistratsabteilung 67' as a standalone entity.

**Content:**
```
\bMagistratsabteilung\s+67\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.267 | 0.002 | 0.005 | 15 | 4 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 11 | 1128 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated_TRAIN/148818.1_9`)

```
Mit Schreiben der Magistratsabteilung 67 vom 28. April 2025 (Lenkererhebung) wurde die  Firma Firma als Zulassungsbesitzerin des in Rede stehenden mehrspurigen Kraftfahrzeuges  aufgefordert, binnen zwei Wochen nach Zustellung Auskunft darüber zu erteilen, wem das  genannte Kraftfahrzeug zum Beanstandungszeitpunkt überlassen wurde.
```

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated_TRAIN/148818.1_55`)

```
Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 18. Juni 2025).
```

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_9`)

```
Mit Schreiben der Magistratsabteilung 67 vom 28. April 2025 (Lenkererhebung) wurde die  Firma Firma als Zulassungsbesitzerin des in Rede stehenden mehrspurigen Kraftfahrzeuges  aufgefordert, binnen zwei Wochen nach Zustellung Auskunft darüber zu erteilen, wem das  genannte Kraftfahrzeug zum Beanstandungszeitpunkt überlassen wurde.
```

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_55`)

```
Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsstrafakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 18. Juni 2025).
```

| Predicted | Gold |
|---|---|
| `Magistratsabteilung 67` | `Magistratsabteilung 67` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_8`)

**False Positives:**

```
Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte die Firma Firma, AdrFirma, als  Zulassungsbesitzerin des in Rede stehenden Fahrzeuges mit Schreiben vom 17. Juni 2025, GZ.  MA67/GZ/2025, zur Lenkerauskunft gemäß § 2 Wiener Parkometergesetz 2006 binnen einer  Frist von zwei Wochen ab Zustellung des Schreibens auf (Lenkererhebung).
```

FP: `Magistratsabteilung 67` (organisation)

**✅ Gold Entities:**
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_54`)

**False Positives:**

```
Die Magistratsabteilung 67 legte die Beschwerde samt dem bezughabenden Verwaltungsakt  dem Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 8. Oktober 2025).
```

FP: `Magistratsabteilung 67` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_20`)

**False Positives:**

```
Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 8. Oktober 2025).
```

FP: `Magistratsabteilung 67` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_20`)

**False Positives:**

```
Die Magistratsabteilung 67 legte die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 8. Oktober 2025).
```

FP: `Magistratsabteilung 67` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_1`)

**False Positives:**

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Emanuela Deider, Astätt 60, 4682 Wilding, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 26. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 29. August 2025, Zahl: MA67/MA-GZ/2025 zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.
```

FP: `Magistratsabteilung 67` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Karoline Windsteig` (person)
- `Emanuela Deider` (person)
- `Astätt 60, 4682 Wilding, Österreich` (address)
- `Wien` (city)
- `Wien` (city)
- `Wien` (city)
- `Wien` (city)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

## `specific_gozcu_getranke`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Gözcü Getränke'.

**Content:**
```
\bGözcü\s+Getränke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1379 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_412`)

```
Ein Firmenbuchauszug vom 9.7.2024 ergab, dass die Gözcü Getränke  seit 15.5.2024 aufgrund  einer Neufassung des Gesellschaftsvertrages infolge Verkaufs nunmehr RgR Dipl.
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_419`)

```
Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum Gözcü Getränke) war im Jahr 2010 Gruppenmittglied  der Unternehmensgruppe mit dem Gruppenträger Magdalena Diegmueller, LLB (vormals Lubomir Merschmeyer).
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_420`)

```
Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum Gözcü Getränke) ist als Rechtsnachfolgerin der  Roelfsen Versicherung  auch partielle Rechtsnachfolgerin der Houdek Maschinenbau.
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

</details>

---

## `specific_deloitte_tax`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Deloitte Tax Wirtschaftsprüfungs GmbH'.

**Content:**
```
\bDeloitte\s+Tax\s+Wirtschaftsprüfungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1356 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_2`)

```
Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Fabienne Jostl, Aufschließungsweg Löx Gründe Tschierweg 3, 9862 Vorderkrems, Österreich  vertreten durch Deloitte Tax Wirtschaftsprüfungs  GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerden gegen die Bescheide des  Finanzamtes Österreich vom 5.11.2024 und 26.5.2025 betreffend Umsatzsteuer 2022 und 2023  zu Recht erkannt (Steuernummer 81-450/8995):   I. Die Beschwerdevorentscheidungen des Finanzamtes Österreich vom 17.7.2025, mit  welchen über die Beschwerden gegen die Bescheide des Finanzamtes für Großbetriebe  vom 5.11.2024 (USt 2022) und 26.5.2025 (USt 2023) abgesprochen wurde, werden  wegen Unzuständigkeit der bescheiderlassenden Behörde aufgehoben.
```

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs  GmbH` | `Deloitte Tax Wirtschaftsprüfungs  GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

</details>

---

## `specific_fa_waldviertel`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'FA Waldviertel' which was missing from the rules.

**Content:**
```
\bFA\s+Waldviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1740 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Edwin Brunnarius  in der Beschwerdesache Eberhard Grossmüller,  Garanaser Straße 17H, 3800 Merkenbrechts, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Schubertstraße 62, 8010 Graz, über die Beschwerde vom  21. März 2023 gegen den Bescheid des FA Waldviertel  vom 17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer 94-628/5503  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_88`)

```
Schreiben der steuerlichen Vertretung der Bf. vom 14. Juni 2021:   Mit Abweisungsbescheid vom 04.02.2020 des FA Waldviertel wurde Familienbeihilfe für die  das Kind … (Nachname die Bf.) (VNR … 05 00) für den Zeitraum September 2019 bis Februar  2020 (ist der Zeitpunkt der Erlassung des Bescheides) abgewiesen.
```

| Predicted | Gold |
|---|---|
| `FA Waldviertel` | `FA Waldviertel` |

</details>

---

## `specific_sudver_handel`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sudver Handel Services GMBH'.

**Content:**
```
\bSudver\s+Handel\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)

```
Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.
```

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)

```
Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.
```

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

</details>

---

## `specific_glanznorost`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Glanznorost Institut GMBH'.

**Content:**
```
\bGlanznorost\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)

```
Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.
```

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)

```
Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.
```

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

</details>

---

## `specific_mag_ghesla`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Mag. Ghesla Steuerberater GmbH'.

**Content:**
```
\bMag\.\s+Ghesla\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 988 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.
```

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.
```

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

</details>

---

## `specific_finanzamt_neunkirchen_wr`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Neunkirchen Wr. Neustadt' and its genitive form.

**Content:**
```
\bFinanzamt(?:es)?\s+Neunkirchen\s+Wr\.?\s+Neustadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1227 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Corvin Diebald, Pitzelstätten 4, 2490 Ebenfurth, Österreich, vertreten durch Dr. Ronald Rödler, Lagerstraße 5/1/20, 2460  Bruck/Leitha über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 11. September 2019  betreffend Aussetzung gemäß § 212a BAO zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes  Neunkirchen Wr. Neustadt` | `Finanzamtes  Neunkirchen Wr. Neustadt` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_76`)

```
für die Jahre 2001 bis 2003 wurde vom Finanzamt Neunkirchen Wr.  Neustadt zu Eingangsrechnungen der geprüften Gesellschaften festgestellt, dass diesen seitens  der entsprechenden Geschäftspartner niemals Gegenleistungen gegenübergestanden hätten,  sondern die Erbringung von Leistungen durch die in den Rechnungen angeführten Personen  vorgetäuscht wurden.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Neunkirchen Wr.  Neustadt` | `Finanzamt Neunkirchen Wr.  Neustadt` |

</details>

---

## `specific_inet_system`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'INET System Informations GmbH' specifically.

**Content:**
```
\bINET\s+System\s+Informations\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 105 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_84`)

```
Weiters wurde am 9. Dezember 2008 im Rahmen der Ermittlungen zu den  Feststellungsbescheiden 2000 bis 2007 zur Geltendmachung des Angabenanspruchs ein  Ergänzungsersuchen des Finanzamts Neunkirchen Wiener Neustadt an INET System  Informations GmbH und Mitges.
```

| Predicted | Gold |
|---|---|
| `INET System  Informations GmbH` | `INET System  Informations GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_87`)

```
Im Jahr 2009 wurde am 9.10.2009 der Prüfungsauftrag betreffend die INET System  Informations GmbH und Mitges.
```

| Predicted | Gold |
|---|---|
| `INET System  Informations GmbH` | `INET System  Informations GmbH` |

</details>

---

## `specific_bundesministeriums_fuer_inneres`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Inneres' (genitive) and 'Bundesministerium für Inneres' (nominative).

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 268 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_87`)

```
Dass die  Liegenschaft vor dem 31.12.2019 an den Käufer übergeben wurde hat die Bf. einerseits selbst  in ihrer Erklärung an Eides statt vom 19.07.2022 ausgeführt und deckt sich andererseits mit  den Eintragungen im Zentralen Melderegister des Bundesministeriums für Inneres (demnach  wurde der verfahrensgegenständliche Hauptwohnsitz am 19.12.2019 abgemeldet).
```

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Inneres` | `Bundesministeriums für Inneres` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_72`)

```
Die Differenz iHv 2.114,80 €  entspricht dem mit dem Kurzzeiteinsatz zusammenhängenden, im Lohnzettel des  Bundesministerium für Inneres ausgewiesenen Reisekostenersatz, welcher zuvor iSd § 47 EStG  durch Abzug vom Arbeitslohn versteuert wurde.
```

| Predicted | Gold |
|---|---|
| `Bundesministerium für Inneres` | `Bundesministerium für Inneres` |

</details>

---

## `specific_cervenka_neunubel_telekom_ag`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Cervenka&Neunübel Telekom AG' which was missing from the rules.

**Content:**
```
\bCervenka&Neunübel\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 877 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_56`)

```
Der Beschwerdeführer war seit 21.4.1992 und auch noch in den streitgegenständlichen Jahren  als Monteur bei der Cervenka&Neunübel Telekom AG, unselbstständig erwerbstätig.
```

| Predicted | Gold |
|---|---|
| `Cervenka&Neunübel Telekom AG` | `Cervenka&Neunübel Telekom AG` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_80`)

```
Die  Feststellungen zur beruflichen Tätigkeit des Beschwerdeführers, zu den konkreten Einsatzorten  und zu den von seinem Arbeitgeber geleisteten Kostenersätzen gründen sich auf das Schreiben  der Cervenka&Neunübel Telekom AG  vom 9.6.2016 sowie die mit diesem Schreiben übermittelten Beilagen  („Dienstnehmerkalender“ und „Baustellenbesetzung“).
```

| Predicted | Gold |
|---|---|
| `Cervenka&Neunübel Telekom AG` | `Cervenka&Neunübel Telekom AG` |

</details>

---

## `specific_kriminalpolizei_oesterreich`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Kriminalpolizei in Österreich'.

**Content:**
```
\bKriminalpolizei\s+in\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_55`)

```
Die Kürzung betrifft wahrscheinlich die Dienstreisen im Zuge meiner  Tätigkeit bei der Kriminalpolizei in Österreich.
```

| Predicted | Gold |
|---|---|
| `Kriminalpolizei in Österreich` | `Kriminalpolizei in Österreich` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_67`)

```
Die Kürzung der Reisekosten um die Aufwendungen iZm dem Frontex-Einsatz seien nicht  gerechtfertigt, da diese Dienstreisen ausschließlich im Rahmen der Tätigkeit bei der  Kriminalpolizei in Österreich getätigt worden seien.
```

| Predicted | Gold |
|---|---|
| `Kriminalpolizei in Österreich` | `Kriminalpolizei in Österreich` |

</details>

---

## `specific_bm_fuer_inneres`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'BM für Inneres'.

**Content:**
```
\bBM\s+für\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 245 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_45`)

```
Auf den Lohnzettel des BM für Inneres wird verwiesen.
```

| Predicted | Gold |
|---|---|
| `BM für Inneres` | `BM für Inneres` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_51`)

```
Der Betrag, welcher vom BM für Inneres als Bezüge gem. § 26 EStG ausbezahlt wird, betrifft  den Kfz-Aufwand, die Miete der Wohnung und sonstigen Reisekosten, wie etwa Fahrkarten  usw., jedoch keine Tagesgelder.
```

| Predicted | Gold |
|---|---|
| `BM für Inneres` | `BM für Inneres` |

</details>

---

## `specific_hla_tourismus`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Höhere Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit' and its genitive form 'Höheren'.

**Content:**
```
\bHöher(?:e|en)\s+Lehranstalt\s+für\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_3`)

```
Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin bezog für die Tochter T., geb. 2003, wegen Schulbesuch (Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit in Krems) bis Juni 2022  Familienbeihilfe.
```

| Predicted | Gold |
|---|---|
| `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` | `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_34`)

```
Sachverhalt:  T. legte am 30.05.2022 die Reifeprüfung an der Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit ab und machte danach keine weitere Ausbildung.
```

| Predicted | Gold |
|---|---|
| `Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit` | `Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit` |

</details>

---

## `specific_england_org`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'England' as an organisation in this specific legal context (e.g., jurisdiction/entity reference).

**Content:**
```
\bEngland\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 669 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_17`)

```
Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.
```

| Predicted | Gold |
|---|---|
| `England` | `England` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_58`)

```
Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).
```

| Predicted | Gold |
|---|---|
| `England` | `England` |

</details>

---

## `specific_seneCura_laurentius_park_bludenz`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'SeneCura Laurentius Park Bludenz' with flexible whitespace.

**Content:**
```
\bSeneCura\s+Laurentius\s+Park\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1313 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_61`)

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Mutter der Bf war in den streitgegenständlichen Jahren im Pflegeheim SeneCura Laurentius  Park Bludenz (beginnend ab 28.01.2016) untergebracht.
```

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius  Park Bludenz` | `SeneCura Laurentius  Park Bludenz` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_80`)

```
2. Beweiswürdigung  Der Sachverhalt ist grundsätzlich unstrittig und ergibt sich als solcher aus dem Akt,  insbesondere den angeführten Aktenteilen wie den Bestätigungen der PVA, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.
```

| Predicted | Gold |
|---|---|
| `SeneCura  Laurentius Park Bludenz` | `SeneCura  Laurentius Park Bludenz` |

</details>

---

## `specific_bfg_genitive`

**F1:** 0.002 | **Precision:** 0.222 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'BFG´s' (genitive) and 'BFG,' (with comma) as complete entities to prevent partial matching.

**Content:**
```
\bBFG(?:\u00b4s|,)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.222 | 0.001 | 0.002 | 9 | 2 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 7 | 1727 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149768.1`) ( sent_id: `findok-manually-annotated_TRAIN/149768.1_18`)

```
Die Stellungnahme vom 10.03.2025 im Rahmen des Beschwerdeverfahrens vor dem  BFG, RV/5100109/2025, betreffend Einkommensteuer 2022 werde als Beweismittel im  Einkommensteuerverfahren 2023 vorgelegt.
```

| Predicted | Gold |
|---|---|
| `BFG,` | `BFG,` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149768.1`) ( sent_id: `findok-manually-annotated_TRAIN/149768.1_23`)

```
Die Stellungnahme vom 10.03.2025 im Rahmen des  Beschwerdeverfahrens vor dem BFG, RV/5100109/2025 (bis dato noch kein Erkenntnis),  betreffend Einkommensteuer 2022 werde als Beweismittel im Einkommensteuerverfahren  2023 vorgelegt.
```

| Predicted | Gold |
|---|---|
| `BFG,` | `BFG,` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_101`)

**False Positives:**

```
Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).
```

FP: `BFG,` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_101`)

**False Positives:**

```
Der nachfolgende abweisende Bescheid wurde bekämpft und schlussendlich entschied das  BFG, indem es die Beschwerde als unbegründet abwies (RV/2100724/2019).
```

FP: `BFG,` (organisation)

**✅ Gold Entities:**
- `BFG` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)

**False Positives:**

```
Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.
```

FP: `BFG,` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)
- `UFS` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_355`)

**False Positives:**

```
Damit war aber auch das Finanzamt Wien 1/23  gem. § 282 BAO verpflichtet, die Rechtsanschauung  des BFG´s umzusetzen (und zwar ungeachtet des Umstandes, dass sofort eine Amtsrevision  gegen das BFG-Erkenntnis eingebracht wurde).
```

FP: `BFG´s` (organisation)

**✅ Gold Entities:**
- `Finanzamt Wien 1/23` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_358`)

**False Positives:**

```
Erst der VwGH hat die unrichtige Rechtsansicht des BFG´s dahingehend in seinen Ausführungen  korrigiert, dass kein freies Wahlrecht in Bezug auf den innerbetrieblichen Verlustausgleich  existiert, sondern für den späteren Verlustvortrag der Folgejahre ausschließlich eine  objektbezogene Zuordnung maßgebend ist.
```

FP: `BFG´s` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_pensionsversicherungsanstalt`

**F1:** 0.002 | **Precision:** 0.154 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt'.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.154 | 0.001 | 0.002 | 13 | 2 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 11 | 1264 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_38`)

```
Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.
```

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)

```
Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.
```

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_41`)

**False Positives:**

```
Denn beide eine dauerhafte Erwerbsunfähigkeit bejahenden Gutachten beziehen sich  hinsichtlich der Frage des Eintritts der dauerhaften Erwerbsunfähigkeit auf ein von der Bf  vorgelegtes, von der Pensionsversicherungsanstalt in Auftrag gegebenes Gutachten vom 2. Juli  2021: Dieses stellt fest, dass der Bf „aufgrund der reduzierten psychomotorischen  Belastbarkeit und der geringen Stresstoleranz mit mehrfach gescheiterten Arbeitsversuchen  […] keine Tätigkeiten zumutbar [sind]“.
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_42`)

**False Positives:**

```
Eine sich auf das genannte Gutachten der  Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme vom 6. Juli 2021 hält  fest, dass „das Gesamtleistungskalkül […] für Tätigkeiten auf dem allgemeinen Arbeitsmarkt  vorübergehend mehr als 6 Monate nicht aus[reicht] ab Antragstellung 29.06.2021“.
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_45`)

**False Positives:**

```
Da das für die Pensionsversicherungsanstalt erstellte Gutachten festhält,  dass die Bf „seit ca. 2006 mit Unterbrechung bei Jugend am Werk“ tätig ist, geht die sich auf  das Gutachten der Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme  davon aus, dass die Bf seit 2006 originär invalid (iSd § 255 Abs. 7 ASVG) ist.
```

FP: `Pensionsversicherungsanstalt` (organisation)

```
Da das für die Pensionsversicherungsanstalt erstellte Gutachten festhält,  dass die Bf „seit ca. 2006 mit Unterbrechung bei Jugend am Werk“ tätig ist, geht die sich auf  das Gutachten der Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme  davon aus, dass die Bf seit 2006 originär invalid (iSd § 255 Abs. 7 ASVG) ist.
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_46`)

**False Positives:**

```
Vor dem  Hintergrund der Ausführungen des von der Pensionsversicherungsanstalt in Auftrag gegebenen  3 von 6 Seite 4 von 6
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_24`)

**False Positives:**

```
Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

</details>

---

## `specific_fa_braunau`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Braunau Ried Schärding'.

**Content:**
```
\bFinanzamt\s+Braunau\s+Ried\s+Sch\u00e4rding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 996 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde des Marion Voits, Kasparekgasse 1, 4981 Fraham, Österreich, vom 19. Oktober 2022 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 10. Oktober 2022 betreffend Pfändung einer Geldforderung 2022 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Braunau Ried Schärding` | `Finanzamt Braunau Ried Schärding` |

</details>

---

## `specific_fa_braunau_ried_schärding`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Braunau Ried Schärding'.

**Content:**
```
\bFA\s+Braunau\s+Ried\s+Sch\u00e4rding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 992 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_40`)

```
Am 11.11.2022  ging der gepfändete Betrag in Höhe von EUR 4.681,64 am Konto des FA Braunau Ried Schärding  ein und ist am  Abgabenkonto des Beschwerdeführers verbucht.
```

| Predicted | Gold |
|---|---|
| `FA Braunau Ried Schärding` | `FA Braunau Ried Schärding` |

</details>

---

## `specific_finanzamt_landeck_reutte`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Landeck Reutte' and its genitive form.

**Content:**
```
\bFinanzamt(?:es)?\s+Landeck\s+Reutte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 214 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Elmar Neimayer  in der Beschwerdesache Viola Siebenhühner, LLB,  Jokischberg 11, 3571 Maiersch, Österreich, über die Beschwerde vom 14. Dezember 2010 gegen die jeweils am   8. Oktober 2010 ausgefertigten Bescheide des Finanzamtes Landeck Reutte betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2006 bis 2008 (Steuernummer 063/3127 )zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Landeck Reutte` | `Finanzamtes Landeck Reutte` |

</details>

---

## `specific_finanzamt_waldviertel`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Waldviertel' specifically.

**Content:**
```
\bFinanzamt\s+Waldviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 177 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_78`)

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt    Vorausgegangenes Verfahren:  Am 4. Februar 2020 hatte das Finanzamt Waldviertel folgenden Bescheid an die Bf. erlassen:   Abweisungsbescheid   Ihr Antrag vom 16.9.2019 auf Familienbeihilfe wird abgewiesen für:   5 von 10 Seite 6 von 10
```

| Predicted | Gold |
|---|---|
| `Finanzamt Waldviertel` | `Finanzamt Waldviertel` |

</details>

---

## `specific_tritri_it`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Tritri-IT'.

**Content:**
```
\bTritri-IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1392 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_348`)

```
(Der Vollständigkeit halber  wird angemerkt, dass damals alle Beschwerden des Tritri-IT -Konzernes durch denselben  Richter beim BFG entschieden wurden).
```

| Predicted | Gold |
|---|---|
| `Tritri-IT` | `Tritri-IT` |

</details>

---

## `specific_mur_alver_og`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mur Alver OG' which was missing.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1570 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_26`)

```
keine Leistungsbeschreibung enthalte und nicht der Bf als Empfänger aufscheine und eine  Rechnung der „Mur Alver OG“ Leuchten aus dem Luxussegment anführe.
```

| Predicted | Gold |
|---|---|
| `Mur Alver OG` | `Mur Alver OG` |

</details>

---

## `specific_ams_osterreich`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'AMS Österreich'.

**Content:**
```
\bAMS\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1300 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_6`)

```
Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer vom AMS Österreich der Abgabenbehörde übermittelten korrigierten  Mitteilung nahm die Behörde das Verfahren betreffend Einkommensteuer 2019 gemäß § 303  Abs. 1 BAO wieder auf und erließ unter Berücksichtigung der nunmehr korrigierten  Arbeitslosengeldzahlung iHv 1.228,50 Euro für das Jahr 2019 einen neuen  Einkommensteuerbescheid 2019.
```

| Predicted | Gold |
|---|---|
| `AMS Österreich` | `AMS Österreich` |

</details>

---

## `specific_landespolizeidirketion_tirol`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirketion Tirol'.

**Content:**
```
\bLandespolizeidirketion\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 424 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149316.1`) ( sent_id: `findok-manually-annotated_TRAIN/149316.1_6`)

```
Mit Verständigungen gem. § 82 Abs. 9 KFG 1967 wurde durch die Landespolizeidirketion  Tirol an die Finanzpolizei mitgeteilt, dass im Zuge von Kontrollen festgestellt werden konnte,  dass die Beschwerdeführerin gemeinsam mit ihrem Ehemann und ebenso deren gemeinsame  1 von 7 Seite 2 von 7
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirketion  Tirol` | `Landespolizeidirketion  Tirol` |

</details>

---

## `specific_musikhochschule_wien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Musikhochschule Wien'.

**Content:**
```
\bMusikhochschule\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1160 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)

```
Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.
```

| Predicted | Gold |
|---|---|
| `Musikhochschule Wien` | `Musikhochschule Wien` |

</details>

---

## `specific_konservatorium_wien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Konservatorium der Stadt Wien'.

**Content:**
```
\bKonservatorium\s+der\s+Stadt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1160 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)

```
Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.
```

| Predicted | Gold |
|---|---|
| `Konservatorium  der Stadt Wien` | `Konservatorium  der Stadt Wien` |

</details>

---

## `specific_wiener_philharmoniker`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Wiener Philharmoniker'.

**Content:**
```
\bWiener\s+Philharmoniker\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1147 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_153`)

```
An der in diesen beiden Erkenntnis zum Ausdruck gebrachten Rechtsansicht hat der  Verwaltungsgerichtshof in seinem einen Berufsmusiker und Mitglied der Wiener  Philharmoniker betreffenden, Erkenntnis vom 21. September 2005, 2001/13/0241,  festgehalten und sie vertieft.
```

| Predicted | Gold |
|---|---|
| `Wiener  Philharmoniker` | `Wiener  Philharmoniker` |

</details>

---

## `specific_ufs_bfg`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'UFS/BFG' as a single entity.

**Content:**
```
\bUFS/BFG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 102 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_94`)

```
Obwohl sich im  weiteren Verfahren (beim UFS/BFG) herausstellte, dass dies sogenannte „Nichtbescheide“  waren, ist die Erlassung dieser Schriftstücke nach Rechtsansicht des BFG trotzdem als nach  außen gerichtete Amtshandlung zu werten.
```

| Predicted | Gold |
|---|---|
| `UFS/BFG` | `UFS/BFG` |

</details>

---

## `specific_how_to_spend_it`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'How to spend it Verlag GmbH'.

**Content:**
```
\bHow\s+to\s+spend\s+it\s+Verlag\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 100 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_134`)

```
*** „How to spend it Verlag GmbH u. Mitges.“: € 613,72  Beteiligung INET II: € -2.235,63 (aufgrund des rechtskräftigem BFG-Erkenntnisses  RV/7102483/2013 vom 27.5.2022 bzw. BP-Bericht vom 29.22.2010 (ABNr.: 121095/09) zur  St.nr.
```

| Predicted | Gold |
|---|---|
| `How to spend it Verlag GmbH` | `How to spend it Verlag GmbH` |

</details>

---

## `specific_garanta_versicherungsag`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Garanta VersicherungsAG'.

**Content:**
```
\bGaranta\s+VersicherungsAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 211 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_56`)

```
Dem Vorlageantrag beigelegt wurden eine Versicherungsbestätigung zur Mobilitätsgarantie  der Garanta VersicherungsAG (undatiert) für den Zeitraum 26.08.2011 bis 25.08.2012 für die  Beschwerdeführerin, eine Wartungsliste vom 26.08.2011 für das Auto der Beschwerdeführerin  und eine englische Bestätigung des The International Sivananda Yoga Vedanta Centre in  Canada vom 24.05.2003, in der die Beschwerdeführerin als Teacher of Yoga bezeichnet wird.
```

| Predicted | Gold |
|---|---|
| `Garanta VersicherungsAG` | `Garanta VersicherungsAG` |

</details>

---

## `specific_sivananda_yoga`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'The International Sivananda Yoga Vedanta Centre'.

**Content:**
```
\bThe\s+International\s+Sivananda\s+Yoga\s+Vedanta\s+Centre\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 211 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_56`)

```
Dem Vorlageantrag beigelegt wurden eine Versicherungsbestätigung zur Mobilitätsgarantie  der Garanta VersicherungsAG (undatiert) für den Zeitraum 26.08.2011 bis 25.08.2012 für die  Beschwerdeführerin, eine Wartungsliste vom 26.08.2011 für das Auto der Beschwerdeführerin  und eine englische Bestätigung des The International Sivananda Yoga Vedanta Centre in  Canada vom 24.05.2003, in der die Beschwerdeführerin als Teacher of Yoga bezeichnet wird.
```

| Predicted | Gold |
|---|---|
| `The International Sivananda Yoga Vedanta Centre` | `The International Sivananda Yoga Vedanta Centre` |

</details>

---

## `specific_da_deutsche_allgemeine`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'DA Deutsche Allgemeine Versicherung AG'.

**Content:**
```
\bDA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 202 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_113`)

```
Bis August 2006 hatte die  Beschwerdeführerin einen Audi A 3 (siehe Vorschreibung der Kraftfahrversicherung durch die  DA Deutsche Allgemeine Versicherung AG vom Jänner 2006).
```

| Predicted | Gold |
|---|---|
| `DA Deutsche Allgemeine Versicherung AG` | `DA Deutsche Allgemeine Versicherung AG` |

</details>

---

## `specific_geschenkartikel_gmbh`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Geschenkartikel GmbH'.

**Content:**
```
\bGeschenkartikel\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 200 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_211`)

```
Der Beschwerdeführerin wurde mit Vorhalt vom 13.11.2019 mitgeteilt, dass die dem BFG  vorliegenden Belegkopien nur teilweise lesbar sind und ein Nachweis an Aufwendungen für  Arbeitsmittel (ohne Massageliege) iHv € 1.213,81 vorliegt (Rechnung Geschenkartikel GmbH €  92,73;
```

| Predicted | Gold |
|---|---|
| `Geschenkartikel GmbH` | `Geschenkartikel GmbH` |

</details>

---

## `specific_aved_cosmetic`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'AVED cosmetic'.

**Content:**
```
\bAVED\s+cosmetic\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 196 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_223`)

```
Trotz Aufforderung des Finanzamtes zur Vorlage des Zahlungsnachweises und nochmaligen  Vorhalt durch das Bundesfinanzgericht wurde ein Zahlungsnachweis der Kosten der Firma  AVED cosmetic iHv € 975,48 nicht vorgelegt.
```

| Predicted | Gold |
|---|---|
| `AVED cosmetic` | `AVED cosmetic` |

</details>

---

## `specific_yoga_vidya_gmbh`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Yoga Vidya GmbH'.

**Content:**
```
\bYoga\s+Vidya\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 194 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/128676.1`) ( sent_id: `findok-manually-annotated_TRAIN/128676.1_230`)

```
Bei den Einzelanwendungen handelt es sich laut der vorgelegten Abrechnung vom 19.10.2006  von der Yoga Vidya GmbH um jeweils eine Anwendung Abhyanga, Garshan, kleine Abhyanga,  Shiro- und Mukabhyanga, Jambeera Pindas Sveda, Upanasveda mit Lepa und Padabhyanga.
```

| Predicted | Gold |
|---|---|
| `Yoga Vidya GmbH` | `Yoga Vidya GmbH` |

</details>

---

## `specific_magistrat_klagenfurt`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Klagenfurt' and its genitive form 'Magistrats der Stadt Klagenfurt'.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Klagenfurt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 271 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_69`)

```
Mit selbem Datum wurde das Magistrat der Stadt Klagenfurt  ersucht, den Bauakt die strittige Liegenschaft betreffend vorzulegen, welchem Ersuchen am  19.03.2024 nachgekommen wurde.
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Klagenfurt` | `Magistrat der Stadt Klagenfurt` |

</details>

---

## `specific_tschurtschenthaler_walder_fister`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH'.

**Content:**
```
\bTschurtschenthaler,\s+Walder,\s+Fister\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 276 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_2`)

```
Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Mag. Janosch Moehrle, Bakk. rer. nat., Neue Frauengasse 2, 3180 Hintereben, Österreich  vertreten durch Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH, Dr. Arthur Lemisch Platz 7, 9020 Klagenfurt, über die Beschwerde  vom 3. Juni 2022 gegen den Bescheid des Finanzamtes Österreich vom 4. Mai 2022 betreffend  Einkommensteuer 2020 (Steuernummer 71-848/5765) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH` | `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH` |

</details>

---

## `specific_immobilienbuero_mandl`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Immobilienbüro Mandl'.

**Content:**
```
\bImmobilienbüro\s+Mandl\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 273 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_58`)

```
Darüber hinaus seien die  vorliegenden Pläne keine amtlichen Pläne, sondern vom Immobilienbüro Mandl erstellte.
```

| Predicted | Gold |
|---|---|
| `Immobilienbüro Mandl` | `Immobilienbüro Mandl` |

</details>

---

## `specific_finanzamt_fur_grossbetriebe`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt für Großbetriebe'.

**Content:**
```
\bFinanzamt\s+für\s+Großbetriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1049 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)

```
Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

</details>

---

## `specific_finanzamt_wien_3_6_7_11_15_schwechat_gerasdorf`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf' and its genitive form 'Finanzamtes'.

**Content:**
```
\bFinanzamtes?\s+Wien\s+3/6/7/11/15\s+Schwechat\s+Gerasdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 882 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Alois Ahl  in der Beschwerdesache Romana van Straaten, MBA,  Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich, vertreten durch Dr. Anna Schlosser-Péter, Kurrentgasse 6/3, 1010  Wien, über die Beschwerden vom 23. März 2015 gegen die Bescheide des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich) vom 17. März 2015  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer  38-795/8528, zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf` | `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf` |

</details>

---

## `specific_easo`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'EASO'.

**Content:**
```
\bEASO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_62`)

```
Werbungskosten die in Zusammenhang mit Frontex, EASO, ... Einsätzen stehen, dürfen daher in  solchen Fällen nicht berücksichtigt werden.
```

| Predicted | Gold |
|---|---|
| `EASO` | `EASO` |

</details>

---

## `specific_european_frontex_genitive`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Europäischen Grenzschutzagentur Frontex' (genitive) and 'Europäische Grenzschutzagentur Frontex' (nominative).

**Content:**
```
\bEuropäisch(?:en)?\s+Grenzschutzagentur\s+Frontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 245 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_46`)

```
Für die Tätigkeit  bei der "Europäischen Grenzschutzagentur Frontex" wird eine Reisezulage in der Höhe von 98,--  Euro täglich gewährt.
```

| Predicted | Gold |
|---|---|
| `Europäischen Grenzschutzagentur Frontex` | `Europäischen Grenzschutzagentur Frontex` |

</details>

---

## `specific_hlf_krems`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'HLF Krems/Donau'.

**Content:**
```
\bHLF\s+Krems/Donau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_28`)

```
Die Bf. bringt im Vorlageantrag, eingelangt beim Finanzamt am 23.03.2023, vor, dass ihre  Tochter T. am 30.05.2022 an der HLF Krems/Donau maturiert habe und damit in die alte  2 von 6 Seite 3 von 6
```

| Predicted | Gold |
|---|---|
| `HLF Krems/Donau` | `HLF Krems/Donau` |

</details>

---

## `specific_hallas_partner_wirtschaftspruefung`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG' with flexible spacing.

**Content:**
```
\bHallas\s*&\s*Partner\s+Wirtschaftspr\u00fcfung\s+und\s+Steuerberatung\s+GmbH\s*&\s*Co\s*KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1214 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Ferdinand Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt  Österreich) vom 31. Oktober 2017 betreffend Festsetzung eines Verspätungszuschlages  betreffend Einkommensteuer 2015 und 2016 und Umsatzsteuer 2015 und 2016,  Steuernummer 86-167/7419  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` | `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` |

</details>

---

## `specific_bezirksgericht_purkersdorf`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht Purkersdorf'.

**Content:**
```
\bBezirksgericht\s+Purkersdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 672 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_11`)

```
ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.
```

| Predicted | Gold |
|---|---|
| `Bezirksgericht Purkersdorf` | `Bezirksgericht Purkersdorf` |

</details>

---

## `specific_grazer_treuhand_gmbh_partner_kg`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Grazer Treuhand Steuerberatung GmbH & Partner KG'.

**Content:**
```
\bGrazer\s+Treuhand\s+Steuerberatung\s+GmbH\s+&\s+Partner\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 438 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_1`)

```
IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Maximilian Karrer  in der Beschwerdesache VetR Tosca Buecher,  Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich, vertreten durch Grazer Treuhand Steuerberatung GmbH & Partner KG,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 gegen den Bescheid des  Finanzamts Graz-Stadt vom 12.10.2016 betreffend Abweisung des Antrages gemäß § 299 BAO  vom 9.7.2015 auf Aufhebung des Einkommensteuerbescheides 2014 des Finanzamts Graz- Stadt vom 20.5.2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Grazer Treuhand Steuerberatung GmbH & Partner KG` | `Grazer Treuhand Steuerberatung GmbH & Partner KG` |

</details>

---

## `specific_finanzamts_graz_stadt`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Finanzamts Graz-Stadt' and 'Finanzamts Graz- Stadt' (genitive with space).

**Content:**
```
\bFinanzamts\s+Graz\-?\s+Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 438 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_1`)

```
IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Maximilian Karrer  in der Beschwerdesache VetR Tosca Buecher,  Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich, vertreten durch Grazer Treuhand Steuerberatung GmbH & Partner KG,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 gegen den Bescheid des  Finanzamts Graz-Stadt vom 12.10.2016 betreffend Abweisung des Antrages gemäß § 299 BAO  vom 9.7.2015 auf Aufhebung des Einkommensteuerbescheides 2014 des Finanzamts Graz- Stadt vom 20.5.2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamts Graz- Stadt` | `Finanzamts Graz- Stadt` |

</details>

---

## `specific_ufs_salzburg`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'UFS Salzburg' specifically to prevent partial matching of 'UFS'.

**Content:**
```
\bUFS\s+Salzburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 16 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_98`)

```
Gegenteiliges ergibt sich auch nicht aus der von der  belangten Behörde in diesem Zusammenhang ins Treffen geführten Entscheidung des UFS  Salzburg vom 20.8.2013, RV/0389-S/13 (dort hatte der Berufungswerber die Verbuchung einer  von ihm auf Grund einer noch anhängigen VwGH-Beschwerde erwarteten Gutschrift, also  tatsächlich die Verbuchung einer zukünftigen Gutschrift beantragt).
```

| Predicted | Gold |
|---|---|
| `UFS  Salzburg` | `UFS  Salzburg` |

</details>

---

## `specific_verwaltungsgericht_wien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgericht Wien'.

**Content:**
```
\bVerwaltungsgericht\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 440 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_15`)

```
Die Verfügungen mit den Zahlen   MA67/GZ/2024 vom 31.03.2025 und   MA67/GZ-2/2024 vom 02.04.2025  jedoch sind nicht berechtigt, daher erhebe ich hiermit das Rechtsmittel der Beschwerde an das  Verwaltungsgericht Wien.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

</details>

---

## `specific_steuerberater_metzler`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Steuerberater Metzler & Adelsberger OG'.

**Content:**
```
\bSteuerberater\s+Metzler\s+&\s+Adelsberger\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1574 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.
```

| Predicted | Gold |
|---|---|
| `Steuerberater Metzler & Adelsberger OG` | `Steuerberater Metzler & Adelsberger OG` |

</details>

---

## `specific_finanzamt_innsbruck`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Innsbruck' and its genitive form 'Finanzamtes Innsbruck'.

**Content:**
```
\bFinanzamtes?\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1574 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.
```

| Predicted | Gold |
|---|---|
| `Finanzamtes  Innsbruck` | `Finanzamtes  Innsbruck` |

</details>

---

## `specific_ikea`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Ikea' as an organisation.

**Content:**
```
\bIkea\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |

</details>

---

## `specific_obi`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Obi' as an organisation.

**Content:**
```
\bObi\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Obi` | `Obi` |

</details>

---

## `specific_leiner`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Leiner' as an organisation.

**Content:**
```
\bLeiner\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Leiner` | `Leiner` |

</details>

---

## `specific_möbelix`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Möbelix' as an organisation.

**Content:**
```
\bMöbelix\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Möbelix` | `Möbelix` |

</details>

---

## `specific_mömax`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'MömaX' as an organisation.

**Content:**
```
\bMömaX\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `MömaX` | `MömaX` |

</details>

---

## `specific_ottode`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Otto.de' as an organisation.

**Content:**
```
\bOtto\.de\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Otto.de` | `Otto.de` |

</details>

---

## `specific_xxxlutz`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'xxxLutz' as an organisation.

**Content:**
```
\bxxxLutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `xxxLutz` | `xxxLutz` |

</details>

---

## `specific_quelleat`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Quelle.at' as an organisation.

**Content:**
```
\bQuelle\.at\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1569 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)

```
Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Quelle.at` | `Quelle.at` |

</details>

---

## `specific_krankenpflegevereins_bludenz`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Krankenpflegevereins Bludenz' (genitive) and 'Krankenpflegeverein Bludenz' with flexible whitespace.

**Content:**
```
\bKrankenpflegeverein(?:s)?\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1304 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_88`)

```
Die Kosten lt Bestätigungen des Krankenpflegevereins  Bludenz (welche auch mittels Kontoauszüge nachgewiesen wurden) iHv 625,54 Euro (für 2016),  485,50 Euro (für 2017) und 457,25 Euro (für 2018) sind somit zwangsläufig erwachsen und  werden daher als außergewöhnliche Belastung mit Selbstbehalt anerkannt.
```

| Predicted | Gold |
|---|---|
| `Krankenpflegevereins  Bludenz` | `Krankenpflegevereins  Bludenz` |

</details>

---

## `specific_innmarine_gmbh`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'InnMarine GMBH'.

**Content:**
```
\bInnMarine\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1224 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_3`)

```
Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid von 3. Oktober 2018 wurde der Beschwerdeführer gemäß § 9a BAO für die  aushaftenden Abgabenschulden der InnMarine GMBH (Primärschuldnerin) im Ausmaß von  € 99.885,72 in Anspruch genommen.
```

| Predicted | Gold |
|---|---|
| `InnMarine GMBH` | `InnMarine GMBH` |

</details>

---

## `specific_lenfeld_leys_sonderegger`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lenfeld/Leys/Sonderegger Rechtsanwälte'.

**Content:**
```
\bLenfeld/Leys/Sonderegger\s+Rechtsanwälte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 65 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1_1`)

```
IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ashley Ditges  in der Beschwerdesache Willibald Urbanowicz,  Caritasstraße 286, 3920 Heinreichs, Österreich, vertreten durch Lenfeld/Leys/Sonderegger Rechtsanwälte, Malserstraße 19,  6500 Landeck, über die Beschwerde vom 14. Dezember 2023 gegen den Bescheid des  Finanzamtes Österreich vom 14. November 2023 betreffend Rückforderung von  Familienbeihilfe und Kinderabsetzbeträgen für die Monate Oktober 2021 bis Jänner 2022,  Steuernummer 83-447/1877,  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Lenfeld/Leys/Sonderegger Rechtsanwälte` | `Lenfeld/Leys/Sonderegger Rechtsanwälte` |

</details>

---

## `specific_universitaet_innsbruck`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Universität Innsbruck'.

**Content:**
```
\bUniversität\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 63 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149462.1_29`)

```
Nach dem Studienblatt der Universität Innsbruck inskribierte der Sohn im Wintersemester  2019/20 im Diplomstudium Rechtswissenschaften.
```

| Predicted | Gold |
|---|---|
| `Universität Innsbruck` | `Universität Innsbruck` |

</details>

---

## `specific_bundesministerin_fuer_finanzen`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerin für Finanzen' (feminine form).

**Content:**
```
\bBundesministerin\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1100 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_74`)

```
Gemäß § 4 Abs 1 Verordnung der Bundesministerin für Finanzen über die Kriterien zur  Ermittlung des Pendlerpauschales und des Pendlereuros, zur Einrichtung eines  Pendlerrechners und zum Vorliegen eines Familienwohnsitzes (Pendlerverordnung), BGBl II  2013/276 idF BGBl II 2022/275 liegt ein Familienwohnsitz (§ 16 Abs 1 Z 6 lit f und § 20 Abs 1 Z 2  lit e EStG 1988) „dort, wo  1.
```

| Predicted | Gold |
|---|---|
| `Bundesministerin für Finanzen` | `Bundesministerin für Finanzen` |

</details>

---

## `specific_bdo_austria_gmbh_wp_u_stbges`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BDO Austria GmbH WP- u. StBges.'

**Content:**
```
\bBDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1546 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,
```

| Predicted | Gold |
|---|---|
| `BDO Austria GmbH WP- u. StBges.` | `BDO Austria GmbH WP- u. StBges.` |

</details>

---

## `specific_leitnerleitner_gmbh_wirtschaftspruefer_und_steuerberater`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater'

**Content:**
```
\bLeitnerLeitner\s+GmbH\s+Wirtschaftspr\u00fcfer\s+und\s+Steuerberater
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1546 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,
```

| Predicted | Gold |
|---|---|
| `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` | `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` |

</details>

---

## `specific_betriebspruefung_gmbh`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Betriebsprüfung GmbH'.

**Content:**
```
\bBetriebsprüfung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1415 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_229`)

```
Nach Ansicht der Betriebsprüfung GmbH das Finanzamt müsse der gesamte im Jahr 2007  erwirtschaftete Verlust der Houdek Maschinenbau  ermittelt und aufgrund der Abspaltung von 11  Tankstellen aliquot zwischen der Houdek Maschinenbau  und der Schmeltz Luftfahrt  aufgeteilt werden,  wodurch sich nicht nur eine Änderung des steuerlichen Ergebnisses 2007 ergäbe, sondern auch  eine Anpassung der Verlustvorträge und der in Folgejahren vorgenommenen  Verlustverwertung erfolgen müsse.
```

| Predicted | Gold |
|---|---|
| `Betriebsprüfung GmbH` | `Betriebsprüfung GmbH` |

</details>

---

## `specific_x_gmbh_hyphen`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'X-GmbH' (hyphenated) which was missing from the rules.

**Content:**
```
\bX-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1399 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_268`)

```
Übersehen werden dabei insbesondere die Ausführungen des VwGH in Rz 25: „Eine andere  Frage ist es, von wem dieser Jahresverlust - in Anbetracht der zum Ablauf des 31. Dezember  2007 vorgenommenen Spaltung des X-GmbH - in den Folgejahren [Herv d Verf] als  Verlustvortrag iSd § 8 Abs 4 KStG 1988 geltend gemacht werden kann."
```

| Predicted | Gold |
|---|---|
| `X-GmbH` | `X-GmbH` |

</details>

---

## `specific_ams`

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'AMS' (Arbeitsmarktservice).

**Content:**
```
\bAMS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 1300 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_27`)

```
Ebenso sei ihm aufgrund dieser Behinderung eine Umschulung von einem Art Beruf auf neuer  Beruf vom AMS finanziert worden.
```

| Predicted | Gold |
|---|---|
| `AMS` | `AMS` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_6`)

**False Positives:**

```
Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer vom AMS Österreich der Abgabenbehörde übermittelten korrigierten  Mitteilung nahm die Behörde das Verfahren betreffend Einkommensteuer 2019 gemäß § 303  Abs. 1 BAO wieder auf und erließ unter Berücksichtigung der nunmehr korrigierten  Arbeitslosengeldzahlung iHv 1.228,50 Euro für das Jahr 2019 einen neuen  Einkommensteuerbescheid 2019.
```

FP: `AMS` (organisation)

**✅ Gold Entities:**
- `AMS Österreich` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_11`)

**False Positives:**

```
II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. erhielt für das Jahr 2019 folgende Zahlungen vom Arbeitsmarktservice (AMS):  Am 18.03.2019 308,35 Euro für den Zeitraum 14.01.
```

FP: `AMS` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Arbeitsmarktservice (AMS)` (organisation)

</details>

---

## `specific_bfh`

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BFH' (Bundesfinanzgericht in Germany).

**Content:**
```
\bBFH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 1204 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_64`)

```
Zur Frage der Ordnungsmäßigkeit des Fahrtenbuches sei auf die Rechtsprechung  des deutschen BFH zu verweisen, die auch für die österreichische Rechtslage relevant sei.
```

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_43`)

**False Positives:**

```
BFH, BStBl 1997 II 642;
```

FP: `BFH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_49`)

**False Positives:**

```
BFH, BStBl 1997 II 642;
```

FP: `BFH` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_amtes_fuer_betrugsbekampfung`

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmtes?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 1258 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_22`)

```
Die belangte Behörde verweigere die Buchung der UVAs und NOVA- Meldungen mit dem Hinweis, dass man auf eine Aussage des Amtes für Betrugsbekämpfung  (ABB) warte.
```

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)

**False Positives:**

```
Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22
```

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)

**False Positives:**

```
Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22
```

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

</details>

---

## `specific_bundesministers_fuer_finanzen`

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Finanzen' (genitive) and 'Bundesminister für Finanzen' (nominative).

**Content:**
```
\bBundesminister(?:s)?\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 1100 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149801.1`) ( sent_id: `findok-manually-annotated_TRAIN/149801.1_6`)

```
Darüber hinaus begehrte er den Freibetrag für Behinderung (§ 35 Abs 3 EStG) und den  pauschalen Freibetrag wegen Unzumutbarkeit der Benützung öffentlicher Verkehrsmittel nach  § 3 Abs 1 Verordnung des Bundesministers für Finanzen über außergewöhnliche Belastungen  (hinfort: § 3 Abs 1 VO).
```

| Predicted | Gold |
|---|---|
| `Bundesministers für Finanzen` | `Bundesministers für Finanzen` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_73`)

**False Positives:**

```
Der Bundesminister für Finanzen wird ermächtigt, Kriterien zur Festlegung der Entfernung  und der Zumutbarkeit der Benützung eines Massenverkehrsmittels mit Verordnung festzulegen.
```

FP: `Bundesminister für Finanzen` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) ( sent_id: `findok-manually-annotated_TRAIN/148648.1_103`)

**False Positives:**

```
Der Bundesminister für Finanzen wird ermächtigt, Kriterien zur Festlegung der  Entfernung und der Zumutbarkeit der Benützung eines Massenverkehrsmittels mit  Verordnung festzulegen.
```

FP: `Bundesminister für Finanzen` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_oecd`

**F1:** 0.001 | **Precision:** 0.200 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'OECD'.

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.200 | 0.001 | 0.001 | 5 | 1 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 4 | 939 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_94`)

```
Die Zentralstelle kann den Beamten mit seiner Zustimmung  1. zu Ausbildungszwecken oder als Nationalen Experten zu einer Einrichtung, die im Rahmen  der europäischen Integration oder der OECD tätig ist, oder  2.
```

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_107`)

**False Positives:**

```
Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].
```

FP: `OECD` (organisation)

```
Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].
```

FP: `OECD` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_107`)

**False Positives:**

```
Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].
```

FP: `OECD` (organisation)

```
Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].
```

FP: `OECD` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

</details>

---

## `specific_vfgh`

**F1:** 0.001 | **Precision:** 0.026 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VfGH' (Verfassungsgerichtshof) but excludes citation contexts like '(VfGH ...'.

**Content:**
```
\bVfGH\b(?!\s*\()
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.026 | 0.001 | 0.001 | 39 | 1 | 38 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 38 | 1439 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_32`)

```
Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.
```

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**

```
Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_157`)

**False Positives:**

```
Der VfGH hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_159`)

**False Positives:**

```
Dem genannten VfGH-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung aus dem Jahr 1984 gab die zuständige FLD der Berufung einer  Gesellschafterin gegen die einheitliche und gesonderte Gewinnfeststellung in der Form statt,  dass die im Erstbescheid bei der Gesellschafterin zur Gänze als Gewinnanteil behandelte  Ablösezahlung mit 2/3 zu aktivieren und auf 6 Jahre verteilt abzuschreiben war.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_162`)

**False Positives:**

```
Der VfGH bejahte die Anwendbarkeit des Vorfragentatbestandes.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**

```
Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_company_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Pastl+Bächle Handel' which contains a plus sign and lacks a standard suffix.

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

## `specific_textil_steingartlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Textil Steingartlog'.

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

## `specific_bauermeister_getränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bauermeister Getränke'.

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

## `specific_sophie_wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sophie Wittmeir'.

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

## `specific_starker_beratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Starker Beratung'.

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

## `specific_ugqq_verlag_og`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'UGQQ Verlag OG'.

**Content:**
```
\bUGQQ\s+Verlag\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_tal_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Tal-Druck'.

**Content:**
```
\bTal-Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_nord_trinex_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Nord Trinex GMBH'.

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

## `specific_trafenfen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Trafenfen Automotive' which lacks a standard suffix.

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

## `specific_oppert_elektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Oppert Elektro'.

**Content:**
```
\bOppert\s+Elektro\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_hagdorn_robotik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hagdorn Robotik'.

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

## `specific_planung_monuniost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Planung Monuniost'.

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

## `specific_raiffeisenbank_stallhofen`

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

## `specific_nordevent_gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'NordEvent Gruppe'.

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

## `specific_bezirksgericht_zell`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirksgericht Zell am See'.

**Content:**
```
\bBezirksgericht\s+Zell\s+am\s+See\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_donau_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Donau-Druck'.

**Content:**
```
\bDonau-Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_greiner_mai_event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Greiner-Mai Event'.

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

## `specific_waldtra_sicherheit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Waldtra-Sicherheit'.

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

## `specific_mur_ververzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mur Ververzor Betriebe' which lacks a standard corporate suffix.

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

## `specific_wod_sicherheit_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'WOD Sicherheit KG'.

**Content:**
```
\bWOD\s+Sicherheit\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_zumholte_verlag_og`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Zumholte Verlag OG'.

**Content:**
```
\bZumholte\s+Verlag\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_strohsack_und_dresbeimdieke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Strohsack und Dresbeimdieke Versand'.

**Content:**
```
\bStrohsack\s+und\s+Dresbeimdieke\s+Versand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_kudla_kuehnel_solar`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Kudla&Kühnel Solar'.

**Content:**
```
\bKudla&Kühnel\s+Solar\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamt_salzburg_land`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Salzburg-Land'.

**Content:**
```
\bFinanzamt\s+Salzburg-Land\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_norkel_software_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Norkel-Software GMBH'.

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

## `specific_rpxf_immobilien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'RPXF Immobilien'.

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

## `specific_finanzamt_klagenfurt_sv_w`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Klagenfurt St. Veit Wolfsberg'.

**Content:**
```
\bFinanzamt\s+Klagenfurt\s+St\.\s+Veit\s+Wolfsberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_mauriczat_medien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mauriczat Medien' which lacks a standard corporate suffix.

**Content:**
```
\bMauriczat\s+Medien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_sudevent_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'SüdEvent AG'.

**Content:**
```
\bS\u00fcdEvent\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_zyjy_automotive_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'ZYJY Automotive AG'.

**Content:**
```
\bZYJY\s+Automotive\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_nyj_event_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'NYJ Event AG'.

**Content:**
```
\bNYJ\s+Event\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_kubzyk_elektro_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Kubzyk Elektro AG'.

**Content:**
```
\bKubzyk\s+Elektro\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_baden_modling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Baden Mödling'.

**Content:**
```
\bFA\s+Baden\s+M\u00f6dling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_schwechat_gerasdorf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Schwechat Gerasdorf'.

**Content:**
```
\bFA\s+Schwechat\s+Gerasdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_wien_2_20_21_22`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Wien 2/20/21/22'.

**Content:**
```
\bFA\s+Wien\s+2/20/21/22\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_freistadt_urbahr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Freistadt Rohrbach Urfahr'.

**Content:**
```
\bFA\s+Freistadt\s+Rohrbach\s+Urfahr\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_valbruckzor_energie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Valbruckzor-Energie'.

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

## `specific_technik_ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Technik Ostbachal'.

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

## `specific_fa_deutschlandsberg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Deutschlandsberg Leibnitz Voitsberg'.

**Content:**
```
\bFA\s+Deutschlandsberg\s+Leibnitz\s+Voitsberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_salzburg_stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Salzburg-Stadt' and 'www.FA Salzburg-Stadt'.

**Content:**
```
(?:www\.)?FA\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_klusner_paffgen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Klusner&Päffgen Bildung GMBH'.

**Content:**
```
\bKlusner\&P\u00e4ffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_tschermack_pharma`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Tschermack Pharma GMBH'.

**Content:**
```
\bTschermack\s+Pharma\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_rosilius_pflege`

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

## `specific_yavasoglu_analyse`

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

## `specific_finanzamt_gmunden_vocklabruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Gmunden Vöcklabruck'.

**Content:**
```
\bFinanzamt\s+Gmunden\s+V\u00f6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_ruterborries_fridrich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Rüterborries+Friderich Möbel' which contains a plus sign and lacks a standard corporate suffix.

**Content:**
```
\bR\u00fcterborries\+Friderich\s+M\u00f6bel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_dgcv_ecommerce`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'DGCV E-Commerce GMBH' handling the em-dash or hyphen.

**Content:**
```
\bDGCV\s+E[\u2013\u2014\-]Commerce\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_nkah_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'NKAH Luftfahrt Vertrieb' which lacks a standard corporate suffix.

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

## `specific_unter_donunisee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Unter Donunisee AG' to ensure exact match and prevent context capture.

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

## `specific_lognex_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lognex-IT AG'.

**Content:**
```
\bLognex\-IT\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_sudgarten_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'SüdGarten GMBH'.

**Content:**
```
\bS\u00fcdGarten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_wien_waldnor_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wien Waldnor KG'.

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

## `specific_naass_elektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Naaß Elektro GMBH'.

**Content:**
```
\bNaaß\s+Elektro\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bersud_möbel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bersud Möbel GMBH'.

**Content:**
```
\bBersud\s+Möbel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_unter_heimdorf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Unter Heimdorf GMBH'.

**Content:**
```
\bUnter\s+Heimdorf\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_yxtg_maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'YXTG Maschinenbau'.

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

## `specific_mittel_logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mittel-Logistik'.

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

## `specific_alessi_event_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Alessi Event GMBH'.

**Content:**
```
\bAlessi\s+Event\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bludszat_maschinenbau_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bludszat Maschinenbau GMBH'.

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

## `specific_stadt_logglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Stadt Logglanz'.

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

## `specific_finanzamt_judenburg_liezen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Judenburg Liezen'.

**Content:**
```
\bFinanzamt\s+Judenburg\s+Liezen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamt_oststeiermark`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Oststeiermark'.

**Content:**
```
\bFinanzamt\s+Oststeiermark\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fabruck_eisenstadt_oberwart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Bruck Eisenstadt Oberwart'.

**Content:**
```
\bFA\s+Bruck\s+Eisenstadt\s+Oberwart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_amstetten_melk_scheibbs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Amstetten Melk Scheibbs'.

**Content:**
```
\bFA\s+Amstetten\s+Melk\s+Scheibbs\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_dias_telekom_institut`

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

## `specific_rheindigital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'RheinDigital'.

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

## `specific_zoruniglanz`

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

## `specific_chen_setzekorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Chen Setzekorn'.

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

## `specific_conwil_marine`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Conwil-Marine'.

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

## `specific_paweltschik_telekom`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Paweltschik Telekom GMBH'.

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

## `specific_basdas_pharma`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Basdas Pharma AG'.

**Content:**
```
\bBasdas\s+Pharma\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamt_tirol_ost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Tirol Ost'.

**Content:**
```
\bFinanzamt\s+Tirol\s+Ost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_tirol_ost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Tirol Ost'.

**Content:**
```
\bFA\s+Tirol\s+Ost\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bezirksgericht_silz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirksgericht Silz'.

**Content:**
```
\bBezirksgericht\s+Silz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_lg_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'LG Innsbruck'.

**Content:**
```
\bLG\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_landesgericht_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Landesgericht Innsbruck'.

**Content:**
```
\bLandesgericht\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_west_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'West-Luftfahrt'.

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

## `specific_annemie_bott`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_stadte_energie_holding`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_milan_haendlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Milan Händlein'.

**Content:**
```
\bMilan\s+Händlein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_manfredo_herrschmann`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Manfredo Herrschmann'.

**Content:**
```
\bManfredo\s+Herrschmann\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_krolitzki_beratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Krolitzki Beratung'.

**Content:**
```
\bKrolitzki\s+Beratung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_gronemeier_hovelberndt_ecommerce`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Grönemeier&Hövelberndt E‑Commerce' handling the em-dash.

**Content:**
```
\bGr\u00f6nemeier\&H\u00f6velberndt\s+E[\u2013\u2014\-]Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_keltrizor_handel_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Keltrizor Handel KG' which was missing.

**Content:**
```
\bKeltrizor\s+Handel\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_volkbank_wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'VOLKSBANK WIEN' which was missing.

**Content:**
```
\bVOLKSBANK\s+WIEN\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_elender_cloud`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Elender Cloud' which was missing.

**Content:**
```
\bElender\s+Cloud\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_sünramm_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sünramm Druck' which was missing.

**Content:**
```
\bSünramm\s+Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_süd_sudwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Süd Sudwil' which was missing.

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

## `specific_südversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SüdVersand' which was missing.

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

## `specific_gäbelt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gäbelt' as an organisation in this context (party name).

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

## `specific_steinfurtglanz_landwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Steinfurtglanz-Landwirtschaft'.

**Content:**
```
\bSteinfurtglanz-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_ennsbildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'EnnsBildung'.

**Content:**
```
\bEnnsBildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_ostwilnexlogistik_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'OstWilnexLogistik AG'.

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

## `specific_mur_donwerk_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mur Donwerk GMBH'.

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

## `specific_dlcg_bildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'DLCG Bildung'.

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

## `specific_bahrdt_digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bahrdt Digital'.

**Content:**
```
\bBahrdt\s+Digital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_wildorftra_ki_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wildorftra KI GMBH'.

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

## `specificbruckmonwil_digital_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bruckmonwil Digital GMBH'.

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

## `specific_sud_nortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Süd Nortri' specifically.

**Content:**
```
\bS\u00fcd\s+Nortri\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_hulsebusch_breithaupt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hülsebusch + Breithaupt Versicherung' specifically.

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

## `specific_logal_gruppe`

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

## `specific_enns_werkal_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Enns Werkal GMBH' specifically.

**Content:**
```
\bEnns\s+Werkal\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_lexkel_vertrieb_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lexkel Vertrieb KG' and 'Lexkel Vertrieb KG.'

**Content:**
```
\bLexkel\s+Vertrieb\s+KG(?:\.)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_kornfelder_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kornfelder Recycling'

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

## `specific_fuchsl_touristik_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Füchsl Touristik GMBH'

**Content:**
```
\bF\u00fchsl\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_magerlein_logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mägerlein Logistik'

**Content:**
```
\bM\u00e4gerlein\s+Logistik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_dongartcon_landwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Dongartcon-Landwirtschaft GMBH'.

**Content:**
```
\bDongartcon\-Landwirtschaft\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bezirksgericht_neunkirchen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirksgericht Neunkirchen'.

**Content:**
```
\bBezirksgericht\s+Neunkirchen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_traun_aluni_institut`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Traun Aluni Institut GMBH'.

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

## `specific_monlogtri_analyse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Monlogtri-Analyse GMBH'.

**Content:**
```
\bMonlogtri\-Analyse\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_unter_gartglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Unter Gartglanz GMBH'.

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

## `specific_fa_niederosterreich_mitte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'FA Niederösterreich Mitte'.

**Content:**
```
\bFA\s+Niederösterreich\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamt_niederosterreich_mitte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Niederösterreich Mitte'.

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

## `specific_finanzamt_baden_modling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Baden Mödling'.

**Content:**
```
\bFinanzamt\s+Baden\s+Mödling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_blazickova_hepprich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Blazickova & Hepprich Energie AG'.

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

## `specific_mittelheizung_werke_ag`

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

## `specific_traun_digital_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Traun-Digital KG'.

**Content:**
```
\bTraun\-Digital\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_mertznich_bau_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mertznich Bau GMBH'.

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

## `specific_gernot_hirschkorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Gernot Hirschkorn' (treated as organisation in this context).

**Content:**
```
\bGernot\s+Hirschkorn\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_hinklein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hinklein' which is a party name treated as an organisation.

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

## `specific_fa_linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Linz'.

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

## `specific_huberswoboda`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH'.

**Content:**
```
\bHuber\s+Swoboda\s+Oswald\s+Aixberger\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_unterrecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'UnterRecycling Services GMBH'.

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

## `specific_osterreichische_gesellschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Österreichische Gesellschaft für Europapolitik'.

**Content:**
```
\bÖsterreichische\s+Gesellschaft\s+für\s+Europapolitik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bm_fuer_finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BM für Finanzen'.

**Content:**
```
\bBM\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_obufug_rule`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific long entity '"ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH - Wirtschaftsprüfungs- und Steuerberatungsgesellschaft'.

**Content:**
```
\b"ÖBUG"\s+DR\.\s+NIKOLAUS\s+Wirtschaftstreuhand\s+GmbH\s*-\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bks_steuerberatung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BKS Steuerberatung GmbH & Co KG'.

**Content:**
```
\bBKS\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fachhochschule_karnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fachhochschule Kärnten'.

**Content:**
```
\bFachhochschule\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fh_karnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FH Kärnten'.

**Content:**
```
\bFH\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_sozialversicherung_bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherungsanstalt der Bauern' and 'Sozialversicherung der Bauern'.

**Content:**
```
\bSozialversicherung(?:sanstalt)?\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 695 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_200`)

**False Positives:**

```
Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.
```

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated_TRAIN/149834.1_200`)

**False Positives:**

```
Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.
```

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

</details>

---

## `specific_bmf_arbeit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz'.

**Content:**
```
\bBundesministers\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_imre_schaffer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Imre & Schaffer Rechtsanwälte OG'.

**Content:**
```
\bImre\s+&\s+Schaffer\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_steiermark_mitte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Steiermark Mitte' and 'Finanzamt Steiermark Mitte'.

**Content:**
```
\b(?:FA|Finanzamt)\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_vorarlberg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Vorarlberg'.

**Content:**
```
\bFA\s+Vorarlberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_landeck_reutte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Landeck Reutte'.

**Content:**
```
\bFA\s+Landeck\s+Reutte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_oststeiermark`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Oststeiermark'.

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

## `specific_finanzamt_salzburg_stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt'.

**Content:**
```
\bFinanzamt\s+Salzburg-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamtbruck_eisenstadt_oberwart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Bruck Eisenstadt Oberwart'.

**Content:**
```
\bFinanzamt\s+Bruck\s+Eisenstadt\s+Oberwart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_company_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches generic company patterns like 'Name Industry KG' including Steuerberatung.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*)\s+(Handel|Versand|Dienstleistung|Technik|Elektro|Möbel|Maschinenbau|Software|Digital|Logistik|Immobilien|Versicherung|Pharma|Medien|Verlag|Institut|Bau|Touristik|Recycling|Energie|Cloud|Analyse|Transport|Service|Produktion|Entwicklung|Planung|Konstruktion|Fertigung|Herstellung|Vertrieb|Marketing|Consulting|Engineering|Architecture|Design|Construction|Management|Finance|Accounting|Legal|Tax|Audit|Insurance|Banking|Investment|Real\s+Estate|Property|Development|Holding|Group|Corp|Inc|Ltd|AG|KG|GmbH|UG|OHG|GbR|PartG|WEG|Steuerberatung)\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzen_tradonnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzen Tradonnex' which was missing from the rules.

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

## `specific_norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Norconheim' which was missing from the rules.

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

## `specific_lg_zrs_wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'LG für ZRS Wien'.

**Content:**
```
\bLG\s+für\s+ZRS\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bundesministeriums_fuer_justiz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Justiz' (genitive) and 'Bundesministerium für Justiz' (nominative).

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Justiz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_karl_franzens_universitat_graz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Karl-Franzens- Universität Graz' and variants with or without space after hyphen.

**Content:**
```
\bKarl-Franzens-?\s*Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamt_klosterneuburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Klosterneuburg' and its genitive form 'Finanzamtes Klosterneuburg'.

**Content:**
```
\bFinanzamtes?\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_kings_school_worcester`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'King's School Worcester' explicitly to cover the full name variant.

**Content:**
```
\bKing['\u00b4]\s+School\s+Worcester\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_fa_kirchdorf_perg_steyr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Kirchdorf Perg Steyr' in addition to 'Finanzamt Kirchdorf Perg Steyr'.

**Content:**
```
\b(?:FA|Finanzamt)\s+Kirchdorf\s+Perg\s+Steyr\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamt_osterreich_dst12`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich (DST12)'.

**Content:**
```
\bFinanzamt\s+Österreich\s*\(DST12\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_saxinger_chalupsky`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Saxinger Chalupsky & Partner Rechtsanwälte GmbH'.

**Content:**
```
\bSaxinger\s+Chalupsky\s+&\s+Partner\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_mittel_unisyn_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mittel Unisyn GMBH'.

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

## `specific_ober_lemostnor_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Ober Lemostnor AG'.

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

## `specific_vennes_recycling_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Vennes Recycling AG'.

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

## `specific_baers_walterscheidt_handel_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bärs & Walterscheidt Handel GMBH'.

**Content:**
```
\bBärs\s+&\s+Walterscheidt\s+Handel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_b_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'B-GmbH'.

**Content:**
```
\bB-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_a_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'A-GmbH'.

**Content:**
```
\bA-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_hausverwaltung_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hausverwaltung-GmbH'.

**Content:**
```
\bHausverwaltung-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_finanzamt_hollabrunn_korneuburg_tulln`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Hollabrunn Korneuburg Tulln' and its genitive form.

**Content:**
```
\bFinanzamtes?\s+Hollabrunn\s+Korneuburg\s+Tulln\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bfg_aussenstelle_linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BFG, Außenstelle Linz'.

**Content:**
```
\bBFG,\s*Außenstelle\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1483 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)

**False Positives:**

```
Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.
```

FP: `BFG, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)
- `UFS` (organisation)

</details>

---

## `specific_bfg_aussenstelle_linz_paren`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BFG (Außenstelle Linz)'.

**Content:**
```
\bBFG\s*\(\s*Außenstelle\s+Linz\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_psd_wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'PSD Wien' as a standalone entity.

**Content:**
```
\bPSD\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_psycho_wagner_spital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Psychiatrie Otto Wagner Spital-' with flexible spacing.

**Content:**
```
\bPsychiatrie\s+Otto\s+Wagner\s+Spital-\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bundesamt_soziales`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its genitive form 'Bundesamtes für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamtes?\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 875 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_148`)

**False Positives:**

```
Stets ist jedoch erforderlich, dass die Tatsache der Behinderung und das  Ausmaß der Minderung der Erwerbsfähigkeit durch eine amtliche Bescheinigung (hier: des  Bundesamtes für Soziales und Behindertenwesen) nachgewiesen wird (§ 35 Abs. 2 EStG 1988).
```

FP: `Bundesamtes für Soziales und Behindertenwesen` (organisation)

**✅ Gold Entities:**

</details>

---

## `specific_london_film_academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and its typo 'London Film Acadamy'.

**Content:**
```
\bLondon\s+Film\s+Acad(eme)y\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_bundeskanzleramtes`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramtes' (genitive) and 'Bundeskanzleramt' (nominative).

**Content:**
```
\bBundeskanzleramtes?\b
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

