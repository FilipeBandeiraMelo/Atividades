var operacao = '/';

let resultado;
let resto;

function calculadora(n1, n2){

    if (operacao === "+"){
        resultado = n1 + n2;
        console.log(`O resultado da operação é: ${resultado}`);
    } else if (operacao === "-"){
        resultado = n1 - n2;
        console.log(`O resultado da operação é: ${resultado}`);
    } else if (operacao === "*"){
        resultado = n1 * n2;
        console.log(`O resultado da operação é: ${resultado}`);
    } else if (operacao === "/"){
        resultado = n1 / n2;
        resto = n1 % n2;
        console.log(`O resultado da operação é: ${resultado} com resto: ${resto}`);
    }
}

calculadora(30, 13);