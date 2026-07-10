from dataclasses import dataclass
from abc import ABC, abstractmethod # importa o módulo Abstract Base Class
@dataclass
class Pessoa(ABC): # Torna a classe "Pessoa" uma classe abstrata que não pode ser instanciada.
    nome : str = ''
    idade : int = 0

    def fazer_aniversario(self):
        self.idade += 1
    @abstractmethod # cria um método abstrato, obrigando todas as subclasses a tê-lo com instruções específicas
    def estudar(self, materia) -> str:  # observe que todas as subclasses de alguma forma estudam, mas de um modo diferente.
        pass

@dataclass
class Aluno(Pessoa):
    curso : str = ''
    turma : str = ''

    def fazer_matricula(self, novo_curso) -> None:
        self.curso = novo_curso
        self.turma = '1° ano'
    
    def estudar(self, materia):
        return f'O aluno {self.nome} do {self.turma} está estudando {materia} na biblioteca.'


@dataclass
class Professor(Pessoa):
    especialidade : str = ''
    nivel : str = ''

    def dar_aula(self, aula) -> str:
        return f'O professor {self.nome} está dando aula de {aula}!'

    def estudar(self, materia):
        return f'O professor {self.nome} de {self.especialidade} está estudando {materia} para dar aula.'
        

@dataclass
class Funcionario(Pessoa):
    cargo : str = ''
    setor : str = ''

    def bater_ponto(self, horario):
        return f'{self.nome} bateu seu ponto às {horario}.'

    def estudar(self, materia):
        return f'O(a) funcionário(a) {self.nome}, {self.cargo} do setor de {self.setor} está estudando {materia}.'