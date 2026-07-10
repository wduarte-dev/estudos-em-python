from abc import ABC, abstractmethod
from time import sleep
from random import choices

def reticencias() -> None:
    for c in range(3):
            sleep(1)
            print('.', end = '', flush = True)
            sleep(1)
    print()

class BebidaQuente(ABC):
    def preparar(self):
        print('--  INICIANDO O PREPARO:  --')
        self.ferver_agua()
        self.extrair()
        self.servir()
        print('--      FINALIZADO!      --')

    def ferver_agua(self):
        temperatura = 24
        estado = 'morna'
        while True:
            tempo = choices([0.1, 0.2, 0.5, 1], k = 1)[0]
            txt = f'A água está {estado}, a temperatura de {temperatura}°C...            '
            print(f'{txt}', end = '\r', flush=True)
            match temperatura:
                case 50: estado = 'ficando quente'
                case 80: estado = 'começando a borbulhar'
                case 99: estado = 'fervendo'
                case 100: 
                    print(f'\r{txt}', end = '', flush=True)
                    sleep(2)
                    print()
                    break
            temperatura += 1
            sleep(tempo)

    @abstractmethod
    def extrair(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def extrair(self):
        print('Jogando água quente no coador', end = '')
        reticencias()
    
    def servir(self):
        print('Servindo numa xícara pequena', end = '')
        reticencias()

class Cha(BebidaQuente):
    def extrair(self):
        print('Colocando água na xícara com sachê', end = '')
        reticencias()
    
    def servir(self):
        print('Colocando açúcar e servindo numa xícara média', end = '')
        reticencias()

class Leite(BebidaQuente):
    def extrair(self):
        print('Colocando leite em pó e misturando', end = '')
        reticencias()
    
    def servir(self):
        print('Servindo num copo médio com café', end = '')
        reticencias()

cafe1 = Cafe()
cafe1.preparar()

cha1 = Cha()
cha1.preparar()

leite1 = Leite()
leite1.preparar()