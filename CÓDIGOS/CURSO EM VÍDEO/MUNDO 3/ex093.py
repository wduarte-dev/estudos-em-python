jogador = {}
gols = []
s = 0
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input('Quantas partidas jogou? '))
for c in range(1, partidas + 1):
    n = int(input(f'Quantos gols na {c}° partida? '))
    s += n
    gols.append(n)
jogador['gols'] = gols[:]
jogador['total'] = s
print('-'*30)
print(jogador)
print('-'*30)
for chave, valor in jogador.items():
    print(f'A chave "{chave}" tem o valor {valor}')
print('-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas ao todo, sendo:')
for c in range(1, partidas + 1):
    n = c - 1
    print(f'=> Na {c}° partida, fez {gols[n]} gols')
print(f'Foi um total de {s} gols.')
