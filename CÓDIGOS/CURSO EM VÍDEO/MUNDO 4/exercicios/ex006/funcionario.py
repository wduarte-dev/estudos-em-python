from dataclasses import dataclass
from pessoa import Pessoa
@dataclass
class Funcionario(Pessoa):
    cargo : str = ''
    setor : str = ''

    def bater_ponto(self, horario):
        return f'{self.nome} bateu seu ponto às {horario}.'