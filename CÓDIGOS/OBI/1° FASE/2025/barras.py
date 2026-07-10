lista = []
colunas = int(input())
numeros = input().split()
numeros = list(map(int, numeros))
linhas = max(numeros)
for c in range(0, linhas):
    lista.append(list(0 for n in range(0, colunas)))
for pos, numero in enumerate(numeros):
    coluna = -1
    elemento = pos
    while numero > 0:
        lista[coluna][elemento] = 1
        numero -= 1
        coluna -= 1
for c in range(0, linhas):
    print(*lista[c])