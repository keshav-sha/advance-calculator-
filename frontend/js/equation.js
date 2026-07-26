// ==========================================
// Equation Solver
// ==========================================

const API = "http://127.0.0.1:8000";

const equationType =
document.getElementById("equationType");

const dynamicInputs =
document.getElementById("dynamicInputs");

// ==========================================
// Change Input Fields
// ==========================================

equationType.addEventListener(
    "change",
    loadInputs
);

window.onload = loadInputs;

function loadInputs(){

    const type = equationType.value;

    dynamicInputs.innerHTML="";

    if(type==="linear"){

        dynamicInputs.innerHTML=`

        <div class="group">
            <label>a</label>
            <input type="number" id="a">
        </div>

        <div class="group">
            <label>b</label>
            <input type="number" id="b">
        </div>

        `;

    }

    else if(type==="quadratic"){

        dynamicInputs.innerHTML=`

        <div class="group">
            <label>a</label>
            <input type="number" id="a">
        </div>

        <div class="group">
            <label>b</label>
            <input type="number" id="b">
        </div>

        <div class="group">
            <label>c</label>
            <input type="number" id="c">
        </div>

        `;

    }

    else if(type==="polynomial"){

        dynamicInputs.innerHTML=`

        <div class="group">
            <label>Coefficients</label>

            <input
            type="text"
            id="coefficients"
            placeholder="Example: 1,-6,11,-6">

        </div>

        `;

    }

    else{

        dynamicInputs.innerHTML=`

        <div class="group">
            <label>a₁</label>
            <input type="number" id="a1">
        </div>

        <div class="group">
            <label>b₁</label>
            <input type="number" id="b1">
        </div>

        <div class="group">
            <label>c₁</label>
            <input type="number" id="c1">
        </div>

        <div class="group">
            <label>a₂</label>
            <input type="number" id="a2">
        </div>

        <div class="group">
            <label>b₂</label>
            <input type="number" id="b2">
        </div>

        <div class="group">
            <label>c₂</label>
            <input type="number" id="c2">
        </div>

        `;

    }

}

// ==========================================
// Solve Equation
// ==========================================

async function solveEquation(){

    const type = equationType.value;

    let endpoint="";

    let body={};

    if(type==="linear"){

        endpoint="/equation/linear";

        body={

            a:Number(document.getElementById("a").value),

            b:Number(document.getElementById("b").value)

        };

    }

    else if(type==="quadratic"){

        endpoint="/equation/quadratic";

        body={

            a:Number(document.getElementById("a").value),

            b:Number(document.getElementById("b").value),

            c:Number(document.getElementById("c").value)

        };

    }

    else if(type==="polynomial"){

        endpoint="/equation/polynomial";

        body={

            coefficients:
            document.getElementById("coefficients")
            .value
            .split(",")
            .map(Number)

        };

    }

    else{

        endpoint="/equation/simultaneous";

        body={

            a1:Number(document.getElementById("a1").value),

            b1:Number(document.getElementById("b1").value),

            c1:Number(document.getElementById("c1").value),

            a2:Number(document.getElementById("a2").value),

            b2:Number(document.getElementById("b2").value),

            c2:Number(document.getElementById("c2").value)

        };

    }

    try{

        const response = await fetch(API+endpoint,{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify(body)

        });

        if(!response.ok){

            throw new Error("Server Error");

        }

        const result = await response.json();

        showResult(result);

    }

    catch(error){

        document.getElementById("resultBox")
        .innerHTML=

        `
        <h2>Unable to solve equation.</h2>
        `;

        console.error(error);

    }

}

// ==========================================
// Display Result
// ==========================================

function showResult(result){

    const box =
    document.getElementById("resultBox");

    box.innerHTML="";

    if(typeof result==="object"){

        box.innerHTML=

        `
        <pre>

${JSON.stringify(result,null,4)}

        </pre>

        `;

    }

    else{

        box.innerHTML=

        `<h2>${result}</h2>`;

    }

}