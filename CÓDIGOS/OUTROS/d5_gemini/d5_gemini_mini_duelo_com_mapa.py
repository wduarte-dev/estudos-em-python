from abc import ABC
from rich import print
from rich.console import Console
from os import system
from dataclasses import dataclass
class Batalha:
    @staticmethod
    def gerar_mapa(p1, p2):
        mapa = [ [[' '] for _ in range(11)] for _ in range(11) ]
        mapa[p1.y][p1.x].pop()
        mapa[p1.y][p1.x].append('*')
        mapa[p2.y][p2.x].pop()
        mapa[p2.y][p2.x].append('@')
        print(f'[red]{p1.nome} (*): {p1.hp}HP[/]')
        print(*mapa)
        print(f'[blue]{p2.nome} (@): {p2.hp}HP[/]\n')

@dataclass
class Personagem(ABC):
    nome : str = 'Desconhecido'
    poder : float = 10
    x : int = 0
    y : int = 0
    hp : float = 100

    def acao(self, input_var, obj_oponente):
        match input_var:
                case 'w': self.y -= 1 if self.y != 0 else 0
                case 'a': self.x -= 1 if self.x != 0 else 0
                case 's': self.y += 1 if self.y != 10 else 0
                case 'd': self.x += 1 if self.x != 10 else 0
                case 'q': self.atacar(obj_oponente)
                case _: pass
    
    def atacar(self, alvo : Personagem):
        alvo.hp -= self.poder
        if alvo.hp <= 0:
            self.game_over(alvo)
    
    def game_over(self, alvo):
        print(f'[red]{alvo.nome} morre brutalmente.[/]\n[blue]{self.nome} pode comemorar a vontade![/]')
        exit()

@dataclass
class Guerreiro(Personagem):
    def __post_init__(self):
        self.hp = 150
        self.poder = 25
        self.x = 0
        self.y = 0
    
    def atacar(self, alvo : Personagem):
        distancia_x = abs(self.x - alvo.x)
        distancia_y = abs(self.y - alvo.y)
        if distancia_x <= 1 and distancia_y <= 1:
            super().atacar(alvo)
            print('[red]P1: Executa um ataque em cheio![/]')
            input()
            return None
        print('[red]P1: Impossível atacar o alvo.[/]')
        input()

@dataclass
class Arqueiro(Personagem):
    def __post_init__(self):
        self.flechas : int = 50
        self.poder = 18
        self.x = 10
        self.y = 10

    def atacar(self, alvo : Personagem):
        if (alvo.x == self.x or alvo.y == self.y) and self.flechas > 0:
            self.flechas -= 1
            super().atacar(alvo)
            print('[red]P2: Acerta uma flechada em cheio![/]')
            input()
            return None
        print('[blue]P2: Impossível atirar no alvo.[/]')
        input()
        
console = Console()
p1 = Guerreiro('Garland, O Temido')
p2 = Arqueiro('Edgar, O Caça-Deuses')

def main():
    while True:
        Batalha.gerar_mapa(p1, p2)

        direcao1 = console.input('[red]P1 (*): [/]').lower().strip()
        p1.acao(direcao1, p2)

        direcao2 = console.input('[blue]P2 (@): [/]').lower().strip()
        p2.acao(direcao2, p1)

        system('clear')

if __name__ == '__main__':
    main()