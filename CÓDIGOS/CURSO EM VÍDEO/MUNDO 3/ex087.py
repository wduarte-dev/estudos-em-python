matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
largura = 1
soma_pares = 0
soma_terceira_coluna = 0
for linha in range(1, 4):
    for coluna in range(1, 4):
        matriz[linha-1][coluna-1] = int(input(f'Digite um número para a posição ({linha}, {coluna})\n> '))
        n = matriz[linha-1][coluna-1]
        if len(str(n)) > largura:
            largura = len(str(n))
        if n % 2 == 0:
            soma_pares += n
        if coluna == 3:
            soma_terceira_coluna += n
maior_valor_2_linha = max(matriz[1])
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^{largura}}]', end = '')
    print()
print(f'''Soma de todos os pares: {soma_pares}
Soma dos valores da 3° coluna: {soma_terceira_coluna}
Maior valor da segunda linha: {maior_valor_2_linha}''')