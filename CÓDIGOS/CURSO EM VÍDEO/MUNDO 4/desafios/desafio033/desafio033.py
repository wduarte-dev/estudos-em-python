from abc import ABC
from dataclasses import dataclass
from datetime import date

@dataclass
class Pessoa(ABC):
    _nome : str 
    _nascimento : int


    def __post_init__(self):
        self.idade

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        try:
            ano_atual = date.today().year
            if ano < ano_atual and ano > 1875:
                self._nascimento = ano
                return None
            raise ValueError('O ano de nascimento é inválido.')
        except:
            print('\033[31mErro desconhecido, verifique as informações e tente novamente.\033[0m')
            exit()
        
    
    @property
    def idade(self):
        ano_atual = date.today().year
        if self._nascimento < ano_atual and self._nascimento > 1875:
            return ano_atual - self._nascimento
        raise ValueError('O ano de nascimento especificado é inválido.')
    
    @idade.setter
    def idade(self, idade):
        raise PermissionError('A idade não pode ser alterada, para isso, altere a data de nascimento.')

@dataclass
class Aluno(Pessoa):
    _curso : str

    def __post_init__(self):
        self.cursos_oficiais : list[str] = ['ADM', 'AUT', 'EIM', 'ADS']
        if self._curso in self.cursos_oficiais:
            pass
        else:
            raise ValueError('Curso especificado não existe.')

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso.upper() in self.cursos_oficiais:
            self._curso = curso.upper()
            return None
        raise ValueError('O curso especificado não existe.')

    def add_curso(self, curso):
        if curso.upper() in self.cursos_oficiais:
            raise ValueError('O curso especificado já existe.')
        self.cursos_oficiais.append(curso.upper())