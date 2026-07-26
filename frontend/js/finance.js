// ==========================================
// Financial Calculator
// ==========================================

const API = "http://127.0.0.1:8000";

// ==========================================
// Read Input
// ==========================================

function getInputData() {

    return {

        principal: Number(document.getElementById("principal").value),

        rate: Number(document.getElementById("rate").value),

        time: Number(document.getElementById("time").value),

        monthly_investment: Number(document.getElementById("monthlyInvestment").value)

    };

}

// ==========================================
// Display Result
// ==========================================

function showResult(data) {

    const box = document.getElementById("resultBox");

    if (typeof data === "object") {

        box.innerHTML = "<pre>" +
            JSON.stringify(data, null, 2) +
            "</pre>";

    } else {

        box.innerHTML = `<h2>${data}</h2>`;

    }

}

// ==========================================
// API Request
// ==========================================

async function sendRequest(endpoint, body) {

    try {

        const response = await fetch(API + endpoint, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(body)

        });

        if (!response.ok) {

            throw new Error("Unable to connect.");

        }

        const data = await response.json();

        showResult(data);

    }

    catch (error) {

        showResult("❌ Backend Error");

        console.error(error);

    }

}

// ==========================================
// Main Calculator
// ==========================================

function calculateFinance() {

    const type = document.getElementById("calculatorType").value;

    const data = getInputData();

    switch(type){

        case "simple_interest":

            sendRequest("/finance/simple-interest", data);

            break;

        case "compound_interest":

            sendRequest("/finance/compound-interest", data);

            break;

        case "emi":

            sendRequest("/finance/emi", data);

            break;

        case "loan":

            sendRequest("/finance/loan", data);

            break;

        case "sip":

            sendRequest("/finance/sip", data);

            break;

        case "fd":

            sendRequest("/finance/fd", data);

            break;

        case "roi":

            sendRequest("/finance/roi", data);

            break;

        case "cagr":

            sendRequest("/finance/cagr", data);

            break;

        default:

            alert("Unknown calculator type.");

    }

}