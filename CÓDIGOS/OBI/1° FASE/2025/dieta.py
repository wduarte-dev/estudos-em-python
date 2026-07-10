lista2 = 0
lista = input().split(' ')
lista[0] = int(lista[0])
lista[1] = int(lista[1])
total = 0
for c in range(0, lista[0]):
    lista2 = input().split(' ')
    total += int(lista2[0])*4 + int(lista2[1])*9 + int(lista2[2])*4
maximo = lista[1] - total
print(maximo)
