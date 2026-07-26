// ==========================================
// Unit Converter
// ==========================================

const API = "http://127.0.0.1:8000";

// ------------------------------------------
// Available Units
// ------------------------------------------

const units = {

    length: [
        "meter",
        "kilometer",
        "centimeter",
        "millimeter",
        "inch",
        "foot",
        "yard",
        "mile"
    ],

    weight: [
        "kilogram",
        "gram",
        "milligram",
        "pound",
        "ounce",
        "ton"
    ],

    temperature: [
        "celsius",
        "fahrenheit",
        "kelvin"
    ],

    area: [
        "square_meter",
        "square_kilometer",
        "acre",
        "hectare"
    ],

    volume: [
        "liter",
        "milliliter",
        "cubic_meter",
        "gallon"
    ],

    time: [
        "second",
        "minute",
        "hour",
        "day",
        "week"
    ],

    speed: [
        "mps",
        "kmph",
        "mph"
    ],

    energy: [
        "joule",
        "calorie",
        "kilowatt_hour"
    ],

    storage: [
        "bit",
        "byte",
        "kb",
        "mb",
        "gb",
        "tb"
    ]

};

// ------------------------------------------
// Load Units
// ------------------------------------------

const category = document.getElementById("category");
const fromUnit = document.getElementById("fromUnit");
const toUnit = document.getElementById("toUnit");

category.addEventListener("change", loadUnits);

window.onload = loadUnits;

function loadUnits() {

    const selected = category.value;

    fromUnit.innerHTML = "";
    toUnit.innerHTML = "";

    units[selected].forEach(unit => {

        let option1 = document.createElement("option");
        option1.value = unit;
        option1.textContent = unit.replaceAll("_", " ");

        let option2 = document.createElement("option");
        option2.value = unit;
        option2.textContent = unit.replaceAll("_", " ");

        fromUnit.appendChild(option1);
        toUnit.appendChild(option2);

    });

}

// ------------------------------------------
// Convert
// ------------------------------------------

async function convertUnit() {

    const value = Number(document.getElementById("value").value);

    if (isNaN(value)) {

        alert("Enter a valid value.");

        return;

    }

    const body = {

        category: category.value,

        from_unit: fromUnit.value,

        to_unit: toUnit.value,

        value: value

    };

    try {

        const response = await fetch(API + "/converter", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(body)

        });

        if (!response.ok) {

            throw new Error("Server Error");

        }

        const result = await response.json();

        document.getElementById("resultBox").innerHTML =

            `
            <h2>${result.result}</h2>
            `;

    }

    catch(error){

        document.getElementById("resultBox").innerHTML =

            `
            <h2>Unable to connect to FastAPI.</h2>
            `;

        console.error(error);

    }

}
