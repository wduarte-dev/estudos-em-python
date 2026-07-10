while True:
    try:
        from random import randint
        numero_pc = randint(1,5)
        numero_user = int(input('Tente adivinhar! Digite um número de 1 a 5: '))
        if numero_user >5 or numero_user < 0:
            print('Requisitos não atendidos, tente novamente!\n')
            continue
    except ValueError:
        print('Oops! Digito inválido, tente novamente.\n')
        continue
    
    if numero_pc == numero_user:
        print('Parabens! Você adivinhou o número!')
        break
    else:
        print(f'Errou, o número era {numero_pc}! Tente novamente.\n')
        continue