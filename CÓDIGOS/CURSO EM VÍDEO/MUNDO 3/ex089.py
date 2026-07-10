listona = [] # listona = [ [nome, [n1, n2]], [nome, [n1, n2]] ]
listinha = []
notas = []
cmd = 's'
while cmd == 's':
    nome = input('Nome do aluno: ')
    notas.append(int(input('1° Nota: ')))
    notas.append(int(input('2° Nota: ')))
    listinha.append(nome)
    listinha.append(notas[:])
    listona.append(listinha[:])
    notas.clear()
    listinha.clear()
    cmd = input('Deseja continuar? [S/N]\n> ').lower()
# BOLETIM
print('_='*20)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for c in range(0, len(listona)):
    media = (listona[c][1][0]+listona[c][1][1])/2
    print(f'{c:<4}{listona[c][0]:<10}{media:>8}')
c = 0
while c != 999:
    print('-='*22)
    c = int(input('Mostrar notas de qual aluno? (999 interrompe)\n> '))
    try:
        print(f'As notas de {listona[c][0]} foram {listona[c][1]}.')
    except IndexError:
        exit()