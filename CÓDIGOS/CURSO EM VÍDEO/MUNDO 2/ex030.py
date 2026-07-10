while True:
    try:
        numero = int(input('Digite um número inteiro: '))
    except:
        print('Dígito inválido, tente novamente.\n')
        continue
    
    if numero%2 == 0:
        print('O número é par.')
        break
    else:
        print('O número é impar.')
        break