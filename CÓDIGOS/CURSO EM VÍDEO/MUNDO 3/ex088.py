from random import randint
from time import sleep
jogos = int(input('Digite o número de jogos: '))
lista = []
sorteio = []
for jogo in range(0, jogos):
    for numero in range(0, 6):
        n = randint(1, 60)
        while n in sorteio:
            n = randint(1, 60)
        sorteio.append(n)
    lista.append(sorteio[:])
    sorteio.clear()
sleep(1)
print('-'*30)
for c in range(0, jogos):
    print(f'Jogo {c+1}: {lista[c]}')
    sleep(1)
print('-'*30)