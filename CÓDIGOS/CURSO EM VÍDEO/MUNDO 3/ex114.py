import requests
url = 'https://pudim.com.br/'
try:
    response = requests.get(url)
except:
    print('\033[31mNão foi possível acessar o site.\033[0m')
    exit()

if response.status_code == 200:
    print('\033[32mConsegui acessar o site com sucesso!\033[0m')
else:
    print('\033[31mNão foi possível acessar o site.\033[0m')