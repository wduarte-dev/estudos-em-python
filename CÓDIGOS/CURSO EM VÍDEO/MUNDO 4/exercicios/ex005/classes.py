from dataclasses import dataclass
@dataclass
class Pessoa:
    nome : str = ''
    idade : int = 0

    def fazer_aniversario(self):
        self.idade += 1

@dataclass
class Aluno(Pessoa):
    curso : str = ''
    turma : str = ''

    def fazer_matricula(self, novo_curso) -> None:
        self.curso = novo_curso
        self.turma = '1° ano'

@dataclass
class Professor(Pessoa):
    especialidade : str = ''
    nivel : str = ''

    def dar_aula(self, aula) -> str:
        return f'O professor {self.nome} está dando aula de {aula}!'
        

@dataclass
class Funcionario(Pessoa):
    cargo : str = ''
    setor : str = ''

    def bater_ponto(self, horario):
        return f'{self.nome} bateu seu ponto às {horario}.'

