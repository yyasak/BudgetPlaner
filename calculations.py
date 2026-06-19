def total(werte):
    return sum(werte)


def zahl(formular, name):
    return float(formular.get(name) or 0)


def calculate_restgeld(gehalt, reserve, fixkosten, variablekosten):
    return gehalt - reserve - fixkosten - variablekosten


def berechne_fixkosten(formular):
    fixkosten_liste = [
        zahl(formular, "miete"),
        zahl(formular, "strom"),
        zahl(formular, "internet"),
        zahl(formular, "versicherungen"),
        zahl(formular, "abos"),
        zahl(formular, "handyvertrag"),
        zahl(formular, "ratenzahlungen")
    ]

    for key in formular:
        if "fix_betrag_" in key:
            fixkosten_liste.append(zahl(formular, key))

    return total(fixkosten_liste)


def berechne_variablekosten(formular):
    variable_liste = [
        zahl(formular, "lebensmittel"),
        zahl(formular, "tanken"),
        zahl(formular, "freizeit"),
        zahl(formular, "kleidung"),
        zahl(formular, "restaurant"),
        zahl(formular, "streaming")
    ]

    for key in formular:
        if "var_betrag_" in key:
            variable_liste.append(zahl(formular, key))

    return total(variable_liste)


def groesster_variabler_kostenpunkt(formular):
    kategorien = {
        "Lebensmittel": zahl(formular, "lebensmittel"),
        "Tanken": zahl(formular, "tanken"),
        "Freizeit": zahl(formular, "freizeit"),
        "Kleidung": zahl(formular, "kleidung"),
        "Restaurant": zahl(formular, "restaurant"),
        "Streaming": zahl(formular, "streaming")
    }

    groesste_kategorie = max(kategorien, key=kategorien.get)
    groesster_betrag = kategorien[groesste_kategorie]

    return groesste_kategorie, groesster_betrag


def bewerte_restgeld(restgeld):
    if restgeld < 0:
        return "Achtung: Du gibst mehr Geld aus als du einnimmst."
    elif restgeld < 200:
        return "Dein Restgeld ist eher knapp."
    else:
        return "Deine Finanzplanung sieht gut aus."


def smarter_tipp(gehalt, fixkosten, variablekosten, restgeld):
    if restgeld < 0:
        return "Du gibst aktuell mehr Geld aus als du einnimmst."
    elif fixkosten > gehalt * 0.5:
        return "Deine Fixkosten sind sehr hoch."
    elif variablekosten > fixkosten:
        return "Deine variablen Kosten sind höher als deine Fixkosten."
    elif restgeld > 500:
        return "Sehr gute Finanzplanung. Du kannst gut sparen."
    else:
        return "Deine Ausgaben sehen insgesamt ausgeglichen aus."


def monatsvergleich_text(differenz):
    if differenz < 0:
        return "Diesen Monat hast du mehr Geld ausgegeben."
    elif differenz > 0:
        return "Diesen Monat hast du weniger Geld ausgegeben."
    else:
        return "Deine Ausgaben sind gleich geblieben."


def berechne_ergebnisdaten(formular, letzter_monat, letzte_berechnung):
    gehalt = zahl(formular, "gehalt")
    reserve = zahl(formular, "reserve")
    fixkosten = zahl(formular, "fixkosten")

    variablekosten = berechne_variablekosten(formular)
    gesamtausgaben = fixkosten + variablekosten

    restgeld = calculate_restgeld(
        gehalt,
        reserve,
        fixkosten,
        variablekosten
    )

    if gehalt > 0:
        budget_prozent = min((gesamtausgaben / gehalt) * 100, 100)
        sparquote = (restgeld / gehalt) * 100
        fixkostenquote = (fixkosten / gehalt) * 100
        variablekostenquote = (variablekosten / gehalt) * 100
    else:
        budget_prozent = 0
        sparquote = 0
        fixkostenquote = 0
        variablekostenquote = 0

    if budget_prozent < 70:
        balken_farbe = "green"
    elif budget_prozent < 90:
        balken_farbe = "orange"
    else:
        balken_farbe = "red"

    groesste_kategorie, groesster_betrag = groesster_variabler_kostenpunkt(formular)

    letztes_restgeld = letzter_monat.get("restgeld", 0)
    differenz = restgeld - letztes_restgeld
    vergleich_text = monatsvergleich_text(differenz)

    return {
        "gehalt": gehalt,
        "reserve": reserve,
        "fixkosten": fixkosten,
        "variablekosten": variablekosten,
        "restgeld": restgeld,
        "bewertung": bewerte_restgeld(restgeld),
        "tipp": smarter_tipp(gehalt, fixkosten, variablekosten, restgeld),
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