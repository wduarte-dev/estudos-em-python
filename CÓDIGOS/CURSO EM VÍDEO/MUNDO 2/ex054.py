from datetime import date
ano_atual = date.today().year
anos = []
maiores = []
menores = []
for c in range(1, 8):
    cmd = int(input(f'Digite o {c}° ano de nascimento: '))
    anos.append(cmd)

for ano_nascimento in anos:
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maiores.append(idade)
    else:
        menores.append(idade)

print(f'{len(maiores)} pessoas atingiram a maioridade e {len(menores)} não a atingiram.')