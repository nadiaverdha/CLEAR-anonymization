# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-07-22T01:28:43.410825

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris_train/Qwen_Qwen3.5-35B-A3B/organisation/2026-07-21/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 1000 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 800 |
| Validation documents | 200 |
| Test documents | 482 |
| Train sentences | 3807 |
| Validation sentences | 967 |
| Test sentences | 22062 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 200 |
| Refinement iterations | 1 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 2 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 50 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Best Batch Idx | 48 |
| Best Batch F1 | 0.9023668639053255 |
| Best Rules Serialized | [{'id': '2e7b3770', 'name': 'abbreviation_ogh', 'description': "Matches the specific abbreviation 'OGH' as a standalone entity.", 'format': 'regex', 'content': '(?i)\\bOGH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '3105645d', 'name': 'german_kg_entities', 'description': 'Matches German KG entities, ensuring hyphenated names are captured fully.', 'format': 'regex', 'content': '(?<![A-Za-zäöüß\\s/\\-])(?<!der\\s)(?<!die\\s)(?<!den\\s)(?<!im\\s)(?<!von\\s)([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+KG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '2bade35a', 'name': 'german_it_ag', 'description': "Matches specific IT company patterns like 'Hünkes IT AG' or 'Shepherd IT AG' to ensure full name capture.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+IT\\s+AG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd864d90e', 'name': 'german_software_werke', 'description': "Matches specific organization patterns like 'Software Werke' to catch entities that might be missed by generic rules.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+Software\\s+Werke\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '82171dd5', 'name': 'german_limited_entities', 'description': 'Matches German Limited entities with strict word boundaries and hyphen support.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+Limited\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '7321af99', 'name': 'german_vwgh', 'description': "Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof) as an organisation.", 'format': 'regex', 'content': '(?i)\\bVwGH\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '6e6d391c', 'name': 'swiss_organisation_sak', 'description': 'Matches Swiss compensation organizations like SAK and PVA, including full compound names.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?(?:SAK|PVA)\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '435b4dd4', 'name': 'specific_post_ag', 'description': 'Matches specific Post AG entity to prevent partial matching.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?Post\\s+AG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'fc2c8ee9', 'name': 'german_og_entities', 'description': 'Matches German OG entities requiring a valid capitalized name prefix (at least one word) and preventing matching of preceding articles/prepositions.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+OG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b179ae5e', 'name': 'german_court_names_inflected', 'description': 'Matches German court names including inflected forms, ensuring hyphenated city names like Graz-Ost and multi-word names like Innere Stadt Wien are fully captured, plus missing cities.', 'format': 'regex', 'content': '(?i)\\b(?:Oberste\\s+Gerichtshof|Oberster\\s+Gerichtshof|Obersten\\s+Gerichtshof|Oberstes\\s+Gerichtshof|Obersten\\s+Gerichtshofs|Oberste\\s+Gerichtshofs|Oberlandesgericht(?:s)?\\s+(?:Wien|Linz|Graz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Spittal\\s+an\\s+der\\s+Drau|Feldbach|Deutschlandsberg|Bruck\\s+an\\s+der\\s+Mur|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\\s+im\\s+Innkreis|Leoben|Bludenz|F\\u00fcnfh\\u00e4us|Favoriten|Hietzing|Innere\\s+Stadt\\s+Wien|Josefstadt|Laa\\s+an\\s+der\\s+Thaya|Liesing|Melk|Neusiedl\\s+am\\s+See|Schwechat|St\\.\\s+Lorenzen|St\\.\\s+P\\u00f6lten|Steyr|Telfs|V\\u00f6cklabruck|Wels|Wiener\\s+Neustadt|Korneuburg|Feldkirch|Hall\\s+in\\s+Tirol|Kufstein|M\\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\\s+an\\s+der\\s+Krems|Bad\\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\\s+im\\s+Innkreis|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\\s+an\\s+der\\s+Mur|Deutschlandsberg|Feldbach|Spittal\\s+an\\s+der\\s+Drau|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Zell\\s+am\\s+Ziller|Imst|Weiz|Kitzb\\u00fchel|Freistadt|Donaustadt|Innere\\s+Stadt\\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\\u00f6lkermarkt|G\\u00e4nserndorf|Dornbirn)|Landesgericht(?:s)?\\s+(?:f\\u00fcr\\s+(?:Strafsachen|Zivilrechtssachen|Handelssachen)?\\s+)?(?:Wien|Graz|Linz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Spittal\\s+an\\s+der\\s+Drau|Feldbach|Deutschlandsberg|Bruck\\s+an\\s+der\\s+Mur|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\\s+im\\s+Innkreis|Leoben|Bludenz|F\\u00fcnfh\\u00e4us|Favoriten|Hietzing|Innere\\s+Stadt\\s+Wien|Josefstadt|Laa\\s+an\\s+der\\s+Thaya|Liesing|Melk|Neusiedl\\s+am\\s+See|Schwechat|St\\.\\s+Lorenzen|St\\.\\s+P\\u00f6lten|Steyr|Telfs|V\\u00f6cklabruck|Wels|Wiener\\s+Neustadt|Korneuburg|Feldkirch|Hall\\s+in\\s+Tirol|Kufstein|M\\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\\s+an\\s+der\\s+Krems|Bad\\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\\s+im\\s+Innkreis|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\\s+an\\s+der\\s+Mur|Deutschlandsberg|Feldbach|Spittal\\s+an\\s+der\\s+Drau|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Salzburg|Schwechat|St\\.\\s+Lorenzen|Telfs|V\\u00f6cklabruck|Wels|Wiener\\s+Neustadt|Klagenfurt|Leoben|Ried\\s+im\\s+Innkreis|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\\s+an\\s+der\\s+Mur|Deutschlandsberg|Feldbach|Spittal\\s+an\\s+der\\s+Drau|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Zell\\s+am\\s+Ziller|Imst|Weiz|Kitzb\\u00fchel|Freistadt|Donaustadt|Innere\\s+Stadt\\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\\u00f6lkermarkt|G\\u00e4nserndorf|Dornbirn|Salzburg|St\\.\\s+P\\u00f6lten)|Bezirksgericht(?:s)?\\s+(?:f\\u00fcr\\s+(?:Strafsachen|Zivilrechtssachen|Handelssachen)?\\s+)?(?:Wien|Graz|Linz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Spittal\\s+an\\s+der\\s+Drau|Feldbach|Deutschlandsberg|Bruck\\s+an\\s+der\\s+Mur|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\\s+im\\s+Innkreis|Leoben|Bludenz|F\\u00fcnfh\\u00e4us|Favoriten|Hietzing|Innere\\s+Stadt\\s+Wien|Josefstadt|Laa\\s+an\\s+der\\s+Thaya|Liesing|Melk|Neusiedl\\s+am\\s+See|Schwechat|St\\.\\s+Lorenzen|St\\.\\s+P\\u00f6lten|Steyr|Telfs|V\\u00f6cklabruck|Wels|Wiener\\s+Neustadt|Korneuburg|Feldkirch|Hall\\s+in\\s+Tirol|Kufstein|M\\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\\s+an\\s+der\\s+Krems|Bad\\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\\s+im\\s+Innkreis|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\\s+an\\s+der\\s+Mur|Deutschlandsberg|Feldbach|Spittal\\s+an\\s+der\\s+Drau|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Schwechat|St\\.\\s+Lorenzen|Telfs|V\\u00f6cklabruck|Wels|Wiener\\s+Neustadt|Klagenfurt|Leoben|Ried\\s+im\\s+Innkreis|Krems\\s+an\\s+der\\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\\s+an\\s+der\\s+Mur|Deutschlandsberg|Feldbach|Spittal\\s+an\\s+der\\s+Drau|G\\u00fcssing|Leibnitz|F\\u00fcrstenfeld|Zell\\s+am\\s+Ziller|Imst|Weiz|Kitzb\\u00fchel|Freistadt|Donaustadt|Innere\\s+Stadt\\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\\u00f6lkermarkt|G\\u00e4nserndorf|Dornbirn|Favoriten|Graz-West)|Verfassungsgerichtshof|Verfassungsgerichtshofs)\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'e0f77f37', 'name': 'german_verfassungsgerichtshof', 'description': 'Matches Verfassungsgerichtshof and its inflected forms.', 'format': 'regex', 'content': '(?i)\\b(?:Verfassungsgerichtshof|Verfassungsgerichtshofs)\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1f4c261e', 'name': 'german_ogk', 'description': 'Matches the abbreviation ÖGK (Österreichische Gebietskrankenkasse).', 'format': 'regex', 'content': '(?i)\\bÖGK\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '917a767d', 'name': 'german_at_domain_org', 'description': "Matches German organisation names ending in .at (e.g., 'Logder.at').", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\.at\\b', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'b8676a95', 'name': 'abbreviation_obb', 'description': 'Matches the specific abbreviation ÖBB (Österreichische Bundesbahnen).', 'format': 'regex', 'content': '(?i)\\bÖBB\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'd6d5f83b', 'name': 'german_prozessfinanzierungs_ag', 'description': "Matches 'Prozessfinanzierungs AG' entities.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+Prozessfinanzierungs\\s+AG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '48a8080a', 'name': 'german_anwaltsgesellschaft_mbh', 'description': "Matches 'Anwaltsgesellschaft mbH' and 'Rechtsanwaltsgesellschaft mbH' patterns specifically.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?(?:Anwaltsgesellschaft|Rechtsanwaltsgesellschaft)\\s+mbH\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '87451718', 'name': 'german_rechtsanwaelte_gmbh', 'description': "Matches 'Rechtsanwälte GmbH' and 'Anwälte GmbH' patterns specifically with strict boundaries.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])(?:[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+(?:Rechtsanwälte|Anwälte)\\s+GmbH\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '1e582b7d', 'name': 'german_versicherungs_ag', 'description': "Matches specific 'Versicherungs AG' patterns with hyphenated names and complex prefixes.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+Versicherungs\\s+AG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '49b15449', 'name': 'german_rechtsanwaelte_kg', 'description': "Matches law firms ending in 'Rechtsanwälte KG' or 'Anwälte KG' with strict boundaries, handling slashes and hyphens in names.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+(?:Rechtsanwälte|Anwälte)\\s+KG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'cdd62ffc', 'name': 'german_gmbh_co_kg_entities', 'description': 'Matches German GmbH & Co KG entities with strict boundaries.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])(?:[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+GmbH\\s*&\\s*Co\\s*KG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'caef27cb', 'name': 'german_gesmh_co_kg', 'description': 'Matches German GesmbH & Co KG entities specifically to handle the compound suffix.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])([A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+GesmbH\\s+&\\s+Co\\s+KG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '0019616d', 'name': 'abbreviation_sovag', 'description': "Matches the specific abbreviation 'SOVAG' as an organisation.", 'format': 'regex', 'content': '(?i)\\bSOVAG\\b', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'fea2281b', 'name': 'german_ltd_entities', 'description': 'Matches German Ltd entities (e.g., Wind Glanzversyn Ltd) which were previously missed.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])(?:[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+Ltd\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '8af20562', 'name': 'german_magistrat_entities', 'description': "Matches 'Magistrat der Stadt [City]' entities, stopping strictly before administrative codes like MA 11.", 'format': 'regex', 'content': '(?i)\\bMagistrat\\s+der\\s+Stadt\\s+([A-Z][a-zA-Z\\s-]+)(?=\\s+(?:MA\\s+\\d+|Bezirk|Gasse|Straße|Platz|Nr\\.?|\\d+|\\.|,|\\s*$))', 'priority': 9, 'output_template': {'text': 'Magistrat der Stadt $1', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '40736cb6', 'name': 'german_gmbh_entities', 'description': "Matches German GmbH entities, allowing hyphens in names and handling complex prefixes like 'Anwaltsgesellschaft'.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])(?:[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+(?:Rechtsanwälte|Anwälte|Anwaltsgesellschaft|Rechtsanwaltsgesellschaft|mbH|Gesellschaft|mbH\\s*&\\s*Co\\s*KG)\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '02034379', 'name': 'german_ag_entities', 'description': 'Matches German AG entities, allowing hyphens in names and handling complex prefixes.', 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])(?:[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+(?:Aktiengesellschaft|AG)\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': '829de65e', 'name': 'german_it_gmbh_entities', 'description': "Matches specific 'IT GmbH' patterns like 'Werkkelgart IT GmbH' which were missed by generic rules.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])(?:[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+IT\\s+GmbH\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}, {'id': 'a9a3845e', 'name': 'german_rechtsanwaelte_og', 'description': "Matches law firms ending in 'Rechtsanwälte OG' or 'Anwälte OG' with strict boundaries.", 'format': 'regex', 'content': '(?i)(?<![A-Za-zäöüß\\s/\\-])(?:[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+)?[A-Z][A-Za-z0-9\\s&+\\-\\/]*\\s+(?:Rechtsanwälte|Anwälte)\\s+OG\\b', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'organisation'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 97.9% |
| True Positives | 3355 |
| False Positives | 74 |
| False Negatives | 652 |
| Total Gold Entities | 4007 |
| Micro Precision | 97.8% |
| Micro Recall | 83.7% |
| Micro F1 | 90.2% |
| Macro F1 | 90.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `abbreviation_ogh` | 22.1% | 100.0% | 12.4% | 497 | 497 | 0 |
| `german_vwgh` | 0.4% | 100.0% | 0.2% | 9 | 9 | 0 |
| `german_verfassungsgerichtshof` | 0.7% | 100.0% | 0.3% | 14 | 14 | 0 |
| `german_court_names_inflected` | 82.6% | 99.4% | 70.7% | 2851 | 2833 | 18 |
| `abbreviation_obb` | 0.4% | 69.2% | 0.2% | 13 | 9 | 4 |
| `german_gmbh_co_kg_entities` | 0.0% | 33.3% | 0.0% | 3 | 1 | 2 |
| `german_kg_entities` | 0.0% | 25.0% | 0.0% | 4 | 1 | 3 |
| `german_gmbh_entities` | 0.1% | 12.0% | 0.1% | 25 | 3 | 22 |
| `german_ag_entities` | 0.1% | 11.5% | 0.1% | 26 | 3 | 23 |
| `german_it_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_software_werke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_limited_entities` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `swiss_organisation_sak` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_post_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_og_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_ogk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_at_domain_org` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `german_prozessfinanzierungs_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_anwaltsgesellschaft_mbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_rechtsanwaelte_gmbh` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `german_versicherungs_ag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_rechtsanwaelte_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_gesmh_co_kg` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `abbreviation_sovag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_ltd_entities` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `german_magistrat_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_it_gmbh_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_rechtsanwaelte_og` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `abbreviation_ogh`

**F1:** 0.221 | **Precision:** 1.000 | **Recall:** 0.124  

**Format:** `regex`  
**Rule ID:** `2e7b3770`  
**Description:**
Matches the specific abbreviation 'OGH' as a standalone entity.

**Content:**
```
(?i)\bOGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.124 | 0.221 | 497 | 497 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 497 | 0 | 3510 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc22_25d`) (sent_id: `deanon_260716_TRAIN/10Nc22_25d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob10_16t`) (sent_id: `deanon_260716_TRAIN/10Ob10_16t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob11_18t`) (sent_id: `deanon_260716_TRAIN/10Ob11_18t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob12_22w`) (sent_id: `deanon_260716_TRAIN/10Ob12_22w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob13_20i`) (sent_id: `deanon_260716_TRAIN/10Ob13_20i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob17_24h`) (sent_id: `deanon_260716_TRAIN/10Ob17_24h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

</details>

---

## `german_verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `e0f77f37`  
**Description:**
Matches Verfassungsgerichtshof and its inflected forms.

**Content:**
```
(?i)\b(?:Verfassungsgerichtshof|Verfassungsgerichtshofs)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 14 | 14 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 0 | 3659 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_93`)


Die nach den Vorgaben des Verfassungsgerichtshofs gebotene steuerliche Entlastung des Geldunterhaltspflichtigen basiert auf dem Modell der getrennten Haushaltsführung (vgl RIS-Justiz RS0117015), in dem ein Elternteil seine Unterhaltspflicht durch Betreuungsleistungen und der andere durch Geldleistungen (allenfalls kombiniert mit anzurechnenden Naturalleistungen) erfüllt. Bei getrennter Haushaltsführung hat die Familienbeihilfe die Funktion, Betreuungsleistungen abzugelten und die steuerliche Entlastung des Geldunterhaltspflichtigen zu bewirken (RIS-Justiz RS0117015 [T20]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 1** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_147`)


3.2.6.Auch der Verfassungsgerichtshof hat sich bereits mehrfach (G 164/2014;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_152`)


Der Verfassungsgerichtshof führte allerdings aus, dass die Bestimmungen des Fern- und Auswärtsgeschäfte-Gesetzes den Vorschriften der Verbraucherrechte-RL entsprächen, welche den Mitgliedstaaten keinen Spielraum bei der Umsetzung einräumten;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_154`)


Auch von einem Vorabentscheidungsersuchen an den EuGH sah der Verfassungsgerichtshof ab (ErwG 74).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_155`)


Darüber hinaus setzte sich der Verfassungsgerichtshof in diesem Erkenntnis mit Art 14 Abs 2 der Verbraucherrechte-RL, der durch § 15 Abs 4 FAGG umgesetzt wurde, auseinander und äußerte keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz (entspricht § 15 Abs 4 letzter Satz FAGG): Der Verfassungsgerichtshof hat keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_159`)


Der Verfassungsgerichtshof kann nun nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL diesen von der Rechtsprechung des Gerichtshofes der Europäischen Union aufgestellten Kriterien im Rahmen der Verhältnismäßigkeitsprüfung eines Unionsrechtsakts widerspricht: Die Bestimmungen der Verbraucherrechte-RL verfolgen das Ziel eines umfassenden Verbraucherschutzes bei Fernabsatzverträgen und außerhalb von Geschäftsräumen geschlossenen Verträgen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_161`)


Der Verfassungsgerichtshof hat keine Zweifel, dass die in Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL normierte Rechtsfolge für den Unternehmer bei mangelnder Belehrung über das Widerrufsrecht geeignet ist, das Ziel des umfassenden Verbraucherschutzes bei Fernabsatzverträgen und bei außerhalb von Geschäftsräumen geschlossenen Verträgen zu erreichen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_162`)


Der Verfassungsgerichtshof kann auch nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL über das hinausgeht, was zur Verfolgung des mit der Regelung verfolgten Ziels des umfassenden Verbraucherschutzes erforderlich ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_165`)


Der Verfassungsgerichtshof hat sohin keine Zweifel an deren Gültigkeit.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `ÖBB` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/9ObA27_15h`) (sent_id: `deanon_260716_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `german_vwgh`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `7321af99`  
**Description:**
Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof) as an organisation.

