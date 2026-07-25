const API = "http://127.0.0.1:8000";

function getNumbers(){

    return {

        a: Number(document.getElementById("number1").value),

        b: Number(document.getElementById("number2").value)

    };

}

function showResult(value){

    document.getElementById("result").innerHTML=value;

}

async function send(endpoint,data){

    try{

        const response=await fetch(API+endpoint,{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify(data)

        });

        const result=await response.json();

        if(result.result!==undefined){

            showResult(result.result);

        }

        else if(result.detail){

            alert(result.detail);

        }

    }

    catch(error){

        alert("Cannot connect to FastAPI backend.");

    }

}

function add(){

    send("/add",getNumbers());

}

function subtract(){

    send("/subtract",getNumbers());

}

function multiply(){

    send("/multiply",getNumbers());

}

function divide(){

    send("/divide",getNumbers());

}

function percentage(){

    send("/percentage",getNumbers());

}

function square(){

    const value=Number(document.getElementById("number1").value);

    send("/square",{value:value});

}

function cube(){

    const value=Number(document.getElementById("number1").value);

    send("/cube",{value:value});

}

function sqrt(){

    const value=Number(document.getElementById("number1").value);

    send("/scientific/sqrt",{value:value});

}
