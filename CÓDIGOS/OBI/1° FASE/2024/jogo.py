'''
ATENÇÃO! NÃO FOI FEITO 100% SOLO, E SIM COM AJUDA DE IA, POIS ERA QUASE IMPOSSÍVEL DE FAZER SOZINHO
NO MEU NÍVEL ATUAL. SE O WELLINGTON DO FUTURO CONSEGUE DE OLHOS FECHADOS, MEUS PARABÉNS, PQ EU FUI HUMILHADO.
'''

from copy import deepcopy
N, Q = [int(n) for n in input().split()]
matriz = []
vizinhos = 0

for _ in range(N):
        lista = []
        linha = input()
        for elemento in linha:
            lista.append(int(elemento))
        matriz.append(lista[:])

for passo in range(Q):
    matriz_seguinte = [[] for _ in range(N)]
    for linha in range(0, N):
        for coluna in range(0, N):
            estado = matriz[linha][coluna]
            for linha_var in range(-1, 2):
                for coluna_var in range(-1, 2):
                    if coluna_var == 0 and linha_var == 0:
                        continue
                    else:
                        linha_vizinho = linha + linha_var
                        coluna_vizinho = coluna + coluna_var
                    if 0 <= coluna_vizinho < N and 0 <= linha_vizinho < N:
                        if matriz[linha_vizinho][coluna_vizinho] == 1:
                            vizinhos += 1
            if estado == 0 and vizinhos == 3:
                estado = 1
            if estado == 0 and vizinhos != 3:
                estado = 0
            if estado == 1 and (vizinhos == 2 or vizinhos == 3):
                estado = 1
            if estado == 1 and vizinhos < 2:
                estado = 0
            if estado == 1 and vizinhos > 3:
                estado = 0
            matriz_seguinte[linha].append(estado)
            vizinhos = 0
    matriz = deepcopy(matriz_seguinte)
for linha in matriz:
    print(''.join(str(celula) for celula in linha))

