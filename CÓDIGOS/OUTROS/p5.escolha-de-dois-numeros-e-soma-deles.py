import random
import decimal
lista = input('Digite uma lista de números (separados por espaço): ').split( )
escolhidos = random.sample(lista, k=2)
print(f'Os dois números sorteados: {escolhidos}')
soma = decimal.Decimal(float(escolhidos[0]) + float(escolhidos[1]))
print(f'Soma deles: {soma}.')
