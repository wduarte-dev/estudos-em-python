from utils import cmd_input
event_loot = 'None'

def starter_chest_loot():
    global event_loot
    from random import choices
    from time import sleep
    import items
    import player
    cmd = cmd_input('\nDeseja abrir o baú? (s) / (n) ', ['s', 'n'])
    if cmd == 's':
        sleep(1)
        loot_chest_weapons = list(items.data['weapons']['starter_chest_loot'].keys())
        loot_chest_weapons_rarity = list(items.data['weapons']['starter_chest_loot'][weapon]['rarity'] for weapon in items.data['weapons']['starter_chest_loot'])
        event_loot = choices(loot_chest_weapons, weights = loot_chest_weapons_rarity, k=1)[0]
        return equip_loot()
    else:
        return None

def equip_loot():
    import player
    global event_loot
    print(f'Item dado: {event_loot}!')
    cmd = cmd_input('\nDeseja equipar? (s) / (n) ', ['s', 'n'])
    if cmd == 's':
        player.data['weapon'] = event_loot
        print(f'{event_loot} agora é sua nova arma!')
        return None
    elif cmd == 'n':
        event_loot = 'None'
        return None