from myfunctions import list_that
while True:
    try:
        lista = list_that('Digite o peso e a altura, respectivamente, separando-os por espaço: ')
        peso_altura = list(map(float, lista))
        altura = abs(peso_altura[1])
        peso = abs(peso_altura[0])
    except ValueError:
        print('Não digite caracteres que não sejam números! Tente novamente.\n')
        continue
    except IndexError:
        print('Alguma informação ficou faltando! Tente novamente.\n')
        continue
    
    if altura == 0 or peso == 0:
        print('Um dos valores é nulo, tente novamente.\n')
        continue
    
    print('-='*23)
    print(f'Sua altura é {altura} metros e você pesa {peso}kg.')
    print('-='*23)
    
    cmd = input('As informações estão corretas? (s) / (n) ')
    if cmd == 'n':
        print('Reiniciando programa...\n')
        continue
    else:
        IMC = peso/altura**2
        if IMC < 18.5:
            print('-='*20)
            print('Abaixo do peso')
        elif 18.5 <= IMC < 25:
            print('-='*20)
            print('Peso ideal')
        elif 25 <= IMC < 30:
            print('-='*20)
            print('Sobrepeso')
        elif 30 <= IMC < 40:
            print('-='*20)
            print('Obesidade')
        else:
            print('-='*20)
            print('Obesidade mórbida')
    break