while True:
    print('-'*19)
    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Digite o 2° número: '))
    print('-'*19)
    cmd = input('''
O que você deseja fazer?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')
    if cmd == '1':
        print(f'A soma de {n1} com {n2} é {n1+n2}.\n')
    if cmd == '2':
        print(f'O produto de {n1} com {n2} é {n1*n2}.\n')
    if cmd =='3':
        print(f'O maior deles é o {max(n1, n2)}.\n')
    if cmd == '4':
        continue
    if cmd == '5':
        break