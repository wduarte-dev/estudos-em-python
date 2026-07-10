from time import sleep
from rich import print
def check():
    try:
        open('pessoas_cadastradas.txt', 'r')
    except FileNotFoundError:
        print('[red]ERRO! O arquivo "pessoas_cadastradas.txt" foi removido.[/]')
        sleep(1)
        print('[red]Criando novamente...[/]')
        sleep(1)
        open('pessoas_cadastradas.txt', 'w').close()