# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (ris)

Generated on: 2026-05-21T21:10:39.714837

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-21/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 1000 |
| Validation documents | 252 |
| Test documents | 23285 |
| Train sentences | 2083 |
| Validation sentences | 451 |
| Test sentences | 23285 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 10 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 100 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Seeded From | findok |
| Seed Rule Count | 88 |
| New Rules Added | 33 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 1171 |
| Phase1 Eval Sentences | 213 |
| Transfer Train Sentences | 912 |
| Transfer Eval Sentences | 238 |
| Best Batch Idx | 5 |
| Best Batch F1 | 0.10955056179775281 |
| Best Rules Serialized | [{'id': '297fcc00', 'name': 'Greiner-Mai Event', 'description': "Matches the specific entity 'Greiner-Mai Event'.", 'format': 'regex', 'content': '\\bGreiner-Mai\\s+Event\\b', 'priority': 3, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1edc6ba7', 'name': 'NordDaten', 'description': "Matches the specific entity 'NordDaten'.", 'format': 'regex', 'content': '\\bNordDaten\\b', 'priority': 3, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '687bd956', 'name': 'Technik Ostbachal', 'description': "Matches the specific entity 'Technik Ostbachal'.", 'format': 'regex', 'content': '\\bTechnik\\s+Ostbachal\\b', 'priority': 3, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '606c3ff4', 'name': 'Vossbein Lebensmittel', 'description': "Matches the specific entity 'Vossbein Lebensmittel'.", 'format': 'regex', 'content': '\\bVossbein\\s+Lebensmittel\\b', 'priority': 3, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b15a7862', 'name': 'Paweltschik Telekom GMBH', 'description': "Matches the specific entity 'Paweltschik Telekom GMBH'.", 'format': 'regex', 'content': '\\bPaweltschik\\s+Telekom\\s+GMBH\\b', 'priority': 3, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'bcd7be36', 'name': 'Nexgartuni Finanzen Planung GMBH', 'description': "Matches the specific entity 'Nexgartuni Finanzen Planung GMBH'.", 'format': 'regex', 'content': '\\bNexgartuni\\s+Finanzen\\s+Planung\\s+GMBH\\b', 'priority': 3, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '5f0c9201', 'name': 'AlpenSicherheit GMBH', 'description': "Matches the specific entity 'AlpenSicherheit GMBH'.", 'format': 'regex', 'content': '\\bAlpenSicherheit\\s+GMBH\\b', 'priority': 3, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '470fcb8c', 'name': 'Reinemut Smoch Handel', 'description': "Matches the specific entity 'Reinemut + Smoch Handel' found in multiple failures.", 'format': 'regex', 'content': 'Reinemut\\s*\\+\\s*Smoch\\s*Handel', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7c422cd1', 'name': 'FA Salzburg-Stadt', 'description': "Matches 'FA Salzburg-Stadt' and 'Finanzamt Salzburg-Stadt' including the www. prefix.", 'format': 'regex', 'content': '(?:www\\.)?FA\\s*Salzburg\\-Stadt|Finanzamt\\s*Salzburg\\-Stadt', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '92ef9b5e', 'name': 'TalVerverwerkGarten GMBH', 'description': "Matches the specific entity 'TalVerverwerkGarten GMBH' including the ellipsis variant.", 'format': 'regex', 'content': '\\bTalVerverwerkGarten\\s+GMBH(?:\\u2026)?\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd026d57e', 'name': 'Henken', 'description': "Matches the specific entity 'Henken'.", 'format': 'regex', 'content': '\\bHenken\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7f815650', 'name': 'Süd-Landwirtschaft', 'description': "Matches the specific entity 'Süd-Landwirtschaft'.", 'format': 'regex', 'content': '\\bSüd-Landwirtschaft\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '4eee39aa', 'name': 'Specific Company Grönemeier', 'description': "Matches the specific entity 'Grönemeier&Hövelberndt E‑Commerce'.", 'format': 'regex', 'content': '\\bGr\\u00f6nemeier&H\\u00f6velberndt\\s+E\\u2011Commerce\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '41e4c5a7', 'name': 'Specific Company Milan Händlein', 'description': "Matches the specific entity 'Milan Händlein'.", 'format': 'regex', 'content': '\\bMilan\\s+H\\u00e4ndlein\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'c7f29664', 'name': 'Specific Company Annemie Bott', 'description': "Matches the specific entity 'Annemie Bott'.", 'format': 'regex', 'content': '\\bAnnemie\\s+Bott\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '45df2358', 'name': 'Specific Company Krolitzki', 'description': "Matches the specific entity 'Krolitzki Beratung'.", 'format': 'regex', 'content': '\\bKrolitzki\\s+Beratung\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'ff59234b', 'name': 'Specific Company Manfredo Herrschmann', 'description': "Matches the specific entity 'Manfredo Herrschmann'.", 'format': 'regex', 'content': '\\bManfredo\\s+Herrschmann\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '16526f53', 'name': 'Specific Company StadtEnergie', 'description': "Matches the specific entity 'StadtEnergie Holding'.", 'format': 'regex', 'content': '\\bStadtEnergie\\s+Holding\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '9a352a4b', 'name': 'Specific Company Laskowsky', 'description': "Matches the specific entity 'Laskowsky Umwelt'.", 'format': 'regex', 'content': '\\bLaskowsky\\s+Umwelt\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '467653e9', 'name': 'Specific Company TraunChemie', 'description': "Matches the specific entity 'TraunChemie GMBH'.", 'format': 'regex', 'content': '\\bTraunChemie\\s+GMBH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'a70a0e0b', 'name': 'Specific Company Butkus', 'description': "Matches the specific entity 'Butkus Metall'.", 'format': 'regex', 'content': '\\bButkus\\s+Metall\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7fb61038', 'name': 'Specific Company Englert', 'description': "Matches the specific entity 'Englert Möbel'.", 'format': 'regex', 'content': '\\bEnglert\\s+M\\u00f6bel\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e899b8a9', 'name': 'Specific Company Keldonbach', 'description': "Matches the specific entity 'Keldonbach Sicherheit GMBH'.", 'format': 'regex', 'content': '\\bKeldonbach\\s+Sicherheit\\s+GMBH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1f257002', 'name': 'Sanitär Talder GMBH', 'description': "Matches the specific entity 'Sanitär Talder GMBH'.", 'format': 'regex', 'content': 'Sanitär\\s+Talder\\s+GMBH', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '11028e60', 'name': 'Roelfsen Versicherung', 'description': "Matches the specific entity 'Roelfsen Versicherung'.", 'format': 'regex', 'content': 'Roelfsen\\s+Versicherung', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '91685d83', 'name': 'Lubomir Merschmeyer', 'description': "Matches the specific entity 'Lubomir Merschmeyer'.", 'format': 'regex', 'content': 'Lubomir\\s+Merschmeyer', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e110e4b5', 'name': 'Houdek Maschinenbau', 'description': "Matches the specific entity 'Houdek Maschinenbau'.", 'format': 'regex', 'content': 'Houdek\\s+Maschinenbau', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '19a4f00e', 'name': 'Schmeltz Luftfahrt', 'description': "Matches the specific entity 'Schmeltz Luftfahrt'.", 'format': 'regex', 'content': 'Schmeltz\\s+Luftfahrt', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'cfe657a4', 'name': 'Dorfcon-Verlag', 'description': "Matches the specific entity 'Dorfcon-Verlag'.", 'format': 'regex', 'content': 'Dorfcon-Verlag', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '3407167e', 'name': 'Lexdon IT', 'description': "Matches the specific entity 'Lexdon IT'.", 'format': 'regex', 'content': 'Lexdon\\s+IT', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '733a2290', 'name': 'Stadt Logglanz', 'description': "Matches the specific entity 'Stadt Logglanz'.", 'format': 'regex', 'content': 'Stadt\\s+Logglanz', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'a13a0930', 'name': 'Gözcü Getränke', 'description': "Matches the specific entity 'Gözcü Getränke'.", 'format': 'regex', 'content': 'Gözcü\\s+Getränke', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8e6cc383', 'name': 'Hörup Gastronomie AG', 'description': "Matches the specific entity 'Hörup Gastronomie AG'.", 'format': 'regex', 'content': 'Hörup\\s+Gastronomie\\s+AG', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '2e5c5578', 'name': 'Dammke KI GMBH', 'description': "Matches the specific entity 'Dammke KI GMBH'.", 'format': 'regex', 'content': 'Dammke\\s+KI\\s+GMBH', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e8d7d3d8', 'name': 'TraunChemie GMBH', 'description': "Matches the specific entity 'TraunChemie GMBH'.", 'format': 'regex', 'content': 'TraunChemie\\s+GMBH', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '3850ee07', 'name': 'Tritri-IT', 'description': "Matches the specific entity 'Tritri-IT'.", 'format': 'regex', 'content': 'Tritri-IT', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '46c6a075', 'name': 'Finanzamt Wien 1/23', 'description': "Matches 'Finanzamt Wien 1/23'.", 'format': 'regex', 'content': 'Finanzamt\\s+Wien\\s+1/23', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1446165d', 'name': 'FA Wien 1/23', 'description': "Matches 'FA Wien 1/23'.", 'format': 'regex', 'content': '\\bFA\\s+Wien\\s+1/23', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '66e0c123', 'name': 'Naaß Elektro GMBH', 'description': "Matches the specific entity 'Naaß Elektro GMBH'.", 'format': 'regex', 'content': 'Naaß\\s+Elektro\\s+GMBH', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '86f251e0', 'name': 'Bersud Möbel GMBH', 'description': "Matches the specific entity 'Bersud Möbel GMBH'.", 'format': 'regex', 'content': 'Bersud\\s+Möbel\\s+GMBH', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'ad00504a', 'name': 'Unter Heimdorf GMBH', 'description': "Matches the specific entity 'Unter Heimdorf GMBH'.", 'format': 'regex', 'content': 'Unter\\s+Heimdorf\\s+GMBH', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd0cea1d1', 'name': 'WXE Textil GMBH', 'description': "Matches the specific entity 'WXE Textil GMBH'.", 'format': 'regex', 'content': 'WXE\\s+Textil\\s+GMBH', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8cb601c4', 'name': 'Kornfelder Recycling', 'description': "Matches the specific entity 'Kornfelder Recycling'.", 'format': 'regex', 'content': 'Kornfelder\\s+Recycling', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b90a5241', 'name': 'DGCV E-Commerce GMBH', 'description': "Matches the specific entity 'DGCV E-Commerce GMBH' (handling both en-dash and hyphen variants if necessary, but focusing on the text provided).", 'format': 'regex', 'content': 'DGCV\\s+E[\\u2011-]Commerce\\s+GMBH', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '2e67d665', 'name': 'UGQQ Verlag OG', 'description': "Matches the specific entity 'UGQQ Verlag OG'.", 'format': 'regex', 'content': 'UGQQ\\s+Verlag\\s+OG', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd1b9dad6', 'name': 'Fatima Finkenbein', 'description': "Matches the specific entity 'Fatima Finkenbein' as an organization in this context.", 'format': 'regex', 'content': 'Fatima\\s+Finkenbein', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e85980b6', 'name': 'Wien Waldnor KG', 'description': "Matches the specific entity 'Wien Waldnor KG'.", 'format': 'regex', 'content': '\\bWien\\s+Waldnor\\s+KG\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '28965f3f', 'name': 'Botho Mikloweit', 'description': "Matches the specific entity 'Botho Mikloweit' as an organization in this context.", 'format': 'regex', 'content': '\\bBotho\\s+Mikloweit\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b775ac82', 'name': 'Kraftver-Gastronomie GMBH', 'description': "Matches the specific entity 'Kraftver-Gastronomie GMBH'.", 'format': 'regex', 'content': '\\bKraftver-Gastronomie\\s+GMBH\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '980b9a06', 'name': 'Gartgart Dienstleistungen GMBH', 'description': "Matches the specific entity 'Gartgart Dienstleistungen GMBH'.", 'format': 'regex', 'content': '\\bGartgart\\s+Dienstleistungen\\s+GMBH\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '197e92cb', 'name': 'Gogel Daten GMBH', 'description': "Matches the specific entity 'Gogel Daten GMBH'.", 'format': 'regex', 'content': '\\bGogel\\s+Daten\\s+GMBH\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'db01081f', 'name': 'Klein-Vorholt KI GMBH', 'description': "Matches the specific entity 'Klein-Vorholt KI GMBH'.", 'format': 'regex', 'content': '\\bKlein-Vorholt\\s+KI\\s+GMBH\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b6b0b60b', 'name': 'Raiffeisenkasse Retz-Pulkautal', 'description': "Matches the specific entity 'Raiffeisenkasse Retz-Pulkautal'.", 'format': 'regex', 'content': '\\bRaiffeisenkasse\\s+Retz-Pulkautal\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'cb0cc520', 'name': 'Nord Kellex', 'description': "Matches the specific entity 'Nord Kellex'.", 'format': 'regex', 'content': '\\bNord\\s+Kellex\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '4e1374bc', 'name': 'Specific Company Norconheim', 'description': "Matches the specific entity 'Norconheim'.", 'format': 'regex', 'content': '\\bNorconheim\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '24d13a6b', 'name': 'Specific Company Nexdorf-Metall', 'description': "Matches the specific entity 'Nexdorf-Metall'.", 'format': 'regex', 'content': '\\bNexdorf-Metall\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'bf14d09e', 'name': 'Specific Company Oppert Elektro', 'description': "Matches the specific entity 'Oppert Elektro'.", 'format': 'regex', 'content': '\\bOppert\\s+Elektro\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '271fecc4', 'name': 'Specific Company Zimmerhackel Bau', 'description': "Matches the specific entity 'Zimmerhackel Bau'.", 'format': 'regex', 'content': '\\bZimmerhackel\\s+Bau\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '14ac09bd', 'name': 'Specific Company Vahrenkamp Luftfahrt', 'description': "Matches the specific entity 'Vahrenkamp Luftfahrt'.", 'format': 'regex', 'content': '\\bVahrenkamp\\s+Luftfahrt\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'c03e94b9', 'name': 'Specific Company Gorius und Ziegann Event GMBH', 'description': "Matches the specific entity 'Gorius und Ziegann Event GMBH'.", 'format': 'regex', 'content': '\\bGorius\\s+und\\s+Ziegann\\s+Event\\s+GMBH\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e8f5f0e9', 'name': 'Specific Company Raiffeisenbank Rion Vöcklabruck', 'description': "Matches the specific entity 'Raiffeisenbank Rion Vöcklabruck'.", 'format': 'regex', 'content': '\\bRaiffeisenbank\\s+Rion\\s+V\\u00f6cklabruck\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '9d77209f', 'name': 'Specific Company Basdas Pharma AG', 'description': "Matches the specific entity 'Basdas Pharma AG'.", 'format': 'regex', 'content': '\\bBasdas\\s+Pharma\\s+AG\\b', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '5ad4913c', 'name': 'Depp Versand', 'description': "Matches the specific entity 'Depp Versand'.", 'format': 'regex', 'content': '\\bDepp\\s+Versand\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'ca4bc5ae', 'name': 'SüdEvent AG', 'description': "Matches the specific entity 'SüdEvent AG'.", 'format': 'regex', 'content': '\\bSüdEvent\\s+AG\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '4470d15c', 'name': 'Obernöder+Küsbert Touristik GMBH', 'description': "Matches the specific entity 'Obernöder+Küsbert Touristik GMBH'.", 'format': 'regex', 'content': '\\bObernöder\\+Küsbert\\s+Touristik\\s+GMBH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '3beed63c', 'name': 'Talost GMBH', 'description': "Matches the specific entity 'Talost GMBH'.", 'format': 'regex', 'content': '\\bTalost\\s+GMBH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'a87b0377', 'name': 'Finanzamt with location', 'description': "Matches full names of tax authorities, ensuring 'Oststeiermark' and 'Salzburg-Stadt' are covered.", 'format': 'regex', 'content': '\\bFinanzamt\\s+(?:Steiermark\\s+Mitte|Nieder\\u00f6sterreich\\s+Mitte|Salzburg-Land|Salzburg-Stadt|Vorarlberg|Waldviertel|Klosterneuburg|Bruck\\s+Eisenstadt\\s+Oberwart|Klagenfurt\\s+St\\.\\s+Veit\\s+Wolfsberg|Graz-Stadt|Innsbruck|Linz|Tirol\\s+Ost|Bruck\\s+Leoben\\s+M\\u00fcrzzuschlag|Braunau\\s+Ried\\s+Sch\\u00e4rding|Grieskirchen\\s+Wels|Deutschlandsberg\\s+Leibnitz\\s+Voitsberg|Judenburg\\s+Liezen|Baden\\s+M\\u00f6dling|Amstetten\\s+Melk\\s+Scheibbs|Kirchdorf\\s+Perg\\s+Steyr|St\\.\\s+Johann\\s+Tamsweg\\s+Zell\\s+am\\s+See|Landeck\\s+Reutte|Schwechat\\s+Gerasdorf|Freistadt\\s+Rohrbach\\s+Urfahr|Purkersdorf|Wien\\s+\\d+/\\d+(?:/\\d+)*(?:/\\d+)*|Gmunden\\s+V\\u00f6cklabruck|Wels\\s+S\\u00fcd|Oststeiermark|[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd5845d57', 'name': 'FA abbreviation with location', 'description': "Matches abbreviated tax authorities, ensuring 'Oststeiermark' and 'Salzburg-Stadt' are covered.", 'format': 'regex', 'content': '\\bFA\\s+(?:Steiermark\\s+Mitte|Nieder\\u00f6sterreich\\s+Mitte|Salzburg-Land|Salzburg-Stadt|Vorarlberg|Waldviertel|Klosterneuburg|Bruck\\s+Eisenstadt\\s+Oberwart|Klagenfurt\\s+St\\.\\s+Veit\\s+Wolfsberg|Graz-Stadt|Innsbruck|Linz|Tirol\\s+Ost|Bruck\\s+Leoben\\s+M\\u00fcrzzuschlag|Braunau\\s+Ried\\s+Sch\\u00e4rding|Grieskirchen\\s+Wels|Deutschlandsberg\\s+Leibnitz\\s+Voitsberg|Judenburg\\s+Liezen|Baden\\s+M\\u00f6dling|Amstetten\\s+Melk\\s+Scheibbs|Kirchdorf\\s+Perg\\s+Steyr|St\\.\\s+Johann\\s+Tamsweg\\s+Zell\\s+am\\s+See|Landeck\\s+Reutte|Schwechat\\s+Gerasdorf|Freistadt\\s+Rohrbach\\s+Urfahr|Purkersdorf|Wien\\s+\\d+/\\d+(?:/\\d+)*(?:/\\d+)*|Gmunden\\s+V\\u00f6cklabruck|Wels\\s+S\\u00fcd|Oststeiermark|[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b3da11b4', 'name': 'Inn-Recycling Institut GMBH', 'description': "Matches the specific entity 'Inn-Recycling Institut GMBH'.", 'format': 'regex', 'content': '\\bInn-Recycling\\s+Institut\\s+GMBH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'c0c96d4e', 'name': 'EnnsBildung', 'description': "Matches the specific entity 'EnnsBildung'.", 'format': 'regex', 'content': '\\bEnnsBildung\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'c87f2aeb', 'name': 'Olivier u. Bartha Recycling', 'description': "Matches the specific entity 'Olivier u. Bartha Recycling'.", 'format': 'regex', 'content': '\\bOlivier\\s+u\\.\\s+Bartha\\s+Recycling\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '30f675c7', 'name': 'West-Luftfahrt', 'description': "Matches the specific entity 'West-Luftfahrt'.", 'format': 'regex', 'content': '\\bWest-Luftfahrt\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7c18768f', 'name': 'Chen Setzekorn', 'description': "Matches the specific entity 'Chen Setzekorn'.", 'format': 'regex', 'content': '\\bChen\\s+Setzekorn\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '80112cb8', 'name': 'Istvan Gerart', 'description': "Matches the specific entity 'Istvan Gerart'.", 'format': 'regex', 'content': '\\bIstvan\\s+Gerart\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '0faa5e01', 'name': 'Berwaldkel-Möbel AG', 'description': "Matches the specific entity 'Berwaldkel-Möbel AG'.", 'format': 'regex', 'content': '\\bBerwaldkel-Möbel\\s+AG\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'c413d0ce', 'name': 'Landesgericht', 'description': "Matches district courts like 'Landesgericht Innsbruck'.", 'format': 'regex', 'content': '\\bLandesgericht\\s+[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e5b7265e', 'name': 'LG abbreviation', 'description': "Matches 'LG' followed by city names, e.g., 'LG Innsbruck'.", 'format': 'regex', 'content': '\\bLG\\s+[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8193c833', 'name': 'Raiffeisen Rionalbank Hall in Tirol', 'description': "Matches the specific entity 'Raiffeisen Rionalbank Hall in Tirol'.", 'format': 'regex', 'content': '\\bRaiffeisen\\s+Rionalbank\\s+Hall\\s+in\\s+Tirol\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '3d168562', 'name': 'SüdVersand', 'description': "Matches the specific entity 'SüdVersand'.", 'format': 'regex', 'content': '\\bSüdVersand\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '045672f7', 'name': 'Raiffeisenbank Wels Süd', 'description': "Matches the specific entity 'Raiffeisenbank Wels Süd'.", 'format': 'regex', 'content': '\\bRaiffeisenbank\\s+Wels\\s+Süd\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '410590b8', 'name': 'TraunLuftfahrt Solutions', 'description': "Matches the specific entity 'TraunLuftfahrt Solutions'.", 'format': 'regex', 'content': '\\bTraunLuftfahrt\\s+Solutions\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '913a2c4e', 'name': 'Mittel-Logistik', 'description': "Matches the specific entity 'Mittel-Logistik'.", 'format': 'regex', 'content': '\\bMittel-Logistik\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8cf2120f', 'name': 'Fensudlog GMBH', 'description': "Matches the specific entity 'Fensudlog GMBH'.", 'format': 'regex', 'content': '\\bFensudlog\\s+GMBH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '03c5bade', 'name': 'Psomadakis Touristik', 'description': "Matches the specific entity 'Psomadakis Touristik'.", 'format': 'regex', 'content': '\\bPsomadakis\\s+Touristik\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '98fff7bd', 'name': 'Specific Compound AG 1', 'description': "Matches specific compound AG entities like 'Fenbach-IT AG', 'SüdCloud AG', 'Ost-Metall AG', 'Frise und Stasiak Wind AG', 'Uniglanz Bildung Solutions AG', 'QBAW Forschung AG' and similar patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+AG)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'dbf477dc', 'name': 'Specific Compound Aktiengesellschaft', 'description': "Matches 'Kraftwerk-E‑Commerce Aktiengesellschaft' and similar full forms.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Aktiengesellschaft)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd2473613', 'name': 'Specific Compound u. Fuhrer', 'description': "Matches 'Pfeiffenschneider u. Fuhrer Forschung AG' and similar 'u.' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+u\\.\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+AG)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'f3e2904e', 'name': 'Bezirksgericht', 'description': "Matches district courts like 'Bezirksgericht Mattersburg', handling repeated instances correctly.", 'format': 'regex', 'content': '\\bBezirksgericht\\s+[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*', 'priority': 5, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e092b6a3', 'name': 'Lowercase GmbH Company', 'description': "Matches companies ending in 'gmbh' (all lowercase) found in training data.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+gmbh)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '46c40acb', 'name': 'Specific Compound GmbH 2', 'description': "Matches 'Inn-Recycling Institut GMBH' and similar 'Institut' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Institut\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'a16f5744', 'name': 'Specific Compound GmbH 3', 'description': "Matches 'Talost GMBH' and similar single word + GmbH patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '0a71e1ad', 'name': 'Specific Compound GmbH 4', 'description': "Matches 'Obernöder+Küsbert Touristik GMBH' and similar '+' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Touristik\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '4b2a55bb', 'name': 'Specific Compound GmbH 5', 'description': "Matches 'Kraftver-Gastronomie GMBH' and similar hyphenated patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Gastronomie\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b1bb9235', 'name': 'Specific Compound GmbH 6', 'description': "Matches 'Gartgart Dienstleistungen GMBH' and similar 'Dienstleistungen' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Dienstleistungen\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '0c5fe463', 'name': 'Specific Compound GmbH 7', 'description': "Matches 'Gogel Daten GMBH' and similar 'Daten' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Daten\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '18b660ce', 'name': 'Specific Compound GmbH 8', 'description': "Matches 'Klein-Vorholt KI GMBH' and similar 'KI' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+KI\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '5fd08af0', 'name': 'Specific Compound GmbH 9', 'description': "Matches 'Naaß Elektro GMBH' and similar 'Elektro' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Elektro\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'f7a6637a', 'name': 'Specific Compound GmbH 10', 'description': "Matches 'Bersud Möbel GMBH' and similar 'Möbel' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Möbel\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '339678e2', 'name': 'Specific Compound GmbH 11', 'description': "Matches 'Unter Heimdorf GMBH' and similar 'Heimdorf' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Heimdorf\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '5dc5ef00', 'name': 'Specific Compound GmbH 12', 'description': "Matches 'WXE Textil GMBH' and similar 'Textil' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Textil\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '9349efe7', 'name': 'Specific Compound GmbH 13', 'description': "Matches 'Kornfelder Recycling' and similar 'Recycling' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Recycling)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '716fe16e', 'name': 'Specific Compound GmbH 14', 'description': "Matches 'DGCV E-Commerce GMBH' and similar 'E-Commerce' patterns.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+E-Commerce\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8f71bc96', 'name': 'General AG Company', 'description': "Matches companies ending in AG, ensuring strict boundaries to avoid capturing preceding context like 'von der' or legal party lists.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?(?!(?:Partei|Die|Der|des|der|von|der|in|mit|auf|an|bei|nach|vor|zu|für|um|ohne|durch|gegen|über|unter|neben|zwischen|entlang|statt|außer|bis|seit|während|wegen|trotz|dank|laut|gemäß|entsprechend|Richter|Senatspräsident|Hofrat|Hofrätin|Mag\\.|Dr\\.)(?:\\s+|\\n))(?![A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*\\s+AG)([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+AG)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '4df85cb0', 'name': 'General GMBH Company', 'description': 'Matches companies ending in GmbH, ensuring strict boundaries to avoid capturing preceding context.', 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?(?!(?:Partei|Die|Der|des|der|von|der|in|mit|auf|an|bei|nach|vor|zu|für|um|ohne|durch|gegen|über|unter|neben|zwischen|entlang|statt|außer|bis|seit|während|wegen|trotz|dank|laut|gemäß|entsprechend|Richter|Senatspräsident|Hofrat|Hofrätin|Mag\\.|Dr\\.)(?:\\s+|\\n))(?![A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*\\s+GmbH)([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+GmbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '60837e20', 'name': 'Specific Compound GmbH 1', 'description': "Matches specific compound GmbH entities like 'Schlezak+Bareuter Pharma GmbH', 'EnnsSanitär GmbH', 'Kärgel + Rafalzik Maschinenbau GmbH', 'Inn-Finanzen Gesellschaft mbH' and similar patterns with lowercase 'gmbh'.", 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Gesellschaft\\s+mbH)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'a77c2523', 'name': 'Limited Company', 'description': 'Matches companies ending in Limited.', 'format': 'regex', 'content': '(?<!\\w)(?:^|\\s|\\(|\\[|\\"|\\\'|,|\\.)\\s*(?:Firma\\s+)?([A-Z][a-zA-Z0-9+&\\-\\s]*(?:\\s+[A-Z][a-zA-Z0-9+&\\-\\s]*)*\\s+Limited)(?=\\s|$|\\)|\\]|\\"|\\\'|,|\\.|;|\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1517df6b', 'name': 'Specific Organisation Wallkötter', 'description': "Matches 'Wallkötter Finanzen GmbH'.", 'format': 'regex', 'content': '\\bWallkötter\\s+Finanzen\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7d7825a3', 'name': 'Specific Organisation Fensudwil', 'description': "Matches 'Fensudwil GmbH'.", 'format': 'regex', 'content': '\\bFensudwil\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '0f978a3d', 'name': 'Specific Organisation Fenseeuni', 'description': "Matches 'Fenseeuni GmbH'.", 'format': 'regex', 'content': '\\bFenseeuni\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'f3a90c13', 'name': 'Specific Organisation Rudschinski', 'description': "Matches 'Rudschinski Handel GmbH'.", 'format': 'regex', 'content': '\\bRudschinski\\s+Handel\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '6b6a23db', 'name': 'Specific Organisation Jasensky', 'description': "Matches 'Jasensky Medien GmbH'.", 'format': 'regex', 'content': '\\bJasensky\\s+Medien\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'eca61406', 'name': 'Specific Organisation Inn-Energie', 'description': "Matches 'Inn-Energie GmbH'.", 'format': 'regex', 'content': '\\bInn-Energie\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '76beaa9e', 'name': 'Specific Organisation Kleinkurt', 'description': "Matches 'Kleinkurt Sicherheit GmbH'.", 'format': 'regex', 'content': '\\bKleinkurt\\s+Sicherheit\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1d5f76d7', 'name': 'Specific Organisation Getränke', 'description': "Matches 'Getränke Logwerk GmbH'.", 'format': 'regex', 'content': '\\bGetränke\\s+Logwerk\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '36c952d0', 'name': 'Specific Organisation Bergstresser', 'description': "Matches 'Bergstresser Beratung GmbH'.", 'format': 'regex', 'content': '\\bBergstresser\\s+Beratung\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'fdf4007c', 'name': 'Specific Organisation Zormonkel', 'description': "Matches 'Zormonkel Telekom AG'.", 'format': 'regex', 'content': '\\bZormonkel\\s+Telekom\\s+AG\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '4aee51a5', 'name': 'Specific Organisation Donau', 'description': "Matches 'Donau Furtdernex GmbH'.", 'format': 'regex', 'content': '\\bDonau\\s+Furtdernex\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd29c4851', 'name': 'Specific Organisation EnnsLogistik', 'description': "Matches 'EnnsLogistik Aktiengesellschaft'.", 'format': 'regex', 'content': '\\bEnnsLogistik\\s+Aktiengesellschaft\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '511a4f34', 'name': 'Specific Organisation Talmonwald', 'description': "Matches 'Talmonwald-Gastronomie GmbH'.", 'format': 'regex', 'content': '\\bTalmonwald-Gastronomie\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1be87fe8', 'name': 'Specific Organisation Hernschier', 'description': "Matches 'Hernschier Heizung AG'.", 'format': 'regex', 'content': '\\bHernschier\\s+Heizung\\s+AG\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e518f0ca', 'name': 'Specific Organisation MittelRobotik', 'description': "Matches 'MittelRobotik Betriebe GmbH'.", 'format': 'regex', 'content': '\\bMittelRobotik\\s+Betriebe\\s+GmbH\\b', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.0% |
| True Positives | 39 |
| False Positives | 328 |
| False Negatives | 306 |
| Total Gold Entities | 345 |
| Micro Precision | 10.6% |
| Micro Recall | 11.3% |
| Micro F1 | 11.0% |
| Macro F1 | 11.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Specific Compound GmbH 10` | 0.6% | 100.0% | 0.3% | 1 | 1 | 0 |
| `Specific Compound GmbH 12` | 0.6% | 100.0% | 0.3% | 1 | 1 | 0 |
| `Specific Compound GmbH 1` | 1.2% | 100.0% | 0.6% | 2 | 2 | 0 |
| `Lowercase GmbH Company` | 1.1% | 66.7% | 0.6% | 3 | 2 | 1 |
| `General AG Company` | 2.2% | 26.7% | 1.2% | 15 | 4 | 11 |
| `Specific Compound AG 1` | 3.3% | 26.1% | 1.7% | 23 | 6 | 17 |
| `Specific Compound GmbH 3` | 10.9% | 22.3% | 7.2% | 112 | 25 | 87 |
| `LG abbreviation` | 0.6% | 16.7% | 0.3% | 6 | 1 | 5 |
| `General GMBH Company` | 4.8% | 14.3% | 2.9% | 70 | 10 | 60 |
| `Bezirksgericht` | 0.8% | 1.6% | 0.6% | 126 | 2 | 124 |
| `Greiner-Mai Event` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `NordDaten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Technik Ostbachal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vossbein Lebensmittel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Paweltschik Telekom GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nexgartuni Finanzen Planung GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AlpenSicherheit GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Reinemut Smoch Handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Salzburg-Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TalVerverwerkGarten GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Henken` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Süd-Landwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Grönemeier` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Milan Händlein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Annemie Bott` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Krolitzki` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Manfredo Herrschmann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company StadtEnergie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Laskowsky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company TraunChemie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Butkus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Englert` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Keldonbach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sanitär Talder GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Roelfsen Versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lubomir Merschmeyer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Houdek Maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schmeltz Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dorfcon-Verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lexdon IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stadt Logglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gözcü Getränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hörup Gastronomie AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dammke KI GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TraunChemie GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tritri-IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien 1/23` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Wien 1/23` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Naaß Elektro GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bersud Möbel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unter Heimdorf GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WXE Textil GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kornfelder Recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `DGCV E-Commerce GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UGQQ Verlag OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fatima Finkenbein` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wien Waldnor KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Botho Mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kraftver-Gastronomie GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gartgart Dienstleistungen GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gogel Daten GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Klein-Vorholt KI GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenkasse Retz-Pulkautal` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nord Kellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Norconheim` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Nexdorf-Metall` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Oppert Elektro` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Zimmerhackel Bau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Vahrenkamp Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Gorius und Ziegann Event GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Raiffeisenbank Rion Vöcklabruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Basdas Pharma AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Depp Versand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SüdEvent AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Obernöder+Küsbert Touristik GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Talost GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt with location` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `FA abbreviation with location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Inn-Recycling Institut GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `EnnsBildung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Olivier u. Bartha Recycling` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `West-Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Chen Setzekorn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Istvan Gerart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Berwaldkel-Möbel AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht` | 0.0% | 0.0% | 0.0% | 87 | 0 | 87 |
| `Raiffeisen Rionalbank Hall in Tirol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SüdVersand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank Wels Süd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TraunLuftfahrt Solutions` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mittel-Logistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fensudlog GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Psomadakis Touristik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound Aktiengesellschaft` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `Specific Compound u. Fuhrer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound GmbH 2` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound GmbH 4` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound GmbH 5` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound GmbH 6` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Specific Compound GmbH 7` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Specific Compound GmbH 8` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Specific Compound GmbH 9` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Specific Compound GmbH 11` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound GmbH 13` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound GmbH 14` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Limited Company` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Specific Organisation Wallkötter` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Fensudwil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Fenseeuni` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Rudschinski` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Jasensky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Inn-Energie` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Kleinkurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Getränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Bergstresser` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Zormonkel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Donau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation EnnsLogistik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Talmonwald` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation Hernschier` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Organisation MittelRobotik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Specific Compound AG 1`

**F1:** 0.033 | **Precision:** 0.261 | **Recall:** 0.017  

**Format:** `regex`  
**Rule ID:** `98fff7bd`  
**Description:**
Matches specific compound AG entities like 'Fenbach-IT AG', 'SüdCloud AG', 'Ost-Metall AG', 'Frise und Stasiak Wind AG', 'Uniglanz Bildung Solutions AG', 'QBAW Forschung AG' and similar patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+AG)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.261 | 0.017 | 0.033 | 23 | 6 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 17 | 337 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Analyse Kelunizor AG` | `Analyse Kelunizor AG` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `LGR Medien GmbH` (organisation)
- `OVX Finanzen` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `TraunBau AG` | `TraunBau AG` |

**Missed by this rule (FN):**

- `Ing. KzlR MedR Brunhild Syndikus` (person)
- `Böhnstedt+Bittlmeier Verlag GmbH` (organisation)
- `Wien Traalmon Betriebe` (organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei OMedR Eleonore Wunderling, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG, Amanda Deutschlender, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Claeser Forschung AG` — partial — pred is substring of gold: `Fildhaut & Claeser Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Eleonore Wunderling`(person)
- `Fildhaut & Claeser Forschung AG`(organisation)
- `Amanda Deutschlender`(person)

</details>

---

## `Specific Compound GmbH 3`

**F1:** 0.109 | **Precision:** 0.223 | **Recall:** 0.072  

**Format:** `regex`  
**Rule ID:** `a16f5744`  
**Description:**
Matches 'Talost GMBH' and similar single word + GmbH patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.223 | 0.072 | 0.109 | 112 | 25 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 25 | 87 | 319 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Dersudheim Digital GmbH` | `Dersudheim Digital GmbH` |

**Missed by this rule (FN):**

- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)
- `Ingolf Grimpe` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Energie Conwald GmbH` | `Energie Conwald GmbH` |

**Example 3** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_5`)


Metall Monglanz GmbH, beide Johann-Puch-Straße 5, 8741 Reisstraße, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Metall Monglanz GmbH` | `Metall Monglanz GmbH` |

**Missed by this rule (FN):**

- `Johann-Puch-Straße 5, 8741 Reisstraße, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_4`)


Text Begründung: Die klagende GmbH mit Sitz in Wien begehrt von dem in Graz wohnhaften Beklagten die Zahlung von 5.232 EUR an Werklohn für eine Entrümpelung der Wohnungen Top 2, 3 und 4 in einem dem Beklagten gehörigen Haus in 1150 Wien.

**False Positives:**

- `Die klagende GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH` — partial — gold is substring of pred: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_8`)


Text Begründung: Im Jahr 2004 errichtete eine GmbH (im Folgenden Unternehmerin) auf einer Liegenschaft eine Stützmauer aus unvermörtelten geschlichteten Natursteinen (Steinschlichtung).

**False Positives:**

- `Im Jahr 2004 errichtete eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_38`)


Auftraggeber sei nur die GmbH gewesen.

**False Positives:**

- `Auftraggeber sei nur die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH` — partial — gold is substring of pred: `HochAnalyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HochAnalyse GmbH`(organisation)
- `Piedro Ehmken`(person)
- `Ludewigs Handel GmbH`(organisation)
- `Deborah Lochhuber`(person)

</details>

---

## `General GMBH Company`

**F1:** 0.048 | **Precision:** 0.143 | **Recall:** 0.029  

**Format:** `regex`  
**Rule ID:** `4df85cb0`  
**Description:**
Matches companies ending in GmbH, ensuring strict boundaries to avoid capturing preceding context.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?(?!(?:Partei|Die|Der|des|der|von|der|in|mit|auf|an|bei|nach|vor|zu|für|um|ohne|durch|gegen|über|unter|neben|zwischen|entlang|statt|außer|bis|seit|während|wegen|trotz|dank|laut|gemäß|entsprechend|Richter|Senatspräsident|Hofrat|Hofrätin|Mag\.|Dr\.)(?:\s+|\n))(?![A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+GmbH)([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.143 | 0.029 | 0.048 | 70 | 10 | 60 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 60 | 332 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Donau-Automotive GmbH` | `Donau-Automotive GmbH` |

**Missed by this rule (FN):**

- `Dr. Ralph Kreidenweiß` (person)
- `Ebersreith 11, 8761 Götzendorf, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `LGR Medien GmbH` | `LGR Medien GmbH` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `OVX Finanzen` (organisation)
- `Analyse Kelunizor AG` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `DonauLexlogbruckPlanung GmbH` | `DonauLexlogbruckPlanung GmbH` |

**Missed by this rule (FN):**

- `Lebensmittel Glanzconuni AG` (organisation)
- `Immanuel Gspan` (person)
- `Fridolin Braunhold` (person)
- `Mag. Frauke Steinweg` (person)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/5Ob84_16p`) (sent_id: `deanon_TRAIN/5Ob84_16p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der Rechtssache der klagenden Partei Dimitri Ringlstetter, vertreten durch Dr. Friedrich Gatscha, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Heimaluni-Event GmbH, Vorderstraß 39, 3920 Harruck, Österreich, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, 2. IJWQ Digital Services GmbH, Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich, vertreten durch Mag. Alain Danner, Rechtsanwalt in Wien, 3. Dr. Amalia Brodke, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wegen 1. Übertragung der Zusage auf Einräumung von Wohnungseigentum (30.000 EUR), 2. Einverleibung von Miteigentum (50.000 EUR), 3. Zahlung (122.785,01 EUR sA), 4. Feststellung (15.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 95.000 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. März 2016, GZ 34 R 152/15w-50, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Heimaluni-Event GmbH` | `Heimaluni-Event GmbH` |
| `IJWQ Digital Services GmbH` | `IJWQ Digital Services GmbH` |

**Missed by this rule (FN):**

- `Dimitri Ringlstetter` (person)
- `Vorderstraß 39, 3920 Harruck, Österreich` (address)
- `Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich` (address)
- `Dr. Amalia Brodke` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH` — partial — gold is substring of pred: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_8`)


Text Begründung: Im Jahr 2004 errichtete eine GmbH (im Folgenden Unternehmerin) auf einer Liegenschaft eine Stützmauer aus unvermörtelten geschlichteten Natursteinen (Steinschlichtung).

**False Positives:**

- `Im Jahr 2004 errichtete eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_38`)


Auftraggeber sei nur die GmbH gewesen.

**False Positives:**

- `Auftraggeber sei nur die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH` — partial — gold is substring of pred: `HochAnalyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HochAnalyse GmbH`(organisation)
- `Piedro Ehmken`(person)
- `Ludewigs Handel GmbH`(organisation)
- `Deborah Lochhuber`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Bezirksgericht`

**F1:** 0.008 | **Precision:** 0.016 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `f3e2904e`  
**Description:**
Matches district courts like 'Bezirksgericht Mattersburg', handling repeated instances correctly.

**Content:**
```
\bBezirksgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.006 | 0.008 | 126 | 2 | 124 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 124 | 343 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_7`)


Nach dem Klagsvorbringen sei er am 19. 8. 2009 im Strandbad Bezirksgericht Silz beim Verlassen des Wassers von einem ca zwei Fäuste großen Stein ins Gesicht getroffen worden, der vom damals sechsjährigen Beklagten geworfen worden sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 1** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_18`)


Verwiesen werde auf einen Akt der Staatsanwaltschaft Bezirksgericht Wels, in welchem gegen den Schädiger Vorerhebungen geführt, jedoch mangels Deliktsfähigkeit eingestellt worden seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wels` | `Bezirksgericht Wels` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Bezirksgericht Judenburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

</details>

---

## `Landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c413d0ce`  
**Description:**
Matches district courts like 'Landesgericht Innsbruck'.

**Content:**
```
\bLandesgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 87 | 0 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 87 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Verfahrenshilfesache der Antragstellerin Florenzia Elefterakis, gegen den Antragsgegner Univ.-Prof. Dr. Leander Rossetti, wegen Bewilligung der Verfahrenshilfe, über den Antrag der Antragstellerin auf Delegierung der Rechtssache an das Landesgericht Korneuburg den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Rechtssache an das Landesgericht Korneuburg wird abgewiesen.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation
- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Florenzia Elefterakis`(person)
- `Dr. Leander Rossetti`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_4`)


Text Begründung: Die Antragstellerin richtete an das Landesgericht Linz einen Antrag auf Bewilligung der Verfahrenshilfe, weil sie gegen einen gerichtlichen Sachverständigen wegen eines in einem Pflegegeldprozess unrichtig erstatteten Gutachtens eine Schadenersatzklage auf Zahlung entgangenen Pflegegeldes und von Schmerzengeld erheben wolle.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_5`)


Das Landesgericht Linz leitete ein Verbesserungsverfahren ein.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_6`)


