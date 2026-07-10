numeros = [[], []]
for c in range (0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else: 
        numeros[1].append(n)
print(f'''Pares: {sorted(numeros[0])}
Ímpares: {sorted(numeros[1])}
''')

    