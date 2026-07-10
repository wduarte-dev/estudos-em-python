'REFATORAMENTO DO DESAFIO 17 PRA FIXAÇÃO'
from rich.panel import Panel
from rich import print
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        renderable_param_upper = ' '*5 + self.nome + ' '*5
        width_format = len(renderable_param_upper)
        renderable_param_mid = '-'*width_format
        eua_format = f'{self.preco:,.2f}'
        brazil_format = 'R$' + str(eua_format).replace('.', 'x').replace(',', '.').replace('x', ',')
        renderable_param_lower = f'[green]{brazil_format:.^{width_format}}[/]'
        painel = Panel.fit(renderable='[bold]' + renderable_param_upper + '[/]' +'\n' + '[green]' + renderable_param_mid + '[/]' + '\n'+renderable_param_lower, 
        title='Produto', 
        border_style='yellow')
        print(painel)
        

p1 = Produto('Redmi 13C', 899.99)
p2 = Produto('Ferrari F50 (Leilão)', 45000000)
p3 = Produto('iPhone Pro Max', 25000.85)
p4 = Produto('Mouse', 120)
p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
p4.etiqueta()