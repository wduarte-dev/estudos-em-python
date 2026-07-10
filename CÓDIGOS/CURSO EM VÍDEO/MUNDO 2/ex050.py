n1 = int(input('Digite o primeiro número (inteiro): '))
n2 = int(input('Digite o segundo número (inteiro): '))
n3 = int(input('Digite o terceiro número (inteiro): '))
n4 = int(input('Digite o quarto número (inteiro): '))
n5 = int(input('Digite o quinto número (inteiro): '))
n6 = int(input('Digite o sexto número (inteiro): '))
lista = [n1, n2, n3, n4, n5, n6]
menor_n = min(lista)
maior_n = max(lista)
soma = 0
for numero in lista:
    if numero % 2 == 0:
        soma += numero
print(soma)