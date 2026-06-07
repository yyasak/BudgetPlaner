<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Einkommen</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

<main class="flow-page">

<div class="section-header">
    <p class="section-label">Schritt 1 von 4</p>

    <h2>Monatsbudget planen</h2>

    <p>
        Gib zuerst dein monatliches Einkommen und deine gewünschte Reserve ein.
    </p>
</div>

<form class="expense-form" action="/fixkosten" method="post">

    <div class="form-group">
        <label for="gehalt">Monatliches Gehalt</label>
        <input type="number" id="gehalt" name="gehalt">
    </div>

    <div class="form-group">
        <label for="reserve">Monatliche Reserve</label>
        <input type="number" id="reserve" name="reserve">
    </div>

    <button class="button button--primary" type="submit">
        Weiter zu Fixkosten
    </button>

</form>
</main>
</body>
</html>