from dataclasses import dataclass
from hashlib import sha256
from rich import inspect

@dataclass
class Credencial:
    __hash = ''
    
    @property
    def senha(self):
        return None

    @senha.setter
    def senha(self, senha) -> None:
        self.__hash = sha256(senha.encode('utf-8')).hexdigest()

    def validar(self, senha):
        validacao_hash = sha256(senha.encode('utf-8')).hexdigest()
        if self.__hash == validacao_hash:
            return True
        return False

c1 = Credencial()
c1.senha = 'wellington00'
print(c1.senha)                         # retorna None
inspect(c1, private=True, methods=True)
print(c1.validar('wellington00'))       # retorna True
print(c1.validar('w3ll1ngt0n00@'))      # retorna False