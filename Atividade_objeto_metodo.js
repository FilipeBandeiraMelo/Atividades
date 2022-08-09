const cliente = {
    nome: 'André',
    idade: 36,
    cpf: '12543652266',
    email: 'andre@email.com',
    fones: ['5591235498', '5521988743124'],
    saldo: 200,
    mostrarSaldo: function (valor) {
        let showSaldo = valor
        console.log(`saldo inicial: ${showSaldo} reais`);
        return
    },
    depositar: function (valor) {
        this.saldo += valor;
    },
    sacar: function (valor) {
        this.saldo -= valor;
    }
}

cliente.mostrarSaldo(cliente.saldo);
cliente.depositar(30);
console.log(`saldo pós depósito de 30 reais: ${cliente.saldo}`);
cliente.sacar(100);
console.log(`saldo pós saque de 100 reais: ${cliente.saldo}`);



