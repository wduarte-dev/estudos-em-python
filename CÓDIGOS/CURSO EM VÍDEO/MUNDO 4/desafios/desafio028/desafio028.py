from dataclasses import dataclass
from rich.panel import Panel
from rich import print
from os import system, name

@dataclass
class Termostato:
    __temperatura = 24.0

    def __post_init__(self):
        self.display()

    @property # é um getter
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter # é um setter
    def temperatura(self, valor):
        if 16 <= valor <= 30 and valor % 0.5 == 0:
            self.__temperatura = valor
            return None
        return None
    
    def display(self):
        while True:
            system('cls' if name == 'nt' else 'clear')
            termostato_display = Panel.fit(title='TERMOSTATO', renderable=f'{'TEMP. ATUAL':^15}\n' + f'{(' [cyan](-)[/] ' + f'{self.temperatura}°C' + ' [red](+)[/] '):^15}')
            print(termostato_display)
            try:
                cmd = input()
            except KeyboardInterrupt:
                exit()
            match cmd:
                case '+': self.temperatura += 0.5
                case '-': self.temperatura -= 0.5
                case _:
                    try:
                        self.temperatura = float(cmd)
                    except ValueError:
                        pass

t1 = Termostato()