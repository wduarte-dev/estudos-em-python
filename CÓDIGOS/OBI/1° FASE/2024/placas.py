placa = input()
# antigo padrão brasileiro
if (placa[0:3].isalpha() == True and placa[0:3].isupper() == True) and (placa[3] == '-') and (placa[4:9].isdigit() == True) and len(placa) == 8:
    print(1)
    exit()
if (placa[0:3].isalpha() == True and placa[4].isalpha() == True) and (placa[3].isdigit() == True) and (placa[5:7].isdigit() == True) and len(placa) == 7:
    print(2)
    exit()
else:
    print(0)