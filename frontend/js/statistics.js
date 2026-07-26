// ===========================================
// Statistics Calculator
// ===========================================

const API = "http://127.0.0.1:8000";

// ===========================================
// Read Input
// ===========================================

function getNumbers() {

    const text = document.getElementById("numbers").value.trim();

    if (text === "") {

        alert("Please enter some numbers.");

        return null;

    }

    const numbers = text
        .split(",")
        .map(item => Number(item.trim()))
        .filter(item => !isNaN(item));

    if (numbers.length === 0) {

        alert("Invalid input.");

        return null;

    }

    return numbers;

}

// ===========================================
// Show Result
// ===========================================

function showResult(value) {

    document.getElementById("resultBox").innerHTML = value;

}

// ===========================================
// Send Request
// ===========================================

async function calculate(endpoint, body) {

    try {

        const response = await fetch(API + endpoint, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(body)

        });

        if (!response.ok) {

            throw new Error("Server Error");

        }

        const data = await response.json();

        showResult(data.result);

    }

    catch (error) {

        showResult("Unable to connect to FastAPI.");

    }

}

// ===========================================
// Statistics Functions
// ===========================================

function mean() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/mean", { numbers });

}

function median() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/median", { numbers });

}

function mode() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/mode", { numbers });

}

function variance() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/variance", { numbers });

}

function stdDeviation() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/std", { numbers });

}

function minimum() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/min", { numbers });

}

function maximum() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/max", { numbers });

}

function sum() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/sum", { numbers });

}

function count() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/count", { numbers });

}

function range() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/range", { numbers });

}

function quartiles() {

    const numbers = getNumbers();

    if (numbers)
        calculate("/statistics/quartiles", { numbers });

}

function percentile() {

    const numbers = getNumbers();

    if (!numbers)
        return;

    const p = prompt("Enter Percentile (0-100)");

    if (p === null)
        return;

    calculate("/statistics/percentile", {

        numbers: numbers,

        percentile: Number(p)

    });

}

// ===========================================
// Keyboard Shortcut
// ===========================================

document.addEventListener("keydown", function (event) {

    if (event.ctrlKey && event.key === "Enter") {

        mean();

    }

});