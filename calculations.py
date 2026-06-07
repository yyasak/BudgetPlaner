def total(werte):
    return sum(werte)


def calculate_restgeld(
    gehalt,
    reserve,
    fixkosten,
    variable_kosten
):
    return (
        gehalt
        - reserve
        - fixkosten
        - variable_kosten
    )

def bewerte_restgeld(restgeld):

    if restgeld < 0:
        return "Achtung: Du gibst mehr Geld aus als du einnimmst."

    elif restgeld < 200:
        return "Dein Restgeld ist eher knapp."

    else:
        return "Deine Finanzplanung sieht gut aus."

def smarter_tipp(
    gehalt,
    fixkosten,
    variablekosten,
    restgeld
):

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