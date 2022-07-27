/* Exercício 3 - Crie uma função que receba como parâmetro
   uma lista de 4 elementos, adicione 2 elementos a lista e
   imprima a lista */

function nomeLista(n1) {
    return n1.push(5, 6)
}
let lista = [1, 2, 3, 4];
nomeLista(lista)
console.log(lista);
