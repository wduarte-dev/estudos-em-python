'ESTRUTURA SIMPLES (E INICIANTE) DE CLASSES E OBJETOS EM POO'

class Pessoa:
    def __init__(self): # Método Construtor
        self.nome = 'Desconhecido'
        self.idade = 0
        self.altura = 0

    # Métodos da classe
    def envelhecer(self, anos):
        self.idade += anos
    def cartório(self, nome):        
        self.nome = nome
    def definir_altura(self, altura):
        self.altura = altura
    def crescer(self):
        self.altura += 0.1
    def dados(self):
        return f'O nome é {self.nome}, tem {self.idade} anos e {self.altura:.2f}m de altura'

'VOCÊ PODE ATUALIZAR OS DADOS ATRAVÉS DE MÉTODOS'
Usuário1 = Pessoa()
Usuário1.envelhecer(17) # O mesmo que Pessoa.envelhecer(Usuário, 17)
Usuário1.cartório('Wellington')
Usuário1.definir_altura(1.84)
print(Usuário1.dados())

'VOCÊ PODE ATUALIZAR OS DADOS DIRETAMENTE ATRAVÉS DOS ATRIBUTOS'
Usuário2 = Pessoa()
Usuário2.idade = 13
Usuário2.nome = 'Lara'
Usuário2.altura = 1.75
print(Usuário2.dados())