Die Antragstellerin beantwortete den schriftlichen Verbesserungsauftrag und beantragte die Delegierung des Verfahrens an das Landesgericht Korneuburg mit der Begründung, dass sie wegen ihrer körperlichen Behinderungen der Einladung der Richterin des Landesgerichts Linz, sie wegen offener Fragen bei Gericht aufzusuchen, nicht folgen könne.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_8`)


Das Landesgericht Linz äußerte sich zu diesem Antrag dahin, eine Delegierung könnte zweckmäßig sein, erscheine doch eine persönliche (ergänzende) Befragung der Antragstellerin zum Verfahrenshilfeantrag sinnvoll.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `General AG Company`

**F1:** 0.022 | **Precision:** 0.267 | **Recall:** 0.012  

**Format:** `regex`  
**Rule ID:** `8f71bc96`  
**Description:**
Matches companies ending in AG, ensuring strict boundaries to avoid capturing preceding context like 'von der' or legal party lists.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?(?!(?:Partei|Die|Der|des|der|von|der|in|mit|auf|an|bei|nach|vor|zu|für|um|ohne|durch|gegen|über|unter|neben|zwischen|entlang|statt|außer|bis|seit|während|wegen|trotz|dank|laut|gemäß|entsprechend|Richter|Senatspräsident|Hofrat|Hofrätin|Mag\.|Dr\.)(?:\s+|\n))(?![A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+AG)([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+AG)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.267 | 0.012 | 0.022 | 15 | 4 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 11 | 339 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `TraunBau AG` | `TraunBau AG` |

**Missed by this rule (FN):**

- `Ing. KzlR MedR Brunhild Syndikus` (person)
- `Böhnstedt+Bittlmeier Verlag GmbH` (organisation)
- `Wien Traalmon Betriebe` (organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/8Ob35_23i`) (sent_id: `deanon_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Pflege Deruni, und 2. Marchesi+Kusnezow Transport AG, Grabenseeweg 48, 8272 Ebersdorf, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Valerie Wilczenski, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Marchesi+Kusnezow Transport AG` | `Marchesi+Kusnezow Transport AG` |

**Missed by this rule (FN):**

- `Pflege Deruni` (organisation)
- `Grabenseeweg 48, 8272 Ebersdorf, Österreich` (address)
- `DI Valerie Wilczenski` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 3** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG` — partial — gold is substring of pred: `Donostzor-Software AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 4** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG` — partial — gold is substring of pred: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

</details>

---

## `Specific Compound Aktiengesellschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dbf477dc`  
**Description:**
Matches 'Kraftwerk-E‑Commerce Aktiengesellschaft' and similar full forms.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Aktiengesellschaft)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft` — partial — gold is substring of pred: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 4** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft` — partial — gold is substring of pred: `Heizung Werkuni Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

</details>

---

## `LG abbreviation`

**F1:** 0.006 | **Precision:** 0.167 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `e5b7265e`  
**Description:**
Matches 'LG' followed by city names, e.g., 'LG Innsbruck'.

**Content:**
```
\bLG\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.003 | 0.006 | 6 | 1 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 5 | 294 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `LG Wels` | `LG Wels` |

**Missed by this rule (FN):**

- `FN912691n` (business_register_number)
- `Landesgericht Klagenfurt` (organisation)
- `Holtschmidt Versicherung GmbH` (organisation)
- `Lohneis Pflege gesellschaft mbH` (organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `LG Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob68_14z`) (sent_id: `deanon_TRAIN/4Ob68_14z_22`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `LG Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_40`)


Dieser Auffassung hat sich zwischenzeitig bereits zweitinstanzliche Rechtsprechung ausdrücklich (vgl etwa LG Salzburg EFSlg 156.701 [2018], 159.791, 159.792 [2019];

**False Positives:**

- `LG Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_41`)


LG Linz EFSlg 156.702 [2018], 159.793 [2019]) und die Entscheidung 9 Ob 57/17y offensichtlich angeschlossen.

**False Positives:**

- `LG Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Ob127_14y`) (sent_id: `deanon_TRAIN/7Ob127_14y_64`)


2.1 In Deutschland setzt der Versicherungsfall „Schneedruck“ voraus, dass die versicherte Sache durch die Wirkung des Gewichts von Schnee oder Eismassen beschädigt wird (LG Meiningen r & s 2009, 69;

**False Positives:**

- `LG Meiningen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Greiner-Mai Event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `297fcc00`  
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

## `NordDaten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1edc6ba7`  
**Description:**
Matches the specific entity 'NordDaten'.

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

## `Technik Ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `687bd956`  
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

## `Vossbein Lebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `606c3ff4`  
**Description:**
Matches the specific entity 'Vossbein Lebensmittel'.

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

## `Paweltschik Telekom GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b15a7862`  
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

## `Nexgartuni Finanzen Planung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bcd7be36`  
**Description:**
Matches the specific entity 'Nexgartuni Finanzen Planung GMBH'.

**Content:**
```
\bNexgartuni\s+Finanzen\s+Planung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AlpenSicherheit GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5f0c9201`  
**Description:**
Matches the specific entity 'AlpenSicherheit GMBH'.

**Content:**
```
\bAlpenSicherheit\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinemut Smoch Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `470fcb8c`  
**Description:**
Matches the specific entity 'Reinemut + Smoch Handel' found in multiple failures.

**Content:**
```
Reinemut\s*\+\s*Smoch\s*Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7c422cd1`  
**Description:**
Matches 'FA Salzburg-Stadt' and 'Finanzamt Salzburg-Stadt' including the www. prefix.

**Content:**
```
(?:www\.)?FA\s*Salzburg\-Stadt|Finanzamt\s*Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TalVerverwerkGarten GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `92ef9b5e`  
**Description:**
Matches the specific entity 'TalVerverwerkGarten GMBH' including the ellipsis variant.

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

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Specific Compound GmbH 3`

**F1:** 0.109 | **Precision:** 0.223 | **Recall:** 0.072  

**Format:** `regex`  
**Rule ID:** `a16f5744`  
**Description:**
Matches 'Talost GMBH' and similar single word + GmbH patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.223 | 0.072 | 0.109 | 112 | 25 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 25 | 87 | 319 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Dersudheim Digital GmbH` | `Dersudheim Digital GmbH` |

**Missed by this rule (FN):**

- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)
- `Ingolf Grimpe` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Energie Conwald GmbH` | `Energie Conwald GmbH` |

**Example 3** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_5`)


Metall Monglanz GmbH, beide Johann-Puch-Straße 5, 8741 Reisstraße, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Metall Monglanz GmbH` | `Metall Monglanz GmbH` |

**Missed by this rule (FN):**

- `Johann-Puch-Straße 5, 8741 Reisstraße, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Donau-Automotive GmbH` | `Donau-Automotive GmbH` |

**Missed by this rule (FN):**

- `Dr. Ralph Kreidenweiß` (person)
- `Ebersreith 11, 8761 Götzendorf, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d__4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Josefine Rummelt und 3. Hammerla Umwelt GmbH, Friedgasse 46, 3264 Unteramt, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen die Beschlüsse des Oberlandesgerichts Graz als Rekursgericht vom 1. Februar 2013, GZ 7 R 4/13g-31 und 7 R 5/13d-32, womit die Beschlüsse des Landesgerichts Leoben vom 30. Juli 2012, GZ 2 Nc 25/11a-16, und vom 2. Oktober 2012, GZ 2 Nc 25/11a, 28/11t-22, bestätigt wurden, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hammerla Umwelt GmbH` | `Hammerla Umwelt GmbH` |

**Missed by this rule (FN):**

- `Dr. Josefine Rummelt` (person)
- `Friedgasse 46, 3264 Unteramt, Österreich` (address)

**Example 7** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Fengart GmbH` | `Fengart GmbH` |
| `LGR Medien GmbH` | `LGR Medien GmbH` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `OVX Finanzen` (organisation)
- `Analyse Kelunizor AG` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

| Predicted | Gold |
|---|---|
| `Klingenbeil Versand GmbH` | `Klingenbeil Versand GmbH` |

**Example 9** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 10** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `DonauLexlogbruckPlanung GmbH` | `DonauLexlogbruckPlanung GmbH` |

**Missed by this rule (FN):**

