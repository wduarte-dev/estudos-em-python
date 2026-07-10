from myfunctions import get_float
lado1 = get_float(input('Digite o valor do primeiro lado: '))
lado2 = get_float(input('Digite o valor do segundo lado: '))
lado3 = get_float(input('Digite o valor do terceiro lado: '))
lista = [lado1, lado2, lado3]
maior = max(lista)
menor = min(lista)
lista.remove(maior)
lista.remove(menor)
meio = lista[0]
if meio + menor > maior:
    print('Um triângulo PODE ser formado a partir dos lados fornecidos.')
    if lado1==lado2 and lado2==lado3:
        print('E o triângulo formado será EQUILÁTERO.')
    if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print('E o triângulo formado será ESCALENO.')
    if (lado1 == lado2 and lado3 != lado1) or (lado3==lado2 and lado1 != lado2) or (lado1 == lado3 and lado2 != lado3):
        print('E o triângulo formado será ISÓSCELES.')
        
else:
    print('Um triângulo NÃO PODE ser formado a partir dos lados fornecidos.')