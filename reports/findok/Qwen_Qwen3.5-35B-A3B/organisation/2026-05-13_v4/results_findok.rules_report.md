# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-13T21:00:18.721600

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-13_v4/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 400 |
| Validation documents | 101 |
| Test documents | 12 |
| Train sentences | 1171 |
| Validation sentences | 213 |
| Test sentences | 1247 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 20 |
| Refinement iterations | 0 |
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
| Batch size | 20 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 85.1% |
| True Positives | 4 |
| False Positives | 2 |
| False Negatives | 252 |
| Total Gold Entities | 256 |
| Micro Precision | 66.7% |
| Micro Recall | 1.6% |
| Micro F1 | 3.1% |
| Macro F1 | 3.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `tax_authority_finanzamt` | 1.6% | 100.0% | 0.8% | 2 | 2 | 0 |
| `tax_authority_fa` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `tax_authority_fa_graz_stadt` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `company_uniconval` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bankhaus_denzel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_cervenka` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_textil_steingartlog` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_keltrizor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_dlcg_bildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_scheibenzuber_textil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bahrdt_digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hudec_christian` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hendrick_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_reinemut_smoch` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sudversand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenbank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_traunluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_www` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_tirol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_sophie_wittmeir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_zoruniglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mittelheizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_rosilius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_klosterneuburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_wien_2202122` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_niederoesterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_steiermark_mitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_maschinenbau_derwilsee` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mauriczat_medien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenbank_wienerwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenbank_suedweststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bawag_wohnbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_klusner_paeffgen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_tschermack_pharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_talverwerk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sud_landwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_henken` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sud_nortri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hulsebusch_breithaupt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ruterborries_friderich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_touristik_wildon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_logseemon_metall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_volkbank_wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_conwil_marine` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_tal_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_dias_telekom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_nordevent` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_annemie_bott` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_stadtenergie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_milan_haendlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_manfredo_herrschmann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_krolitzki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_gronemeier_hovelberndt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_baden_modling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_psomadakis_touristik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mittel_logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_fensudlog` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_luehrig_hundertmarck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_englert_mobel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_laskowsky_umwelt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sanitar_talder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_stadt_logglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_roelfsen_versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_lubomir_merschmeyer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_houdek_maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_schmeltz_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_dorfcon_verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_lexdon_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_wien_1_23` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_tritri_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_goeczu_getranke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hoerup_gastronomie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_dammke_ki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_naass_elektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bersud_mobel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_unter_heimdorf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_wxe_textil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_kornfelder_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_dgcv_ecommerce` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_fatima_finkenbein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ugqq_verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_conuni_heizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_stadt_dorfkraft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_digital_seeal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_inn_monost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_trafenfen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `court_zell_am_see` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_draufinanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_kelgart_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_donau_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_xjov_cloud` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_wildorftra_ki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `companybruckmonwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_niederoesterreich_vorsorge` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_lexkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_noruniwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_traun_digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_unibach_getranke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bierwerth` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_wien_waldnor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_kraftver_gastronomie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_gartgart_dienstleistungen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_botho_mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_kleinvorholt_ki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_gogel_daten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenkasse_retz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nord_kellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mur_ververzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_pastl_bachle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nordtravalumwelt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_oppert_elektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nexdorf_metall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_zimmerhackel_bau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `court_neunkirchen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_oststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_oststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bludszat_maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_gokdemir_landwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_talkel_versand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hebebrand_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_wald_bruckval` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_seyberth_kaben` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_wacr_möbel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_gorius_und_ziegann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenbank_rion` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_basdas_pharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_vahrenkamp_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_starker_beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_waldviertel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_landeck_reutte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sunramm_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_talwerk_logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_rpxf_immobilien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_rheindigital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_kok_heberlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_leiss_software` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_okur_automotive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_celikkanat_garten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_getranke_nexdorfzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_depp_versand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_obernoeder_kusbert` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_talost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sudevent` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ostwilnexlogistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_unter_services` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_lutkehans_event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_innluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_zyjy_automotive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nyj_event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_kubzyk_elektro_slash` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_kubzyk_elektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_dorfkraft_sanitar` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_logal_gruppe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hempel_heizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_schneppensieper_bultbrunne` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hagdorn_robotik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_enns_software` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_strohsack_dresbeimdieke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_gernot_hirschkorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_waldtouristik_technologien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hoch_synwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mur_donwerk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_elender_cloud` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_fuchsl_touristik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_traun_landwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_unter_services_compound` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_general` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_inn_recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bcol_event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_freimut_ohlroge` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ennsbildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_oliver_bartha` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisen_hall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_west_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_buhrfeindt_lebensmittel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_enns_werkal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_chen_setzekorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ostgart_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `entity_istvan_gerart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_innmarine_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hochlebensmittel_holding` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `court_silz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_waldtra_sicherheit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_oberrecycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_bergplanung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_yxtg_maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_norkel_software` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_alessi_event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `court_innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_berwaldkel_mobel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_wiederspan_beratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mur_alver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sievens_automotive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nord_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ostgetränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nord_trinex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_logkeltal_marine` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_zschieschank_transport` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mullbrandt_digital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_schoenfelder_textil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ober_chemie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_amundi_austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sud_sudwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nowothnig_wind` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_magerlein_logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_wenker_bau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sonnberg_holz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_fa_www_grieskirchen_wels` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_generic_suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_generic_suffix_strict` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `company_donau_furtkraftwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_donau_druck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `company_uniconval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Uniconval-Luftfahrt'.

**Content:**
```
\bUniconval-Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_bankhaus_denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bankhaus Denzel'.

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

