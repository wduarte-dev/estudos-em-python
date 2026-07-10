# 35 anos de contribuição
import datetime
dados = {}
dados['Nome'] = input('Nome: ')
dados['Idade'] = datetime.date.today().year - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho (0 -> não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Aposentadoria'] = 35 - (datetime.date.today().year - dados['Contratação']) + dados['Idade']
    dados['Salário'] = float(input('Salário: '))
print('-'*25)
for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')