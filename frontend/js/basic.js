// ======================================
// Advanced Calculator - Basic Calculator
// ======================================

const API_BASE = "http://127.0.0.1:8000";

const display = document.getElementById("display");

let currentExpression = "";

// ======================================
// Display Functions
// ======================================

function append(value) {
    currentExpression += value;
    display.value = currentExpression;
}

function clearDisplay() {
    currentExpression = "";
    display.value = "";
}

function deleteLast() {
    currentExpression = currentExpression.slice(0, -1);
    display.value = currentExpression;
}

// ======================================
// Backend Request
// ======================================

async function sendRequest(endpoint, body) {

    try {

        const response = await fetch(API_BASE + endpoint, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(body)

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Calculation failed.");
        }

        return data.result;

    } catch (error) {

        alert(error.message);

        return null;

    }

}

// ======================================
// Calculate
// ======================================

async function calculate() {

    if (currentExpression.trim() === "") {
        return;
    }

    let operator = null;

    if (currentExpression.includes("+")) {

        operator = "+";

    } else if (currentExpression.includes("-")) {

        operator = "-";

    } else if (currentExpression.includes("*")) {

        operator = "*";

    } else if (currentExpression.includes("/")) {

        operator = "/";

    } else {

        alert("Unsupported expression.");
        return;

    }

    const values = currentExpression.split(operator);

    if (values.length !== 2) {

        alert("Invalid expression.");
        return;

    }

    const a = parseFloat(values[0]);

    const b = parseFloat(values[1]);

    if (isNaN(a) || isNaN(b)) {

        alert("Please enter valid numbers.");

        return;

    }

    let endpoint = "";

    switch (operator) {

        case "+":
            endpoint = "/add";
            break;

        case "-":
            endpoint = "/subtract";
            break;

        case "*":
            endpoint = "/multiply";
            break;

        case "/":
            endpoint = "/divide";
            break;

    }

    const result = await sendRequest(endpoint, {
        a: a,
        b: b
    });

    if (result !== null) {

        currentExpression = result.toString();

        display.value = currentExpression;

    }

}

// ======================================
// Keyboard Support
// ======================================

document.addEventListener("keydown", function (event) {

    const key = event.key;

    if ("0123456789".includes(key)) {

        append(key);

    }

    else if (key === ".") {

        append(".");

    }

    else if (key === "+") {

        append("+");

    }

    else if (key === "-") {

        append("-");

    }

    else if (key === "*") {

        append("*");

    }

    else if (key === "/") {

        append("/");

    }

    else if (key === "Enter") {

        event.preventDefault();

        calculate();

    }

    else if (key === "Backspace") {

        deleteLast();

    }

    else if (key === "Escape") {

        clearDisplay();

    }

});

// ======================================
// Backend Status Check
// ======================================

async function checkBackend() {

    try {

        const response = await fetch(API_BASE);

        if (response.ok) {

            console.log("✅ Backend Connected");

        }

    }

    catch {

        console.log("❌ Backend Not Running");

    }

}

checkBackend();

// ======================================
// Advanced Operations
// ======================================

async function square() {

    const value = parseFloat(display.value);

    if (isNaN(value)) {
        alert("Enter a valid number.");
        return;
    }

    const result = await sendRequest("/square", {
        value: value
    });

    if (result !== null) {
        currentExpression = result.toString();
        display.value = currentExpression;
    }
}

async function cube() {

    const value = parseFloat(display.value);

    if (isNaN(value)) {
        alert("Enter a valid number.");
        return;
    }

    const result = await sendRequest("/cube", {
        value: value
    });

    if (result !== null) {
        currentExpression = result.toString();
        display.value = currentExpression;
    }
}

async function sqrt() {

    const value = parseFloat(display.value);

    if (isNaN(value)) {
        alert("Enter a valid number.");
        return;
    }

    const result = await sendRequest("/scientific/sqrt", {
        value: value
    });

    if (result !== null) {
        currentExpression = result.toString();
        display.value = currentExpression;
    }
}
async function percentage() {

    const input = prompt("Enter percentage value (Example: 25 for 25%)");

    if (input === null) return;

    const percent = parseFloat(input);

    const number = parseFloat(display.value);

    if (isNaN(number) || isNaN(percent)) {
        alert("Invalid input.");
        return;
    }

    const result = await sendRequest("/percentage", {
        a: number,
        b: percent
    });

    if (result !== null) {
        currentExpression = result.toString();
        display.value = currentExpression;
    }

}
async function power() {

    const exponent = prompt("Enter Power");

    if (exponent === null) return;

    const base = parseFloat(display.value);

    if (isNaN(base) || isNaN(exponent)) {

        alert("Invalid number.");

        return;

    }

    const result = await sendRequest("/power", {

        a: base,

        b: parseFloat(exponent)

    });

    if (result !== null) {

        currentExpression = result.toString();

        display.value = currentExpression;
        loadHistory();

    }

}
// ======================================
// Memory Functions
// ======================================

let memory = 0;

function memoryStore() {

    memory = parseFloat(display.value) || 0;

    alert("Stored in Memory");

}

function memoryRecall() {

    display.value = memory;

    currentExpression = memory.toString();

}

function memoryClear() {

    memory = 0;

    alert("Memory Cleared");

}

function memoryAdd() {

    memory += parseFloat(display.value) || 0;

    alert("Memory Updated");

}

function memorySubtract() {

    memory -= parseFloat(display.value) || 0;

    alert("Memory Updated");


} 
// =====================================
// Load History
// =====================================

async function loadHistory(){

    const historyDiv =
        document.getElementById("historyList");

    try{

        const response =
            await fetch(API_BASE + "/history");

        const data =
            await response.json();

        historyDiv.innerHTML="";

        if(data.history.length===0){

            historyDiv.innerHTML=
                "<p>No calculations.</p>";

            return;

        }

        data.history.forEach(item=>{

            historyDiv.innerHTML += `

                <div class="history-item">

                    <strong>${item.operation}</strong>

                    <br>

                    ${item.expression}

                    <br>

                    <span>= ${item.result}</span>

                </div>

            `;

        });

    }

    catch{

        historyDiv.innerHTML=
            "<p>Unable to load history.</p>";

    }

}

loadHistory();
async function clearHistory(){

    await fetch(API_BASE + "/history",{

        method:"DELETE"

    });

    loadHistory();

}
showToast("Stored in Memory");  
function showToast(message){

    const toast =
        document.getElementById("toast");

    toast.innerHTML=message;

    toast.classList.add("show");

    setTimeout(()=>{

        toast.classList.remove("show");

    },2500);


}
document.querySelectorAll("button")
.forEach(button=>{

    button.addEventListener("click",()=>{

        button.style.transform="scale(.92)";

        setTimeout(()=>{

            button.style.transform="scale(1)";

        },120);

    });

});