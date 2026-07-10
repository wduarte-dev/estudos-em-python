from rich.panel import Panel as Painel
from rich.prompt import Prompt as Comando
from rich.align import Align
from rich import print
from verificador import check
def verificacao_de_duplicatas(nome, idade):
    with open('pessoas_cadastradas.txt', 'r') as arquivo:
        txt_lista = list(arquivo)
        for indice, item in enumerate(txt_lista):
            try:
                if (indice + 1) % 2 != 0:
                    nome_check = item.replace('\n', '')
                    idade_check = int(txt_lista[indice + 1].replace('\n', ''))
                    if nome_check == nome and idade_check == idade:
                        print('[red]A MESMA PESSOA E IDADE JÁ ESTÃO CADASTRADAS![/]')
                        return True
            except IndexError:
                break
        
        
def cadastrar_pessoa():
    with open('pessoas_cadastradas.txt', 'a') as arquivo:
        cadastro_txt = Align.center('CADASTRO')
        cadastro_painel_1 = Painel(cadastro_txt)
        print(cadastro_painel_1)
        try:
            nome = Comando.ask('Digite o nome')
            while True:
                idade = Comando.ask('Digite a idade')
                try:
                    idade = int(idade) 
                except ValueError:
                    print('[red]ERRO! Idade em formato inválido.\nTente novamente...')
                    continue
                check = verificacao_de_duplicatas(nome, idade)
                if check:
                    cmd = input('\033[31mDeseja prosseguir? (S) / (N)\n> \033[0m').upper()
                    if cmd == 'N':
                        return 0
                arquivo.write(nome + '\n')
                arquivo.write(f'{idade}\n')
                break
            cadastro_txt2 = Align.center('PESSOA CADASTRADA COM SUCESSO!')
            cadastro_painel_2 = Painel(cadastro_txt2)
            print(cadastro_painel_2)
        except KeyboardInterrupt:
            print('\n[red]Abortando operação...[/]')


if __name__ == '__main__':
    cadastrar_pessoa()