- `Lebensmittel Glanzconuni AG` (organisation)
- `Immanuel Gspan` (person)
- `Fridolin Braunhold` (person)
- `Mag. Frauke Steinweg` (person)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich` (address)

**Example 11** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

**Example 12** (doc_id: `deanon_TRAIN/5Ob84_16p`) (sent_id: `deanon_TRAIN/5Ob84_16p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der Rechtssache der klagenden Partei Dimitri Ringlstetter, vertreten durch Dr. Friedrich Gatscha, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Heimaluni-Event GmbH, Vorderstraß 39, 3920 Harruck, Österreich, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, 2. IJWQ Digital Services GmbH, Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich, vertreten durch Mag. Alain Danner, Rechtsanwalt in Wien, 3. Dr. Amalia Brodke, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wegen 1. Übertragung der Zusage auf Einräumung von Wohnungseigentum (30.000 EUR), 2. Einverleibung von Miteigentum (50.000 EUR), 3. Zahlung (122.785,01 EUR sA), 4. Feststellung (15.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 95.000 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. März 2016, GZ 34 R 152/15w-50, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Heimaluni-Event GmbH` | `Heimaluni-Event GmbH` |
| `IJWQ Digital Services GmbH` | `IJWQ Digital Services GmbH` |

**Missed by this rule (FN):**

- `Dimitri Ringlstetter` (person)
- `Vorderstraß 39, 3920 Harruck, Österreich` (address)
- `Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich` (address)
- `Dr. Amalia Brodke` (person)

**Example 13** (doc_id: `deanon_TRAIN/6Ob105_20i`) (sent_id: `deanon_TRAIN/6Ob105_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Josepha Imhof, vertreten durch Mag. Erwin Falkner, Rechtsanwalt in Wien, gegen die beklagte Partei R. Nieder Logmonbruck GmbH, Anselm Froncek, vertreten durch Hoffmann & Sykora Rechtsanwälte KG in Tulln, wegen 6.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 13. November 2019, GZ 21 R 208/19z-53, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Tulln vom 23. Juni 2019, GZ 11 C 276/18p-49, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Nieder Logmonbruck GmbH` | `Nieder Logmonbruck GmbH` |

**Missed by this rule (FN):**

- `Josepha Imhof` (person)
- `Anselm Froncek` (person)

**Example 14** (doc_id: `deanon_TRAIN/6Ob207_18m`) (sent_id: `deanon_TRAIN/6Ob207_18m_4`)


Balnuweit Technik GmbH, sowie 2. Ost Werkmon GmbH, alle Am Waidfeld 8, 5211 Gstöckat, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen (zuletzt) Widerrufs, Veröffentlichung und Zahlung von 9.000 EUR, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 30. Mai 2018, GZ 5 R 39/18v-27, womit über Berufung der beklagten Parteien das Urteil des Handelsgerichts Wien vom 24. Jänner 2018, GZ 39 Cg 26/17t-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Balnuweit Technik GmbH` | `Balnuweit Technik GmbH` |
| `Ost Werkmon GmbH` | `Ost Werkmon GmbH` |

**Missed by this rule (FN):**

- `Am Waidfeld 8, 5211 Gstöckat, Österreich` (address)

**Example 15** (doc_id: `deanon_TRAIN/6Ob2_12f`) (sent_id: `deanon_TRAIN/6Ob2_12f_5`)


Jakubiak Handel GmbH, Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich, 2.

| Predicted | Gold |
|---|---|
| `Jakubiak Handel GmbH` | `Jakubiak Handel GmbH` |

**Missed by this rule (FN):**

- `Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich` (address)

**Example 16** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_17`)


Diese Partner sind: Seedon-Touristik GmbH, Digital Donnor gmbh, YLHZ Umwelt GmbH oder die Verwendung sinngleicher Klauseln zuunterlassen;

| Predicted | Gold |
|---|---|
| `Seedon-Touristik GmbH` | `Seedon-Touristik GmbH` |
| `YLHZ Umwelt GmbH` | `YLHZ Umwelt GmbH` |

**Missed by this rule (FN):**

- `Digital Donnor gmbh` (organisation)

**Example 17** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_360`)


Diese Partner sind: Snajder und Frohne Marine GmbH, Uniunibach-Pharma gmbh, Betti Sanitär GmbH.

| Predicted | Gold |
|---|---|
| `Snajder und Frohne Marine GmbH` | `Snajder und Frohne Marine GmbH` |

**Missed by this rule (FN):**

- `Uniunibach-Pharma gmbh` (organisation)
- `Betti Sanitär GmbH.` (organisation)

**Example 18** (doc_id: `deanon_TRAIN/6Ob86_20w`) (sent_id: `deanon_TRAIN/6Ob86_20w_6`)


Solar Bruckstein GmbH, Scherrers Getränke, 2. SüdDerveruniMaschinenbau AG, Untere Hofäcker 14, 5771 Sinning, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 27.758,24 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 5. März 2020, GZ 1 R 4/20w-44, mit dem das Urteil des Landesgerichts St. Pölten vom 28. Oktober 2019, GZ 3 Cg 62/17m-40, bestätigt wurde, den Beschluss gefasst:  Spruch Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `Solar Bruckstein GmbH` | `Solar Bruckstein GmbH` |

**Missed by this rule (FN):**

- `Scherrers Getränke` (organisation)
- `SüdDerveruniMaschinenbau AG` (organisation)
- `Untere Hofäcker 14, 5771 Sinning, Österreich` (address)

**Example 19** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_5`)


Schefuss Forschung GmbH, beide Raidenstraße 62, 8354 Aigen, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Schefuss Forschung GmbH` | `Schefuss Forschung GmbH` |

**Missed by this rule (FN):**

- `Raidenstraße 62, 8354 Aigen, Österreich` (address)

**Example 20** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_4`)


Kraftzorstein-Telekom GmbH Karsten Öllinger, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, und 2. Univ.-Prof.in Rebecca Obermeyr GmbH Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich, vertreten durch Lederer Hoff & Apfelbacher Rechtsanwälte GmbH in Wien, wegen 11.388,49 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Juni 2019, GZ 5 R 60/19h-33, mit dem das Urteil des Handelsgerichts Wien vom 12. März 2019, GZ 51 Cg 62/17z-28, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kraftzorstein-Telekom GmbH` | `Kraftzorstein-Telekom GmbH` |

**Missed by this rule (FN):**

- `Karsten Öllinger` (person)
- `Univ.-Prof.in Rebecca Obermeyr` (person)
- `Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_4`)


Text Begründung: Die klagende GmbH mit Sitz in Wien begehrt von dem in Graz wohnhaften Beklagten die Zahlung von 5.232 EUR an Werklohn für eine Entrümpelung der Wohnungen Top 2, 3 und 4 in einem dem Beklagten gehörigen Haus in 1150 Wien.

**False Positives:**

- `Die klagende GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH` — partial — gold is substring of pred: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_8`)


Text Begründung: Im Jahr 2004 errichtete eine GmbH (im Folgenden Unternehmerin) auf einer Liegenschaft eine Stützmauer aus unvermörtelten geschlichteten Natursteinen (Steinschlichtung).

**False Positives:**

- `Im Jahr 2004 errichtete eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_38`)


Auftraggeber sei nur die GmbH gewesen.

**False Positives:**

- `Auftraggeber sei nur die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH` — partial — gold is substring of pred: `HochAnalyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HochAnalyse GmbH`(organisation)
- `Piedro Ehmken`(person)
- `Ludewigs Handel GmbH`(organisation)
- `Deborah Lochhuber`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Niemetz Metall GmbH` — partial — pred is substring of gold: `Strathewerd u. Niemetz Metall GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Assenov Sicherheit GmbH` — partial — pred is substring of gold: `Freimut & Assenov Sicherheit GmbH`
- `Eckert Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)

**Example 7** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Eckert Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)

**Example 9** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 11** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__26`)


Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH in gekürzter Form (§ 270 Abs 4 StPO) ausgefertigt wurde, verletzt es das Gesetz in § 22 Abs 5 VbVG iVm § 270 Abs 2 Z 5 StPO.“

**False Positives:**

- `Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH` — partial — gold is substring of pred: `Hup & Glossner Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hup & Glossner Solar GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH` — partial — gold is substring of pred: `VRDN Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VRDN Versand GmbH`(organisation)
- `David Tanzler`(person)
- `Dr. Livia Zinkel`(person)

**Example 13** (doc_id: `deanon_TRAIN/18OCg12_19t`) (sent_id: `deanon_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH, Jean Nellner, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Lydia Astorre, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH` — partial — gold is substring of pred: `Trabruckgart Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trabruckgart Holding GmbH`(organisation)
- `Jean Nellner`(person)
- `Lydia Astorre`(person)

**Example 14** (doc_id: `deanon_TRAIN/1Ob187_14b`) (sent_id: `deanon_TRAIN/1Ob187_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Juliana Enssle, vertreten durch Dr. Albert Heiss, Rechtsanwalt in Innsbruck, gegen den Antragsgegner PhD MedR Oskar Sträßer, vertreten durch Dr. Christian Fuchs Rechtsanwalt GmbH, Innsbruck, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse nach den §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 30. Mai 2014, GZ 52 R 76/13b-174, womit dem Rekurs des Antragsgegners nicht Folge gegeben und über Rekurs der Antragstellerin der Beschluss des Bezirksgerichts Innsbruck vom 30. November 2012, GZ 1 C 8/07f-163, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Beschluss vom 19. März 2015 wird dahin berichtigt, dass es im zweiten Absatz des Spruchs „Dem außerordentlichen Revisionsrekurs des Antragsgegners [anstelle von Antragstellers] wird teilweise Folge gegeben“ und auf Seite 5 der Begründung „Das Erstgericht verpflichtete […] den Antragsgegner zur Leistung […] lautet.

**False Positives:**

- `Christian Fuchs Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Juliana Enssle`(person)
- `PhD MedR Oskar Sträßer`(person)

**Example 15** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Sandmeier IT GmbH` — partial — pred is substring of gold: `Boothe u. Sandmeier IT GmbH`
- `Farhad Paya Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 17** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH, Gabriel van Straaten, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Olaf Doerrien, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH` — partial — gold is substring of pred: `Ibrahim Gerlicher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ibrahim Gerlicher`(person)
- `Gabriel van Straaten`(person)
- `Olaf Doerrien`(person)

**Example 18** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH` — partial — gold is substring of pred: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 19** (doc_id: `deanon_TRAIN/1Ob51_14b`) (sent_id: `deanon_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH, Erhard Blaufuß, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

**False Positives:**

- `Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH` — partial — gold is substring of pred: `Landwirtschaft Glanzlemglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwirtschaft Glanzlemglanz GmbH`(organisation)
- `Erhard Blaufuß`(person)

**Example 20** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_7`)


Die GmbH verkaufte diesen ohne sein Wissen an ihre rumänische Tochtergesellschaft, die ihn an einen Kunden weiterverkaufte.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_44`)


Dem Vorwurf, der Beklagte habe es verabsäumt, einem (irrtümlichen) Verkauf fremder Fahrzeuge und Maschinen durch die GmbH durch ein geeignetesKontrollsystem vorzubeugen(vgl RS0023927), sind die Feststellungen entgegenzuhalten: Er hatte ein System eingeführt, nach dem alle auf Betriebsliegenschaften der GmbH befindlichen Geräte und Maschinen in Listen eingetragen und die jeweiligen Eigentümer vermerkt wurden, sodass über im fremden Eigentum stehende Sachen keine Rechnung und kein Lieferschein ausgestellt werden konnten.

**False Positives:**

- `Verkauf fremder Fahrzeuge und Maschinen durch die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/1Ob7_20s`) (sent_id: `deanon_TRAIN/1Ob7_20s_5`)


Francois Klingsoehr, vertreten durch die Dr. Schartner Rechtsanwalt GmbH, Altenmarkt im Pongau, gegen die beklagte Partei Egon Lammprecht, vertreten durch Dr. Reinfried Eberl und andere Rechtsanwälte in Salzburg, wegen Wiederherstellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 20. November 2019, GZ 22 R 322/19k-13, mit dem das Urteil des Bezirksgerichts St. Johann im Pongau vom 12. September 2019, GZ 2 C 152/19t-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Entscheidungen der Vorinstanzen werden aus Anlass der Revision einschließlich des durchgeführten Verfahrens als nichtig aufgehoben.

**False Positives:**

- `Schartner Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Francois Klingsoehr`(person)
- `Egon Lammprecht`(person)

**Example 23** (doc_id: `deanon_TRAIN/1Ob82_18t`) (sent_id: `deanon_TRAIN/1Ob82_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH, Oskar Stelzel, vertreten durch die KRONBERGER Rechtsanwälte Gesellschaft mbH, Wien, gegen die beklagte Partei Brian Hüpsch, vertreten durch Dr. Werner Loos, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. März 2018, GZ 38 R 303/17s-48, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 4. August 2017, GZ 22 C 163/16w-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH` — partial — gold is substring of pred: `MurUmwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MurUmwelt GmbH`(organisation)
- `Oskar Stelzel`(person)
- `Brian Hüpsch`(person)

**Example 24** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

**False Positives:**

- `Er selbst war ua als Fenstermonteur in der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/2Ob194_24d`) (sent_id: `deanon_TRAIN/2Ob194_24d_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Rut Dolff, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Samuel Nachtwei, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Simon Wallner Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rut Dolff`(person)
- `Samuel Nachtwei`(person)

**Example 26** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

**False Positives:**

- `Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH` — partial — gold is substring of pred: `Ostvallem-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ostvallem-Robotik GmbH`(organisation)

**Example 27** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

**False Positives:**

- `Dabei wiesen die anwesenden Mitarbeiter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_63`)


Eine Plakette mit Namen, Anschrift und Kontaktdaten der GmbH war auch auf dem an den Kläger verkauften Gerät angebracht.

**False Positives:**

- `Anschrift und Kontaktdaten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_78`)


Die Bachtri GmbH hat vor der Auslieferung des neu zusammengesetzten Geräts eine Druckprobe durchgeführt.

**False Positives:**

- `Die Bachtri GmbH` — partial — gold is substring of pred: `Bachtri GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachtri GmbH`(organisation)

**Example 30** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_80`)


Die Maerklin und Steckelmann Software GmbH befüllte den neu zusammengesetzten Luftentfeuchter Anfang 2011 mit dem Kältemittel R22, dessen Verwendung seit 1. 1.

**False Positives:**

- `Die Maerklin und Steckelmann Software GmbH` — partial — gold is substring of pred: `Maerklin und Steckelmann Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maerklin und Steckelmann Software GmbH`(organisation)

**Example 31** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH` — partial — gold is substring of pred: `Waldzorval Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)

**Example 32** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH` — partial — gold is substring of pred: `Stadt-Robotik GmbH`
- `Partner Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Ing. Verona Obersteiner`(person)

**Example 33** (doc_id: `deanon_TRAIN/3Ob12_11b`) (sent_id: `deanon_TRAIN/3Ob12_11b_30`)


5. Die Beurteilung des Berufungsgerichts, der Oppositionskläger habe ausreichend dargetan, dass die von ihm behobenen Beträge in Höhe von insgesamt 114.500 EUR in den Bilanzen der GmbH nicht verbucht wurden, weshalb er auch in diesem Umfang der Titelverpflichtung entsprochen habe, wirft ebenfalls keine im Rahmen einer außerordentlichen Revision aufzugreifende erhebliche Rechtsfrage auf: Es steht durch die gelegte Rechnung in Verbindung mit den Bilanzen der GmbH, in deren Besitz der Oppositionsbeklagte unstrittig ist, fest, dass weder der Gesamtbetrag von 114.500 EUR noch Teilbeträge davon in den Bilanzen der GmbH verbucht wurde.

**False Positives:**

- `Es steht durch die gelegte Rechnung in Verbindung mit den Bilanzen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH` — partial — gold is substring of pred: `Kraftnorost Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 35** (doc_id: `deanon_TRAIN/3Ob150_16d`) (sent_id: `deanon_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH, Hon.-Prof.in Dr.in Silvana Früboes, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Talseemon GmbH, Finn Auctor, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

**False Positives:**

- `Kodek als weitere Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH` — partial — gold is substring of pred: `SGQ Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SGQ Versand GmbH`(organisation)
- `Hon.-Prof.in Dr.in Silvana Früboes`(person)
- `Talseemon GmbH`(organisation)
- `Finn Auctor`(person)

**Example 36** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH` — partial — gold is substring of pred: `Bruckgartver GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 37** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH` — partial — gold is substring of pred: `Nexostlem GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

**Example 38** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH, Hubert Englmaier, vertreten durch Dr. Martin Holzer, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Florian Corvetti, vertreten durch Dr. Heimo Jilek, Rechtsanwalt in Leoben, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Berufungsgericht vom 3. November 2010, GZ 1 R 244/10i-34, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Leoben vom 9. Juni 2010, GZ 5 C 315/09y-28, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision der klagenden Partei wird Folge gegeben, das angefochtene Urteil aufgehoben und die Rechtssache zur neuerlichen Entscheidung an das Berufungsgericht zurückverwiesen.

**False Positives:**

- `Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH` — partial — gold is substring of pred: `Riecken Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Riecken Maschinenbau GmbH`(organisation)
- `Hubert Englmaier`(person)
- `Florian Corvetti`(person)

**Example 39** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH, Esra Bubenischek, vertreten durch Mag. Gerold Schwarzer, Rechtsanwalt in Wien, gegen die beklagte und widerklagende Partei HR Hilde vom Dorf, wegen 286.300,47 EUR sA und 41.219,24 EUR sA, über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Februar 2021, GZ 1 R 168/20m-26, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stefula als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH` — partial — gold is substring of pred: `Gambal Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gambal Software GmbH`(organisation)
- `Esra Bubenischek`(person)
- `HR Hilde vom Dorf`(person)

**Example 40** (doc_id: `deanon_TRAIN/4Ob145_18d`) (sent_id: `deanon_TRAIN/4Ob145_18d_4`)


Matzka und Dr. Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH, Lieselotte Wesp, vertreten durch Hauswirth - Kleiber Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1) DI Amber Rzehatschek, 2) DI Esra Noth, ebendort, beide vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, 3) Trinks Möbel GmbH, Hütten 15, 5221 Lasberg, Österreich, vertreten durch Mag. Thomas Stenitzer und Mag. Kurt Schick, Rechtsanwälte in Laa an der Thaya, und 4) DI (FH) Wladimir Runzheimer, vertreten durch Mag. Bernhard Österreicher, Rechtsanwalt in Pfaffstätten, wegen 127.614,09 EUR sA und Feststellung (Streitwert: 5.200 EUR), über die außerordentliche Revision der erst- und zweitbeklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. April 2018, GZ 1 R 179/17a-29, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH` — partial — gold is substring of pred: `MGL Forschung Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MGL Forschung Consulting GmbH`(organisation)
- `Lieselotte Wesp`(person)
- `DI Amber Rzehatschek`(person)
- `DI Esra Noth`(person)
- `Trinks Möbel GmbH`(organisation)
- `Hütten 15, 5221 Lasberg, Österreich`(address)
- `Wladimir Runzheimer`(person)

**Example 41** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH` — partial — gold is substring of pred: `XDC Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 42** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Jörg Drathschmidt, vertreten durch Dr. Winfried Sattlegger und andere Rechtsanwälte in Linz, gegen die beklagte Partei Wien Dorfsud GmbH, Gerlinde Balcerzak, vertreten durch Dr. Helmut Trenkwalder, Rechtsanwalt in Linz, und die Nebenintervenientin auf Seiten der beklagten Partei Waldfen-Versand GmbH, Eva Boztas, vertreten durch Schneider & Schneider Rechtsanwalts GmbH in Wien, wegen 35.628,94 EUR sA Zug um Zug gegen Herausgabe eines Fahrzeugs, über den Rekurs der Nebenintervenientin gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 7. November 2019, GZ 6 R 114/19f-41, mit dem das Urteil des Landesgerichts Linz vom 3. Juli 2019, GZ 36 Cg 4/17m-36, im klagsstattgebenden Teil (Spruchpunkt 1.) aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Schneider Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jörg Drathschmidt`(person)
- `Wien Dorfsud GmbH`(organisation)
- `Gerlinde Balcerzak`(person)
- `Waldfen-Versand GmbH`(organisation)
- `Eva Boztas`(person)

**Example 43** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH` — partial — gold is substring of pred: `Dueckers Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 44** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH` — partial — gold is substring of pred: `Kraftheimglanz-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftheimglanz-Versand GmbH`(organisation)

