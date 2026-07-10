cmd = input('Digite a expressão: ')
lista = []
for caractere in cmd:
    if caractere == '(':
        lista.append('(')
    if caractere == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append('Erro.')
            break
if len(lista) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')