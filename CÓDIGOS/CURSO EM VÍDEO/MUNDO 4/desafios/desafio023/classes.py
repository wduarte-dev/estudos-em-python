from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from math import sqrt

@dataclass
class Poligono(ABC):
    @property
    @abstractmethod
    def quantidade_de_lados(self) -> int:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass

@dataclass
class Triangulo(Poligono):
    tamanho_do_1o_lado : float = 0
    tamanho_do_2o_lado : float = 0
    tamanho_do_3o_lado : float = 0

    def __post_init__(self):
        a = self.tamanho_do_1o_lado
        b = self.tamanho_do_2o_lado
        c = self.tamanho_do_3o_lado

        if (a+b <= c) or (a+c <= b) or (b+c <= a):
            raise ValueError('The triangle must exist.')

    @property
    def quantidade_de_lados(self):
        return 3

    def perimetro(self):
        return self.tamanho_do_1o_lado + self.tamanho_do_2o_lado + self.tamanho_do_3o_lado

    def area(self):
        p = self.perimetro() / 2
        lado1 = self.tamanho_do_1o_lado
        lado2 = self.tamanho_do_2o_lado
        lado3 = self.tamanho_do_3o_lado
        return sqrt(p * (p - lado1) * (p - lado2) * (p - lado3))


@dataclass
class Quadrado(Poligono):
    tamanho_do_lado : float = 0

    @property
    def quantidade_de_lados(self):
        return 4

    def perimetro(self):
        return self.tamanho_do_lado * 4
    
    def area(self):
        return self.tamanho_do_lado ** 2


@dataclass
class Retangulo(Poligono):
    base: float = 0
    altura: float = 0

    @property
    def quantidade_de_lados(self):
        return 4
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

    def area(self):
        return self.base * self.altura
    
