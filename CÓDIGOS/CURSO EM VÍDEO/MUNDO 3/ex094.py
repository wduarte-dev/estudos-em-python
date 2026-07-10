dict = {}
info = []
women = []
age_sum = 0
while True:
    dict['Nome'] = input('Nome: ')
    dict['Gênero'] = input('Gênero [M/F]: ').upper()
    if dict['Gênero'] == 'F':
        women.append(dict['Nome'])
    dict['Idade'] = int(input('Idade: '))
    age_sum += dict['Idade']
    info.append(list(dict.values()))
    dict.clear()
    print(info, dict)
    cmd = input('Deseja continuar? [s]/[n]\n> ').lower()
    if cmd == 'n':
        break
average = round(age_sum/len(info), 2)
print('-'*20)
print(f'''- Pessoas cadastradas: {len(info)}
- Média de idade do grupo: {average}''')
print('- Mulheres: ', end = '')
print(*women, sep = ', ')
print('- Pessoas acima da média:')
for n in range(0, len(info)):
    if info[n][2] > average:
        print(f'Nome: {info[n][0]}, gênero: {info[n][1]} e idade: {info[n][2]}')