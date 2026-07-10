from random import choice
from time import sleep
while True:
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    computador = choice(escolhas)
    usuario = int(input('1 -> Pedra ; 2 -> Papel ;  3 -> Tesoura: '))
    if usuario != 1 and usuario != 2 and usuario != 3:
        while True:
            print('\033[31mComando inválido.\033[0m')
            usuario = int(input('1 -> Pedra ; 2 -> Papel ;  3 -> Tesoura: '))
            if usuario == 1 or usuario == 2 or usuario == 3:
                break
            else:
                continue
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!')
    print(f'Máquina: \033[32m{computador}\033[0m')
    sleep(1)
    if usuario == 1 and computador == 'Papel':
        print('-='*15)
        print('Você PERDEU!')
        print('-='*15)
    elif usuario == 1 and computador == 'Pedra':
        print('-='*15)
        print('EMPATE!')
        print('-='*15)
    elif usuario == 2 and computador == 'Tesoura':
        print('-='*15)
        print('Você PERDEU!')
        print('-='*15)
    elif usuario == 2 and computador == 'Papel':
        print('-='*15)
        print('EMPATE!')
        print('-='*15)
    elif usuario == 3 and computador == 'Pedra':
        print('-='*15)
        print('Você PERDEU!')
        print('-='*15)
    elif usuario == 3 and computador == 'Tesoura':
        print('-='*15)
        print('EMPATE!')
        print('-='*15)
    else:
        print('-='*15)
        print('Você GANHOU!')
        print('-='*15)
    input('Pressione ENTER para reiniciar.\n')
    continue
