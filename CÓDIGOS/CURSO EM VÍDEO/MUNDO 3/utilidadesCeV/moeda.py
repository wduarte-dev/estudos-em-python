def reais(valor):
    valor_formatado = f'R${valor:.2f}'
    valor_formatado = valor_formatado.replace('.', ',')
    return valor_formatado


def aumentar(valor, porcentagem, formatar=False):
    if formatar:
        return reais(valor * (1 + porcentagem / 100))
    return valor * (1 + porcentagem / 100)


def diminuir(valor, porcentagem, formatar=False):
    if formatar:
        return reais(valor * (1 - porcentagem / 100))
    return valor * (1 - porcentagem / 100)


def dobro(valor, formatar=False):
    if formatar:
        return reais(valor * 2)
    return valor * 2


def metade(valor, formatar=False):
    if formatar:
        return reais(valor / 2)
    return valor / 2    


def tabela(valor, aumento, reducao):
    from rich.table import Table
    from rich.console import Console
    tabela = Table(title='DADOS')
    tabela.add_column('Descrição', justify='center')
    tabela.add_column('Valor', justify='center')
    tabela.add_row('Preço analisado:', reais(valor))
    tabela.add_row('Dobro do preço:', dobro(valor, True))
    tabela.add_row('Metade do preço:', metade(valor, True))
    tabela.add_row(f'{aumento}% de aumento:', aumentar(valor, aumento, True))
    tabela.add_row(f'{reducao}% de redução:', diminuir(valor, reducao, True))
    Console().print(tabela)


if __name__ == '__main__':
    valor = float(leiaDinheiro('Digite o preço: R$'))
    aumento = float(leiaDinheiro('Digite o aumento (0-100): '))
    reducao = float(leiaDinheiro('Digite a redução (0-100): '))
    tabela(valor, aumento, reducao)

