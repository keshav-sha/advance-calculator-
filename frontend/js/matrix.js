// ==========================================
// Matrix Calculator
// ==========================================

const API = "http://127.0.0.1:8000";

const matrixA = document.getElementById("matrixA");
const matrixB = document.getElementById("matrixB");
const resultMatrix = document.getElementById("resultMatrix");
const matrixSize = document.getElementById("matrixSize");
const generateBtn = document.getElementById("generateBtn");

// ==========================================
// Generate Matrix Inputs
// ==========================================

generateBtn.addEventListener("click", generateMatrices);

window.onload = generateMatrices;

function generateMatrices() {

    const size = parseInt(matrixSize.value);

    matrixA.innerHTML = "";
    matrixB.innerHTML = "";
    resultMatrix.innerHTML = "";

    matrixA.style.gridTemplateColumns = `repeat(${size},65px)`;
    matrixB.style.gridTemplateColumns = `repeat(${size},65px)`;
    resultMatrix.style.gridTemplateColumns = `repeat(${size},65px)`;

    for (let i = 0; i < size * size; i++) {

        const inputA = document.createElement("input");
        inputA.type = "number";
        inputA.value = 0;
        matrixA.appendChild(inputA);

        const inputB = document.createElement("input");
        inputB.type = "number";
        inputB.value = 0;
        matrixB.appendChild(inputB);

    }

}
// ==========================================
// Read Matrix
// ==========================================

function getMatrix(container) {

    const size = parseInt(matrixSize.value);

    const inputs = container.querySelectorAll("input");

    let matrix = [];

    let index = 0;

    for (let i = 0; i < size; i++) {

        let row = [];

        for (let j = 0; j < size; j++) {

            row.push(Number(inputs[index].value));

            index++;

        }

        matrix.push(row);

    }

    return matrix;

}
// ==========================================
// Show Result
// ==========================================

function showMatrix(matrix){

    resultMatrix.innerHTML="";

    const size = matrix.length;

    resultMatrix.style.gridTemplateColumns =
        `repeat(${size},65px)`;

    matrix.forEach(row=>{

        row.forEach(value=>{

            const input =
                document.createElement("input");

            input.value=value;

            input.readOnly=true;

            resultMatrix.appendChild(input);

        });

    });

}
// ==========================================
// API Request
// ==========================================

async function send(endpoint,data){

    try{

        const response = await fetch(API+endpoint,{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify(data)

        });

        const result = await response.json();

        return result;

    }

    catch{

        alert("Backend not running.");

    }

}
async function addMatrix(){

    const result = await send(

        "/matrix/add",

        {

            matrix1:getMatrix(matrixA),

            matrix2:getMatrix(matrixB)

        }

    );

    showMatrix(result.result);

}
async function subtractMatrix(){

    const result = await send(

        "/matrix/subtract",

        {

            matrix1:getMatrix(matrixA),

            matrix2:getMatrix(matrixB)

        }

    );

    showMatrix(result.result);

}
async function multiplyMatrix(){

    const result = await send(

        "/matrix/multiply",

        {

            matrix1:getMatrix(matrixA),

            matrix2:getMatrix(matrixB)

        }

    );

    showMatrix(result.result);

}
async function transposeMatrix(){

    const result = await send(

        "/matrix/transpose",

        {

            matrix:getMatrix(matrixA)

        }

    );

    showMatrix(result.result);

}
async function determinantMatrix(){

    const result = await send(

        "/matrix/determinant",

        {

            matrix:getMatrix(matrixA)

        }

    );

    resultMatrix.innerHTML =

        "<h2>"+result.result+"</h2>";

}
async function inverseMatrix(){

    const result = await send(

        "/matrix/inverse",

        {

            matrix:getMatrix(matrixA)

        }

    );

    showMatrix(result.result);

}
async function identityMatrix(){

    const size = parseInt(matrixSize.value);

    const result = await send(

        "/matrix/identity",

        {

            size:size

        }

    );

    showMatrix(result.result);

}
async function scalarMultiply(){

    const scalar = Number(

        prompt("Enter Scalar Value")

    );

    if(isNaN(scalar)) return;

    const result = await send(

        "/matrix/scalar",

        {

            matrix:getMatrix(matrixA),

            scalar:scalar

        }

    );

    showMatrix(result.result);

}