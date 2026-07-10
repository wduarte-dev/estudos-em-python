from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect

from rich.traceback import install # instala o modulo que monitora os erros do python
install() # a exibição dos erros do python agora ficam muito mais bonitos!

print('[purple]Olá mundo com Rich e coloração roxa![/] :sunglasses: <- [italic]Óculos escuros[/]')
print('[bold blue]Negrito com letra azul![/]')
print('[bold red on blue]Negrito, com letra vermelha e fundo azul![/]')
# python -m rich.emoji -> exibe todos os emojis disponíveis na bibloteca rich
# Saída: 

text_box = Panel('[red]Isso aqui é um painel de exemplo, com letra vermelha![/] :+1:')
print(text_box)
text_box_2 = Panel('[blue]Já aqui nós temos um painel com título![/]', title='[red]TÍTULO[/]')
print(text_box_2)
text_box_3 = Panel('[yellow]Já aqui nós temos um painel com título e a borda colorida![/]', title='[red]TÍTULO[/]', style='violet')
print(text_box_3)
text_box_4 = Panel('[green]Também posso controlar a largura disso...[/]', width=50)
print(text_box_4)
# Saída: 

tabela = Table(title='\nTABELA DE PREÇOS', style='blue')
tabela.add_column('Produtos', justify='left', style='dark_green', header_style='dark_blue')
tabela.add_column('Preço', justify='center', style='green', header_style='dark_blue')
tabela.add_row('Lápis', 'R$0.50')
tabela.add_row('Caneta esferográfica', 'R$1.50')
tabela.add_row('Borracha', 'R$1.00')
tabela.add_row('Caderno 10 matérias', 'R$15.00')
tabela.add_row('Mochila', 'R$110.00')
print(tabela)
# Saída: 

inspect(int, all=True) # analisa toda a classe de uma forma extremamente organizada

def divisao(a, b):
    return a / b
print(divisao(50, 0))