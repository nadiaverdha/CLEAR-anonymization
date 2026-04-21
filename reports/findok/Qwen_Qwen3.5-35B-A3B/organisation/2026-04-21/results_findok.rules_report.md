# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-21T09:24:31.482809

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-21/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training examples | 2172 |
| Validation examples | 373 |
| Test examples | 12077 |
| Train annotations | 2891 |
| Validation annotations | 471 |
| Test annotations | 3323 |
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

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 90.6% |
| True Positives | 690 |
| False Positives | 447 |
| Micro Precision | 60.7% |
| Micro Recall | 39.6% |
| Micro F1 | 47.9% |
| Macro F1 | 47.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Specific_Org_GozcuGetränke` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `Specific_Org_SchmeltzLuftfahrt` | 1.3% | 100.0% | 0.6% | 11 | 11 | 0 |
| `Specific_Org_HoudekMaschinenbau` | 6.2% | 100.0% | 3.2% | 56 | 56 | 0 |
| `Specific_Org_LexdonIT` | 0.8% | 100.0% | 0.4% | 7 | 7 | 0 |
| `Specific_Org_EventSudkraftlex` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `Specific_Org_RoelfsenVersicherung` | 3.6% | 100.0% | 1.8% | 32 | 32 | 0 |
| `Specific_Org_LubomirMerschmeyer` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Specific_Org_CervenkaNeunubel` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific_Org_FinanzamtKlosterneuburg` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_ReinemutSmoch` | 4.5% | 100.0% | 2.3% | 40 | 40 | 0 |
| `Org_AMS_Oesterreich` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Org_Raiffeisenbank_Karnische` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `Specific_Org_TschurtschenthalerWalderFister` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Hamburger_Fern_Hochschule` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Universitaet_Wien` | 2.0% | 100.0% | 1.0% | 18 | 18 | 0 |
| `Specific_Org_HLFTourismus` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Org_DeloitteTaxWirtschaftsprüfungs` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `Org_Finanzamt_Grossbetriebe` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Garanta_VersicherungsAG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Sivananda` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_AVED` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Yoga_Vidya` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Mag_Ghesla` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific_Org_Geschenkartikel` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_OeGK` | 4.5% | 100.0% | 2.3% | 40 | 40 | 0 |
| `Specific_Org_England` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific_Org_University_of_Bristol` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Specific_Org_Hallas_Partner` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Dorfcon_Verlag` | 1.0% | 100.0% | 0.5% | 9 | 9 | 0 |
| `Specific_Org_LeitnerLeitner` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_X_GmbH` | 2.2% | 100.0% | 1.1% | 19 | 19 | 0 |
| `Specific_Org_R_GmbH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific_Org_Betriebsprüfung_GmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_TritriIT` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Retail_Chains` | 1.0% | 100.0% | 0.5% | 9 | 9 | 0 |
| `Specific_Org_AnwalteMandlMitterbauer` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Berwaldkel_Möbel_AG` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Specific_Org_InnMarine` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Bezirkshauptmannschaft_Bludenz` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `Specific_Org_OeBB` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific_Org_SeneCura_Laurentius_Park_Bludenz` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Specific_Org_Krankenpflegevereins_Bludenz` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_Verwaltungsgericht_Wien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_TAXCOACH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_University_St_Gallen` | 0.8% | 100.0% | 0.4% | 7 | 7 | 0 |
| `Specific_Org_MusikhochschuleWien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_KonservatoriumStadtWien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_WienerPhilharmoniker` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Specific_Org_BankhausDenzel` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Specific_Org_MerkurTreuhand` | 1.1% | 100.0% | 0.6% | 10 | 10 | 0 |
| `Specific_Org_Schabetsberger` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Specific_Org_WU_Wien` | 1.6% | 93.3% | 0.8% | 15 | 14 | 1 |
| `Specific_Org_SENECURA` | 0.8% | 87.5% | 0.4% | 8 | 7 | 1 |
| `Specific_Org_Wirtschaftsuniversitaet_Wien` | 1.4% | 85.7% | 0.7% | 14 | 12 | 2 |
| `Specific_Org_JKU_Linz` | 1.3% | 84.6% | 0.6% | 13 | 11 | 2 |
| `Specific_Org_Kings_School` | 0.5% | 80.0% | 0.2% | 5 | 4 | 1 |
| `Specific_Org_SUVA` | 5.3% | 75.0% | 2.8% | 64 | 48 | 16 |
| `Specific_Org_PVA` | 0.6% | 71.4% | 0.3% | 7 | 5 | 2 |
| `Specific_Org_Johannes_Kepler_Universitaet_Linz` | 0.6% | 62.5% | 0.3% | 8 | 5 | 3 |
| `Court_Bezirksgericht` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Specific_Org_Kings_School_Worcester` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Specific_Org_Verwaltungsgerichtshof` | 17.8% | 42.3% | 11.3% | 466 | 197 | 269 |
| `Specific_Org_SeneCura_Laurentius_Park` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `General_Org_AG` | 0.3% | 33.3% | 0.2% | 9 | 3 | 6 |
| `Specific_Org_JKU` | 0.7% | 28.6% | 0.3% | 21 | 6 | 15 |
| `Specific_Org_Verfassungsgerichtshof` | 0.7% | 27.3% | 0.3% | 22 | 6 | 16 |
| `General_Org_GmbH` | 2.1% | 26.4% | 1.1% | 72 | 19 | 53 |
| `Specific_Org_WU` | 0.3% | 15.8% | 0.2% | 19 | 3 | 16 |
| `Specific_Org_MerkurTreuhand_NoGmbH` | 0.1% | 9.1% | 0.1% | 11 | 1 | 10 |
| `Court_Landesgericht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_EnnsBildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_KornfelderRecycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_SeeGarttalder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_WaldTouristik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_GetränkeNexdorfzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_OkurAutomotive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_CelikkanatGarten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_YXTG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_KlusnerPaffgen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_TschermackPharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_GrönemeierHövelberndt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_DrauFinanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_DonauDruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_AnnemieBott` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_StadtEnergie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Triloglex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Sievens` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_NordDruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_OstGetränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_MilanHändlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_SünrammDruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_SüdNortri` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_KraftverGastronomie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_InnLuftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_HochLebensmittel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_MittelHeizungWerke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_VossbeinLebensmittel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_RheinDigital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_KokHeberlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_LeissSoftware` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_PastlBachle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_WaldtraSicherheit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Zoruniglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_AlalMedien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_PastelPharma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_ElenderCloud` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_TextilSteingartlog` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_NowothnigWind` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_FinanzenTradonnex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_GartgartDienstleistungen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_SanitärTalter` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_BludszatMaschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_RaiffeisenbankWelsSüd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_BauermeisterGetränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_NordKellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_KrolitzkiBeratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_ForschungWaldlemtal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_ManfredoHerrschmann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_RuterborriesFriderichMöbel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_VolksbankWien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_GartgartDienstleistungenGMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_EnergieSynlexder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_ChenSetzekorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_SüdLemkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_SteinfurtglanzLandwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_KubzykElektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_StarkerBeratung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_FHKaernten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_FachhochschuleKaernten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_KarlFranzensUniversitaetGraz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_BGmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_AGmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_HausverwaltungGmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `General_Org_KG` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `Specific_Org_FinanzamtSalzburgStadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Org_Bundesministers_Arbeit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Raiffeisenbank_Stallhofen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_BDO_Austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_GreinerMaiEvent` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_DLCG_Bildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_DGCV_ECommerce` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Unter_Donunisee` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_LondonFilmAcademy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Bundeskanzleramt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Bundesministeriums_Fuer_Justiz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_SaxingerChalupsky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Verwaltungsgerichtshof_Parenthetical` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Imre_Schaffer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_Talwerk_Logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_BKSSteuerberatung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Org_OBUG_Nikolaus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Org_FA_Location` | 0.0% | 0.0% | 0.0% | 52 | 0 | 52 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Specific_Org_HoudekMaschinenbau`

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Description:**
Matches Houdek Maschinenbau specifically.

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

**Example 0** (doc_id: ``)

```
... Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der <<<Houdek Maschinenbau>>>, Str.Nr.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: ``)

```
95-002/7970, BV 24:  Das Unternehmen <<<Houdek Maschinenbau>>>  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: ``)

```
... die Nachfolgejahre wurden folgende  Umgründungsschritte bei <<<Houdek Maschinenbau>>>  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages ...
```

```
... des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die <<<Houdek Maschinenbau>>>  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: ``)

```
Zum Stichtag 31.12.2008 ist die <<<Houdek Maschinenbau>>>  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: ``)

```
... Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der <<<Houdek Maschinenbau>>>, insoweit das auch nach der Abspaltung zum  31.12.2007 bei ...
```

```
... insoweit das auch nach der Abspaltung zum  31.12.2007 bei der <<<Houdek Maschinenbau>>>  verbliebende Vermögen betroffen ist.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `Specific_Org_ReinemutSmoch`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches Reinemut + Smoch Handel specifically.

**Content:**
```
\bReinemut\s+\+\s+Smoch\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1224 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. <<<Reinemut + Smoch Handel>>>, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 1** (doc_id: ``)

```
... 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  <<<Reinemut + Smoch Handel>>>  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 2** (doc_id: ``)

```
... des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der <<<Reinemut + Smoch Handel>>>  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 3** (doc_id: ``)

```
Über die <<<Reinemut + Smoch Handel>>>  wird gemäß §§ 28a Abs. 2 und 33 Abs. 5 FinStrG iVm §§ 3-5 ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 4** (doc_id: ``)

```
... Angelegenheiten verantwortliche Geschäftsführer der Firma  <<<Reinemut + Smoch Handel>>>, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

</details>

---

## `Specific_Org_OeGK`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches ÖGK (Österreichische Gesundheitskasse).

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

**Example 0** (doc_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: ``)

```
... die oben  angeführten Abgaben - entsprechend dem Vorgehen der <<<ÖGK>>> - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: ``)

```
... Zuge derselben GPLB angefallen seien,  seien diese seitens der <<<ÖGK>>> der GmbH vorgeschrieben worden, sodass Herr F nicht damit  ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: ``)

```
... in die Databox des EU gerichtet  wurden, die Bescheide der <<<ÖGK>>> allerdings an die GmbH übermittelt wurden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Specific_Org_RoelfsenVersicherung`

**F1:** 0.036 | **Precision:** 1.000 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches Roelfsen Versicherung specifically.

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

**Example 0** (doc_id: ``)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der <<<Roelfsen Versicherung>>>, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: ``)

```
Kff. Sandra Khartchenko  als RNF der <<<Roelfsen Versicherung>>>  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: ``)

```
... betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (<<<Roelfsen Versicherung>>>  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: ``)

```
Bescheidadressaten waren  sowohl das Gruppenmitglied <<<Roelfsen Versicherung>>>  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: ``)

```
... Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die <<<Roelfsen Versicherung>>>  durch Übertragung des  gesamten Betriebes (mit Ausnahme der ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

---

## `Specific_Org_EventSudkraftlex`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches Event Sudkraftlex GMBH specifically.

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

**Example 0** (doc_id: ``)

```
... abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die <<<Event Sudkraftlex GMBH>>>  hinsichtlich der oa.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: ``)

```
... Bescheides gegen den Beschuldigten als Geschäftsführer der <<<Event Sudkraftlex GMBH>>>  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: ``)

```
... handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der <<<Event Sudkraftlex GMBH>>>.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: ``)

```
... der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die <<<Event Sudkraftlex GMBH>>>  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: ``)

```
... MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der <<<Event Sudkraftlex GMBH>>>  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Specific_Org_Verwaltungsgerichtshof`

**F1:** 0.178 | **Precision:** 0.423 | **Recall:** 0.113  

**Format:** `regex`  
**Description:**
Matches Verwaltungsgerichtshof and its genitive form Verwaltungsgerichtshofes.

