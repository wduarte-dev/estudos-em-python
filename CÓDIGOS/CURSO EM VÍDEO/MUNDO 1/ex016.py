num = input('Digite um número decimal: ')
num = float(num.replace(',','.'))
num_int = num//1
print(f'A parte inteira do número {num} é {num_int:.0f}.')

'''
metodo alternativo (com biblioteca math)
from math import floor as arredondar_baixo
num = input('Digite um número decimal: ')
num = float(num.replace(',','.'))
num_int = arredondar_baixo(num)
print(f'A parte inteira do número {num} é {num_int:.0f}.')
'''
