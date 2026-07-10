import random
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input ('Digite o quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
escolha1 = random.choice(lista)
print(f'\nPrimeira apresentação: {escolha1};')
lista.remove(escolha1)
escolha2 = random.choice(lista)
print(f'Segunda apresentação: {escolha2};')
lista.remove(escolha2)
escolha3 = random.choice(lista)
print(f'Terceira apresentação: {escolha3};')
lista.remove(escolha3)
print(f'Quarta apresentação: {lista[0]}.')

'''
Resumido:
from random import shuffle
alunos = input('Digite os alunos que farão as apresentações, separando-os por vírgula: ').split(', ')
shuffle(alunos)
print(f'A sequência é: {alunos}.')
'''
