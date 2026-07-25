// =========================================
// Advanced Calculator Dashboard
// =========================================

// Backend URL
const API_BASE = "http://127.0.0.1:8000";

// =========================================
// Theme Toggle
// =========================================

const themeButton = document.getElementById("themeButton");

let darkMode = true;

themeButton.addEventListener("click", () => {

    document.body.classList.toggle("light-mode");

    darkMode = !darkMode;

    if (darkMode) {

        themeButton.innerHTML =
            '<i class="fa-solid fa-moon"></i>';

    } else {

        themeButton.innerHTML =
            '<i class="fa-solid fa-sun"></i>';

    }

});

// =========================================
// Check Backend Connection
// =========================================

async function checkBackend() {

    try {

        const response = await fetch(API_BASE);

        if (!response.ok)
            throw new Error();

        console.log("Backend Connected");

    }

    catch {

        alert("Unable to connect to FastAPI Backend.");

    }

}

checkBackend();

// =========================================
// Load History
// =========================================

async function loadHistory() {

    const historyDiv =
        document.getElementById("historyContainer");

    try {

        const response =
            await fetch(API_BASE + "/history");

        const data = await response.json();

        if (data.history.length === 0) {

            historyDiv.innerHTML =
                "<p>No calculations yet.</p>";

            return;

        }

        historyDiv.innerHTML = "";

        data.history.forEach(item => {

            historyDiv.innerHTML += `

            <div class="history-item">

                <strong>${item.operation}</strong>

                <br>

                ${item.expression}

                <br>

                <span>${item.result}</span>

            </div>

            `;

        });

    }

    catch {

        historyDiv.innerHTML =
            "<p>Unable to load history.</p>";

    }

}

loadHistory();