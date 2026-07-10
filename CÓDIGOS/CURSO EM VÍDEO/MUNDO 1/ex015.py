while True:
    while True:
        try: 
            dias = int(input('Dias em que o carro foi usado: '))
            if dias <=0:
                print('\nO valor de dias é inválido. Tente novamente.')
                continue
            else:
                break
            
        except ValueError:
            print('\nO número de dias é inválido! Tente novamente.')
            continue

    while True:
        try:
            kmrodado = input('Km rodado: ')
            kmrodado = kmrodado.replace(',','.')
            kmrodado = float(kmrodado)
            if kmrodado < 0:
                print('\nO valor de quilômetros é inválido. Tente novamente.')
                continue
            else:
                break
        except ValueError:
            print('\nO número de quilômetros é inválido! Tente novamente.')
            continue


    valor_dias = 60*dias
    valor_km = 0.15*kmrodado
    print(f'O valor em dias é de R${valor_dias:.2f}.\nO valor pelos km rodados é de R${valor_km:.2f}.')
    print(f'Preço total = R${valor_dias+valor_km:.2f}.')
    cmd = input('\nPressione ( r ) para reiniciar ou qualquer outra tecla para sair. ')
    if cmd == 'r':
        continue
    else:
        break


    
