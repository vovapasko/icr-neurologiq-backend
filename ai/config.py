import os
from collections import namedtuple

# 32 because we don't need symbols after space to be included
ascii_index_to_check = 48

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))   # gets the directory where current file is
save_filename = 'results'

file_formats_to_save_names = {
    'json': f'{save_filename}.json',
    'csv': f'{save_filename}.csv'
}

OCRLocation = namedtuple("Location", ["id", "bbox", "filter_keywords"])

OCR_LOCATIONS = [

    # up right
    OCRLocation("psd_kontonummer", (1075, 271, 441, 53), ["psd", "kontonummer"]),

    # kontoinhaber block
    OCRLocation("kontoinhar_vorname_name", (839, 552, 669, 49), ["vorname", "name"]),
    OCRLocation("kontoinhaber_strasse", (839, 619, 669, 49), ["strasse", "hausnummer"]),
    OCRLocation("kontoinhaber_plz_ort", (839, 690, 669, 49), ["plz", "ort"]),
    OCRLocation("kontoinhaber_telefon_privat", (839, 763, 319, 49), ["telefon", "privat"]),
    OCRLocation("kontoinhaber_telefon_geschaeftlich", (1182, 763, 319, 49), ["telefon", "geschaeftlich"]),
    OCRLocation("kntoinhaber_geburtsdatum", (839, 834, 671, 56), ["geburtsdatum"]),
    OCRLocation("kontoinhaber_email", (839, 910, 671, 56), ["email"]),

    # beitrittserklaerung
    OCRLocation("beitrittserklaerung_weiteren", (523, 1118, 185, 69), []),  # alternativ 78x46
    OCRLocation("beitrittserklaerung_geschaeftsanteil", (1057, 1124, 185, 75), []),  # alternativ 68x51 nicht lesbar

    OCRLocation("auftrag_iban", (209, 1347, 455, 49), ["iban"]),
    OCRLocation("sepa_betrag_psd_bank_konto", (128, 1641, 234, 47), ["betrag"]),  # nicht lesbar
    OCRLocation("sepa_iban", (760, 1639, 513, 50), ["iban"]),

    OCRLocation("psd_formularnummer", (193, 2212, 125, 61), [])
]

ORC_second_page = [
    # SEPA-Lastschriftmandat
    OCRLocation("sepa_lastschriftmandat_identifikationsnummer", (145, 102, 629, 50), ["glaeubireger",
                                                                                      "identifikationsnummer", "ci",
                                                                                      "creditor", "identifier"]),
    OCRLocation("sepa_lastschriftmandat_mandatsreferenz", (805, 101, 732, 52), ["mandatsreferenz", "von",
                                                                               "der", "bank", "ausgefuellt"]),
    OCRLocation("sepa_lastschriftmandat_kontoinhaber", (137, 340, 1393, 55), ["x", "kontoinhaber", "vorname", "name"]),
    OCRLocation("sepa_lastschriftmandat_anschrift", (137, 415, 1391, 40), ["x", "anschrift", "strasse", "hausnummer",
                                                                           "plz", "ort", "bitte", "angeben", "wenn",
                                                                           "kontoinhaber", "nicht", "gleichzeitig"
                                                                           "zahlungsempfaenger", "darlehensnehmer"
                                                                           "ist"]),
    OCRLocation("sepa_lastschriftmandat_kreditinstitut", (137, 474, 630, 49), ["x", "kreditinstitut"]),
    OCRLocation("sepa_lastschriftmandat_bic", (803, 474, 733, 45), ["x", "ausserhalb", "des", "europaeischen",
                                                                    "wirtschaftsraums"]),
    OCRLocation("sepa_lastschriftmandat_iban", (137, 539, 1395, 41), ["x", "iban"]),
    OCRLocation("sepa_lastschriftmandat_ort_datum", (137, 613, 566, 65), ["x", ",", "ort", "datum", "angabe", "immer",
                                                                          "erforderlich"]),
    OCRLocation("sepa_lastschriftmandat_unterschrift", (740, 613, 799, 64), ["unterschrift", "der", "des",
                                                                             "girokontoinhaber", "s", "gesetzlichen",
                                                                             "vertreters", "fuer", "das", "sepa",
                                                                             "lastschriftmandat", "immer",
                                                                             "erforderlich"]),
    OCRLocation("sepa_lastschriftmandat_zugelassen", (595, 726, 273, 44), [])
]