**Content:**
```
\bVerwaltungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.113 | 0.178 | 466 | 197 | 269 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 197 | 269 | 1544 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: ``)

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: ``)

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: ``)

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: ``)

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `General_Org_GmbH`

**F1:** 0.021 | **Precision:** 0.264 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches company names ending in GMBH, ensuring the full name is captured by requiring a preceding capitalized word, excluding court/tax terms.

**Content:**
```
(?<!\w)(?<!Arbeitgeber\s)(?<!Firma\s)(?<!Fa\.\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Holding\s)(?<!Services\s)(?<!Unter\s)(?<!Unternehmens\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Elektro\s)(?<!Steuerberatungs\s)(?<!Wirtschaftsprüfung\s)(?<!Bundesfinanzgericht\s)(?<!Finanzamt\s)(?<!Magistrat\s)(?<!Verwaltungsgericht\s)(?<!Verfassungsgericht\s)(?<!Adr\s)(?<!Adresse\s)(?<!Finanzamtes\s)(?<!Finanzamt\s)(?:Die\s+)?([A-Z][a-zA-Z0-9\-]+(?:\s+[A-Z][a-zA-Z0-9\-]+)*\s+GMBH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.264 | 0.011 | 0.021 | 72 | 19 | 53 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 53 | 1584 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Juni bis Dezember 2017 bereits Verjährung eingetreten und die  <<<KQPC Versand GMBH>>>  im Jänner 2018 nicht mehr tätig gewesen sei.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: ``)

```
Die <<<KQPC Versand GMBH>>>  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten ...
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: ``)

```
... hinsichtlich der Funktion des Beschuldigten (Geschäftsführer <<<Event Sudkraftlex GMBH>>>  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes ...
```

```
... (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer <<<KQPC Versand GMBH>>>) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: ``)

```
... GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), <<<Sudver Handel Services GMBH>>>  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, ...
```

```
... Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und <<<Glanznorost Institut GMBH>>> (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 ...
```

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

**Example 4** (doc_id: ``)

```
... (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  <<<Event Sudkraftlex GMBH>>>  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC <<<Versand GMBH>>>  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, ...
```

FP: `Versand GMBH` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 1** (doc_id: ``)

**False Positives:**

```
Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC <<<Versand GMBH>>>  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die ...
```

FP: `Versand GMBH` (organisation)

**✅ Gold Entities:**
- `KQPC Versand GMBH` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event <<<Sudkraftlex GMBH>>>  hinsichtlich der oa.
```

FP: `Sudkraftlex GMBH` (organisation)

**✅ Gold Entities:**
- `Event Sudkraftlex GMBH` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
... Bescheides gegen den Beschuldigten als Geschäftsführer der Event <<<Sudkraftlex GMBH>>>  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung ...
```

FP: `Sudkraftlex GMBH` (organisation)

**✅ Gold Entities:**
- `Event Sudkraftlex GMBH` (organisation)

**Example 4** (doc_id: ``)

**False Positives:**

```
... Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC <<<Versand GMBH>>>  als auch der Event Sudkraftlex GMBH.
```

FP: `Versand GMBH` (organisation)

```
... Geschäftsführer  der KQPC Versand GMBH  als auch der Event <<<Sudkraftlex GMBH>>>.
```

FP: `Sudkraftlex GMBH` (organisation)

**✅ Gold Entities:**
- `KQPC Versand GMBH` (organisation)
- `Event Sudkraftlex GMBH` (organisation)

</details>

---

## `Org_FA_Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt abbreviations (FA) followed by location names (e.g., FA Spittal Villach, FA Salzburg-Stadt, FA Landeck Reutte).

**Content:**
```
\bFA\s+[A-Za-zäöüÄÖÜß][A-Za-zäöüÄÖÜß\s-]+(?:\s+[A-Za-zäöüÄÖÜß][A-Za-zäöüÄÖÜß\s-]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 52 | 0 | 52 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 52 | 1743 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... über die Beschwerde vom  21. März 2023 gegen den Bescheid des <<<FA Waldviertel  vom >>>17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer ...
```

FP: `FA Waldviertel  vom ` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: ``)

**False Positives:**

```
... über die Beschwerde vom  21. März 2023 gegen den Bescheid des <<<FA Waldviertel  vom >>>17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer ...
```

FP: `FA Waldviertel  vom ` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 2** (doc_id: ``)

**False Positives:**

```
Zu A. und B. führte das <<<FA begründend aus>>>, dass der Bf. für mehr als ein Kind Familienbeihilfe  bezogen ...
```

FP: `FA begründend aus` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Der Bf. brachte beim <<<FA am >>>11.09.2023 folgende Beschwerde ein:  „Zum einen hat meine Tochter, ...
```

FP: `FA am ` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
... Beschwerde des Bf. gegen den Rückforderungsbescheid wurde vom <<<FA mit  Beschwerdevorentscheidung vom >>>11.09.2023 mit folgender Begründung abgewiesen:  „Gemäß § 2 ...
```

FP: `FA mit  Beschwerdevorentscheidung vom ` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific_Org_WU`

**F1:** 0.003 | **Precision:** 0.158 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches WU as an abbreviation for Wirtschaftsuniversität Wien.

**Content:**
```
\bWU\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.158 | 0.002 | 0.003 | 19 | 3 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 16 | 638 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
Siehe Internetseite JKU und <<<WU>>>  Karriereaussichten!
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 1** (doc_id: ``)

```
 Beispieldarstellung Übereinstimmung Lehrplan <<<WU>>> mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, ...
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 2** (doc_id: ``)

```
... sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (<<<WU>>>: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“, ...
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (<<<WU>>> Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
 Abgangsbescheinigung der <<<WU>>> Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... ECTS-Punkten an der JKU Linz absolviert wurden und dass an der <<<WU>>> Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
... der  Beschwerde angekündigte Nachreichung der Unterlagen der <<<WU>>> Wien (Vergleich der  Studienrichtungen).
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 4** (doc_id: ``)

**False Positives:**

```
... es sich bei BA Sozial- und Wirtschaftswissenschaften an der <<<WU>>>  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

</details>

---

## `Specific_Org_Verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 0.273 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches Verfassungsgerichtshof (full name) and its genitive form Verfassungsgerichtshofes.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
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

**Example 0** (doc_id: ``)

```
... Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem <<<Verfassungsgerichtshof>>>  oder vor dem Gerichtshof der Europäischen Union.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: ``)

```
... hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim <<<Verfassungsgerichtshof>>> zu stellen.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: ``)

```
... Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  <<<Verfassungsgerichtshof>>> (§ 88a Abs. 2 VfGG) nicht zulässig.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: ``)

```
Darüber hinaus hat der <<<Verfassungsgerichtshof>>> in seinem Beschluss vom 19. September 2025  zu E 1733/2025 ...
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: ``)

```
... unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom <<<Verfassungsgerichtshof>>> geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH ...
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Der <<<Verfassungsgerichtshof>>> (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen, ...
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
Der <<<Verfassungsgerichtshof>>> ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein ...
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Dies unter Bezug auf ein Erkenntnis des  <<<Verfassungsgerichtshofes>>> (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
2.4 Zitierte Entscheidung des <<<Verfassungsgerichtshofes>>> gegenständlich nicht einschlägig   Wie das Finanzamt unter ...
```

FP: `Verfassungsgerichtshofes` (organisation)

```
... einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des <<<Verfassungsgerichtshofes>>> (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
Im der  zitierten Entscheidung des <<<Verfassungsgerichtshofes>>> zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Court_Landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Regional Courts (Landesgericht) and its abbreviation LG, ensuring it captures the full location including 'für [Location]' patterns but stops before dates or 'vom'.

**Content:**
```
\b(?:Landesgericht|LG)\s+(?:f\u00fcr\s+)?[A-Za-z0-9\-]+(?:\s+[A-Za-z0-9\-]+)*(?=\s+(?:vom|am|vom\s+\d+|am\s+\d+)|$|[,;])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_EnnsBildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches EnnsBildung specifically.

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

## `Specific_Org_KornfelderRecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Kornfelder Recycling specifically.

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

## `Specific_Org_SeeGarttalder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches See Garttalder specifically.

**Content:**
```
\bSee\s+Garttalder\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_WaldTouristik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches WaldTouristik Technologien specifically.

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

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Specific_Org_Verwaltungsgerichtshof`

**F1:** 0.178 | **Precision:** 0.423 | **Recall:** 0.113  

**Format:** `regex`  
**Description:**
Matches Verwaltungsgerichtshof and its genitive form Verwaltungsgerichtshofes.

**Content:**
```
\bVerwaltungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.113 | 0.178 | 466 | 197 | 269 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 197 | 269 | 1544 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: ``)

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: ``)

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: ``)

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: ``)

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific_Org_HoudekMaschinenbau`

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Description:**
Matches Houdek Maschinenbau specifically.

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

**Example 0** (doc_id: ``)

```
... Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der <<<Houdek Maschinenbau>>>, Str.Nr.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: ``)

```
95-002/7970, BV 24:  Das Unternehmen <<<Houdek Maschinenbau>>>  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: ``)

```
... die Nachfolgejahre wurden folgende  Umgründungsschritte bei <<<Houdek Maschinenbau>>>  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages ...
```

```
... des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die <<<Houdek Maschinenbau>>>  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: ``)

```
Zum Stichtag 31.12.2008 ist die <<<Houdek Maschinenbau>>>  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: ``)

```
... Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der <<<Houdek Maschinenbau>>>, insoweit das auch nach der Abspaltung zum  31.12.2007 bei ...
```

```
... insoweit das auch nach der Abspaltung zum  31.12.2007 bei der <<<Houdek Maschinenbau>>>  verbliebende Vermögen betroffen ist.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `Specific_Org_SUVA`

**F1:** 0.053 | **Precision:** 0.750 | **Recall:** 0.028  

**Format:** `regex`  
**Description:**
Matches Schweizerischen Unfallversicherungsanstalt (SUVA) and SUVA.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)\b|\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.028 | 0.053 | 64 | 48 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 48 | 16 | 937 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Ansatz blieb und die von der Invalidenversicherung sowie der <<<SUVA>>> ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: ``)

```
Die beantragte Steu- erfreiheit der von der <<<SUVA>>> bezogenen Invalidenrente verneinte das Finanzamt indes mit ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: ``)

```
... Teil der Invali- denrente entfallenden Anteiles der von der <<<SUVA>>> einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: ``)

```
... Vertretung ergänzend vor, dass beim  Beschwerdeführer von der <<<SUVA>>> aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: ``)

```
... und Folge- jahre unter Berücksichtigung der gesamten von der <<<SUVA>>> bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (<<<SUVA>>>) sowie einer Pensi- onskassenleistung resultierenden Einkünfte ...
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
... und ursächlichen Umstände des Unfalles, aufgrund  dessen die <<<SUVA>>>-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte, ...
```

FP: `SUVA` (organisation)

```
... Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der <<<SUVA>>>) und des Zusammenhanges mit der Beschäftigung;
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... Unterlagen der <<<SUVA>>> zur Einschätzung des Grades der Behinderung (zB <<<SUVA>>>-Gutach- ten) und die zugrundeliegenden medizinischen Befunde ...
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
... Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die <<<SUVA>>>-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes ...
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
... (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (<<<SUVA>>>) in Höhe von jährlich 56.236,80 CHF.
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

</details>

---

## `Specific_Org_ReinemutSmoch`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches Reinemut + Smoch Handel specifically.

**Content:**
```
\bReinemut\s+\+\s+Smoch\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1224 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. <<<Reinemut + Smoch Handel>>>, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 1** (doc_id: ``)

```
... 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  <<<Reinemut + Smoch Handel>>>  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 2** (doc_id: ``)

```
... des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der <<<Reinemut + Smoch Handel>>>  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 3** (doc_id: ``)

```
Über die <<<Reinemut + Smoch Handel>>>  wird gemäß §§ 28a Abs. 2 und 33 Abs. 5 FinStrG iVm §§ 3-5 ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

**Example 4** (doc_id: ``)

```
... Angelegenheiten verantwortliche Geschäftsführer der Firma  <<<Reinemut + Smoch Handel>>>, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung ...
```

| Predicted | Gold |
|---|---|
| `Reinemut + Smoch Handel` | `Reinemut + Smoch Handel` |

</details>

---

## `Specific_Org_OeGK`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches ÖGK (Österreichische Gesundheitskasse).

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

**Example 0** (doc_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: ``)

```
... die oben  angeführten Abgaben - entsprechend dem Vorgehen der <<<ÖGK>>> - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: ``)

