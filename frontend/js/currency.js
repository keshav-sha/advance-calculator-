// ==========================================
// Currency Converter
// ==========================================

const API = "http://127.0.0.1:8000";

// ==========================================
// Convert Currency
// ==========================================

async function convertCurrency() {

    const amount = Number(document.getElementById("amount").value);

    const from = document.getElementById("fromCurrency").value;

    const to = document.getElementById("toCurrency").value;

    if (isNaN(amount) || amount <= 0) {

        alert("Please enter a valid amount.");

        return;

    }

    const body = {

        amount: amount,

        from_currency: from,

        to_currency: to

    };

    try {

        const response = await fetch(API + "/currency/convert", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(body)

        });

        if (!response.ok) {

            throw new Error("Currency conversion failed.");

        }

        const data = await response.json();

        document.getElementById("resultBox").innerHTML = `

            <h2>${amount} ${from}</h2>

            <h3>=</h3>

            <h2>${data.result} ${to}</h2>

            <br>

            <p>Exchange Rate : ${data.rate}</p>

        `;

    }

    catch (error) {

        document.getElementById("resultBox").innerHTML =

            "<h2>Unable to connect to backend.</h2>";

        console.error(error);

    }

}

// ==========================================
// Swap Currency
// ==========================================

function swapCurrencies() {

    const from = document.getElementById("fromCurrency");

    const to = document.getElementById("toCurrency");

    const temp = from.value;

    from.value = to.value;

    to.value = temp;

}

// ==========================================
// Auto Convert on Enter
// ==========================================

document.addEventListener("keydown", function(event){

    if(event.key==="Enter"){

        convertCurrency();

    }

});