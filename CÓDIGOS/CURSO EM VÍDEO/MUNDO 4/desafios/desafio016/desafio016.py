# Desafio começa no 16 por que os anteriores eram teóricos (múltipla escolha / dissertativos)
from rich import print
from rich import inspect
class Funcionario:
    empresa = 'DUARTECH'
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self) -> str:
        return f':handshake: Olá! Eu sou [blue]{self.nome}[/], {self.cargo} do setor de {self.setor} na empresa [blue]{Funcionario.empresa}[/].'

f1 = Funcionario('Carlos', 'TI', 'Programador')
f2 = Funcionario('Maria', 'Administração', 'Diretora')
f3 = Funcionario('Lara', 'Moda', 'Estilista')
print(f1.apresentação())
print(f2.apresentação())
print(f3.apresentação())
# inspect(f1, methods=True)