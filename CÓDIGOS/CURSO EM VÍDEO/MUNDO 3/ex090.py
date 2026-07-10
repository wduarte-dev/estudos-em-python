aluno = {}
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input(f'Digite a média de {aluno['nome']}: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Aluno: {aluno['nome']}\nMédia: {aluno['media']}\nSituação: {aluno['situacao']}')