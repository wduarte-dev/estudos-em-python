from dataclasses import dataclass
from pessoa import Pessoa
@dataclass
class Aluno(Pessoa):
    curso : str = ''
    turma : str = ''

    def fazer_matricula(self, novo_curso) -> None:
        self.curso = novo_curso
        self.turma = '1° ano'