**Example 45** (doc_id: `deanon_TRAIN/4Ob224_23d`) (sent_id: `deanon_TRAIN/4Ob224_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, den Hofrat Mag. Dr. Wurdinger und die Hofrätin Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH, Andreas Häntsch, Deutschland, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Emma Bergner kammer, Cathleen Hofschulte, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, wegen Unterlassung, Widerruf und Veröffentlichung desselben (Gesamtstreitwert 46.200 EUR), aus Anlass der außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Oktober 2023, GZ 4 R 99/23t-32, mit dem das Urteil des Handelsgerichts Wien vom 27. April 2023, GZ 57 Cg 34/21g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die gemeinsame Anzeige beider Parteien vom 27. August 2024 über das vereinbarte Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH` — partial — gold is substring of pred: `Verlexglanz-Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verlexglanz-Marine GmbH`(organisation)
- `Andreas Häntsch`(person)
- `Emma Bergner`(person)
- `Cathleen Hofschulte`(person)

**Example 46** (doc_id: `deanon_TRAIN/4Ob26_20g`) (sent_id: `deanon_TRAIN/4Ob26_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH, Corbinian Wischnowski, LLM, vertreten durch Rechtsanwaltskanzlei Dr. Wendling GmbH in Kitzbühel, gegen die beklagte Partei Osttallem Getränke GmbH, Zdenko Weimer, BA, Deutschland, vertreten durch Dr. Dan Katzlinger, Rechtsanwalt in Innsbruck, wegen 70.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Dezember 2019, GZ 10 R 49/19k-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH` — partial — gold is substring of pred: `Evelyn Peterhansel`
- `Wendling GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Evelyn Peterhansel`(person)
- `Corbinian Wischnowski, LLM`(person)
- `Osttallem Getränke GmbH`(organisation)
- `Zdenko Weimer, BA`(person)

**Example 47** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Lovrek sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Dr. Sean Schoenenborn, gegen die beklagte Partei Dr. Hagen Kanat, vertreten durch Eisenberger & Herzog Rechtsanwalts GmbH in Graz, wegen 234.164,98 EUR sA, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, gemäß § 31 JN anstelle des Landesgerichts für Zivilrechtssachen Graz das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben, zur Verhandlung und Entscheidung dieser Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Herzog Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Sean Schoenenborn`(person)
- `Dr. Hagen Kanat`(person)

**Example 48** (doc_id: `deanon_TRAIN/5Ob129_18h`) (sent_id: `deanon_TRAIN/5Ob129_18h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Futerer u. Dirrnagel Luftfahrt GmbH, Susette Wülfken, vertreten durch Dr. Stefan Hoffmann, Dr. Thomas Herzog, Rechtsanwälte in Vöcklabruck, gegen die beklagte Partei Doris Grosscurth, vertreten durch Mag. Percy Hirsch, Rechtsanwalt in Wels, wegen 5.092,80 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. April 2018, GZ 22 R 135/18m-47, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Dirrnagel Luftfahrt GmbH` — partial — pred is substring of gold: `Futerer u. Dirrnagel Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Futerer u. Dirrnagel Luftfahrt GmbH`(organisation)
- `Susette Wülfken`(person)
- `Doris Grosscurth`(person)

**Example 49** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Penners Medien GmbH, Wilhelmine Kobinger, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei JRQA Landwirtschaft Rechtsanwälte GmbH, Kometenweg 43, 3200 Rennersdorf, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Steger als weitere Richter in der Rechtssache der klagenden Partei Penners Medien GmbH` — partial — gold is substring of pred: `Penners Medien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Penners Medien GmbH`(organisation)
- `Wilhelmine Kobinger`(person)
- `JRQA Landwirtschaft`(organisation)
- `Kometenweg 43, 3200 Rennersdorf, Österreich`(address)

**Example 50** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_31`)


Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH gegenüber Dritten könne außerdem mit einem Interessenkonflikt zwischen der Gesellschaft und dem Mehrheitsgesellschafter keinesfalls begründet werden.

**False Positives:**

- `Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_80`)


Wird eine GmbH durch einen Dritten geschädigt, ist der dem Gesellschafter dadurch entstehende Nachteil in seinem Vermögen ein nicht ersatzfähiger mittelbarer Schaden.

**False Positives:**

- `Wird eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/5Ob184_21a`) (sent_id: `deanon_TRAIN/5Ob184_21a_4`)


Techn R Jaden Damcke, 2. Florian Adatepe, ebenda, beide vertreten durch Schlösser & Partner Rechtsanwälte OG in Wien, gegen die Antragsgegnerin Xenia Droeßler, vertreten durch Mag. Michael Operschal Rechtsanwalt GmbH in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den Revisionsrekurs der Antragsteller gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Mai 2021, GZ 40 R 2/21x-15, mit dem der Sachbeschluss des Bezirksgerichts Floridsdorf vom 30. Oktober 2020, GZ 28 Msch 9/19g-11, abgeändert wurde, den Sachbeschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Michael Operschal Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Techn R Jaden Damcke`(person)
- `Florian Adatepe`(person)
- `Xenia Droeßler`(person)

**Example 53** (doc_id: `deanon_TRAIN/5Ob221_22v`) (sent_id: `deanon_TRAIN/5Ob221_22v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH in Liquidation, Steugasse 3, 6123 Vomperbach, Österreich, vertreten durch Mag. Gottfried Tazol, Rechtsanwalt in Völkermarkt, gegen die beklagte Partei SeeSanitär AG, Helge Schreyvogel, BEd, vertreten durch Mag. Alexander Todor-Kostic LL.M., Mag. Silke Todor-Kostic, Rechtsanwälte in Velden am Wörthersee, wegen 84.999,13 EUR sA, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 62.200,50 EUR sA) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. Oktober 2022, GZ 5 R 74/22z-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Steger als weitere Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH` — partial — gold is substring of pred: `Fabian + Michailoff Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fabian + Michailoff Analyse GmbH`(organisation)
- `Steugasse 3, 6123 Vomperbach, Österreich`(address)
- `SeeSanitär AG`(organisation)
- `Helge Schreyvogel, BEd`(person)

**Example 54** (doc_id: `deanon_TRAIN/5Ob93_24y`) (sent_id: `deanon_TRAIN/5Ob93_24y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH, Florenzia Lohmöller, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dipl.-Ing. Juliana Maurice, wegen Unterfertigung eines Wohnungseigentumsvertrags und Feststellung, hier: Anmerkung der Klage, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 26. April 2024, GZ 15 R 41/24w-18, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 126 Abs 1 GBG iVm § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH` — partial — gold is substring of pred: `Jozwiak Robotik GmbH`
- `Damian GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Jozwiak Robotik GmbH`(organisation)
- `Florenzia Lohmöller`(person)
- `Dipl.-Ing. Juliana Maurice`(person)

**Example 55** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Gitschthaler als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätinnen Dr. Kodek und Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei MurFinanzen GmbH, OStR Thorsten Bobb, vertreten durch Dr. Ralph Mayer, Rechtsanwalt in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei MurFinanzen GmbH` — partial — gold is substring of pred: `MurFinanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MurFinanzen GmbH`(organisation)
- `OStR Thorsten Bobb`(person)

**Example 56** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH, Ilona Hoernle, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Wickl Logistik GmbH, Vitus Glassbrenner, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH` — partial — gold is substring of pred: `Unlandherm KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unlandherm KI GmbH`(organisation)
- `Ilona Hoernle`(person)
- `Wickl Logistik GmbH`(organisation)
- `Vitus Glassbrenner`(person)

**Example 57** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_6`)


Die GmbH war Eigentümerin einer Liegenschaft, der Beklagte ist Eigentümer der Nachbarliegenschaft.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_10`)


Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH verbüchert.

**False Positives:**

- `Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_12`)


Die GmbH wurde 2018 gemäß § 40 FBG wegen Vermögenslosigkeit im Firmenbuch gelöscht.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der Schenker Elektro GmbH, FN FN119011j, wegen § 10 Abs 2 FBG, über den Revisionsrekurs des Österreichischen Verbandes Gemeinnütziger Bauvereinigungen Revisionsverband, 1010 Wien, Bösendorferstraße 7, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 3. September 2020, GZ 6 R 158/20d-6, womit der Rekurs gegen den Beschluss des Handelsgerichts Wien vom 20. Juli 2020, GZ 72 Fr 3266/20f-3, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Faber als weitere Richter in der Firmenbuchsache der Schenker Elektro GmbH` — partial — gold is substring of pred: `Schenker Elektro GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schenker Elektro GmbH`(organisation)
- `FN119011j`(business_register_number)

**Example 61** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

**False Positives:**

- `Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH` — partial — gold is substring of pred: `FN110230q`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN110230q`(business_register_number)
- `Seetra-Recycling GmbH`(organisation)

**Example 62** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_155`)


Abs 1 lit a WGG kann durch Zwischenschaltung einer GmbH umgangen werden.

**False Positives:**

- `Abs 1 lit a WGG kann durch Zwischenschaltung einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH` — partial — gold is substring of pred: `FN912691n`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN912691n`(business_register_number)
- `Landesgericht Klagenfurt`(organisation)
- `Holtschmidt Versicherung GmbH`(organisation)
- `LG Wels`(organisation)
- `Lohneis Pflege gesellschaft mbH`(organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich`(address)

**Example 65** (doc_id: `deanon_TRAIN/6Ob69_23z`) (sent_id: `deanon_TRAIN/6Ob69_23z_34`)


Die (vom Beklagten vorgelegte) Vereinbarung mit der GmbH entspreche nicht der von der Klägerin behaupteten, weil die Regelung des Entgelts (eines Zuschlags von 20 %) darin fehle.

**False Positives:**

- `Vereinbarung mit der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/7Ob141_16k`) (sent_id: `deanon_TRAIN/7Ob141_16k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Seedorf Vertrieb GmbH, Felix Bernloehr, vertreten durch Dr. Helmut Fetz und andere, Rechtsanwälte in Leoben, gegen die beklagte Partei Mlynarik Handel Aktiengesellschaft, Veropastraße 16, 2413 Edelstal, Österreich, vertreten durch Dr. Heimo Jilek und Dr. Martin Sommer, Rechtsanwälte in Leoben, wegen 61.848,15 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 25. Mai 2016, GZ 5 R 9/16g-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Singer als weitere Richter in der Rechtssache der klagenden Partei Seedorf Vertrieb GmbH` — partial — gold is substring of pred: `Seedorf Vertrieb GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Seedorf Vertrieb GmbH`(organisation)
- `Felix Bernloehr`(person)
- `Mlynarik Handel Aktiengesellschaft`(organisation)
- `Veropastraße 16, 2413 Edelstal, Österreich`(address)

**Example 67** (doc_id: `deanon_TRAIN/7Ob180_16w`) (sent_id: `deanon_TRAIN/7Ob180_16w_4`)


Dr. Arnd Anagnostou, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Helge Brookhoff, vertreten durch Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, wegen Ehescheidung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juni 2016, GZ 42 R 130/16b-33, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Dezember 2015, GZ 3 C 9/14w-27, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Damian GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Arnd Anagnostou`(person)
- `Helge Brookhoff`(person)

**Example 68** (doc_id: `deanon_TRAIN/7Ob31_19p`) (sent_id: `deanon_TRAIN/7Ob31_19p_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Alpen Traostal GmbH, Florens Mühle, vertreten durch Mag. Stefan Korab, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. RheinImmobilien Gesellschaft mbH, Melcherweg 193, 8242 Kronegg, Österreich, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, wegen 151.623,74 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 20. Dezember 2018, GZ 129 R 98/18g-76, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Alpen Traostal GmbH` — partial — gold is substring of pred: `Alpen Traostal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen Traostal GmbH`(organisation)
- `Florens Mühle`(person)
- `RheinImmobilien Gesellschaft mbH`(organisation)
- `Melcherweg 193, 8242 Kronegg, Österreich`(address)

**Example 69** (doc_id: `deanon_TRAIN/7Ob35_16x`) (sent_id: `deanon_TRAIN/7Ob35_16x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei NGU Energie Dienstleistungen GmbH, Noah Rübke, vertreten durch Köhler Draskovits Unger Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Franziskus Rußkamp, vertreten durch Dr. Hans Wagner, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 9. Dezember 2015, GZ 39 R 367/15g-26, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Singer als weitere Richter in der Rechtssache der klagenden Partei NGU Energie Dienstleistungen GmbH` — partial — gold is substring of pred: `NGU Energie Dienstleistungen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NGU Energie Dienstleistungen GmbH`(organisation)
- `Noah Rübke`(person)
- `Franziskus Rußkamp`(person)

**Example 70** (doc_id: `deanon_TRAIN/7Ob4_12g`) (sent_id: `deanon_TRAIN/7Ob4_12g_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei TVOW Verlag GmbH, Werner Megerlein, vertreten durch Dr. Roland Kometer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Bruckzor Umwelt Services GmbH, Valerian Landwehrkamp, vertreten durch Rainer Kurbos, Rechtsanwalt in Graz, wegen 8.635,55 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 25. Oktober 2011, GZ 1 R 84/11a-18, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Wurdinger als weitere Richter in der Rechtssache der klagenden Partei TVOW Verlag GmbH` — partial — gold is substring of pred: `TVOW Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TVOW Verlag GmbH`(organisation)
- `Werner Megerlein`(person)
- `Bruckzor Umwelt Services GmbH`(organisation)
- `Valerian Landwehrkamp`(person)

**Example 71** (doc_id: `deanon_TRAIN/7Ob63_18t`) (sent_id: `deanon_TRAIN/7Ob63_18t_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Automotive Bergartglanz GmbH, Denis Leithe, vertreten durch Dr. Erwin Markl, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Bruckfen Manufaktur GmbH, Jeannine Orthel, vertreten durch Graf & Pitkowitz, Rechtsanwälte GmbH in Wien, wegen 31.500 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2018, GZ 2 R 130/17b-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Automotive Bergartglanz GmbH` — partial — gold is substring of pred: `Automotive Bergartglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Automotive Bergartglanz GmbH`(organisation)
- `Denis Leithe`(person)
- `Bruckfen Manufaktur GmbH`(organisation)
- `Jeannine Orthel`(person)

**Example 72** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_4`)


Kraftzorstein-Telekom GmbH Karsten Öllinger, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, und 2. Univ.-Prof.in Rebecca Obermeyr GmbH Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich, vertreten durch Lederer Hoff & Apfelbacher Rechtsanwälte GmbH in Wien, wegen 11.388,49 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Juni 2019, GZ 5 R 60/19h-33, mit dem das Urteil des Handelsgerichts Wien vom 12. März 2019, GZ 51 Cg 62/17z-28, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Eckert Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kraftzorstein-Telekom GmbH`(organisation)
- `Karsten Öllinger`(person)
- `Univ.-Prof.in Rebecca Obermeyr`(person)
- `Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich`(address)

**Example 73** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Krollpfeifer Wind GmbH` — partial — pred is substring of gold: `Abramczyk & Krollpfeifer Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

**Example 74** (doc_id: `deanon_TRAIN/8Ob92_16m`) (sent_id: `deanon_TRAIN/8Ob92_16m_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn sowie die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Familienrechtssache des Antragstellers Dr. Erhard Jungscholz, vertreten durch PHH Prochaska Havranek Rechtsanwälte GmbH in Wien, wider den Antragsgegner Techn R Lothar Vogelbein, vertreten durch Dr. Robert Steiner Rechtsanwalt GmbH in Spittal an der Drau, wegen Unterhalt, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 28. Juli 2016, GZ 3 R 112/16d-29, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Robert Steiner Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Erhard Jungscholz`(person)
- `Techn R Lothar Vogelbein`(person)

**Example 75** (doc_id: `deanon_TRAIN/8Ob97_23g`) (sent_id: `deanon_TRAIN/8Ob97_23g_4`)


Matzka, Dr. Stefula und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Bartholomaeus Digital GmbH, Dorothea Siemers, vertreten durch Dr. Hanno Hofmann, Rechtsanwalt in Graz, gegen die beklagte Partei Winceck Solar GmbH, Rupert Frangenberg, vertreten durch Mag. Dr. Günther Schmied, Rechtsanwalt in Graz, wegen Übergabeauftrags, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 21. Juni 2023, GZ 5 R 26/23i-49, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Graz-West vom 29. Dezember 2022, GZ 111 C 5/22w-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Thunhart als weitere Richter in der Rechtssache der klagenden Partei Bartholomaeus Digital GmbH` — partial — gold is substring of pred: `Bartholomaeus Digital GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bartholomaeus Digital GmbH`(organisation)
- `Dorothea Siemers`(person)
- `Winceck Solar GmbH`(organisation)
- `Rupert Frangenberg`(person)

**Example 76** (doc_id: `deanon_TRAIN/8ObA10_21k`) (sent_id: `deanon_TRAIN/8ObA10_21k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner (aus dem Kreis der Arbeitgeber) und Wolfgang Jelinek (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Thebuss + Großekemper Bildung AG, Univ.-Prof.in Anna Helffer, vertreten durch Dr. Raimund Gehart, Rechtsanwalt in Wien, gegen die beklagte Partei Paulina Strnadl, vertreten durch Dr. Franz Josef Hofer Rechtsanwalt GmbH in Friesach, wegen 5.625,88 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. Dezember 2020, GZ 6 Ra 69/20v-19, mit dem das Urteil des Landesgerichts Klagenfurt als Arbeits- und Sozialgericht vom 15. Mai 2020, GZ 35 Cga 90/19x-11, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Franz Josef Hofer Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Thebuss + Großekemper Bildung AG`(organisation)
- `Univ.-Prof.in Anna Helffer`(person)
- `Paulina Strnadl`(person)

**Example 77** (doc_id: `deanon_TRAIN/8ObA21_11p`) (sent_id: `deanon_TRAIN/8ObA21_11p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Dr. Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke GmbH & Co OG, Heinickegasse 3x, 4984 Klingersberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Waltraud Seckl, vertreten durch Dr. Friedrich Schubert, Rechtsanwalt in Wien, wegen 19.335,55 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 31. Jänner 2011, GZ 7 Ra 121/10f-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke GmbH` — partial — gold is substring of pred: `Wilost Garten Werke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilost Garten Werke GmbH`(organisation)
- `Heinickegasse 3x, 4984 Klingersberg, Österreich`(address)
- `Ing. Waltraud Seckl`(person)

**Example 78** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Dehn und den Hofrat des Obersten Gerichtshofs Dr. Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei WestSicherheit GmbH, OMedR Paulina von Tietzen, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Amber Landscheid, vertreten durch Dr. Karl-Heinz Plankel, Dr. Herwig Mayrhofer ua, Rechtsanwälte in Dornbirn, wegen 15.600 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, anstelle des Landesgerichts Salzburg als Arbeits- und Sozialgericht das Arbeits- und Sozialgericht Wien zur Verhandlung und Entscheidung der Rechtssache des Landesgerichts Salzburg als Arbeits- und Sozialgericht AZ 15 Cga 88/15d zu bestimmen, wird abgewiesen.

**False Positives:**

- `Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei WestSicherheit GmbH` — partial — gold is substring of pred: `WestSicherheit GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WestSicherheit GmbH`(organisation)
- `OMedR Paulina von Tietzen`(person)
- `Amber Landscheid`(person)

**Example 79** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_29`)


[5] Die Wald Lemsudlex GmbH informierte den Kläger am 19. 10. 2016 darüber, dass die benötigte Software zur Verfügung stehe und sein Fahrzeug nun (kostenlos) umprogrammiert werden könne.

**False Positives:**

- `Die Wald Lemsudlex GmbH` — partial — gold is substring of pred: `Wald Lemsudlex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wald Lemsudlex GmbH`(organisation)

</details>

---

## `General GMBH Company`

**F1:** 0.048 | **Precision:** 0.143 | **Recall:** 0.029  

**Format:** `regex`  
**Rule ID:** `4df85cb0`  
**Description:**
Matches companies ending in GmbH, ensuring strict boundaries to avoid capturing preceding context.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?(?!(?:Partei|Die|Der|des|der|von|der|in|mit|auf|an|bei|nach|vor|zu|für|um|ohne|durch|gegen|über|unter|neben|zwischen|entlang|statt|außer|bis|seit|während|wegen|trotz|dank|laut|gemäß|entsprechend|Richter|Senatspräsident|Hofrat|Hofrätin|Mag\.|Dr\.)(?:\s+|\n))(?![A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+GmbH)([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.143 | 0.029 | 0.048 | 70 | 10 | 60 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 60 | 332 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Donau-Automotive GmbH` | `Donau-Automotive GmbH` |

**Missed by this rule (FN):**

- `Dr. Ralph Kreidenweiß` (person)
- `Ebersreith 11, 8761 Götzendorf, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `LGR Medien GmbH` | `LGR Medien GmbH` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `OVX Finanzen` (organisation)
- `Analyse Kelunizor AG` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `DonauLexlogbruckPlanung GmbH` | `DonauLexlogbruckPlanung GmbH` |

**Missed by this rule (FN):**

- `Lebensmittel Glanzconuni AG` (organisation)
- `Immanuel Gspan` (person)
- `Fridolin Braunhold` (person)
- `Mag. Frauke Steinweg` (person)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/5Ob84_16p`) (sent_id: `deanon_TRAIN/5Ob84_16p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der Rechtssache der klagenden Partei Dimitri Ringlstetter, vertreten durch Dr. Friedrich Gatscha, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Heimaluni-Event GmbH, Vorderstraß 39, 3920 Harruck, Österreich, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, 2. IJWQ Digital Services GmbH, Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich, vertreten durch Mag. Alain Danner, Rechtsanwalt in Wien, 3. Dr. Amalia Brodke, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wegen 1. Übertragung der Zusage auf Einräumung von Wohnungseigentum (30.000 EUR), 2. Einverleibung von Miteigentum (50.000 EUR), 3. Zahlung (122.785,01 EUR sA), 4. Feststellung (15.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 95.000 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. März 2016, GZ 34 R 152/15w-50, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Heimaluni-Event GmbH` | `Heimaluni-Event GmbH` |
| `IJWQ Digital Services GmbH` | `IJWQ Digital Services GmbH` |

**Missed by this rule (FN):**

- `Dimitri Ringlstetter` (person)
- `Vorderstraß 39, 3920 Harruck, Österreich` (address)
- `Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich` (address)
- `Dr. Amalia Brodke` (person)

**Example 5** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_17`)


Diese Partner sind: Seedon-Touristik GmbH, Digital Donnor gmbh, YLHZ Umwelt GmbH oder die Verwendung sinngleicher Klauseln zuunterlassen;

| Predicted | Gold |
|---|---|
| `Seedon-Touristik GmbH` | `Seedon-Touristik GmbH` |
| `YLHZ Umwelt GmbH` | `YLHZ Umwelt GmbH` |

**Missed by this rule (FN):**

- `Digital Donnor gmbh` (organisation)

**Example 6** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_360`)


Diese Partner sind: Snajder und Frohne Marine GmbH, Uniunibach-Pharma gmbh, Betti Sanitär GmbH.

| Predicted | Gold |
|---|---|
| `Snajder und Frohne Marine GmbH` | `Snajder und Frohne Marine GmbH` |

**Missed by this rule (FN):**

- `Uniunibach-Pharma gmbh` (organisation)
- `Betti Sanitär GmbH.` (organisation)

**Example 7** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_4`)


Kraftzorstein-Telekom GmbH Karsten Öllinger, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, und 2. Univ.-Prof.in Rebecca Obermeyr GmbH Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich, vertreten durch Lederer Hoff & Apfelbacher Rechtsanwälte GmbH in Wien, wegen 11.388,49 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Juni 2019, GZ 5 R 60/19h-33, mit dem das Urteil des Handelsgerichts Wien vom 12. März 2019, GZ 51 Cg 62/17z-28, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kraftzorstein-Telekom GmbH` | `Kraftzorstein-Telekom GmbH` |

**Missed by this rule (FN):**

- `Karsten Öllinger` (person)
- `Univ.-Prof.in Rebecca Obermeyr` (person)
- `Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH` — partial — gold is substring of pred: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_8`)


Text Begründung: Im Jahr 2004 errichtete eine GmbH (im Folgenden Unternehmerin) auf einer Liegenschaft eine Stützmauer aus unvermörtelten geschlichteten Natursteinen (Steinschlichtung).

**False Positives:**

- `Im Jahr 2004 errichtete eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_38`)


Auftraggeber sei nur die GmbH gewesen.

**False Positives:**

- `Auftraggeber sei nur die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH` — partial — gold is substring of pred: `HochAnalyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HochAnalyse GmbH`(organisation)
- `Piedro Ehmken`(person)
- `Ludewigs Handel GmbH`(organisation)
- `Deborah Lochhuber`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__26`)


Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH in gekürzter Form (§ 270 Abs 4 StPO) ausgefertigt wurde, verletzt es das Gesetz in § 22 Abs 5 VbVG iVm § 270 Abs 2 Z 5 StPO.“

**False Positives:**

- `Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH` — partial — gold is substring of pred: `Hup & Glossner Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hup & Glossner Solar GmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH` — partial — gold is substring of pred: `VRDN Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VRDN Versand GmbH`(organisation)
- `David Tanzler`(person)
- `Dr. Livia Zinkel`(person)

**Example 9** (doc_id: `deanon_TRAIN/18OCg12_19t`) (sent_id: `deanon_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH, Jean Nellner, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Lydia Astorre, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH` — partial — gold is substring of pred: `Trabruckgart Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trabruckgart Holding GmbH`(organisation)
- `Jean Nellner`(person)
- `Lydia Astorre`(person)

**Example 10** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 11** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Sandmeier IT GmbH` — partial — pred is substring of gold: `Boothe u. Sandmeier IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 12** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH, Gabriel van Straaten, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Olaf Doerrien, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH` — partial — gold is substring of pred: `Ibrahim Gerlicher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ibrahim Gerlicher`(person)
- `Gabriel van Straaten`(person)
- `Olaf Doerrien`(person)

**Example 13** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH` — partial — gold is substring of pred: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 14** (doc_id: `deanon_TRAIN/1Ob51_14b`) (sent_id: `deanon_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH, Erhard Blaufuß, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

**False Positives:**

- `Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH` — partial — gold is substring of pred: `Landwirtschaft Glanzlemglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwirtschaft Glanzlemglanz GmbH`(organisation)
- `Erhard Blaufuß`(person)

**Example 15** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_44`)


Dem Vorwurf, der Beklagte habe es verabsäumt, einem (irrtümlichen) Verkauf fremder Fahrzeuge und Maschinen durch die GmbH durch ein geeignetesKontrollsystem vorzubeugen(vgl RS0023927), sind die Feststellungen entgegenzuhalten: Er hatte ein System eingeführt, nach dem alle auf Betriebsliegenschaften der GmbH befindlichen Geräte und Maschinen in Listen eingetragen und die jeweiligen Eigentümer vermerkt wurden, sodass über im fremden Eigentum stehende Sachen keine Rechnung und kein Lieferschein ausgestellt werden konnten.

**False Positives:**

- `Verkauf fremder Fahrzeuge und Maschinen durch die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/1Ob82_18t`) (sent_id: `deanon_TRAIN/1Ob82_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH, Oskar Stelzel, vertreten durch die KRONBERGER Rechtsanwälte Gesellschaft mbH, Wien, gegen die beklagte Partei Brian Hüpsch, vertreten durch Dr. Werner Loos, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. März 2018, GZ 38 R 303/17s-48, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 4. August 2017, GZ 22 C 163/16w-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH` — partial — gold is substring of pred: `MurUmwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MurUmwelt GmbH`(organisation)
- `Oskar Stelzel`(person)
- `Brian Hüpsch`(person)

**Example 17** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

**False Positives:**

- `Er selbst war ua als Fenstermonteur in der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

**False Positives:**

- `Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH` — partial — gold is substring of pred: `Ostvallem-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ostvallem-Robotik GmbH`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

**False Positives:**

- `Dabei wiesen die anwesenden Mitarbeiter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_63`)


Eine Plakette mit Namen, Anschrift und Kontaktdaten der GmbH war auch auf dem an den Kläger verkauften Gerät angebracht.

**False Positives:**

- `Anschrift und Kontaktdaten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH` — partial — gold is substring of pred: `Waldzorval Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)

**Example 22** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH` — partial — gold is substring of pred: `Stadt-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Ing. Verona Obersteiner`(person)

**Example 23** (doc_id: `deanon_TRAIN/3Ob12_11b`) (sent_id: `deanon_TRAIN/3Ob12_11b_30`)


5. Die Beurteilung des Berufungsgerichts, der Oppositionskläger habe ausreichend dargetan, dass die von ihm behobenen Beträge in Höhe von insgesamt 114.500 EUR in den Bilanzen der GmbH nicht verbucht wurden, weshalb er auch in diesem Umfang der Titelverpflichtung entsprochen habe, wirft ebenfalls keine im Rahmen einer außerordentlichen Revision aufzugreifende erhebliche Rechtsfrage auf: Es steht durch die gelegte Rechnung in Verbindung mit den Bilanzen der GmbH, in deren Besitz der Oppositionsbeklagte unstrittig ist, fest, dass weder der Gesamtbetrag von 114.500 EUR noch Teilbeträge davon in den Bilanzen der GmbH verbucht wurde.

**False Positives:**

- `Es steht durch die gelegte Rechnung in Verbindung mit den Bilanzen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH` — partial — gold is substring of pred: `Kraftnorost Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 25** (doc_id: `deanon_TRAIN/3Ob150_16d`) (sent_id: `deanon_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH, Hon.-Prof.in Dr.in Silvana Früboes, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Talseemon GmbH, Finn Auctor, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

**False Positives:**

- `Kodek als weitere Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH` — partial — gold is substring of pred: `SGQ Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SGQ Versand GmbH`(organisation)
- `Hon.-Prof.in Dr.in Silvana Früboes`(person)
- `Talseemon GmbH`(organisation)
- `Finn Auctor`(person)

**Example 26** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH` — partial — gold is substring of pred: `Bruckgartver GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 27** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH` — partial — gold is substring of pred: `Nexostlem GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

**Example 28** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH, Hubert Englmaier, vertreten durch Dr. Martin Holzer, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Florian Corvetti, vertreten durch Dr. Heimo Jilek, Rechtsanwalt in Leoben, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Berufungsgericht vom 3. November 2010, GZ 1 R 244/10i-34, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Leoben vom 9. Juni 2010, GZ 5 C 315/09y-28, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision der klagenden Partei wird Folge gegeben, das angefochtene Urteil aufgehoben und die Rechtssache zur neuerlichen Entscheidung an das Berufungsgericht zurückverwiesen.

**False Positives:**

- `Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH` — partial — gold is substring of pred: `Riecken Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Riecken Maschinenbau GmbH`(organisation)
- `Hubert Englmaier`(person)
- `Florian Corvetti`(person)

**Example 29** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH, Esra Bubenischek, vertreten durch Mag. Gerold Schwarzer, Rechtsanwalt in Wien, gegen die beklagte und widerklagende Partei HR Hilde vom Dorf, wegen 286.300,47 EUR sA und 41.219,24 EUR sA, über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Februar 2021, GZ 1 R 168/20m-26, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stefula als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH` — partial — gold is substring of pred: `Gambal Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gambal Software GmbH`(organisation)
- `Esra Bubenischek`(person)
- `HR Hilde vom Dorf`(person)

**Example 30** (doc_id: `deanon_TRAIN/4Ob145_18d`) (sent_id: `deanon_TRAIN/4Ob145_18d_4`)


Matzka und Dr. Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH, Lieselotte Wesp, vertreten durch Hauswirth - Kleiber Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1) DI Amber Rzehatschek, 2) DI Esra Noth, ebendort, beide vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, 3) Trinks Möbel GmbH, Hütten 15, 5221 Lasberg, Österreich, vertreten durch Mag. Thomas Stenitzer und Mag. Kurt Schick, Rechtsanwälte in Laa an der Thaya, und 4) DI (FH) Wladimir Runzheimer, vertreten durch Mag. Bernhard Österreicher, Rechtsanwalt in Pfaffstätten, wegen 127.614,09 EUR sA und Feststellung (Streitwert: 5.200 EUR), über die außerordentliche Revision der erst- und zweitbeklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. April 2018, GZ 1 R 179/17a-29, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH` — partial — gold is substring of pred: `MGL Forschung Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MGL Forschung Consulting GmbH`(organisation)
- `Lieselotte Wesp`(person)
- `DI Amber Rzehatschek`(person)
- `DI Esra Noth`(person)
- `Trinks Möbel GmbH`(organisation)
- `Hütten 15, 5221 Lasberg, Österreich`(address)
- `Wladimir Runzheimer`(person)

**Example 31** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH` — partial — gold is substring of pred: `XDC Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 32** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH` — partial — gold is substring of pred: `Dueckers Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 33** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH` — partial — gold is substring of pred: `Kraftheimglanz-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftheimglanz-Versand GmbH`(organisation)

**Example 34** (doc_id: `deanon_TRAIN/4Ob224_23d`) (sent_id: `deanon_TRAIN/4Ob224_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, den Hofrat Mag. Dr. Wurdinger und die Hofrätin Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH, Andreas Häntsch, Deutschland, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Emma Bergner kammer, Cathleen Hofschulte, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, wegen Unterlassung, Widerruf und Veröffentlichung desselben (Gesamtstreitwert 46.200 EUR), aus Anlass der außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Oktober 2023, GZ 4 R 99/23t-32, mit dem das Urteil des Handelsgerichts Wien vom 27. April 2023, GZ 57 Cg 34/21g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die gemeinsame Anzeige beider Parteien vom 27. August 2024 über das vereinbarte Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH` — partial — gold is substring of pred: `Verlexglanz-Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verlexglanz-Marine GmbH`(organisation)
- `Andreas Häntsch`(person)
- `Emma Bergner`(person)
- `Cathleen Hofschulte`(person)

**Example 35** (doc_id: `deanon_TRAIN/4Ob26_20g`) (sent_id: `deanon_TRAIN/4Ob26_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH, Corbinian Wischnowski, LLM, vertreten durch Rechtsanwaltskanzlei Dr. Wendling GmbH in Kitzbühel, gegen die beklagte Partei Osttallem Getränke GmbH, Zdenko Weimer, BA, Deutschland, vertreten durch Dr. Dan Katzlinger, Rechtsanwalt in Innsbruck, wegen 70.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Dezember 2019, GZ 10 R 49/19k-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH` — partial — gold is substring of pred: `Evelyn Peterhansel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Evelyn Peterhansel`(person)
- `Corbinian Wischnowski, LLM`(person)
- `Osttallem Getränke GmbH`(organisation)
- `Zdenko Weimer, BA`(person)

**Example 36** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Penners Medien GmbH, Wilhelmine Kobinger, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei JRQA Landwirtschaft Rechtsanwälte GmbH, Kometenweg 43, 3200 Rennersdorf, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Steger als weitere Richter in der Rechtssache der klagenden Partei Penners Medien GmbH` — partial — gold is substring of pred: `Penners Medien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Penners Medien GmbH`(organisation)
- `Wilhelmine Kobinger`(person)
- `JRQA Landwirtschaft`(organisation)
- `Kometenweg 43, 3200 Rennersdorf, Österreich`(address)

**Example 37** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_31`)


Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH gegenüber Dritten könne außerdem mit einem Interessenkonflikt zwischen der Gesellschaft und dem Mehrheitsgesellschafter keinesfalls begründet werden.

**False Positives:**

- `Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_80`)


Wird eine GmbH durch einen Dritten geschädigt, ist der dem Gesellschafter dadurch entstehende Nachteil in seinem Vermögen ein nicht ersatzfähiger mittelbarer Schaden.

**False Positives:**

- `Wird eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/5Ob221_22v`) (sent_id: `deanon_TRAIN/5Ob221_22v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH in Liquidation, Steugasse 3, 6123 Vomperbach, Österreich, vertreten durch Mag. Gottfried Tazol, Rechtsanwalt in Völkermarkt, gegen die beklagte Partei SeeSanitär AG, Helge Schreyvogel, BEd, vertreten durch Mag. Alexander Todor-Kostic LL.M., Mag. Silke Todor-Kostic, Rechtsanwälte in Velden am Wörthersee, wegen 84.999,13 EUR sA, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 62.200,50 EUR sA) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. Oktober 2022, GZ 5 R 74/22z-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Steger als weitere Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH` — partial — gold is substring of pred: `Fabian + Michailoff Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fabian + Michailoff Analyse GmbH`(organisation)
- `Steugasse 3, 6123 Vomperbach, Österreich`(address)
- `SeeSanitär AG`(organisation)
- `Helge Schreyvogel, BEd`(person)

**Example 40** (doc_id: `deanon_TRAIN/5Ob93_24y`) (sent_id: `deanon_TRAIN/5Ob93_24y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH, Florenzia Lohmöller, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dipl.-Ing. Juliana Maurice, wegen Unterfertigung eines Wohnungseigentumsvertrags und Feststellung, hier: Anmerkung der Klage, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 26. April 2024, GZ 15 R 41/24w-18, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 126 Abs 1 GBG iVm § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH` — partial — gold is substring of pred: `Jozwiak Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jozwiak Robotik GmbH`(organisation)
- `Florenzia Lohmöller`(person)
- `Dipl.-Ing. Juliana Maurice`(person)

**Example 41** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Gitschthaler als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätinnen Dr. Kodek und Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei MurFinanzen GmbH, OStR Thorsten Bobb, vertreten durch Dr. Ralph Mayer, Rechtsanwalt in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei MurFinanzen GmbH` — partial — gold is substring of pred: `MurFinanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MurFinanzen GmbH`(organisation)
- `OStR Thorsten Bobb`(person)

**Example 42** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH, Ilona Hoernle, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Wickl Logistik GmbH, Vitus Glassbrenner, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH` — partial — gold is substring of pred: `Unlandherm KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unlandherm KI GmbH`(organisation)
- `Ilona Hoernle`(person)
- `Wickl Logistik GmbH`(organisation)
- `Vitus Glassbrenner`(person)

**Example 43** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_10`)


Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH verbüchert.

**False Positives:**

- `Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der Schenker Elektro GmbH, FN FN119011j, wegen § 10 Abs 2 FBG, über den Revisionsrekurs des Österreichischen Verbandes Gemeinnütziger Bauvereinigungen Revisionsverband, 1010 Wien, Bösendorferstraße 7, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 3. September 2020, GZ 6 R 158/20d-6, womit der Rekurs gegen den Beschluss des Handelsgerichts Wien vom 20. Juli 2020, GZ 72 Fr 3266/20f-3, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Faber als weitere Richter in der Firmenbuchsache der Schenker Elektro GmbH` — partial — gold is substring of pred: `Schenker Elektro GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schenker Elektro GmbH`(organisation)
- `FN119011j`(business_register_number)

**Example 45** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

**False Positives:**

- `Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH` — partial — gold is substring of pred: `FN110230q`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN110230q`(business_register_number)
- `Seetra-Recycling GmbH`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_155`)


Abs 1 lit a WGG kann durch Zwischenschaltung einer GmbH umgangen werden.

**False Positives:**

- `Abs 1 lit a WGG kann durch Zwischenschaltung einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH` — partial — gold is substring of pred: `FN912691n`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN912691n`(business_register_number)
- `Landesgericht Klagenfurt`(organisation)
- `Holtschmidt Versicherung GmbH`(organisation)
- `LG Wels`(organisation)
- `Lohneis Pflege gesellschaft mbH`(organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich`(address)

**Example 49** (doc_id: `deanon_TRAIN/6Ob69_23z`) (sent_id: `deanon_TRAIN/6Ob69_23z_34`)


Die (vom Beklagten vorgelegte) Vereinbarung mit der GmbH entspreche nicht der von der Klägerin behaupteten, weil die Regelung des Entgelts (eines Zuschlags von 20 %) darin fehle.

**False Positives:**

- `Vereinbarung mit der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_TRAIN/7Ob141_16k`) (sent_id: `deanon_TRAIN/7Ob141_16k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Seedorf Vertrieb GmbH, Felix Bernloehr, vertreten durch Dr. Helmut Fetz und andere, Rechtsanwälte in Leoben, gegen die beklagte Partei Mlynarik Handel Aktiengesellschaft, Veropastraße 16, 2413 Edelstal, Österreich, vertreten durch Dr. Heimo Jilek und Dr. Martin Sommer, Rechtsanwälte in Leoben, wegen 61.848,15 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 25. Mai 2016, GZ 5 R 9/16g-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Singer als weitere Richter in der Rechtssache der klagenden Partei Seedorf Vertrieb GmbH` — partial — gold is substring of pred: `Seedorf Vertrieb GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Seedorf Vertrieb GmbH`(organisation)
- `Felix Bernloehr`(person)
- `Mlynarik Handel Aktiengesellschaft`(organisation)
- `Veropastraße 16, 2413 Edelstal, Österreich`(address)

**Example 51** (doc_id: `deanon_TRAIN/7Ob31_19p`) (sent_id: `deanon_TRAIN/7Ob31_19p_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Alpen Traostal GmbH, Florens Mühle, vertreten durch Mag. Stefan Korab, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. RheinImmobilien Gesellschaft mbH, Melcherweg 193, 8242 Kronegg, Österreich, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, wegen 151.623,74 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 20. Dezember 2018, GZ 129 R 98/18g-76, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Alpen Traostal GmbH` — partial — gold is substring of pred: `Alpen Traostal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen Traostal GmbH`(organisation)
- `Florens Mühle`(person)
- `RheinImmobilien Gesellschaft mbH`(organisation)
- `Melcherweg 193, 8242 Kronegg, Österreich`(address)

**Example 52** (doc_id: `deanon_TRAIN/7Ob35_16x`) (sent_id: `deanon_TRAIN/7Ob35_16x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei NGU Energie Dienstleistungen GmbH, Noah Rübke, vertreten durch Köhler Draskovits Unger Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Franziskus Rußkamp, vertreten durch Dr. Hans Wagner, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 9. Dezember 2015, GZ 39 R 367/15g-26, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Singer als weitere Richter in der Rechtssache der klagenden Partei NGU Energie Dienstleistungen GmbH` — partial — gold is substring of pred: `NGU Energie Dienstleistungen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NGU Energie Dienstleistungen GmbH`(organisation)
- `Noah Rübke`(person)
- `Franziskus Rußkamp`(person)

**Example 53** (doc_id: `deanon_TRAIN/7Ob4_12g`) (sent_id: `deanon_TRAIN/7Ob4_12g_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei TVOW Verlag GmbH, Werner Megerlein, vertreten durch Dr. Roland Kometer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Bruckzor Umwelt Services GmbH, Valerian Landwehrkamp, vertreten durch Rainer Kurbos, Rechtsanwalt in Graz, wegen 8.635,55 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 25. Oktober 2011, GZ 1 R 84/11a-18, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Wurdinger als weitere Richter in der Rechtssache der klagenden Partei TVOW Verlag GmbH` — partial — gold is substring of pred: `TVOW Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TVOW Verlag GmbH`(organisation)
- `Werner Megerlein`(person)
- `Bruckzor Umwelt Services GmbH`(organisation)
- `Valerian Landwehrkamp`(person)

**Example 54** (doc_id: `deanon_TRAIN/7Ob63_18t`) (sent_id: `deanon_TRAIN/7Ob63_18t_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Automotive Bergartglanz GmbH, Denis Leithe, vertreten durch Dr. Erwin Markl, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Bruckfen Manufaktur GmbH, Jeannine Orthel, vertreten durch Graf & Pitkowitz, Rechtsanwälte GmbH in Wien, wegen 31.500 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2018, GZ 2 R 130/17b-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Automotive Bergartglanz GmbH` — partial — gold is substring of pred: `Automotive Bergartglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Automotive Bergartglanz GmbH`(organisation)
- `Denis Leithe`(person)
- `Bruckfen Manufaktur GmbH`(organisation)
- `Jeannine Orthel`(person)

**Example 55** (doc_id: `deanon_TRAIN/8Ob97_23g`) (sent_id: `deanon_TRAIN/8Ob97_23g_4`)


Matzka, Dr. Stefula und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Bartholomaeus Digital GmbH, Dorothea Siemers, vertreten durch Dr. Hanno Hofmann, Rechtsanwalt in Graz, gegen die beklagte Partei Winceck Solar GmbH, Rupert Frangenberg, vertreten durch Mag. Dr. Günther Schmied, Rechtsanwalt in Graz, wegen Übergabeauftrags, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 21. Juni 2023, GZ 5 R 26/23i-49, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Graz-West vom 29. Dezember 2022, GZ 111 C 5/22w-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Thunhart als weitere Richter in der Rechtssache der klagenden Partei Bartholomaeus Digital GmbH` — partial — gold is substring of pred: `Bartholomaeus Digital GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bartholomaeus Digital GmbH`(organisation)
- `Dorothea Siemers`(person)
- `Winceck Solar GmbH`(organisation)
- `Rupert Frangenberg`(person)

**Example 56** (doc_id: `deanon_TRAIN/8ObA21_11p`) (sent_id: `deanon_TRAIN/8ObA21_11p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Dr. Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke GmbH & Co OG, Heinickegasse 3x, 4984 Klingersberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Waltraud Seckl, vertreten durch Dr. Friedrich Schubert, Rechtsanwalt in Wien, wegen 19.335,55 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 31. Jänner 2011, GZ 7 Ra 121/10f-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke GmbH` — partial — gold is substring of pred: `Wilost Garten Werke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilost Garten Werke GmbH`(organisation)
- `Heinickegasse 3x, 4984 Klingersberg, Österreich`(address)
- `Ing. Waltraud Seckl`(person)

**Example 57** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Dehn und den Hofrat des Obersten Gerichtshofs Dr. Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei WestSicherheit GmbH, OMedR Paulina von Tietzen, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Amber Landscheid, vertreten durch Dr. Karl-Heinz Plankel, Dr. Herwig Mayrhofer ua, Rechtsanwälte in Dornbirn, wegen 15.600 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, anstelle des Landesgerichts Salzburg als Arbeits- und Sozialgericht das Arbeits- und Sozialgericht Wien zur Verhandlung und Entscheidung der Rechtssache des Landesgerichts Salzburg als Arbeits- und Sozialgericht AZ 15 Cga 88/15d zu bestimmen, wird abgewiesen.

**False Positives:**

- `Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei WestSicherheit GmbH` — partial — gold is substring of pred: `WestSicherheit GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WestSicherheit GmbH`(organisation)
- `OMedR Paulina von Tietzen`(person)
- `Amber Landscheid`(person)

**Example 58** (doc_id: `deanon_TRAIN/9Ob72_18f`) (sent_id: `deanon_TRAIN/9Ob72_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Beilmaier&Herpolsheimer Daten GmbH, Dipl.-Ing. Ramon Neess, vertreten durch Knirsch Gschaider & Cerha Rechtsanwälte OG in Wien, sowie des Nebenintervenienten auf Seiten der klagenden Partei Dr. Hilde Gemperl, gegen die beklagte Partei Kirci & Issakov Sicherheit GesmbH, Stowassergasse 117, 2840 Hütten, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, wegen 159.824,87 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2018, GZ 129 R 55/18h-40, mit dem der Berufung der klagenden Partei gegen das Urteil des Handelsgerichts Wien vom 6. April 2018, GZ 21 Cg 23/15s-36, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

**False Positives:**

- `Stefula in der Rechtssache der klagenden Partei Beilmaier&Herpolsheimer Daten GmbH` — partial — gold is substring of pred: `Beilmaier&Herpolsheimer Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Beilmaier&Herpolsheimer Daten GmbH`(organisation)
- `Dipl.-Ing. Ramon Neess`(person)
- `Dr. Hilde Gemperl`(person)
- `Kirci & Issakov Sicherheit GesmbH`(organisation)
- `Stowassergasse 117, 2840 Hütten, Österreich`(address)

**Example 59** (doc_id: `deanon_TRAIN/9Ob80_15b`) (sent_id: `deanon_TRAIN/9Ob80_15b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Tarmann-Prentner und Dr. Dehn, den Hofrat des Obersten Gerichtshofs Dr. Hargassner und die Hofrätin des Obersten Gerichtshofs Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei Rosenstil Luftfahrt GmbH, Anton Lehrheuer, vertreten durch Dr. Franz Hitzenberger ua, Rechtsanwälte in Vöcklabruck, gegen die beklagte Partei Wehrstedt Marine GmbH, Zoltan Menssing, vertreten durch Dr. Robert Galler und Dr. Rudolf Höpflinger, Rechtsanwälte in Salzburg, wegen 15.000 EUR sA, über die Revision der klagenden Partei (Revisionsinteresse: 7.620,94 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 28. September 2015, GZ 4 R 130/15p-56, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 5. Juni 2015, GZ 5 Cg 134/12w-47, teilweise Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei Rosenstil Luftfahrt GmbH` — partial — gold is substring of pred: `Rosenstil Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rosenstil Luftfahrt GmbH`(organisation)
- `Anton Lehrheuer`(person)
- `Wehrstedt Marine GmbH`(organisation)
- `Zoltan Menssing`(person)

</details>

---

## `Specific Compound AG 1`

**F1:** 0.033 | **Precision:** 0.261 | **Recall:** 0.017  

**Format:** `regex`  
**Rule ID:** `98fff7bd`  
**Description:**
Matches specific compound AG entities like 'Fenbach-IT AG', 'SüdCloud AG', 'Ost-Metall AG', 'Frise und Stasiak Wind AG', 'Uniglanz Bildung Solutions AG', 'QBAW Forschung AG' and similar patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+AG)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.261 | 0.017 | 0.033 | 23 | 6 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 17 | 337 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Analyse Kelunizor AG` | `Analyse Kelunizor AG` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `LGR Medien GmbH` (organisation)
- `OVX Finanzen` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `TraunBau AG` | `TraunBau AG` |

**Missed by this rule (FN):**

- `Ing. KzlR MedR Brunhild Syndikus` (person)
- `Böhnstedt+Bittlmeier Verlag GmbH` (organisation)
- `Wien Traalmon Betriebe` (organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich` (address)

**Example 5** (doc_id: `deanon_TRAIN/8Ob35_23i`) (sent_id: `deanon_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Pflege Deruni, und 2. Marchesi+Kusnezow Transport AG, Grabenseeweg 48, 8272 Ebersdorf, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Valerie Wilczenski, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Marchesi+Kusnezow Transport AG` | `Marchesi+Kusnezow Transport AG` |

**Missed by this rule (FN):**

- `Pflege Deruni` (organisation)
- `Grabenseeweg 48, 8272 Ebersdorf, Österreich` (address)
- `DI Valerie Wilczenski` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei OMedR Eleonore Wunderling, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG, Amanda Deutschlender, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Claeser Forschung AG` — partial — pred is substring of gold: `Fildhaut & Claeser Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Eleonore Wunderling`(person)
- `Fildhaut & Claeser Forschung AG`(organisation)
- `Amanda Deutschlender`(person)

**Example 5** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG` — partial — gold is substring of pred: `Donostzor-Software AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 6** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG` — partial — gold is substring of pred: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 7** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG` — partial — gold is substring of pred: `Lebensmittel Glanzconuni AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lebensmittel Glanzconuni AG`(organisation)
- `Immanuel Gspan`(person)
- `Fridolin Braunhold`(person)
- `Mag. Frauke Steinweg`(person)
- `DonauLexlogbruckPlanung GmbH`(organisation)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich`(address)

**Example 8** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG an.

**False Positives:**

- `Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG` — partial — gold is substring of pred: `Conkraftnor-Event AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Conkraftnor-Event AG`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG` — partial — gold is substring of pred: `Mozar und Kuebler Daten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

**Example 10** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/7Ob162_20d`) (sent_id: `deanon_TRAIN/7Ob162_20d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei DDr.in Gisela Loy, vertreten durch Mag. Marco und Mag. Amelie Kunczicky, Rechtsanwälte in Mayrhofen, gegen die beklagte Partei Helferich & Zeitler Marine AG, Jessica Seebald, vertreten durch Mag. Thomas Anker und DI Mag. Nikolaus Gratl, Rechtsanwäte in Innsbruck, wegen Urkundeneinsicht, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Juni 2020, GZ 4 R 55/20z-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Zeitler Marine AG` — partial — pred is substring of gold: `Helferich & Zeitler Marine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr.in Gisela Loy`(person)
- `Helferich & Zeitler Marine AG`(organisation)
- `Jessica Seebald`(person)

**Example 12** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_4`)


Cynthia Martchenko AG, Schmidhuberstraße 73, 4792 Landertsberg, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2. Reisch + Weißert Getränke AG und 3.

**False Positives:**

- `Cynthia Martchenko AG` — partial — gold is substring of pred: `Cynthia Martchenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cynthia Martchenko`(person)
- `Schmidhuberstraße 73, 4792 Landertsberg, Österreich`(address)
- `Reisch + Weißert Getränke AG`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/7Ob92_19h`) (sent_id: `deanon_TRAIN/7Ob92_19h_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Tosca Janetscheck, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Domingo + Sinner Robotik AG Liliana Böbe, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Sinner Robotik AG` — partial — pred is substring of gold: `Domingo + Sinner Robotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tosca Janetscheck`(person)
- `Domingo + Sinner Robotik AG`(organisation)
- `Liliana Böbe`(person)

**Example 14** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei, Guggeis Automotive Bank InnBildung Betriebe AG, Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich, vertreten durch Dr. Mag. Günther Riess, Mag. Christine Schneider, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Doris Froemmel, vertreten durch Czernich Hofstädter Guggenberger & Partner, Rechtsanwälte in Innsbruck, wegen 2.278.895,88 EUR sA, über die Rekurse beider Parteien gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Oktober 2010, GZ 4 R 168/10b-76, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Feldkirch vom 20. Mai 2010, GZ 6 Cg 71/08s-71, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch 1.

**False Positives:**

- `Guggeis Automotive Bank InnBildung Betriebe AG` — partial — gold is substring of pred: `Guggeis Automotive`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Guggeis Automotive`(organisation)
- `InnBildung Betriebe AG`(organisation)
- `Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich`(address)
- `Doris Froemmel`(person)

**Example 15** (doc_id: `deanon_TRAIN/8Ob121_22k`) (sent_id: `deanon_TRAIN/8Ob121_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG, Theophil Bings, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ÖkR Christoph Adamske Privatstiftung,*, vertreten durch Dr. Felix Michael Klement, Rechtsanwalt in Wien, wegen 1.500.000 USD sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien vom 28. April 2022, GZ 2 R 133/21z-42, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG` — partial — gold is substring of pred: `Roettgermann + Soldmann Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roettgermann + Soldmann Heizung AG`(organisation)
- `Theophil Bings`(person)
- `ÖkR Christoph Adamske`(person)

**Example 16** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_13`)


Die West Heimwaldstein Solutions AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die West Heimwaldstein Solutions AG` — partial — gold is substring of pred: `West Heimwaldstein Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Heimwaldstein Solutions AG`(organisation)

</details>

---

## `General AG Company`

**F1:** 0.022 | **Precision:** 0.267 | **Recall:** 0.012  

**Format:** `regex`  
**Rule ID:** `8f71bc96`  
**Description:**
Matches companies ending in AG, ensuring strict boundaries to avoid capturing preceding context like 'von der' or legal party lists.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?(?!(?:Partei|Die|Der|des|der|von|der|in|mit|auf|an|bei|nach|vor|zu|für|um|ohne|durch|gegen|über|unter|neben|zwischen|entlang|statt|außer|bis|seit|während|wegen|trotz|dank|laut|gemäß|entsprechend|Richter|Senatspräsident|Hofrat|Hofrätin|Mag\.|Dr\.)(?:\s+|\n))(?![A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+AG)([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+AG)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.267 | 0.012 | 0.022 | 15 | 4 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 11 | 339 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `TraunBau AG` | `TraunBau AG` |

**Missed by this rule (FN):**

- `Ing. KzlR MedR Brunhild Syndikus` (person)
- `Böhnstedt+Bittlmeier Verlag GmbH` (organisation)
- `Wien Traalmon Betriebe` (organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/8Ob35_23i`) (sent_id: `deanon_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Pflege Deruni, und 2. Marchesi+Kusnezow Transport AG, Grabenseeweg 48, 8272 Ebersdorf, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Valerie Wilczenski, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Marchesi+Kusnezow Transport AG` | `Marchesi+Kusnezow Transport AG` |

**Missed by this rule (FN):**

- `Pflege Deruni` (organisation)
- `Grabenseeweg 48, 8272 Ebersdorf, Österreich` (address)
- `DI Valerie Wilczenski` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 3** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG` — partial — gold is substring of pred: `Donostzor-Software AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 4** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG` — partial — gold is substring of pred: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 5** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG` — partial — gold is substring of pred: `Lebensmittel Glanzconuni AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lebensmittel Glanzconuni AG`(organisation)
- `Immanuel Gspan`(person)
- `Fridolin Braunhold`(person)
- `Mag. Frauke Steinweg`(person)
- `DonauLexlogbruckPlanung GmbH`(organisation)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich`(address)

**Example 6** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG an.

**False Positives:**

- `Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG` — partial — gold is substring of pred: `Conkraftnor-Event AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Conkraftnor-Event AG`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG` — partial — gold is substring of pred: `Mozar und Kuebler Daten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

**Example 8** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei, Guggeis Automotive Bank InnBildung Betriebe AG, Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich, vertreten durch Dr. Mag. Günther Riess, Mag. Christine Schneider, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Doris Froemmel, vertreten durch Czernich Hofstädter Guggenberger & Partner, Rechtsanwälte in Innsbruck, wegen 2.278.895,88 EUR sA, über die Rekurse beider Parteien gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Oktober 2010, GZ 4 R 168/10b-76, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Feldkirch vom 20. Mai 2010, GZ 6 Cg 71/08s-71, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch 1.

**False Positives:**

- `Guggeis Automotive Bank InnBildung Betriebe AG` — partial — gold is substring of pred: `Guggeis Automotive`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Guggeis Automotive`(organisation)
- `InnBildung Betriebe AG`(organisation)
- `Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich`(address)
- `Doris Froemmel`(person)

**Example 10** (doc_id: `deanon_TRAIN/8Ob121_22k`) (sent_id: `deanon_TRAIN/8Ob121_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG, Theophil Bings, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ÖkR Christoph Adamske Privatstiftung,*, vertreten durch Dr. Felix Michael Klement, Rechtsanwalt in Wien, wegen 1.500.000 USD sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien vom 28. April 2022, GZ 2 R 133/21z-42, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG` — partial — gold is substring of pred: `Roettgermann + Soldmann Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roettgermann + Soldmann Heizung AG`(organisation)
- `Theophil Bings`(person)
- `ÖkR Christoph Adamske`(person)

</details>

---

## `Specific Compound GmbH 1`

**F1:** 0.012 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `60837e20`  
**Description:**
Matches specific compound GmbH entities like 'Schlezak+Bareuter Pharma GmbH', 'EnnsSanitär GmbH', 'Kärgel + Rafalzik Maschinenbau GmbH', 'Inn-Finanzen Gesellschaft mbH' and similar patterns with lowercase 'gmbh'.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Gesellschaft\s+mbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.012 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 277 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/17Ob19_23b`) (sent_id: `deanon_TRAIN/17Ob19_23b_7`)


Die Kläger brachten gegen den Beklagten als ehemaligen Insolvenzverwalter der A. Rater Finanzen Gesellschaft mbH eine von ihnen selbst verfasste Schadenersatzklage verbunden mit einem Antrag auf Bewilligung der Verfahrenshilfe ein.

| Predicted | Gold |
|---|---|
| `Rater Finanzen Gesellschaft mbH` | `Rater Finanzen Gesellschaft mbH` |

**Example 1** (doc_id: `deanon_TRAIN/7Ob31_19p`) (sent_id: `deanon_TRAIN/7Ob31_19p_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Alpen Traostal GmbH, Florens Mühle, vertreten durch Mag. Stefan Korab, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. RheinImmobilien Gesellschaft mbH, Melcherweg 193, 8242 Kronegg, Österreich, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, wegen 151.623,74 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 20. Dezember 2018, GZ 129 R 98/18g-76, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `RheinImmobilien Gesellschaft mbH` | `RheinImmobilien Gesellschaft mbH` |

**Missed by this rule (FN):**

- `Alpen Traostal GmbH` (organisation)
- `Florens Mühle` (person)
- `Melcherweg 193, 8242 Kronegg, Österreich` (address)

</details>

---

## `Lowercase GmbH Company`

**F1:** 0.011 | **Precision:** 0.667 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `e092b6a3`  
**Description:**
Matches companies ending in 'gmbh' (all lowercase) found in training data.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+gmbh)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.006 | 0.011 | 3 | 2 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 1 | 110 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_17`)


Diese Partner sind: Seedon-Touristik GmbH, Digital Donnor gmbh, YLHZ Umwelt GmbH oder die Verwendung sinngleicher Klauseln zuunterlassen;

| Predicted | Gold |
|---|---|
| `Digital Donnor gmbh` | `Digital Donnor gmbh` |

**Missed by this rule (FN):**

- `Seedon-Touristik GmbH` (organisation)
- `YLHZ Umwelt GmbH` (organisation)

**Example 1** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_360`)


Diese Partner sind: Snajder und Frohne Marine GmbH, Uniunibach-Pharma gmbh, Betti Sanitär GmbH.

| Predicted | Gold |
|---|---|
| `Uniunibach-Pharma gmbh` | `Uniunibach-Pharma gmbh` |

**Missed by this rule (FN):**

- `Snajder und Frohne Marine GmbH` (organisation)
- `Betti Sanitär GmbH.` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9Ob10_21t`) (sent_id: `deanon_TRAIN/9Ob10_21t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte Dr. Fichtenau, Hon.-Prof. Dr. Dehn, Dr. Hargassner, und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Schnake Robotik gmbh, Jeanne Großkopf, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Volkmar Kapelner GmbH, Reinberg-Litschau 11, 9343 Aich, Österreich, vertreten durch Advokatur Dr. Herbert Schöpf, LL.M., Rechtsanwalt-GmbH in Innsbruck, sowie die Nebenintervenientin auf Seiten der beklagten Partei EKFS Landwirtschaft AG & Co KG, Burgstallerstraße 10, 4892 Röth, Österreich, vertreten durch Hämmerle & Hübner Rechtsanwälte OG in Innsbruck, wegen 115.062,53 EUR sA, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 104.999,62 EUR sA) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Jänner 2021, GZ 3 R 76/20f-144, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Korn als weitere Richter in der Rechtssache der klagenden Partei Schnake Robotik gmbh` — partial — gold is substring of pred: `Schnake Robotik gmbh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schnake Robotik gmbh`(organisation)
- `Jeanne Großkopf`(person)
- `Volkmar Kapelner`(person)
- `Reinberg-Litschau 11, 9343 Aich, Österreich`(address)
- `EKFS Landwirtschaft AG`(organisation)
- `Burgstallerstraße 10, 4892 Röth, Österreich`(address)

</details>

---

## `Bezirksgericht`

**F1:** 0.008 | **Precision:** 0.016 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `f3e2904e`  
**Description:**
Matches district courts like 'Bezirksgericht Mattersburg', handling repeated instances correctly.

**Content:**
```
\bBezirksgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.006 | 0.008 | 126 | 2 | 124 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 124 | 343 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_7`)


Nach dem Klagsvorbringen sei er am 19. 8. 2009 im Strandbad Bezirksgericht Silz beim Verlassen des Wassers von einem ca zwei Fäuste großen Stein ins Gesicht getroffen worden, der vom damals sechsjährigen Beklagten geworfen worden sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 1** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_18`)


Verwiesen werde auf einen Akt der Staatsanwaltschaft Bezirksgericht Wels, in welchem gegen den Schädiger Vorerhebungen geführt, jedoch mangels Deliktsfähigkeit eingestellt worden seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wels` | `Bezirksgericht Wels` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Bezirksgericht Judenburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_4`)


Kfm. Raul Bialleck Plc, pA Ernestine Enger, Deutschland, wegen 1.624 EUR sA über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernestine Enger`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_7`)


[2] Das von der Klägerin angerufene Bezirksgericht Schwechat wies die Klage mit rechtskräftigem Beschluss vom 19. Jänner 2022 mangels internationaler Zuständigkeit zurück.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_36`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel;

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Delia Truepschuch, geboren am 1. Februar 2026, und Aloisa Eckmaier, geboren am 28. Februar 1976, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation
- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Delia Truepschuch`(person)
- `1. Februar 2026`(date)
- `Aloisa Eckmaier`(person)
- `28. Februar 1976`(date)

**Example 10** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

**False Positives:**

- `Bezirksgericht Feldkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

**False Positives:**

- `Bezirksgericht Neunkirchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `ÖkR Priv.-Doz. Sven Egerth`(person)
- `3. Mai`(date)

**Example 15** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_5`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation
- `Bezirksgericht Braunau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 16** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_6`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_9`)


Die klagende Partei beantragt die Delegierung des Verfahrens vom Bezirksgericht Graz-West an das Bezirksgericht Fünfhaus.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_11`)


Das Bezirksgericht Graz-West spricht sich für die Delegierung aus.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Zarin Steevens, geboren 26. Mai 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Dorothea Akkaya, und des Antragsgegners Mirko Hamidi, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation
- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Zarin Steevens`(person)
- `26. Mai`(date)
- `Dorothea Akkaya`(person)
- `Mirko Hamidi`(person)

**Example 20** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_8`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Raumberg 325, 2301 Schönau an der Donau, Österreich aufhalte (ON 7).

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Raumberg 325, 2301 Schönau an der Donau, Österreich`(address)

**Example 21** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_10`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_14`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_16`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_18`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_21`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation
- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation
- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 26** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_22`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_23`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/10Ob2_10g`) (sent_id: `deanon_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Dagobert Borghart anhängig.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dagobert Borghart`(person)

**Example 29** (doc_id: `deanon_TRAIN/10Ob4_17m`) (sent_id: `deanon_TRAIN/10Ob4_17m_8`)


Am 20. 9. 2016 beantragte die Antragstellerin beim Bezirksgericht Josefstadt die Erhöhung der monatlichen Unterhaltszahlung auf 440 EUR ab 1. 9. 2016.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_6`)


Aus Anlass einer vom Bezirksgericht Linz am 17. Dezember 2015 ausgesprochenen Verurteilung, AZ 17 U 185/14t, wurde die Probezeit der bedingten Entlassung auf fünf Jahre verlängert (vgl ON 58 S 7 der Hv-Akten).

**False Positives:**

- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_9`)


Hinsichtlich des Vollzugs der verhängten Freiheitsstrafe und des widerrufenen Strafrests bewilligte das Bezirksgericht Steyr (als erkennendes Gericht im Sinn des § 7 StVG [vglJerabek, WK-StPO § 494a Rz 15]) mit Beschluss vom 27. April 2016 dem Verurteilten einen Strafaufschub gemäß § 6 Abs 1 Z 2 lit a StVG bis zum 1. Mai 2017 (ON 11 der U-Akten).

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_10`)


Mit am 10. Februar 2017 beim Bezirksgericht Steyr eingelangtem Schreiben ersuchte der Verurteilte den „Haftaufschub 5 U 42/16w-17 der im Mai 2017 ausläuft, in eine bedingte Haftstrafe umzuändern“, wobei er zusammengefasst vorbrachte, dass er seit August 2016 als Küchenhilfe tätig sei, seinen Zahlungsverpflichtungen nachkomme und nun die Möglichkeit einer stationären Drogenentzugsbehandlung wahrnehmen möchte (ON 18 der U-Akten).

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_12`)


Mit Note vom 17. Februar 2017 teilte das Landesgericht St. Pölten dem Bezirksgericht Steyr mit, „dass derAntrag offensichtlich auf nachträgliche Milderung der mit Urteil des BG Steyr vom 11.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_15`)


Das Bezirksgericht Steyr übermittelte daraufhin die Akten dem Obersten Gerichtshof zur Entscheidung über einen Zuständigkeitskonflikt (ON 23 der U-Akten): Nach Ansicht des vorlegenden Gerichts sei das Bezirksgericht Steyr zwar zur Entscheidung über den Antrag auf nachträgliche Strafmilderung hinsichtlich der mit Urteil des Bezirksgerichts Steyr vom 11. April 2016 verhängten unbedingten Freiheitsstrafe zuständig;

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation
- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 36** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_18`)


Daraufhin übermittelte das Bezirksgericht Steyr die Akten dem Landesgericht St. Pölten mit dem Ersuchen um Äußerung zur Zuständigkeitsfrage im Sinn der Ausführungen des Obersten Gerichtshofs.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_21`)


2012 verhängte Strafmaß von sechzehn Monaten Freiheitsstrafe herabsetzen möge, sondern darauf, dass das Bezirksgericht Steyr seine urteilsmäßige Entscheidung vom 11.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_27`)


Daher kommt – entgegen der Ansicht des Landesgerichts St. Pölten – im Rahmen des § 31a StGB eine nachträgliche Änderung des vom Bezirksgericht Steyr (gemeinsam mit dem Urteil) gefassten Beschlusses auf Widerruf der zu AZ 38 BE 50/13x des Landesgerichts Steyr gewährten bedingten Entlassung nicht in Betracht.

**False Positives:**

- `Bezirksgericht Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/12Os132_12x`) (sent_id: `deanon_TRAIN/12Os132_12x_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in seinem Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Bezirksgericht Innsbruck verwiesen.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/12Os132_12x`) (sent_id: `deanon_TRAIN/12Os132_12x_7`)


Nach einer gescheiterten staatsanwaltschaftlichen Diversion wurde das in der Folge vom Bezirksgericht Innsbruck zu AZ 8 U 408/09v geführte Verfahren mit Beschluss vom 19. Mai 2010 (ON 28) gemäß §§ 35 Abs 1 iVm 37 SMG unter Bestimmung einer Probezeit von zwei Jahren vorläufig eingestellt.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/12Os132_12x`) (sent_id: `deanon_TRAIN/12Os132_12x_8`)


Mangels Einlangens von Bestätigungen über den Beginn und den anschließenden Verlauf aufgetragener klinisch-psychologischer Beratung und Betreuung sowie einer ärztlichen Entzugs- und Substitutionsbehandlung und weil der Angeklagte sich der Kontrolluntersuchung nach dem SMG entzog (ON 35), was solcherart auch einer weiteren diversionellen Erledigung entgegensteht, setzte das Bezirksgericht Innsbruck das Strafverfahren mit Beschluss vom 29. Oktober 2010 gemäß § 38 Abs 1 Z 2 SMG fort (ON 37).

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Pentzold des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Bezirksgericht Leopoldstadt Nenad Pentzold` — partial — gold is substring of pred: `Pentzold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pentzold`(person)

**Example 45** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__7`)


Das angefochtene Urteil, das im Übrigen unberührt bleibt, wird im Ausspruch über die Verbandsgeldbuße aufgehoben und die Sache in diesem Umfang wird zu neuer Verhandlung und Entscheidung an das Bezirksgericht Spittal an der Drau verwiesen.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__11`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_3`)


Kopf Der Oberste Gerichtshof hat am 23. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Melounek als Schriftführerin in der Strafsache gegen Fabiano Pflichtbeil wegen Vergehen der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB in dem zu AZ 3 U 21/17x des Bezirksgerichts Lienz und zu AZ 5 U 52/17h des Bezirksgerichts Wiener Neustadt geführten Kompetenzkonflikt nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Wiener Neustadt zu führen.

**False Positives:**

- `Bezirksgericht Wiener Neustadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pflichtbeil`(person)

**Example 48** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_4`)


Gründe:  Rechtliche Beurteilung Mit am 24. Februar 2015 beim Bezirksgericht Lienz eingebrachtem Strafantrag (ON 13) legte die Staatsanwaltschaft Innsbruck Fabiano Pierskala zur Last, er habe seine im Familienrecht begründete Unterhaltspflicht gegenüber Leonardo Mehltreter in den Zeiträumen 1. bis 31. März 2015, 1. bis 30. Juni 2015 und 1. August 2015 bis 3. November 2016 gröblich verletzt, und erachtete durch dieses Verhalten „das“ (richtig: mehrere) Vergehen der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB verwirklicht.

**False Positives:**

- `Bezirksgericht Lienz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_5`)


Das Bezirksgericht Lienz überwies die Sache wegen örtlicher Unzuständigkeit dem Bezirksgericht Wiener Neustadt (§ 38 erster Satz StPO).

**False Positives:**

- `Bezirksgericht Lienz` — no gold match — likely missing annotation
- `Bezirksgericht Wiener Neustadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 50** (doc_id: `deanon_TRAIN/15Ns82_10t`) (sent_id: `deanon_TRAIN/15Ns82_10t_3`)


Kopf Der Oberste Gerichtshof hat am 19. Jänner 2011 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Jahn als Schriftführerin in den Strafsachen gegen Christoph Cihlarz wegen des Vergehens der Körperverletzung nach § 83 Abs 1 StGB, AZ 9 U 55/10p des Bezirksgerichts Hartberg, und AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya über den Kompetenzkonflikt betreffend die Durchführung des zu AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya anhängigen Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Für die Durchführung des Strafverfahrens gegen Christoph Cöllner wegen § 83 Abs 1 StGB, AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya, ist das Bezirksgericht Hartberg zuständig.

**False Positives:**

- `Bezirksgericht Hartberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Cihlarz`(person)

**Example 51** (doc_id: `deanon_TRAIN/15Ns82_10t`) (sent_id: `deanon_TRAIN/15Ns82_10t_7`)


Nach Abtretung an das Bezirksgericht Hartberg zur Verbindung mit dem zuvor genannten Verfahren wurde dieses Verfahren vom Bezirksgericht Hartberg an das Bezirksgericht Laa an der Thaya mit dem Bemerken rückabgetreten, dass „eine Einbeziehung auf Grund der angebotenen Diversion nicht möglich“ sei, worauf das Bezirksgericht Laa an der Thaya die Akten zur Entscheidung gemäß § 38 dritter Satz StPO vorlegte.

**False Positives:**

- `Bezirksgericht Hartberg` — no gold match — likely missing annotation
- `Bezirksgericht Hartberg` — no gold match — likely missing annotation
- `Bezirksgericht Laa` — no gold match — likely missing annotation
- `Bezirksgericht Laa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Example 52** (doc_id: `deanon_TRAIN/15Ns82_10t`) (sent_id: `deanon_TRAIN/15Ns82_10t_12`)


Das Bezirksgericht Hartberg, in dessen Zuständigkeit die frühere Straftat (15. Mai 2010) fällt, ist daher nach § 37 Abs 3 iVm § 37 Abs 2 zweiter Satz StPO für die Durchführung des (demnach zu verbindenden) Strafverfahrens AZ 4 U 59/10i des Bezirksgerichts Laa an der Thaya zuständig.

**False Positives:**

- `Bezirksgericht Hartberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/15Os97_10v`) (sent_id: `deanon_TRAIN/15Os97_10v_14`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, verletzt der Vorgang, dass es das Bezirksgericht Innsbruck unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Graeupner im Verfahren AZ 23 BE29/06a des Landesgerichts Innsbruck gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich das Vollzugsgericht in Kenntnis zu setzen, § 494a Abs 7 StPO, wonach das erkennende Gericht all jene Gerichte unverzüglich zu verständigen hat, deren Vorentscheidungen von einer Entscheidung nach § 494a Abs 1 und 6 StPO betroffen sind.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Graeupner`(person)

**Example 54** (doc_id: `deanon_TRAIN/15Os97_10v`) (sent_id: `deanon_TRAIN/15Os97_10v_17`)


Das Bezirksgericht Innsbruck hätte daher sogleich nach Fassung seines Probezeitverlängerungsbeschlusses - und nicht erst im Zuge der Endverfügung vom 31. März 2010 - das Vollzugsgericht davon in Kenntnis setzen müssen.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)

**Example 56** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_7`)


Sie beantragt beim Obersten Gerichtshof gemäß § 28 JN unter Anschluss der einzubringenden Klage die Ordination des Bezirksgerichts für Handelssachen Wien als örtlich zuständiges Gericht, auch wenn aufgrund des Abflugorts das Bezirksgericht Schwechat naheliegend erschiene, das aber in Fluggastsachen überlastet sei.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_10`)


