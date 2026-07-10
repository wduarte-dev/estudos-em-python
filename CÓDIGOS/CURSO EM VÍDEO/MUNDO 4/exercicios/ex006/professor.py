from dataclasses import dataclass
from pessoa import Pessoa
@dataclass
class Professor(Pessoa):
    especialidade : str = ''
    nivel : str = ''

    def dar_aula(self, aula) -> str:
        return f'O professor {self.nome} está dando aula de {aula}!'