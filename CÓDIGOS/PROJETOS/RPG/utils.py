def battle_start_text():
    from random import choice
    dialogues = []
    dialogues.append('te olha fixamente.')
    dialogues.append('te encara.')
    dialogues.append('não parece ser amigável...')
    dialogues.append('se irrita com sua presença.')
    dialogues.append('está disposto a matá-lo.')
    dialogues.append('não terá piedade.')
    dialogues.append('tentará te aniquilar a qualquer custo.')
    dialogues.append('esboça um sorriso presunçoso.')
    dialogues.append('esboça um sorriso assustador.')
    dialogues.append('espera alguma ação sua.')
    dialogues.append('não parece ter medo da sua presença.')
    dialogues.append('te amedronta.')
    dialogues.append('não está para brincadeira.')
    return choice(dialogues)
    
def n(number):
    return round(number, 2)

def cmd_input(text, commands):
    from time import sleep
    while True:
        cmd = input(text).lower()
        if cmd in commands:
            sleep(1)
            return cmd
        else:
            print('\033[31mComando inválido, tente novamente.\033[0m\n')
            
def check_on_hp():
    import player
    if player.data['hp'] > player.data['hpmax']:
        player.data['hp'] = player.data['hpmax']
        return None

def stylized_text(text, time):
    from time import sleep
    for word in text:
        print(word, end = '', flush = True)
        sleep(time)
    sleep(1)
    return None

def get_weapon_values(weapon_name):
    import items
    for weapons in items.data['weapons'].values():
        if weapon_name in weapons:
            return weapons[weapon_name]
    else:
        return print('Valor não encontrado')
        
