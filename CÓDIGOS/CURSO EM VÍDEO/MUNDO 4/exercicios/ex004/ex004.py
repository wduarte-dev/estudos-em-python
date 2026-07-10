from dataclasses import dataclass
from rich import print, inspect
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

# BLOCO DE TESTES 1
a1 = Aluno('João', 19, 'Ciência da Computação', '1° ano')
p1 = Professor('Raimundo', 48, 'Tecnologia da Informação', 'Mestrado')
f1 = Funcionario('Ivânia', 39, 'Diretora', 'Educação')
inspect(a1, methods=True)
a1.fazer_aniversario()
print(a1.idade)
inspect(p1, methods=True)
inspect(f1, methods=True)

# BLOCO DE TESTES 2
a2 = Aluno('Jorge', 17)
a2.fazer_matricula('Estrutura e Análise de Dados')
a2.fazer_aniversario()
inspect(a2)

p2 = Professor('Carlos', 32, 'Teologia', 'Doutorado')
print(p2.dar_aula('Religiões de Matriz Africana'))

f2 = Funcionario('Cláudio', 28, 'Inspetor', 'Educação')
print(f2.bater_ponto('6:50'))

