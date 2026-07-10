class ContaBancaria:
    '''
    Sistema de saques e depósitos simples.
    Instância: ContaBancaria(id, titular, saldo)
    '''
    def __init__(self, id, titular, saldo):
        self.id = id # Atributo público
        self._titular = titular # Atributo protegido
        self.__saldo = saldo # Atributo privado

    def sacar(self, valor):
        if self.__saldo >= abs(valor):
            self.__saldo -= abs(valor)
            print('Saque autorizado.')
            return None
        print('\033[31m__saldo INSUFICIENTE\033[0m')

    def depositar(self, valor):
        self.__saldo += abs(valor)
        print('Depósito autorizado.')

    def __str__(self):
        return f'{self.__dict__}'
        
print(ContaBancaria.__doc__)
c1 = ContaBancaria('001', 'Wellington', 1000)

print(c1)

''' Sistema desativado para exibição da visibilidade dos atributos
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
'''