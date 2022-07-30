// Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir. 
// Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”.

// Não é necessário, mas, caso deseje tornar o sistema mais realista para que o tempo realmente passe em segundos, 
// você pode usar a função time.sleep() que existe na Python (acesse o link em anexo). No entanto, é preciso adicionar uma biblioteca antes de executá-la. 

function sleep(ms) {
    return new Promise(
        resolve => setTimeout(resolve, ms)
    );
}

async function delayedGreeting() {
    console.log("iniciando contagem regressiva");
    await sleep(2000)
    for (let i = 5; i >= 1; i--) {
        await sleep(1000)
        console.log(i);
    }
    await sleep(1000)
    console.log("BUM!!!");
}

delayedGreeting();

//A sugestão da atividade era fazer em python com a função time.sleep(), porém decidi converter para javascript que é a linguagem estudada no curso.
