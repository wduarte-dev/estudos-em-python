lista = []
counter = 0
for c in range(1, 6):
    n = float(input(f'Digite o {c}° número: '))
    counter += 1
    if counter == 1:
        lista.append(n)
        print('Elemento adicionado na posição 0.')
    if counter == 2:
        if n >= lista[0]:
            lista.insert(1, n)
            print('Elemento adicionado na posição 1.')
        else:
            lista.insert(0, n)
            print('Elemento adicionado na posição 0.')
    if counter == 3:
        if n >= lista[1]:
            lista.insert(2, n)
            print('Elemento adicionado na posição 2.')
        if n <= lista[0]:
            lista.insert(0, n)
            print('Elemento adicionado na posição 0.')
        elif n > lista[0] and n < lista[1]:
            lista.insert(1, n)
            print('Elemento adicionado na posição 1.')
    if counter == 4:
        if n >= lista[2]:
            lista.insert(3, n)
            print('Elemento adicionado na posição 3.')
        if n <= lista[0]:
            lista.insert(0, n)
            print('Elemento adicionado na posição 0.')
        if n > lista[0] and n < lista [1]:
            lista.insert(1, n)
            print('Elemento adicionado na posição 1.')
        elif n > lista[1] and n < lista[2]:
            lista.insert(2, n)
            print('Elemento adicionado na posição 2.')
    if counter == 5:
        if n >= lista[3]:
            lista.insert(4, n)
            print('Elemento adicionado na posição 4.')
        if n <= lista[0]:
            lista.insert(0, n)
            print('Elemento adicionado na posição 0.')
        if n > lista[0] and n <= lista[1]:
            lista.insert(1, n)
            print('Elemento adicionado na posição 1.')
        if n > lista[1] and n <= lista[2]:
            lista.insert(2, n)
            print('Elemento adicionado na posição 2.')
        elif n > lista[2] and n < lista[3]:
            lista.insert(3, n)
            print('Elemento adicionado na posição 3.')
    print('-'*30)
print(f'Valores digitados em ordem: {lista}')