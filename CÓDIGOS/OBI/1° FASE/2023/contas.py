saldo = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())
counter = 0
lista = []
lista.append(n1)
lista.append(n2)
lista.append(n3)
for conta in sorted(lista):
    saldo -= conta
    if saldo >= 0:
        counter += 1
print(counter)
