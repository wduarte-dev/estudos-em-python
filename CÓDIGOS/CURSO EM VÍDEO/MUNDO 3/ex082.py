total = []
pares = []
impares = []
while True:
    n = int(input('Digite um número inteiro: '))
    total.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    cmd = input('Deseja continuar? [S/N]\n> ').lower()
    if cmd == 'n':
        break
print(f'''
Lista completa: {total}
{f'Lista dos pares: {pares}' if len(pares) > 0 else 'Nenhum número par foi digitado.'}
{f'Lista dos ímpares: {impares}' if len(impares) > 0 else 'Nenhum número ímpar foi digitado.'}
''')