## `company_cervenka`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Cervenka&Neunübel Telekom AG'.

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

## `company_textil_steingartlog`

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

## `company_keltrizor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Keldonbach Sicherheit GMBH'.

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

## `company_dlcg_bildung`

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

## `company_scheibenzuber_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Scheibenzuber Textil'.

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

## `company_bahrdt_digital`

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

## `company_hudec_christian`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hudec&Christian Immobilien GMBH'.

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

## `company_hendrick_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hendrick Recycling GMBH'.

**Content:**
```
\bHendrick\s+Recycling\s+GMBH\b
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

## `tax_authority_finanzamt`

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Description:**
Matches full tax authority names 'Finanzamt' or 'Finanzamtes' followed by specific multi-word locations. REMOVED 'Salzburg-Stadt' to fix false positive.

**Content:**
```
\bFinanzamte?\s+(?:Steiermark\s+Mitte|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Vorarlberg|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Salzburg\-Stadt|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Nieder\u00f6sterreich\s+Mitte|Innsbruck|Klosterneuburg|Wien\s+2/20/21/22|Wien\s+1/23|Tirol\s+Ost|Schwechat\s+Gerasdorf|Waldviertel|Salzburg\-Land|Bruck\s+Eisenstadt\s+Oberwart|Grieskirchen\s+Wels|Freistadt\s+Rohrbach\s+Urfahr|Purkersdorf|Judenburg\s+Liezen|Amstetten\s+Melk\s+Scheibbs|Linz|Baden\s+M\u00f6dling|Oststeiermark)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.016 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 26 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

</details>

---

## `tax_authority_fa`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities 'FA' followed by specific multi-word locations including 'Deutschlandsberg Leibnitz Voitsberg'.

**Content:**
```
(?<!www\.)\bFA\s+(?:Steiermark\s+Mitte|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Vorarlberg|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Salzburg\-Stadt|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Nieder\u00f6sterreich\s+Mitte|Innsbruck|Klosterneuburg|Wien\s+2/20/21/22|Wien\s+1/23|Tirol\s+Ost|Schwechat\s+Gerasdorf|Waldviertel|Salzburg\-Land|Bruck\s+Eisenstadt\s+Oberwart|Grieskirchen\s+Wels|Freistadt\s+Rohrbach\s+Urfahr|Purkersdorf|Judenburg\s+Liezen|Amstetten\s+Melk\s+Scheibbs)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 33 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

</details>

---

## `tax_authority_fa_graz_stadt`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'FA Graz-Stadt' specifically.

**Content:**
```
\bFA\s+Graz-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 255 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `Stella Marschalk, Bakk. techn.` (person)

</details>

---

## `company_uniconval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Uniconval-Luftfahrt'.

**Content:**
```
\bUniconval-Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_bankhaus_denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bankhaus Denzel'.

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

## `company_cervenka`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Cervenka&Neunübel Telekom AG'.

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

## `company_textil_steingartlog`

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

## `company_keltrizor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Keldonbach Sicherheit GMBH'.

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

