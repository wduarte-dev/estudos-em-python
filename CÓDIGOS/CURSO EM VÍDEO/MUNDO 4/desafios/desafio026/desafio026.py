from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from rich.panel import Panel
from rich import print

@dataclass
class Funcionario(ABC):
    nome : str
    _inss_aliquota : list[float] = field(default_factory=lambda: [7.5, 9, 12, 14], init=False)
    _inss_salarios : list[float] = field(default_factory=lambda: [1621, 2902.84, 4354.27], init=False)
    _inss_parcela_a_deduzir : list[float] = field(default_factory=lambda: [0, 24.32, 111.4, 198.49], init=False)
    _salario_minimo : float = field(default_factory=lambda: 1612, init=False)
    _salario : float = field(default_factory=lambda: 0, init=False)

    @property
    def salario(self):
        return self._salario

    @property
    def salario_minimo(self):
        return self._salario_minimo

    @property
    def inss_aliquota(self) -> list[float]:
        return self._inss_aliquota

    @property
    def inss_salarios(self) -> list[float]:
        return self._inss_salarios
    
    @property
    def inss_parcela_a_deduzir(self) -> list[float]:
        return self._inss_parcela_a_deduzir

    @abstractmethod
    def calcular_salario(self) -> float:
        pass
    
    def desconto_inss(self):
        DESCONTO_MAXIMO = 988.09
        if self._salario <= self._inss_salarios[0]:
            desconto = (self._salario * self._inss_aliquota[0]/100) - self._inss_parcela_a_deduzir[0]
        elif self._salario <= self._inss_salarios[1]:
            desconto = (self._salario * self._inss_aliquota[1]/100) - self._inss_parcela_a_deduzir[1]
        elif self._salario <= self._inss_salarios[2]:
            desconto = (self._salario * self._inss_aliquota[2]/100) - self._inss_parcela_a_deduzir[2]
        else:
            desconto = (self._salario * self._inss_aliquota[3]/100) - self._inss_parcela_a_deduzir[3]
        if desconto > DESCONTO_MAXIMO:
            desconto = DESCONTO_MAXIMO
        return desconto

    def analisar_salario(self):
        salario = self.calcular_salario()
        painel = Panel.fit(title='ANÁLISE DE SALÁRIO', renderable=f'''O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${salario:.2f}[/]
e corresponde a [yellow]{(salario / self._salario_minimo):.1f} salários mínimos.[/]''')
        print(painel)

        

@dataclass
class Horista(Funcionario):
    valor_hora : float 
    horas_trabalhadas : int

    def calcular_salario(self):
        self._salario = self.valor_hora * self.horas_trabalhadas
        return self._salario - self.desconto_inss()
        
@dataclass
class Mensalista(Funcionario):
    salario_bruto : float

    def calcular_salario(self) -> float:
        self._salario = self.salario_bruto
        return self._salario - self.desconto_inss()

f1 = Mensalista('Wellington', 5000)
print(f1.calcular_salario())
f1.analisar_salario()


f2 = Horista('Paulo', 12, 200)
print(f2.calcular_salario())
f2.analisar_salario()

f3 = Mensalista('Amanda', 9500)
print(f3.calcular_salario())
f3.analisar_salario()




