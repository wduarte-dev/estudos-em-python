def voto():
    ano = int(input('Digite o ano de nascimento: '))
    from rich import print
    from rich.panel import Panel
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 18 and idade <= 69:
        painel = Panel(f'Com [bold]{idade}[/] anos o voto é [red]OBRIGATÓRIO.[/]', width=40)
        print(painel)
    elif idade <= 15:
        painel = Panel(f'Com [bold]{idade}[/] anos o voto é [red]PROIBIDO POR LEI.[/]', width=45)
        print(painel)
    else:
        painel = Panel(f'Com [bold]{idade}[/] anos o voto é [green]FACULTATIVO.[/]', width=40)
        print(painel)

voto()