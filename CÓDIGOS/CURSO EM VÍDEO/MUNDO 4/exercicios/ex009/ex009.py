from dataclasses import dataclass

@dataclass
class Avaliacao:
    nome : str
    disciplina : str
    _nota : float = 0 # Atributo protegido (#)

    def get_nota(self): # Método GETTER
        return self._nota

    def set_nota(self, valor): # Método SETTER
        if 0 <= valor <= 10:
            self._nota = valor
            return None
        print('Nota inválida.')

a1 = Avaliacao('Wellington', 'Python', 2.5)
a1.set_nota(8)
print(a1.get_nota())
