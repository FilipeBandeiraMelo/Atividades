/* Exercício 2 - Crie uma função que receba uma string como argumento
   e retorne a mesma string em letras maiúsculas.
   Faça uma chamada à função, passando como parâmetro uma string */
function exibirTexto(texto) {
    return texto.toUpperCase();
}

let resultado = exibirTexto("converter texto minúsculo para maiúsculo");
console.log(resultado);