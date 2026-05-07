// Write the function below
function calculate() {
    let res = 0
    for (let i = 1; i <= 10000; i++) {
        res += i;
    }
    console.log(res)
}

let n = 5; // Don't change this line

// Execute your function n times with a loop
for (let i = 0; i < n; i++) {
    calculate()
}

/*Escribe una función llamada printMessage que:

Imprime el mensaje: "This is a reusable function!".
Llama a la función printMessage 3 veces en tu programa. */

function printMessage() {
    console.log("This is a reusable function!")
}

printMessage()
printMessage()
printMessage()