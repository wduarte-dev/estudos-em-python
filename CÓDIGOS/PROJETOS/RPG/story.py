from time import sleep
from utils import cmd_input, stylized_text
from combat import game_over
import ascii

def game_start():
    print('-='*25)
    input('Pressione ENTER para iniciar sua jornada...')
    print('-='*25)
    for c in range(1, 50):
        print('▒█'*25)
        sleep(0.15)
    return None
        
        
        
        
        
        
        
        
        
def game_initial_dialogue():
    import player
    stylized_text(f'''
...
''', 1)
    cmd_input('1 > Abrir os olhos.\n  > ', ['1'])

    sleep(5)
    stylized_text(f'''
"..."

"Bem-vindo novamente ao jogo."
"Talvez tenha se esquecido das regras,"
"mas vamos ao início..."

"Qual é o seu nome?"
''', 0.10)
    
    player.data['name'] = input('> ')

    sleep(1)
    stylized_text(f'''
"..."
"{player.data['name']}?"
''', 0.10)

    sleep(3)
    stylized_text(f'''
"Você sabe por que está aqui?"
''', 0.10)

    cmd_input('[1] "Não."\n   > ', ['1'])

    sleep(2)
    stylized_text(f'''
"Sim, eu já sabia."
"Você descobrirá eventualmente."
''', 0.10)

    sleep(2)
    stylized_text(f'''
"Tome isto, lhe será útil."
''', 0.10)

    cmd_input('[1] Pegar o isqueiro que foi jogado no chão.\n   > ', ['1'])
    sleep(1)
    print('Isqueiro adicionado ao inventário.')
    player.inventory.append('Isqueiro')

    sleep(2)
    stylized_text(f'''
"Seu inventário. Poderá acessá-lo em ocasiões específicas..."
"Seja cauteloso."
"..."
"Acenda o isqueiro."
''', 0.10)

    cmd_input('[1] Acender o isqueiro.\n   > ', ['1'])

    sleep(1)
    stylized_text(f'''
Com a luz do isqueiro, você não consegue ver nada
a não ser um caminho escuro.
''', 0.10)

    sleep(2)
    stylized_text(f'''
"Está vendo? Há um caminho possível na sua frente."
"Você terá caminhos para escolher..."
"E eventuais lutas."
"Seu objetivo é sobreviver."
"..."
"Embora os outros não tenham conseguido."
''', 0.10)

    sleep(2)
    stylized_text('''
"..."
"Espero que você não me dê problemas."
''', 0.10)
    
    sleep(2)
    cmd_input('[1] Seguir em frente\n   > ', ['1'])

    sleep(1)
    stylized_text('''
Você segue pelo único caminho disponível,
por um local que parece ser uma caverna.
''', 0.05)
    return None











def sixth_sense_chest():
    import player
    curse_n = 0
    sleep(1)
    stylized_text('''
Você achou um baú!
''', 0.05)
    while True:
        cmd = cmd_input('Deseja abrí-lo? (s) / \033[9m(n)\033[0m ', ['s', 'n'])
        if cmd == 'n':
            curse_n += 1
            if curse_n == 2:
                stylized_text(f'''
"..."
Um som estremece a caverna.
Uma lança atravessa seu pescoço.
"..."
"Eu te avisei, {player.data['name']}."
''', 0.10)
                player.data['hp'] = 0
                game_over()
            else:
                stylized_text('''
"..."
"Abra o baú e siga as regras."
"Você não quer morrer, quer?"
''', 0.25)
                continue
        else:
            break
        
    sleep(2)
    print(f'Item dado: \033[33mLente!\033[0m')
    sleep(1)
    
    while True:
        cmd = cmd_input('\nDeseja equipar? (s) / \033[9m(n)\033[0m ', ['s', 'n'])
        if cmd == 's':
            player.data['6th_sense'] = True
            print(f'Você coloca a lente nos seus olhos...')
            break
        elif cmd == 'n':
            curse_n += 1
            if curse_n == 2:
                stylized_text(f'''
Uma lança impetuosa atravessa seu pescoço.
"..."
"Eu te avisei, {player.data['name']}."
''', 0.10)
                player.data['hp'] = 0
                game_over()
            else:
                stylized_text('''
"..."
"Coloque a lente e siga as regras."
"Você não quer morrer, quer?"
''', 0.25)
                continue
    sleep(3)
    print('\n\033[35mSua percepção do local melhora...\033[0m')
    sleep(2)
    print('\nEscolhas com possíveis riscos agora são destacadas em \033[31mVERMELHO\033[0m.')

    
    
    
    
    
    



def rat_initial_combat_story():
    from combat import combat
    import player
    sleep(1)
    stylized_text('''
Ao olhar para frente, você encontra mais um caminho.
...
Mas sua intuição agora diz que não há algo muito amigável lá.
''', 0.05)

    sleep(2)
    cmd_input('\033[31m[1] Seguir em frente\033[0m\n   > ', ['1'])

    sleep(1)
    stylized_text('''
Você segue em frente.
...
''', 0.05)

    sleep(2)
    stylized_text('''
E se depara com uma figura assustadora...
''', 0.10)

    sleep(3)
    ascii.rat_ascii_stare()
    sleep(5)
    stylized_text('''
Isto te encara profundamente.
Os olhos estão famintos.
E a boca está suja de sangue...
Você permanece imóvel.
''', 0.10)

    sleep(3)
    stylized_text(f'''
"Você já deve ter percebido, {player.data['name']}."
"Nada aqui é normal."
"Nem este rato gigante."
"..."

''', 0.10)
    sleep(3)

    player.data['area'] = 'rat_initial_battle'
    combat('Rato selvagem')

    sleep(3)
    stylized_text(f'''
"Escute, {player.data['name']},"
"Sua missão é me trazer esta lente."
"..."
"Em troca, te tirarei desse lugar."
''', 0.10)

    sleep(1)
    stylized_text(f'''
"Não será fácil."
"..."
"Não termine como os outros."
''', 0.10)

    sleep(1)
    stylized_text(f'''
"Se tentar quebrar as regras..."
''', 0.10)

    sleep(1)
    stylized_text(f'''
"Eu acabarei com a sua vida."
''', 0.25)

    cmd_input('[1] Seguir em frente\n   > ', ['1'])