**Content:**
```
(?i)\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 3761 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_29`)


Hingegen sind die Kosten einer rechtsfreundlichen Vertretung vom Bundesverwaltungsgericht nicht zuzusprechen (VwGH 2005/04/0257;ReisnerinHeid/Preslmayr, Vergaberecht4[2015] Rz 2034).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_44`)


Ein Antrag auf Feststellung des in einem Nachprüfungsverfahren geltend gemachten Vergaberechtsverstoßes ist nämlich nach dem Widerruf dieses Vergabeverfahrens nicht mehr möglich (VwGH 2012/04/0133).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os138_19i`) (sent_id: `deanon_260716_TRAIN/12Os138_19i_11`)


VwGH Ro 2014/03/0045).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_260716_TRAIN/12Os71_19m_12Os72_19h__10`)


VwGH Ro 2014/03/0045).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/7Ob193_21i`) (sent_id: `deanon_260716_TRAIN/7Ob193_21i_23`)


[6] 4.1 Der hier interessierende Art 9.2.3.1.1 des Rahmenvertrags entspricht § 117 Abs 4 GewO 1994 (vgl VwGH 2007/04/0198 mwN).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8Ob101_14g`) (sent_id: `deanon_260716_TRAIN/8Ob101_14g_12`)


Hinsichtlich der vom Klagebegehren betroffenen Liegenschaften hat nicht nur die Agrarbehörde über diese Frage bereits entschieden, sondern liegt auch ein letztinstanzliches Erkenntnis des Verwaltungsgerichtshofs vor (VwGH 15.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_34`)


2.2.Demgegenüber erachtetMüller(Judikaturdivergenzen zwischen VwGH und OGH? - Eine Entwarnung, ZAS 2003/22;ders, Nochmals: Kollektivvertraglicher Mindestlohn und Sachbezug in der Sozialversicherung, ASoK 2002, 220), die kollektivvertraglichen Entlohnungsbestimmungen im Ergebnis als zweiseitig zwingende Anordnung eines Barzahlungsgebots, sodass es auf einen Günstigkeitsvergleich nicht mehr ankomme.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Missed by this rule (FN):**

- `OGH` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_35`)


Diese Ansicht teilen auchLöschnigg(Entscheidungsanmerkung zu VwGH 95/08/0037, DRdA 2003, 340 f),Spitzl/Huber(inKuras[Hrsg], Handbuch Arbeitsrecht [1997] Pkt. 3.2.3.),Preiss(in ZellKomm2§ 78 GewO Rz 7),Kozak(inReissner, AngG2§ 42 Rz 34) undKarner(inMazal/Risak, Arbeitsrecht, System und Praxiskommentar [2014] Kap.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_41`)


Ob der Marktwert der vom Arbeitgeber tatsächlich gewährten Naturalbezüge im Ergebnis höher sei als der „vereinbarte Wert“, dh höher als jener Teil des Barentgelts, an dessen Stelle die Sachbezüge geleistet werden sollten, sei daher unentscheidend (VwGH vom 22. 3. 1994, 92/08/0150;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

## `german_court_names_inflected`

**F1:** 0.826 | **Precision:** 0.994 | **Recall:** 0.707  

**Format:** `regex`  
**Rule ID:** `b179ae5e`  
**Description:**
Matches German court names including inflected forms, ensuring hyphenated city names like Graz-Ost and multi-word names like Innere Stadt Wien are fully captured, plus missing cities.

**Content:**
```
(?i)\b(?:Oberste\s+Gerichtshof|Oberster\s+Gerichtshof|Obersten\s+Gerichtshof|Oberstes\s+Gerichtshof|Obersten\s+Gerichtshofs|Oberste\s+Gerichtshofs|Oberlandesgericht(?:s)?\s+(?:Wien|Linz|Graz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Spittal\s+an\s+der\s+Drau|Feldbach|Deutschlandsberg|Bruck\s+an\s+der\s+Mur|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\s+im\s+Innkreis|Leoben|Bludenz|F\u00fcnfh\u00e4us|Favoriten|Hietzing|Innere\s+Stadt\s+Wien|Josefstadt|Laa\s+an\s+der\s+Thaya|Liesing|Melk|Neusiedl\s+am\s+See|Schwechat|St\.\s+Lorenzen|St\.\s+P\u00f6lten|Steyr|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Korneuburg|Feldkirch|Hall\s+in\s+Tirol|Kufstein|M\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\s+an\s+der\s+Krems|Bad\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Zell\s+am\s+Ziller|Imst|Weiz|Kitzb\u00fchel|Freistadt|Donaustadt|Innere\s+Stadt\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\u00f6lkermarkt|G\u00e4nserndorf|Dornbirn)|Landesgericht(?:s)?\s+(?:f\u00fcr\s+(?:Strafsachen|Zivilrechtssachen|Handelssachen)?\s+)?(?:Wien|Graz|Linz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Spittal\s+an\s+der\s+Drau|Feldbach|Deutschlandsberg|Bruck\s+an\s+der\s+Mur|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\s+im\s+Innkreis|Leoben|Bludenz|F\u00fcnfh\u00e4us|Favoriten|Hietzing|Innere\s+Stadt\s+Wien|Josefstadt|Laa\s+an\s+der\s+Thaya|Liesing|Melk|Neusiedl\s+am\s+See|Schwechat|St\.\s+Lorenzen|St\.\s+P\u00f6lten|Steyr|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Korneuburg|Feldkirch|Hall\s+in\s+Tirol|Kufstein|M\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\s+an\s+der\s+Krems|Bad\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Salzburg|Schwechat|St\.\s+Lorenzen|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Zell\s+am\s+Ziller|Imst|Weiz|Kitzb\u00fchel|Freistadt|Donaustadt|Innere\s+Stadt\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\u00f6lkermarkt|G\u00e4nserndorf|Dornbirn|Salzburg|St\.\s+P\u00f6lten)|Bezirksgericht(?:s)?\s+(?:f\u00fcr\s+(?:Strafsachen|Zivilrechtssachen|Handelssachen)?\s+)?(?:Wien|Graz|Linz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Spittal\s+an\s+der\s+Drau|Feldbach|Deutschlandsberg|Bruck\s+an\s+der\s+Mur|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\s+im\s+Innkreis|Leoben|Bludenz|F\u00fcnfh\u00e4us|Favoriten|Hietzing|Innere\s+Stadt\s+Wien|Josefstadt|Laa\s+an\s+der\s+Thaya|Liesing|Melk|Neusiedl\s+am\s+See|Schwechat|St\.\s+Lorenzen|St\.\s+P\u00f6lten|Steyr|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Korneuburg|Feldkirch|Hall\s+in\s+Tirol|Kufstein|M\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\s+an\s+der\s+Krems|Bad\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Schwechat|St\.\s+Lorenzen|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Zell\s+am\s+Ziller|Imst|Weiz|Kitzb\u00fchel|Freistadt|Donaustadt|Innere\s+Stadt\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\u00f6lkermarkt|G\u00e4nserndorf|Dornbirn|Favoriten|Graz-West)|Verfassungsgerichtshof|Verfassungsgerichtshofs)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.994 | 0.707 | 0.826 | 2851 | 2833 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2833 | 18 | 1173 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Missed by this rule (FN):**

- `Jason Langeloh` (person)
- `Selma Einoeder` (person)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_8`)


[3] Mit Antrag vom 21. 2. 2025 beantragte der Kläger – noch vor der vorbereitenden Tagsatzung – die Delegierung der Rechtssache an das Bezirksgericht Dornbirn, weil nicht nur er sowie das Unternehmen, in dessen Kfz-Werkstatt das Fahrzeug repariert worden sei, und dem er im Verfahren den Streit verkündet habe, sondern auch die von ihm in großer Zahl namhaft gemachten Zeugen ihren (Wohn-)Sitz in Vorarlberg hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_9`)


Zudem befinde sich das in Rede stehende Fahrzeug im Sprengel des Bezirksgerichts Dornbirn.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_14`)


Das Erstgericht legte den Akt dem Obersten Gerichtshof unter Hinweis auf den Verfahrensstand, aber entgegen § 31 Abs 3 JN ohne eigene Stellungnahme zur Zweckmäßigkeit, zur Entscheidung über den Delegierungsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_27`)


dieser könnte auch aus dem Sprengel des Bezirksgerichts Dornbirn oder dessen näherer Umgebung gewählt werden, was die Anreisekosten für eine Befundaufnahme jedenfalls reduzieren würde.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Kordelia Meelis` (person)
- `Fatima Tengel` (person)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_23`)


2.1 Als Grundlage für eine Ordination kommt daher nur der Fall des § 28 Abs 1 Z 2 JN in Betracht, wonach die Bestimmung eines örtlich zuständigen Gerichts durch den Obersten Gerichtshof dann zulässig ist, wenn der Antragsteller seinen Wohnsitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre (RIS-Justiz RS0112108).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Verfahrenshilfesache der Antragstellerin Roberta Eikmeier, gegen den Antragsgegner Univ.-Prof. Dr. Iris Roenisch, wegen Bewilligung der Verfahrenshilfe, über den Antrag der Antragstellerin auf Delegierung der Rechtssache an das Landesgericht Korneuburg den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Rechtssache an das Landesgericht Korneuburg wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Roberta Eikmeier` (person)
- `Dr. Iris Roenisch` (person)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_4`)


Text Begründung: Die Antragstellerin richtete an das Landesgericht Linz einen Antrag auf Bewilligung der Verfahrenshilfe, weil sie gegen einen gerichtlichen Sachverständigen wegen eines in einem Pflegegeldprozess unrichtig erstatteten Gutachtens eine Schadenersatzklage auf Zahlung entgangenen Pflegegeldes und von Schmerzengeld erheben wolle.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_5`)


Das Landesgericht Linz leitete ein Verbesserungsverfahren ein.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_6`)


Die Antragstellerin beantwortete den schriftlichen Verbesserungsauftrag und beantragte die Delegierung des Verfahrens an das Landesgericht Korneuburg mit der Begründung, dass sie wegen ihrer körperlichen Behinderungen der Einladung der Richterin des Landesgerichts Linz, sie wegen offener Fragen bei Gericht aufzusuchen, nicht folgen könne.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_8`)


Das Landesgericht Linz äußerte sich zu diesem Antrag dahin, eine Delegierung könnte zweckmäßig sein, erscheine doch eine persönliche (ergänzende) Befragung der Antragstellerin zum Verfahrenshilfeantrag sinnvoll.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_6`)


Die in Wien ansässige klagende Gesellschaft nimmt die in Linz ansässige beklagte Gesellschaft beim Landesgericht Linz auf restliche Honorare für Planungsleistungen für ein Bauvorhaben in Klosterneuburg bei Wien in Anspruch.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_12`)


[3] Bereits in der Klage beantragt dieKlägerindie Delegierung der Rechtssache an das Landesgericht Korneuburg.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_29`)


Die Rechtssache weist keinen eindeutigen Schwerpunkt zum Landesgericht Korneuburg auf.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_30`)


Zwar ist das Bauvorhaben im Sprengel des Landesgerichts Korneuburg situiert.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_32`)


Damit kann nicht gesagt werden, dass die Gründe für eine Übertragung der Rechtssache vom Landesgericht Linz an das Landesgericht Korneuburg überwiegen.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgericht Judenburg` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

**False Positives:**

- `Bezirksgerichts Graz` — partial — pred is substring of gold: `Bezirksgerichts Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Jason Langeloh`(person)
- `Selma Einoeder`(person)
- `Bezirksgerichts Graz-Ost`(organisation)
- `Bezirksgericht Dornbirn`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_9`)


Nach Aufforderung im Sinn des § 252 Abs 3 ZPO benannte die Klägerin fristgerecht das Bezirksgericht Graz-Ost als das für die Durchführung des ordentlichen Verfahrens zuständige Gericht.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_11`)


[3] Vor dem Bezirksgericht Graz-Ost beantragte sie die Vorlage der Rechtssache an den Obersten Gerichtshof zur Ordination nach § 28 Abs 1 Z 3 JN sowie die Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs (ON 18).

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Obersten Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_16`)


[5] Das Bezirksgericht Graz-Ost unterbrach das Verfahren bis zur Entscheidung des Obersten Gerichtshofs, „ein örtlich zuständiges Gericht gemäß § 98 Abs 1 Z 3 JN für die Geltendmachung der Forderungen der klagenden Partei gegenüber der Beklagten aus der gegenständlichen Geschäftsbeziehung zu bestimmen“, und sprach aus, dass das Verfahren nur über Antrag der Parteien fortgesetzt werde.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_19`)


Das Bezirksgericht Graz-Ost legte den Akt dem Obersten Gerichtshof zur Entscheidung nach § 28 Abs 1 Z 3 JN vor.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_30`)


Die Rechtssache wurde an das von der Klägerin namhafte gemachte Bezirksgericht Graz-Ost überwiesen.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_33`)


