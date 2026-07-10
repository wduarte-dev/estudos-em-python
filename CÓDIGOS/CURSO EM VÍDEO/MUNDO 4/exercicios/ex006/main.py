from rich import print, inspect
from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

def main():
    # BLOCO DE TESTES 1
    a1 = Aluno('João', 19, 'Ciência da Computação', '1° ano')
    p1 = Professor('Raimundo', 48, 'Tecnologia da Informação', 'Mestrado')
    f1 = Funcionario('Ivânia', 39, 'Diretora', 'Educação')
    inspect(a1, methods=True)
    a1.fazer_aniversario()
    print(a1.idade)
    inspect(p1, methods=True)
    inspect(f1, methods=True)

    # BLOCO DE TESTES 2
    a2 = Aluno('Jorge', 17)
    a2.fazer_matricula('Estrutura e Análise de Dados')
    a2.fazer_aniversario()
    inspect(a2)

    p2 = Professor('Carlos', 32, 'Teologia', 'Doutorado')
    print(p2.dar_aula('Religiões de Matriz Africana'))

    f2 = Funcionario('Cláudio', 28, 'Inspetor', 'Educação')
    print(f2.bater_ponto('6:50'))

if __name__ == '__main__':
    main()