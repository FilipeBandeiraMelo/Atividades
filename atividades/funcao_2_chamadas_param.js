/* Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. 
   Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada, com 4 elementos */

function fn(a, lista) {
    console.log(a);
    if (lista === true) {
        console.log(lista);
    }
}

fn(a = 100);
fn(lista = [1, 2, 3, 4]);