[12] 2.3 Solange das Bezirksgericht Graz-Ost seine sich aus § 252 Abs 3 ZPO ergebende Zuständigkeit nicht rechtskräftig verneint hat, ist der Oberste Gerichtshof nicht zur Bestimmung eines örtlich zuständigen Gerichts nach § 28 Abs 1 Z 3 JN berufen (RS0046450;

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Oberste Gerichtshof`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Bezirksgerichts Graz` — partial — pred is substring of gold: `Bezirksgerichts Graz-West`
- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Bezirksgericht Braunau am Inn`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Obersten Gerichtshof`(organisation)

</details>

---

## `abbreviation_obb`

**F1:** 0.004 | **Precision:** 0.692 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `b8676a95`  
**Description:**
Matches the specific abbreviation ÖBB (Österreichische Bundesbahnen).

**Content:**
```
(?i)\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.692 | 0.002 | 0.004 | 13 | 9 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 4 | 2504 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `ÖBB-Holding AG` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_80`)


Auch im ÖBB-Dienstrecht der 'Allgemeinen Vertragsbedingungen für Dienstverträge bei den Österreichischen Bundesbahnen' (AVB), die als Vertragsschablone für die ÖBB-Angestellten mit einem Eintritt vor dem 01.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |
| `ÖBB` | `ÖBB` |

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_83`)


Von dieser Regelung betroffen sind rund 27.000 ÖBB-Angestellte.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_86`)


Ohne eine Neuregelung werden die betroffenen ÖBB-Angestellten (auch wenn sie bereits im Ruhestand sind) die Neufestsetzung ihres Vorrückungsstichtages begehren und die Gehaltsdifferenz der letzten 3 Jahre (Verjährungsfrist) geltend machen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 4** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_87`)


Daraus ergibt sich auch für die Zukunft eine finanzielle Belastung für die ÖBB, sowie eine höhere Belastung des Bundes aus den künftigen Ruhegenüssen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_213`)


GP 1) wird dazu ausgeführt, dass ohne Neuregelung die betroffenen ÖBB-Angestellten die Neufestsetzung ihres Vorrückungsstichtags begehren und die Gehaltsdifferenz in den letzten drei Jahren (Verjährungsfrist) geltend machen werden.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_214`)


Daraus ergebe sich eine finanzielle Belastung für die ÖBB und für den Bund.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Verfassungsgerichtshofs` (organisation)
- `Verfassungsgerichtshof` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob169_15g`) (sent_id: `deanon_260716_TRAIN/1Ob169_15g_55`)


C-417/13,ÖBB-Personenverkehr, ECLI:EU:C:2015:38, Rn 66 f).

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob99_24h`) (sent_id: `deanon_260716_TRAIN/2Ob99_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende und die Hofräte MMag. Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei ÖBB-Infrastruktur Aktiengesellschaft, Kathreinweg 48, 4572 Schalchgraben, Österreich, vertreten durch Dr. Martin Wandl und Dr. Wolfgang Krempl, Rechtsanwälte in St. Pölten, gegen die beklagten Parteien 1. Melina McNaughtan, 2. Ophelia Middelkamp, und 3. ÖkR HR Karlheinz Göttl, alle vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, wegen 54.038,42 EUR sA, über die Revisionen sämtlicher Streitteile gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. März 2024, GZ 11 R 5/24w-61, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Linz vom 28. November 2023, GZ 5 Cg 82/22m-54, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Infrastruktur Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `ÖBB-Infrastruktur Aktiengesellschaft`(organisation)
- `Kathreinweg 48, 4572 Schalchgraben, Österreich`(address)
- `Melina McNaughtan`(person)
- `Ophelia Middelkamp`(person)
- `ÖkR HR Karlheinz Göttl`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Personenverkehr AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dieter Kovacs`(person)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

**False Positives:**

- `ÖBB` — similar text (different position): `ÖBB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB`(organisation)
- `ÖBB-Holding AG`(organisation)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `german_ag_entities`

**F1:** 0.001 | **Precision:** 0.115 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `02034379`  
**Description:**
Matches German AG entities, allowing hyphens in names and handling complex prefixes.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Aktiengesellschaft|AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.115 | 0.001 | 0.001 | 26 | 3 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 23 | 3992 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_4`)


Wien Derconlex AG, Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich, vertreten durch Mag. Klemens Mayer, Mag. Stefan Herrmann Rechtsanwälte in Wien, wegen 410.325,23 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Mai 2020, GZ 30 R 106/20h-73, mit dem das Urteil des Handelsgerichts Wien vom 15. Jänner 2020, GZ 10 Cg 15/16k-69, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wien Derconlex AG` | `Wien Derconlex AG` |

**Missed by this rule (FN):**

- `Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Uniber-Verlag AG` | `Uniber-Verlag AG` |

**Missed by this rule (FN):**

- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Fenuni AG` (organisation)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)
- `Liebenwein Rechtsanwälte GmbH` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_5`)


See-Umwelt Manufaktur AG, Zosen 244, 9543 Sauboden, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `See-Umwelt Manufaktur AG` | `See-Umwelt Manufaktur AG` |

**Missed by this rule (FN):**

- `Zosen 244, 9543 Sauboden, Österreich` (address)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Antonewitz Chemie AG` — partial — pred is substring of gold: `Langhansl+Antonewitz Chemie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_52`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_10`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Griete+Leine Technik AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Leine Technik AG` — partial — pred is substring of gold: `Griete+Leine Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Griete+Leine Technik AG`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Florentin Jakobautzki, vertreten durch die Konrad Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Lischke&Rohleff Solar AG, Volkshausplatz 46, 3830 Pyhra, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 106.196,74 EUR sA und Feststellung (Streitwert 156.303,26 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Oktober 2017, GZ 129 R 24/17y-24, womit das Urteil des Handelsgerichts Wien vom 2. August 2017, GZ 10 Cg 1/16a-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohleff Solar AG` — partial — pred is substring of gold: `Lischke&Rohleff Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Florentin Jakobautzki`(person)
- `Konrad Rechtsanwälte GmbH`(organisation)
- `Lischke&Rohleff Solar AG`(organisation)
- `Volkshausplatz 46, 3830 Pyhra, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die ONTJ Textil AG an.

**False Positives:**

- `Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die ONTJ Textil AG` — partial — gold is substring of pred: `ONTJ Textil AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ONTJ Textil AG`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_33`)


Diese Gesetzeslücke sei durch eine analoge Anwendung des § 14 Abs 3 FBG auf gemeinnützige Bauvereinigungen in sämtlichen möglichen Rechtsformen (also auch in der Rechtsform einer GmbH oder AG) anzuwenden.

**False Positives:**

- `also auch in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_137`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/6Ob51_21z`) (sent_id: `deanon_260716_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Fabienne Müffler, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei See Conlemgart Gruppe Bank Schlötels&Katzenberg Digital AG, C - Obersee 27A, 4963 Nöfing, Österreich, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

**False Positives:**

- `Katzenberg Digital AG` — partial — pred is substring of gold: `Schlötels&Katzenberg Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Fabienne Müffler`(person)
- `See Conlemgart Gruppe Bank`(organisation)
- `Schlötels&Katzenberg Digital AG`(organisation)
- `C - Obersee 27A, 4963 Nöfing, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_4`)


Isabel Nestle AG, Reinsbach 186, 9131 Dolina, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2.

**False Positives:**

- `Isabel Nestle AG` — partial — gold is substring of pred: `Isabel Nestle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isabel Nestle`(person)
- `Reinsbach 186, 9131 Dolina, Österreich`(address)
- `Jank Weiler Operenyi Rechtsanwälte OG`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_12`)


Die OberSoftware AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die OberSoftware AG` — partial — gold is substring of pred: `OberSoftware AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OberSoftware AG`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_123`)


In einer weiteren Entscheidung in Zusammenhang mit Abschalteinrichtungen, der Rechtssache C-100/21,QBgegenMercedes-Benz Group AG, beantwortet der EuGH die an ihn gestellten Vorlagefragen wie folgt: „1. Art 18 Abs 1, Art 26 Abs 1 und Art 46 der Richtlinie 2007/46/EG in Verbindung mit Art 5 Abs 2 VO 715/2007/EG sind dahin auszulegen, dass sie neben allgemeinen Rechtsgütern die Einzelinteressen des individuellen Käufers eines Kraftfahrzeugs gegenüber dessen Hersteller schützen, wenn dieses Fahrzeug mit einer unzulässigen Abschalteinrichtung im Sinne von Art 5 Abs 2 dieser Verordnung ausgestattet ist.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_125`)


In seiner Entscheidungsbegründung rekapituliert der EuGH zunächst, dass ein individueller Käufer, der ein Fahrzeug erwirbt, das zur Serie eines genehmigten Fahrzeugtyps gehört und somit mit einer Übereinstimmungsbescheinigung versehen ist, vernünftiger Weise erwarten kann, dass die VO 715/2007/EG und insbesondere deren Art 5 bei diesem Fahrzeug eingehalten werden (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 81 unter Hinweis auf C-145/20,Porsche Inter Auto und Volkswagen, Rn 54).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_127`)


[34] Konkret leitet der EuGH aus den Bestimmungen über die Übereinstimmungsbescheinigung (Art 18 Abs 1 und Art 26 Abs 1 der Rahmen-RL [RL 2007/46/EG des Europäischen Parlaments und des Rates vom 5. 9. 2007 zur Schaffung eines Rahmens für die Genehmigung von Kraftfahrzeugen und Kraftfahrzeuganhängern sowie von Systemen, Bauteilen und selbstständigen technischen Einheiten für diese Fahrzeuge; künftig: RL 2007/46/EG]) ab, dass die Übereinstimmungsbescheinigung „eine unmittelbare Verbindung zwischen dem Automobilhersteller und dem individuellen Käufer eines Kraftfahrzeugs herstellt, mit der diesem gewährleistet werden soll, dass das Fahrzeug mit den maßgeblichen Rechtsvorschriften der Union übereinstimmt“ (C-100/21,QBgegenMercedes-Benz Group AG, Rn 82).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_147`)


Für diesen Schadenersatzanspruch macht der EuGH grundsätzliche Vorgaben, nämlich in dem Sinn, dass die Mitgliedstaaten in einem solchen Fall einen Schadenersatzanspruch zu Gunsten eines Käufers gegenüber dem Hersteller vorzusehen haben, wenn dem Käufer durch diese Abschalteinrichtung ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_148`)


Dabei handelt es sich um einen im nationalen Recht wurzelnden Schadenersatzanspruch, der am unionsrechtlichen Effektivitätsgrundsatz zu messen ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 93), also eine wirksame, verhältnismäßige und abschreckende Sanktion für den Verstoß darstellen muss (vgl EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 90).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`
- `QBgegenMercedes-Benz Group AG` — similar text (different position): `Benz Group AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)
- `Benz Group AG`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_149`)


Im Übrigen richten sich die Modalitäten dieses Schadenersatzanspruchs nach nationalem Recht (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 92), hier also unstrittig nach österreichischem Recht.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_151`)


Eine unionsrechtliche Vorgabe eines Schadenersatzanspruchs ist das Vorliegen eines Schadens: Der EuGH betont, dass dem Käufer eines mit einer unzulässigen Abschalteinrichtung ausgestatteten Fahrzeugs ein Schadenersatzanspruch zusteht, wenn ihm ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_153`)


Als nachteilige Folge – vor der ein Fahrzeugkäufer durch das Unionsrecht geschützt werden soll – sieht der EuGH an, dass durch die Unzulässigkeit der Abschalteinrichtung die Gültigkeit der EG-Typengenehmigung und daran anschließend die der Übereinstimmungsbescheinigung in Frage gestellt werden, was wiederum (unter anderem) zu einer Unsicherheit über die Nutzungsmöglichkeit (Anmeldung, Verkauf oder Inbetriebnahme des Fahrzeugs) und „letztlich“ zu einem Schaden führen kann (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_173`)


Ebenso wenig lässt die Feststellung erkennen, ob der Kläger die Notwendigkeit des Software-Updates und die vom EuGH angesprochene Unsicherheit über die Nutzungsmöglichkeit des Fahrzeugs (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84; vgl zu dieser Unsicherheit auch die mit der Entscheidung des EuGH vom 8.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

</details>

---

## `german_gmbh_entities`

**F1:** 0.001 | **Precision:** 0.120 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `40736cb6`  
**Description:**
Matches German GmbH entities, allowing hyphens in names and handling complex prefixes like 'Anwaltsgesellschaft'.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Rechtsanwälte|Anwälte|Anwaltsgesellschaft|Rechtsanwaltsgesellschaft|mbH|Gesellschaft|mbH\s*&\s*Co\s*KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.120 | 0.001 | 0.001 | 25 | 3 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 22 | 3946 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_4`)


MJIL Holz Consulting gesellschaft mbH, Feldbaumstraße 8c, 4892 Walligen, Österreich, 2.

| Predicted | Gold |
|---|---|
| `MJIL Holz Consulting gesellschaft mbH` | `MJIL Holz Consulting gesellschaft mbH` |

**Missed by this rule (FN):**

- `Feldbaumstraße 8c, 4892 Walligen, Österreich` (address)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_5`)


RheinIT Services -gesellschaft mbH, Torbergstraße 49, 8046 Neudorf, Österreich, 3.

| Predicted | Gold |
|---|---|
| `RheinIT Services -gesellschaft mbH` | `RheinIT Services -gesellschaft mbH` |

**Missed by this rule (FN):**

- `Torbergstraße 49, 8046 Neudorf, Österreich` (address)

**Example 2** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_6`)


Inn-Logistik gesellschaft mbH, Sanatoriumstraße 22, 4084 Ensfeld, Österreich, alle vertreten durch Dr. Nikolaus Kraft, Rechtsanwalt in Wien, wegen Unzulässigkeitserklärung einer Exekution (§ 36 EO), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 19. September 2017, GZ 47 R 281/17x-41, womit das Urteil des Bezirksgerichts Meidling vom 20. Juni 2016, GZ 5 C 1/15w-37, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Inn-Logistik gesellschaft mbH` | `Inn-Logistik gesellschaft mbH` |

**Missed by this rule (FN):**

- `Sanatoriumstraße 22, 4084 Ensfeld, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Meidling` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_5`)


Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft mit Sitz in Deutschland im Europäischen Mahnverfahren nach der Verordnung (EG) 1896/2006 des Europäischen Parlaments und des Rates vom 12.

**False Positives:**

- `Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_39`)


Die Frist sei durch Rechtsanwälte vereinbart worden, die regelmäßig Fristen zu berücksichtigen hätten, sodass diese immer darauf achteten, ob ein durch „Ziffern bestimmtes Fristende“ ein Sonntag oder anerkannter Feiertag sei.

**False Positives:**

- `Die Frist sei durch Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/17Ob19_23b`) (sent_id: `deanon_260716_TRAIN/17Ob19_23b_6`)


Die Kläger brachten gegen den Beklagten als ehemaligen Insolvenzverwalter der A. WienTalsteinwaldE‑Commerce Gesellschaft mbH eine von ihnen selbst verfasste Schadenersatzklage verbunden mit einem Antrag auf Bewilligung der Verfahrenshilfe ein.

**False Positives:**

