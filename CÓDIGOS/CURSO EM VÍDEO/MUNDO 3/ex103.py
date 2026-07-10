def ficha(nome = '<não informado>', gols = 0):
    if nome.strip() == '':
        nome = '<não informado>'
    if gols.strip() == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')

    
nome = input()
gols = input()
ficha(nome, gols)