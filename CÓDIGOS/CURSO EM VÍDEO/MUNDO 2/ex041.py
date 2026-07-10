# esse programa pode ser melhorado adicionando o mês em que a pessoa nasceu (para saber a idade de forma precisa)
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Sua idade é de {idade-1}-{idade} anos, sendo sua categoria a:')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <=14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif idade > 20:
    print('MASTER')
else:
    print('SÊNIOR')