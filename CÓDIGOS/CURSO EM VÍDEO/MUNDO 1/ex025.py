nome = input('Digite seu nome: ').replace(' ','')
if nome.upper().find('SILVA') == -1:
    print('''Você não tem 'Silva' no nome!''')
else:
    print('''Você tem 'Silva' no nome!''')