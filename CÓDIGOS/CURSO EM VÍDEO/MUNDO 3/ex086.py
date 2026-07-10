# matriz = [0]*9
# for i in range(0, 9):
#     matriz[i] = int(input(f'Digite um valor para {i}\n> '))
# for i in range(0, 9, 3):
#     print(matriz[i], matriz[i+1], matriz[i+2])
tamanho = 1
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(1, 4):
    for j in range(1, 4):
        matriz[i-1][j-1] = int(input(f'Digite um valor para ({i}, {j}): '))
        if matriz[i-1][j-1] > tamanho:
            tamanho = matriz[i-1][j-1]
print('-')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^{len(str(tamanho))}}]', end = '')
    print()