2. Der Oberste Gerichtshof hat bereits in anderen gleichgelagerten Fällen der Durchsetzung von Ansprüchen nach der EU-Fluggastrechte-VO gegen das auch hier beklagte Flugunternehmen mit Sitz in Hirschmühle 31, 8221 Hofing, Österreich (Serbien) die Ordination bewilligt und das Bezirksgericht Schwechat, in dessen Sprengel der Abflughafen liegt, als zuständiges Gericht bestimmt (6 Nc 1/19b = ZVR 2019/114, 259 [zustMayr];

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hirschmühle 31, 8221 Hofing, Österreich`(address)

**Example 58** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_6`)


Mit der am 20. 8. 2012 beim Bezirksgericht Bezirksgericht Hallein eingebrachten Klage begehrte der Minderjährige von einem in Deutschland wohnhaften minderjährigen Beklagten Schadenersatz von 3.850 EUR sA und die Feststellung seiner Haftung für sämtliche aus dessen Steinwurf resultierenden Spät- und Dauerfolgen.

**False Positives:**

- `Bezirksgericht Bezirksgericht Hallein` — partial — gold is substring of pred: `Bezirksgericht Hallein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hallein`(organisation)

**Example 59** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_69`)


8. 2012 beim gemäß Art 5 Nr 3 EuGVVO zuständigen Bezirksgericht Bezirksgericht Weiz (Gericht des Ortes, an dem das schädigende Ereignis eingetreten ist) im Elektronischen Rechtsverkehr eingebracht.

**False Positives:**

- `Bezirksgericht Bezirksgericht Weiz` — partial — gold is substring of pred: `Bezirksgericht Weiz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Weiz`(organisation)

**Example 60** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Bezirksgericht Amstetten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 61** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. Musger als weitere Richter in der Rechtssache der klagenden Partei Glanzbruckkraft-Recycling -Aktiengesellschaft, Steindläcker 26, 4183 Obertraberg, Österreich, vertreten durch THUM WEINREICH SCHWARZ CHYBA REITER Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Verband der Versicherungsunternehmen Österreichs, Schwarzenbergplatz 7, 1030 Wien, vertreten durch Mag. Georg E. Thalhammer, Rechtsanwalt in Wien, wegen 11.550 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Innere Stadt Wien das Bezirksgericht Kitzbühel bestimmt.

**False Positives:**

- `Bezirksgericht Kitzb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Glanzbruckkraft-Recycling`(organisation)
- `Steindläcker 26, 4183 Obertraberg, Österreich`(address)

**Example 62** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_4`)


