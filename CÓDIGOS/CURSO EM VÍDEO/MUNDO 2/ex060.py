while True:
    try:
        n = int(input('Número inteiro: '))
        break
    except ValueError:
        print('Digite um número válido.\n')
        continue

digit = n
result = 1
while n != 1:
    if n == 0:
        print('0! (fatorial) é igual a 1.')
        break
    elif n < 0: 
        print('Fatorial não é definido para números negativos.')
        break
    result *= n
    n -= 1
if n > 0:
    print(f'{digit}! (fatorial) é igual a {result}.')