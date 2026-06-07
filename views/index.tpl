<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SpendWise</title>

    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

<header class="site-header">
    <div class="site-header__content">
        <h1>SpendWise</h1>

        <nav class="process-navigation">
            <ul>
                <li><a href="#dashboard">Dashboard</a></li>
                <li><a href="#ausgaben">Ausgaben</a></li>
                <li><a href="#analyse">Analyse</a></li>
                <li><a href="#sparen">Sparen</a></li>
            </ul>
        </nav>
    </div>
</header>

<section class="start-planning">

    <a href="/einkommen" class="start-button">
        Budgetplanung starten
    </a>

    <p class="start-info">
        --- Erfasse dein Einkommen, deine Fixkosten und deine variablen Kosten
        und erhalte anschließend eine vollständige Auswertung ---
    </p>

</section>

<main>

    <section id="dashboard">
        <div class="section-header">
            <p class="section-label">Dashboard</p>
            <h2>Monatsübersicht</h2>
        </div>

        <div class="budget-overview">
            <div class="budget-card">
                <h3>Monatsbudget</h3>
                <p id="monthly-budget">0 €</p>
            </div>

            <div class="budget-card">
                <h3>Ausgaben</h3>
                <p id="spent-total">0 €</p>
            </div>

            <div class="budget-card">
                <h3>Verfügbar</h3>
                <p id="remaining-budget">0 €</p>
            </div>

            <div class="budget-card">
                <h3>Einträge</h3>
                <p id="expense-count">0</p>
            </div>
        </div>
    </section>

    <section id="ausgaben">
        <div class="section-header">
            <p class="section-label">Ausgaben</p>
            <h2>Neue Ausgabe hinzufügen</h2>
        </div>

        <div class="management-layout">

            <form id="expense-form" class="expense-form">
                <div class="form-group">
                    <label for="betrag">Betrag</label>
                    <input type="number" id="betrag" placeholder="z. B. 25">
                </div>

                <div class="form-group">
                    <label for="kategorie">Kategorie</label>
                    <select id="kategorie">
                        <option value="">Bitte wählen</option>
                        <option value="Lebensmittel">Lebensmittel</option>
                        <option value="Freizeit">Freizeit</option>
                        <option value="Transport">Transport</option>
                        <option value="Miete">Miete</option>
                        <option value="Sonstiges">Sonstiges</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="datum">Datum</label>
                    <input type="date" id="datum">
                </div>

                <div class="form-group">
                    <label for="beschreibung">Beschreibung</label>
                    <input type="text" id="beschreibung" placeholder="z. B. Einkauf">
                </div>

                <button class="button button--primary" type="submit">
                    Speichern
                </button>
            </form>

            <div class="chart-panel">
                <h3>Letzte Ausgaben</h3>
                <ul id="recent-expenses-list"></ul>
            </div>
        </div>
    </section>

    <section id="analyse">
        <div class="section-header">
            <p class="section-label">Analyse</p>
            <h2>Auswertung</h2>
        </div>

        <div class="analysis-grid">

            <div class="chart-panel">
                <h3>Ausgabenliste</h3>

                <table>
                    <thead>
                        <tr>
                            <th>Datum</th>
                            <th>Beschreibung</th>
                            <th>Kategorie</th>
                            <th>Betrag</th>
                        </tr>
                    </thead>

                    <tbody id="expense-table-body-analysis"></tbody>
                </table>
            </div>
        </div>

        <div class="chart-panel">
            <h3>Kategorien</h3>

            <canvas 
                id="expense-chart" 
                width="250" 
                height="250">
            </canvas>

            <div id="chart-legend"></div>
   
        </div>
    </div>
</section>

    <section id="sparen">
        <div class="section-header">
            <p class="section-label">Sparen</p>
            <h2>Sparziel</h2>
        </div>

        <div class="management-layout">

            <form id="saving-form" class="expense-form">
                <div class="form-group">
                    <label for="saving-name-input">Name</label>
                    <input type="text" id="saving-name-input">
                </div>

                <div class="form-group">
                    <label for="saving-goal-input">Zielbetrag</label>
                    <input type="number" id="saving-goal-input">
                </div>

                <div class="form-group">
                    <label for="saving-current-input">Aktueller Betrag</label>
                    <input type="number" id="saving-current-input">
                </div>

                <div class="form-group">
                    <label for="saving-deadline-input">Zieldatum</label>
                    <input type="month" id="saving-deadline-input">
                </div>

                <button class="button button--primary" type="submit">
                    Aktualisieren
                </button>
            </form>

            <div class="summary-card">
                <h3 id="saving-title">Sparziel</h3>
                <p id="saving-text">0 €</p>
                <span id="saving-deadline-text"></span>

                <div class="progress-track">
                    <div id="saving-progress" class="progress-fill"></div>
                </div>
            </div>
        </div>
    </section>

</main>
<script src="/static/script.js"></script>
</body>
</html>
