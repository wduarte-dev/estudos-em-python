from datetime import date 
ano = int(input('Digite o ano do seu nascimento: '))
ano_alist = ano+18
ano_atual = date.today().year
prazo = ano_alist - ano_atual
if ano_alist < ano_atual:
    prazo = prazo*-1
    print(f'Já se passou o tempo do alistamento.\nAtraso: {prazo} anos.')
elif ano_alist > ano_atual:
    print(f'Você ainda deverá se alistar.\nFaltam {prazo} anos para o alistamento obrigatório.')
else:
    print('É hora de se alistar!')

