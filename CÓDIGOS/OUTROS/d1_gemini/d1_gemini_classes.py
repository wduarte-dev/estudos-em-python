class ContaBancaria:
    def __init__(self, titular): # Aqui é o Método Construtor, ele será executado e atribuirá atributos ao objeto quando instanciado através do dunder init
        self.titular = titular
        self.saldo = 0
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor

Conta1 = ContaBancaria('Larinha')
Conta1.depositar(100)
Conta1.sacar(30)
print(f'{Conta1.titular} tem R${Conta1.saldo:.2f}')