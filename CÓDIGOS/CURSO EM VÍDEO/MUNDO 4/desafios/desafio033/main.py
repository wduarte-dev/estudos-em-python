from desafio033 import Aluno
from rich import inspect

a1 = Aluno('Wellington', 2003, 'EIM')
a1.add_curso('ENG')
a1.curso = 'eng'
a1.add_curso('moda')
print(a1.curso)
a1.nascimento = 2008
inspect(a1, private=True, methods=True)