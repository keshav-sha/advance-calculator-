const API="http://127.0.0.1:8000";

const display=document.getElementById("display");

let memory=0;

function setValue(v){

display.value=v;

}

async function send(endpoint,value){

const response=await fetch(API+endpoint,{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

value:value

})

});

const data=await response.json();

setValue(data.result);

}

function sin(){

send("/scientific/sin",Number(display.value));

}

function cos(){

send("/scientific/cos",Number(display.value));

}

function tan(){

send("/scientific/tan",Number(display.value));

}

function log10(){

send("/scientific/log",Number(display.value));

}

function ln(){

send("/scientific/ln",Number(display.value));

}

function sqrt(){

send("/scientific/sqrt",Number(display.value));

}

function factorial(){

send("/scientific/factorial",Number(display.value));

}

async function pi(){

const response=await fetch(API+"/scientific/pi");

const data=await response.json();

setValue(data.result);

}

async function euler(){

const response=await fetch(API+"/scientific/e");

const data=await response.json();

setValue(data.result);

}

function clearDisplay(){

display.value="";

}

function memoryAdd(){

memory+=Number(display.value);

}

function memorySubtract(){

memory-=Number(display.value);

}

function memoryRecall(){

display.value=memory;

}

function memoryClear(){

memory=0;

}

function power(){

const exponent=prompt("Enter Power");

if(exponent==null)return;

fetch(API+"/power",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

a:Number(display.value),

b:Number(exponent)

})

})

.then(res=>res.json())

.then(data=>{

display.value=data.result;

});

}