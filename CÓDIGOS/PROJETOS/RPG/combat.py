from utils import n, cmd_input, stylized_text
from time import sleep

def combat(enemy_name):
    import player
    from utils import battle_start_text
    for c in range (3, 0, -1):
        print(c, end='.')
        sleep(0.33)
        print(end='.')
        sleep(0.33)
        print(end='.')
        sleep(0.33)
    print(f'\n\033[1m{enemy_name} fica em posição de luta.\033[0m')
    sleep(1)
    player.data['area'] = 'rat_initial_battle'
    while True:
        print('\n=-=-=-=-=-LUTE OU MORRA=-=-=-=-=')
        print(f'{enemy_name} {battle_start_text()}')
        if player.data['area'] == 'rat_initial_battle':
            action = initial_combat(enemy_name)
        elif player.data['area'] != 'rat_initial_battle':
            cmd = cmd_input('Ações:\n[1] Atacar\n[2] Checar STATUS\n[3] Fugir ', ['1', '2', '3'])
            if cmd == '1':
                action = combat_action_attack(enemy_name)
            if cmd == '2':
                action = combat_action_check_status(enemy_name)
            if cmd == '3':
                action = combat_action_run(enemy_name)
        if action == True:
            continue
        if action == False:
            break
        
def combat_action_attack(enemy_name):
    from time import sleep
    import player
    import enemy
    import items
    enemy.enemy_stats()
    plyr_dmg = get_weapon_values(player.data['weapon'])['dmg']
    while n(player.data['hp']) > 0 and n(enemy.mutable_data[enemy_name]['hp']) > 0:
        enemy.mutable_data[enemy_name]['hp'] = n(enemy.mutable_data[enemy_name]['hp'] - plyr_dmg)
        print(f"\nVocê o ataca!\nVida do inimigo: {enemy.mutable_data[enemy_name]['hp']}")
        sleep(1)
        if enemy.mutable_data[enemy_name]['hp'] > 0:
            player.data['hp'] -= get_weapon_values(enemy.mutable_data[enemy_name]['weapon'])['dmg']
            print(f"\nMas o inimigo reage! \nSua vida: {player.data['hp']:.2f}")
            sleep(1)
        game_over()
    sleep(1)
    player.data['xp'] += enemy.data[enemy_name]['xp']
    print('\nVITÓRIA!')
    print(f"XP ganho = + {enemy.data[enemy_name]['xp']}")
    print(f"XP atual = {player.data['xp']}")
    
    
    sleep(1)
    return False  

def combat_action_check_status(enemy_name):
    from time import sleep
    from random import choices
    import player
    import enemy
    enemy.enemy_stats()
    print('\n-=-=-=-=STATUS=-=-=-=-')
    cmd = cmd_input(f'(1) Sua vida\n(2) Dano da sua arma\n(3) Vida do inimigo\n(4) Dano do inimigo\n(5) SAIR ', ['1', '2', '3', '4', '5'])
    if cmd == '1':
        sleep(2)
        stylized_text("Você coloca a mão no peito, verificando seus batimentos cardíacos...", 0.05)
        print(f"\nVida atual: {player.data['hp']:.2f}HP\n")
        sleep(2)
        return True
    if cmd == '2':
        sleep(2)
        player.data['hp'] = n(player.data['hp'] - get_weapon_values(player.data['weapon'])['dmg'])
        stylized_text("Você se machuca para verificar a letalidade em si mesmo...", 0.05)
        print(f"\nDano: {get_weapon_values(player.data['weapon'])['dmg']}")
        game_over()
        sleep(2)
        return True
    if cmd == '3':
        sleep(2)
        stylized_text('Você observa o físico e as condições do inimigo detalhadamente...', 0.05)
        sleep(2)
        print('\nVida do inimigo com base na sua percepção:')
        low_perception = choices([0.8, 0.85, 0.90, 0.95, 1], k=1)[0]*enemy.mutable_data[enemy_name]['hp']
        high_perception = choices([1.2, 1.15, 1.10, 1.05, 1], k=1)[0]*enemy.mutable_data[enemy_name]['hp']
        print(f"{low_perception:.2f}HP ~ {high_perception:.2f}HP")
        sleep(2)
        return True
    if cmd == '4':
        sleep(2)
        player.data['hp'] = n(player.data['hp'] - get_weapon_values(enemy.mutable_data[enemy_name]['weapon'])['dmg'])
        stylized_text("Você baixa sua a guarda por um momento, deixando o inimigo te atacar...", 0.05)
        print(f"\nDano de {enemy.mutable_data[enemy_name]['weapon']} recebido: {get_weapon_values(enemy.mutable_data[enemy_name]['weapon'])['dmg']}")
        game_over()
        sleep(2)
        return True
    if cmd == '5':
        return True
    
def combat_action_run(enemy_name):
    from random import choices
    from time import sleep
    import player
    import enemy
    enemy.enemy_stats()
    fate = choices(['sucess', 'fail'], weights = [70, 30], k=1)[0]
    print('Você tenta fugir...')
    sleep(2)
    if fate == 'sucess':
        return False
    elif fate == 'fail':
        sleep(1)
        print('Ao deslizar pelas rochas e cair no chão...\nO inimigo te ataca e você se recompõe rapidamente.')
        sleep(1)
        player.data['hp'] = n(player.data['hp'] - 1.5*get_weapon_values(enemy.mutable_data[enemy_name]['weapon'])['dmg'])
        return True
        
def game_over():
    from time import sleep
    import player
    if n(player.data['hp']) <= 0:
        sleep(2)
        print('\nGAME OVER')
        exit()

    
############### FUNÇÕES DE BATALHAS MODIFICADAS #################
def initial_combat(enemy_name):
    cmd0 = cmd_input('Ações:\n[1] Atacar\n\033[9m[2] Fugir\033[0m\n[3] Tutorial ', ['1', '2', '3'])
    if cmd0 == '1':
        combat_action_attack(enemy_name)
        return False
    if cmd0 == '2':
        sleep(1)
        print('O rato está bloqueando a saída.')
        sleep(1)
        return True
    if cmd0 == '3':
        stylized_text(f'''
"Tutorial?"
"Não consegue lidar com um simples rato?"
"..."
"Apenas mate-o!"
''', 0.10)
        return True