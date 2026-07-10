class ContaBancaria:
    '''
    Sistema de saques e depósitos simples.
    Instância: ContaBancaria(id, titular, saldo)
    '''
    def __init__(self, id, titular, saldo):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Saque autorizado.')
            return
        print('\033[31mSALDO INSUFICIENTE\033[0m')

    def depositar(self, valor):
        self.saldo += valor
        print('Depósito autorizado.')

    def __str__(self):
        return f'O titular {self.titular} de id {self.id} possui R${self.saldo:.2f} na conta.'
        
print(ContaBancaria.__doc__)
c1 = ContaBancaria('001', 'Wellington', 1000)
while True:
    print(f'\n{c1}')
    print('O que deseja fazer?\n[1] Sacar\n[2] Depositar\n[3] Sair')
    cmd = input('> ')
    if cmd == '1':
        saque = float(input('Valor: R$'))
        c1.sacar(saque)
    elif cmd == '2':
        deposito = float(input('Valor: R$'))
        c1.depositar(deposito)
    else:
        break