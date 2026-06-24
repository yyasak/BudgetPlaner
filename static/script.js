/* ---------------- KONSTANTEN ---------------- */
const STORAGE_KEY = "spendwise-data";

/* ---------------- STANDARDDATEN ---------------- */
const defaultState = {
    monthlyBudget: 0,
    monthlyIncome: 0,

    savingGoalName: "",
    savingGoal: 0,
    savingCurrent: 0,
    savingDeadline: "",

    previousMonthTotals: {},
    reminders: [],
    selectedCalendarDate: "",
    expenses: []
};

/* ---------------- DOM ELEMENTE ---------------- */
const elements = {
    expenseForm: document.querySelector("#expense-form"),
    budgetForm: document.querySelector("#budget-form"),
    savingForm: document.querySelector("#saving-form"),

    amountInput: document.querySelector("#betrag"),
    categoryInput: document.querySelector("#kategorie"),
    dateInput: document.querySelector("#datum"),
    descriptionInput: document.querySelector("#beschreibung"),

    budgetInput: document.querySelector("#budget-input"),
    incomeInput: document.querySelector("#income-input"),

    savingNameInput: document.querySelector("#saving-name-input"),
    savingGoalInput: document.querySelector("#saving-goal-input"),
    savingCurrentInput: document.querySelector("#saving-current-input"),
    savingDeadlineInput: document.querySelector("#saving-deadline-input"),

    spentTotal: document.querySelector("#spent-total"),
    remainingBudget: document.querySelector("#remaining-budget"),
    monthlyBudget: document.querySelector("#monthly-budget"),
    expenseCount: document.querySelector("#expense-count"),

    expenseTableBody: document.querySelector("#expense-table-body-analysis"),
    recentExpensesList: document.querySelector("#recent-expenses-list"),

    categorySummary: document.querySelector("#category-summary"),
    chartLegend: document.querySelector("#chart-legend"),

    savingTitle: document.querySelector("#saving-title"),
    savingText: document.querySelector("#saving-text"),
    savingDeadlineText: document.querySelector("#saving-deadline-text"),
    savingProgress: document.querySelector("#saving-progress")

};

/* ---------------- DATENSPEICHERUNG ---------------- */
let appState = loadState();

function loadState() {
    const savedState = localStorage.getItem(STORAGE_KEY);

    if (!savedState) {
        return structuredClone(defaultState);
    }

    try {
        return {
            ...structuredClone(defaultState),
            ...JSON.parse(savedState)
        };
    } catch {
        return structuredClone(defaultState);
    }
}

function saveState() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
}

async function syncBackend() {
    try {
        await fetch(API_ENDPOINT, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(appState)
        });
    } catch {
        console.warn("Backend aktuell nicht erreichbar.");
    }
}

/* ---------------- FORMATIERUNG ---------------- */
function formatEuro(value) {
    return new Intl.NumberFormat("de-DE", {
        style: "currency",
        currency: "EUR",
        maximumFractionDigits: 0
    }).format(value);
}

function formatDate(date) {
    return new Intl.DateTimeFormat("de-DE", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric"
    }).format(new Date(date));
}

function formatMonth(date = new Date()) {
    return new Intl.DateTimeFormat("de-DE", {
        month: "long",
        year: "numeric"
    }).format(date);
}

function todayIso() {
    return new Date().toISOString().split("T")[0];
}

/* ---------------- BERECHNUNGEN ---------------- */
function totalExpenses() {
    return appState.expenses.reduce((sum, expense) => {
        return sum + expense.amount;
    }, 0);
}

function categoryTotals() {
    return appState.expenses.reduce((totals, expense) => {
        totals[expense.category] = (totals[expense.category] || 0) + expense.amount;
        return totals;
    }, {});
}

/* ---------------- DASHBOARD RENDERING ---------------- */
function renderBudget() {
    if (
        !elements.spentTotal ||
        !elements.remainingBudget ||
        !elements.monthlyBudget ||
        !elements.expenseCount
    ) {
        return;
    }

    const spent = totalExpenses();
    const remaining = appState.monthlyBudget - spent;

    elements.spentTotal.textContent = formatEuro(spent);
    elements.remainingBudget.textContent = formatEuro(remaining);
    elements.monthlyBudget.textContent = formatEuro(appState.monthlyBudget);
    elements.expenseCount.textContent = `${appState.expenses.length} Einträge gespeichert`;
}