```
... Zuge derselben GPLB angefallen seien,  seien diese seitens der <<<ÖGK>>> der GmbH vorgeschrieben worden, sodass Herr F nicht damit  ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: ``)

```
... in die Databox des EU gerichtet  wurden, die Bescheide der <<<ÖGK>>> allerdings an die GmbH übermittelt wurden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Specific_Org_RoelfsenVersicherung`

**F1:** 0.036 | **Precision:** 1.000 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches Roelfsen Versicherung specifically.

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

**Example 0** (doc_id: ``)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der <<<Roelfsen Versicherung>>>, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: ``)

```
Kff. Sandra Khartchenko  als RNF der <<<Roelfsen Versicherung>>>  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: ``)

```
... betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (<<<Roelfsen Versicherung>>>  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: ``)

```
Bescheidadressaten waren  sowohl das Gruppenmitglied <<<Roelfsen Versicherung>>>  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: ``)

```
... Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die <<<Roelfsen Versicherung>>>  durch Übertragung des  gesamten Betriebes (mit Ausnahme der ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

---

## `Specific_Org_EventSudkraftlex`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches Event Sudkraftlex GMBH specifically.

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

**Example 0** (doc_id: ``)

```
... abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die <<<Event Sudkraftlex GMBH>>>  hinsichtlich der oa.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: ``)

```
... Bescheides gegen den Beschuldigten als Geschäftsführer der <<<Event Sudkraftlex GMBH>>>  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: ``)

```
... handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der <<<Event Sudkraftlex GMBH>>>.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: ``)

```
... der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die <<<Event Sudkraftlex GMBH>>>  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: ``)

```
... MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der <<<Event Sudkraftlex GMBH>>>  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `Specific_Org_X_GmbH`

**F1:** 0.022 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches X GmbH specifically to handle single-letter company names.

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

**Example 0** (doc_id: ``)

```
... 2007 von EUR -882.676,16  vorrangig mit Gewinnen 2007 von der <<<X GmbH>>> verbliebenen Tankstellen (Teilbetrieben) in  Höhe von EUR 1.183.053,01 ...
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |

**Example 1** (doc_id: ``)

```
... also letztlich, weicher Teil des Jahresverlustes 2007  der <<<X GmbH>>> in Anbetracht des § 35 UmgrStG von der <<<X GmbH>>> in den auf das ...
```

```
... Jahresverlustes 2007  der <<<X GmbH>>> in Anbetracht des § 35 UmgrStG von der <<<X GmbH>>> in den auf das Jahr 2007  folgenden Jahren als Verlustvortrag ...
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 2** (doc_id: ``)

```
Für den Revisionsfall folge daraus: Die <<<X GmbH>>> habe - unter Berücksichtigung der unstrittigen  Feststellungen ...
```

```
... entsprechend dem Verursachungszusammenhang auf die bei der  <<<X GmbH>>> verbliebenen und auf die im Wege einer Spaltung auf die R GmbH ...
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

**Example 3** (doc_id: ``)

```
... des Veranlagungsjahres 2007 von 3,632.188,29 EUR durch die <<<X  GmbH>>> erzielt worden sei.
```

| Predicted | Gold |
|---|---|
| `X  GmbH` | `X  GmbH` |

**Example 4** (doc_id: ``)

```
Auch wenn der <<<X GmbH>>> bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X ...
```

```
... GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der <<<X GmbH>>> der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor ...
```

| Predicted | Gold |
|---|---|
| `X GmbH` | `X GmbH` |
| `X GmbH` | `X GmbH` |

</details>

---

## `General_Org_GmbH`

**F1:** 0.021 | **Precision:** 0.264 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches company names ending in GMBH, ensuring the full name is captured by requiring a preceding capitalized word, excluding court/tax terms.

**Content:**
```
(?<!\w)(?<!Arbeitgeber\s)(?<!Firma\s)(?<!Fa\.\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Holding\s)(?<!Services\s)(?<!Unter\s)(?<!Unternehmens\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Elektro\s)(?<!Steuerberatungs\s)(?<!Wirtschaftsprüfung\s)(?<!Bundesfinanzgericht\s)(?<!Finanzamt\s)(?<!Magistrat\s)(?<!Verwaltungsgericht\s)(?<!Verfassungsgericht\s)(?<!Adr\s)(?<!Adresse\s)(?<!Finanzamtes\s)(?<!Finanzamt\s)(?:Die\s+)?([A-Z][a-zA-Z0-9\-]+(?:\s+[A-Z][a-zA-Z0-9\-]+)*\s+GMBH)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.264 | 0.011 | 0.021 | 72 | 19 | 53 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 53 | 1584 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Juni bis Dezember 2017 bereits Verjährung eingetreten und die  <<<KQPC Versand GMBH>>>  im Jänner 2018 nicht mehr tätig gewesen sei.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: ``)

```
Die <<<KQPC Versand GMBH>>>  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten ...
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: ``)

```
... hinsichtlich der Funktion des Beschuldigten (Geschäftsführer <<<Event Sudkraftlex GMBH>>>  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes ...
```

```
... (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer <<<KQPC Versand GMBH>>>) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: ``)

```
... GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), <<<Sudver Handel Services GMBH>>>  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, ...
```

```
... Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und <<<Glanznorost Institut GMBH>>> (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 ...
```

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

**Example 4** (doc_id: ``)

```
... (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  <<<Event Sudkraftlex GMBH>>>  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC <<<Versand GMBH>>>  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, ...
```

FP: `Versand GMBH` (organisation)

**✅ Gold Entities:**
- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Brunhild Katschmareck` (person)
- `KQPC Versand GMBH` (organisation)
- `Spiegelgrundstraße 45, 5061 Vorderfager, Österreich` (address)

**Example 1** (doc_id: ``)

**False Positives:**

```
Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC <<<Versand GMBH>>>  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die ...
```

FP: `Versand GMBH` (organisation)

**✅ Gold Entities:**
- `KQPC Versand GMBH` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event <<<Sudkraftlex GMBH>>>  hinsichtlich der oa.
```

FP: `Sudkraftlex GMBH` (organisation)

**✅ Gold Entities:**
- `Event Sudkraftlex GMBH` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
... Bescheides gegen den Beschuldigten als Geschäftsführer der Event <<<Sudkraftlex GMBH>>>  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung ...
```

FP: `Sudkraftlex GMBH` (organisation)

**✅ Gold Entities:**
- `Event Sudkraftlex GMBH` (organisation)

**Example 4** (doc_id: ``)

**False Positives:**

```
... Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC <<<Versand GMBH>>>  als auch der Event Sudkraftlex GMBH.
```

FP: `Versand GMBH` (organisation)

```
... Geschäftsführer  der KQPC Versand GMBH  als auch der Event <<<Sudkraftlex GMBH>>>.
```

FP: `Sudkraftlex GMBH` (organisation)

**✅ Gold Entities:**
- `KQPC Versand GMBH` (organisation)
- `Event Sudkraftlex GMBH` (organisation)

</details>

---

## `Specific_Org_Universitaet_Wien`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Description:**
Matches Universität Wien specifically.

**Content:**
```
\bUniversit\u00e4t\s+Wien\b
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

**Example 0** (doc_id: ``)

```
... Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der <<<Universität Wien>>> inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: ``)

```
... Sommersemester 2020 das Studium  Rechtswissenschaften an der <<<Universität Wien>>> betrieben.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften (UA101) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 4** (doc_id: ``)

```
... Unterrichtsfächern Biologie und Umweltkunde  und Spanisch an der <<<Universität Wien>>>) bis September 2021 Familienbeihilfe und  Kinderabsetzbeträge.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

## `Specific_Org_WU_Wien`

**F1:** 0.016 | **Precision:** 0.933 | **Recall:** 0.008  

**Format:** `regex`  
**Description:**
Matches WU Wien specifically.

**Content:**
```
\bWU\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.933 | 0.008 | 0.016 | 15 | 14 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 1 | 627 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
 Abgangsbescheinigung der <<<WU Wien>>> vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- ...
```

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 1** (doc_id: ``)

```
... ECTS-Punkten an der JKU Linz absolviert wurden und dass an der <<<WU Wien>>>  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten ...
```

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 2** (doc_id: ``)

```
... der  Beschwerde angekündigte Nachreichung der Unterlagen der <<<WU Wien>>> (Vergleich der  Studienrichtungen).
```

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 3** (doc_id: ``)

```
... es sich bei BA Sozial- und Wirtschaftswissenschaften an der <<<WU  Wien>>> und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium ...
```

| Predicted | Gold |
|---|---|
| `WU  Wien` | `WU  Wien` |

**Example 4** (doc_id: ``)

```
Die von der belangten Behörde angeforderten Angaben der <<<WU Wien>>> wurden mit diesem  Schreiben jedoch nicht vorgelegt.
```

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (<<<WU Wien>>>) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- ...
```

FP: `WU Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

</details>

---

## `Specific_Org_Wirtschaftsuniversitaet_Wien`

**F1:** 0.014 | **Precision:** 0.857 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches Wirtschaftsuniversität Wien and its variations including the parenthetical abbreviation (WU Wien).

**Content:**
```
\bWirtschaftsuniversit\u00e4t\s+Wien(?:\s*\(\s*WU\s+Wien\s*\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.857 | 0.007 | 0.014 | 14 | 12 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 2 | 1663 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
Im Wintersemester 2018/2019 war sie an der <<<Wirtschaftsuniversität Wien>>> inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: ``)

```
Im Wintersemester 2018/2019 war sie an der <<<Wirtschaftsuniversität Wien>>> inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: ``)

```
... 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  <<<Wirtschaftsuniversität Wien>>> in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: ``)

