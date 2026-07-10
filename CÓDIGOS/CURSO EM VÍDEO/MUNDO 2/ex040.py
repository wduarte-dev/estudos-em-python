while True:
    n1 = float(input('Digite a primeira nota de 1 a 10: '))
    if n1 > 10 or n1 < 0:
       print('Esse valor não segue os requisitos, reinicie o programa e tente novamente.')
       break
    n2 = float(input('Agora digite a segunda nota: '))
    if n2 > 10 or n2 < 0:
        print('Esse valor não segue os requisitos, reinicie o programa e tente novamente.')
        break
    med = (n1+n2)/2
    if med >= 7:
        print('APROVADO')
    elif med < 5:
        print('REPROVADO')
    else:
        print('RECUPERAÇÃO')
    break