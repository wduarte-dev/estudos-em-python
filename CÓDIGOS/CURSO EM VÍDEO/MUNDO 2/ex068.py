over18 = men = women_less20 = 0
while True:
    print('-'*5+'CADASTRE UMA PESSOA'+'-'*5)
    age = int(input('Digite a idade do indivíduo:\n> '))
    gender = input('Digite o seu gênero [F/M]:\n> ').upper()
    if age > 18:
        over18 += 1
    if gender == 'M':
        men += 1
    if gender == 'F' and age < 20:
        women_less20 += 1 
    print('-'*29)
    while True:
        cmd = input('Deseja continuar? (s)/(n)\n> ').lower()
        if cmd == 'n':
            break
        if cmd != 's':
            continue
        else:
            break
    if cmd == 'n':
        break

print('-='*25)
print(f'''Dados:
Pessoas maiores de idade: {over18}
Homens: {men}
Mulheres com menos de 20 anos: {women_less20}''')
print('-='*25)
                      