Text Begründung: Die klagende Partei begehrt in ihrer beim Bezirksgericht Innere Stadt Wien am allgemeinen Gerichtsstand der beklagten Partei eingebrachten Klage Schadenersatz nach einem Verkehrsunfall auf der B 178 im Ortsgebiet von Going am Wilden Kaiser.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_7`)


Nachdem die beklagte Partei das Klagebegehren dem Grunde und der Höhe nach bestritten hatte, beantragte die klagende Partei die Delegierung der Rechtssache an das Bezirksgericht Kitzbühel, in dessen Sprengel sich der Unfall ereignet habe.

**False Positives:**

- `Bezirksgericht Kitzb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_11`)


Das Bezirksgericht Innere Stadt Wien hält die Delegierung für zweckmäßig.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/2Ob162_23x`) (sent_id: `deanon_TRAIN/2Ob162_23x_8`)


Text Begründung: [1] Beim Bezirksgericht St. Johann im Pongau ist zu AZ 455 A 78/22f das Verlassenschaftsverfahren nach dem 2022 verstorbenen Erblasser anhängig.

**False Positives:**

- `Bezirksgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)

**Example 67** (doc_id: `deanon_TRAIN/3Nc32_19i`) (sent_id: `deanon_TRAIN/3Nc32_19i_5`)


Das Bezirksgericht Telfs legte den Akt unmittelbar (dh ohne jede sonstige Erledigung) von Amts wegen dem Obersten Gerichtshof zwecks Entscheidung über eine Ordination nach § 28 JN vor.

**False Positives:**

- `Bezirksgericht Telfs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/3Nc32_19i`) (sent_id: `deanon_TRAIN/3Nc32_19i_8`)


Da das angerufene Bezirksgericht Telfs bislang noch nicht negativ über seine Zuständigkeit entschieden hat, kommt eine Ordination nach § 28 JN nicht in Betracht.

**False Positives:**

- `Bezirksgericht Telfs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

**Example 70** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_30`)


Als örtlich zuständiges Exekutionsgericht für die beabsichtigte Rechteexekution ist das Bezirksgericht Salzburg zu bestimmen, weil die Logcon-Möbel.at GmbH als Registrierungsstelle der von der beabsichtigten Exekutionsführung betroffenen Domain der Verpflichteten im Sprengel dieses Gerichts ihren Sitz hat.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Logcon-Möbel.at`(organisation)

**Example 71** (doc_id: `deanon_TRAIN/3Ob203_11s`) (sent_id: `deanon_TRAIN/3Ob203_11s_9`)


Am selben Tag langte eine von den Antragstellern selbst verfasste Berufung per Fax beim Bezirksgericht Saalfelden ein.

**False Positives:**

- `Bezirksgericht Saalfelden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_5`)


Für die Bewilligung und die Vollziehung der beabsichtigten Exekution gegen die Zweitbeklagte auf Urteilsveröffentlichung wird das Bezirksgericht Innere Stadt Wien als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_8`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_19`)


Dem Ordinationsantrag ist somit stattzugeben und zweckmäßigerweise das Bezirksgericht Innere Stadt Wien als zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Innere Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_14`)


Mit dem vorliegendenOrdinationsantragbegehren die Kläger, für die Rechtssache das Bezirksgericht Imst als örtlich zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Imst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_15`)


Sie gestehen zu, dass das angerufene Bezirksgericht Imst nicht zufolge § 83 Abs 1 JN zuständig sei, weil der Bestandgegenstand nicht im Sprengel dieses Bezirksgerichts, sondern im Fürstentum Liechtenstein liege.

**False Positives:**

- `Bezirksgericht Imst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_4`)


Kirsten Falterer, MA, vertreten durch Mag. Daniel Schöpf, Mag. Christian Maurer, Mag. Daniel Maurer, Rechtsanwälte in Salzburg, gegen die beklagte Partei Mona Gronmayer, BSc, vertreten durch die Steiner Anderwald Rechtsanwälte OG in Spittal an der Drau, wegen 28.017,16 EUR sA, über Vorlage des Akts AZ 3 C 361/20p des Bezirksgerichts Spittal an der Drau zur Entscheidung eines negativen Kompetenzkonflikts, den Beschluss gefasst:  Spruch Zur Fortführung dieser Rechtssache ist das Bezirksgericht Spittal an der Drau zuständig.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kirsten Falterer, MA`(person)
- `Mona Gronmayer, BSc`(person)

**Example 78** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_6`)


Text Begründung: Mit der beim Bezirksgericht Salzburg eingebrachten Mahnklage begehrte der Kläger von der Beklagten die Zahlung von 28.017,16 EUR sA.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_9`)


In ihrem Einspruch gegen den vom Bezirksgericht Salzburg erlassenen Zahlungsbefehl erhob die Beklagte die Einrede der sachlichen und örtlichen Unzuständigkeit mit der Begründung, die Rechnungen stünden in einem tatsächlichen und rechtlichen Zusammenhang und seien daher zusammenzurechnen.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_11`)


Der Kläger räumte daraufhin ein, dass die Forderungen gemäß § 55 JN zusammenzurechnen seien, und stellte für den Fall, dass sich das Bezirksgericht Salzburg für unzuständig erklärt, den Antrag, die Klage an das nicht offenbar unzuständige Landesgericht Salzburg zu überweisen.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_12`)


Für den Fall der Unzuständigkeit dieses Landesgerichts beantragte er die Überweisung an das Landesgericht Klagenfurt, allenfalls an das Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_13`)


Das Bezirksgericht Salzburg sprach mit rechtskräftigem Beschluss vom 6. Dezember 2019 seine sachliche Unzuständigkeit aus und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_17`)


Über Antrag des Klägers hob das Landesgericht Klagenfurt die Zurückweisung der Klage mit rechtskräftigem Beschluss vom 14. Februar 2020 auf und überwies die Rechtssache dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_18`)


Das Bezirksgericht Spittal an der Drau lehnte mit rechtskräftigem Beschluss vom 20. Mai 2020 „die Übernahme der überwiesenen Rechtssache ab“ und erklärte sich für sachlich unzuständig.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_20`)


Das Bezirksgericht Spittal an der Drau legte den Akt dem Oberlandesgericht Graz gemäß § 47 Abs 2 JN zur Entscheidung über den negativen Kompetenzkonflikt vor.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_24`)


Zwar haben hier das Bezirksgericht Salzburg, das Landesgericht Salzburg, das Landesgericht Klagenfurt und das Bezirksgericht Spittal an der Drau jeweils seine Zuständigkeit verneint.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation
- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 87** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_25`)


Allerdings besteht ein Streit über die Zuständigkeit iSd § 47 Abs 1 JN nur zwischen dem Landesgericht Klagenfurt und dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_36`)


5.Das Bezirksgericht Spittal an der Drau missachtete mit seiner Unzuständigkeitsentscheidung die dargestellte Bindungswirkung des vorausgehenden Beschlusses des Landesgerichts Klagenfurt.

**False Positives:**

- `Bezirksgericht Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und den Hofrat Dr. Steger als weitere Richter in der Pflegschaftssache des mj Dr.in Selina Mäntler, geboren am 1. Dezember 2003, Vater Techn R DDr. OStR KzlR Daniel von Reichardt, vertreten durch Prof. Dr. Georg Zanger, Rechtsanwalt in Wien, wegen Obsorge, über den Delegierungsantrag der Mutter Lynn Eisenbarth, vertreten durch Mag. Britta Schönhart-Loinig, Rechtsanwältin in Wien, den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Pflegschaftssache vom Bezirksgericht Gänserndorf an das Bezirksgericht Villach wird abgewiesen.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Selina Mäntler`(person)
- `1. Dezember 2003`(date)
- `Techn R DDr. OStR KzlR Daniel von Reichardt`(person)
- `Lynn Eisenbarth`(person)

**Example 90** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_22`)


7. 2019 die Delegierung der Pflegschaftssache an das Bezirksgericht Villach nach § 31 Abs 1 JN.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_28`)


Da der Mittelpunkt der Lebensführung des Kindes nunmehr in Velden liege und offene Anträge nicht gegen eine Zuständigkeitsübertragung sprächen, sei das Bezirksgericht Villach besser in der Lage, die pflegschaftsgerichtlichen Agenden zu besorgen.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_36`)


Die Handhabung des pflegschaftsgerichtlichen Schutzes des Kindes sei durch das Bezirksgericht Gänserndorf wirksamer gestaltbar als durch das Bezirksgericht Villach, das die Familie überhaupt noch nicht kenne.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_58`)


das delegierte Bezirksgericht Villach müsste sich in den mittlerweile bereits umfangreichen Pflegschaftsakt erst einarbeiten.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_62`)


Dass in diesem Verfahrensstadium die Delegierung der Pflegschaftssache an das Bezirksgericht Villach dem Kindeswohl besser entsprechen würde als die Weiterführung des Obsorge- und Kontaktrechtsverfahrens durch den bisher zuständigen Richter des Bezirksgerichts Gänserndorf, ist ebensowenig zu erkennen wie eine dadurch erzielbare Verfahrensbeschleunigung und Erleichterung des Gerichtszugangs für sämtliche Beteiligte.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_TRAIN/5Nc28_19s`) (sent_id: `deanon_TRAIN/5Nc28_19s_63`)


Der Umstand, dass der Minderjährige derzeit im Sprengel des Bezirksgerichts Villach wohnt und für die Mutter seine Betreuung bei Terminen am Bezirksgericht Villach leichter zu organisieren wäre als beim Bezirksgericht Gänserndorf, reicht daher für eine Bejahung der Zweckmäßigkeit iSd § 31 Abs 1 JN nicht aus.

