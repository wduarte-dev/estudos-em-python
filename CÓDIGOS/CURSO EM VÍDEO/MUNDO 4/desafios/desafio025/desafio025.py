from abc import ABC, abstractmethod
from dataclasses import dataclass
from rich.table import Table
from rich import print

@dataclass
class Transporte(ABC):
    distancia : float = 0
    @abstractmethod
    def calc_frete(self) -> float | str:
        pass

    def tabela_de_fretes(self, *meios_de_transporte):
        pass

class Moto(Transporte):
    def calc_frete(self) -> float | str:
        return f'R${0.5 * self.distancia:.2f}'

class Caminhao(Transporte):
    def calc_frete(self) -> float | str:
        if self.distancia < 50:
            return 'Não disponível.'
        return f'R${1.2 * self.distancia:.2f}'

class Drone(Transporte):
    def calc_frete(self) -> float | str:
        if self.distancia > 10:
            return 'Não disponível.'
        return f'R${9.5 * self.distancia:.2f}'

# BLOCO DE TESTES 1
distancia1 = 8
transporte1 = Drone(distancia1)
print(f'A entrega de {type(transporte1).__name__} numa distância de {transporte1.distancia}km é igual a {transporte1.calc_frete()}')

transporte2 = Moto(distancia1)
print(f'A entrega de {type(transporte2).__name__} numa distância de {transporte2.distancia}km é igual a {transporte2.calc_frete()}')

transporte3 = Caminhao(distancia1)
print(f'A entrega de {type(transporte3).__name__} numa distância de {transporte3.distancia}km é igual a {transporte3.calc_frete()}')

# BLOCO DE TESTES 2
distancia2 = 80
tabela = Table(show_lines=True)
tabela.add_column('Distância (km)', justify='center')
tabela.add_column('Meio', justify='center')
tabela.add_column('Frete (R$)')
lista_de_transportes = [Moto(distancia2), Caminhao(distancia2), Drone(distancia2)]
for meio_de_transporte in lista_de_transportes:
    tabela.add_row(f'{meio_de_transporte.distancia}km', f'{type(meio_de_transporte).__name__}', f'{meio_de_transporte.calc_frete()}')
print(tabela)