import requests
try:
    resposta = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')
except:
    print('ERRO! Falha na conexão.')
    exit()
if resposta.status_code == 200:
    dados = resposta.json()
    usd_brl = float(dados['USDBRL']['high'])
    eur_brl = float(dados['EURBRL']['high'])
    print('-'*30)
    print(f'''Cotação USD em BRL: R${usd_brl:.2f}
Cotação EUR em BRL: R${eur_brl:.2f}''')
    print('-'*30)
else:
    print('Erro desconhecido, provavalmente o site está fora do ar. ')