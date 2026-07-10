numbers = []
cmd = 'S'
while cmd == 'S':
    print('-'*25)
    n = float(input('Digite um número: '))
    if n in numbers:
        print('Valor não adicionado.')
    else:
        numbers.append(n)
        print('Valor adicionado.')
    cmd = input('Deseja continuar? [S/N]\n> ').upper()
print('-'*50)
print(f'Valores em ordem crescente: {sorted(numbers)}')
print('-'*50)