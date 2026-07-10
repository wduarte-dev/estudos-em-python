from random import randint
wins = 0
while True:
    n_pc = randint(0, 10)
    print('-'*26)
    user = input('Ímpar ou par [I/P]:\n> ').upper()
    n_user = int(input('Número de 0 a 10:\n> '))
    print('-'*26)
    print('\n'+'-='*26)
    if user == 'P' and (n_pc + n_user) % 2 == 0:
        wins += 1
        print(f'Você venceu!\nComputador: {n_pc} //> Soma: {n_pc + n_user}\nReiniciando...')
    elif user == 'I' and (n_pc + n_user) % 2 != 0:
        wins += 1
        print(f'Você venceu!\nComputador: {n_pc} // Soma: {n_pc + n_user}\nReiniciando...')
    else:
        print(f'Você perdeu!\nComputador: {n_pc} // Soma: {n_pc + n_user}\nVitórias consecutivas: {wins}')
        print('-='*26+'\n')
        break
    print('-='*26+'\n')