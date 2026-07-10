import math

while True:
    try:
        area = input('\nDigite a área em m²: ')
        area = area.replace(',' , '.')
        area = float(area)
        if area > 1e5:
            input('O valor é extremamente alto. Deseja continuar? ')
        if area <=0:
            print('Valor inválido, tente novamente.')
            continue
    except ValueError:
        print('Valor inválido, tente novamente.')
        continue
        
    litros = area/3
    latas = math.ceil(litros/18)
    preço = latas*80
    print(f'Quantidade de latas de tinta: {latas:.0f};\nPreço total: R${preço:.2f}.')

    comando = input(f'\nDigite qualquer tecla para sair ou ( r ) para reiniciar: ')
    if comando == 'r':
        continue
    else:
        break
        
    
