n = int(input('Digite um número (verificação de números primos): '))
lista = []
for c in range (1, n+1):
    if n % c == 0:
        lista.append(c)
if len(lista) == 2:
    print('O número é primo!')
else:
    print('O número não é primo.')