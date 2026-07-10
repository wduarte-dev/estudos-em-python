'HELP E DOCSTRINGS'
def exemplo_de_help():
    help(print)
    # Ou, pra documentação toda:
    print(input.__doc__)

# docstrings = Documentação dos metodos criados em uma biblioteca.
def soma(a, b):
    """
    -> Aqui fica a mensagem da função, exemplo: Soma dois números.
    :param a: Informa sobre o parâmetro indicado, exemplo: Primeiro elemento da soma.
    :param b: Informa sobre o parâmetro indicado, exemplo: Segundo elemento da soma.
    :return: Fala o que a função retorna, exemplo: Retorna a soma entre os dois parâmetros, a e b.
    Criado por mim xD
    """
    return a + b

def exemplo_de_help_com_metodo_próprio():
    help(soma)

# Criação de parâmetros opcionais:
def somar(a=0, b=0, c=0):
    return a + b + c
# Perceba que, como a, b e c já recebem zero por padrão, se a função não receber eles, ela não
# causará erros.
r1 = somar(6, 3)
r2 = somar(1)
r3 = somar(1, 2, 3)
print(r1, r2, r3) # Saída: 9 1 6


'ESCOPO DE VARIÁVEIS (global fora de função e local dentro de função)'
valor = 'Valor qualquer'
variavel_global = valor # essa variável funciona dentro e fora de funções
# toda variável criada aqui é do ESCOPO GLOBAL

def funcao():
    variavel_local = valor # essa variável não funciona fora da função
    # toda variável criada aqui é do ESCOPO LOCAL
    # a não ser que você utilize "global" , como no próximo exemplo

def funcao_com_var_global():
    global a
    a = 5

funcao_com_var_global()
print(a) # Saída: 5


'RETORNANDO VALORES EM FUNÇÕES'
def funcao_com_retorno(valor):
    return valor
resultado = funcao_com_retorno('Valor retornado com sucesso!')
print(resultado) # Saída: 'Valor retornado com sucesso!'





