from dataclasses import dataclass
@dataclass
class Retangulo:
    _base : float = 1
    _altura : float = 1
    _area : float = 1

    def atualizar_area(self):
        self._area = abs(self._base * self._altura)

    def __post_init__(self):
        self.atualizar_area()

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, valor):
        raise ValueError('A área não pode ser alterada se a base e a altura são fixas.')
    
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        try:
            self._base = abs(valor)
            self.atualizar_area()
        except:
            raise ValueError('A medida da base fornecida é inválida.')

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        try:
            self._altura = abs(valor)
            self.atualizar_area()
        except:
            raise ValueError('A medida da altura fornecida é inválida.')

    @property
    def medidas(self):
        return f'Base: {self._base}\nAltura: {self._altura}\nÁrea: {self._area}'
    
    @medidas.setter
    def medidas(self, valor : tuple):
        try:
            self._base = abs(valor[0])
            self._altura = abs(valor[1])
            self.atualizar_area()
        except:
            raise ValueError('As medidas fornecidas são inválidas.')