- `Commerce Gesellschaft mbH` — partial — pred is substring of gold: `WienTalsteinwaldE‑Commerce Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WienTalsteinwaldE‑Commerce Gesellschaft mbH`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob12_16w`) (sent_id: `deanon_260716_TRAIN/1Ob12_16w_18`)


3. Die Widerbeklagte kündigte der Widerklägerin (einer Rechtsanwaltsgesellschaft) am 22. 8. 2007 das Vollmachtsverhältnis.

**False Positives:**

- `einer Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob53_25p`) (sent_id: `deanon_260716_TRAIN/1Ob53_25p_40`)


Dies lässt der Revisionswerber, der davon ausgeht, dass der Beklagte aufgrund eines Verstoßes „der Gesellschaft“ gegen ihre (insbesondere Verwahrungs-)Pflichten aus dem mit ihm abgeschlossenen Vertrag hafte, außer Acht.

**False Positives:**

- `der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_55`)


8.Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH als Bemessungsgrundlage zugrunde, sondern die Gewinnanteile des Beklagten an dieser Rechtsanwälte GmbH; zu einer allfälligen Minderung dieses Einkommens des Beklagten wurde eine Negativfeststellung getroffen, die zu seinen Lasten geht.

**False Positives:**

- `Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/4Ob226_21w`) (sent_id: `deanon_260716_TRAIN/4Ob226_21w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Schwarzenbacher als Vorsitzenden und die Hofrätinnen und Hofräte, Hon.-Prof. PD Dr. Rassi, MMag. Matzka, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei James Skrypczik, vertreten durch Mag. Dr. Stefan Rieder, Rechtsanwalt in Salzburg, gegen die beklagte Partei G-*gesellschaft mbH, Frenzelstraße 73, 8102 Thoneben, Österreich, vertreten durch Univ.-Prof. Dr. Friedrich Harrer und Dr. Iris Harrer-Hörzinger, Rechtsanwälte in Salzburg, wegen 40.070 EUR und Feststellung (Gesamtstreitwert 45.070 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. September 2021, GZ 6 R 93/21w-69, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `gesellschaft mbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `James Skrypczik`(person)
- `Frenzelstraße 73, 8102 Thoneben, Österreich`(address)
- `Oberlandesgerichts Linz`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/4Ob76_14a`) (sent_id: `deanon_260716_TRAIN/4Ob76_14a_23`)


Im Fall der Kabelweiterverbreitung ist jedenfalls die VDFS diejenige Gesellschaft, die als zur Wahrnehmung der Rechte des Berechtigten berechtigt gilt.“

**False Positives:**

- `Im Fall der Kabelweiterverbreitung ist jedenfalls die VDFS diejenige Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Savitski&Flashar Möbel GmbH, Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei Fryc+Brotzler Energie Rechtsanwälte GmbH, Lange Gasse 15, 4891 Plain, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brotzler Energie Rechtsanwälte` — partial — pred is substring of gold: `Fryc+Brotzler Energie Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Savitski&Flashar Möbel GmbH`(organisation)
- `Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich`(address)
- `Fryc+Brotzler Energie Rechtsanwälte GmbH`(organisation)
- `Lange Gasse 15, 4891 Plain, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_7`)


Sie begehrte die beklagte Rechtsanwaltsgesellschaft zu verpflichten, die Rechtsberatung und/oder Rechtsvertretung dieser GmbH in bestimmt bezeichneten Angelegenheiten zu unterlassen.

**False Positives:**

- `Sie begehrte die beklagte Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_23`)


Aber selbst wenn die Beklagte die Gesellschaft aufgrund eines aus der gleichzeitigen Vertretung der Mehrheitsgesellschafterin abgeleiteten Interessenkonflikts nicht vertreten dürfte, könnte die Klägerin als Minderheitsgesellschafterin daraus keine eigenen Unterlassungsansprüche ableiten.

**False Positives:**

- `Aber selbst wenn die Beklagte die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_27`)


Eine Schutzwirkung des Mandatsvertrags zwischen der Gesellschaft und dem Rechtsanwalt zugunsten des Minderheitsgesellschafters sei schon deswegen zu verneinen, weil es ja gerade Aufgabe des Vertreters der Gesellschaft sei, deren Interessen auch gegen konfligierende Interessen der Minderheitsgesellschafter zu verteidigen.

**False Positives:**

- `Eine Schutzwirkung des Mandatsvertrags zwischen der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_73`)


Ihre Argumentation, warum es geboten sei, § 10 Abs 1 RAO und § 10 Abs 1 RL-BA 2015 als Schutzgesetze (auch) zugunsten des (Minderheits-)Gesellschafters einer Klientin zu verstehen, sodass dieser deren Verletzung (und die sich daraus ergebende Verpflichtung zur Unterlassung der Vertretung und Beratung der Gesellschaft) selbständig durchsetzen könne, erschöpft sich im Wesentlichen in der Behauptung, dass diesen Regelungen letztlich der Schutz des Gesellschaftsinteresses zu Grunde liege, dieses Gesellschaftsinteresse aber nur gewahrt sei, wenn die Interessen aller Gesellschafter, nicht nur jene des Mehrheitsgesellschafters, berücksichtigt würden.

**False Positives:**

- `und die sich daraus ergebende Verpflichtung zur Unterlassung der Vertretung und Beratung der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_260716_TRAIN/5Ob78_13a`) (sent_id: `deanon_260716_TRAIN/5Ob78_13a_9`)


2.Nach § 89c Abs 5 Z 1 GOG idF BGBl I 2012/26 sind Rechtsanwälte und Notare - nach Maßgabe der technischen Möglichkeiten - zur Teilnahme am Elektronischen Rechtsverkehr verpflichtet.

**False Positives:**

- `c Abs 5 Z 1 GOG idF BGBl I 2012/26 sind Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob11_23w`) (sent_id: `deanon_260716_TRAIN/6Ob11_23w_11`)


Die stille Gesellschaft ist eine Personengesellschaft (6 Ob 73/05m) in Form einer reinen Innengesellschaft (RS0035024;

**False Positives:**

- `Die stille Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_260716_TRAIN/6Ob16_20a`) (sent_id: `deanon_260716_TRAIN/6Ob16_20a_9`)


Die Gesellschaft sei auf dem Gebiet der Mechanik und Elektromechanik tätig.

**False Positives:**

- `Die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_16`)


Deren Gesellschafter sind die Gesellschaft mit einer voll eingezahlten Stammeinlage von 6.033.242,30 EUR und die Conuni-Bildung GMBH mit einer voll eingezahlten Stammeinlage von 100 EUR.

**False Positives:**

- `Deren Gesellschafter sind die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Conuni-Bildung GMBH`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_28`)


Die Gesellschaft halte 99,99 % der Anteile an der Bauvereinigung;

**False Positives:**

- `Die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_40`)


Dem entsprechend sei der Firmenbuchstand bei den Gesellschaftern der Gesellschaft unrichtig, die eingetragenen Gesellschafter seien zu löschen und die ursprünglichen Gesellschafter wieder einzutragen.

**False Positives:**

- `Dem entsprechend sei der Firmenbuchstand bei den Gesellschaftern der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_69`)


Die Einholung einer Revisionsrekursbeantwortung der von den begehrten Firmenbucheintragungen ebenso betroffenen Gesellschaft (oder der Gesellschafter) ist daher nicht erforderlich.

**False Positives:**

- `Die Einholung einer Revisionsrekursbeantwortung der von den begehrten Firmenbucheintragungen ebenso betroffenen Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_82`)


Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft mit beschränkter Haftung oder der Aktiengesellschaft hat die Prüfung diesen Vorschriften zu entsprechen.

**False Positives:**

- `Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_260716_TRAIN/6Ob244_17a`) (sent_id: `deanon_260716_TRAIN/6Ob244_17a_14`)


1.1.Der Beklagte wurde zwar im Jahr 2016 wegen unrichtiger Wiedergabe der finanziellen Lage der Gesellschaft in den Jahresabschlüssen 2009/2010 und 2010/2011 nach § 122 Abs 1 Z 1 GmbHG idF vor Inkrafttreten des BGBl I 2015/112 strafrechtlich verurteilt, wobei der erstgenannte Jahresabschluss am 4.

**False Positives:**

- `Der Beklagte wurde zwar im Jahr 2016 wegen unrichtiger Wiedergabe der finanziellen Lage der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `german_it_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2bade35a`  
**Description:**
Matches specific IT company patterns like 'Hünkes IT AG' or 'Shepherd IT AG' to ensure full name capture.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+IT\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_software_werke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d864d90e`  
**Description:**
Matches specific organization patterns like 'Software Werke' to catch entities that might be missed by generic rules.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Software\s+Werke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `swiss_organisation_sak`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e6d391c`  
**Description:**
Matches Swiss compensation organizations like SAK and PVA, including full compound names.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?(?:SAK|PVA)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_post_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `435b4dd4`  
**Description:**
Matches specific Post AG entity to prevent partial matching.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?Post\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_og_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fc2c8ee9`  
**Description:**
Matches German OG entities requiring a valid capitalized name prefix (at least one word) and preventing matching of preceding articles/prepositions.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_ogk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f4c261e`  
**Description:**
Matches the abbreviation ÖGK (Österreichische Gebietskrankenkasse).

**Content:**
```
(?i)\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_prozessfinanzierungs_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d6d5f83b`  
**Description:**
Matches 'Prozessfinanzierungs AG' entities.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Prozessfinanzierungs\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_anwaltsgesellschaft_mbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `48a8080a`  
**Description:**
Matches 'Anwaltsgesellschaft mbH' and 'Rechtsanwaltsgesellschaft mbH' patterns specifically.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?(?:Anwaltsgesellschaft|Rechtsanwaltsgesellschaft)\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_versicherungs_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1e582b7d`  
**Description:**
Matches specific 'Versicherungs AG' patterns with hyphenated names and complex prefixes.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Versicherungs\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_rechtsanwaelte_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `49b15449`  
**Description:**
Matches law firms ending in 'Rechtsanwälte KG' or 'Anwälte KG' with strict boundaries, handling slashes and hyphens in names.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Rechtsanwälte|Anwälte)\s+KG\b
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

## `german_court_names_inflected`

**F1:** 0.826 | **Precision:** 0.994 | **Recall:** 0.707  

**Format:** `regex`  
**Rule ID:** `b179ae5e`  
**Description:**
Matches German court names including inflected forms, ensuring hyphenated city names like Graz-Ost and multi-word names like Innere Stadt Wien are fully captured, plus missing cities.

**Content:**
```
(?i)\b(?:Oberste\s+Gerichtshof|Oberster\s+Gerichtshof|Obersten\s+Gerichtshof|Oberstes\s+Gerichtshof|Obersten\s+Gerichtshofs|Oberste\s+Gerichtshofs|Oberlandesgericht(?:s)?\s+(?:Wien|Linz|Graz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Spittal\s+an\s+der\s+Drau|Feldbach|Deutschlandsberg|Bruck\s+an\s+der\s+Mur|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\s+im\s+Innkreis|Leoben|Bludenz|F\u00fcnfh\u00e4us|Favoriten|Hietzing|Innere\s+Stadt\s+Wien|Josefstadt|Laa\s+an\s+der\s+Thaya|Liesing|Melk|Neusiedl\s+am\s+See|Schwechat|St\.\s+Lorenzen|St\.\s+P\u00f6lten|Steyr|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Korneuburg|Feldkirch|Hall\s+in\s+Tirol|Kufstein|M\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\s+an\s+der\s+Krems|Bad\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Zell\s+am\s+Ziller|Imst|Weiz|Kitzb\u00fchel|Freistadt|Donaustadt|Innere\s+Stadt\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\u00f6lkermarkt|G\u00e4nserndorf|Dornbirn)|Landesgericht(?:s)?\s+(?:f\u00fcr\s+(?:Strafsachen|Zivilrechtssachen|Handelssachen)?\s+)?(?:Wien|Graz|Linz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Spittal\s+an\s+der\s+Drau|Feldbach|Deutschlandsberg|Bruck\s+an\s+der\s+Mur|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\s+im\s+Innkreis|Leoben|Bludenz|F\u00fcnfh\u00e4us|Favoriten|Hietzing|Innere\s+Stadt\s+Wien|Josefstadt|Laa\s+an\s+der\s+Thaya|Liesing|Melk|Neusiedl\s+am\s+See|Schwechat|St\.\s+Lorenzen|St\.\s+P\u00f6lten|Steyr|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Korneuburg|Feldkirch|Hall\s+in\s+Tirol|Kufstein|M\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\s+an\s+der\s+Krems|Bad\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Salzburg|Schwechat|St\.\s+Lorenzen|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Zell\s+am\s+Ziller|Imst|Weiz|Kitzb\u00fchel|Freistadt|Donaustadt|Innere\s+Stadt\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\u00f6lkermarkt|G\u00e4nserndorf|Dornbirn|Salzburg|St\.\s+P\u00f6lten)|Bezirksgericht(?:s)?\s+(?:f\u00fcr\s+(?:Strafsachen|Zivilrechtssachen|Handelssachen)?\s+)?(?:Wien|Graz|Linz|Innsbruck|Salzburg|Eisenstadt|Klagenfurt|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Spittal\s+an\s+der\s+Drau|Feldbach|Deutschlandsberg|Bruck\s+an\s+der\s+Mur|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Ried\s+im\s+Innkreis|Leoben|Bludenz|F\u00fcnfh\u00e4us|Favoriten|Hietzing|Innere\s+Stadt\s+Wien|Josefstadt|Laa\s+an\s+der\s+Thaya|Liesing|Melk|Neusiedl\s+am\s+See|Schwechat|St\.\s+Lorenzen|St\.\s+P\u00f6lten|Steyr|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Korneuburg|Feldkirch|Hall\s+in\s+Tirol|Kufstein|M\u00f6dling|Graz-West|Graz-Ost|Eferding|Amstetten|Kirchdorf\s+an\s+der\s+Krems|Bad\s+Ischl|Gmunden|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Schwechat|St\.\s+Lorenzen|Telfs|V\u00f6cklabruck|Wels|Wiener\s+Neustadt|Klagenfurt|Leoben|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Horn|Neulengbach|Grieskirchen|Bruck\s+an\s+der\s+Mur|Deutschlandsberg|Feldbach|Spittal\s+an\s+der\s+Drau|G\u00fcssing|Leibnitz|F\u00fcrstenfeld|Zell\s+am\s+Ziller|Imst|Weiz|Kitzb\u00fchel|Freistadt|Donaustadt|Innere\s+Stadt\s+Wien|Hernals|Villach|Bregenz|Eisenstadt|Leopoldstadt|Wels|Neunkirchen|D\u00f6bling|Floridsdorf|Mistelbach|Urfahr|Schladming|V\u00f6lkermarkt|G\u00e4nserndorf|Dornbirn|Favoriten|Graz-West)|Verfassungsgerichtshof|Verfassungsgerichtshofs)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.994 | 0.707 | 0.826 | 2851 | 2833 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2833 | 18 | 1173 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Missed by this rule (FN):**

- `Jason Langeloh` (person)
- `Selma Einoeder` (person)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_8`)


[3] Mit Antrag vom 21. 2. 2025 beantragte der Kläger – noch vor der vorbereitenden Tagsatzung – die Delegierung der Rechtssache an das Bezirksgericht Dornbirn, weil nicht nur er sowie das Unternehmen, in dessen Kfz-Werkstatt das Fahrzeug repariert worden sei, und dem er im Verfahren den Streit verkündet habe, sondern auch die von ihm in großer Zahl namhaft gemachten Zeugen ihren (Wohn-)Sitz in Vorarlberg hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_9`)


Zudem befinde sich das in Rede stehende Fahrzeug im Sprengel des Bezirksgerichts Dornbirn.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_14`)


Das Erstgericht legte den Akt dem Obersten Gerichtshof unter Hinweis auf den Verfahrensstand, aber entgegen § 31 Abs 3 JN ohne eigene Stellungnahme zur Zweckmäßigkeit, zur Entscheidung über den Delegierungsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_27`)


dieser könnte auch aus dem Sprengel des Bezirksgerichts Dornbirn oder dessen näherer Umgebung gewählt werden, was die Anreisekosten für eine Befundaufnahme jedenfalls reduzieren würde.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Kordelia Meelis` (person)
- `Fatima Tengel` (person)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_23`)


