from dataclasses import dataclass
@dataclass
class Funcionario:
    nome : str = 'Não especificado'
    salario_base : float = 0

    def calcular_salario(self) -> float:
        return self.salario_base

@dataclass
class Gerente(Funcionario):
    bonus : float = 0

    def calcular_salario(self) -> float:
        return self.salario_base + self.bonus

@dataclass
class Vendedor(Funcionario):
    vendas_feitas : int = 0
    comissao : float = 0

    def calcular_salario(self) -> float:
        return self.salario_base + (self.vendas_feitas * self.comissao)

g1 = Gerente('Flávio', 2500, 250)
v1 = Vendedor('Daniela', 1250, 35, 5)
print(v1.calcular_salario())
print(g1.calcular_salario())