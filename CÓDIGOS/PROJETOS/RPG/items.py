data = {
    'weapons': {
        'starter': {
            'Soco': {'dmg': 0.5},
            },
        
        'enemy_weapons': {
            'Mordida fraca': {'dmg': 1.96},
            'Mordida forte': {'dmg': 0.30},
            'Soco brutal': {'dmg': 0.65},
            'Testadora': {'dmg': 5},
            },
        
        'starter_chest_loot': {
            'Espada quebrada': {'dmg': 0.65, 'rarity': 0},
            'Bastão de madeira': {'dmg': 0.8, 'rarity': 0},
            },
    },
}

for weapon in data['weapons']['starter_chest_loot']:
    from math import floor
    dmg = data['weapons']['starter_chest_loot'][weapon]['dmg']
    rarity = floor(100 / (1+dmg**2))
    data['weapons']['starter_chest_loot'][weapon]['rarity'] = rarity
    