**False Positives:**

- `Bezirksgericht Villach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_TRAIN/6Ob199_10y`) (sent_id: `deanon_TRAIN/6Ob199_10y_5`)


Im vorliegenden Verfahren geht es um die pflegschaftsbehördliche Genehmigung eines Vergleichs vor dem Bezirksgericht Meidling.

**False Positives:**

- `Bezirksgericht Meidling` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_4`)


Ophelia Kadlecova, und 2. Constanze Ishikawa, wegen Erlassung einer einstweiligen Verfügung, infolge der Vorlage des Aktes 1 C 16/12t des Bezirksgerichts Wiener Neustadt zur Entscheidung über den negativen Kompetenzkonflikt mit dem Bezirksgericht Mürzzuschlag nach § 47 JN den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag auf Erlassung der einstweiligen Verfügung ist das Bezirksgericht Wiener Neustadt zuständig.

**False Positives:**

- `Bezirksgericht Wiener Neustadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ophelia Kadlecova`(person)
- `Constanze Ishikawa`(person)

</details>

---

## `Specific Compound GmbH 10`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `f7a6637a`  
**Description:**
Matches 'Bersud Möbel GMBH' and similar 'Möbel' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Möbel\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob145_18d`) (sent_id: `deanon_TRAIN/4Ob145_18d_4`)


Matzka und Dr. Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH, Lieselotte Wesp, vertreten durch Hauswirth - Kleiber Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1) DI Amber Rzehatschek, 2) DI Esra Noth, ebendort, beide vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, 3) Trinks Möbel GmbH, Hütten 15, 5221 Lasberg, Österreich, vertreten durch Mag. Thomas Stenitzer und Mag. Kurt Schick, Rechtsanwälte in Laa an der Thaya, und 4) DI (FH) Wladimir Runzheimer, vertreten durch Mag. Bernhard Österreicher, Rechtsanwalt in Pfaffstätten, wegen 127.614,09 EUR sA und Feststellung (Streitwert: 5.200 EUR), über die außerordentliche Revision der erst- und zweitbeklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. April 2018, GZ 1 R 179/17a-29, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Trinks Möbel GmbH` | `Trinks Möbel GmbH` |

**Missed by this rule (FN):**

- `MGL Forschung Consulting GmbH` (organisation)
- `Lieselotte Wesp` (person)
- `DI Amber Rzehatschek` (person)
- `DI Esra Noth` (person)
- `Hütten 15, 5221 Lasberg, Österreich` (address)
- `Wladimir Runzheimer` (person)

</details>

---

## `Specific Compound GmbH 12`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `5dc5ef00`  
**Description:**
Matches 'WXE Textil GMBH' and similar 'Textil' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Textil\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 166 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

</details>

---

## `LG abbreviation`

**F1:** 0.006 | **Precision:** 0.167 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `e5b7265e`  
**Description:**
Matches 'LG' followed by city names, e.g., 'LG Innsbruck'.

**Content:**
```
\bLG\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.003 | 0.006 | 6 | 1 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 5 | 294 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `LG Wels` | `LG Wels` |

**Missed by this rule (FN):**

- `FN912691n` (business_register_number)
- `Landesgericht Klagenfurt` (organisation)
- `Holtschmidt Versicherung GmbH` (organisation)
- `Lohneis Pflege gesellschaft mbH` (organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `LG Steyr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob68_14z`) (sent_id: `deanon_TRAIN/4Ob68_14z_22`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `LG Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_40`)


Dieser Auffassung hat sich zwischenzeitig bereits zweitinstanzliche Rechtsprechung ausdrücklich (vgl etwa LG Salzburg EFSlg 156.701 [2018], 159.791, 159.792 [2019];

**False Positives:**

- `LG Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_41`)


LG Linz EFSlg 156.702 [2018], 159.793 [2019]) und die Entscheidung 9 Ob 57/17y offensichtlich angeschlossen.

**False Positives:**

- `LG Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Ob127_14y`) (sent_id: `deanon_TRAIN/7Ob127_14y_64`)


2.1 In Deutschland setzt der Versicherungsfall „Schneedruck“ voraus, dass die versicherte Sache durch die Wirkung des Gewichts von Schnee oder Eismassen beschädigt wird (LG Meiningen r & s 2009, 69;

**False Positives:**

- `LG Meiningen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Greiner-Mai Event`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `297fcc00`  
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

## `NordDaten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1edc6ba7`  
**Description:**
Matches the specific entity 'NordDaten'.

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

## `Technik Ostbachal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `687bd956`  
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

## `Vossbein Lebensmittel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `606c3ff4`  
**Description:**
Matches the specific entity 'Vossbein Lebensmittel'.

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

## `Paweltschik Telekom GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b15a7862`  
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

## `Nexgartuni Finanzen Planung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bcd7be36`  
**Description:**
Matches the specific entity 'Nexgartuni Finanzen Planung GMBH'.

**Content:**
```
\bNexgartuni\s+Finanzen\s+Planung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AlpenSicherheit GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5f0c9201`  
**Description:**
Matches the specific entity 'AlpenSicherheit GMBH'.

**Content:**
```
\bAlpenSicherheit\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinemut Smoch Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `470fcb8c`  
**Description:**
Matches the specific entity 'Reinemut + Smoch Handel' found in multiple failures.

**Content:**
```
Reinemut\s*\+\s*Smoch\s*Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7c422cd1`  
**Description:**
Matches 'FA Salzburg-Stadt' and 'Finanzamt Salzburg-Stadt' including the www. prefix.

**Content:**
```
(?:www\.)?FA\s*Salzburg\-Stadt|Finanzamt\s*Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TalVerverwerkGarten GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `92ef9b5e`  
**Description:**
Matches the specific entity 'TalVerverwerkGarten GMBH' including the ellipsis variant.

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

## `Henken`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d026d57e`  
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

## `Süd-Landwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7f815650`  
**Description:**
Matches the specific entity 'Süd-Landwirtschaft'.

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

## `Specific Company Grönemeier`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4eee39aa`  
**Description:**
Matches the specific entity 'Grönemeier&Hövelberndt E‑Commerce'.

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

## `Specific Company Milan Händlein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `41e4c5a7`  
**Description:**
Matches the specific entity 'Milan Händlein'.

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

## `Specific Company Annemie Bott`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c7f29664`  
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

## `Specific Company Krolitzki`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `45df2358`  
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

## `Specific Company Manfredo Herrschmann`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ff59234b`  
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

## `Specific Company StadtEnergie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `16526f53`  
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

## `Specific Company Laskowsky`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9a352a4b`  
**Description:**
Matches the specific entity 'Laskowsky Umwelt'.

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

## `Specific Company TraunChemie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `467653e9`  
**Description:**
Matches the specific entity 'TraunChemie GMBH'.

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

## `Specific Company Butkus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a70a0e0b`  
**Description:**
Matches the specific entity 'Butkus Metall'.

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

## `Specific Company Englert`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7fb61038`  
**Description:**
Matches the specific entity 'Englert Möbel'.

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

## `Specific Company Keldonbach`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e899b8a9`  
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

## `Sanitär Talder GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f257002`  
**Description:**
Matches the specific entity 'Sanitär Talder GMBH'.

**Content:**
```
Sanitär\s+Talder\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Roelfsen Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `11028e60`  
**Description:**
Matches the specific entity 'Roelfsen Versicherung'.

**Content:**
```
Roelfsen\s+Versicherung
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lubomir Merschmeyer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `91685d83`  
**Description:**
Matches the specific entity 'Lubomir Merschmeyer'.

**Content:**
```
Lubomir\s+Merschmeyer
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Houdek Maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e110e4b5`  
**Description:**
Matches the specific entity 'Houdek Maschinenbau'.

**Content:**
```
Houdek\s+Maschinenbau
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schmeltz Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `19a4f00e`  
**Description:**
Matches the specific entity 'Schmeltz Luftfahrt'.

**Content:**
```
Schmeltz\s+Luftfahrt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dorfcon-Verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cfe657a4`  
**Description:**
Matches the specific entity 'Dorfcon-Verlag'.

**Content:**
```
Dorfcon-Verlag
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lexdon IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3407167e`  
**Description:**
Matches the specific entity 'Lexdon IT'.

**Content:**
```
Lexdon\s+IT
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stadt Logglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `733a2290`  
**Description:**
Matches the specific entity 'Stadt Logglanz'.

**Content:**
```
Stadt\s+Logglanz
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gözcü Getränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a13a0930`  
**Description:**
Matches the specific entity 'Gözcü Getränke'.

**Content:**
```
Gözcü\s+Getränke
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hörup Gastronomie AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e6cc383`  
**Description:**
Matches the specific entity 'Hörup Gastronomie AG'.

**Content:**
```
Hörup\s+Gastronomie\s+AG
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dammke KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2e5c5578`  
**Description:**
Matches the specific entity 'Dammke KI GMBH'.

**Content:**
```
Dammke\s+KI\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TraunChemie GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e8d7d3d8`  
**Description:**
Matches the specific entity 'TraunChemie GMBH'.

**Content:**
```
TraunChemie\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tritri-IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3850ee07`  
**Description:**
Matches the specific entity 'Tritri-IT'.

**Content:**
```
Tritri-IT
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien 1/23`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `46c6a075`  
**Description:**
Matches 'Finanzamt Wien 1/23'.

**Content:**
```
Finanzamt\s+Wien\s+1/23
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Wien 1/23`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1446165d`  
**Description:**
Matches 'FA Wien 1/23'.

**Content:**
```
\bFA\s+Wien\s+1/23
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Naaß Elektro GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66e0c123`  
**Description:**
Matches the specific entity 'Naaß Elektro GMBH'.

**Content:**
```
Naaß\s+Elektro\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bersud Möbel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `86f251e0`  
**Description:**
Matches the specific entity 'Bersud Möbel GMBH'.

**Content:**
```
Bersud\s+Möbel\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Unter Heimdorf GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ad00504a`  
**Description:**
Matches the specific entity 'Unter Heimdorf GMBH'.

**Content:**
```
Unter\s+Heimdorf\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WXE Textil GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d0cea1d1`  
**Description:**
Matches the specific entity 'WXE Textil GMBH'.

**Content:**
```
WXE\s+Textil\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kornfelder Recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8cb601c4`  
**Description:**
Matches the specific entity 'Kornfelder Recycling'.

**Content:**
```
Kornfelder\s+Recycling
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `DGCV E-Commerce GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b90a5241`  
**Description:**
Matches the specific entity 'DGCV E-Commerce GMBH' (handling both en-dash and hyphen variants if necessary, but focusing on the text provided).

**Content:**
```
DGCV\s+E[\u2011-]Commerce\s+GMBH
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UGQQ Verlag OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2e67d665`  
**Description:**
Matches the specific entity 'UGQQ Verlag OG'.

**Content:**
```
UGQQ\s+Verlag\s+OG
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fatima Finkenbein`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d1b9dad6`  
**Description:**
Matches the specific entity 'Fatima Finkenbein' as an organization in this context.

**Content:**
```
Fatima\s+Finkenbein
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wien Waldnor KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e85980b6`  
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

## `Botho Mikloweit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `28965f3f`  
**Description:**
Matches the specific entity 'Botho Mikloweit' as an organization in this context.

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

## `Kraftver-Gastronomie GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b775ac82`  
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

## `Gartgart Dienstleistungen GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `980b9a06`  
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

## `Gogel Daten GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `197e92cb`  
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

## `Klein-Vorholt KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `db01081f`  
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

## `Raiffeisenkasse Retz-Pulkautal`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b6b0b60b`  
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

## `Nord Kellex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cb0cc520`  
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

## `Specific Company Norconheim`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4e1374bc`  
**Description:**
Matches the specific entity 'Norconheim'.

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

## `Specific Company Nexdorf-Metall`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `24d13a6b`  
**Description:**
Matches the specific entity 'Nexdorf-Metall'.

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

## `Specific Company Oppert Elektro`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bf14d09e`  
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

## `Specific Company Zimmerhackel Bau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `271fecc4`  
**Description:**
Matches the specific entity 'Zimmerhackel Bau'.

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

## `Specific Company Vahrenkamp Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `14ac09bd`  
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

## `Specific Company Gorius und Ziegann Event GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c03e94b9`  
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

## `Specific Company Raiffeisenbank Rion Vöcklabruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e8f5f0e9`  
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

## `Specific Company Basdas Pharma AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9d77209f`  
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

## `Depp Versand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5ad4913c`  
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

## `SüdEvent AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ca4bc5ae`  
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

## `Obernöder+Küsbert Touristik GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4470d15c`  
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

## `Talost GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3beed63c`  
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

## `Finanzamt with location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a87b0377`  
**Description:**
Matches full names of tax authorities, ensuring 'Oststeiermark' and 'Salzburg-Stadt' are covered.

**Content:**
```
\bFinanzamt\s+(?:Steiermark\s+Mitte|Nieder\u00f6sterreich\s+Mitte|Salzburg-Land|Salzburg-Stadt|Vorarlberg|Waldviertel|Klosterneuburg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Innsbruck|Linz|Tirol\s+Ost|Bruck\s+Leoben\s+M\u00fcrzzuschlag|Braunau\s+Ried\s+Sch\u00e4rding|Grieskirchen\s+Wels|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Amstetten\s+Melk\s+Scheibbs|Kirchdorf\s+Perg\s+Steyr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Landeck\s+Reutte|Schwechat\s+Gerasdorf|Freistadt\s+Rohrbach\s+Urfahr|Purkersdorf|Wien\s+\d+/\d+(?:/\d+)*(?:/\d+)*|Gmunden\s+V\u00f6cklabruck|Wels\s+S\u00fcd|Oststeiermark|[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 55 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/8Ob31_24b`) (sent_id: `deanon_TRAIN/8Ob31_24b_20`)


C-545/18,DP/Finanzamt Linz, C-920/19,FluctusundFluentum;

**False Positives:**

- `Finanzamt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `FA abbreviation with location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d5845d57`  
**Description:**
Matches abbreviated tax authorities, ensuring 'Oststeiermark' and 'Salzburg-Stadt' are covered.

**Content:**
```
\bFA\s+(?:Steiermark\s+Mitte|Nieder\u00f6sterreich\s+Mitte|Salzburg-Land|Salzburg-Stadt|Vorarlberg|Waldviertel|Klosterneuburg|Bruck\s+Eisenstadt\s+Oberwart|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Graz-Stadt|Innsbruck|Linz|Tirol\s+Ost|Bruck\s+Leoben\s+M\u00fcrzzuschlag|Braunau\s+Ried\s+Sch\u00e4rding|Grieskirchen\s+Wels|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Amstetten\s+Melk\s+Scheibbs|Kirchdorf\s+Perg\s+Steyr|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Landeck\s+Reutte|Schwechat\s+Gerasdorf|Freistadt\s+Rohrbach\s+Urfahr|Purkersdorf|Wien\s+\d+/\d+(?:/\d+)*(?:/\d+)*|Gmunden\s+V\u00f6cklabruck|Wels\s+S\u00fcd|Oststeiermark|[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Inn-Recycling Institut GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b3da11b4`  
**Description:**
Matches the specific entity 'Inn-Recycling Institut GMBH'.

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

## `EnnsBildung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c0c96d4e`  
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

## `Olivier u. Bartha Recycling`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c87f2aeb`  
**Description:**
Matches the specific entity 'Olivier u. Bartha Recycling'.

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

## `West-Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `30f675c7`  
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

## `Chen Setzekorn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7c18768f`  
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

## `Istvan Gerart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `80112cb8`  
**Description:**
Matches the specific entity 'Istvan Gerart'.

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

## `Berwaldkel-Möbel AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0faa5e01`  
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

## `Landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c413d0ce`  
**Description:**
Matches district courts like 'Landesgericht Innsbruck'.

**Content:**
```
\bLandesgericht\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 87 | 0 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 87 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Verfahrenshilfesache der Antragstellerin Florenzia Elefterakis, gegen den Antragsgegner Univ.-Prof. Dr. Leander Rossetti, wegen Bewilligung der Verfahrenshilfe, über den Antrag der Antragstellerin auf Delegierung der Rechtssache an das Landesgericht Korneuburg den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Rechtssache an das Landesgericht Korneuburg wird abgewiesen.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation
- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Florenzia Elefterakis`(person)
- `Dr. Leander Rossetti`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_4`)


Text Begründung: Die Antragstellerin richtete an das Landesgericht Linz einen Antrag auf Bewilligung der Verfahrenshilfe, weil sie gegen einen gerichtlichen Sachverständigen wegen eines in einem Pflegegeldprozess unrichtig erstatteten Gutachtens eine Schadenersatzklage auf Zahlung entgangenen Pflegegeldes und von Schmerzengeld erheben wolle.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_5`)


Das Landesgericht Linz leitete ein Verbesserungsverfahren ein.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_6`)


Die Antragstellerin beantwortete den schriftlichen Verbesserungsauftrag und beantragte die Delegierung des Verfahrens an das Landesgericht Korneuburg mit der Begründung, dass sie wegen ihrer körperlichen Behinderungen der Einladung der Richterin des Landesgerichts Linz, sie wegen offener Fragen bei Gericht aufzusuchen, nicht folgen könne.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc13_15s`) (sent_id: `deanon_TRAIN/10Nc13_15s_8`)


Das Landesgericht Linz äußerte sich zu diesem Antrag dahin, eine Delegierung könnte zweckmäßig sein, erscheine doch eine persönliche (ergänzende) Befragung der Antragstellerin zum Verfahrenshilfeantrag sinnvoll.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_3`)


Kopf Der Oberste Gerichtshof hat am 30. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz als weitere Richter in Gegenwart der Richterin Dr. Sadoghi als Schriftführerin in den Strafsachen gegen Peter Hanrich zu AZ 35 Hv 99/12a des Landesgerichts St. Pölten und zu AZ 5 U 42/16w des Bezirksgerichts Steyr, zwischen diesen Gerichten geführten Zuständigkeitsstreit nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag des Verurteilten auf nachträgliche Milderung der mit Urteil des Landesgerichts St. Pölten vom 3. September 2012, GZ 35 Hv 99/12a-16, ausgesprochenen Freiheitsstrafe ist das Landesgericht St. Pölten zuständig.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hanrich`(person)

**Example 6** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_11`)


Das Bezirksgericht Steyr übermittelte eine Kopie dieses Antrags dem Landesgericht St. Pölten zu AZ 35 Hv 99/12a „zur Entscheidung über den Antrag auf Strafmilderung zu der widerrufenen bedingten Entlassung zu 38 BE 50/13x LG Steyr (§ 410 StPO)“.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_12`)


Mit Note vom 17. Februar 2017 teilte das Landesgericht St. Pölten dem Bezirksgericht Steyr mit, „dass derAntrag offensichtlich auf nachträgliche Milderung der mit Urteil des BG Steyr vom 11.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_16`)


hinsichtlich des widerrufenen Teils aus der bedingten Entlassung zu AZ 38 BE 50/13x des Landesgerichts Steyr komme die Zuständigkeit jedoch dem Landesgericht St. Pölten zu, weil dieses in erster Instanz erkannt habe.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_18`)


Daraufhin übermittelte das Bezirksgericht Steyr die Akten dem Landesgericht St. Pölten mit dem Ersuchen um Äußerung zur Zuständigkeitsfrage im Sinn der Ausführungen des Obersten Gerichtshofs.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_19`)


Nunmehr legt das Landesgericht St. Pölten die Akten dem Obersten Gerichtshof vor, weil nach Ansicht des Einzelrichters der Antrag des Verurteilten nicht darauf abziele, „dass das Landesgericht St. Pölten das mit Urteil vom 03.

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation
- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 11** (doc_id: `deanon_TRAIN/11Ns22_17z`) (sent_id: `deanon_TRAIN/11Ns22_17z_23`)


12. 2013 zu 38 BE 50/13x gewährte bedingte Entlassung widerrufen wurde, dahingehend mildern möge, dass vom Widerruf abgesehen wird“, und sich das Landesgericht St. Pölten für diese „Milderung des Urteils des Bezirksgerichts Steyr durch Absehen vom Widerruf der bedingten Entlassung“ für nicht zuständig erachtet (ON 61 der Hv-Akten).

**False Positives:**

- `Landesgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_6`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 13. Juni 2019, AZ 28 Bl 68/19p, nicht Folge gegeben.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_4`)


Gründe:  Rechtliche Beurteilung Nach dem Norbert Naegelkraemer durch das Landesgericht Krems an der Donau am 4. Dezember 2015, GZ 16 Hv 32/15g-23, mehrerer Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB schuldig erkannt und zu einer teilbedingten Freiheitsstrafe verurteilt worden war, ordnete der Einzelrichter des genannten Landesgerichts nach Rechtskraft des Urteils die Zustellung der Aufforderung zum Strafantritt an den Verurteilten an.

**False Positives:**

- `Landesgericht Krems` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__5`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 17. Mai 2018, AZ 22 Bl 38/18f, 22 Bl 43/18s, nicht Folge gegeben.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_12`)


Bei der Glaubwürdigkeitsbeurteilung ließ das Erstgericht weder die Divergenzen in den Angaben der Asli Dawids (vgl US 14) noch ihre Verurteilung durch das Landesgericht Feldkirch unberücksichtigt (vgl US 16).

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dawids`(person)

**Example 17** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__8`)


Mit zugleich gefasstem Beschluss sprach das Landesgericht Innsbruck gemäß § 265 StPO - ebenfalls unter Bestimmung einer dreijährigen Probezeit - die bedingte Entlassung aus dem im Urteilszeitpunkt noch nicht (durch Anrechnung der Vorhaft) verbüßten (unbedingten) Strafteil von einem Monat, zwanzig Tagen und einer Stunde aus (ON 48, nicht journalisierte Kopie des genannten Urteils).

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__11`)


Unter einem fasste das Landesgericht Innsbruck den Beschluss, vom Widerruf der mit Urteil dieses Gerichts vom 6. März 2009, GZ 23 Hv 189/07m-104, gewährten bedingten Strafnachsicht abzusehen, die mit dem gemeinsam mit diesem Urteil ergangenen Beschluss gewährte bedingte Entlassung jedoch zu widerrufen (ON 49 S 3).

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__13`)


Mit - unbekämpft in Rechtskraft erwachsenem - Beschluss vom 3. Februar 2012 (ON 54) rechnete das Landesgericht Innsbruck „gem § 400 StPO“ die in der Zeit vom 13. Dezember 2011, 17:00 Uhr, bis zum 23. Jänner 2012, 17:00 Uhr, im Verfahren AZ 27 HR 323/11h (= 20 Hv 43/12b) des Landesgerichts Feldkirch erlittene Verwahrungs- und Untersuchungshaft auf die mit Urteil vom 10. Jänner 2012 (ON 49) verhängte Freiheitsstrafe an (1) und sprach aus, dass der nach dieser Anrechnung aus dem genannten Urteil und dem gleichzeitig mit diesem gefassten Widerrufsbeschluss verbleibende Strafrest von einem Monat und zehn Tagen unter Bestimmung einer Probezeit von drei Jahren „bedingt nachgesehen“ werde (2).

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__21`)


Da das Landesgericht Innsbruck hinsichtlich der mit - sogleich in Rechtskraft erwachsenem (ON 49 S 4) - Urteil vom 10. Jänner 2012 ausgesprochenen (ON 49 S 2) und der mit dem unter einem gefassten Widerrufsbeschluss aktualisierten (ON 49 S 3; siehe dazu aber (3) des Erkenntnisses) Freiheitsstrafe keine Strafvollzugsanordnung erließ, verletzte es somit § 397 erster Satz StPO iVm § 3 Abs 1 StVG.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__26`)


Ein Nachteil entstand der Verurteilten dadurch auch in Bezug auf die einen Monat übersteigende Untersuchungshaftzeit nicht, weil das Landesgericht Feldkirch zu AZ 20 Hv 43/12b - unter Missachtung des § 38 Abs 1 StGB - die vom Punkt 1 des Beschlusses des Landesgerichts Innsbruck vom 3. Februar 2012 (ON 54) umfasste Haftzeit (erneut zur Gänze) auf die im bezeichneten Verfahren verhängte (unbedingte) Freiheitsstrafe anrechnete.

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/14Os159_11f_14Os160_11b_`) (sent_id: `deanon_TRAIN/14Os159_11f_14Os160_11b__19`)


Das Landesgericht Wr. Neustadt hat durch seine Beschlussfassung auf Verlängerung der Probezeit nach § 494a Abs 6 StPO eine ihm nicht (mehr) zustehende Kompetenz in Anspruch genommen und solcherart den sich aus dem 16.

**False Positives:**

- `Landesgericht Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_3`)


Kopf Der Oberste Gerichtshof hat am 1. Februar 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in der Strafsache gegen Christian Enghardt wegen Überwachung von Entscheidungen über Bewährungsmaßnahmen, AZ 196 Ns 10/16y des Landesgerichts für Strafsachen Wien, über den Zuständigkeitsstreit zwischen diesem Gericht und dem Landesgericht Klagenfurt nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Enghardt`(person)

**Example 24** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_4`)


2005 den Beschluss gefasst:  Spruch Zur Führung des Verfahrens zur Überwachung der Entscheidungen des Amtsgerichts Zehdenick vom 25. November 2014, AZ 41 Ds 3101 Js 9050/14 (41/14), ist das Landesgericht Klagenfurt zuständig.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_5`)


Gründe:  Rechtliche Beurteilung Mit einem am 8. September 2016 beim Landesgericht Klagenfurt eingelangten Schreiben ersucht die Staatsanwaltschaft Neuruppin um „Übernahme der weiteren Strafvollstreckung der Gesamtfreiheitsstrafe“ und (der Sache nach nur) um Überwachung der Entscheidungen des Amtsgerichts Zehdenick (Deutschland) vom 25. November 2014, AZ 41 Ds 3101 Js 9050/14 (41/14), mit denen Christian Emanuelli wegen Diebstahls in besonders schwerem Fall und wegen Urkundenfälschung zu einer – für eine Bewährungszeit von fünf Jahren ausgesetzten – Gesamtfreiheitsstrafe von einem Jahr und neun Monaten verurteilt wurde und die Anordnung von Bewährungshilfe sowie die Erteilung von Weisungen erfolgten (ON 12).

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_6`)


Das Landesgericht Klagenfurt trat das Verfahren nach einer Melderegisterabfrage – derzufolge der Verurteilte zuletzt am 17. August 2016 in Klagenfurt gemeldet war und seither keine aufrechte Meldung aufweist (ON 13 S 3) – am 15. September 2016 „gemäß § 40a Abs 3 EU-JZG iVm § 40a Abs 2 zweiter Satz EU-JZG“ dem Landesgericht für Strafsachen Wien ab, weil Christian Ewersmann „nicht mehr im Sprengel des Landesgerichts Klagenfurt wohnhaft“ sei (ON 1 S 5).

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ewersmann`(person)

