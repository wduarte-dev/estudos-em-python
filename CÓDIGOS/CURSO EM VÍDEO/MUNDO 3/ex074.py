counter = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
numeros = (n1, n2, n3, n4)
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')
while True:
    try:
        print(f'O primeiro valor 3 está na posição {numeros.index(3) + 1}')
        break
    except: 
        print((f'O número 3 não foi digitado.'))
        break
print('Os números pares digitados foram: ', end = '')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end = ' ')
    else: 
        counter += 1
    if counter == 4:
        print('Nenhum número par foi digitado.')
