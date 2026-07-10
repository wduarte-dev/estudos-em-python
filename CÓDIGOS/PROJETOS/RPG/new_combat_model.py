from time import sleep
from utils import battle_start_text, cmd_input, get_weapon_values, n
import enemy
import player
import random
enemy.enemy_stats()
enemy_name = 'Rato selvagem'
actions = ['1', '2', '3']
state0_chances = [60, 30, 10]
state1_chances = [35, 45, 20]
state2_chances = [40, 40, 20]


for c in range (3, 0, -1):
    print(c, end='.')
    sleep(0.33)
    print(end='.')
    sleep(0.33)
    print(end='.')
    sleep(0.33)
sleep(2)
print('\n')
print('-='*15)
print('-=-=-=-=-=-=FIGHT!=-=-=-=-=-=-')
print('-='*15)
sleep(2)
for c in range(1, 25):
    print('▒█'*15)
    sleep(0.15)

enemy.enemy_stats()
plyr_dmg = get_weapon_values(player.data['weapon'])['dmg']
enemy_dmg = get_weapon_values(enemy.mutable_data['Rato selvagem']['weapon'])['dmg']
enemy_state = enemy.data['Rato selvagem']['initial_state']
enemy_hp = enemy.mutable_data['Rato selvagem']['hp']

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=-=-=-=-LUTE OU MORRA-=-=-=-=-=-=-=')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
sleep(1)
print(f'{enemy_name} {battle_start_text()}')
sleep(1)
pa = cmd_input('Ações:\n[1] Atacar\n[2] Esquivar\n[3] Provocar\n[4] Fugir\n   > ', ['1', '2', '3'])

enemy.update_reaction()
if enemy.mutable_data['Rato selvagem']['hp'] < 0.20*enemy.mutable_data['Rato selvagem']['hp']:
    enemy_state = 1
    
if enemy_state == 0:
    ea = random.choices(actions, weights = state0_chances, k=1)[0]
elif enemy_state == 1:
    ea = random.choices(actions, weights = state1_chances, k=1)[0]
elif enemy_state == 2:
    ea = random.choices(actions, weights = state2_chances, k=1)[0]

if pa == '1' and ea == '1':
    print('Você parte para o ataque!')
    print('E o inimigo tambem!')
    if player.data['1stmove'] > enemy.data['Rato selvagem']['1stmove']:
        print('Mas você é tão ágil que o acerta primeiro!')
        enemy.mutable_data['Rato selvagem']['hp'] = n(enemy.mutable_data[enemy_name]['hp'] - plyr_dmg)
    else:
        print('Mas ele é tão ágil que te acerta primeiro!')
        player.data['hp'] -= n(enemy_dmg)
        
if pa == '1' and ea == '2':
    print('Você parte para o ataque!')
    print('O inimigo decide se esquivar')
    non_reaction_chance = 1 - enemy.mutable_data['Rato selvagem']['reaction']
    reaction_chance = enemy.mutable_data['Rato selvagem']['reaction']
    reaction = random.choices([False, True], weights = [non_reaction_chance, reaction_chance], k=1)[0]
    if reaction == True:
        print('Ele reage e te acerta antes de você se recompor')
        player.data['hp'] -= 1.5*enemy_dmg
    else:
        print('Você se recompõe rápido e retorna na defensiva')
    
if pa == '1' and ea == '3':
    print('Você parte para o ataque!')
    print('O inimigo te provoca')
    enemy.mutable_data['Rato selvagem']['hp'] = n(enemy.mutable_data[enemy_name]['hp'] - 1.25*plyr_dmg)
    print('Você o acerta com toda a sua força!')
    
if pa == '2' and ea == '1':
    print('Você decide se esquivar')
    print('O inimigo parte para o ataque')
    non_reaction_chance = 1 - player.data['reaction']
    reaction_chance = player.data['reaction']
    reaction = random.choices([False, True], weights = [non_reaction_chance, reaction_chance], k=1)[0]
    if reaction == True:
        print('Você reage e acerta antes dele se recompor')
        enemy.mutable_data[enemy_name]['hp'] -= 1.5*enemy_dmg
    else:
        print('O inimigo se recompõe rapidamente e retorna na defensiva')
    
if pa == '2' and ea == '2':
    print('Você decide se esquivar')
    print('O inimigo decide se esquivar')
    print('Nada aconteceu.')

if pa == '2' and ea == '3':
    print('Você decide se esquivar')
    print('O inimigo te provoca e fortalece seus ataques')
    print('Você fica irritado e mais vulnerável!')
    enemy_dmg *= 1.025
    
if pa == '3' and ea == '1':
    print('Você provoca o inimigo')
    print('O inimigo parte para o ataque')
    player.data['hp'] -= 1.25*enemy_dmg
    print('Ele te acerta com toda sua força!')
    
if pa == '3' and ea == '2':
    print('Você provoca o inimigo e fortalece seus ataques')
    print('O inimigo decide se esquivar')
    print('Ele fica irritado e mais vulnerável!')
    plyr_dmg *= 1.025
    
if pa == '3' and ea == '3':
    print('Você provoca o inimigo e fortalece seus ataques')
    print('O inimigo te provoca e fortalece seus ataques')
    print('Ambos ficam mais dispostos pelo calor da luta!')
    plyr_dmg *= 1.025
    enemy_dmg *= 1.025