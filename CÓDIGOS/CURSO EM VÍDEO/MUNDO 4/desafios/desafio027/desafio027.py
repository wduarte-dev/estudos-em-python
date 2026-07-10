from abc import ABC, abstractmethod
from random import randint, choices
from dataclasses import dataclass, field
from time import sleep
from rich import print

@dataclass
class Personagem(ABC):
    nome : str
    vida : int

    @property
    @abstractmethod
    def golpes(self) -> list[str]:
        pass

    def atacar(self, alvo, forca) -> None:
        golpe_usado = choices(self.golpes, k=1)[0]
        print(f'[bold green]{self.nome}[/]([dark green]{self.vida}[/]) atacou [red]{alvo.nome}[/]([dark green]{alvo.vida}[/]) com [blue]{golpe_usado}[/] de [bold dark blue]{forca}[/] de força!')
        dano = randint(0, forca)
        alvo.receber_dano(dano)

    def receber_dano(self, dano) -> None:
        self.vida -= dano
        print(f'[red]{self.nome}[/] recebeu [red]{dano}[/] de dano!')
        self.game_over()

    def game_over(self):
        if self.vida <= 0:
            print(f'[red]{self.nome} morre com o golpe fatal![/]')
            exit()
    
    @abstractmethod
    def curar(self) -> None:
        pass

@dataclass
class Guerreiro(Personagem):
    def curar(self):
        cura = randint(0, 5)
        self.vida += cura
        print(f'[red]{self.nome}[/] usou [green]Poção de Saúde[/] e curou [green]{cura}HP![/]')
    
    @property
    def golpes(self):
        return ['Corte Diagonal', 'Corte Horizontal', 'Mordhau']

@dataclass
class Mago(Personagem):
    def curar(self):
        cura = randint(0, 8)
        self.vida += cura
        print(f'[red]{self.nome}[/] usou [green]Magia Regeneradora[/] e curou [green]{cura}HP![/]')
    
    @property
    def golpes(self):
        return ['Bola de Fogo', 'Ataque Rápido', 'Magia Perfurante']

# RINHA INSANA PLACAR P1 X P2 -> 1x3
p1 = Guerreiro('Garland', 20) # GUERREIRO TEM + VIDA, - ATAQUE, - CURA e COMBO (ataca duas vezes)
p2 = Mago('Beltraus', 15) # MAGO TEM - VIDA, + ATAQUE, + CURA

while True:
    p1.atacar(p2, randint(0, 10))
    sleep(1)
    p1.atacar(p2, randint(0, 5))
    sleep(5)
    p2.curar()
    print()
    sleep(2)
    p2.atacar(p1, randint(0, 15))
    sleep(5)
    p1.curar()
    print()
    sleep(2)
