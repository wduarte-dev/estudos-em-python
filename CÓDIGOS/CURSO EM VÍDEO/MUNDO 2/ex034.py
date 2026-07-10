salario = input('Digite o salário em reais: ').replace(',','.').replace(' ', '').strip()
salario = float(salario)
if salario >1250:
    novo_salario = salario*1.1
    print(f'Salário sem aumento -> R${salario:.2f}\nSalário com aumento de 10% -> R${novo_salario:.2f}')
else:
    novo_salario = salario*1.15
    print(f'Salário sem aumento -> R${salario:.2f}\nSalário com aumento de 15% -> R${novo_salario:.2f}')