2.1 Als Grundlage für eine Ordination kommt daher nur der Fall des § 28 Abs 1 Z 2 JN in Betracht, wonach die Bestimmung eines örtlich zuständigen Gerichts durch den Obersten Gerichtshof dann zulässig ist, wenn der Antragsteller seinen Wohnsitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre (RIS-Justiz RS0112108).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Verfahrenshilfesache der Antragstellerin Roberta Eikmeier, gegen den Antragsgegner Univ.-Prof. Dr. Iris Roenisch, wegen Bewilligung der Verfahrenshilfe, über den Antrag der Antragstellerin auf Delegierung der Rechtssache an das Landesgericht Korneuburg den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Rechtssache an das Landesgericht Korneuburg wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Roberta Eikmeier` (person)
- `Dr. Iris Roenisch` (person)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_4`)


Text Begründung: Die Antragstellerin richtete an das Landesgericht Linz einen Antrag auf Bewilligung der Verfahrenshilfe, weil sie gegen einen gerichtlichen Sachverständigen wegen eines in einem Pflegegeldprozess unrichtig erstatteten Gutachtens eine Schadenersatzklage auf Zahlung entgangenen Pflegegeldes und von Schmerzengeld erheben wolle.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_5`)


Das Landesgericht Linz leitete ein Verbesserungsverfahren ein.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_6`)


Die Antragstellerin beantwortete den schriftlichen Verbesserungsauftrag und beantragte die Delegierung des Verfahrens an das Landesgericht Korneuburg mit der Begründung, dass sie wegen ihrer körperlichen Behinderungen der Einladung der Richterin des Landesgerichts Linz, sie wegen offener Fragen bei Gericht aufzusuchen, nicht folgen könne.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_8`)


Das Landesgericht Linz äußerte sich zu diesem Antrag dahin, eine Delegierung könnte zweckmäßig sein, erscheine doch eine persönliche (ergänzende) Befragung der Antragstellerin zum Verfahrenshilfeantrag sinnvoll.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_6`)


Die in Wien ansässige klagende Gesellschaft nimmt die in Linz ansässige beklagte Gesellschaft beim Landesgericht Linz auf restliche Honorare für Planungsleistungen für ein Bauvorhaben in Klosterneuburg bei Wien in Anspruch.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_12`)


[3] Bereits in der Klage beantragt dieKlägerindie Delegierung der Rechtssache an das Landesgericht Korneuburg.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_29`)


Die Rechtssache weist keinen eindeutigen Schwerpunkt zum Landesgericht Korneuburg auf.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_30`)


Zwar ist das Bauvorhaben im Sprengel des Landesgerichts Korneuburg situiert.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_32`)


Damit kann nicht gesagt werden, dass die Gründe für eine Übertragung der Rechtssache vom Landesgericht Linz an das Landesgericht Korneuburg überwiegen.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgericht Judenburg` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_8`)


Andernfalls könnte eine Verschiebung der funktionellen Zuständigkeit eintreten, weil mangels Bestätigung des Übertragungsbeschlusses durch das Rekursgericht gar keine Grundlage für die Genehmigung einer Zuständigkeitsübertragung durch den Obersten Gerichtshof bestünde (9 Nc 15/14a;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Bernadette Marsilius, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Laurentia Eißmann, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Bernadette Marsilius` (person)
- `Laurentia Eißmann` (person)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_6`)


12. 2006 zur Einführung eines Europäischen Mahnverfahrens (EuMahnVO) vor dem Bezirksgericht für Handelssachen Wien die Zahlung von Forderungen aus in den Jahren 2018 und 2019 geschlossenen Werkverträgen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht für Handelssachen Wien` | `Bezirksgericht für Handelssachen Wien` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_7`)


[2] Das Bezirksgericht für Handelssachen Wien erließ – nach Verbesserung des Antrags – den Europäischen Zahlungsbefehl, gegen den die Beklagte fristgerecht Einspruch erhob.

| Predicted | Gold |
|---|---|
| `Bezirksgericht für Handelssachen Wien` | `Bezirksgericht für Handelssachen Wien` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_10`)


Das Bezirksgericht für Handelssachen Wien überwies die Rechtssache an dieses Gericht.

| Predicted | Gold |
|---|---|
| `Bezirksgericht für Handelssachen Wien` | `Bezirksgericht für Handelssachen Wien` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_11`)


[3] Vor dem Bezirksgericht Graz-Ost beantragte sie die Vorlage der Rechtssache an den Obersten Gerichtshof zur Ordination nach § 28 Abs 1 Z 3 JN sowie die Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs (ON 18).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-Ost` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_16`)


[5] Das Bezirksgericht Graz-Ost unterbrach das Verfahren bis zur Entscheidung des Obersten Gerichtshofs, „ein örtlich zuständiges Gericht gemäß § 98 Abs 1 Z 3 JN für die Geltendmachung der Forderungen der klagenden Partei gegenüber der Beklagten aus der gegenständlichen Geschäftsbeziehung zu bestimmen“, und sprach aus, dass das Verfahren nur über Antrag der Parteien fortgesetzt werde.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-Ost` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_19`)


Das Bezirksgericht Graz-Ost legte den Akt dem Obersten Gerichtshof zur Entscheidung nach § 28 Abs 1 Z 3 JN vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-Ost` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_21`)


Die Voraussetzungen für eine Ordination durch den Obersten Gerichtshof liegen nicht vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_22`)


[8] 1.1 Für das Verfahren nach der Europäischen Mahnverfahrensverordnung ist in Österreich nach § 252 Abs 2 ZPO ausschließlich das Bezirksgericht für Handelssachen Wien zuständig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht für Handelssachen Wien` | `Bezirksgericht für Handelssachen Wien` |

**Example 40** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_33`)


[12] 2.3 Solange das Bezirksgericht Graz-Ost seine sich aus § 252 Abs 3 ZPO ergebende Zuständigkeit nicht rechtskräftig verneint hat, ist der Oberste Gerichtshof nicht zur Bestimmung eines örtlich zuständigen Gerichts nach § 28 Abs 1 Z 3 JN berufen (RS0046450;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-Ost` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_35`)


Die rechtskräftige Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs über den Ordinationsantrag ändert an diesem Ergebnis nichts.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_36`)


Wenn die internationale Zuständigkeit eines österreichischen Gerichts zu verneinen ist, weil keine wirksame Gerichtsstandsvereinbarung vorliegt, scheidet eine Ordination durch den Obersten Gerichtshof nach § 28 Abs 1 Z 3 JN jedenfalls aus.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Marlene Friss` (person)
- `WestTelekom GmbH` (organisation)
- `Rehwald 11, 4723 Fronberg, Österreich` (address)

**Example 44** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_4`)


Text Begründung: Mit ihrer erkennbar an den Obersten Gerichtshof gerichteten Eingabe vom 6.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Nc22_25d`) (sent_id: `deanon_260716_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Kassandra Pach, gegen die beklagte Partei Mag. Veronika Rimkus, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Kassandra Pach` (person)
- `Mag. Veronika Rimkus` (person)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Nc22_25d`) (sent_id: `deanon_260716_TRAIN/10Nc22_25d_5`)


Der nach eigenen Angaben keinen „festen Wohnsitz“ habende Kläger erhob vor dem Bezirksgericht Neusiedl am See eine Klage auf Feststellung, dass der Beklagte nicht berechtigt sei, Daten in eine Datenanwendung einzufügen „bzw“ dass der Beklagte für die Entfernung solcher Daten aus der Anwendung „zuständig“ sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neusiedl am See` | `Bezirksgericht Neusiedl am See` |

**Example 48** (doc_id: `deanon_260716_TRAIN/10Nc22_25d`) (sent_id: `deanon_260716_TRAIN/10Nc22_25d_6`)


[2] Das Bezirksgericht Neusiedl am See und der Beklagte äußerten sich dahingehend, dass sie die Delegierung für nicht zweckmäßig erachteten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neusiedl am See` | `Bezirksgericht Neusiedl am See` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofräte Mag. Ziegelbauer und Mag. Schober als weitere Richter in der Rechtssache der klagenden Partei Estelle Neusser, vertreten durch die Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Flora Baireuther Plc, pA Esra Roettger, Deutschland, wegen 1.624 EUR sA über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `Estelle Neusser` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Flora Baireuther` (person)
- `Esra Roettger` (person)

**Example 50** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_6`)


[2] Das von der Klägerin angerufene Bezirksgericht Schwechat wies die Klage mit rechtskräftigem Beschluss vom 19. Jänner 2022 mangels internationaler Zuständigkeit zurück.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 51** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_13`)


An die rechtskräftige Verneinung der internationalen Zuständigkeit des von der Klägerin angerufenen Bezirksgerichts Schwechat ist der Oberste Gerichtshof gebunden (RIS-Justiz RS0046568 [T5]).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Schwechat` | `Bezirksgerichts Schwechat` |
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_14`)


[6] 2. Für den Fall, dass für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts nicht gegeben oder nicht zu ermitteln sind, bestimmt § 28 Abs 1 Z 2 JN, dass der Oberste Gerichtshof aus den sachlich zuständigen Gerichten eines zu bestimmen hat, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 53** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_20`)


Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (etwa für Serbien [6 Nc 1/19b], die Vereinigten Arabischen Emirate [4 Nc 11/19h], die Ukraine [4 Nc 23/19y], Ägypten [8 Nc 18/20v] oder Mexiko [4 Nc 20/20h]; vgl im Übrigen die Bsp in RS0046148).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 54** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_35`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel;

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 55** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Missed by this rule (FN):**

- `Gerhard Lohrmann` (person)
- `10. August 1983` (date)
- `Veit Künneken` (person)
- `31. Mai 1967` (date)
- `Bezirksgerichts Feldkirchen` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 57** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 58** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 59** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_9`)


Das übertragende Gericht legte aufgrund dieser Weigerung den Akt dem Obersten Gerichtshof als gemeinsam übergeordnetem Gericht zur Entscheidung gemäß § 111 Abs 2 JN vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 60** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Selma Eichler, LLM` (person)
- `13. September` (date)
- `Bezirksgerichts Graz-West` (organisation)
- `Bezirksgericht Graz-West` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-West` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Ober-Automotive GmbH` (organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich` (address)
- `Katharina Rothschadl` (person)

**Example 63** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_15`)


Das Erstgericht wies die Klage wegen Fehlens eines inländischen Gerichtsstands und somit der österreichischen internationalen Zuständigkeit rechtskräftig zurück und legte daraufhin den Akt dem Obersten Gerichtshof zur Entscheidung über den hilfsweise gestellten Ordinationsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 64** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Pflegschaftssache des mj Andreas Wolfgang Schachenmayr, geboren am 8. Juli 2004, und der mj Herta Vanessa Steinfuhrt, geboren am 4. April 2007, wegen Übertragung der Zuständigkeit nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Die mit Beschluss des Bezirksgerichts Salzburg vom 9. 9. 2009, AZ 42 PS 56/09a, verfügte Übertragung der Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Mödling wird genehmigt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgerichts Salzburg` | `Bezirksgerichts Salzburg` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Andreas Wolfgang Schachenmayr` (person)
- `Herta Vanessa Steinfuhrt` (person)

**Example 65** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_4`)


Begründung:  Rechtliche Beurteilung Die Zuständigkeit in der früher beim Bezirksgericht Steyr und beim Bezirksgericht Mattighofen anhängig gewesenen Pflegschaftssache wurde mit Beschluss des Bezirksgerichts Salzburg vom 26.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |
| `Bezirksgerichts Salzburg` | `Bezirksgerichts Salzburg` |

**Missed by this rule (FN):**

- `Bezirksgericht Mattighofen` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_7`)


2. 2009 beim Bezirksgericht Salzburg den Antrag, ihm die (einstweilige) Obsorge über die beiden Minderjährigen zu übertragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 67** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_10`)


Die Mutter ist mit den beiden Kindern in der Folge in den Sprengel des Bezirksgerichts Mödling verzogen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |

**Example 68** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_12`)


2009 übertrug das Bezirksgericht Salzburg die Zuständigkeit zur Führung der Pflegschaftssache gemäß § 111 JN dem Bezirksgericht Mödling, weil die beiden Minderjährigen ihren Aufenthalt nunmehr im Sprengel dieses Gerichts hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 69** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_13`)


Auch die Mutter beantragte die Übertragung der Zuständigkeit an das Bezirksgericht Mödling, weil sie mit den Kindern nunmehr ihren Wohnsitz im Sprengel dieses Gerichts habe und sie dort auch vom Jugendwohlfahrtsträger betreut werde.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 70** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_14`)


Das Bezirksgericht Mödling lehnte die Übernahme der Pflegschaftssache unter Hinweis auf die noch offenen Obsorgeanträge der Eltern ab.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 71** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_16`)


Über Aufforderung des Obersten Gerichtshofs (10 Nc 19/09i) wurde die Zustellung nachgeholt. Die Parteien erhoben gegen den Übertragungsbeschluss kein Rechtsmittel, sodass nunmehr die Voraussetzungen für eine Entscheidung nach § 111 JN vorliegen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 72** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_17`)


Die Übertragung der Führung der Pflegschaftssache an das Bezirksgericht Mödling ist gerechtfertigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 73** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Dietlind Schiewick` (person)
- `23. Oktober` (date)
- `Bezirkshauptmannschaft Vöcklabruck` (organisation)
- `Gisela Akcakaya, MSc` (person)
- `Ernst Hartjens` (person)

**Example 74** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_7`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Kreutzerstraße 7, 4851 Haunolding, Österreich aufhalte (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Vöcklabruck` | `Bezirksgericht Vöcklabruck` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Kreutzerstraße 7, 4851 Haunolding, Österreich` (address)

**Example 75** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_9`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 76** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_13`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 77** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_15`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 78** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_17`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 79** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_18`)


1. 2021 bzw mit Beschluss vom 29. 1. 2021 ab, weil § 111 JN auf Verfahren in Abstammungssachen keine Anwendung finde und die Minderjährige im Zeitpunkt der Antragstellung ihren gewöhnlichen Aufenthalt nicht im Sprengel des Bezirksgerichts Josefstadt gehabt habe (ON 28).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Example 80** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_20`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 81** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 82** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 83** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_23`)


Ohne rechtskräftigen Übertragungsbeschluss nach § 111 Abs 1 JN kommt eine Entscheidung des Obersten Gerichtshofs nach § 111 Abs 2 JN nicht in Betracht (RS0047067).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 84** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_24`)


Dies gilt jedenfalls dann, wenn das für die Entscheidung über einen Rekurs gegen den Übertragungsbeschluss zuständige Gericht mit dem zur Genehmigung nach § 111 Abs 2 JN berufenen Gericht (hier der Oberste Gerichtshof) nicht ident ist (RS0047067 [T14]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 85** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)

**Example 86** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_5`)


Das von der Klägerin mit ihrer Klage angerufene Bezirksgericht Schwechat hat die internationale und örtliche Zuständigkeit rechtskräftig verneint (RIS-Justiz RS0046450).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 87** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_6`)


Rechtliche Beurteilung Nach § 28 Abs 1 Z 2 JN hat der Oberste Gerichtshof, wenn für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts im Sinne dieses Gesetzes oder einer anderen Rechtsvorschrift nicht gegeben oder nicht zu ermitteln sind, aus den sachlich zuständigen Gerichten eines zu bestimmen, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn unter anderem der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 88** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_7`)


Der Oberste Gerichtshof hat in gleich gelagerten Fällen (4 Nc 11/19h, 6 Nc 1/19b, 7 Nc 23/19w) die Ordination bewilligt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 89** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_11`)


Unter Berücksichtigung dieser Vorgaben erscheint eine Zuweisung der Sache an das Bezirksgericht Schwechat als zweckmäßig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 90** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Bezirksgerichts Kitzbühel` | `Bezirksgerichts Kitzbühel` |

