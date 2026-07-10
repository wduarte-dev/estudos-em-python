import requests
url = 'https://webhooksite.net/d9d6d6a2-8179-4330-b218-759bad81eeae'
player_stats = {
    'name': 'Welli',
    'score': 1600,
    'level': 12,
}
response = requests.post(url, json=player_stats) # envia a informação até o site por json
if response.status_code == 200: # 200 significa que deu certo
    print(response.text) # pega o texto de resposta do site (configura)
else:
    print('Erro desconhecido.')