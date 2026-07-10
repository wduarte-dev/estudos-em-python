while True:
    n = int(input('\nQuer ver a tabuada de qual número? (n° negativo para parar)\n> '))
    if n < 0:
        print('\nPROGRAMA ENCERRADO')
        break
    print('-'*12)
    for c in range(1, 11):
        print(f'{c} x {n} = {n*c}')
    print('-'*12)
    