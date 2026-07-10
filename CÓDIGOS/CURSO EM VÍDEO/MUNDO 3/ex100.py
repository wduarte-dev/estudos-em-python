from time import sleep
from random import choices
def sorteio(*args):
    sorteio = []
    print('Sorteando valores... ', end = ' ', flush = True)
    sleep(0.5)
    for c in range(5):
        num = choices(args, k = 1)[0]
        sorteio.append(num)
        sleep(0.5)
        print(num, end = ' ', flush = True)
    return sorteio
def somaPar(resultado):
    pares = []
    s = 0
    for num in resultado:
        if num % 2 == 0:
            pares.append(num)
    for par in pares:
        s += par
    sleep(1)
    if len(pares) != 0:
        print('\nA soma dos pares', end = ' ')
        print(*pares, sep = ', ', end = ' ')
        print(f'é {s}')
    else:
        print('\nNão há nenhum par a ser somado.')

resultado = sorteio(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
somaPar(resultado)
