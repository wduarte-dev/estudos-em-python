N = int(input())
lista = [0]
for _ in range(N):
    var1 = len(lista)
    for indice, numero in enumerate(lista):
        if indice % 2 == 0:
            print('0', end = '')
        else:
            print('1', end = '')
    print()
    lista.append(0)
    lista.append(0)