from rich import print
class Caneta:
    def __init__(self, modelo = 'Não informado', cor = 'Não informado', tampada = True):
        self.modelo = modelo
        self.cor = cor
        self.tampada = tampada

    def destampar(self):
        self.tampada = False
        
    def tampar(self):
        self.tampada = True
        
    def escrever(self, msg):
        if self.tampada:
            print('[yellow]Você não pode escrever com a caneta tampada![/]')
        else:
            if self.cor == 'Não informado':
                print('ERRO! A caneta está sem tinta!')
                return
            elif self.cor == 'azul':
                print('[blue]' + msg + '[/]')
            elif self.cor == 'vermelha':
                print('[red]' + msg + '[/]')
            elif self.cor == 'verde':
                print('[green]' + msg + '[/]')

c1 = Caneta(modelo = 'BIC', cor = 'vermelha')
c2 = Caneta(modelo = 'FABER CASTELL', cor = 'azul')
c3 = Caneta(modelo = 'MARCA DESCONHECIDA', cor = 'verde')
c1.escrever('Testando caneta vermelha...')
c1.destampar()
c1.escrever('Agora sim posso escrever!')
c2.destampar()
c2.escrever('Testando caneta azul...')
c3.destampar()
c3.escrever('Testando caneta verde...')
c3.tampar()
c3.escrever('A caneta está tampada, eu não posso escrever com ela assim!')


