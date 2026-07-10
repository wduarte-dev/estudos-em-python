while True:
    numero = input('\nDigite um número inteiro de 0 a 9999: ').replace(' ', '')
    try:
        int(numero)
    except ValueError:
        print('Número inválido, tente novamente seguindo os requisitos.')
        continue
    if int(numero) < 0 or int(numero) > 9999:
        print('O número não está no limite especificado, tente novamente.')
        continue
    if len(numero) == 1:
        print(f'Unidade: {numero[0]}')
    if len(numero) == 2:
        print(f'Unidade: {numero[0]}')
        print(f'Dezena: {numero[1]}')
    if len(numero) == 3:
        print(f'Unidade: {numero[0]}')
        print(f'Dezena: {numero[1]}')
        print(f'Centena: {numero[2]}')
    if len(numero) == 4:
        print(f'Unidade: {numero[0]}')
        print(f'Dezena: {numero[1]}')
        print(f'Centena: {numero[2]}')
        print(f'Milhar: {numero[3]}')
    cmd = input('Deseja reiniciar? ( r ) ou qualquer outra tecla para sair. ')
    if cmd == 'r':
        continue
    else:
        break