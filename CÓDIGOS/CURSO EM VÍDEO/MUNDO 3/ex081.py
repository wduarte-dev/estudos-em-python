cmd = 'S'
lista = []
while cmd == 'S':
    n = lista.append(float(input('Digite um número: ')))
    cmd = input('Quer continuar? [S/N]\n> ').upper()
print(f'''
Quantidade de números digitados -> {len(lista)}
Lista decrescente -> {sorted(lista)[::-1]}
{'O valor 5 faz parte da lista!' if 5 in lista else 'O valor 5 não faz parte da lista!'}
''')