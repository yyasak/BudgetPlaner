<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <title>Variable Kosten</title>

    <link rel="stylesheet" href="/static/style.css">
</head>

<body>

    <main class="flow-page">

    <div class="section-header">
    <p class="section-label">Schritt 3 von 4</p>
    <h2>Variable Kosten erfassen</h2>
    <p>
        Erfasse nun alle flexiblen Ausgaben.
    </p>
    </div>
    <form class="expense-form" action="/ergebnis" method="post">

        <!-- Werte von vorherigen Seiten weitergeben -->

        <input type="hidden" name="gehalt" value="{{gehalt}}">
        <input type="hidden" name="reserve" value="{{reserve}}">
        <input type="hidden" name="fixkosten" value="{{fixkosten}}">

        <div class="form-grid">

    <div class="form-group">
        <label for="lebensmittel">Lebensmittel</label>
        <input type="number" id="lebensmittel" name="lebensmittel">
    </div>

    <div class="form-group">
        <label for="tanken">Tanken</label>
        <input type="number" id="tanken" name="tanken">
    </div>

    <div class="form-group">
        <label for="freizeit">Freizeit</label>
        <input type="number" id="freizeit" name="freizeit">
    </div>

    <div class="form-group">
        <label for="kleidung">Kleidung</label>
        <input type="number" id="kleidung" name="kleidung">
    </div>

    <div class="form-group">
        <label for="restaurant">Restaurant</label>
        <input type="number" id="restaurant" name="restaurant">
    </div>

    <div class="form-group">
        <label for="streaming">Streaming</label>
        <input type="number" id="streaming" name="streaming">
    </div>

</div>

<div class="section-header">
    <h3>Weitere Ausgaben</h3>
</div>

<div id="eigene-variable-kosten"></div>

    <div class="form-actions">

    <button
        class="button button--secondary"
        type="button"
        onclick="neueVariableKosten()">

        + Weitere variable Kosten hinzufügen

    </button>

    <button
            class="button button--primary"
            type="submit">

            Ergebnis anzeigen

        </button>
    </div>

    </form>
    </main>

    <script src="/static/script.js"></script>

</body>
</html>