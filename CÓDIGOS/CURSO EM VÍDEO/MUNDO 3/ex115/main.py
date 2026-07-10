from rich.panel import Panel as Painel
from rich.align import Align
from rich import print
from time import sleep
from cadastro import *
from tabela import *
from verificador import check
def menu():
    check()
    boas_vindas = Painel('Bem-vindo(a) ao sistema de cadastro!', width=40)
    print(Align.center(boas_vindas))
    while True:
        comandos = Painel('''[1] Cadastrar uma nova pessoa;
[2] Visualizar tabela de cadastrados;
[3] Sair do programa.''')
        print(comandos)
        try:
            cmd = input()
        except KeyboardInterrupt:
            print('\n[red]Fechando...[/]')
            exit()
        if cmd == '1':
            cadastrar_pessoa()
            sleep(1)
        elif cmd == '2':
            exibir_tabela()
            sleep(1)
        elif cmd == '3':
            sleep(1)
            print('[red]Fechando...[/]')
            exit()
        else:
            print('[red]Comando inválido.[/]')

if __name__ == '__main__':
    menu()
