import random
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
opcoes = [nome1, nome2, nome3, nome4]
escolhido = random.choice(opcoes)
print(f'Alunos: {nome1}, {nome2}, {nome3} e {nome4};\nO aluno escolhido para apagar a lousa foi: {escolhido}')

'''
versão resumida demais

from random import choice
alunos = input('Digite o nome dos alunos, separando-os por vírgula: ').split(', ')
print(f'O aluno escolhido foi {choice(alunos)}.')
'''
