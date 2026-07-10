# state 0 -> agressivo; 1 -> defensivo, 2 -> imprevisível
from utils import get_weapon_values, n
from math import floor

data = {
    'Rato selvagem': {'hp': 3, 'weapon': 'Mordida fraca', 'xp': 0.5, 'initial_state': True, '1stmove': 0, 'reaction': 0},
}

mutable_data = None

def enemy_stats():
    from copy import deepcopy
    global mutable_data
    mutable_data = deepcopy(data)
    return None

def update_reaction():
    for enemy in data:
        xp = data[enemy]['xp']
        dmg = get_weapon_values(data[enemy]['weapon'])['dmg']
        hp = mutable_data[enemy]['hp']
        reaction = n((xp * (hp + 1))**0.5 / dmg**1.25)
        mutable_data[enemy]['reaction'] = reaction
