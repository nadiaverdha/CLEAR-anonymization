DATASET_CLASS_DEFINITIONS = {
    "ler": {
        "PERS": "Personen (Familien-, Vor-, Beinamen und Pseudonyme)",
        "LOC": "Ortsnamen und geographische Bezeichnungen (Land, Stadt, Region)",
        "ORG": "Organisationsnamen (Parteien, Vereine, Institutionen, Unternehmen)",
        "NRM": "Rechtsnormen (europäische Normen, Gesetze, Rechtsverordnungen)",
        "RS": "Rechtsprechung (Zitate von Gerichtsentscheidungen, keine Personennamen)",
        "LIT": "Rechtsliteratur (Fachliteratur, Gesetzgebungsmaterialien)",
        "REG": "Einzelfallregelungen (Vorschriften, Verträge)",
    },
    "m2n": {
        "person": "Personennamen",
        "organisation": "Organisationsnamen",
        "account": "Konten",
        "email_address": "E-Mail-Adressen",
        "date": "Datumsangaben",
        "business_register_number": "Handelsregister- oder Unternehmensnummern",
        "phone_number": "Telefonnummern",
        "website": "Webseiten oder URLs",
        "vehicle_license": "Kfz-Kennzeichen",
        "vat_reg_no": "Umsatzsteuer-Identifikationsnummern",
        "address": "Postadressen",
        "tax_number": "Steuernummern",
    },
}


def get_dataset_class_definitions(dataset: str) -> dict[str, str]:
    if dataset not in DATASET_CLASS_DEFINITIONS:
        raise ValueError(f"Unknown dataset: {dataset}")
    return DATASET_CLASS_DEFINITIONS[dataset]


__all__ = [
    "DATASET_CLASS_DEFINITIONS",
    "get_dataset_class_definitions",
]
