from hashlib import sha256
from stdiomask import getpass
class ContaBancaria:
    '''
    Sistema de saques e depósitos simples.
    Instância: ContaBancaria(id, titular, saldo)
    '''

    def __init__(self, id, titular, saldo = 0, senha = None):
        self._id = id 
        self._titular = titular 
        self.__saldo = saldo 
        self.__senha = senha
        self.__post_init__()
    
    def validar_senha(self, senha):
        if senha is None:
            senha = getpass(f'[{self._titular.upper()}] Digite a senha: ')
        hash_senha_informada = sha256(senha.encode('utf-8')).hexdigest()
        if hash_senha_informada != self.__hash:
            raise PermissionError('Permissão negada.')
        return None
            
    def __post_init__(self):
        if self.__senha is None:
            self.__senha = getpass(f'[{self._titular.upper()}] Digite a senha: ')
        self.__hash = sha256(self.__senha.encode('utf-8')).hexdigest()
        del self.__senha

    def sacar(self, valor, senha = None):
        self.validar_senha(senha)
        if self.__saldo >= abs(valor):
            self.__saldo -= abs(valor)
            print('Saque autorizado.')
            return None
        print('\033[31mSALDO INSUFICIENTE\033[0m')

    def depositar(self, valor):
        self.__saldo += abs(valor)
        print('Depósito autorizado.')
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, senha = None):
        self.validar_senha(senha)
        self._titular = input('Novo titular: ')

    @property
    def saldo(self):
        self.validar_senha(senha = None)
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        raise PermissionError('Erro ao alterar o saldo diretamente.')
        

    def __str__(self):
        return f'{self.__dict__}'