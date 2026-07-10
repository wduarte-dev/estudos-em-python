from desafio032 import ContaBancaria
from rich import inspect
def main():
    print(ContaBancaria.__doc__)
    c1 = ContaBancaria('001', 'Wellington', 1000, 'wellington1234')
    while True:
        print('\nO que deseja fazer?\n[1] Sacar\n[2] Depositar\n[3] Saldo atual\n[4] Sair\n[5] Alterar titular')
        cmd = input('> ')
        match cmd:
            case '1':
                saque = float(input('Valor: R$'))
                c1.sacar(saque)
            case '2':
                deposito = float(input('Valor: R$'))
                c1.depositar(deposito)
            case '3':
                print(f'O saldo atual de [{c1.titular.upper()}] é {c1.saldo}.')
            case '4':
                exit()
            case '5':
                c1.titular = None
            case _:
                continue
    

if __name__ == '__main__':
    main()