## `company_dlcg_bildung`

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

## `company_scheibenzuber_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Scheibenzuber Textil'.

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

## `company_bahrdt_digital`

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

## `company_hudec_christian`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hudec&Christian Immobilien GMBH'.

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

## `company_hendrick_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hendrick Recycling GMBH'.

**Content:**
```
\bHendrick\s+Recycling\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_reinemut_smoch`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Reinemut + Smoch Handel'.

**Content:**
```
\bReinemut\s+\+\s+Smoch\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'SüdVersand'.

**Content:**
```
\bS\u00fcdVersand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_raiffeisenbank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Raiffeisenbank Wels Süd'.

**Content:**
```
\bRaiffeisenbank\s+Wels\s+S\u00fcd\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'TraunLuftfahrt Solutions' specifically. Ensures the specific name is captured.

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

## `tax_authority_fa_www`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific web-based tax authority references 'www.FA Salzburg-Stadt' and 'www.FA Grieskirchen Wels' found in training data.

**Content:**
```
\bwww\.FA\s+(?:Salzburg\-Stadt|Grieskirchen\s+Wels)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_tirol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific tax authority abbreviation 'FA Tirol Ost'.

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

## `entity_sophie_wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sophie Wittmeir' identified as an organization in training data.

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

## `company_zoruniglanz`

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

## `company_mittelheizung`

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

## `company_rosilius`

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

## `company_yavasoglu`

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

## `tax_authority_fa_klosterneuburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Klosterneuburg' specifically.

**Content:**
```
\bFA\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_wien_2202122`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Wien 2/20/21/22' specifically.

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

## `tax_authority_fa_niederoesterreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Niederösterreich Mitte' specifically.

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

## `tax_authority_finanzamt_steiermark_mitte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Steiermark Mitte' specifically.

**Content:**
```
\bFinanzamt\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_maschinenbau_derwilsee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Maschinenbau Derwilsee' specifically.

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

## `company_mauriczat_medien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mauriczat Medien' specifically.

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

## `company_raiffeisenbank_wienerwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Wienerwald' specifically.

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

## `company_raiffeisenbank_suedweststeiermark`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenbank Süd-Weststeiermark' specifically.

**Content:**
```
\bRaiffeisenbank\s+Süd-Weststeiermark\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_bawag_wohnbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BAWAG P.S.K. Wohnbaubank' specifically.

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

## `company_klusner_paeffgen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Klusner&Päffgen Bildung GMBH' specifically.

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

## `company_tschermack_pharma`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Tschermack Pharma GMBH' specifically.

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

## `company_talverwerk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'TalVerverwerkGarten GMBH' and its ellipsis variant found in training data.

**Content:**
```
\bTalVerverwerkGarten\s+GMBH(?:\u2026)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_sud_landwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Süd-Landwirtschaft'.

**Content:**
```
\bS\u00fcd-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_henken`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Henken'.

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

## `company_sud_nortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Süd Nortri'.

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

## `company_hulsebusch_breithaupt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hülsebusch + Breithaupt Versicherung'.

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

## `company_ruterborries_friderich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Rüterborries+Friderich Möbel'.

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

## `company_touristik_wildon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Touristik Wildon'.

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

## `company_logseemon_metall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Logseemon-Metall AG'.

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

## `company_volkbank_wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'VOLKSBANK WIEN'.

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

## `company_conwil_marine`

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

## `company_tal_druck`

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

## `entity_dias_telekom`

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

## `entity_nordevent`

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

## `entity_annemie_bott`

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

## `entity_stadtenergie`

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

## `entity_milan_haendlein`

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

## `entity_manfredo_herrschmann`

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

## `entity_krolitzki`

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

## `tax_authority_fa_linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific tax authority abbreviation 'FA Linz'.

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

## `company_gronemeier_hovelberndt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Grönemeier&Hövelberndt E‑Commerce' found in training data and failure cases.

**Content:**
```
\bGr\u00f6nemeier&H\u00f6velberndt\s+E\u2011Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_finanzamt_linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Linz' specifically.

**Content:**
```
\bFinanzamt\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_finanzamt_baden_modling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Baden Mödling' specifically.

