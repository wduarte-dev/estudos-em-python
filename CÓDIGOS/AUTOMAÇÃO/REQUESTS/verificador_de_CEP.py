import requests 
cep = input('Digite o CEP para consulta: ')
try:
    resposta = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
except:
    print('ERRO! Verifique a conexão com a internet')
    exit()
if resposta.status_code == 200:
    print('Conectado ao site com sucesso!')
    dados = resposta.json()
    if 'erro' in dados.keys():
        print('CEP não encontrado no banco de dados.')
        exit()
    print('-'*25)
    print(f'''Logradouro: {dados['logradouro'].upper()}
Bairro: {dados['bairro'].upper()}
Cidade: {dados['localidade'].upper()}''')
    print('-'*25)
else:
    print('ERRO! Site fora do ar ou CEP inválido.')