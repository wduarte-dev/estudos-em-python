from utils import cmd_input

def campfire():
    cmd = cmd_input('\nUma fogueira! Deseja descansar? (s) / (n) ', ['s', 'n'])
    if cmd == 'n':
        return None
    elif cmd == 's':
        campfire_recover()

def campfire_recover():
    from random import choices
    from utils import check_on_hp
    from time import sleep
    import player
    plyr_hpmax = player.data['hpmax']
    hp_recover = [0.1*plyr_hpmax, 0.2*plyr_hpmax, 0.3*plyr_hpmax, 0.4*plyr_hpmax, 0.5*plyr_hpmax]
    respective_rarity = [55.4, 20.8, 11.1, 7.2, 5.5] # frequência relativa de (multiplier^-1.5/150)
    campfire_recover = choices(hp_recover, weights = respective_rarity, k=1)[0]
    player.data['hp'] += campfire_recover
    check_on_hp()
    print(f'HP recuperado = +{campfire_recover:.2f} HP')
    sleep(1)
    return None
