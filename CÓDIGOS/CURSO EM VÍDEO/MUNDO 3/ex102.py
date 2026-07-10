def fatorial(n, show=False):
    '''
    -> Essa função serve para calcular o fatorial de qualquer número pertencente aos naturais.
    :param n: Fatorial do número a ser calculado.
    :param show: Opcional, mostra a sequência de multiplicação utilizada.
    :return: Retorna os valores calculados.
    '''
    num = 1
    if n == 0:
        return 1
    if n < 0:
        return '\033[31mErro! Valor precisa ser positivo.\033[0m'
    for fat in range(2, n + 1):
        num *= fat
    if show:
        fat_show = ' x '.join(f'{c}' for c in range(1, n + 1)) + str(f' = {num}')
        return fat_show
    else:
        return num

help(fatorial)