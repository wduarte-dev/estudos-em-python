while True:
    try:
        reais = float(input('Dinheiro em R$: '))
        if reais <=0:
            print('Oops! Valor inválido, tente novamente.')
            continue
    except:
        print('Oops! Valor inválido, tente novamente.')
        continue

    dolar = reais/5
    print(f'O valor de R${reais:.2f} pode ser convertido em ${dolar:.2f}.')
    cmd = input('Deseja reiniciar a operação? (s)/(n) ')
    if cmd == 's':
        continue
    else:
        break
