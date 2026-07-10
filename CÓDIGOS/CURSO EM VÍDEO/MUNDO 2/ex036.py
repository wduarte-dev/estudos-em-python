valor_casa = input('Digite o valor da casa, em reais, sem pontos nem vírgulas: ').strip().replace(' ', '').replace('.','').replace(',','')
valor_casa = int(valor_casa)
salario = input('Do mesmo modo, digite seu salario em reais: ').strip().replace(' ', '').replace('.','').replace(',','')
salario = int(salario)
anos = input('Em quantos anos você pretende pagar? ').strip().replace(' ', '').replace('.','').replace(',','')
anos = int(anos)
prestacao= valor_casa / (anos * 12)
if prestacao > 1.30*salario:
    print('-='*30)
    print(f'Empréstimo negado. Motivo: A prestação mensal de R${prestacao:.2f} é superior a 130% do salário de R${salario:.2f}')
    print(f'Na possibilidade de um erro, revalide as informações ou consulte o suporte.')
    print('-='*30)
else:
    print('-='*30)
    print(f'Empréstimo aprovado! Confirme as informações:\nPreço da casa: R${valor_casa}\nSalário: R${salario}')
    print(f'Prestação mensal: R${prestacao:.2f}')
    print('=-'*30)
    