**Content:**
```
\bFinanzamt\s+Baden\s+M\u00f6dling\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_psomadakis_touristik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Psomadakis Touristik' specifically.

**Content:**
```
\bPsomadakis\s+Touristik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_mittel_logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mittel-Logistik' specifically.

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

## `company_fensudlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fensudlog GMBH' specifically.

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

## `company_luehrig_hundertmarck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Luehrig + Hundertmarck Holz GMBH' specifically.

**Content:**
```
\bLuehrig\s+\+\s+Hundertmarck\s+Holz\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_englert_mobel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Englert Möbel' identified in training data and failure cases.

**Content:**
```
\bEnglert\s+M\u00f6bel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_laskowsky_umwelt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Laskowsky Umwelt' identified in training data and failure cases.

**Content:**
```
\bLaskowsky\s+Umwelt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_sanitar_talder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sanitär Talder GMBH'.

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

## `entity_stadt_logglanz`

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

## `company_roelfsen_versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Roelfsen Versicherung'.

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

## `entity_lubomir_merschmeyer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lubomir Merschmeyer'.

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

## `company_houdek_maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_schmeltz_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_dorfcon_verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_lexdon_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_wien_1_23`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific tax authority abbreviation 'FA Wien 1/23'.

**Content:**
```
\bFA\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_tritri_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Tritri-IT' identified in training data.

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

## `company_goeczu_getranke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_hoerup_gastronomie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hörup Gastronomie AG'.

**Content:**
```
\bHörup\s+Gastronomie\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_dammke_ki`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Dammke KI GMBH'.

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

## `company_naass_elektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Naaß Elektro GMBH'.

**Content:**
```
\bNaa\u00df\s+Elektro\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_bersud_mobel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bersud Möbel GMBH'.

**Content:**
```
\bBersud\s+M\u00f6bel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_unter_heimdorf`

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

## `company_wxe_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'WXE Textil GMBH'.

**Content:**
```
\bWXE\s+Textil\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_kornfelder_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Kornfelder Recycling'.

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

## `company_dgcv_ecommerce`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'DGCV E-Commerce GMBH'.

**Content:**
```
\bDGCV\s+E\u2011Commerce\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `entity_fatima_finkenbein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Fatima Finkenbein' identified as an organization in training data.

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

## `company_ugqq_verlag`

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

## `company_conuni_heizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Conuni-Heizung'.

**Content:**
```
\bConuni-Heizung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_stadt_dorfkraft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Stadt Dorfkraft'.

**Content:**
```
\bStadt\s+Dorfkraft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_digital_seeal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Digital Seeal'.

**Content:**
```
\bDigital\s+Seeal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_inn_monost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Inn Monost'.

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

## `company_trafenfen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Trafenfen Automotive' and 'Trafenfen Automotive GmbH'.

**Content:**
```
\bTrafenfen\s+Automotive(?:\s+GmbH)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `court_zell_am_see`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht Zell am See'.

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

## `company_draufinanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DrauFinanzen'.

**Content:**
```
\bDrauFinanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_kelgart_druck`

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

## `company_donau_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DonauRecycling GMBH'.

**Content:**
```
\bDonauRecycling\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_xjov_cloud`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'XJOV Cloud Dienstleistungen GMBH'.

**Content:**
```
\bXJOV\s+Cloud\s+Dienstleistungen\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_wildorftra_ki`

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

## `companybruckmonwil`

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

## `organisation_niederoesterreich_vorsorge`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Niederösterreichische Vorsorgekasse'.

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

## `company_lexkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lexkel Vertrieb KG' and 'Lexkel Vertrieb KG.' (with optional trailing period).

**Content:**
```
\bLexkel\s+Vertrieb\s+KG\.?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_noruniwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Noruniwald-Technik'.

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

## `company_traun_digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Traun-Digital KG'.

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

## `company_unibach_getranke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Unibach-Getränke AG'.

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

## `company_bierwerth`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bierwerth'.

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

## `company_wien_waldnor`

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

## `company_kraftver_gastronomie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Kraftver-Gastronomie GMBH'.

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

## `company_gartgart_dienstleistungen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Gartgart Dienstleistungen GMBH'.

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

## `entity_botho_mikloweit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Botho Mikloweit' identified as an organization in training data.

