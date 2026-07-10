from math import floor
texto = 'BANCO ANGOLANO'
print('='*35)
print(f'{texto:^35}')
print('='*35)
valor = int(input('Digite o valor a ser sacado: R$'))
notas_50 = floor(valor/50)
valor -= notas_50*50
notas_20 = floor(valor/20)
valor -= notas_20*20
notas_10 = floor(valor/10)
valor -= notas_10*10
notas_1 = floor(valor/1)
valor -= notas_1*1
print('-'*35)
print(f"{f'Notas de 50 -> {notas_50}' if notas_50 > 0 else ''}{f'\nNotas de 20 -> {notas_20}' if notas_20 > 0 else ''}{f'\nNotas de 10 -> {notas_10}' if notas_10 > 0 else ''}{f'\nNotas de 1 -> {notas_1}' if notas_1 > 0 else ''}")
print('-'*35)