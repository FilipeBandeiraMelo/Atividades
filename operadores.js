let nota1 = 7
let nota2 = 7
let nota3 = 5

let media = (nota1 + nota2 + nota3) / 3
let resultado = media >= 7 ? "Aprovado" : "Reprovado"
console.log(resultado)

let notaParaAprovacao = (21 - nota1 - nota2)
if (notaParaAprovacao > 10){
    console.log("O aluno já foi reprovado por média")
} else {
    console.log(`O aluno precisa tirar ${notaParaAprovacao} na próxima prova para ser Aprovado`);
}


