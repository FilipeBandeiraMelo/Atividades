// // Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro 
// será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
// // 1. Soma
// // 2. Subtração
// // 3. Multiplicação
// // 4. Divisão

// // Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

function operacao(n1, n2, entrada) {
    switch (entrada) {
        case 1: return n1 + n2;
        case 2: return n1 - n2;
        case 3: return n1 * n2;
        case 4: return n1 / n2;
        default: return 0;
    }
}

let resultado = operacao(20, 5, 1);
console.log(resultado);