function renderExpenses() {
    if (!elements.expenseTableBody) {
        return;
    }

    elements.expenseTableBody.innerHTML = "";
   
    const expenses = [...appState.expenses]
        .sort((a, b) => new Date(b.date) - new Date(a.date));

    expenses.forEach((expense) => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${formatDate(expense.date)}</td>
            <td>${expense.description}</td>
            <td>${expense.category}</td>
            <td>${formatEuro(expense.amount)}</td>
        `;

        elements.expenseTableBody.append(row);
    });
}

function renderRecentExpenses() {
    if (!elements.recentExpensesList) {
    return;
    }
    
    elements.recentExpensesList.innerHTML = "";

    const recent = [...appState.expenses]
        .sort((a, b) => new Date(b.date) - new Date(a.date))
        .slice(0, 5);

    recent.forEach((expense) => {
        const item = document.createElement("li");

        item.innerHTML = `
            <div>
                <strong>${expense.description}</strong>
                <span>${formatDate(expense.date)} · ${expense.category}</span>
            </div>
            <b>${formatEuro(expense.amount)}</b>
        `;

        elements.recentExpensesList.append(item);
    });
}

function renderChart() {
    const canvas = document.querySelector("#expense-chart");

    if (!canvas) {
        return;
    }

    const ctx = canvas.getContext("2d");
    const totals = categoryTotals();

    const values = Object.values(totals);

    if (values.length === 0) {
        return;
    }

    const total = values.reduce((sum, value) => sum + value, 0);

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const colors = [
        "#4f46e5",
        "#10b981",
        "#f59e0b",
        "#ef4444",
        "#06b6d4",
        "#8b5cf6"
    ];

    let startAngle = 0;

    Object.entries(totals).forEach(([category, amount], index) => {
        const sliceAngle = (amount / total) * Math.PI * 2;

        ctx.beginPath();
        ctx.moveTo(125, 125);

        ctx.arc(
            125,
            125,
            100,
            startAngle,
            startAngle + sliceAngle
        );

        ctx.closePath();
        ctx.fillStyle = colors[index % colors.length];
        ctx.fill();

        startAngle += sliceAngle;
    });
}

function renderLegend() {
    if (!elements.chartLegend) {
        return;
    }

    elements.chartLegend.replaceChildren();

    const totals = categoryTotals();

    const colors = [
        "#4f46e5",
        "#10b981",
        "#f59e0b",
        "#ef4444",
        "#06b6d4",
        "#8b5cf6"
    ];

    Object.keys(totals).forEach((category, index) => {
        const item = document.createElement("div");

        item.className = "legend-item";

        item.innerHTML = `
            <span class="legend-color"
                  style="background:${colors[index % colors.length]}"></span>
            <span>${category}</span>
        `;

        elements.chartLegend.append(item);
    });
}

function renderSavings() {
    if (!elements.savingProgress) {
        return;
    }

    const goal = appState.savingGoal || 1;

    const percent = Math.min(
        Math.round((appState.savingCurrent / goal) * 100),
        100
    );

    elements.savingTitle.textContent = appState.savingGoalName;

    elements.savingText.textContent =
        `${formatEuro(appState.savingCurrent)} von ${formatEuro(appState.savingGoal)} erreicht`;

    elements.savingDeadlineText.textContent =
        `bis ${appState.savingDeadline}`;

    elements.savingProgress.style.width = `${percent}%`;
}

function renderAll() {
    renderBudget();
    renderExpenses();
    renderRecentExpenses();
    renderChart();
    renderLegend();
    renderSavings();

    saveState();
}

/* ---------------- FORMULAR HANDLER ---------------- */
function handleExpenseSubmit(event) {
    event.preventDefault();

    const amount = Number(elements.amountInput.value);
    const category = elements.categoryInput.value;
    const date = elements.dateInput.value;
    let description = elements.descriptionInput.value.trim();

    if (!amount || !category || !date ) {
        alert("Bitte Betrag, Kategorie und Datum ausfüllen.");
        return;
    }

    if (!description) {
	description = "Keine Beschreibung";
    }

    appState.expenses.push({
        id: Date.now(),
        amount,
        category,
        date,
        description
    });

    elements.expenseForm.reset();
    elements.dateInput.value = todayIso();

    renderAll();
}

function handleBudgetSubmit(event) {
    event.preventDefault();

    appState.monthlyBudget = Number(elements.budgetInput.value);
    appState.monthlyIncome = Number(elements.incomeInput.value);

    renderAll();
}

function handleSavingSubmit(event) {
    event.preventDefault();

    appState.savingGoalName = elements.savingNameInput.value;
    appState.savingGoal = Number(elements.savingGoalInput.value);
    appState.savingCurrent = Number(elements.savingCurrentInput.value);
    appState.savingDeadline = elements.savingDeadlineInput.value;

    renderAll();
}

function initFormValues() {
    if (elements.dateInput) {
        elements.dateInput.value = todayIso();
    }

    if (elements.budgetInput) {
        elements.budgetInput.value = appState.monthlyBudget;
    }

    if (elements.incomeInput) {
        elements.incomeInput.value = appState.monthlyIncome;
    }

    if (elements.savingNameInput) {
        elements.savingNameInput.value = appState.savingGoalName;
    }

    if (elements.savingGoalInput) {
        elements.savingGoalInput.value = appState.savingGoal;
    }

    if (elements.savingCurrentInput) {
        elements.savingCurrentInput.value = appState.savingCurrent;
    }

    if (elements.savingDeadlineInput) {
        elements.savingDeadlineInput.value = appState.savingDeadline;
    }
}

/* ---------------- DYNAMISCHE EINGABEFELDER ---------------- */
let nummer = 0;
let variableNummer = 0;

function neueFixkosten() {
    nummer++;

    let bereich = document.getElementById("eigene-fixkosten");

    bereich.innerHTML += `
        <label>Name der Fixkosten:</label>
        <input type="text" name="fix_name_${nummer}">

        <br><br>

        <label>Betrag:</label>
        <input
            type="number"
            min="0"
            step="10"
            name="fix_betrag_${nummer}">
        <br><br>
    `;
}

function neueVariableKosten() {
    variableNummer++;

    let bereich = document.getElementById("eigene-variable-kosten");

    bereich.innerHTML += `
        <label>Name der variablen Kosten:</label>
        <input
            type="number"
            min="0"
            step="10"
            name="var_betrag_${variableNummer}">
        <br><br>

        <label>Betrag:</label>
        <input type="number" name="var_betrag_${variableNummer}">

        <br><br>
    `;
}

function initEvents() {
    if (elements.expenseForm) {
        elements.expenseForm.addEventListener("submit", handleExpenseSubmit);
    }

    if (elements.budgetForm) {
        elements.budgetForm.addEventListener("submit", handleBudgetSubmit);
    }

    if (elements.savingForm) {
        elements.savingForm.addEventListener("submit", handleSavingSubmit);
    }
}

/* ---------------- INITIALISIERUNG ---------------- */
async function init() {
    try {
        const response = await fetch("/api/state");
        const daten = await response.json();

        appState = {
            ...defaultState,
            ...daten,
            monthlyIncome: daten.gehalt || defaultState.monthlyIncome,
            monthlyBudget: daten.gehalt || defaultState.monthlyBudget,
            expenses: [
                {
                    id: 1,
                    date: new Date().toISOString().split("T")[0],
                    description: "Fixkosten",
                    category: "Fixkosten",
                    amount: daten.fixkosten || 0
                },
                {
                    id: 2,
                    date: new Date().toISOString().split("T")[0],
                    description: "Variable Kosten",
                    category: "Variable Kosten",
                    amount: daten.variablekosten || 0
                }
            ]
        };
    } catch {
        appState = loadState();
    }

    initFormValues();
    initEvents();
    renderAll();

    console.log(`SpendWise gestartet – ${formatMonth()}`);
}
init();
