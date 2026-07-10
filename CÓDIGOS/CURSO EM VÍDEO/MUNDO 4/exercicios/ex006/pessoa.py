from dataclasses import dataclass
@dataclass
class Pessoa:
    nome : str = ''
    idade : int = 0

    def fazer_aniversario(self):
        self.idade += 1