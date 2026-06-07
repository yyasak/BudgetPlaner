<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <title>Ergebnis</title>
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>

    <main class="flow-page">

    <div class="section-header">
    <p class="section-label">Schritt 4 von 4</p>

    <h2>Budgetanalyse</h2>
    </div>
        <hr class="section-divider">

        <div class="section-header">
            <h3>Budgetübersicht:</h3>
        </div>
        
        <div class="karten-bereich">

        <div class="karte">
            <h3>💰 Gehalt</h3>
            <p>{{daten["gehalt"]}} €</p>
        </div>

        <div class="karte">
            <h3>🛡️ Reserve</h3>
            <p>{{daten["reserve"]}} €</p>
        </div>

        <div class="karte">
            <h3>🏠 Fixkosten</h3>
            <p>{{daten["fixkosten"]}} €</p>
        </div>

        <div class="karte">
            <h3>🛒 Variable Kosten</h3>
            <p>{{daten["variablekosten"]}} €</p>
        </div>

        <div class="karte highlight">
            <h3>📈 Restgeld</h3>
            <p>{{daten["restgeld"]}} €</p>
        </div>

    </div>

    <hr class="section-divider">

    <div class="section-header">
        <h3>Analyse:</h3>
    </div>

    <div class="karten-bereich">

        <div class="karte">
            <h3>Sparquote</h3>
            <p>{{round(daten["sparquote"],1)}} %</p>
        </div>

        <div class="karte">
            <h3>Fixkostenquote</h3>
            <p>{{round(daten["fixkostenquote"],1)}} %</p>
        </div>

        <div class="karte">
            <h3>Variable Kostenquote</h3>
            <p>{{round(daten["variablekostenquote"],1)}} %</p>
        </div>

    </div>

    <hr class="section-divider">

    <h2>📊 Budgetverbrauch</h2>

    <p>
        {{round(daten["budget_prozent"], 1)}} % des Einkommens wurden eingeplant
    </p>

    <div class="progress-track">
        <div class="progress-fill"
             style="
                width: {{daten['budget_prozent']}}%;
                background-color: {{daten['balken_farbe']}};
             ">
        </div>
    </div>
    <div class="karten-bereich">

    <div class="karte">
        <h3>📊 Bewertung</h3>
        <p>{{daten["bewertung"]}}</p>
    </div>

    <div class="karte">
        <h3>💡 Spartipp</h3>
        <p>{{daten["tipp"]}}</p>
    </div>

    </div>

    <div class="karte">
    <h3>🎯 Größter Kostenpunkt</h3>

    <p>
        {{daten["groesste_kategorie"]}}
    </p>

    <span>
        {{daten["groesster_betrag"]}} €
    </span>
    </div>

    <hr class="section-divider">

    <h3>Vergleich zur letzten Berechnung:</h3>

    % if daten.get("letzte_berechnung"):
        <p>
            Letzte Berechnung:
            <strong>{{daten["letzte_berechnung"]["datum"]}}</strong>
        </p>

        <p>
            Restgeld damals:
            <strong>{{daten["letzte_berechnung"]["restgeld"]}} €</strong>
        </p>
    % else:
        <p>Noch keine frühere Berechnung vorhanden.</p>
    % end

    <p>
        Restgeld heute:
        <strong>{{daten["restgeld"]}} €</strong>
    </p>

    <p>{{daten["vergleich_text"]}}</p>

    <div class="form-actions">
        <a class="button button--secondary" href="/reset">
        Monatsdaten zurücksetzen
        </a>

        <a class="button button--primary" href="/">
        Zum Dashboard
        </a>

    </div>
    </main>
</body>
</html>