from rich.panel import Panel
from rich import print
from os import system
import os
class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 1
        self._display_de_volume = [
            '[----------]', '[▒---------]', '[▒▒--------]', '[▒▒▒-------]', '[▒▒▒▒------]', '[▒▒▒▒▒-----]',
            '[▒▒▒▒▒▒----]', '[▒▒▒▒▒▒▒---]', '[▒▒▒▒▒▒▒▒--]', '[▒▒▒▒▒▒▒▒▒-]', '[▒▒▒▒▒▒▒▒▒▒]'
        ]
        self._display_de_canais = ['[white on yellow] 1 [/] 2  3  4  5', 
        '1  [white on yellow] 2 [/] 3  4  5',
        '1  2  [white on yellow] 3 [/] 4  5',
        '1  2  3  [white on yellow] 4 [/] 5',
        '1  2  3  4  [white on yellow] 5 [/]']

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def menu_de_volume(self):
        global menu_vol
        menu_vol = '-' + f' VOL{self.volume} ' + '+'
    
    def menu_de_canais(self):
        global menu_ch
        menu_ch = '<' + f' CH{self.canal} ' + '>'

    def tela(self):
        tela_da_tv = Panel.fit(renderable='', title='[ TV ]')
        self.menu_de_canais()
        self.menu_de_volume()
        botoes_da_tv = menu_ch + '  ' + menu_vol

        if self.ligada:
            tela_da_tv.renderable = f'CANAL = {self._display_de_canais[self.canal - 1]}\nVOLUME = {self._display_de_volume[self.volume]}'
            print(tela_da_tv)
            print(botoes_da_tv, end = ' ')

        elif not self.ligada:
            tela_da_tv.renderable = ':prohibited: [red]A TV ESTÁ DESLIGADA'
            print(tela_da_tv)
    
    def tv(self):
        while True:
            system('clear' if os.name == 'posix' else 'cls')
            self.tela()
            cmd = input('')
            match cmd:
                case '@': self.desligar() if self.ligada else self.ligar()
                case '+': 
                    if self.ligada:
                        self.volume += 1 if self.volume != 10 else 0
                case '-': 
                    if self.ligada:
                        self.volume -= 1 if self.volume != 0 else 0
                case '>': 
                    if self.ligada:
                        self.canal = self.canal + 1 if self.canal != 5 else 1
                case '<': 
                    if self.ligada:
                        self.canal = self.canal - 1 if self.canal != 1 else 5
                case '0': exit()
                case _: None

t1 = Televisão()
t1.tv()