```
... 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  <<<Wirtschaftsuniversität Wien>>> in der Studienrichtung Wirtschaftsrecht inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: ``)

```
Im Wintersemester 2018/2019 war sie an der <<<Wirtschaftsuniversität Wien>>> inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... folgende Unterlagen  vor:   Studienerfolgsnachweis an der <<<Wirtschaftsuniversität Wien>>> (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- ...
```

FP: `Wirtschaftsuniversität Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
... Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der <<<Wirtschaftsuniversität Wien>>> (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der ...
```

FP: `Wirtschaftsuniversität Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

</details>

---

## `Specific_Org_SchmeltzLuftfahrt`

**F1:** 0.013 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches Schmeltz Luftfahrt specifically.

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

**Example 0** (doc_id: ``)

```
... Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die <<<Schmeltz Luftfahrt>>>  übertragen.
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 1** (doc_id: ``)

```
Die <<<Schmeltz Luftfahrt>>>  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag ...
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 2** (doc_id: ``)

```
... Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der <<<Schmeltz Luftfahrt>>> (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 3** (doc_id: ``)

```
Teilbetriebe  <<<Schmeltz Luftfahrt>>>:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau: ...
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 4** (doc_id: ``)

```
Abgespaltene  Tankstellen  <<<Schmeltz Luftfahrt>>> **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte ...
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

</details>

---

## `Specific_Org_JKU_Linz`

**F1:** 0.013 | **Precision:** 0.846 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches JKU Linz specifically.

**Content:**
```
\bJKU\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.846 | 0.006 | 0.013 | 13 | 11 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 2 | 628 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Studienerfolgsnachweis der Johannes Kepler Universität Linz (<<<JKU Linz>>>) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften ...
```

```
... dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der <<<JKU Linz>>> absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen ...
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |
| `JKU Linz` | `JKU Linz` |

**Example 1** (doc_id: ``)

```
 Abgangsbescheinigung der <<<JKU Linz>>> vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften ...
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 2** (doc_id: ``)

```
... Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der <<<JKU Linz>>>  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 3** (doc_id: ``)

```
... Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der <<<JKU Linz>>> aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 4** (doc_id: ``)

```
... UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der <<<JKU Linz>>>.
```

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der <<<JKU Linz>>>  angerechnet wurden
```

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
... abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der <<<JKU Linz>>> angerechnet wurden.
```

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `Specific_Org_MerkurTreuhand`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches Merkur Treuhand Steuerberatung GmbH with flexible whitespace to handle line breaks.

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

**Example 0** (doc_id: ``)

```
... Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch <<<Merkur Treuhand Steuerberatung GmbH>>>, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom 16. ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 1** (doc_id: ``)

```
... bei der belangten Behörde am selben Tage,  übermittelte die <<<Merkur Treuhand Steuerberatung GmbH>>> der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin ...
```

```
... unterfertigte Vollmacht, womit die  Beschwerdeführerin die <<<Merkur Treuhand Steuerberatung GmbH>>> als „Vertreter in allen  steuerlichen, wirtschaftlichen und ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 2** (doc_id: ``)

```
Weiters wurde  der <<<Merkur Treuhand Steuerberatung GmbH>>> darin die Vollmacht „zum Empfang von  Schriftstücken, insbesondere ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 3** (doc_id: ``)

```
Im (Begleit-) Schreiben vom 13.3.2024 führt die <<<Merkur Treuhand Steuerberatung  GmbH>>> aus, dass die Vollmacht als „Spezialvollmacht für das laufende ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung  GmbH` | `Merkur Treuhand Steuerberatung  GmbH` |

**Example 4** (doc_id: ``)

```
... (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  <<<Merkur Treuhand Steuerberatung GmbH>>> weiter.
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

</details>

---

## `Specific_Org_Dorfcon_Verlag`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches Dorfcon-Verlag.

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

**Example 0** (doc_id: ``)

```
... Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit <<<Dorfcon-Verlag>>>  verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 1** (doc_id: ``)

```
Die <<<Dorfcon-Verlag>>>  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz ...
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 2** (doc_id: ``)

```
... Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die <<<Dorfcon-Verlag>>>, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen ...
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 3** (doc_id: ``)

```
... erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und <<<Dorfcon-Verlag>>>  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu ...
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 4** (doc_id: ``)

```
... ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und <<<Dorfcon-Verlag>>>  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen ...
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

</details>

---

## `Specific_Org_Retail_Chains`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches specific retail organizations: Mur Alver OG, Ikea, Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz, Quelle.at.

**Content:**
```
\b(?:Mur\s+Alver\s+OG|Ikea|Obi|Leiner|M(?:ur\s+Alver\s+OG|ö(?:belix|maX))|Otto\.de|xxxLutz|Quelle\.at)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.010 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 1562 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... nicht der Bf als Empfänger aufscheine und eine  Rechnung der „<<<Mur Alver OG>>>“ Leuchten aus dem Luxussegment anführe.
```

| Predicted | Gold |
|---|---|
| `Mur Alver OG` | `Mur Alver OG` |

**Example 1** (doc_id: ``)

```
... Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen <<<Ikea>>>,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at ...
```

```
... waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  <<<Obi>>>, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

```
... Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, <<<Leiner>>>, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

```
... Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, <<<Möbelix>>>, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

```
... von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, <<<MömaX>>>, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |
| `Obi` | `Obi` |
| `Leiner` | `Leiner` |
| `Möbelix` | `Möbelix` |
| `MömaX` | `MömaX` |

</details>

---

## `Specific_Org_LexdonIT`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches Lexdon IT specifically.

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

**Example 0** (doc_id: ``)

```
... übertragende Gesellschaft (neben anderen Gesellschaften) mit der  <<<Lexdon IT>>>  als übernehmende Gesellschaft verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 1** (doc_id: ``)

```
Die <<<Lexdon IT>>>  und  Roelfsen Versicherung  sind aufgrund der dargestellten ...
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 2** (doc_id: ``)

```
... 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die <<<Lexdon IT>>>  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, ...
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 3** (doc_id: ``)

```
Der <<<Lexdon IT>>>  als weiterem partiellen  Gesamtrechtsnachfolger wurde ein ...
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 4** (doc_id: ``)

```
... Rechtsmeinung des Beschwerdeführers geteilt, wonach der bei der  <<<Lexdon IT>>>  im Jahr 2007 insgesamt entstandene Verlust nach Vornahme des ...
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

</details>

---

## `Specific_Org_University_St_Gallen`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches Universität St. Gallen with flexible spacing and optional 'in'.

**Content:**
```
\bUniversit\u00e4t\s+(?:in\s+)?St\.\s+Gallen\b
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

**Example 0** (doc_id: ``)

```
... am … .2000 studiert seit dem Wintersemester 2020/21 an der <<<Universität  in St. Gallen>>> in der Schweiz, das Studium wird ernsthaft und zielstrebig ...
```

| Predicted | Gold |
|---|---|
| `Universität  in St. Gallen` | `Universität  in St. Gallen` |

**Example 1** (doc_id: ``)

```
... Sohn P… (geb. … .00) hat von 2020 bis 2023 erfolgreich an der <<<Universität St. Gallen>>>  studiert.
```

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 2** (doc_id: ``)

```
... Studium hatte sich die Corona-Pandemie für Studierende der <<<Universität St.  Gallen>>> zu Gunsten der Ortsunabhängigkeit der Studierenden ausgewirkt.
```

| Predicted | Gold |
|---|---|
| `Universität St.  Gallen` | `Universität St.  Gallen` |

**Example 3** (doc_id: ``)

```
Außerdem besteht  an der <<<Universität St. Gallen>>> (unabhängig der Pandemie Situation) keine Anwesenheitspflicht.
```

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

**Example 4** (doc_id: ``)

```
... Herbstsemester 2020 für  das Studium der Betriebswirtschaftslehre an der <<<Universität St. Gallen>>> (HSG) in der Schweiz  inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität St. Gallen` | `Universität St. Gallen` |

</details>

---

## `Specific_Org_SENECURA`

**F1:** 0.008 | **Precision:** 0.875 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches SeneCura, SENECURA, Senecura, but NOT if followed by Laurentius Park.

**Content:**
```
\b(?:SeneCura|SENECURA|Senecura)\b(?!(?:\s+Laurentius\s+Park))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.875 | 0.004 | 0.008 | 8 | 7 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 1 | 1317 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
...  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst <<<SENECURA>>> 1.026,29 Euro, Eigenanteil lt Bestätigung <<<SENECURA>>>  3.378,91 ...
```

```
... Hilfsdienst <<<SENECURA>>> 1.026,29 Euro, Eigenanteil lt Bestätigung <<<SENECURA>>>  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |
| `SENECURA` | `SENECURA` |

**Example 1** (doc_id: ``)

```
Für 2017: Mobiler Hilfsdienst <<<SENECURA>>> 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 2** (doc_id: ``)

```
... Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst <<<SENECURA>>>, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 3** (doc_id: ``)

```
... 25.04.2016 (es wurden 4 weitere Rechnungen/Bestätigungen der <<<SeneCura>>>  im Rahmen des Ermittlungsverfahrens von der Bf bzw von deren ...
```

| Predicted | Gold |
|---|---|
| `SeneCura` | `SeneCura` |

**Example 4** (doc_id: ``)

```
... die Bf die Kosten für eine  Besuchshilfe (Mobiler Hilfsdienst <<<Senecura>>>), welcher bereits aber auch in den Jahren, bevor die  Mutter ...
```

| Predicted | Gold |
|---|---|
| `Senecura` | `Senecura` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Dazu wurden von der Bf Bestätigungen der PVA, dem <<<SeneCura>>> Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten ...
```

FP: `SeneCura` (organisation)

**✅ Gold Entities:**
- `PVA` (organisation)
- `SeneCura Laurentius-Park Bludenz` (organisation)

</details>

---

## `Specific_Org_University_of_Bristol`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches University of Bristol.

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

**Example 0** (doc_id: ``)

```
Die Tochter studiert an der <<<University of Bristol>>> bis voraussichtlich Juli 2023.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 1** (doc_id: ``)

```
... getragen hat  und ab September 2020 in einem Studentenwohnheim der <<<University of Bristol>>>.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 2** (doc_id: ``)

```
Am 11. Dezember 2020 bestätigte die <<<University of Bristol>>>, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student ...
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 3** (doc_id: ``)

```
2…7 is studying for a Chemistry (BSc) full time at the <<<University of Bristol>>>.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 4** (doc_id: ``)

```
Miss Maximiliane Sakschewsky, MA … started at the <<<University of Bristol>>> on 28 September 2020 and is  expected to complete her course ...
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

</details>

---

## `Specific_Org_Schabetsberger`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches Schabetsberger Steuerberatung GmbH.

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

**Example 0** (doc_id: ``)

```
... Abgabenschuldner“) wurden der Beschwerdeführerin am 5.4.2024 zu  Handen der <<<Schabetsberger Steuerberatung GmbH>>>, Fischerstiege 9, 1010 Wien, zugestellt.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 1** (doc_id: ``)

```
Die <<<Schabetsberger Steuerberatung GmbH>>> leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 ...
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 2** (doc_id: ``)

```
... Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der <<<Schabetsberger Steuerberatung GmbH>>> die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, ...
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 3** (doc_id: ``)

```
... Vollmachten (daher auch eine allfällige Zustellvollmacht der  <<<Schabetsberger Steuerberatung GmbH>>>) aufgelöst.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 4** (doc_id: ``)

```
Die Zustellung an die <<<Schabetsberger  Steuerberatung GmbH>>> war unwirksam.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger  Steuerberatung GmbH` | `Schabetsberger  Steuerberatung GmbH` |

</details>

---

## `Specific_Org_JKU`

**F1:** 0.007 | **Precision:** 0.286 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches JKU as an abbreviation for Johannes Kepler Universität Linz.

**Content:**
```
\bJKU\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.286 | 0.003 | 0.007 | 21 | 6 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 15 | 633 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der <<<JKU>>> um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: ...
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 1** (doc_id: ``)

```
Siehe Internetseite <<<JKU>>> und WU  Karriereaussichten!
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 2** (doc_id: ``)

```
... Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der <<<JKU>>> um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: ...
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 3** (doc_id: ``)

```
 Beispieldarstellung Übereinstimmung Lehrplan WU mit <<<JKU>>>:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10 ...
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 4** (doc_id: ``)

```
... „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (<<<JKU>>>: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, ...
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Studienerfolgsnachweis der Johannes Kepler Universität Linz (<<<JKU>>> Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften ...
```

FP: `JKU` (organisation)

```
... dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der <<<JKU>>> Linz absolviert wurden und dass an der WU Wien  absolvierte ...
```

FP: `JKU` (organisation)

```
... absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der <<<JKU>>> Linz  angerechnet wurden
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
 Abgangsbescheinigung der <<<JKU>>> Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften ...
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `JKU Linz` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der <<<JKU>>> Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch ...
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
... Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der <<<JKU>>> Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 4** (doc_id: ``)

**False Positives:**

```
... UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der <<<JKU>>> Linz.
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

</details>

---

## `Specific_Org_Verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 0.273 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches Verfassungsgerichtshof (full name) and its genitive form Verfassungsgerichtshofes.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
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

**Example 0** (doc_id: ``)

```
... Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem <<<Verfassungsgerichtshof>>>  oder vor dem Gerichtshof der Europäischen Union.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: ``)

```
... hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim <<<Verfassungsgerichtshof>>> zu stellen.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: ``)

```
... Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  <<<Verfassungsgerichtshof>>> (§ 88a Abs. 2 VfGG) nicht zulässig.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: ``)

```
Darüber hinaus hat der <<<Verfassungsgerichtshof>>> in seinem Beschluss vom 19. September 2025  zu E 1733/2025 ...
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: ``)

```
... unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom <<<Verfassungsgerichtshof>>> geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH ...
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
Der <<<Verfassungsgerichtshof>>> (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen, ...
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``)

**False Positives:**

```
Der <<<Verfassungsgerichtshof>>> ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein ...
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``)

**False Positives:**

```
Dies unter Bezug auf ein Erkenntnis des  <<<Verfassungsgerichtshofes>>> (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
2.4 Zitierte Entscheidung des <<<Verfassungsgerichtshofes>>> gegenständlich nicht einschlägig   Wie das Finanzamt unter ...
```

FP: `Verfassungsgerichtshofes` (organisation)

```
... einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des <<<Verfassungsgerichtshofes>>> (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
Im der  zitierten Entscheidung des <<<Verfassungsgerichtshofes>>> zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `Org_Raiffeisenbank_Karnische`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the specific multi-line bank name Raiffeisenbank Karnische Rion Bankstelle St.Stefan.

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

**Example 0** (doc_id: ``)

```
... Kontoinhaber des Kontos mit der  AT78 2024 1897 7421 2903  bei der <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  sei.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 1** (doc_id: ``)

```
... es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der  <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  um kein ODER-Konto, sondern ein UND-Konto handle.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 2** (doc_id: ``)

```
Der <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  wurde der Bescheid vom 10.10.2022 zugestellt und aufgetragen, ...
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 3** (doc_id: ``)

```
... Kontoinhaber des Kontos mit der AT78 2024 1897 7421 2903  bei der  <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 4** (doc_id: ``)

```
... Beschwerdeführers betreffend  Konto AT78 2024 1897 7421 2903  bei der <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  gründen sich auf die Kontenregisterauskunft.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

</details>

---

## `Specific_Org_PVA`

**F1:** 0.006 | **Precision:** 0.714 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches PVA (Public Pension Insurance) specifically.

**Content:**
```
\bPVA\b
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

**Example 0** (doc_id: ``)

```
... Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der <<<PVA>>> einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 1** (doc_id: ``)

```
Dazu wurden von der Bf Bestätigungen der <<<PVA>>>, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 2** (doc_id: ``)

```
Davon wurde ein Selbstbetrag von der <<<PVA>>> direkt  an den Kostenträger zur teilweisen Deckung der Verpflegungskosten ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 3** (doc_id: ``)

```
... (lt Verständigung über die Leistungshöhe zum 01.01.2017 der <<<PVA>>>  war dies ein Betrag von ca 200,00 bis 230,00 Euro) verblieb ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 4** (doc_id: ``)

```
... insbesondere den angeführten Aktenteilen wie den Bestätigungen der <<<PVA>>>, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, <<<PVA>>>-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).
```

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)
- `SENECURA` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, <<<PVA>>>-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene ...
```

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)

