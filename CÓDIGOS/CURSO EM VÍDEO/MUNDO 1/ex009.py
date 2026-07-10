while True:
    try:
        numero = int(input('Digite um número INTEIRO: '))
    except ValueError:
        print('Oops! A entrada não é válida, tente novamente\n')
        continue

    um = numero*1
    dois = numero*2
    tres = numero*3
    quatro = numero*4
    cinco = numero*5
    seis = numero*6
    sete = numero*7
    oito = numero*8
    nove = numero*9
    dez = numero*10

    print(f'Tabuada:\n{numero}x1 = {um}\n{numero}x2 = {dois}\n{numero}x3 = {tres}')
    print(f'{numero}x4 = {quatro}\n{numero}x5 = {cinco}\n{numero}x6 = {seis}\n{numero}x7 = {sete}')
    print(f'{numero}x8 = {oito}\n{numero}x9 = {nove}\n{numero}x10 = {dez}')
    cmd = input('Pressione ( r ) para reiniciar ou qualquer outra tecla para fechar a operação: ')
    if cmd == 'r':
        continue
    else:
        break
    
    
        
