from bottle import route, run, template, request, static_file

from calculations import total, calculate_restgeld, bewerte_restgeld, smarter_tipp, monatsvergleich_text
from data_service import save_state, load_state, lade_letzten_monat, speichere_aktuellen_monat, reset_monat, speichere_letzte_berechnung, lade_letzte_berechnung

@route("/")
def dashboard():
    return template("index")

@route("/einkommen")
def einkommen_seite():
    return template("einkommen")

@route("/fixkosten", method="POST")
def fixkosten():
    gehalt = float(request.forms.get("gehalt") or 0)
    reserve = float(request.forms.get("reserve") or 0)

    return template(
        "fixkosten",
        gehalt=gehalt,
        reserve=reserve
    )


@route("/variablekosten", method="POST")
def variablekosten():
    gehalt = float(request.forms.get("gehalt") or 0)
    reserve = float(request.forms.get("reserve") or 0)

    miete = float(request.forms.get("miete") or 0)
    strom = float(request.forms.get("strom") or 0)
    internet = float(request.forms.get("internet") or 0)
    versicherungen = float(request.forms.get("versicherungen") or 0)
    abos = float(request.forms.get("abos") or 0)
    handyvertrag = float(request.forms.get("handyvertrag") or 0)
    ratenzahlungen = float(request.forms.get("ratenzahlungen") or 0)

    fixkosten_liste = [
        miete,
        strom,
        internet,
        versicherungen,
        abos,
        handyvertrag,
        ratenzahlungen
    ]

    for key in request.forms:
        if "fix_betrag_" in key:
            betrag = float(request.forms.get(key) or 0)
            fixkosten_liste.append(betrag)

    fixkosten = total(fixkosten_liste)

    return template(
        "variablekosten",
        gehalt=gehalt,
        reserve=reserve,
        fixkosten=fixkosten
    )


@route("/ergebnis", method="POST")
def ergebnis():
    gehalt = float(request.forms.get("gehalt") or 0)
    reserve = float(request.forms.get("reserve") or 0)
    fixkosten = float(request.forms.get("fixkosten") or 0)

    lebensmittel = float(request.forms.get("lebensmittel") or 0)
    tanken = float(request.forms.get("tanken") or 0)
    freizeit = float(request.forms.get("freizeit") or 0)
    kleidung = float(request.forms.get("kleidung") or 0)
    restaurant = float(request.forms.get("restaurant") or 0)
    streaming = float(request.forms.get("streaming") or 0)

    variable_kategorien = {
        "Lebensmittel": lebensmittel,
        "Tanken": tanken,
        "Freizeit": freizeit,
        "Kleidung": kleidung,
        "Restaurant": restaurant,
        "Streaming": streaming
    }

    groesste_kategorie = max(
        variable_kategorien,
        key=variable_kategorien.get
    )

    groesster_betrag = variable_kategorien[groesste_kategorie]

    variablekosten_liste = [
        lebensmittel,
        tanken,
        freizeit,
        kleidung,
        restaurant,
        streaming
    ]

    for key in request.forms:
        if "var_betrag_" in key:
            betrag = float(request.forms.get(key) or 0)
            variablekosten_liste.append(betrag)

    variablekosten = total(variablekosten_liste)

    gesamtausgaben = fixkosten + variablekosten

    if gehalt > 0:
        budget_prozent = min((gesamtausgaben / gehalt) * 100, 100)
    else:
        budget_prozent = 0

    if budget_prozent < 70:
        balken_farbe = "green"

    elif budget_prozent < 90:
        balken_farbe = "orange"

    else:
        balken_farbe = "red"

    restgeld = calculate_restgeld(
        gehalt,
        reserve,
        fixkosten,
        variablekosten
    )

    if gehalt > 0:
       sparquote = (restgeld / gehalt) * 100
       fixkostenquote = (fixkosten / gehalt) * 100
       variablekostenquote = (variablekosten / gehalt) * 100
    else:
       sparquote = 0
       fixkostenquote = 0
       variablekostenquote = 0

    vergleich = lade_letzten_monat()
    letztes_restgeld = vergleich.get("restgeld", 0)
    differenz = restgeld - letztes_restgeld
    vergleich_text = monatsvergleich_text(differenz)

    bewertung = bewerte_restgeld(restgeld)

    tipp = smarter_tipp(
        gehalt,
        fixkosten,
        variablekosten,
        restgeld
    )

    letzte_berechnung = lade_letzte_berechnung()

    daten = {
        "gehalt": gehalt,
        "reserve": reserve,
        "fixkosten": fixkosten,
        "variablekosten": variablekosten,
        "restgeld": restgeld,
        "bewertung": bewertung,
        "tipp": tipp,
        "letztes_restgeld": letztes_restgeld,
        "differenz": differenz,
        "vergleich_text": vergleich_text,
        "gesamtausgaben": gesamtausgaben,
	"budget_prozent": budget_prozent,
	"balken_farbe": balken_farbe,
	"sparquote": sparquote,
	"fixkostenquote": fixkostenquote,
	"variablekostenquote": variablekostenquote,
        "groesste_kategorie": groesste_kategorie,
        "groesster_betrag": groesster_betrag,
	"letzte_berechnung": letzte_berechnung
    }

    save_state(daten)
    speichere_aktuellen_monat(daten)
    speichere_letzte_berechnung(daten)

    return template("ergebnis", daten=daten)

@route("/api/state")
def api_state():
    return load_state()


@route("/static/<datei:path>")
def static_dateien(datei):
    return static_file(datei, root="static")


@route("/reset")
def reset():
    reset_monat()

    return """
    <h1>Monatsdaten wurden zurückgesetzt.</h1>
    <a href="/">Zurück zur Startseite</a>
    """


if __name__ == "__main__":
    run(host="127.0.0.1", port=8080, debug=True)