lista = []
counter = 0
while counter < 5:
    print('='*37)
    n = int(input('Digite um número\n> '))
    counter += 1
    if len(lista) == 0:
        lista.append(n)
    else:
        if n <= lista[0]:
            lista.insert(0, n)
            print('Elemento adicionado na primeira posição!')
            continue
        if n >= lista[-1]:
            lista.append(n)
            print('Elemento adicionado na última posição!')
            continue
        for numero in lista:
            if n > numero and n <= (lista[lista.index(numero) + 1]):
                lista.insert(lista.index(numero) + 1, n)
                print(f'Elemento adicionado na posição {lista.index(numero) + 1}!\nEntre o {numero} e o {lista[lista.index(numero) + 1]}')
print('='*37)
print(f'Lista em ordem crescente: {lista}')