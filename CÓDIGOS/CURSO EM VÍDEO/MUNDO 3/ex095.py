# Estrutura do dicionário:
# info = jogador, jogo1, jogo2, jogo3 ... jogon
info_dict = {}
info_list = []
maxi = 0
while True:
    sum = 0
    info_dict['jogador'] = input('Nome do jogador: ').capitalize()
    n = int(input('Quantidade de partidas: '))
    for x in range(1, n+1):
        info_dict[f'jogo{x}'] = int(input(f'Quantidade de gols na partida {x}: '))
        sum += info_dict[f'jogo{x}']
    info_dict[f'total_score'] = sum
    info_list.append(list(info_dict.values()))
    info_dict.clear()
    cmd = input('Deseja continuar? (s) / (n)\n> ').lower()
    if cmd == 'n':
        break
for minlist in info_list:
    if len(minlist) > maxi:
        maxi = len(minlist)
goals_format = 4+2*maxi
print('-'*(27+goals_format))
print(f'{'N°':<3}{'Nome':<15}{'Gols':<{goals_format}}{'Total'}')
for x in range(0, len(info_list)):
    print(f'{x:<3}{info_list[x][0]:<15}{str(info_list[x][1:-1]):<{goals_format}}{info_list[x][-1]}')
print('-'*(27+goals_format))
while True:
    cmd = int(input('Mostrar dados de qual jogador? (999 encerra)\n> '))
    if cmd != 999:
        try:
            print('-'*(27+goals_format))
            print(f'Levantamento do jogador {info_list[cmd][0]}:')
            for n, numero in enumerate(info_list[cmd][1:-1]):
                print(f'No jogo {n+1} fez {numero} gols.')
            print('-'*(27+goals_format))
        except IndexError:
            print('ERRO! Número não encontrado, tente novamente.\n')
            continue
    else:
        break
