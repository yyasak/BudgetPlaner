import json
from datetime import datetime

DATEI = "state.json"

# --Lädt die gespeicherten Anwendungsdaten-- 
def load_state():
    try:
        with open(DATEI, "r") as datei:
            daten = json.load(datei)

        return daten

    except:
        return {}

# -- Speichert Daten in der state.json--
def save_state(daten):
    with open(DATEI, "w") as datei:
        json.dump(daten, datei, indent=4)


def lade_letzten_monat():
    daten = load_state()

    return daten.get("aktueller_monat", {})



# --Führt alle Speicheropeartionen zusammen aus 
def speichere_aktuellen_monat(daten):
    alte_daten = load_state()

    alte_daten["aktueller_monat"] = {
        "restgeld": daten["restgeld"],
        "fixkosten": daten["fixkosten"],
        "variablekosten": daten["variablekosten"]
    }

    save_state(alte_daten)

def reset_monat():
    save_state({})

def speichere_letzte_berechnung(daten):
    alte_daten = load_state()

    alte_daten["letzte_berechnung"] = {
        "datum": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "restgeld": daten["restgeld"]
    }

    save_state(alte_daten)


def lade_letzte_berechnung():
    daten = load_state()

    return daten.get("letzte_berechnung", {})

def speichere_alle_daten(daten):
    save_state(daten)
    speichere_aktuellen_monat(daten)
    speichere_letzte_berechnung(daten)