numbers = []
p_maior = []
p_menor = []
for n in range(1, 6):
    numbers.append(float(input(f'Digite o {n}° número\n> ')))
for p, n in enumerate(numbers):
    if max(numbers) == n:
        p_maior.append(p+1)
    if min(numbers) == n:
        p_menor.append(p+1)
if max(numbers) != min(numbers):
    print(f'''
O maior valor foi {max(numbers)} e está na(s) posição(ões) {str(p_maior)[1:-1]}
O menor valor foi {min(numbers)} e está na(s) posição(ões) {str(p_menor)[1:-1]}
''')
else:
    print(f'''
Os valores são iguais a {max(numbers)} e estão nas posições {str(p_maior)[1:-1]}
''')