**Content:**
```
\bBotho\s+Mikloweit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_kleinvorholt_ki`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Klein-Vorholt KI GMBH'.

**Content:**
```
\bKlein-Vorholt\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_gogel_daten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Gogel Daten GMBH'.

**Content:**
```
\bGogel\s+Daten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_raiffeisenkasse_retz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Raiffeisenkasse Retz-Pulkautal'.

**Content:**
```
\bRaiffeisenkasse\s+Retz-Pulkautal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_nord_kellex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Nord Kellex'.

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

## `company_mur_ververzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mur Ververzor Betriebe'.

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

## `company_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Pastl+Bächle Handel' found in training data and failure cases.

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

## `company_nordtravalumwelt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'NordTravalUmwelt AG' found in training data and failure cases.

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

## `company_norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Norconheim' identified in training data.

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

## `company_oppert_elektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Oppert Elektro' identified in training data.

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

## `company_nexdorf_metall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Nexdorf-Metall' identified in training data.

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

## `company_zimmerhackel_bau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Zimmerhackel Bau' identified in training data.

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

## `court_neunkirchen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirksgericht Neunkirchen' identified in training data.

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

## `tax_authority_fa_oststeiermark`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Oststeiermark' specifically to ensure high recall despite spacing variations.

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

## `tax_authority_finanzamt_oststeiermark`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Oststeiermark' specifically.

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

## `company_bludszat_maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bludszat Maschinenbau GMBH' found in multiple failure cases.

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

## `company_gokdemir_landwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gökdemir Landwirtschaft AG' found in failure cases.

**Content:**
```
\bGökdemir\s+Landwirtschaft\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_talkel_versand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Talkel-Versand AG' found in failure cases.

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

## `company_hebebrand_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hebebrand Recycling AG' found in failure cases.

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

## `company_wald_bruckval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wald Bruckval AG' found in failure cases.

**Content:**
```
\bWald\s+Bruckval\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_seyberth_kaben`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Seyberth + Kaben Getränke AG' found in failure cases.

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

## `company_wacr_möbel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'WACR Möbel Planung AG' found in failure cases.

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

## `company_gorius_und_ziegann`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Gorius und Ziegann Event GMBH'.

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

## `company_raiffeisenbank_rion`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Raiffeisenbank Rion Vöcklabruck'.

**Content:**
```
\bRaiffeisenbank\s+Rion\s+V\u00f6cklabruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_basdas_pharma`

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

## `company_vahrenkamp_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Vahrenkamp Luftfahrt'.

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

## `company_starker_beratung`

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

## `tax_authority_fa_waldviertel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Waldviertel' specifically.

**Content:**
```
\bFA\s+Waldviertel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_landeck_reutte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Landeck Reutte' specifically.

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

## `company_sunramm_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sünramm Druck'.

**Content:**
```
\bS\u00fcnramm\s+Druck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_talwerk_logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Talwerk Logistik Holding GMBH'.

**Content:**
```
\bTalwerk\s+Logistik\s+Holding\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_rpxf_immobilien`

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

## `company_rheindigital`

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

## `company_kok_heberlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kök & Heberlein Bau' only if not immediately followed by a legal suffix like GmbH & Co KG.

**Content:**
```
\bK\u00f6k\s+&\s+Heberlein\s+Bau(?![\s]*(?:GmbH|KG|AG|&\s*Co))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_leiss_software`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Leiss Software' only if not immediately followed by a legal suffix like GmbH & Co KG.

**Content:**
```
\bLeiss\s+Software(?![\s]*(?:GmbH|KG|AG|&\s*Co))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_okur_automotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Okur Automotive' only if not immediately followed by a legal suffix like GmbH & Co KG.

**Content:**
```
\bOkur\s+Automotive(?![\s]*(?:GmbH|KG|AG|&\s*Co))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_celikkanat_garten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Celikkanat Garten' only if not immediately followed by a legal suffix like GmbH & Co KG.

**Content:**
```
\bCelikkanat\s+Garten(?![\s]*(?:GmbH|KG|AG|&\s*Co))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_getranke_nexdorfzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Getränke Nexdorfzor GMBH'.

**Content:**
```
\bGetr\u00e4nke\s+Nexdorfzor\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_depp_versand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Depp Versand'.

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

