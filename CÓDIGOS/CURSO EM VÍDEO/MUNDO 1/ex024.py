cidade = input('Digite o nome de uma cidade: ').replace(' ', '')
if cidade.upper()[0:5].find('SANTO') == -1:
    print('''A cidade não começa com 'Santo'!''')
else:
    print('''A cidade começa com 'Santo'!''')
