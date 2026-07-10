from rich.table import Table as Tabela
from rich.console import Console
from rich import print
from verificador import check
def exibir_tabela():
    tabela = Tabela(title='DADOS', show_lines=True)
    tabela.add_column('Nome', justify='center')
    tabela.add_column('Idade', justify='center')
    with open('pessoas_cadastradas.txt', 'r') as arquivo:
        for n, linha in enumerate(arquivo):
            if not linha:
                break
            if (n + 1) % 2 != 0:
                nome = linha.strip()
            else:
                idade = linha.strip()
                tabela.add_row(nome, idade)
    print(tabela)