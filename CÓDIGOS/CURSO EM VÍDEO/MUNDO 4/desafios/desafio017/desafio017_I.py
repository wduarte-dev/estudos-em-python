from rich.panel import Panel
from rich.console import Console
from rich.align import Align
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        renderable_param_upper = (' '*5) + self.nome + (' '*5)
        aligner = len(renderable_param_upper)
        # preco = 15500000
        eua_format = f'{self.preco:,.2f}'
        brazil_format = eua_format.replace(',', 'X').replace('.', ',').replace('X', '.')
        # saida = 15.500.000,00
        renderable_param_midlower = f'\n{'':-^{aligner}}\n{brazil_format:.^{aligner}}'
        painel = Panel.fit(renderable=renderable_param_upper + renderable_param_midlower, title='PRODUTO')
        print(painel)
        
p1 = Produto('Moto G8 Plus', 849.99)
p2 = Produto('Lamborghini Veneno', 15500000)
p3 = Produto('iPhone 17 Pro MAX', 8499.99)
p1.etiqueta()
p2.etiqueta()
p3.etiqueta()