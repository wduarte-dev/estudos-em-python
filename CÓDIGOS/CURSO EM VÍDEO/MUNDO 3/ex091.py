from random import randint
from time import sleep
counter = 0
game = {
    'jogador1':randint(1, 6),
    'jogador2':randint(1, 6),
    'jogador3':randint(1, 6),
    'jogador4':randint(1, 6),
}
print('-'*8+'RESULTADOS'+'-'*8)
results_in_order = sorted(game.values(), reverse = True)
for player, result in game.items():
    print(f'O {player} tirou {result}')
    sleep(1)

print('-'*10+'RANKING'+'-'*9)
while True:
    for player, result in game.items():
        if len(results_in_order) > 0:
            if result == results_in_order[0]:
                print(f'{counter + 1}° LUGAR: {player} com {result}')
                counter += 1
                results_in_order.remove(results_in_order[0])
            else:
                continue
        sleep(1)
    if counter == 4:
        break
    else:
        continue