</details>

---

## `Specific_Org_Johannes_Kepler_Universitaet_Linz`

**F1:** 0.006 | **Precision:** 0.625 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches Johannes Kepler Universität Linz and its variations including the parenthetical abbreviation (JKU Linz).

**Content:**
```
\bJohannes\s+Kepler\s+Universit\u00e4t\s+Linz(?:\s*\(\s*JKU\s+Linz\s*\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.625 | 0.003 | 0.006 | 8 | 5 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 3 | 638 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  <<<Johannes Kepler Universität Linz>>>).
```

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 1** (doc_id: ``)

```
... E-Mail des  Zulassungsservices Lehr und Studienorganisation der <<<Johannes Kepler Universität Linz>>> vom  4 von 16 Seite 5 von 16
```

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 2** (doc_id: ``)

```
... E-Mail des Zulassungsservices Lehr- und Studienorganisation der <<<Johannes Kepler  Universität Linz>>> vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria ...
```

| Predicted | Gold |
|---|---|
| `Johannes Kepler  Universität Linz` | `Johannes Kepler  Universität Linz` |

**Example 3** (doc_id: ``)

```
... Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der <<<Johannes Kepler Universität Linz>>> mit dem Wintersemester 2019/2020 einen  Studienwechsel (und ...
```

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 4** (doc_id: ``)

```
... Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der <<<Johannes  Kepler Universität Linz>>> mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel ...
```

