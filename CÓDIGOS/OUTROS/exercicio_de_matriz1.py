# crie uma matriz aleatória linha (5-15) e coluna (5-15) em que seus índices ímpares representem 1 e os pares 0, invertendo a lógica a cada linha
from random import randint
from rich import print
coluna = randint(5, 15)
linha = randint(5, 15)
counter = 0
linha_counter = 0

matriz = [['0' for _ in range(coluna)] for _ in range(linha)]

for linha in matriz:
    for indice, numero in enumerate(linha):
        if linha_counter % 2 == 0:
            if indice % 2 == 0:
                matriz[counter][indice] = '0'
            else:
                matriz[counter][indice] = '1'
        else:
            if indice % 2 == 0:
                matriz[counter][indice] = '1'
            else:
                matriz[counter][indice] = '0'
    counter += 1
    linha_counter += 1


for linha in matriz:
    print(' '.join(linha))