**Missed by this rule (FN):**

- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Karin Ciliberto` (person)

**Example 91** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_4`)


Anstelle des Bezirksgerichts Kitzbühel wird das Bezirksgericht Mödling als zur Führung des Verlassenschaftsverfahrens zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kitzbühel` | `Bezirksgerichts Kitzbühel` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 92** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_5`)


B e g r ü n d u n g :  Rechtliche Beurteilung Der am 9. September 2009 verstorbene Erblasser hatte seinen Wohnsitz im Sprengel des Bezirksgerichts Kitzbühel.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kitzbühel` | `Bezirksgerichts Kitzbühel` |

**Example 93** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_6`)


Die nachlasszugehörigen Liegenschaften sind überwiegend im Sprengel des Bezirksgerichts Mödling situiert.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |

**Example 94** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_8`)


Die - durch einen Notar mit Kanzleisitz in Wien vertretene - Witwe und die beiden minderjährigen Kinder des Verstorbenen, für die ein Rechtsanwalt mit Kanzleisitz in Wien als Kollisionskurator bestellt wurde, halten sich nach dem von ihnen bestätigten Antragsvorbringen ebenfalls im Sprengel des Bezirksgerichts Mödling auf.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |

**Example 95** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_10`)


Im Hinblick auf die angeführten Umstände erscheint die Übertragung der Zuständigkeit an das Bezirksgericht Mödling im Sinne des § 31 Abs 1 JN zweckmäßig und geeignet, eine Verkürzung und Verbilligung des Verfahrens zu bewirken.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

**False Positives:**

- `Bezirksgerichts Graz` — partial — pred is substring of gold: `Bezirksgerichts Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Jason Langeloh`(person)
- `Selma Einoeder`(person)
- `Bezirksgerichts Graz-Ost`(organisation)
- `Bezirksgericht Dornbirn`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_9`)


Nach Aufforderung im Sinn des § 252 Abs 3 ZPO benannte die Klägerin fristgerecht das Bezirksgericht Graz-Ost als das für die Durchführung des ordentlichen Verfahrens zuständige Gericht.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_11`)


[3] Vor dem Bezirksgericht Graz-Ost beantragte sie die Vorlage der Rechtssache an den Obersten Gerichtshof zur Ordination nach § 28 Abs 1 Z 3 JN sowie die Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs (ON 18).

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Obersten Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_16`)


[5] Das Bezirksgericht Graz-Ost unterbrach das Verfahren bis zur Entscheidung des Obersten Gerichtshofs, „ein örtlich zuständiges Gericht gemäß § 98 Abs 1 Z 3 JN für die Geltendmachung der Forderungen der klagenden Partei gegenüber der Beklagten aus der gegenständlichen Geschäftsbeziehung zu bestimmen“, und sprach aus, dass das Verfahren nur über Antrag der Parteien fortgesetzt werde.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_19`)


Das Bezirksgericht Graz-Ost legte den Akt dem Obersten Gerichtshof zur Entscheidung nach § 28 Abs 1 Z 3 JN vor.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_30`)


Die Rechtssache wurde an das von der Klägerin namhafte gemachte Bezirksgericht Graz-Ost überwiesen.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_33`)


[12] 2.3 Solange das Bezirksgericht Graz-Ost seine sich aus § 252 Abs 3 ZPO ergebende Zuständigkeit nicht rechtskräftig verneint hat, ist der Oberste Gerichtshof nicht zur Bestimmung eines örtlich zuständigen Gerichts nach § 28 Abs 1 Z 3 JN berufen (RS0046450;

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-Ost`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)
- `Oberste Gerichtshof`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Bezirksgerichts Graz` — partial — pred is substring of gold: `Bezirksgerichts Graz-West`
- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Bezirksgericht Braunau am Inn`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

**False Positives:**

- `Bezirksgericht Graz` — partial — pred is substring of gold: `Bezirksgericht Graz-West`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Obersten Gerichtshof`(organisation)

</details>

---

## `abbreviation_ogh`

**F1:** 0.221 | **Precision:** 1.000 | **Recall:** 0.124  

**Format:** `regex`  
**Rule ID:** `2e7b3770`  
**Description:**
Matches the specific abbreviation 'OGH' as a standalone entity.

**Content:**
```
(?i)\bOGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.124 | 0.221 | 497 | 497 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 497 | 0 | 3510 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc13_15s`) (sent_id: `deanon_260716_TRAIN/10Nc13_15s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc22_25d`) (sent_id: `deanon_260716_TRAIN/10Nc22_25d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc24_22v`) (sent_id: `deanon_260716_TRAIN/10Nc24_22v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc2_10s`) (sent_id: `deanon_260716_TRAIN/10Nc2_10s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob10_16t`) (sent_id: `deanon_260716_TRAIN/10Ob10_16t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob11_18t`) (sent_id: `deanon_260716_TRAIN/10Ob11_18t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob12_22w`) (sent_id: `deanon_260716_TRAIN/10Ob12_22w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob13_20i`) (sent_id: `deanon_260716_TRAIN/10Ob13_20i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob17_24h`) (sent_id: `deanon_260716_TRAIN/10Ob17_24h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob20_19t`) (sent_id: `deanon_260716_TRAIN/10Ob20_19t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob3_10d`) (sent_id: `deanon_260716_TRAIN/10Ob3_10d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 55** (doc_id: `deanon_260716_TRAIN/10ObS110_10i`) (sent_id: `deanon_260716_TRAIN/10ObS110_10i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 56** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 57** (doc_id: `deanon_260716_TRAIN/11Ns22_17z`) (sent_id: `deanon_260716_TRAIN/11Ns22_17z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 58** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 59** (doc_id: `deanon_260716_TRAIN/11Os49_13k`) (sent_id: `deanon_260716_TRAIN/11Os49_13k_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 60** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 61** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 62** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 63** (doc_id: `deanon_260716_TRAIN/12Ns18_15s`) (sent_id: `deanon_260716_TRAIN/12Ns18_15s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 64** (doc_id: `deanon_260716_TRAIN/12Ns18_15s`) (sent_id: `deanon_260716_TRAIN/12Ns18_15s_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2015 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafvollzugssache des Stephan Goetzfried wegen bedingter Entlassung aus einer Freiheitsstrafe, AZ 182 BE 268/14h des Landesgerichts für Strafsachen Wien als Vollzugsgericht, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Stephan Goetzfried` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 66** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Herwig Bäseke` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Herwig Berto` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 68** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Oliver Pekarek` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 70** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Gerhard Bukowska` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/12Os107_11v`) (sent_id: `deanon_260716_TRAIN/12Os107_11v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os132_12x`) (sent_id: `deanon_260716_TRAIN/12Os132_12x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os138_19i`) (sent_id: `deanon_260716_TRAIN/12Os138_19i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os202_10p`) (sent_id: `deanon_260716_TRAIN/12Os202_10p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 80** (doc_id: `deanon_260716_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_260716_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 81** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 82** (doc_id: `deanon_260716_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_260716_TRAIN/12Os71_19m_12Os72_19h__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 83** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 84** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 85** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 86** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 87** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 88** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 89** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 90** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 91** (doc_id: `deanon_260716_TRAIN/13Os37_12h`) (sent_id: `deanon_260716_TRAIN/13Os37_12h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 92** (doc_id: `deanon_260716_TRAIN/13Os44_12p`) (sent_id: `deanon_260716_TRAIN/13Os44_12p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 93** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 94** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 95** (doc_id: `deanon_260716_TRAIN/13Os6_14b`) (sent_id: `deanon_260716_TRAIN/13Os6_14b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 96** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 97** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 98** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 99** (doc_id: `deanon_260716_TRAIN/13Os8_11t`) (sent_id: `deanon_260716_TRAIN/13Os8_11t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

</details>

---

## `german_verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `e0f77f37`  
**Description:**
Matches Verfassungsgerichtshof and its inflected forms.

**Content:**
```
(?i)\b(?:Verfassungsgerichtshof|Verfassungsgerichtshofs)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 14 | 14 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 0 | 3659 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_93`)


Die nach den Vorgaben des Verfassungsgerichtshofs gebotene steuerliche Entlastung des Geldunterhaltspflichtigen basiert auf dem Modell der getrennten Haushaltsführung (vgl RIS-Justiz RS0117015), in dem ein Elternteil seine Unterhaltspflicht durch Betreuungsleistungen und der andere durch Geldleistungen (allenfalls kombiniert mit anzurechnenden Naturalleistungen) erfüllt. Bei getrennter Haushaltsführung hat die Familienbeihilfe die Funktion, Betreuungsleistungen abzugelten und die steuerliche Entlastung des Geldunterhaltspflichtigen zu bewirken (RIS-Justiz RS0117015 [T20]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 1** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_147`)


3.2.6.Auch der Verfassungsgerichtshof hat sich bereits mehrfach (G 164/2014;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_152`)


Der Verfassungsgerichtshof führte allerdings aus, dass die Bestimmungen des Fern- und Auswärtsgeschäfte-Gesetzes den Vorschriften der Verbraucherrechte-RL entsprächen, welche den Mitgliedstaaten keinen Spielraum bei der Umsetzung einräumten;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_154`)


Auch von einem Vorabentscheidungsersuchen an den EuGH sah der Verfassungsgerichtshof ab (ErwG 74).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_155`)


Darüber hinaus setzte sich der Verfassungsgerichtshof in diesem Erkenntnis mit Art 14 Abs 2 der Verbraucherrechte-RL, der durch § 15 Abs 4 FAGG umgesetzt wurde, auseinander und äußerte keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz (entspricht § 15 Abs 4 letzter Satz FAGG): Der Verfassungsgerichtshof hat keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_159`)


Der Verfassungsgerichtshof kann nun nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL diesen von der Rechtsprechung des Gerichtshofes der Europäischen Union aufgestellten Kriterien im Rahmen der Verhältnismäßigkeitsprüfung eines Unionsrechtsakts widerspricht: Die Bestimmungen der Verbraucherrechte-RL verfolgen das Ziel eines umfassenden Verbraucherschutzes bei Fernabsatzverträgen und außerhalb von Geschäftsräumen geschlossenen Verträgen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_161`)


Der Verfassungsgerichtshof hat keine Zweifel, dass die in Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL normierte Rechtsfolge für den Unternehmer bei mangelnder Belehrung über das Widerrufsrecht geeignet ist, das Ziel des umfassenden Verbraucherschutzes bei Fernabsatzverträgen und bei außerhalb von Geschäftsräumen geschlossenen Verträgen zu erreichen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_162`)


Der Verfassungsgerichtshof kann auch nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL über das hinausgeht, was zur Verfolgung des mit der Regelung verfolgten Ziels des umfassenden Verbraucherschutzes erforderlich ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_165`)


Der Verfassungsgerichtshof hat sohin keine Zweifel an deren Gültigkeit.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `ÖBB` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/9ObA27_15h`) (sent_id: `deanon_260716_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `german_vwgh`

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `7321af99`  
**Description:**
Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof) as an organisation.

**Content:**
```
(?i)\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 3761 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_29`)


Hingegen sind die Kosten einer rechtsfreundlichen Vertretung vom Bundesverwaltungsgericht nicht zuzusprechen (VwGH 2005/04/0257;ReisnerinHeid/Preslmayr, Vergaberecht4[2015] Rz 2034).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_44`)


Ein Antrag auf Feststellung des in einem Nachprüfungsverfahren geltend gemachten Vergaberechtsverstoßes ist nämlich nach dem Widerruf dieses Vergabeverfahrens nicht mehr möglich (VwGH 2012/04/0133).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os138_19i`) (sent_id: `deanon_260716_TRAIN/12Os138_19i_11`)


VwGH Ro 2014/03/0045).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_260716_TRAIN/12Os71_19m_12Os72_19h__10`)


VwGH Ro 2014/03/0045).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/7Ob193_21i`) (sent_id: `deanon_260716_TRAIN/7Ob193_21i_23`)


[6] 4.1 Der hier interessierende Art 9.2.3.1.1 des Rahmenvertrags entspricht § 117 Abs 4 GewO 1994 (vgl VwGH 2007/04/0198 mwN).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8Ob101_14g`) (sent_id: `deanon_260716_TRAIN/8Ob101_14g_12`)


Hinsichtlich der vom Klagebegehren betroffenen Liegenschaften hat nicht nur die Agrarbehörde über diese Frage bereits entschieden, sondern liegt auch ein letztinstanzliches Erkenntnis des Verwaltungsgerichtshofs vor (VwGH 15.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_34`)


2.2.Demgegenüber erachtetMüller(Judikaturdivergenzen zwischen VwGH und OGH? - Eine Entwarnung, ZAS 2003/22;ders, Nochmals: Kollektivvertraglicher Mindestlohn und Sachbezug in der Sozialversicherung, ASoK 2002, 220), die kollektivvertraglichen Entlohnungsbestimmungen im Ergebnis als zweiseitig zwingende Anordnung eines Barzahlungsgebots, sodass es auf einen Günstigkeitsvergleich nicht mehr ankomme.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Missed by this rule (FN):**

- `OGH` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_35`)


Diese Ansicht teilen auchLöschnigg(Entscheidungsanmerkung zu VwGH 95/08/0037, DRdA 2003, 340 f),Spitzl/Huber(inKuras[Hrsg], Handbuch Arbeitsrecht [1997] Pkt. 3.2.3.),Preiss(in ZellKomm2§ 78 GewO Rz 7),Kozak(inReissner, AngG2§ 42 Rz 34) undKarner(inMazal/Risak, Arbeitsrecht, System und Praxiskommentar [2014] Kap.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_41`)


Ob der Marktwert der vom Arbeitgeber tatsächlich gewährten Naturalbezüge im Ergebnis höher sei als der „vereinbarte Wert“, dh höher als jener Teil des Barentgelts, an dessen Stelle die Sachbezüge geleistet werden sollten, sei daher unentscheidend (VwGH vom 22. 3. 1994, 92/08/0150;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

## `abbreviation_obb`

**F1:** 0.004 | **Precision:** 0.692 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `b8676a95`  
**Description:**
Matches the specific abbreviation ÖBB (Österreichische Bundesbahnen).

**Content:**
```
(?i)\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.692 | 0.002 | 0.004 | 13 | 9 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 4 | 2504 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `ÖBB-Holding AG` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_80`)


Auch im ÖBB-Dienstrecht der 'Allgemeinen Vertragsbedingungen für Dienstverträge bei den Österreichischen Bundesbahnen' (AVB), die als Vertragsschablone für die ÖBB-Angestellten mit einem Eintritt vor dem 01.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |
| `ÖBB` | `ÖBB` |

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_83`)


Von dieser Regelung betroffen sind rund 27.000 ÖBB-Angestellte.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_86`)


Ohne eine Neuregelung werden die betroffenen ÖBB-Angestellten (auch wenn sie bereits im Ruhestand sind) die Neufestsetzung ihres Vorrückungsstichtages begehren und die Gehaltsdifferenz der letzten 3 Jahre (Verjährungsfrist) geltend machen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 4** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_87`)


Daraus ergibt sich auch für die Zukunft eine finanzielle Belastung für die ÖBB, sowie eine höhere Belastung des Bundes aus den künftigen Ruhegenüssen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_213`)


