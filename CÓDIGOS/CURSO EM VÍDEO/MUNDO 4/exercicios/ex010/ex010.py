from dataclasses import dataclass

@dataclass
class Avaliacao:
    nome : str
    disciplina : str
    _nota : float = 0 # Atributo protegido (#)

    @property
    def nota(self): # GETTER (ao usar a1.nota)
        return self._nota
    
    @nota.setter # SETTER (ao usar a1.nota = float)
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
            return None
        print('Nota inválida.')
    
    @nota.deleter
    def nota(self): # Ao usar del a1.nota
        self._nota = 0
    
a1 = Avaliacao('Wellington', 'Python', 2.5)
a1.nota = 8
print(a1.nota)
del a1.nota
print(a1.nota)

