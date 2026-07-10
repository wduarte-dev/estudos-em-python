'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
-  comprar apenas galões de 3,6 litros;
-  misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math
metros_quadrados = float(input('Digite a área em metros quadrados: '))
litros = metros_quadrados/6 * 1.1
print(f'\n-=-=-=-LITROS NECESSÁRIOS-=-=-=-: {litros:.2f}L')
latas = math.ceil(litros/18)
galoes = math.ceil(litros/3.6)
preco_latas = latas*80
preco_galoes = galoes*25
print(f'Quantidade de latas -> {latas} Preço total: R${preco_latas:.2f}')
print(f'Quantidade de galões -> {galoes} Preço total: R${preco_galoes:.2f}')

litros_preencher = litros % 18
galoes = math.ceil(litros_preencher/3.6)
latas = litros//18
galoesp = galoes*25
latasp = latas*80
print('\n=-=-=-=-=MELHOR OPÇÃO-=-=-=-=-')
print(f'Latas: {latas}\nGalões: {galoes}\nPreço total -> R${galoesp+latasp:.2f}\nLitros desperdiçados: {latas*18 + galoes*3.6 - litros:.2f}')
print('-='*15)