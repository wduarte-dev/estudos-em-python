# verificador de ano bissexto apenas com base nas strings (método extremamente desnecessário)
ano = input('Digite um ano qualquer (1 a 9999) e será verificado se ele é bissexto: ').strip()
if  len(ano) == 1 or len(ano)== 2:
    ano = int(ano)
    if ano % 4 == 0:
        print('O ano é bissexto!')
    else:
        print('O ano não é bissexto!')

elif len(ano) == 3:
    if ano.rfind('00') == 1:
        ano = int(ano)
        if ano % 400 == 0:
            print('O ano é bissexto!')
        else:
            print('O ano não é bissexto!')
    else:
        ano = int(ano)
        if ano % 4 == 0:
            print('O ano é bissexto!')
        else:
            print('O ano não é bissexto!')

elif ano.count('0') == 0 or ano.count('0') == 1:
    ano = int(ano)
    if ano % 4 == 0:
        print('O ano é bissexto!')
    else:
        print('O ano não é bissexto!')

elif ano.count('0') == 2:
    if ano.find('00') == 2:
        ano = int(ano)
        if ano % 400 == 0:
            print('O ano é bissexto!')
        else:
            print('O ano não é bissexto!')
    else:
        ano = int(ano)
        if ano % 4 == 0:
            print('O ano é bissexto!')
        else:
            print('O ano não é bissexto!')

elif ano.count('0') == 3:
    ano = int(ano)
    if ano % 400 == 0:
        print('O ano é bissexto!')
    else:
        print('O ano não é bissexto!')
            