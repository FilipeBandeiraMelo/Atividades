// Crie um programa que contenha os seguintes tipos de funções:

// 1. uma função tradicional com a palavra reservada “Function” e sem nenhum parâmetro;
function exibirHoraAtual(){
    console.log(new Date() .getHours());
}
exibirHoraAtual();
//2. uma função tradicional com parâmetros e um retorno de valor;
function soma(a,b){
    return a+b;
}
console.log(soma(3,5));
//3. uma arrow function com parâmetros e que retorne um valor.
const multiplica = (n1,n2) => n1*n2;
console.log(multiplica(3,3));
