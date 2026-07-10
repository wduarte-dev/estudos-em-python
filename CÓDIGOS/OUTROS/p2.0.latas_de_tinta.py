import math

while True:
    try:
        area = input('Digite a área em m²: ')
        area = area.replace(',' , '.')
        area = float(area)
        if area > 1e5:
            input('Valor extremamente alto. Deseja continuar? ')
        break
    except ValueError:
        print('Valor inválido, tente novamente.')

while area <=0:
    print('Valor inválido, tente novamente.')
    area = float(input('Digite a área em m²: '))
    
litros = area/3
latas = math.ceil(litros/18)
preço = latas*80
print(f'Quantidade de latas de tinta: {latas:.0f};\nPreço total: R${preço:.2f}.')
