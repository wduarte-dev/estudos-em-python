data = {
    'name': 'None',
    'hpmax': 10,
    'hp': 10,
    'weapon': 'Soco',
    'xp': 0,
    'area': 'None',
    '6th_sense': False,
    'memórias': 0,
    '1stmove': 0,
    'reaction': 10
}

inventory = [ ]


def level_up():
    from time import sleep
    levels_for_xp = []
    while data['xp'] >= levels_for_xp[0]:
        sleep(2)
        print('Você subiu de nível!\nSeus músculos aparentam estarem mais fortes...')
        sleep(1)
        levels_for_xp.remove(levels_for_xp[0])
        data['hpmax'] *= 1.15
        data['reaction'] += 0.25
    return None
        
    