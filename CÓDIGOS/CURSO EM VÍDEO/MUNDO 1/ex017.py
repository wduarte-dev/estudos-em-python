from math import sqrt as raiz_quadrada
cateto_1 = float(input('Digite o primeiro cateto do triângulo: '))
cateto_2 = float(input('Digite o segundo cateto do triângulo: '))
hipotenusa = raiz_quadrada((pow(cateto_1, 2) + pow(cateto_2, 2)))
print(f'O triângulo de cateto {cateto_1} e cateto {cateto_2} tem hipotenusa igual a {hipotenusa:.2f}')

'''
1° Versão resumida

from math import hypot
c1 = float(input('Digite o cateto 1: '))
c2 = float(input('Digite o cateto 2: '))
hip = hypot(c1, c2)
print(f'A hipotenusa é igual a {hip:.2f}.')
'''
