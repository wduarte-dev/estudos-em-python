# o usuário digita três números e eu mostro qual é o maior e qual é o menor deles
while True:
    try:
        numeros = input('Digite três números, separando-os por espaço: ').replace(',','.').split()
        if len(numeros) > 3 or len(numeros) < 3:
            print('Fora do limite de números, siga os requisitos!\n')
            continue
        n1 = float(numeros[0])
        n2 = float(numeros[1])
        n3 = float(numeros[2])
    except ValueError:
        print('Entrada inválida, tente novamente.\n')
        continue
    
    if n1 >= n2 and n1 >= n3:
        print(f'Maior -> {n1}')
    elif n2 >= n3 and n2 >= n1:
        print(f'Maior -> {n2}')
    elif n3 >= n1 and n3 >= n2:
        print(f'Maior -> {n3}')
    
    if n1 <= n2 and n1 <= n3:
        print(f'Menor -> {n1}')
    elif n2 <= n3 and n2 <= n1:
        print(f'Menor -> {n2}')
    elif n3 <=n1 and n3 <=n2:
        print(f'Menor -> {n3}')
    break

''' Forma mais resumida:

numeros = input('Digite três numeros, separando-os por espaço').split()
numeros = list(map(float, numeros))
print(f'O maior numero é {max(numeros) e o menor é {min(numeros)}.')
'''