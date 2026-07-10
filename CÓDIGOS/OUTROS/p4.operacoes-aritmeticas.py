# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = float(input('Agora, digite um número real: '))
pdm = (2*num1)*(num2/2)
st = (3*num1) + num3
e = num3**3
print(f'\nO produto do dobro de {num1} com metade de {num2} é {pdm:.1f} ;')
print(f'A soma do triplo de {num1} com {num3} é {st:.1f} ;')
print(f'{num3} elevado ao cubo é {e:.1f}.')
