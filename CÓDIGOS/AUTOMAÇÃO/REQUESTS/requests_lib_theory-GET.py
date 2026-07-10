import requests
URL = ''
resposta = requests.get(URL) # Verifica se a URL existe ou se a permissão é concedida
print(respostas)
# Saída: 
# 200 a 299: Sucesso.
# 400 a 499: Você errou algo (URL errada, falta de permissão).
# 500 para cima: O site dos caras tá fora do ar.

if resposta.status_code == 200:
    print('Conectado com sucesso!')
else:
    print('Erro desconhecido.')

dados = resposta.json() # Pega a URL existente e transforma seus dados em json (dicionário do python)
print(dados)