GP 1) wird dazu ausgeführt, dass ohne Neuregelung die betroffenen ÖBB-Angestellten die Neufestsetzung ihres Vorrückungsstichtags begehren und die Gehaltsdifferenz in den letzten drei Jahren (Verjährungsfrist) geltend machen werden.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_214`)


Daraus ergebe sich eine finanzielle Belastung für die ÖBB und für den Bund.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Verfassungsgerichtshofs` (organisation)
- `Verfassungsgerichtshof` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob169_15g`) (sent_id: `deanon_260716_TRAIN/1Ob169_15g_55`)


C-417/13,ÖBB-Personenverkehr, ECLI:EU:C:2015:38, Rn 66 f).

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob99_24h`) (sent_id: `deanon_260716_TRAIN/2Ob99_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende und die Hofräte MMag. Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei ÖBB-Infrastruktur Aktiengesellschaft, Kathreinweg 48, 4572 Schalchgraben, Österreich, vertreten durch Dr. Martin Wandl und Dr. Wolfgang Krempl, Rechtsanwälte in St. Pölten, gegen die beklagten Parteien 1. Melina McNaughtan, 2. Ophelia Middelkamp, und 3. ÖkR HR Karlheinz Göttl, alle vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, wegen 54.038,42 EUR sA, über die Revisionen sämtlicher Streitteile gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. März 2024, GZ 11 R 5/24w-61, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Linz vom 28. November 2023, GZ 5 Cg 82/22m-54, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Infrastruktur Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `ÖBB-Infrastruktur Aktiengesellschaft`(organisation)
- `Kathreinweg 48, 4572 Schalchgraben, Österreich`(address)
- `Melina McNaughtan`(person)
- `Ophelia Middelkamp`(person)
- `ÖkR HR Karlheinz Göttl`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Personenverkehr AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dieter Kovacs`(person)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

**False Positives:**

- `ÖBB` — similar text (different position): `ÖBB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB`(organisation)
- `ÖBB-Holding AG`(organisation)

</details>

---

## `german_gmbh_entities`

**F1:** 0.001 | **Precision:** 0.120 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `40736cb6`  
**Description:**
Matches German GmbH entities, allowing hyphens in names and handling complex prefixes like 'Anwaltsgesellschaft'.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Rechtsanwälte|Anwälte|Anwaltsgesellschaft|Rechtsanwaltsgesellschaft|mbH|Gesellschaft|mbH\s*&\s*Co\s*KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.120 | 0.001 | 0.001 | 25 | 3 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 22 | 3946 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_4`)


MJIL Holz Consulting gesellschaft mbH, Feldbaumstraße 8c, 4892 Walligen, Österreich, 2.

| Predicted | Gold |
|---|---|
| `MJIL Holz Consulting gesellschaft mbH` | `MJIL Holz Consulting gesellschaft mbH` |

**Missed by this rule (FN):**

- `Feldbaumstraße 8c, 4892 Walligen, Österreich` (address)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_5`)


RheinIT Services -gesellschaft mbH, Torbergstraße 49, 8046 Neudorf, Österreich, 3.

| Predicted | Gold |
|---|---|
| `RheinIT Services -gesellschaft mbH` | `RheinIT Services -gesellschaft mbH` |

**Missed by this rule (FN):**

- `Torbergstraße 49, 8046 Neudorf, Österreich` (address)

**Example 2** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_6`)


Inn-Logistik gesellschaft mbH, Sanatoriumstraße 22, 4084 Ensfeld, Österreich, alle vertreten durch Dr. Nikolaus Kraft, Rechtsanwalt in Wien, wegen Unzulässigkeitserklärung einer Exekution (§ 36 EO), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 19. September 2017, GZ 47 R 281/17x-41, womit das Urteil des Bezirksgerichts Meidling vom 20. Juni 2016, GZ 5 C 1/15w-37, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Inn-Logistik gesellschaft mbH` | `Inn-Logistik gesellschaft mbH` |

**Missed by this rule (FN):**

- `Sanatoriumstraße 22, 4084 Ensfeld, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Meidling` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc21_21a`) (sent_id: `deanon_260716_TRAIN/10Nc21_21a_5`)


Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft mit Sitz in Deutschland im Europäischen Mahnverfahren nach der Verordnung (EG) 1896/2006 des Europäischen Parlaments und des Rates vom 12.

**False Positives:**

- `Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_39`)


Die Frist sei durch Rechtsanwälte vereinbart worden, die regelmäßig Fristen zu berücksichtigen hätten, sodass diese immer darauf achteten, ob ein durch „Ziffern bestimmtes Fristende“ ein Sonntag oder anerkannter Feiertag sei.

**False Positives:**

- `Die Frist sei durch Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/17Ob19_23b`) (sent_id: `deanon_260716_TRAIN/17Ob19_23b_6`)


Die Kläger brachten gegen den Beklagten als ehemaligen Insolvenzverwalter der A. WienTalsteinwaldE‑Commerce Gesellschaft mbH eine von ihnen selbst verfasste Schadenersatzklage verbunden mit einem Antrag auf Bewilligung der Verfahrenshilfe ein.

**False Positives:**

- `Commerce Gesellschaft mbH` — partial — pred is substring of gold: `WienTalsteinwaldE‑Commerce Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WienTalsteinwaldE‑Commerce Gesellschaft mbH`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob12_16w`) (sent_id: `deanon_260716_TRAIN/1Ob12_16w_18`)


3. Die Widerbeklagte kündigte der Widerklägerin (einer Rechtsanwaltsgesellschaft) am 22. 8. 2007 das Vollmachtsverhältnis.

**False Positives:**

- `einer Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob53_25p`) (sent_id: `deanon_260716_TRAIN/1Ob53_25p_40`)


Dies lässt der Revisionswerber, der davon ausgeht, dass der Beklagte aufgrund eines Verstoßes „der Gesellschaft“ gegen ihre (insbesondere Verwahrungs-)Pflichten aus dem mit ihm abgeschlossenen Vertrag hafte, außer Acht.

**False Positives:**

- `der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_55`)


8.Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH als Bemessungsgrundlage zugrunde, sondern die Gewinnanteile des Beklagten an dieser Rechtsanwälte GmbH; zu einer allfälligen Minderung dieses Einkommens des Beklagten wurde eine Negativfeststellung getroffen, die zu seinen Lasten geht.

**False Positives:**

- `Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/4Ob226_21w`) (sent_id: `deanon_260716_TRAIN/4Ob226_21w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Schwarzenbacher als Vorsitzenden und die Hofrätinnen und Hofräte, Hon.-Prof. PD Dr. Rassi, MMag. Matzka, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei James Skrypczik, vertreten durch Mag. Dr. Stefan Rieder, Rechtsanwalt in Salzburg, gegen die beklagte Partei G-*gesellschaft mbH, Frenzelstraße 73, 8102 Thoneben, Österreich, vertreten durch Univ.-Prof. Dr. Friedrich Harrer und Dr. Iris Harrer-Hörzinger, Rechtsanwälte in Salzburg, wegen 40.070 EUR und Feststellung (Gesamtstreitwert 45.070 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. September 2021, GZ 6 R 93/21w-69, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `gesellschaft mbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `James Skrypczik`(person)
- `Frenzelstraße 73, 8102 Thoneben, Österreich`(address)
- `Oberlandesgerichts Linz`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/4Ob76_14a`) (sent_id: `deanon_260716_TRAIN/4Ob76_14a_23`)


Im Fall der Kabelweiterverbreitung ist jedenfalls die VDFS diejenige Gesellschaft, die als zur Wahrnehmung der Rechte des Berechtigten berechtigt gilt.“

**False Positives:**

- `Im Fall der Kabelweiterverbreitung ist jedenfalls die VDFS diejenige Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Savitski&Flashar Möbel GmbH, Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei Fryc+Brotzler Energie Rechtsanwälte GmbH, Lange Gasse 15, 4891 Plain, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brotzler Energie Rechtsanwälte` — partial — pred is substring of gold: `Fryc+Brotzler Energie Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Savitski&Flashar Möbel GmbH`(organisation)
- `Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich`(address)
- `Fryc+Brotzler Energie Rechtsanwälte GmbH`(organisation)
- `Lange Gasse 15, 4891 Plain, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_7`)


Sie begehrte die beklagte Rechtsanwaltsgesellschaft zu verpflichten, die Rechtsberatung und/oder Rechtsvertretung dieser GmbH in bestimmt bezeichneten Angelegenheiten zu unterlassen.

**False Positives:**

- `Sie begehrte die beklagte Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_23`)


Aber selbst wenn die Beklagte die Gesellschaft aufgrund eines aus der gleichzeitigen Vertretung der Mehrheitsgesellschafterin abgeleiteten Interessenkonflikts nicht vertreten dürfte, könnte die Klägerin als Minderheitsgesellschafterin daraus keine eigenen Unterlassungsansprüche ableiten.

**False Positives:**

- `Aber selbst wenn die Beklagte die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_27`)


Eine Schutzwirkung des Mandatsvertrags zwischen der Gesellschaft und dem Rechtsanwalt zugunsten des Minderheitsgesellschafters sei schon deswegen zu verneinen, weil es ja gerade Aufgabe des Vertreters der Gesellschaft sei, deren Interessen auch gegen konfligierende Interessen der Minderheitsgesellschafter zu verteidigen.

**False Positives:**

- `Eine Schutzwirkung des Mandatsvertrags zwischen der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_73`)


Ihre Argumentation, warum es geboten sei, § 10 Abs 1 RAO und § 10 Abs 1 RL-BA 2015 als Schutzgesetze (auch) zugunsten des (Minderheits-)Gesellschafters einer Klientin zu verstehen, sodass dieser deren Verletzung (und die sich daraus ergebende Verpflichtung zur Unterlassung der Vertretung und Beratung der Gesellschaft) selbständig durchsetzen könne, erschöpft sich im Wesentlichen in der Behauptung, dass diesen Regelungen letztlich der Schutz des Gesellschaftsinteresses zu Grunde liege, dieses Gesellschaftsinteresse aber nur gewahrt sei, wenn die Interessen aller Gesellschafter, nicht nur jene des Mehrheitsgesellschafters, berücksichtigt würden.

**False Positives:**

- `und die sich daraus ergebende Verpflichtung zur Unterlassung der Vertretung und Beratung der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_260716_TRAIN/5Ob78_13a`) (sent_id: `deanon_260716_TRAIN/5Ob78_13a_9`)


2.Nach § 89c Abs 5 Z 1 GOG idF BGBl I 2012/26 sind Rechtsanwälte und Notare - nach Maßgabe der technischen Möglichkeiten - zur Teilnahme am Elektronischen Rechtsverkehr verpflichtet.

**False Positives:**

- `c Abs 5 Z 1 GOG idF BGBl I 2012/26 sind Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob11_23w`) (sent_id: `deanon_260716_TRAIN/6Ob11_23w_11`)


Die stille Gesellschaft ist eine Personengesellschaft (6 Ob 73/05m) in Form einer reinen Innengesellschaft (RS0035024;

**False Positives:**

- `Die stille Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_260716_TRAIN/6Ob16_20a`) (sent_id: `deanon_260716_TRAIN/6Ob16_20a_9`)


Die Gesellschaft sei auf dem Gebiet der Mechanik und Elektromechanik tätig.

**False Positives:**

- `Die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_16`)


Deren Gesellschafter sind die Gesellschaft mit einer voll eingezahlten Stammeinlage von 6.033.242,30 EUR und die Conuni-Bildung GMBH mit einer voll eingezahlten Stammeinlage von 100 EUR.

**False Positives:**

- `Deren Gesellschafter sind die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Conuni-Bildung GMBH`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_28`)


Die Gesellschaft halte 99,99 % der Anteile an der Bauvereinigung;

**False Positives:**

- `Die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_40`)


Dem entsprechend sei der Firmenbuchstand bei den Gesellschaftern der Gesellschaft unrichtig, die eingetragenen Gesellschafter seien zu löschen und die ursprünglichen Gesellschafter wieder einzutragen.

**False Positives:**

- `Dem entsprechend sei der Firmenbuchstand bei den Gesellschaftern der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_69`)


Die Einholung einer Revisionsrekursbeantwortung der von den begehrten Firmenbucheintragungen ebenso betroffenen Gesellschaft (oder der Gesellschafter) ist daher nicht erforderlich.

**False Positives:**

- `Die Einholung einer Revisionsrekursbeantwortung der von den begehrten Firmenbucheintragungen ebenso betroffenen Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_82`)


Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft mit beschränkter Haftung oder der Aktiengesellschaft hat die Prüfung diesen Vorschriften zu entsprechen.

**False Positives:**

- `Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_260716_TRAIN/6Ob244_17a`) (sent_id: `deanon_260716_TRAIN/6Ob244_17a_14`)


1.1.Der Beklagte wurde zwar im Jahr 2016 wegen unrichtiger Wiedergabe der finanziellen Lage der Gesellschaft in den Jahresabschlüssen 2009/2010 und 2010/2011 nach § 122 Abs 1 Z 1 GmbHG idF vor Inkrafttreten des BGBl I 2015/112 strafrechtlich verurteilt, wobei der erstgenannte Jahresabschluss am 4.

**False Positives:**

- `Der Beklagte wurde zwar im Jahr 2016 wegen unrichtiger Wiedergabe der finanziellen Lage der Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_ag_entities`

**F1:** 0.001 | **Precision:** 0.115 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `02034379`  
**Description:**
Matches German AG entities, allowing hyphens in names and handling complex prefixes.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Aktiengesellschaft|AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.115 | 0.001 | 0.001 | 26 | 3 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 23 | 3992 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_4`)


Wien Derconlex AG, Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich, vertreten durch Mag. Klemens Mayer, Mag. Stefan Herrmann Rechtsanwälte in Wien, wegen 410.325,23 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Mai 2020, GZ 30 R 106/20h-73, mit dem das Urteil des Handelsgerichts Wien vom 15. Jänner 2020, GZ 10 Cg 15/16k-69, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wien Derconlex AG` | `Wien Derconlex AG` |

**Missed by this rule (FN):**

- `Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Uniber-Verlag AG` | `Uniber-Verlag AG` |

**Missed by this rule (FN):**

- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Fenuni AG` (organisation)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)
- `Liebenwein Rechtsanwälte GmbH` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_5`)


See-Umwelt Manufaktur AG, Zosen 244, 9543 Sauboden, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `See-Umwelt Manufaktur AG` | `See-Umwelt Manufaktur AG` |

**Missed by this rule (FN):**

- `Zosen 244, 9543 Sauboden, Österreich` (address)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Antonewitz Chemie AG` — partial — pred is substring of gold: `Langhansl+Antonewitz Chemie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_52`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_10`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Griete+Leine Technik AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Leine Technik AG` — partial — pred is substring of gold: `Griete+Leine Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Griete+Leine Technik AG`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Florentin Jakobautzki, vertreten durch die Konrad Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Lischke&Rohleff Solar AG, Volkshausplatz 46, 3830 Pyhra, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 106.196,74 EUR sA und Feststellung (Streitwert 156.303,26 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Oktober 2017, GZ 129 R 24/17y-24, womit das Urteil des Handelsgerichts Wien vom 2. August 2017, GZ 10 Cg 1/16a-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohleff Solar AG` — partial — pred is substring of gold: `Lischke&Rohleff Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Florentin Jakobautzki`(person)
- `Konrad Rechtsanwälte GmbH`(organisation)
- `Lischke&Rohleff Solar AG`(organisation)
- `Volkshausplatz 46, 3830 Pyhra, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die ONTJ Textil AG an.

**False Positives:**

- `Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die ONTJ Textil AG` — partial — gold is substring of pred: `ONTJ Textil AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ONTJ Textil AG`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_33`)


Diese Gesetzeslücke sei durch eine analoge Anwendung des § 14 Abs 3 FBG auf gemeinnützige Bauvereinigungen in sämtlichen möglichen Rechtsformen (also auch in der Rechtsform einer GmbH oder AG) anzuwenden.

**False Positives:**

- `also auch in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_137`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/6Ob51_21z`) (sent_id: `deanon_260716_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Fabienne Müffler, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei See Conlemgart Gruppe Bank Schlötels&Katzenberg Digital AG, C - Obersee 27A, 4963 Nöfing, Österreich, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

**False Positives:**

