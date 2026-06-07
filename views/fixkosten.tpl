<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <title>Fixkosten</title>

    <link rel="stylesheet" href="/static/style.css">
</head>

<body>

    <main class="flow-page">

    <div class="section-header">
    <p class="section-label">Schritt 2 von 4</p>
    <h2>Fixkosten erfassen</h2>
    <p>
        Trage alle Ausgaben ein, die jeden Monat regelmäßig anfallen.
    </p>
    </div>
    <form class="expense-form" action="/variablekosten" method="post">

        <!-- Werte von Seite 1 weitergeben -->

        <input type="hidden" name="gehalt" value="{{gehalt}}">
        <input type="hidden" name="reserve" value="{{reserve}}">

        <h2>Fixkosten</h2>

        <div class="form-grid">

    <div class="form-group">
        <label for="miete">Miete</label>
        <input type="number" id="miete" name="miete">
    </div>

    <div class="form-group">
        <label for="strom">Strom</label>
        <input type="number" id="strom" name="strom">
    </div>

    <div class="form-group">
        <label for="internet">Internet</label>
        <input type="number" id="internet" name="internet">
    </div>

    <div class="form-group">
        <label for="versicherungen">Versicherungen</label>
        <input type="number" id="versicherungen" name="versicherungen">
    </div>

    <div class="form-group">
        <label for="abos">Abos</label>
        <input type="number" id="abos" name="abos">
    </div>

    <div class="form-group">
        <label for="handyvertrag">Handyvertrag</label>
        <input type="number" id="handyvertrag" name="handyvertrag">
    </div>

    <div class="form-group">
        <label for="ratenzahlungen">Ratenzahlungen</label>
        <input type="number" id="ratenzahlungen" name="ratenzahlungen">
    </div>

</div>

       <div class="section-header">
            <h3>Weitere Ausgaben</h3>
        </div>

        <div id="eigene-fixkosten"></div>

       <button
            class="button button--secondary"
            type="button"
            onclick="neueFixkosten()">

            + Weitere Fixkosten hinzufügen

        </button>

        <button
            class="button button--primary"
            type="submit">

            Weiter zu variablen Kosten

        </button>
    </form>

    <script src="/static/script.js"></script>
</main>
</body>
</html>