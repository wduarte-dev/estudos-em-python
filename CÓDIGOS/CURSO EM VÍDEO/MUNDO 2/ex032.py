from datetime import date
ano = int(input('Digite o ano bissexto (ou 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().day
    print(f'Ano atual: {ano}')
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')