- `Katzenberg Digital AG` — partial — pred is substring of gold: `Schlötels&Katzenberg Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Fabienne Müffler`(person)
- `See Conlemgart Gruppe Bank`(organisation)
- `Schlötels&Katzenberg Digital AG`(organisation)
- `C - Obersee 27A, 4963 Nöfing, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_4`)


Isabel Nestle AG, Reinsbach 186, 9131 Dolina, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2.

**False Positives:**

- `Isabel Nestle AG` — partial — gold is substring of pred: `Isabel Nestle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isabel Nestle`(person)
- `Reinsbach 186, 9131 Dolina, Österreich`(address)
- `Jank Weiler Operenyi Rechtsanwälte OG`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_12`)


Die OberSoftware AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die OberSoftware AG` — partial — gold is substring of pred: `OberSoftware AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OberSoftware AG`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_123`)


In einer weiteren Entscheidung in Zusammenhang mit Abschalteinrichtungen, der Rechtssache C-100/21,QBgegenMercedes-Benz Group AG, beantwortet der EuGH die an ihn gestellten Vorlagefragen wie folgt: „1. Art 18 Abs 1, Art 26 Abs 1 und Art 46 der Richtlinie 2007/46/EG in Verbindung mit Art 5 Abs 2 VO 715/2007/EG sind dahin auszulegen, dass sie neben allgemeinen Rechtsgütern die Einzelinteressen des individuellen Käufers eines Kraftfahrzeugs gegenüber dessen Hersteller schützen, wenn dieses Fahrzeug mit einer unzulässigen Abschalteinrichtung im Sinne von Art 5 Abs 2 dieser Verordnung ausgestattet ist.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_125`)


In seiner Entscheidungsbegründung rekapituliert der EuGH zunächst, dass ein individueller Käufer, der ein Fahrzeug erwirbt, das zur Serie eines genehmigten Fahrzeugtyps gehört und somit mit einer Übereinstimmungsbescheinigung versehen ist, vernünftiger Weise erwarten kann, dass die VO 715/2007/EG und insbesondere deren Art 5 bei diesem Fahrzeug eingehalten werden (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 81 unter Hinweis auf C-145/20,Porsche Inter Auto und Volkswagen, Rn 54).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_127`)


[34] Konkret leitet der EuGH aus den Bestimmungen über die Übereinstimmungsbescheinigung (Art 18 Abs 1 und Art 26 Abs 1 der Rahmen-RL [RL 2007/46/EG des Europäischen Parlaments und des Rates vom 5. 9. 2007 zur Schaffung eines Rahmens für die Genehmigung von Kraftfahrzeugen und Kraftfahrzeuganhängern sowie von Systemen, Bauteilen und selbstständigen technischen Einheiten für diese Fahrzeuge; künftig: RL 2007/46/EG]) ab, dass die Übereinstimmungsbescheinigung „eine unmittelbare Verbindung zwischen dem Automobilhersteller und dem individuellen Käufer eines Kraftfahrzeugs herstellt, mit der diesem gewährleistet werden soll, dass das Fahrzeug mit den maßgeblichen Rechtsvorschriften der Union übereinstimmt“ (C-100/21,QBgegenMercedes-Benz Group AG, Rn 82).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_147`)


Für diesen Schadenersatzanspruch macht der EuGH grundsätzliche Vorgaben, nämlich in dem Sinn, dass die Mitgliedstaaten in einem solchen Fall einen Schadenersatzanspruch zu Gunsten eines Käufers gegenüber dem Hersteller vorzusehen haben, wenn dem Käufer durch diese Abschalteinrichtung ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_148`)


Dabei handelt es sich um einen im nationalen Recht wurzelnden Schadenersatzanspruch, der am unionsrechtlichen Effektivitätsgrundsatz zu messen ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 93), also eine wirksame, verhältnismäßige und abschreckende Sanktion für den Verstoß darstellen muss (vgl EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 90).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`
- `QBgegenMercedes-Benz Group AG` — similar text (different position): `Benz Group AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)
- `Benz Group AG`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_149`)


Im Übrigen richten sich die Modalitäten dieses Schadenersatzanspruchs nach nationalem Recht (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 92), hier also unstrittig nach österreichischem Recht.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_151`)


Eine unionsrechtliche Vorgabe eines Schadenersatzanspruchs ist das Vorliegen eines Schadens: Der EuGH betont, dass dem Käufer eines mit einer unzulässigen Abschalteinrichtung ausgestatteten Fahrzeugs ein Schadenersatzanspruch zusteht, wenn ihm ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_153`)


Als nachteilige Folge – vor der ein Fahrzeugkäufer durch das Unionsrecht geschützt werden soll – sieht der EuGH an, dass durch die Unzulässigkeit der Abschalteinrichtung die Gültigkeit der EG-Typengenehmigung und daran anschließend die der Übereinstimmungsbescheinigung in Frage gestellt werden, was wiederum (unter anderem) zu einer Unsicherheit über die Nutzungsmöglichkeit (Anmeldung, Verkauf oder Inbetriebnahme des Fahrzeugs) und „letztlich“ zu einem Schaden führen kann (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_173`)


Ebenso wenig lässt die Feststellung erkennen, ob der Kläger die Notwendigkeit des Software-Updates und die vom EuGH angesprochene Unsicherheit über die Nutzungsmöglichkeit des Fahrzeugs (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84; vgl zu dieser Unsicherheit auch die mit der Entscheidung des EuGH vom 8.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — partial — gold is substring of pred: `Benz Group AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benz Group AG`(organisation)

</details>

---

## `german_gmbh_co_kg_entities`

**F1:** 0.000 | **Precision:** 0.333 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cdd62ffc`  
**Description:**
Matches German GmbH & Co KG entities with strict boundaries.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+GmbH\s*&\s*Co\s*KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.000 | 0.000 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 3661 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_4`)


Norsee Technologien GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Norsee Technologien GmbH & Co KG` | `Norsee Technologien GmbH & Co KG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/6Ob46_20p`) (sent_id: `deanon_260716_TRAIN/6Ob46_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und durch die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Hargassner sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Zlatan Voelkers, vertreten durch Dr. Farhad Paya Rechtsanwalt GmbH in Klagenfurt am Wörthersee, gegen die beklagte Partei Stolyar&Breitgam Forschung GmbH & Co KG, Zweigniederlassung Marquwardt Verlag, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 15.665 EUR sA, infolge der Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz vom 11. Dezember 2019, GZ 4 R 148/19w-29, mit dem das Urteil des Landesgerichts Klagenfurt vom 21. August 2019, GZ 50 Cg 100/17d-25, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Breitgam Forschung GmbH & Co KG` — partial — pred is substring of gold: `Stolyar&Breitgam Forschung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Zlatan Voelkers`(person)
- `Dr. Farhad Paya Rechtsanwalt GmbH`(organisation)
- `Stolyar&Breitgam Forschung GmbH & Co KG`(organisation)
- `Marquwardt Verlag`(organisation)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Obersten Gerichtshof`(organisation)

</details>

---

## `german_kg_entities`

**F1:** 0.000 | **Precision:** 0.250 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3105645d`  
**Description:**
Matches German KG entities, ensuring hyphenated names are captured fully.

**Content:**
```
(?<![A-Za-zäöüß\s/\-])(?<!der\s)(?<!die\s)(?<!den\s)(?<!im\s)(?<!von\s)([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.000 | 0.000 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 3 | 3661 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_4`)


Norsee Technologien GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Norsee Technologien GmbH & Co KG` | `Norsee Technologien GmbH & Co KG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Mesarec Medien GesmbH & Co KG` — partial — pred is substring of gold: `Hauenschildt&Mesarec Medien GesmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Berti`(person)
- `Norbert Wierich`(person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich`(address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG`(organisation)
- `Susanne Schwarzhuber`(person)
- `Donau-Transport GmbH`(organisation)
- `TraunTouristik Werke GesmbH & Co KG`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob46_20p`) (sent_id: `deanon_260716_TRAIN/6Ob46_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und durch die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Hargassner sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Zlatan Voelkers, vertreten durch Dr. Farhad Paya Rechtsanwalt GmbH in Klagenfurt am Wörthersee, gegen die beklagte Partei Stolyar&Breitgam Forschung GmbH & Co KG, Zweigniederlassung Marquwardt Verlag, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 15.665 EUR sA, infolge der Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz vom 11. Dezember 2019, GZ 4 R 148/19w-29, mit dem das Urteil des Landesgerichts Klagenfurt vom 21. August 2019, GZ 50 Cg 100/17d-25, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Breitgam Forschung GmbH & Co KG` — partial — pred is substring of gold: `Stolyar&Breitgam Forschung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Zlatan Voelkers`(person)
- `Dr. Farhad Paya Rechtsanwalt GmbH`(organisation)
- `Stolyar&Breitgam Forschung GmbH & Co KG`(organisation)
- `Marquwardt Verlag`(organisation)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Obersten Gerichtshof`(organisation)

</details>

---

## `german_it_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2bade35a`  
**Description:**
Matches specific IT company patterns like 'Hünkes IT AG' or 'Shepherd IT AG' to ensure full name capture.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+IT\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_software_werke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d864d90e`  
**Description:**
Matches specific organization patterns like 'Software Werke' to catch entities that might be missed by generic rules.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Software\s+Werke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_limited_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `82171dd5`  
**Description:**
Matches German Limited entities with strict word boundaries and hyphen support.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Limited\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 3669 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Enns-Umwelt Consulting Limited` — partial — gold is substring of pred: `Enns-Umwelt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns-Umwelt`(organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich`(address)
- `Ing. Lara Markart`(person)
- `Radel Stampf Supper Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

</details>

---

## `swiss_organisation_sak`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e6d391c`  
**Description:**
Matches Swiss compensation organizations like SAK and PVA, including full compound names.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?(?:SAK|PVA)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_post_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `435b4dd4`  
**Description:**
Matches specific Post AG entity to prevent partial matching.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?Post\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_og_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fc2c8ee9`  
**Description:**
Matches German OG entities requiring a valid capitalized name prefix (at least one word) and preventing matching of preceding articles/prepositions.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_ogk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f4c261e`  
**Description:**
Matches the abbreviation ÖGK (Österreichische Gebietskrankenkasse).

**Content:**
```
(?i)\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_at_domain_org`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `917a767d`  
**Description:**
Matches German organisation names ending in .at (e.g., 'Logder.at').

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\.at\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 1358 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/5Ob78_13a`) (sent_id: `deanon_260716_TRAIN/5Ob78_13a_6`)


1.2.Nach § 5 Abs 2 ERV 2006 hat das Bundesministerium für Justiz eine Beschreibung über die Art der Datenübermittlung, der vollständigen Datenstruktur, der zulässigen Beilagenformate, einschließlich der Regeln über die Feldinhalte und den höchstzulässigen Umfang für alle elektronischen Eingabe- und Erledigungsarten (Schnittstellenbeschreibung) auf der Website „www.edikte.justiz.gv.at“ bekannt zu machen.

**False Positives:**

- `gv.at` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/5Ob78_13a`) (sent_id: `deanon_260716_TRAIN/5Ob78_13a_21`)


http://www.edikte.justiz.gv.at/edikte/km/ kmhlp05.nsf/all/gbneu!OpenDocument) wurden „aus Gründen der Übersichtlichkeit“ (...) für die GB-Version 1.5 gegenüber der in Produktion befindlichen GB-ERV-Version 2.0v unter 4.1.2 näher aufgelistete Strukturelemente aus den Schemadateien entfernt, darunter auch die (auch bislang nicht freigeschaltet gewesene) „Folgeeingabe/Rekurs, Folgeeingabe/Zurückziehung“.

**False Positives:**

- `gv.at` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_prozessfinanzierungs_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d6d5f83b`  
**Description:**
Matches 'Prozessfinanzierungs AG' entities.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Prozessfinanzierungs\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_anwaltsgesellschaft_mbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `48a8080a`  
**Description:**
Matches 'Anwaltsgesellschaft mbH' and 'Rechtsanwaltsgesellschaft mbH' patterns specifically.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?(?:Anwaltsgesellschaft|Rechtsanwaltsgesellschaft)\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_rechtsanwaelte_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `87451718`  
**Description:**
Matches 'Rechtsanwälte GmbH' and 'Anwälte GmbH' patterns specifically with strict boundaries.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Rechtsanwälte|Anwälte)\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 2054 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_55`)


8.Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH als Bemessungsgrundlage zugrunde, sondern die Gewinnanteile des Beklagten an dieser Rechtsanwälte GmbH; zu einer allfälligen Minderung dieses Einkommens des Beklagten wurde eine Negativfeststellung getroffen, die zu seinen Lasten geht.

**False Positives:**

- `Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Savitski&Flashar Möbel GmbH, Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei Fryc+Brotzler Energie Rechtsanwälte GmbH, Lange Gasse 15, 4891 Plain, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brotzler Energie Rechtsanwälte GmbH` — partial — pred is substring of gold: `Fryc+Brotzler Energie Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Savitski&Flashar Möbel GmbH`(organisation)
- `Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich`(address)
- `Fryc+Brotzler Energie Rechtsanwälte GmbH`(organisation)
- `Lange Gasse 15, 4891 Plain, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)

</details>

---

## `german_versicherungs_ag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1e582b7d`  
**Description:**
Matches specific 'Versicherungs AG' patterns with hyphenated names and complex prefixes.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Versicherungs\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_rechtsanwaelte_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `49b15449`  
**Description:**
Matches law firms ending in 'Rechtsanwälte KG' or 'Anwälte KG' with strict boundaries, handling slashes and hyphens in names.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Rechtsanwälte|Anwälte)\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_gesmh_co_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `caef27cb`  
**Description:**
Matches German GesmbH & Co KG entities specifically to handle the compound suffix.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])([A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+GesmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 3399 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Mesarec Medien GesmbH & Co KG` — partial — pred is substring of gold: `Hauenschildt&Mesarec Medien GesmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Berti`(person)
- `Norbert Wierich`(person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich`(address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG`(organisation)
- `Susanne Schwarzhuber`(person)
- `Donau-Transport GmbH`(organisation)
- `TraunTouristik Werke GesmbH & Co KG`(organisation)

</details>

---

## `abbreviation_sovag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0019616d`  
**Description:**
Matches the specific abbreviation 'SOVAG' as an organisation.

**Content:**
```
(?i)\bSOVAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_ltd_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fea2281b`  
**Description:**
Matches German Ltd entities (e.g., Wind Glanzversyn Ltd) which were previously missed.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+Ltd\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1141 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_133`)


Die genannten Bestimmungen verstoßen daher nicht gegen die Art 16 und 17 der Grundrechtecharta (EuGH C-12/11 [Denise McDonagh/Ryanair Ltd]).

**False Positives:**

- `Denise McDonagh/Ryanair Ltd` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_magistrat_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8af20562`  
**Description:**
Matches 'Magistrat der Stadt [City]' entities, stopping strictly before administrative codes like MA 11.

**Content:**
```
(?i)\bMagistrat\s+der\s+Stadt\s+([A-Z][a-zA-Z\s-]+)(?=\s+(?:MA\s+\d+|Bezirk|Gasse|Straße|Platz|Nr\.?|\d+|\.|,|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_it_gmbh_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `829de65e`  
**Description:**
Matches specific 'IT GmbH' patterns like 'Werkkelgart IT GmbH' which were missed by generic rules.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+IT\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_rechtsanwaelte_og`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a9a3845e`  
**Description:**
Matches law firms ending in 'Rechtsanwälte OG' or 'Anwälte OG' with strict boundaries.

**Content:**
```
(?i)(?<![A-Za-zäöüß\s/\-])(?:[A-Z][A-Za-z0-9\s&+\-\/]*\s+)?[A-Z][A-Za-z0-9\s&+\-\/]*\s+(?:Rechtsanwälte|Anwälte)\s+OG\b
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

