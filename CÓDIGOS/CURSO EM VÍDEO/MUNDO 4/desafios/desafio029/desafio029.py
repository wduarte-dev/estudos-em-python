from rich import inspect

class Diario:
    def __init__(self, senha = 'w3ll1@'):
        self.__senha = senha
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError('A senha não pode ser revelada.')
    
    def escrever(self, mensagem):
        self.__segredos.append(mensagem)
    
    def ler(self, senha = ''):
        if senha != self.__senha:
            raise PermissionError('A senha é inválida.')
        for linha in self.__segredos:
            print(f'- {linha}')

d1 = Diario('senha123')
d1.escrever('Hoje eu aprendi a criar um diário em python.')
d1.escrever('Posso escrever, mas só posso ler se informar a senha.')
d1.escrever('Pão de queijo é bom demais!')
d1.ler('senha123')
inspect(d1, private=True, methods=True)
