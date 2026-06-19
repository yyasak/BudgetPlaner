from bottle import (
    route,
    run,
    template,
    request,
    static_file,
)

from calculations import (
    zahl,
    berechne_fixkosten,
    berechne_ergebnisdaten,
)

from data_service import (
    load_state,
    lade_letzten_monat,
    reset_monat,
    lade_letzte_berechnung,
    speichere_alle_daten,
)


# --Startseite--
# --Zeigt das Dashboard mit den wichtigsten Informationen an--
@route("/")
def dashboard():
    return template("index")


# --Seite zur Eingabe des monatlichen Einkommens--
@route("/einkommen")
def einkommen_seite():
    return template("einkommen")


# --Verarbeitet die Einkommensdaten--
# --und öffnet die Seite zur Eingabe der Fixkosten--
@route("/fixkosten", method="POST")
def fixkosten():
    gehalt = zahl(request.forms, "gehalt")
    reserve = zahl(request.forms, "reserve")

    return template(
        "fixkosten",
        gehalt=gehalt,
        reserve=reserve
    )


# --Verarbeitet die Fixkosten--
# --und öffnet die Seite zur Eingabe der variablen Kosten--
@route("/variablekosten", method="POST")
def variablekosten():
    gehalt = zahl(request.forms, "gehalt")
    reserve = zahl(request.forms, "reserve")

    fixkosten = berechne_fixkosten(request.forms)

    return template(
        "variablekosten",
        gehalt=gehalt,
        reserve=reserve,
        fixkosten=fixkosten
    )


# --Berechnet alle Kennzahlen--
# --und zeigt die Ergebnisseite an--
@route("/ergebnis", method="POST")
def ergebnis():
    daten = berechne_ergebnisdaten(
        request.forms,
        lade_letzten_monat(),
        lade_letzte_berechnung()
    )

    speichere_alle_daten(daten)

    return template("ergebnis", daten=daten)


# --API-Endpunkt zum Laden gespeicherter Daten--
@route("/api/state")
def api_state():
    return load_state()


# --Stellt CSS-, JavaScript- und andere statische Dateien bereit--
@route("/static/<datei:path>")
def static_dateien(datei):
    return static_file(datei, root="static")


# --Setzt gespeicherte Monatsdaten zurück--
@route("/reset")
def reset():
    reset_monat()

    return template("reset")


# --Informationsseite mit Projektbeschreibung und Teammitgliedern--
@route("/about")
def about():
    return template("about")


# --Startet den Bottle-Webserver--
if __name__ == "__main__":
    run(host="127.0.0.1", port=8080, debug=True)