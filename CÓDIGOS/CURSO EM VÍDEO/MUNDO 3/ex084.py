cmd = 'S'
dados = []
temp = []
while cmd == 'S':
    print('-'*30)
    temp.append(input('Nome: '))
    temp.append(int(input('Peso: ')))
    dados.append(temp[:])
    temp.clear()
    cmd = input('Deseja continuar? [S/N]\n> ').upper()
pesos = [dado[1] for dado in dados]
maior_peso = max(pesos)
portmaior = [dado[0] for dado in dados if dado[1] == maior_peso]
menor_peso = min(pesos)
portmenor = [dado[0] for dado in dados if dado[1] == menor_peso]
print('='*45)
print(f'''Total de pessoas cadastradas: {len(dados)}
Maior peso: {maior_peso}kg // Portador(es): {', '.join(portmaior)}
Menor peso: {menor_peso}kg // Portador(es): {', '.join(portmenor)}''')
print('='*45)