## `company_obernoeder_kusbert`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Obernöder+Küsbert Touristik GMBH'.

**Content:**
```
\bObernöder\+Küsbert\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_talost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Talost GMBH'.

**Content:**
```
\bTalost\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_sudevent`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'SüdEvent AG'.

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

## `company_ostwilnexlogistik`

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

## `company_unter_services`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Unter[Name] Services GMBH' patterns found in failure cases.

**Content:**
```
\bUnter\s+[A-Z][a-z]+\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_lutkehans_event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Lütkehans Event GMBH'

**Content:**
```
\bLütkehans\s+Event\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_innluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'InnLuftfahrt GMBH'

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

## `company_zyjy_automotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'ZYJY Automotive AG'

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

## `company_nyj_event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'NYJ Event AG'

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

## `company_kubzyk_elektro_slash`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches '/Kubzyk Elektro AG' (with leading slash)

**Content:**
```
/Kubzyk\s+Elektro\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_kubzyk_elektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kubzyk Elektro AG'

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

## `company_dorfkraft_sanitar`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Dorfkraft-Sanitär AG'

**Content:**
```
\bDorfkraft-Sanitär\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_logal_gruppe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Logal Gruppe'

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

## `company_hempel_heizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hempel Heizung GMBH'.

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

## `company_schneppensieper_bultbrunne`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Schneppensieper & Bültbrunne Touristik'.

**Content:**
```
\bSchneppensieper\s+&\s+Bültbrunne\s+Touristik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_hagdorn_robotik`

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

## `company_enns_software`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Enns-Software'.

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

## `company_strohsack_dresbeimdieke`

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

## `entity_gernot_hirschkorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Gernot Hirschkorn' identified as an organization in training data.

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

## `company_waldtouristik_technologien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'WaldTouristik Technologien'.

**Content:**
```
\bWaldTouristik\s+Technologien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_hoch_synwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Hoch Synwil'.

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

## `company_mur_donwerk`

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

## `company_elender_cloud`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Elender Cloud'.

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

## `company_fuchsl_touristik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Füchsl Touristik GMBH'.

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

## `company_traun_landwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'TraunLandwirtschaft'.

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

## `company_unter_services_compound`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Unter[Name] Services GMBH' where 'Unter' is attached to the name (e.g., UnterRecycling Services GMBH).

**Content:**
```
\bUnter[A-Z][a-zA-Z]+\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_general`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by a capitalized location, excluding known multi-word locations and preventing partial matches like 'FA Graz' when 'Graz-Stadt' follows.

**Content:**
```
\bFA\s+(?!Steiermark\s+Mitte|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Vorarlberg|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Salzburg\-Stadt|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Nieder\u00f6sterreich\s+Mitte|Innsbruck|Klosterneuburg|Wien\s+2/20/21/22|Wien\s+1/23|Tirol\s+Ost|Schwechat\s+Gerasdorf|Waldviertel|Salzburg\-Land|Bruck\s+Eisenstadt\s+Oberwart|Grieskirchen\s+Wels|Freistadt\s+Rohrbach\s+Urfahr|Purkersdorf|Judenburg\s+Liezen|Amstetten\s+Melk\s+Scheibbs|Oststeiermark|Linz|Graz\-Stadt)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)(?!\s+(?:Limited|Inc|Corp|GmbH|AG|KG|&\s*Co))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_inn_recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Inn-Recycling Institut GMBH' found in training data.

**Content:**
```
\bInn-Recycling\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_bcol_event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BCOL Event AG'.

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

## `company_freimut_ohlroge`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Freimut+Ohlroge Analyse AG'.

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

## `company_ennsbildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'EnnsBildung'.

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

## `company_oliver_bartha`

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

## `company_raiffeisen_hall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_west_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'West-Luftfahrt' found in training data and failure cases.

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

## `company_buhrfeindt_lebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Buhrfeindt Lebensmittel GMBH' found in training data and failure cases.

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

## `company_enns_werkal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Enns Werkal GMBH' found in training data and failure cases.

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

## `entity_chen_setzekorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Chen Setzekorn' identified as an organization in training data and failure cases.

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

## `company_ostgart_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Ostgart AG' found in training data and failure cases.

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

## `entity_istvan_gerart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Istvan Gerart' identified as an organization in training data and failure cases.

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