**Example 27** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_7`)


Dieses Gericht legte die Akten dem Obersten Gerichtshof gemäß § 38 StPO (iVm § 1 Abs 2 EU-JZG iVm § 9 Abs 1 ARHG) zur Entscheidung über einen negativen Kompetenzkonflikt vor, weil das Ersuchen der Staatsanwaltschaft Neuruppin nicht die Übernahme der Vollstreckung einer unbedingten Freiheitsstrafe betreffe und zufolge der besonderen Bindung des Verurteilten zu Klagenfurt und aufgrund des letzten Wohnsitzes ebendort „gemäß § 83 Abs 1 und 2 EU-JZG iVm § 1 Abs 2 EU-JZG iVm § 67 Abs 1 ARHG iVm § 9 ARHG iVm § 25 Abs 2 StPO“ das Landesgericht Klagenfurt zuständig sei.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_14`)


Da Christian Ernstschneider im Zeitpunkt des Einlangens des Ersuchens der deutschen Behörden keine aufrechte Meldung in Österreich aufwies und Anhaltspunkte dafür bestehen, dass auch der zuvor ständige Aufenthalt des Verurteilten in Klagenfurt nicht mehr gegeben ist (vgl das Erhebungsergebnis ON 18), hätte das Landesgericht Klagenfurt die Staatsanwaltschaft Neuruppin um Ergänzungen iSd § 84 Abs 2 Z 2 EU-JZG ersuchen müssen.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernstschneider`(person)

**Example 29** (doc_id: `deanon_TRAIN/15Ns89_16f`) (sent_id: `deanon_TRAIN/15Ns89_16f_18`)


Liegt auch nach Durchführung des Ergänzungsverfahrens gemäß § 84 Abs 2 EU-JZG keiner der in § 83 Abs 2 EU-JZG genannten Anknüpfungspunkte vor, hat das von der ersuchenden Behörde als zuständig behauptete angerufene Gericht (hier: das Landesgericht Klagenfurt) die begehrte Überwachung mit Blick auf § 82 Abs 1 und 2 EU-JZG abzulehnen.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in Punkt A./2./ des Schuldspruchs sowie im Strafausspruch aufgehoben und es wird die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/15Os97_10v`) (sent_id: `deanon_TRAIN/15Os97_10v_11`)


Das Landesgericht Innsbruck als Berufungsgericht gab dieser Berufung der Staatsanwaltschaft wegen des Ausspruchs über die Strafe schließlich mit Urteil vom 9. März 2010, AZ 21 B1 478/09s (= ON 26 im Erkenntnisakt) Folge und erhöhte die Freiheitsstrafe auf drei Monate.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/1Nc10_18p`) (sent_id: `deanon_TRAIN/1Nc10_18p_4`)


Text Begründung: Das Landesgericht Klagenfurt entzog mit Beschluss vom 28.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Landesgericht Wiener Neustadt` — no gold match — likely missing annotation
- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)

**Example 34** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_7`)


Die Klägerin begehrte die Delegierung des Verfahrens gemäß § 31 JN an das Landesgericht Feldkirch.

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_23`)


Im vorliegenden Fall haben sowohl die Klägerin als auch das vorlegende Gericht zutreffend auf jene Umstände hingewiesen, die insgesamt eine Delegierung an das Landesgericht Feldkirch zweckmäßig erscheinen lassen (vgl dazu RIS-Justiz RS0046540), kann doch vor diesem Gericht unter Wahrung des Unmittelbarkeitsgrundsatzes das gesamte Beweisverfahren in einem Zug durchgeführt werden, was typischerweise nicht nur zu einer Erleichterung der Gerichtstätigkeit, sondern auch zu einer Verbilligung und Verkürzung des Verfahrens führt.

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben Amtshaftungsanspr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_6`)


Nach Zurück- bzw Abweisung seiner Begehren in erster Instanz lehnte er wiederholt Richter des Landesgerichts Leoben und des Oberlandesgerichts Graz erfolglos ab (vgl Landesgericht Leoben 2 Nc 24/11d, 2 Nc 25/11a, 2 Nc 28/11t;

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_9`)


Am 26. Februar 2013 lehnte er den Vorsitzenden des Ablehnungssenats beim Landesgericht Leoben als befangen und nach Zurückweisung dieses Antrags (2 Nc 3/13v) die Entscheidungsträger dieses Beschlusses als befangen ab.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_11`)


Diese Ablehnung wies der Ablehnungssenat beim Landesgericht Leoben (ohne Beteiligung des abgelehnten Richters) mit Beschluss vom 4. Dezember 2013, 2 Nc 31/13m, zurück.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d__5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben Amtshaftungsanspr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 42** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_109`)


Nr 18/2008 habe ein anderer Senat des Oberlandesgerichts Linz bzw das Landesgericht Salzburg die dort geregelten Pflegeaufwandsätze zuerkannt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_11`)


Seine am 4. Februar 2009 eingebrachte Oppositionsklage, deren Begehren darauf abzielt, dass der Anspruch der Beklagten aus dem Unterhaltsvergleich „sowie auf Unterhalt insgesamt“ erloschen ist, stützt derKlägerzusammengefasst auf eine Unterhaltsverwirkung iSd § 94 Abs 2 Satz 2 ABGB: Die Beklagte habe in dem gegen den Kläger geführten Strafverfahren vor dem Landesgericht Salzburg (31 Hv 139/07k), bezogen auf einen Vorfall am 3. Jänner 2006, unrichtig ausgesagt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_21`)


Unter anderem aufgrund dieses Vorfalls wurde der Kläger im Strafverfahren vor dem Landesgericht Salzburg wegen des Vergehens des Imstichlassens eines Verletzten nach § 94 StGB angeklagt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/3Ob203_11s`) (sent_id: `deanon_TRAIN/3Ob203_11s_14`)


Mit Beschluss des Landesgerichts Salzburg vom 18. Mai 2011, AZ 22 R 192/11f, 22 R 193/11b, wies das Landesgericht Salzburg die Berufung der Antragsteller mit der Begründung zurück, sie seien im Verfahren mehrfach und umfassend darüber belehrt worden, dass die von ihnen angestrebte Umbestellung der Verfahrenshelfer mangels Vorliegens der gesetzlichen Voraussetzungen nicht stattfinden könne.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/3Ob204_13s`) (sent_id: `deanon_TRAIN/3Ob204_13s_5`)


Text Begründung: Der Kläger brachte gegen den in Graz ansässigen Beklagten beim Landesgericht für Zivilrechtssachen Graz eine Schadenersatzklage über 62.769,86 EUR ein und beantragte gleichzeitig die Delegierung gemäß § 31 JN an das Landesgericht Klagenfurt.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/3Ob204_13s`) (sent_id: `deanon_TRAIN/3Ob204_13s_13`)


Gegen diese Entscheidung richtet sich der Rekurs des Klägers, mit dem er weiterhin die Delegierung an das Landesgericht Klagenfurt anstrebt.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_6`)


Mit rechtskräftigem Urteil vom 10. Mai 2007, AZ 19 Cg 136/06a, hat das Landesgericht Leoben infolge erfolgreicher Irrtumsanfechtung (im Hinblick auf die fehlende Vorschadensfreiheit des Fahrzeugs) die nunmehrige Oppositionsklägerin schuldig erkannt, an Philippa Carau Zug um Zug gegen Rückgabe des Pkw einen Betrag von 71.320 EUR sA zu bezahlen.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Philippa Carau`(person)

**Example 49** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_6`)


Text Begründung: Am 4. Oktober 2010 erließ das Landesgericht Mailand (Tribunale Ordinario di Milano) über Antrag der Betreibenden, einer Gesellschaft mit Sitz in Italien, den elektronischen Mahnbescheid (decreto ingiunitivo telematico) zur Zahl 34300/2010, mit dem der Verpflichteten, einer GmbH mit Sitz in Wien, die in Geschäftsverbindung mit der Betreibenden stand, die Zahlung von 522.094,53 EUR sA an die Betreibende innerhalb von 50 Tagen nach Bekanntmachung des Mahnbescheids aufgetragen wurde.

**False Positives:**

- `Landesgericht Mailand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_7`)


Dieser enthielt den Hinweis, dass die Verpflichtete Anspruch darauf habe, vor dem Landesgericht Mailand innerhalb von 50 Tagen nach der Bekanntmachung Einspruch zu erheben, widrigenfalls der Mahnbescheid für endgültig und vollstreckbar erklärt werde.

**False Positives:**

- `Landesgericht Mailand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_11`)


[3] Die vom Beklagten entsprechend dem Wunsch und über ausdrücklichen Auftrag der Klägerin im Mai 2017 beim Landesgericht Salzburg eingebrachte Werklohnklage gegen die in Deutschland ansässige Bauherrschaft wurde wegen fehlender internationaler Zuständigkeit zurückgewiesen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_12`)


Der Klägerin war bei Klagseinbringung bewusst, dass die Werklohnforderung gegenüber der Bauherrschaft bereits verjährt und das Landesgericht Salzburg unzuständig sein könnte.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_43`)


Vielmehr war der Klägerin bei Klagseinbringung bewusst, dass die Werklohnforderung gegenüber der Bauherrschaft bereits verjährt und das Landesgericht Salzburg unzuständig sein könnte.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation
- `Landesgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Rudigkeit Finanzen GmbH`(organisation)
- `Ing. Sascha Rohkrämer`(person)
- `Suddorftra Manufaktur GmbH`(organisation)
- `Ludmilla Nottelmann`(person)

**Example 55** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_6`)


Die Klägerin brachte beim Landesgericht Innsbruck eine Unterlassungs- und Zahlungsklage ein.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_11`)


Nach Einbringen der Klagebeantwortung beantragte sie die Delegierung an das „Landesgericht Wien“.

**False Positives:**

- `Landesgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/4Ob68_14z`) (sent_id: `deanon_TRAIN/4Ob68_14z_22`)


Einen Fortführungsantrag des Anzeigers wies das Landesgericht Innsbruck zurück und das Oberlandesgericht Innsbruck wies dessen dagegen erhobene Beschwerde ebenfalls zurück (LG Innsbruck 21 Bl 173/14w;

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_10`)


Die Streitteile hätten außerdem keine Gerichtsstandvereinbarung getroffen, weshalb das Landesgericht Klagenfurt zuständig sei.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_11`)


Der Kläger räumte daraufhin ein, dass die Forderungen gemäß § 55 JN zusammenzurechnen seien, und stellte für den Fall, dass sich das Bezirksgericht Salzburg für unzuständig erklärt, den Antrag, die Klage an das nicht offenbar unzuständige Landesgericht Salzburg zu überweisen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_12`)


Für den Fall der Unzuständigkeit dieses Landesgerichts beantragte er die Überweisung an das Landesgericht Klagenfurt, allenfalls an das Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_13`)


Das Bezirksgericht Salzburg sprach mit rechtskräftigem Beschluss vom 6. Dezember 2019 seine sachliche Unzuständigkeit aus und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Salzburg.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_14`)


Das Landesgericht Salzburg erklärte sich mit dem in der Verhandlung am 15. Jänner 2020 verkündeten Beschluss für örtlich unzuständig und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Klagenfurt.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation
- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 63** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_16`)


Mit rechtskräftigem Beschluss vom 23. Jänner 2020 wies das Landesgericht Klagenfurt die Klage wegen sachlicher Unzuständigkeit zurück, weil ein Vorbringen in der Klage, wonach die Ansprüche zusammenzurechnen seien, nicht erstattet worden sei.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_17`)


Über Antrag des Klägers hob das Landesgericht Klagenfurt die Zurückweisung der Klage mit rechtskräftigem Beschluss vom 14. Februar 2020 auf und überwies die Rechtssache dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_19`)


Das Landesgericht Klagenfurt sei an den Unzuständigkeitsbeschluss des Bezirksgerichts Salzburg betreffend die sachliche Unzuständigkeit der Bezirksgerichte gebunden und habe daher seine sachliche Unzuständigkeit, mit der Begründung ein Bezirksgericht sei zuständig, nicht mehr aussprechen können.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_24`)


Zwar haben hier das Bezirksgericht Salzburg, das Landesgericht Salzburg, das Landesgericht Klagenfurt und das Bezirksgericht Spittal an der Drau jeweils seine Zuständigkeit verneint.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation
- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 67** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_25`)


Allerdings besteht ein Streit über die Zuständigkeit iSd § 47 Abs 1 JN nur zwischen dem Landesgericht Klagenfurt und dem Bezirksgericht Spittal an der Drau.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Lovrek sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Dr. Sean Schoenenborn, gegen die beklagte Partei Dr. Hagen Kanat, vertreten durch Eisenberger & Herzog Rechtsanwalts GmbH in Graz, wegen 234.164,98 EUR sA, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, gemäß § 31 JN anstelle des Landesgerichts für Zivilrechtssachen Graz das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben, zur Verhandlung und Entscheidung dieser Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht Wiener Neustadt` — no gold match — likely missing annotation
- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Sean Schoenenborn`(person)
- `Dr. Hagen Kanat`(person)

**Example 69** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_6`)


Der Kläger beantragte die Delegation der Rechtsache an das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben.

**False Positives:**

- `Landesgericht Wiener Neustadt` — no gold match — likely missing annotation
- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 70** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Landesgericht Landesgericht Klagenfurt` — partial — gold is substring of pred: `Landesgericht Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN912691n`(business_register_number)
- `Landesgericht Klagenfurt`(organisation)
- `Holtschmidt Versicherung GmbH`(organisation)
- `LG Wels`(organisation)
- `Lohneis Pflege gesellschaft mbH`(organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich`(address)

**Example 71** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_9`)


Dagegen erhob der Ablehnungswerber Rekurs an das Landesgericht Leoben, mit dem er die Ablehnung von Richtern der Rechtsmittelsenate in Zivilrechtssachen verband.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_10`)


Gegen die im Ablehnungsverfahren vor dem Landesgericht Leoben ergangene Entscheidung (GZ 2 Nc 20/10i-3) erhob er Rekurs an das Oberlandesgericht Graz, den er mit einer Ablehnung „sämtlicher Richter des Oberlandesgerichts im Zivilrechtsberufungssenat mit Ausnahme von Dr. Florentine Fromeyer “ verband.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Florentine Fromeyer`(person)

**Example 73** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_7`)


Das Landesgericht Innsbruck eröffnete mit Beschluss vom 24.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_4`)


Text Begründung: Mit ihrer am 22. 12. 2015 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Klage begehrt die in Kagraner Anger 19, 4943 Nonsbach, Österreich (Sbg) ansässige Klägerin vom in Wien wohnhaften Beklagten die Zahlung einer Vertragsstrafe wegen mehrfacher Verstöße gegen das in seinem Agentenvertrag vereinbarte Wettbewerbsverbot.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kagraner Anger 19, 4943 Nonsbach, Österreich`(address)

**Example 75** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_14`)


Das Landesgericht Salzburg als Arbeits- und Sozialgericht sei auch mit den Rechtsangelegenheiten und regelmäßig gleichlautenden Vertragsgrundlagen und Provisions-abrechnungen der Klägerin seit Jahren vertraut.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_15`)


Auch das Landesgericht Salzburg als Arbeits- und Sozialgericht gab im Ergebnis nach Abwägung von Für und Wider eine negative Stellungnahme ab.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_18`)


Am 15. 2. 2016 übermittelte das Landesgericht Salzburg als Arbeits- und Sozialgericht im Nachhang eine von der Klägerin am 8.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_35`)


Zu bedenken ist auch, dass das Landesgericht Salzburg als Arbeits- und Sozialgericht bereits eine Tagsatzung abgehalten und das Prozessprogramm festgelegt hat und mit der Problematik auch aus einem anderen Verfahren vertraut ist, während sich ein Wiener Gericht neu in die Sache einzuarbeiten hätte.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Raiffeisen Rionalbank Hall in Tirol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8193c833`  
**Description:**
Matches the specific entity 'Raiffeisen Rionalbank Hall in Tirol'.

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

## `SüdVersand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d168562`  
**Description:**
Matches the specific entity 'SüdVersand'.

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

## `Raiffeisenbank Wels Süd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `045672f7`  
**Description:**
Matches the specific entity 'Raiffeisenbank Wels Süd'.

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

## `TraunLuftfahrt Solutions`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `410590b8`  
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

## `Mittel-Logistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `913a2c4e`  
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

## `Fensudlog GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8cf2120f`  
**Description:**
Matches the specific entity 'Fensudlog GMBH'.

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

## `Psomadakis Touristik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03c5bade`  
**Description:**
Matches the specific entity 'Psomadakis Touristik'.

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

## `Specific Compound Aktiengesellschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dbf477dc`  
**Description:**
Matches 'Kraftwerk-E‑Commerce Aktiengesellschaft' and similar full forms.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Aktiengesellschaft)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft` — partial — gold is substring of pred: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 4** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft` — partial — gold is substring of pred: `Heizung Werkuni Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 5** (doc_id: `deanon_TRAIN/4Ob13_17s`) (sent_id: `deanon_TRAIN/4Ob13_17s_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft, Inderstadt 17, 2564 Furth, Österreich, vertreten durch die Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Muran Fass, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 35.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Dezember 2016, GZ 2 R 74/16i-24, womit das Urteil des Landesgerichts Ried im Innkreis vom 25. Februar 2016, GZ 5 Cg 191/14m-14, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft` — partial — gold is substring of pred: `Daten Steinlem Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Steinlem Aktiengesellschaft`(organisation)
- `Inderstadt 17, 2564 Furth, Österreich`(address)
- `Muran Fass`(person)

**Example 6** (doc_id: `deanon_TRAIN/8ObA41_17p`) (sent_id: `deanon_TRAIN/8ObA41_17p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn als weitere Richter sowie die fachkundigen Laienrichter Dr. Ingomar Stupar und Mag. Matthias Schachner in der Arbeitsrechtssache der klagenden Partei Edgar Springob, vertreten durch Dr. Anton Tschann, Rechtsanwalt in Bludenz, gegen die beklagte Partei Zach + Merkeli Daten Aktiengesellschaft, Saggau 133, 3240 Poppendorf, Österreich, wegen Vertragsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 13. Juni 2017, GZ 15 Ra 26/17m-39, in nichtöffentlicher Sitzungden Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Merkeli Daten Aktiengesellschaft` — partial — pred is substring of gold: `Zach + Merkeli Daten Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edgar Springob`(person)
- `Zach + Merkeli Daten Aktiengesellschaft`(organisation)
- `Saggau 133, 3240 Poppendorf, Österreich`(address)

</details>

---

## `Specific Compound u. Fuhrer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d2473613`  
**Description:**
Matches 'Pfeiffenschneider u. Fuhrer Forschung AG' and similar 'u.' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+u\.\s+[A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+AG)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound GmbH 2`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `46c40acb`  
**Description:**
Matches 'Inn-Recycling Institut GMBH' and similar 'Institut' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Institut\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound GmbH 4`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0a71e1ad`  
**Description:**
Matches 'Obernöder+Küsbert Touristik GMBH' and similar '+' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Touristik\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound GmbH 5`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b2a55bb`  
**Description:**
Matches 'Kraftver-Gastronomie GMBH' and similar hyphenated patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Gastronomie\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound GmbH 6`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b1bb9235`  
**Description:**
Matches 'Gartgart Dienstleistungen GMBH' and similar 'Dienstleistungen' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Dienstleistungen\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 75 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob35_16x`) (sent_id: `deanon_TRAIN/7Ob35_16x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei NGU Energie Dienstleistungen GmbH, Noah Rübke, vertreten durch Köhler Draskovits Unger Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Franziskus Rußkamp, vertreten durch Dr. Hans Wagner, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 9. Dezember 2015, GZ 39 R 367/15g-26, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Singer als weitere Richter in der Rechtssache der klagenden Partei NGU Energie Dienstleistungen GmbH` — partial — gold is substring of pred: `NGU Energie Dienstleistungen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NGU Energie Dienstleistungen GmbH`(organisation)
- `Noah Rübke`(person)
- `Franziskus Rußkamp`(person)

</details>

---

## `Specific Compound GmbH 7`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0c5fe463`  
**Description:**
Matches 'Gogel Daten GMBH' and similar 'Daten' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Daten\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 18 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9Ob72_18f`) (sent_id: `deanon_TRAIN/9Ob72_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Beilmaier&Herpolsheimer Daten GmbH, Dipl.-Ing. Ramon Neess, vertreten durch Knirsch Gschaider & Cerha Rechtsanwälte OG in Wien, sowie des Nebenintervenienten auf Seiten der klagenden Partei Dr. Hilde Gemperl, gegen die beklagte Partei Kirci & Issakov Sicherheit GesmbH, Stowassergasse 117, 2840 Hütten, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, wegen 159.824,87 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2018, GZ 129 R 55/18h-40, mit dem der Berufung der klagenden Partei gegen das Urteil des Handelsgerichts Wien vom 6. April 2018, GZ 21 Cg 23/15s-36, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

**False Positives:**

- `Stefula in der Rechtssache der klagenden Partei Beilmaier&Herpolsheimer Daten GmbH` — partial — gold is substring of pred: `Beilmaier&Herpolsheimer Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Beilmaier&Herpolsheimer Daten GmbH`(organisation)
- `Dipl.-Ing. Ramon Neess`(person)
- `Dr. Hilde Gemperl`(person)
- `Kirci & Issakov Sicherheit GesmbH`(organisation)
- `Stowassergasse 117, 2840 Hütten, Österreich`(address)

</details>

---

## `Specific Compound GmbH 8`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `18b660ce`  
**Description:**
Matches 'Klein-Vorholt KI GMBH' and similar 'KI' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+KI\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 261 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH, Ilona Hoernle, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Wickl Logistik GmbH, Vitus Glassbrenner, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH` — partial — gold is substring of pred: `Unlandherm KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unlandherm KI GmbH`(organisation)
- `Ilona Hoernle`(person)
- `Wickl Logistik GmbH`(organisation)
- `Vitus Glassbrenner`(person)

</details>

---

## `Specific Compound GmbH 9`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5fd08af0`  
**Description:**
Matches 'Naaß Elektro GMBH' and similar 'Elektro' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Elektro\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 131 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der Schenker Elektro GmbH, FN FN119011j, wegen § 10 Abs 2 FBG, über den Revisionsrekurs des Österreichischen Verbandes Gemeinnütziger Bauvereinigungen Revisionsverband, 1010 Wien, Bösendorferstraße 7, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 3. September 2020, GZ 6 R 158/20d-6, womit der Rekurs gegen den Beschluss des Handelsgerichts Wien vom 20. Juli 2020, GZ 72 Fr 3266/20f-3, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Faber als weitere Richter in der Firmenbuchsache der Schenker Elektro GmbH` — partial — gold is substring of pred: `Schenker Elektro GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schenker Elektro GmbH`(organisation)
- `FN119011j`(business_register_number)

</details>

---

## `Specific Compound GmbH 11`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `339678e2`  
**Description:**
Matches 'Unter Heimdorf GMBH' and similar 'Heimdorf' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Heimdorf\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound GmbH 13`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9349efe7`  
**Description:**
Matches 'Kornfelder Recycling' and similar 'Recycling' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Recycling)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound GmbH 14`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `716fe16e`  
**Description:**
Matches 'DGCV E-Commerce GMBH' and similar 'E-Commerce' patterns.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+E-Commerce\s+GmbH)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Limited Company`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a77c2523`  
**Description:**
Matches companies ending in Limited.

**Content:**
```
(?<!\w)(?:^|\s|\(|\[|\"|\'|,|\.)\s*(?:Firma\s+)?([A-Z][a-zA-Z0-9+&\-\s]*(?:\s+[A-Z][a-zA-Z0-9+&\-\s]*)*\s+Limited)(?=\s|$|\)|\]|\"|\'|,|\.|;|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 262 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob192_11h`) (sent_id: `deanon_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited, London, Kapellergasse 9, 4925 Lungdorf, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited` — partial — gold is substring of pred: `Hamberg Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

</details>

---

## `Specific Organisation Wallkötter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1517df6b`  
**Description:**
Matches 'Wallkötter Finanzen GmbH'.

**Content:**
```
\bWallkötter\s+Finanzen\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Fensudwil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7d7825a3`  
**Description:**
Matches 'Fensudwil GmbH'.

**Content:**
```
\bFensudwil\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Fenseeuni`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0f978a3d`  
**Description:**
Matches 'Fenseeuni GmbH'.

**Content:**
```
\bFenseeuni\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Rudschinski`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f3a90c13`  
**Description:**
Matches 'Rudschinski Handel GmbH'.

**Content:**
```
\bRudschinski\s+Handel\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Jasensky`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6b6a23db`  
**Description:**
Matches 'Jasensky Medien GmbH'.

**Content:**
```
\bJasensky\s+Medien\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Inn-Energie`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `eca61406`  
**Description:**
Matches 'Inn-Energie GmbH'.

**Content:**
```
\bInn-Energie\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Kleinkurt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `76beaa9e`  
**Description:**
Matches 'Kleinkurt Sicherheit GmbH'.

**Content:**
```
\bKleinkurt\s+Sicherheit\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Getränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1d5f76d7`  
**Description:**
Matches 'Getränke Logwerk GmbH'.

**Content:**
```
\bGetränke\s+Logwerk\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Bergstresser`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `36c952d0`  
**Description:**
Matches 'Bergstresser Beratung GmbH'.

**Content:**
```
\bBergstresser\s+Beratung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Zormonkel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fdf4007c`  
**Description:**
Matches 'Zormonkel Telekom AG'.

**Content:**
```
\bZormonkel\s+Telekom\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Donau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4aee51a5`  
**Description:**
Matches 'Donau Furtdernex GmbH'.

**Content:**
```
\bDonau\s+Furtdernex\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation EnnsLogistik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d29c4851`  
**Description:**
Matches 'EnnsLogistik Aktiengesellschaft'.

**Content:**
```
\bEnnsLogistik\s+Aktiengesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Talmonwald`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `511a4f34`  
**Description:**
Matches 'Talmonwald-Gastronomie GmbH'.

**Content:**
```
\bTalmonwald-Gastronomie\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation Hernschier`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1be87fe8`  
**Description:**
Matches 'Hernschier Heizung AG'.

**Content:**
```
\bHernschier\s+Heizung\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Organisation MittelRobotik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e518f0ca`  
**Description:**
Matches 'MittelRobotik Betriebe GmbH'.

**Content:**
```
\bMittelRobotik\s+Betriebe\s+GmbH\b
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

