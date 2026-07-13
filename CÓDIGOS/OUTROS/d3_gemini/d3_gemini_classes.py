# Criação de um tamagotchi com o atributo fome e métodos alimentar() e brincar()
class Pou:
    def __init__(self, name):
        self.name = name
        self.stamina = 100
        self.alive = True
    def play(self):
        if self.alive == False:
            print('But nothing can be done.')
        self.stamina -= 50
        if self.stamina < 0:
            print('Your pet dies of playing.')
            self.alive = False
    def eat(self, food):
        if self.alive == False:
            print('But nothing can be done.')
            return 0
        if food == 'hamburguer':
            self.stamina += 50
        elif food == 'fish':
            self.stamina += 100
        elif food == 'chips':
            self.stamina += 10


pou = Pou('Jorgin') # <- NUNCA, JAMAIS use um objeto com o mesmo nome da classe
pou.play()
pou.eat('hamburguer')
pou.play()
pou.play()
pou.eat('chips')
pou.eat('fish')
print(pou.stamina)
pou.play()
pou.play()
pou.play()
pou.eat('fish')