| Predicted | Gold |
|---|---|
| `Johannes  Kepler Universität Linz` | `Johannes  Kepler Universität Linz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
 Studienerfolgsnachweis der <<<Johannes Kepler Universität Linz>>> (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften ...
```

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
... 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der <<<Johannes Kepler Universität Linz>>> (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember ...
```

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der <<<Johannes Kepler Universität Linz>>> (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder ...
```

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

</details>

---

## `Specific_Org_LubomirMerschmeyer`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Lubomir Merschmeyer specifically (as organization in this context).

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

**Example 0** (doc_id: ``)

```
... und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der <<<Lubomir Merschmeyer>>>, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch ...
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 1** (doc_id: ``)

```
... Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der <<<Lubomir Merschmeyer>>>
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 2** (doc_id: ``)

```
... Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger <<<Lubomir Merschmeyer>>>  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 3** (doc_id: ``)

```
... Unternehmensgruppe mit dem Gruppenträger Magdalena Diegmueller, LLB (vormals <<<Lubomir Merschmeyer>>>).
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

</details>

---

## `Specific_Org_Berwaldkel_Möbel_AG`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Berwaldkel-Möbel AG specifically.

**Content:**
```
\bBerwaldkel-M\u00f6bel\s+AG\b
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

**Example 0** (doc_id: ``)

```
Das Pendlerpauschale war bereits vom Arbeitgeber <<<Berwaldkel-Möbel AG>>>  berücksichtigt worden, hatte  aber dort wegen der Geringfügigkeit ...
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 1** (doc_id: ``)

```
... Pendlerpauschale  in Höhe von 1.476,00 € gekürzten Einkünfte bei der Fa. <<<Berwaldkel-Möbel AG>>>  in Ansatz gebracht.
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 2** (doc_id: ``)

```
Beigelegt war eine Bestätigung der Firma <<<Berwaldkel-Möbel AG>>>  vom 09.03.2021, wonach die Beschwerdeführerin das Pendlerpauschale ...
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

**Example 3** (doc_id: ``)

```
... dadurch  Berücksichtigung gefunden habe, dass die vom Arbeitgeber <<<Berwaldkel-Möbel AG>>>  übermittelten Einkünfte  schon um das Pendlerpauschale gekürzt ...
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

</details>

---

## `Specific_Org_BankhausDenzel`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Bankhaus Denzel specifically.

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

**Example 0** (doc_id: ``)

```
... Beschwerdeführer eine Reihe von Urkunden, darunter ein Kreditantrag an die <<<Bankhaus Denzel>>>  vom 7.9.2000, einen Kfz-Zulassungsschein und eine Auflistung ...
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 1** (doc_id: ``)

```
... Kreditunterlagen aus dem Jahr 2000 sowie ein Schreiben der <<<Bankhaus Denzel>>>  vom 26.3.2015 vor,  worin ihm mitgeteilt wird, dass auf dem ...
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 2** (doc_id: ``)

```
... Beschwerdeführer einen Kredit über ATS 300.000,00 bei der  <<<Bankhaus Denzel>>>  zum Zwecke eines Hausbaues in Ungarn auf.
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 3** (doc_id: ``)

```
... 7.9.2000, der Selbstauskunft vom 31.8.2001 und  dem Schreiben der <<<Bankhaus Denzel>>>  vom 26.3.2015.
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

</details>

---

## `Specific_Org_Kings_School`

**F1:** 0.005 | **Precision:** 0.800 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches King's School and variations including location suffixes.

**Content:**
```
\b(?:King's\s+School|The\s+King's\s+School(?:\s+[A-Za-z]+)?|The\s+King\u00b4s\s+School(?:\s+[A-Za-z]+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.002 | 0.005 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 1 | 668 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
Dort besuchte Maximiliane Sakschewsky, MA  ab Herbst 2014 das <<<King's School>>>.
```

| Predicted | Gold |
|---|---|
| `King's School` | `King's School` |

**Example 1** (doc_id: ``)

```
... Matura - in England Advanced Level  genannt - noch ein Jahr im <<<King's School>>> absolvieren müssen.
```

| Predicted | Gold |
|---|---|
| `King's School` | `King's School` |

**Example 2** (doc_id: ``)

```
... hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte <<<The King´s School Worcester>>>:  I am writing to confirm that Maximiliane Sakschewsky, MA ...
```

```
... Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of <<<The King's  School Worcester>>> from September 2014 until July 2020.
```

| Predicted | Gold |
|---|---|
| `The King´s School Worcester` | `The King´s School Worcester` |
| `The King's  School Worcester` | `The King's  School Worcester` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der <<<King's School>>> Worcester,  Großbritannien.
```

FP: `King's School` (organisation)

**✅ Gold Entities:**
- `Maximiliane Sakschewsky, MA` (person)
- `King's School Worcester` (organisation)
- `Großbritannien` (country)

</details>

---

## `Specific_Org_GozcuGetränke`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Gözcü Getränke specifically.

**Content:**
```
\bG\u00f6zc\u00fc\s+Getränke\b
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

**Example 0** (doc_id: ``)

```
Ein Firmenbuchauszug vom 9.7.2024 ergab, dass die <<<Gözcü Getränke>>>  seit 15.5.2024 aufgrund  einer Neufassung des Gesellschaftsvertrages ...
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 1** (doc_id: ``)

```
Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum <<<Gözcü Getränke>>>) war im Jahr 2010 Gruppenmittglied  der Unternehmensgruppe ...
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 2** (doc_id: ``)

```
Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum <<<Gözcü Getränke>>>) ist als Rechtsnachfolgerin der  Roelfsen Versicherung  auch ...
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

</details>

---

## `Org_DeloitteTaxWirtschaftsprüfungs`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Deloitte Tax Wirtschaftsprüfungs GmbH.

**Content:**
```
\bDeloitte\s+Tax\s+Wirtschaftspr\u00fcfungs\s+GmbH\b
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

**Example 0** (doc_id: ``)

```
... Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch <<<Deloitte Tax Wirtschaftsprüfungs GmbH>>>, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. ...
```

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

**Example 1** (doc_id: ``)

```
... Tschierweg 3, 9862 Vorderkrems, Österreich  vertreten durch <<<Deloitte Tax Wirtschaftsprüfungs  GmbH>>>, Renngasse/Freyung 1, 1013 Wien, über die Beschwerden gegen ...
```

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs  GmbH` | `Deloitte Tax Wirtschaftsprüfungs  GmbH` |

**Example 2** (doc_id: ``)

```
... Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch <<<Deloitte Tax Wirtschaftsprüfungs GmbH>>>, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. ...
```

| Predicted | Gold |
|---|---|
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | `Deloitte Tax Wirtschaftsprüfungs GmbH` |

</details>

---

## `Specific_Org_Bezirkshauptmannschaft_Bludenz`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches Bezirkshauptmannschaft Bludenz specifically.

**Content:**
```
\bBezirkshauptmannschaft\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1323 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der <<<Bezirkshauptmannschaft Bludenz>>> getragen  werden würden, welche auch die von der PVA einbehaltenen ...
```

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 1** (doc_id: ``)

```
werden und die Heimkosten würden von der <<<Bezirkshauptmannschaft Bludenz>>> getragen.
```

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 2** (doc_id: ``)

```
... welcher nicht  selbst getragen werden konnte, wurde von der <<<Bezirkshauptmannschaft Bludenz>>> getragen.
```

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

</details>

---

## `General_Org_AG`

**F1:** 0.003 | **Precision:** 0.333 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches company names ending in AG, ensuring the full name is captured by requiring a preceding capitalized word, excluding court/tax terms.

**Content:**
```
(?<!\w)(?<!Arbeitgeber\s)(?<!Firma\s)(?<!Fa\.\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Holding\s)(?<!Services\s)(?<!Unter\s)(?<!Unternehmens\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Elektro\s)(?<!Steuerberatungs\s)(?<!Wirtschaftsprüfung\s)(?<!Bundesfinanzgericht\s)(?<!Finanzamt\s)(?<!Magistrat\s)(?<!Verwaltungsgericht\s)(?<!Verfassungsgericht\s)(?<!Adr\s)(?<!Adresse\s)(?<!Finanzamtes\s)(?<!Finanzamt\s)(?:Die\s+)?([A-Z][a-zA-Z0-9\-]+(?:\s+[A-Z][a-zA-Z0-9\-]+)*\s+AG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.002 | 0.003 | 9 | 3 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 6 | 1621 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim <<<Nexkelkel AG>>>, Niederau 25, 6731 Bühl, Österreich  tätig.
```

| Predicted | Gold |
|---|---|
| `Nexkelkel AG` | `Nexkelkel AG` |

**Example 1** (doc_id: ``)

```
... Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim <<<Nexkelkel AG>>>, Niederau 25, 6731 Bühl, Österreich  tätig.
```

| Predicted | Gold |
|---|---|
| `Nexkelkel AG` | `Nexkelkel AG` |

**Example 2** (doc_id: ``)

```
... 3 (siehe Vorschreibung der Kraftfahrversicherung durch die  <<<DA Deutsche Allgemeine Versicherung AG>>> vom Jänner 2006).
```

| Predicted | Gold |
|---|---|
| `DA Deutsche Allgemeine Versicherung AG` | `DA Deutsche Allgemeine Versicherung AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Einkünfte aus nichtselbständiger Arbeit von der  X GmbH in <<<Adr AG>>>.
```

FP: `Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
... Entfernung zwischen der Adresse des Arbeitgebers X GmbH in <<<Adr AG>>> und der  österreichischen Wohnadresse Bf-Adr Ö beträgt weniger ...
```

FP: `Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in <<<Adr AG>>> und der österreichischen Wohnadresse Bf-Adr Ö und der Zeitdauer ...
```

FP: `Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `Bundesministerium für Finanzen` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
Arbeitsstätte (<<<Adr AG>>>).
```

FP: `Adr AG` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
... streitgegenständlichen Jahren  als Monteur bei der Cervenka&Neunübel <<<Telekom AG>>>, unselbstständig erwerbstätig.
```

FP: `Telekom AG` (organisation)

**✅ Gold Entities:**
- `Cervenka&Neunübel Telekom AG` (organisation)

</details>

---

## `Specific_Org_WU`

**F1:** 0.003 | **Precision:** 0.158 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches WU as an abbreviation for Wirtschaftsuniversität Wien.

**Content:**
```
\bWU\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.158 | 0.002 | 0.003 | 19 | 3 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 16 | 638 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
Siehe Internetseite JKU und <<<WU>>>  Karriereaussichten!
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 1** (doc_id: ``)

```
 Beispieldarstellung Übereinstimmung Lehrplan <<<WU>>> mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, ...
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

**Example 2** (doc_id: ``)

```
... sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (<<<WU>>>: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“, ...
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (<<<WU>>> Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
 Abgangsbescheinigung der <<<WU>>> Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
... ECTS-Punkten an der JKU Linz absolviert wurden und dass an der <<<WU>>> Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
... der  Beschwerde angekündigte Nachreichung der Unterlagen der <<<WU>>> Wien (Vergleich der  Studienrichtungen).
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 4** (doc_id: ``)

**False Positives:**

```
... es sich bei BA Sozial- und Wirtschaftswissenschaften an der <<<WU>>>  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

</details>

---

## `Specific_Org_CervenkaNeunubel`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Cervenka&Neunübel Telekom AG specifically.

**Content:**
```
\bCervenka\&Neunübel\s+Telekom\s+AG\b
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

**Example 0** (doc_id: ``)

```
... noch in den streitgegenständlichen Jahren  als Monteur bei der <<<Cervenka&Neunübel Telekom AG>>>, unselbstständig erwerbstätig.
```

| Predicted | Gold |
|---|---|
| `Cervenka&Neunübel Telekom AG` | `Cervenka&Neunübel Telekom AG` |

**Example 1** (doc_id: ``)

```
... geleisteten Kostenersätzen gründen sich auf das Schreiben  der <<<Cervenka&Neunübel Telekom AG>>>  vom 9.6.2016 sowie die mit diesem Schreiben übermittelten ...
```

| Predicted | Gold |
|---|---|
| `Cervenka&Neunübel Telekom AG` | `Cervenka&Neunübel Telekom AG` |

</details>

---

## `Specific_Org_HLFTourismus`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Höhere Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit and its abbreviation HLF.

**Content:**
```
\b(?:H\u00f6here\s+Lehranstalt\s+f\u00fcr\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit|HLF\s+(?:Krems/Donau|Krems))\b
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

**Example 0** (doc_id: ``)

```
... Beschwerdeführerin bezog für die Tochter T., geb. 2003, wegen Schulbesuch (<<<Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit>>> in Krems) bis Juni 2022  Familienbeihilfe.
```

| Predicted | Gold |
|---|---|
| `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` | `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` |

**Example 1** (doc_id: ``)

```
... 23.03.2023, vor, dass ihre  Tochter T. am 30.05.2022 an der <<<HLF Krems/Donau>>> maturiert habe und damit in die alte  2 von 6 Seite 3 von 6
```

| Predicted | Gold |
|---|---|
| `HLF Krems/Donau` | `HLF Krems/Donau` |

</details>

---

## `Specific_Org_Mag_Ghesla`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Mag. Ghesla Steuerberater GmbH.

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

**Example 0** (doc_id: ``)

```
... Penken 55, 4903 Hofmanning, Österreich, vertreten durch die <<<Mag. Ghesla Steuerberater GmbH>>>, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen ...
```

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: ``)

```
... Penken 55, 4903 Hofmanning, Österreich, vertreten durch die <<<Mag. Ghesla Steuerberater GmbH>>>, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen ...
```

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

</details>

---

## `Specific_Org_England`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches England as an organization in this context.

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

**Example 0** (doc_id: ``)

```
... MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in <<<England>>> Advanced Level  genannt - noch ein Jahr im King's School absolvieren ...
```

| Predicted | Gold |
|---|---|
| `England` | `England` |

**Example 1** (doc_id: ``)

```
... wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in <<<England>>>).
```

| Predicted | Gold |
|---|---|
| `England` | `England` |

</details>

---

## `Specific_Org_R_GmbH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches R GmbH specifically.

**Content:**
```
\bR\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1466 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... GmbH verbliebenen und auf die im Wege einer Spaltung auf die <<<R GmbH>>> übergegangenen  Tankstellen aufzuteilen sei.
```

| Predicted | Gold |
|---|---|
| `R GmbH` | `R GmbH` |

**Example 1** (doc_id: ``)

```
... GmbH verbliebenen und auf die im Wege einer Spaltung auf die <<<R GmbH>>> übergegangenen  Tankstellen aufzuteilen ist.
```

| Predicted | Gold |
|---|---|
| `R GmbH` | `R GmbH` |

</details>

---

## `Specific_Org_OeBB`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches ÖBB (Austrian Federal Railways).

**Content:**
```
\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1315 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... welche die Tochter zusätzlich noch übernommen hatte (Fahrkarten <<<ÖBB>>> für Besuche,  Betriebskosten der Wohnung in Bludenz, Depotgeld ...
```

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 1** (doc_id: ``)

```
... geltend gemachten Besuchskosten wie für die Jahreskarten der <<<ÖBB>>> sowie der  einzelnen Bahn- oder Bustickets bzw Taxirechnungen ...
```

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

</details>

---

## `Specific_Org_SeneCura_Laurentius_Park_Bludenz`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches SeneCura Laurentius Park Bludenz with flexible spacing.

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

**Example 0** (doc_id: ``)

```
... der Bf war in den streitgegenständlichen Jahren im Pflegeheim <<<SeneCura Laurentius  Park Bludenz>>> (beginnend ab 28.01.2016) untergebracht.
```

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius  Park Bludenz` | `SeneCura Laurentius  Park Bludenz` |

**Example 1** (doc_id: ``)

```
... angeführten Aktenteilen wie den Bestätigungen der PVA, des <<<SeneCura  Laurentius Park Bludenz>>> und den Kontoauszügen.
```

| Predicted | Gold |
|---|---|
| `SeneCura  Laurentius Park Bludenz` | `SeneCura  Laurentius Park Bludenz` |

</details>

---

## `Specific_Org_FinanzamtKlosterneuburg`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Finanzamt Klosterneuburg specifically.

**Content:**
```
\bFinanzamt\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 397 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... 2025 gegen die Bescheide  gemäß §§ 15 und 16 COFAG-NoAG des <<<Finanzamt Klosterneuburg>>>  6. August 2025 betreffend Rückerstattung  zum Fördervertrag ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Klosterneuburg` | `Finanzamt Klosterneuburg` |

</details>

---

## `Org_AMS_Oesterreich`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches AMS Österreich and Arbeitsmarktservice (AMS).

**Content:**
```
\b(?:AMS\s+Österreich|Arbeitsmarktservice\s*\(AMS\))\b
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

**Example 0** (doc_id: ``)

```
Entscheidungsgründe  I. Verfahrensgang  Aufgrund einer vom <<<AMS Österreich>>> der Abgabenbehörde übermittelten korrigierten  Mitteilung nahm ...
```

| Predicted | Gold |
|---|---|
| `AMS Österreich` | `AMS Österreich` |

</details>

---

## `Specific_Org_TschurtschenthalerWalderFister`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH

**Content:**
```
\bTschurtschenthaler,\s*Walder,\s*Fister\s+Rechtsanwälte\s+GmbH\b
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

**Example 0** (doc_id: ``)

```
... Frauengasse 2, 3180 Hintereben, Österreich  vertreten durch <<<Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH>>>, Dr. Arthur Lemisch Platz 7, 9020 Klagenfurt, über die Beschwerde ...
```

| Predicted | Gold |
|---|---|
| `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH` | `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH` |

</details>

---

## `Specific_Org_Hamburger_Fern_Hochschule`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Hamburger Fern-Hochschule specifically.

**Content:**
```
\bHamburger\s+Fern-Hochschule\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 633 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
 Studienerfolgsnachweis der <<<Hamburger Fern-Hochschule>>> betreffend den Studiengang  Betriebswirtschaft für HAK-Absolventen ...
```

| Predicted | Gold |
|---|---|
| `Hamburger Fern-Hochschule` | `Hamburger Fern-Hochschule` |

</details>

---

## `Org_Finanzamt_Grossbetriebe`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Finanzamt für Großbetriebe.

**Content:**
```
\bFinanzamt\s+f\u00fcr\s+Gro\u00dfbetriebe\b
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

**Example 0** (doc_id: ``)

```
... Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  <<<Finanzamt für Großbetriebe>>> (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `Finanzamt für Großbetriebe` | `Finanzamt für Großbetriebe` |

</details>

---

## `Specific_Org_Garanta_VersicherungsAG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Garanta VersicherungsAG (no space before AG).

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

**Example 0** (doc_id: ``)

```
... wurden eine Versicherungsbestätigung zur Mobilitätsgarantie  der <<<Garanta VersicherungsAG>>> (undatiert) für den Zeitraum 26.08.2011 bis 25.08.2012 für ...
```

| Predicted | Gold |
|---|---|
| `Garanta VersicherungsAG` | `Garanta VersicherungsAG` |

</details>

---

## `Specific_Org_Sivananda`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches The International Sivananda Yoga Vedanta Centre.

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

**Example 0** (doc_id: ``)

```
... der Beschwerdeführerin  und eine englische Bestätigung des <<<The International Sivananda Yoga Vedanta Centre>>> in  Canada vom 24.05.2003, in der die Beschwerdeführerin als ...
```

| Predicted | Gold |
|---|---|
| `The International Sivananda Yoga Vedanta Centre` | `The International Sivananda Yoga Vedanta Centre` |

</details>

---

## `Specific_Org_AVED`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches AVED cosmetic.

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

**Example 0** (doc_id: ``)

```
... Bundesfinanzgericht wurde ein Zahlungsnachweis der Kosten der Firma  <<<AVED cosmetic>>> iHv € 975,48 nicht vorgelegt.
```

| Predicted | Gold |
|---|---|
| `AVED cosmetic` | `AVED cosmetic` |

</details>

---

## `Specific_Org_Yoga_Vidya`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Yoga Vidya GmbH.

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

**Example 0** (doc_id: ``)

```
... sich laut der vorgelegten Abrechnung vom 19.10.2006  von der <<<Yoga Vidya GmbH>>> um jeweils eine Anwendung Abhyanga, Garshan, kleine Abhyanga, ...
```

| Predicted | Gold |
|---|---|
| `Yoga Vidya GmbH` | `Yoga Vidya GmbH` |

</details>

---

## `Specific_Org_Geschenkartikel`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Geschenkartikel GmbH.

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

**Example 0** (doc_id: ``)

```
... Arbeitsmittel (ohne Massageliege) iHv € 1.213,81 vorliegt (Rechnung <<<Geschenkartikel GmbH>>> €  92,73;
```

| Predicted | Gold |
|---|---|
| `Geschenkartikel GmbH` | `Geschenkartikel GmbH` |

</details>

---

## `Specific_Org_Hallas_Partner`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, handling newlines.

**Content:**
```
\bHallas\s+&\s+Partner\s+Wirtschaftspr\u00fcfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
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

**Example 0** (doc_id: ``)

```
... Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch <<<Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG>>>, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November ...
```

| Predicted | Gold |
|---|---|
| `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` | `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` |

</details>

---

## `Specific_Org_LeitnerLeitner`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater.

**Content:**
```
\bLeitnerLeitner\s+GmbH\s+Wirtschaftspr\u00fcfer\s+und\s+Steuerberater\b
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

**Example 0** (doc_id: ``)

```
... Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  <<<LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater>>>, Ottensheimer Straße 32,  4040 Linz,
```

| Predicted | Gold |
|---|---|
| `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` | `LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater` |

</details>

---

## `Specific_Org_Betriebsprüfung_GmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Betriebsprüfung GmbH specifically.

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

**Example 0** (doc_id: ``)

```
Nach Ansicht der <<<Betriebsprüfung GmbH>>> das Finanzamt müsse der gesamte im Jahr 2007  erwirtschaftete ...
```

| Predicted | Gold |
|---|---|
| `Betriebsprüfung GmbH` | `Betriebsprüfung GmbH` |

</details>

---

## `Specific_Org_TritriIT`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Tritri-IT specifically.

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

**Example 0** (doc_id: ``)

```
... Vollständigkeit halber  wird angemerkt, dass damals alle Beschwerden des <<<Tritri-IT>>> -Konzernes durch denselben  Richter beim BFG entschieden wurden).
```

| Predicted | Gold |
|---|---|
| `Tritri-IT` | `Tritri-IT` |

</details>

---

## `Specific_Org_AnwalteMandlMitterbauer`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Anwälte Mandl & Mitterbauer GmbH specifically.

**Content:**
```
\bAnwälte\s+Mandl\s+&\s+Mitterbauer\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1293 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch <<<Anwälte Mandl & Mitterbauer GmbH>>>, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. ...
```

| Predicted | Gold |
|---|---|
| `Anwälte Mandl & Mitterbauer GmbH` | `Anwälte Mandl & Mitterbauer GmbH` |

</details>

---

## `Specific_Org_InnMarine`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches InnMarine GMBH specifically.

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

**Example 0** (doc_id: ``)

```
... Beschwerdeführer gemäß § 9a BAO für die  aushaftenden Abgabenschulden der <<<InnMarine GMBH>>> (Primärschuldnerin) im Ausmaß von  € 99.885,72 in Anspruch ...
```

| Predicted | Gold |
|---|---|
| `InnMarine GMBH` | `InnMarine GMBH` |

</details>

---

## `Specific_Org_Krankenpflegevereins_Bludenz`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Krankenpflegevereins Bludenz.

**Content:**
```
\bKrankenpflegevereins\s+Bludenz\b
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

**Example 0** (doc_id: ``)

```
Die Kosten lt Bestätigungen des <<<Krankenpflegevereins  Bludenz>>> (welche auch mittels Kontoauszüge nachgewiesen wurden) iHv ...
```

| Predicted | Gold |
|---|---|
| `Krankenpflegevereins  Bludenz` | `Krankenpflegevereins  Bludenz` |

</details>

---

## `Specific_Org_Verwaltungsgericht_Wien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Verwaltungsgericht Wien.

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

**Example 0** (doc_id: ``)

```
... erhebe ich hiermit das Rechtsmittel der Beschwerde an das  <<<Verwaltungsgericht Wien>>>.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

</details>

---

## `Specific_Org_TAXCOACH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, handling potential newlines.

**Content:**
```
\bTAXCOACH\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 131 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Halauska-Straße 7, 9544 Wiesen, Österreich, vertreten durch <<<TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG>>>, Muthgasse 109, 1190 Wien, über deren Beschwerde vom  3. Dezember ...
```

| Predicted | Gold |
|---|---|
| `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` | `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` |

</details>

---

## `Specific_Org_MusikhochschuleWien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Musikhochschule Wien specifically.

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

**Example 0** (doc_id: ``)

```
... Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der <<<Musikhochschule Wien>>> und am Konservatorium  der Stadt Wien klassisches Schlagwerk ...
```

| Predicted | Gold |
|---|---|
| `Musikhochschule Wien` | `Musikhochschule Wien` |

</details>

---

## `Specific_Org_KonservatoriumStadtWien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Konservatorium der Stadt Wien specifically.

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

**Example 0** (doc_id: ``)

```
... Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am <<<Konservatorium  der Stadt Wien>>> klassisches Schlagwerk sowie Theorie und Komposition an der ...
```

| Predicted | Gold |
|---|---|
| `Konservatorium  der Stadt Wien` | `Konservatorium  der Stadt Wien` |

</details>

---

## `Specific_Org_WienerPhilharmoniker`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Wiener Philharmoniker specifically.

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

**Example 0** (doc_id: ``)

```
... Verwaltungsgerichtshof in seinem einen Berufsmusiker und Mitglied der <<<Wiener  Philharmoniker>>> betreffenden, Erkenntnis vom 21. September 2005, 2001/13/0241, ...
```

| Predicted | Gold |
|---|---|
| `Wiener  Philharmoniker` | `Wiener  Philharmoniker` |

</details>

---

## `Court_Bezirksgericht`

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches District Courts, stopping at whitespace or punctuation.

**Content:**
```
\bBezirksgericht\s+[A-Za-z0-9\-]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.001 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 995 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
ihrem Ehemann nach meiner Einwilligung vor dem <<<Bezirksgericht Purkersdorf>>> - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 ...
```

| Predicted | Gold |
|---|---|
| `Bezirksgericht Purkersdorf` | `Bezirksgericht Purkersdorf` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... 18.10.2022 Beschwerde ein,  und führte begründend aus, das <<<Bezirksgericht Favoriten>>> habe am TT.06.2022 eine  offenkundige Zahlungsunfähigkeit beschlossen ...
```

FP: `Bezirksgericht Favoriten` (organisation)

**✅ Gold Entities:**

</details>

---

## `Specific_Org_Kings_School_Worcester`

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches King's School Worcester specifically.

**Content:**
```
\bKing's\s+School\s+Worcester\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.001 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 666 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der <<<King's School Worcester>>>,  Großbritannien.
```

| Predicted | Gold |
|---|---|
| `King's School Worcester` | `King's School Worcester` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The <<<King's  School Worcester>>> from September 2014 until July 2020.
```

FP: `King's  School Worcester` (organisation)

**✅ Gold Entities:**
- `The King´s School Worcester` (organisation)
- `Maximiliane Sakschewsky, MA` (person)
- `The King's  School Worcester` (organisation)

</details>

---

## `Specific_Org_SeneCura_Laurentius_Park`

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches SeneCura Laurentius Park (without Bludenz) with flexible spacing.

**Content:**
```
\bSeneCura\s+Laurentius\s+Park\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 1314 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
... lebte in Wien, die Mutter der Bf war in Bludenz im Pflegeheim <<<SeneCura Laurentius Park>>>  untergebracht.
```

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius Park` | `SeneCura Laurentius Park` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... der Bf war in den streitgegenständlichen Jahren im Pflegeheim <<<SeneCura Laurentius  Park>>> Bludenz (beginnend ab 28.01.2016) untergebracht.
```

FP: `SeneCura Laurentius  Park` (organisation)

**✅ Gold Entities:**
- `SeneCura Laurentius  Park Bludenz` (organisation)

**Example 1** (doc_id: ``)

**False Positives:**

```
... angeführten Aktenteilen wie den Bestätigungen der PVA, des <<<SeneCura  Laurentius Park>>> Bludenz und den Kontoauszügen.
```

FP: `SeneCura  Laurentius Park` (organisation)

**✅ Gold Entities:**
- `PVA` (organisation)
- `SeneCura  Laurentius Park Bludenz` (organisation)

</details>

---

## `Specific_Org_MerkurTreuhand_NoGmbH`

**F1:** 0.001 | **Precision:** 0.091 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches Merkur Treuhand Steuerberatung without GmbH suffix (for cases where GmbH is missing or split).

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.091 | 0.001 | 0.001 | 11 | 1 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 10 | 34 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: ``)

```
Dass die Bescheide (lediglich) per E-Mail an die <<<Merkur Treuhand  Steuerberatung>>> weitergeleitet wurden, hat diese über Aufforderung des Bundesfinanzgerichtes ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand  Steuerberatung` | `Merkur Treuhand  Steuerberatung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch <<<Merkur Treuhand Steuerberatung>>> GmbH, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Univ.-Prof. Hartwig Boehler` (person)
- `DDr.in Josepha de Haan` (person)
- `Oisching 129, 3071 Wiesen, Österreich` (address)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)
- `St.-Veit-Gasse 50,  1130 Wien` (address)
- `Finanzamtes  Österreich` (organisation)
- `01-186/7053` (tax_number)

**Example 1** (doc_id: ``)

**False Positives:**

```
... bei der belangten Behörde am selben Tage,  übermittelte die <<<Merkur Treuhand Steuerberatung>>> GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

```
... unterfertigte Vollmacht, womit die  Beschwerdeführerin die <<<Merkur Treuhand Steuerberatung>>> GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 2** (doc_id: ``)

**False Positives:**

```
Weiters wurde  der <<<Merkur Treuhand Steuerberatung>>> GmbH darin die Vollmacht „zum Empfang von  Schriftstücken, ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
Im (Begleit-) Schreiben vom 13.3.2024 führt die <<<Merkur Treuhand Steuerberatung>>>  GmbH aus, dass die Vollmacht als „Spezialvollmacht für das ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung  GmbH` (organisation)

**Example 4** (doc_id: ``)

**False Positives:**

```
... (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  <<<Merkur Treuhand Steuerberatung>>> GmbH weiter.
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

</details>

---

## `Court_Landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Regional Courts (Landesgericht) and its abbreviation LG, ensuring it captures the full location including 'für [Location]' patterns but stops before dates or 'vom'.

**Content:**
```
\b(?:Landesgericht|LG)\s+(?:f\u00fcr\s+)?[A-Za-z0-9\-]+(?:\s+[A-Za-z0-9\-]+)*(?=\s+(?:vom|am|vom\s+\d+|am\s+\d+)|$|[,;])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_EnnsBildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches EnnsBildung specifically.

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

## `Specific_Org_KornfelderRecycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Kornfelder Recycling specifically.

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

## `Specific_Org_SeeGarttalder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches See Garttalder specifically.

**Content:**
```
\bSee\s+Garttalder\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_WaldTouristik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches WaldTouristik Technologien specifically.

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

## `Specific_Org_GetränkeNexdorfzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Getränke Nexdorfzor GMBH specifically.

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

## `Specific_Org_OkurAutomotive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Okur Automotive specifically (without KG suffix to avoid over-matching).

**Content:**
```
\bOkur\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_CelikkanatGarten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Celikkanat Garten specifically (without KG suffix to avoid over-matching).

**Content:**
```
\bCelikkanat\s+Garten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_YXTG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches YXTG Maschinenbau specifically.

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

## `Specific_Org_Yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Yavasoglu Analyse AG specifically.

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

## `Specific_Org_KlusnerPaffgen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Klusner&Päffgen Bildung GMBH specifically.

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

## `Specific_Org_TschermackPharma`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Tschermack Pharma GMBH specifically.

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

## `Specific_Org_GrönemeierHövelberndt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Grönemeier&Hövelberndt E-Commerce specifically.

**Content:**
```
\bGr\u00f6nemeier\&H\u00f6velberndt\s+E\u2011Commerce\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_DrauFinanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches DrauFinanzen specifically.

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

## `Specific_Org_DonauDruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Donau-Druck specifically.

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

## `Specific_Org_AnnemieBott`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Annemie Bott specifically.

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

## `Specific_Org_StadtEnergie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches StadtEnergie Holding specifically.

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

## `Specific_Org_Triloglex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Triloglex GMBH specifically.

**Content:**
```
\bTriloglex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_Sievens`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Sievens Automotive GMBH specifically.

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

## `Specific_Org_NordDruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Nord-Druck GMBH specifically.

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

## `Specific_Org_OstGetränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches OstGetränke GMBH specifically.

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

## `Specific_Org_MilanHändlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Milan Händlein specifically.

**Content:**
```
\bMilan\s+H\u00e4ndlein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_SünrammDruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Sünramm Druck specifically.

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

## `Specific_Org_SüdNortri`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Süd Nortri specifically.

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

## `Specific_Org_KraftverGastronomie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Kraftver-Gastronomie GMBH specifically.

**Content:**
```
\bKraftver\-Gastronomie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_InnLuftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches InnLuftfahrt GMBH specifically.

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

## `Specific_Org_HochLebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches HochLebensmittel Holding GMBH specifically.

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

## `Specific_Org_MittelHeizungWerke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches MittelHeizung Werke AG specifically.

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

## `Specific_Org_VossbeinLebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Vossbein Lebensmittel specifically.

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

## `Specific_Org_RheinDigital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches RheinDigital specifically.

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

## `Specific_Org_KokHeberlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Kök & Heberlein Bau specifically.

**Content:**
```
\bKök\s+&\s+Heberlein\s+Bau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_LeissSoftware`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Leiss Software specifically.

**Content:**
```
\bLeiss\s+Software\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_PastlBachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Pastl+Bächle Handel specifically.

**Content:**
```
\bPastl\+Bächle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_WaldtraSicherheit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Waldtra-Sicherheit specifically.

**Content:**
```
\bWaldtra\-Sicherheit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_Zoruniglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Zoruniglanz specifically.

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

## `Specific_Org_AlalMedien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Alal-Medien specifically.

**Content:**
```
\bAlal\-Medien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_PastelPharma`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Pastel Pharma specifically.

**Content:**
```
\bPastel\s+Pharma\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_ElenderCloud`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Elender Cloud specifically.

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

## `Specific_Org_TextilSteingartlog`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Textil Steingartlog specifically.

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

## `Specific_Org_NowothnigWind`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Nowothnig Wind specifically.

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

## `Specific_Org_FinanzenTradonnex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzen Tradonnex specifically.

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

## `Specific_Org_GartgartDienstleistungen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Gartgart Dienstleistungen specifically.

**Content:**
```
\bGartgart\s+Dienstleistungen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_SanitärTalter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Sanitär Talder specifically.

**Content:**
```
\bSanitär\s+Talter\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_BludszatMaschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Bludszat Maschinenbau specifically.

**Content:**
```
\bBludszat\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_RaiffeisenbankWelsSüd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenbank Wels Süd specifically.

**Content:**
```
\bRaiffeisenbank\s+Wels\s+Süd\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_BauermeisterGetränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Bauermeister Getränke specifically.

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

## `Specific_Org_NordKellex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Nord Kellex specifically.

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

## `Specific_Org_KrolitzkiBeratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Krolitzki Beratung specifically.

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

## `Specific_Org_ForschungWaldlemtal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Forschung Waldlemtal specifically.

**Content:**
```
\bForschung\s+Waldlemtal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_ManfredoHerrschmann`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Manfredo Herrschmann specifically.

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

## `Specific_Org_RuterborriesFriderichMöbel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Rüterborries+Friderich Möbel specifically.

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

## `Specific_Org_VolksbankWien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches VOLKSBANK WIEN specifically.

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

## `Specific_Org_GartgartDienstleistungenGMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Gartgart Dienstleistungen GMBH specifically.

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

## `Specific_Org_EnergieSynlexder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Energie Synlexder specifically.

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

## `Specific_Org_ChenSetzekorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Chen Setzekorn specifically.

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

## `Specific_Org_SüdLemkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Süd Lemkel specifically.

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

## `Specific_Org_SteinfurtglanzLandwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Steinfurtglanz-Landwirtschaft specifically.

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

## `Specific_Org_KubzykElektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches /Kubzyk Elektro AG specifically to handle the leading slash.

**Content:**
```
/Kubzyk\s+Elektro\s+AG
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_StarkerBeratung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Starker Beratung specifically.

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

## `Specific_Org_FHKaernten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches FH Kärnten specifically.

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

## `Specific_Org_FachhochschuleKaernten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Fachhochschule Kärnten specifically.

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

## `Specific_Org_KarlFranzensUniversitaetGraz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Karl-Franzens- Universität Graz specifically.

**Content:**
```
\bKarl-Franzens-\s+Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_BGmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches B-GmbH specifically.

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

## `Specific_Org_AGmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches A-GmbH specifically.

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

## `Specific_Org_HausverwaltungGmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Hausverwaltung-GmbH specifically (hyphenated).

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

## `General_Org_KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in KG, excluding common preceding nouns like Arbeitgeber, Firma, Fa.

**Content:**
```
(?<!\w)(?<!Arbeitgeber\s)(?<!Firma\s)(?<!Fa\.\s)(?<!der\s)(?<!die\s)(?<!das\s)(?:Die\s+)?([A-Z][a-zA-Z0-9\-]+(?:\s+[A-Z][a-zA-Z0-9\-]+)*\s+KG)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 5 | 1615 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. <<<MITTERER KG>>>,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde ...
```

FP: `MITTERER KG` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `James Grentz` (person)
- `Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich` (address)
- `T & M TRAUNSTEINER U. MITTERER KG` (organisation)
- `Schubertviertel 38, 4300 St.Valentin` (address)
- `Finanzamtes Österreich` (organisation)
- `90-523/9682` (tax_number)

**Example 1** (doc_id: ``)

**False Positives:**

```
... Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & <<<Co KG>>>, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November ...
```

FP: `Co KG` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Ferdinand Mielnickel` (person)
- `Viertelweg 16, 3720 Gaindorf, Österreich` (address)
- `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` (organisation)
- `Praterstraße 38, 1020 Wien` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt  Österreich` (organisation)
- `86-167/7419` (tax_number)

**Example 2** (doc_id: ``)

**False Positives:**

```
... Österreich, vertreten durch Grazer Treuhand Steuerberatung GmbH & <<<Partner KG>>>,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 ...
```

FP: `Partner KG` (organisation)

**✅ Gold Entities:**
- `Univ.-Prof. Maximilian Karrer` (person)
- `VetR Tosca Buecher` (person)
- `Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich` (address)
- `Grazer Treuhand Steuerberatung GmbH & Partner KG` (organisation)
- `Petersgasse 128a, 8010 Graz` (address)
- `Finanzamts Graz-Stadt` (organisation)
- `Finanzamts Graz- Stadt` (organisation)

**Example 3** (doc_id: ``)

**False Positives:**

```
... Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. <<<MITTERER KG>>>,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde ...
```

FP: `MITTERER KG` (organisation)

**✅ Gold Entities:**
- `Dr. Hans Blasina` (person)
- `James Grentz` (person)
- `Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich` (address)
- `T & M TRAUNSTEINER U. MITTERER KG` (organisation)
- `Schubertviertel 38, 4300 St.Valentin` (address)
- `Finanzamtes Österreich` (organisation)
- `90-523/9682` (tax_number)

**Example 4** (doc_id: ``)

**False Positives:**

```
... durch TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & <<<Co KG>>>, Muthgasse 109, 1190 Wien, über deren Beschwerde vom  3. Dezember ...
```

FP: `Co KG` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Oleg Peltzmann, Bakk. techn.` (person)
- `Ludwig Halauska-Straße 7, 9544 Wiesen, Österreich` (address)
- `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` (organisation)
- `Muthgasse 109, 1190 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `94-582/7899` (tax_number)

</details>

---

## `Specific_Org_FinanzamtSalzburgStadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt Salzburg-Stadt specifically.

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

## `Org_Bundesministers_Arbeit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Bundesministers für Arbeit, Soziales und Konsumentenschutz.

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

## `Specific_Org_Raiffeisenbank_Stallhofen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenbank Stallhofen specifically.

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

## `Specific_Org_BDO_Austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches BDO Austria GmbH WP- u. StBges.

**Content:**
```
\bBDO\s+Austria\s+GmbH\s+WP-\s+u\.\s+StBges\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_GreinerMaiEvent`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Greiner-Mai Event specifically.

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

## `Specific_Org_DLCG_Bildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches DLCG Bildung specifically.

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

## `Specific_Org_DGCV_ECommerce`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches DGCV E-Commerce GMBH specifically.

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

## `Specific_Org_Unter_Donunisee`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Unter Donunisee AG specifically.

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

## `Specific_Org_LondonFilmAcademy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches London Film Academy and common typo London Film Acadamy.

**Content:**
```
\bLondon\s+Film\s+(?:Academy|Acadamy)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_Bundeskanzleramt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Bundeskanzleramt and its genitive form Bundeskanzleramtes.

**Content:**
```
\bBundeskanzler(?:amt|amtes)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_Bundesministeriums_Fuer_Justiz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Bundesministeriums für Justiz specifically.

**Content:**
```
\bBundesministeriums\s+f\u00fcr\s+Justiz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_SaxingerChalupsky`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Saxinger Chalupsky & Partner Rechtsanwälte GmbH specifically.

**Content:**
```
\bSaxinger\s+Chalupsky\s+&\s+Partner\s+Rechtsanw\u00e4lte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_Verwaltungsgerichtshof_Parenthetical`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Verwaltungsgerichtshofes (VwGH) as a single entity.

**Content:**
```
\bVerwaltungsgerichtshof(?:es)?\s*\(\s*VwGH\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_Imre_Schaffer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Imre & Schaffer Rechtsanwälte OG specifically.

**Content:**
```
\bImre\s+&\s+Schaffer\s+Rechtsanw\u00e4lte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_Talwerk_Logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Talwerk Logistik Holding GMBH specifically to prevent truncation by general GmbH rule.

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

## `Specific_Org_BKSSteuerberatung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches BKS Steuerberatung GmbH & Co KG specifically.

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

## `Specific_Org_OBUG_Nikolaus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific long organization name including quotes and hyphenated description.

**Content:**
```
\b"\u00d6BUG"\s+DR\.\s+NIKOLAUS\s+Wirtschaftstreuhand\s+GmbH\s*-\s*Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Org_FA_Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt abbreviations (FA) followed by location names (e.g., FA Spittal Villach, FA Salzburg-Stadt, FA Landeck Reutte).

**Content:**
```
\bFA\s+[A-Za-zäöüÄÖÜß][A-Za-zäöüÄÖÜß\s-]+(?:\s+[A-Za-zäöüÄÖÜß][A-Za-zäöüÄÖÜß\s-]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 52 | 0 | 52 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 52 | 1743 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``)

**False Positives:**

```
... über die Beschwerde vom  21. März 2023 gegen den Bescheid des <<<FA Waldviertel  vom >>>17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer ...
```

FP: `FA Waldviertel  vom ` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 1** (doc_id: ``)

**False Positives:**

```
... über die Beschwerde vom  21. März 2023 gegen den Bescheid des <<<FA Waldviertel  vom >>>17. Februar 2023 betreffend Nachsicht §  236 BAO 2023 Steuernummer ...
```

FP: `FA Waldviertel  vom ` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Edwin Brunnarius` (person)
- `Eberhard Grossmüller` (person)
- `Garanaser Straße 17H, 3800 Merkenbrechts, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Schubertstraße 62, 8010 Graz` (address)
- `FA Waldviertel` (organisation)
- `94-628/5503` (tax_number)

**Example 2** (doc_id: ``)

**False Positives:**

```
Zu A. und B. führte das <<<FA begründend aus>>>, dass der Bf. für mehr als ein Kind Familienbeihilfe  bezogen ...
```

FP: `FA begründend aus` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``)

**False Positives:**

```
Der Bf. brachte beim <<<FA am >>>11.09.2023 folgende Beschwerde ein:  „Zum einen hat meine Tochter, ...
```

FP: `FA am ` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``)

**False Positives:**

```
... Beschwerde des Bf. gegen den Rückforderungsbescheid wurde vom <<<FA mit  Beschwerdevorentscheidung vom >>>11.09.2023 mit folgender Begründung abgewiesen:  „Gemäß § 2 ...
```

FP: `FA mit  Beschwerdevorentscheidung vom ` (organisation)

**✅ Gold Entities:**

</details>

---

</details>

---

