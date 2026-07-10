'MELHORIA DO EX001'
class Pessoa:
    '''
    Essa classe, quando instanciada faz com que o objeto obtenha os atributos nome, idade e altura.
    Para usá-la:
    object = Pessoa(nome, idade, altura)
    '''
    def __init__(self, nome = 'Desconhecido', idade = 0, altura = 0): # Método Construtor
        self.nome = nome
        self.idade = idade
        self.altura = altura

    # Métodos da classe
    def envelhecer(self, anos):
        self.idade += anos
    def crescer(self):
        self.altura += 0.1
    def __str__(self): # Retorna a operação abaixo quando printado (print(objeto))
        return f'O nome é {self.nome}, tem {self.idade} anos e {self.altura:.2f}m de altura'
    def __getstate__(self):
        return 'Para acessar o dicionário, use objectname.__dict__'

Usuário1 = Pessoa('Wellington', 17, 1.8)
print(Usuário1) # aqui que o def __str__(self) age
print(Pessoa.__doc__) # aqui que a docstring age
print(Usuário1.__dict__) # mostra o estado do objeto em formato de dicionário (muito útil para JSON)
print(Usuário1.__getstate__()) # mesmo que o dunder dict, mas o retorno pode ser alterado no def __getstate__(self)
print(Usuário1.__class__) # exibe a classe do objeto