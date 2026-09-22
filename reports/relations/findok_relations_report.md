# Relation Rule Evaluation Report (End-to-End)

Generated on: 2026-09-22T15:34:19.277640

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Documents evaluated | 12 |
| True Positives | 28 |
| False Positives | 0 |
| False Negatives | 8 |
| Total Gold Relations | 36 |
| Precision | 100.0% |
| Recall | 77.8% |
| F1 | 87.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `address_of_comma_separated` | 92.9% | 100.0% | 86.7% | 13 | 13 | 0 |
| `address_of_preposition` | 23.5% | 100.0% | 13.3% | 2 | 2 | 0 |
| `legal_representation_cue` | 100.0% | 100.0% | 100.0% | 4 | 4 | 0 |
| `svnr_in_address_context` | 33.3% | 100.0% | 20.0% | 1 | 1 | 0 |
| `tax_number_steuernummer_pre` | 100.0% | 100.0% | 100.0% | 8 | 8 | 0 |
| `account_of_ownership_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `account_of_bank_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `address_of_verb_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `address_of_list_item` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `address_of_general_comma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `birthdate_abbreviated` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `birthdate_full_form` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `birthdate_context_children` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `birthdate_parenthetical` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `birthdate_list_item` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ceo_of_handelsrechtlicher_geschäftsführer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ceo_of_geschäftsführer_der` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ceo_of_firma_geschäftsführer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ceo_of_verbunden_mit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ceo_of_contextual` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `family_relation_mother_children` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `family_relation_children_list` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `nationality_citizen_phrase` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `svnr_after_steuernummer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `svnr_directly_after_steuernummer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `svnr_with_brackets` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `svnr_following_tax_number` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_number_steuernummer_post` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_number_bescheid_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_number_einkommensteuer_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_number_exclude_svrnr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `works_for_angestellt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `works_for_beschäftigt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `works_for_tätig` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `works_for_arbeitgeber` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `works_for_nichtselbständig` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `address_of_comma_separated` 🏆

**F1:** 0.929 | **Precision:** 1.000 | **Recall:** 0.867  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `289cb605`  
**Description:**
Matches the pattern where a DEP entity (person/org) is followed by a comma and then a GOV entity (address), typical in legal headers.

**Content:**
```
(?:in der Beschwerdesache|vertreten durch)\s*<DEP>[^<]+</DEP>,\s*<GOV>[^<]+</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.867 | 0.929 | 13 | 13 | 0 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (gov_sent: `findok-manually-annotated_VALIDATE/131197.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache <DEP>person</DEP>,  <GOV>address</GOV>, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (gov_sent: `findok-manually-annotated_VALIDATE/134209.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  <DEP>person</DEP>, <GOV>address</GOV>, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149394.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache <DEP>person</DEP>,  <GOV>address</GOV>, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149394.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch <DEP>person</DEP>, <GOV>address</GOV>, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149793.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache <DEP>person</DEP>,  <GOV>address</GOV>, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149793.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch <DEP>organisation</DEP>, <GOV>address</GOV>, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149803.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache <DEP>person</DEP>,  <GOV>address</GOV>  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149676.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache <DEP>person</DEP>,  <GOV>address</GOV>, vertreten durch smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149676.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch <DEP>organisation</DEP>, <GOV>address</GOV>, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149825.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  <DEP>person</DEP>, <GOV>address</GOV>, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `address_of`  **Gold:** `address_of`

</details>

---

## `address_of_preposition` 🏆

**F1:** 0.235 | **Precision:** 1.000 | **Recall:** 0.133  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `62e59af9`  
**Description:**
Matches the pattern where the DEP entity is preceded by a preposition like 'des' or 'der' and followed by a comma and GOV entity.

**Content:**
```
(?:des|der)\s*<DEP>[^<]+</DEP>,\s*<GOV>[^<]+</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.133 | 0.235 | 2 | 2 | 0 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149395.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  <DEP>person</DEP>, <GOV>address</GOV>, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**Predicted:** `address_of`  **Gold:** `address_of`

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149647.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des <DEP>person</DEP>, <GOV>address</GOV>, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**Predicted:** `address_of`  **Gold:** `address_of`

</details>

---

## `legal_representation_cue` 🏆

**F1:** 1.000 | **Precision:** 1.000 | **Recall:** 1.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `a9ffc161`  
**Description:**
Matches the specific phrase 'vertreten durch' connecting a DEP entity (client) and a GOV entity (representative).

**Content:**
```
(?i)<DEP>\w+</DEP>.*?vertreten durch.*?<GOV>\w+</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 1.000 | 1.000 | 4 | 4 | 0 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149394.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache <DEP>person</DEP>,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch <GOV>person</GOV>, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**Predicted:** `legal_representation_of`  **Gold:** `legal_representation_of`

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149793.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache <DEP>person</DEP>,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch <GOV>organisation</GOV>, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `legal_representation_of`  **Gold:** `legal_representation_of`

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149676.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache <DEP>person</DEP>,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch <GOV>organisation</GOV>, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**Predicted:** `legal_representation_of`  **Gold:** `legal_representation_of`

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149825.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  <DEP>person</DEP>, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch <GOV>organisation</GOV>, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `legal_representation_of`  **Gold:** `legal_representation_of`

</details>

---

## `svnr_in_address_context` 🏆

**F1:** 0.333 | **Precision:** 1.000 | **Recall:** 0.200  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `160f2cbe`  
**Description:**
Matches 'SVNR' appearing in the context of an address or person description, identifying the SVNR as the social security number.

**Content:**
```
(?:<DEP>person</DEP>.*?|,\s*\d+\s+\w+.*?\d+)\s*,?\s*SVNR\s*<GOV>social_security_number</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.200 | 0.333 | 1 | 1 | 0 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (gov_sent: `findok-manually-annotated_VALIDATE/138708.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr. 5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache <DEP>person</DEP>,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR <GOV>social_security_number</GOV>  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr. 5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**Predicted:** `social_security_number_of`  **Gold:** `social_security_number_of`

</details>

---

## `tax_number_steuernummer_pre` 🏆

**F1:** 1.000 | **Precision:** 1.000 | **Recall:** 1.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `1cc8667e`  
**Description:**
Matches 'Steuernummer' immediately followed by the <GOV>tax_number</GOV> entity.

**Content:**
```
(?i)Steuernummer\s*<GOV>tax_number</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 1.000 | 1.000 | 8 | 8 | 0 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (gov_sent: `findok-manually-annotated_VALIDATE/134209.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  <DEP>person</DEP>, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer <GOV>tax_number</GOV>, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149394.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache <DEP>person</DEP>,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  <GOV>tax_number</GOV>, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149793.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache <DEP>person</DEP>,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer <GOV>tax_number</GOV>  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149803.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache <DEP>person</DEP>,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer <GOV>tax_number</GOV>, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149676.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache <DEP>person</DEP>,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp. Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  <GOV>tax_number</GOV>, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149825.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  <DEP>person</DEP>, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer <GOV>tax_number</GOV>, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149907.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  <DEP>person</DEP>, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer <GOV>tax_number</GOV>, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (gov_sent: `findok-manually-annotated_VALIDATE/149885.1_1`, dep_sent: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter <DEP>person</DEP>  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  <GOV>tax_number</GOV>  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**Predicted:** `tax_number_of`  **Gold:** `tax_number_of`

</details>

---

## `account_of_ownership_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `091d7a8a`  
**Description:**
Matches 'Kontoinhaberschaft' (account ownership) or 'Konto' followed by the <GOV> entity, indicating the account belongs to the <DEP> entity.

**Content:**
```
(?i)(?:Kontoinhaberschaft.*?betrifft|betrifft.*?Kontoinhaberschaft|Konto\s+<GOV>\w+</GOV>|<GOV>\w+</GOV>\s+bei\s+Bank|Konto\s+<GOV>\w+</GOV>)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `account_of_bank_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `2369aa37`  
**Description:**
Matches the <GOV> entity when it is immediately followed by 'bei' (at) and a bank name, indicating the account is held at that bank.

**Content:**
```
(?i)<GOV>\w+</GOV>\s+bei\s+[A-Z][a-zA-Z\s]+(?:Bank|Bankstelle)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `address_of_verb_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `04028853`  
**Description:**
Matches the pattern where the DEP entity is followed by a comma and GOV entity, specifically looking for the verb 'vertreten' or 'in der' to ensure context.

**Content:**
```
(?:in der|vertreten durch)\s*<DEP>[^<]+</DEP>,\s*<GOV>[^<]+</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `address_of_list_item` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `c800e44b`  
**Description:**
Matches the pattern found in list items where a DEP entity is followed by a comma and GOV entity, often preceded by a number or bullet.

**Content:**
```
(?:\d+\.\s*|\u2022\s*)<DEP>[^<]+</DEP>,\s*<GOV>[^<]+</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `address_of_general_comma` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `8f524771`  
**Description:**
A broader rule matching any DEP followed by a comma and GOV, used as a fallback if specific context words are missing but the structure is clear.

**Content:**
```
<DEP>[^<]+</DEP>,\s*<GOV>[^<]+</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `birthdate_abbreviated` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `3e45fba8`  
**Description:**
Matches 'geb.' or 'geb. am' immediately following a person entity and preceding a date entity.

**Content:**
```
(?:<DEP>person</DEP>),?\s*geb\.?(?:\s*am)?\s*<GOV>date</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `birthdate_full_form` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `9bd7af35`  
**Description:**
Matches the full word 'geboren am' connecting the person and date entities.

**Content:**
```
(?:<DEP>person</DEP>),?\s*geboren\s*am\s*<GOV>date</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `birthdate_context_children` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `2f243fa5`  
**Description:**
Matches birthdate patterns specifically in the context of listing children for family benefits.

**Content:**
```
(?:für\s*seine\s*Kinder|Kinder)\s*(?:<DEP>person</DEP>),?\s*geb\.?(?:\s*am)?\s*<GOV>date</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `birthdate_parenthetical` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `134460da`  
**Description:**
Matches birthdate patterns where the person and date are enclosed in parentheses.

**Content:**
```
\(\s*<DEP>person</DEP>\s*(?:geb\.?(?:\s*am)?)?\s*<GOV>date</GOV>\s*\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `birthdate_list_item` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `41b11e9b`  
**Description:**
Matches birthdate patterns in a list item format (e.g., bullet points).

**Content:**
```
(?:\u2022|\uf0b7)\s*<DEP>person</DEP>\s*(?:\(\s*geb\.?(?:\s*am)?\s*<GOV>date</GOV>\s*\)|,?\s*geb\.?(?:\s*am)?\s*<GOV>date</GOV>)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ceo_of_handelsrechtlicher_geschäftsführer` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `7e3f18f9`  
**Description:**
Matches the specific legal title 'handelsrechtlicher Geschäftsführer' followed by 'der' or 'der Firma' connecting the person and organization.

**Content:**
```
(?i)handelsrechtlicher\s+Geschäftsführer\s+(?:der\s+)?(?:Firma\s+)?<GOV>\w+</GOV>.*?<DEP>\w+</DEP>|<GOV>\w+</GOV>.*?handelsrechtlicher\s+Geschäftsführer\s+(?:der\s+)?(?:Firma\s+)?<DEP>\w+</DEP>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ceo_of_geschäftsführer_der` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `b9f26185`  
**Description:**
Matches 'Geschäftsführer der' (Managing Director of) which is a common variation in the positive examples.

**Content:**
```
(?i)Geschäftsführer\s+der\s+<GOV>\w+</GOV>.*?<DEP>\w+</DEP>|<GOV>\w+</GOV>.*?Geschäftsführer\s+der\s+<DEP>\w+</DEP>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ceo_of_firma_geschäftsführer` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `60a81a29`  
**Description:**
Matches 'Geschäftsführer der Firma' pattern explicitly found in the training data.

**Content:**
```
(?i)Geschäftsführer\s+der\s+Firma\s+<GOV>\w+</GOV>.*?<DEP>\w+</DEP>|<GOV>\w+</GOV>.*?Geschäftsführer\s+der\s+Firma\s+<DEP>\w+</DEP>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ceo_of_verbunden_mit` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `c6daf7c7`  
**Description:**
Matches cases where the person is described as the managing director connected to the company using 'mit' or similar prepositions in the context of the title.

**Content:**
```
(?i)Geschäftsführer\s+(?:der|der\s+Firma|der\s+der)\s+<GOV>\w+</GOV>.*?<DEP>\w+</DEP>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ceo_of_contextual` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `fa92e620`  
**Description:**
Matches the pattern where the person is identified as the managing director in a list or clause structure.

**Content:**
```
(?i)<GOV>\w+</GOV>\s+(?:als\s+)?handelsrechtlicher\s+Geschäftsführer\s+(?:der\s+)?(?:Firma\s+)?<DEP>\w+</DEP>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `family_relation_mother_children` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `701874ba`  
**Description:**
Matches the specific context where the appellant is identified as the mother of children, linking the appellant (GOV) and the child (DEP) in a family relation.

**Content:**
```
(?i)Die\s+Beschwerdeführerin\s+ist\s+Mutter\s+der\s+unten\s+angeführten\s+Kinder.*?(?:<GOV>[^<]+</GOV>|<DEP>[^<]+</DEP>).*(?:<DEP>[^<]+</DEP>|<GOV>[^<]+</GOV>)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `family_relation_children_list` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `49210a4a`  
**Description:**
Matches the list structure following the mother statement where children are enumerated, capturing the relationship between the parent and the listed child.

**Content:**
```
(?i)Mutter\s+der\s+unten\s+angeführten\s+Kinder.*?(?:<GOV>[^<]+</GOV>).*?(?:<DEP>[^<]+</DEP>)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `nationality_citizen_phrase` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `41b92886`  
**Description:**
Matches the German phrase 'ist [GOV] Staatsbürger(in/er)' indicating nationality.

**Content:**
```
(?i)\bist\s+<GOV>[^<]+</GOV>\s+Staatsb\u00fcrger(?:in|er)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `svnr_after_steuernummer` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `d43310b0`  
**Description:**
Matches 'Steuernummer' followed by a number and then 'SVNR' in parentheses, identifying the SVNR as the social security number.

**Content:**
```
(?:Steuernummer\s+\d+[-/]\d+[^)]*)?\s*\(\s*SVNR\s*<GOV>social_security_number</GOV>\s*\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `svnr_directly_after_steuernummer` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `24d13d68`  
**Description:**
Matches 'Steuernummer' followed by a number and then 'SVNR' without parentheses, identifying the SVNR as the social security number.

**Content:**
```
Steuernummer\s+\d+[-/]\d+[^,]*\s*,?\s*SVNR\s*<GOV>social_security_number</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `svnr_with_brackets` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `a53d3064`  
**Description:**
Matches 'SVNR' enclosed in brackets or parentheses, identifying the SVNR as the social security number.

**Content:**
```
\(\s*SVNR\s*<GOV>social_security_number</GOV>\s*\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `svnr_following_tax_number` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `2c2e3309`  
**Description:**
Matches 'SVNR' appearing after a tax number pattern, identifying the SVNR as the social security number.

**Content:**
```
\d+[-/]\d+[^,]*\s*,?\s*SVNR\s*<GOV>social_security_number</GOV>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_number_steuernummer_post` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `2e25f953`  
**Description:**
Matches the <GOV>tax_number</GOV> entity immediately followed by 'Steuernummer' (less common but present in some examples or variations).

**Content:**
```
(?i)<GOV>tax_number</GOV>\s*Steuernummer
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_number_bescheid_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `1ace5113`  
**Description:**
Matches 'Steuernummer' within the context of a 'Bescheid' (tax assessment) to reinforce the tax number relationship.

**Content:**
```
(?i)Bescheid.*?Steuernummer\s*<GOV>tax_number</GOV>|Steuernummer\s*<GOV>tax_number</GOV>.*?Bescheid
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_number_einkommensteuer_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `eccc24af`  
**Description:**
Matches 'Steuernummer' in the context of 'Einkommensteuer' (income tax).

**Content:**
```
(?i)Einkommensteuer.*?Steuernummer\s*<GOV>tax_number</GOV>|Steuernummer\s*<GOV>tax_number</GOV>.*?Einkommensteuer
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_number_exclude_svrnr` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `de0e6f3a`  
**Description:**
Ensures the pattern does not match 'SVNr' (social security number) by explicitly looking for 'Steuernummer'.

**Content:**
```
(?i)Steuernummer\s*<GOV>tax_number</GOV>(?!.*SVNr)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `works_for_angestellt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `8f9f9c87`  
**Description:**
Matches the relation when the person was 'angestellt' (employed) at the organization.

**Content:**
```
(?i)<GOV>\w+</GOV>.*?(?:bei|für)\s+(?:der|die|das|einer|einem)\s+<DEP>\w+</DEP>\s+angestellt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `works_for_beschäftigt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `3c96fdc9`  
**Description:**
Matches the relation when the person was 'beschäftigt' (employed/engaged) at the organization.

**Content:**
```
(?i)<GOV>\w+</GOV>.*?(?:bei|für)\s+(?:der|die|das|einer|einem)\s+<DEP>\w+</DEP>\s+beschäftigt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `works_for_tätig` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `cf98ce14`  
**Description:**
Matches the relation when the person was 'tätig' (active/working) at the organization.

**Content:**
```
(?i)<GOV>\w+</GOV>.*?(?:bei|für)\s+(?:der|die|das|einer|einem)\s+<DEP>\w+</DEP>\s+tätig
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `works_for_arbeitgeber` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `0233eda5`  
**Description:**
Matches the relation when the organization is explicitly referred to as the 'Arbeitgeber' (employer) of the person.

**Content:**
```
(?i)<GOV>\w+</GOV>.*?vom\s+Arbeitgeber\s+<DEP>\w+</DEP>
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `works_for_nichtselbständig` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `RuleFormat.REGEX`  
**Rule ID:** `902ee0ce`  
**Description:**
Matches the relation when the person was 'nichtselbständig tätig' (employed non-self-employed) at the organization.

**Content:**
```
(?i)<GOV>\w+</GOV>.*?(?:bei|für)\s+(?:der|die|das|einer|einem)\s+<DEP>\w+</DEP>.*?nichtselbständig\s+tätig
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