## `company_innmarine_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'InnMarine GMBH' found in training data and failure cases.

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

## `company_hochlebensmittel_holding`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'HochLebensmittel Holding GMBH' found in training data and failure cases.

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

## `court_silz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirksgericht Silz' found in training data and failure cases.

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

## `company_waldtra_sicherheit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Waldtra-Sicherheit' specifically. Priority increased to ensure it captures the full name before any generic suffix matching could occur (though generic rule is removed).

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

## `company_oberrecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'OberRecycling' found in failure cases.

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

## `company_bergplanung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BergPlanung' found in failure cases.

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

## `company_yxtg_maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'YXTG Maschinenbau' found in failure cases.

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

## `company_norkel_software`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Norkel-Software GMBH' found in failure cases.

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

## `company_alessi_event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Alessi Event GMBH' found in failure cases.

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

## `court_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LG Innsbruck' and 'Landesgericht Innsbruck' as organizations.

**Content:**
```
\b(?:LG|Landesgericht)\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_berwaldkel_mobel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Berwaldkel-Möbel AG'.

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

## `company_wiederspan_beratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wiederspan Beratung GMBH'.

**Content:**
```
\bWiederspan\s+Beratung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_mur_alver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mur Alver OG'.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_sievens_automotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sievens Automotive GMBH'.

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

## `company_nord_druck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Nord-Druck GMBH'.

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

## `company_ostgetränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'OstGetränke GMBH'.

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

## `company_nord_trinex`

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

## `company_logkeltal_marine`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Logkeltal Marine'.

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

## `company_zschieschank_transport`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Zschieschank&Heeß Transport GMBH' specifically.

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

## `company_mullbrandt_digital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Müllbrandt u. Worthmeier Digital GMBH' specifically.

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

## `company_schoenfelder_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schoenfelder Textil KG' specifically to override generic rule.

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

## `company_ober_chemie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Ober-Chemie GMBH' specifically to override generic rule.

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

## `company_amundi_austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amundi Austria GmbH' specifically to override generic rule.

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

## `company_sud_sudwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Süd Sudwil' specifically.

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

## `company_nowothnig_wind`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Nowothnig Wind' found in training data.

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

## `company_magerlein_logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Mägerlein Logistik' found in training data.

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

## `company_wenker_bau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wenker Bau GMBH' found in training data.

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

## `company_sonnberg_holz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sonnberg Holz GMBH' found in training data.

**Content:**
```
\bSonnberg\s+Holz\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_fa_www_grieskirchen_wels`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific web-based tax authority reference 'www.FA Grieskirchen Wels' found in training data and failure cases.

**Content:**
```
\bwww\.FA\s+Grieskirchen\s+Wels\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_generic_suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
REMOVED: This rule was too broad, causing false positives on partial names like 'Steuerberatungs GmbH', 'Co KG', and 'Partner GmbH'. It has been deleted to improve precision.

**Content:**
```

```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_generic_suffix_strict`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organization names with generic suffixes (GmbH, AG, KG, etc.) only if preceded by a multi-word proper noun (at least two capitalized words) to avoid false positives on fragments like 'Steuerberatung GmbH'.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*)\s+(?:GmbH|AG|KG|Systeme|Maschinenbau|Recycling|Planung|Software|Sicherheit|Logistik|Handel|Dienstleistungen|Bau|Elektro|Garten|Touristik|Verlag|Vertrieb|Holding|Institut|Gruppe|Werke|Produkte|Technologien|Automotive|Cloud|KI|Medien|Immobilien|Versicherung|Pflege|Analyse|Gastronomie|Lebensmittel|Druck|Textil|Luftfahrt|Energie|Werkal|Werk|Betriebe|E-Commerce|ECommerce)\b(?!(?:\s+&\s*Co\s+KG|\s+GmbH\s+&\s*Co|\s+Steuerberatung|\s+Partners))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 108 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Steuerberatung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mitterbauer GmbH` — partial — pred is substring of gold: `Anwälte Mandl & Mitterbauer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

</details>

---

## `company_donau_furtkraftwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Donau Furtkraftwald AG' and its URL variant '://www.Donau Furtkraftwald AG' found in training data.

**Content:**
```
(?:://www\.)?Donau\s+Furtkraftwald\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_donau_druck`

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

</details>

---

