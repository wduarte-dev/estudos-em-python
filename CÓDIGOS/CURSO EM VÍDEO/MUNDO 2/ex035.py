#pede três lados e verifica se um triângulo pode ser formado
# Requisitos: Os lados não podem ser negativos; não podem ser nulos; não podem ser letras, símbolos ou outros caracteres
# se o usuário digitar mais ou menos que 3 lados, o programa invalida a entrada
# vírgulas são substituídas por pontos automaticamente, evitando erros
# há opção de reiniciar o programa ao final da operação
while True:
    try:
        print('-='*15)
        print('ANALISADOR DE TRIÂNGULOS')
        print('=-'*15)
        lados_str = input('Digite os três lados do triângulo, separando-os por espaço: ').replace(',','.').strip().split()
        if len(lados_str) != 3:
            input('Entrada fora do limite de lados, que é três. Pressione ENTER e tente novamente.\n')
            continue
        elif float(lados_str[0]) <= 0 or float(lados_str[1]) <= 0 or float(lados_str[2]) <= 0:
            input('Não existe lado negativo ou nulo.  Pressione ENTER e tente novamente.\n')
            continue
    except ValueError:
        input('A entrada é inválida, pressione ENTER e tente novamente seguindo os requisitos.\n')
        continue
    lados_float = list(map(float, lados_str))
    maior_lado = max(lados_float)
    menor_lado = min(lados_float)
    lados_float.remove(maior_lado)
    lados_float.remove(menor_lado)
    mediana = lados_float[0]

    if (mediana + menor_lado) > maior_lado:
        print('Com os três lados, forma-se um triângulo.')
        cmd = input('\nDeseja reiniciar? -> ( r )\nSAIR do programa -> Qualquer outra tecla\n')
        if cmd == 'r':
            continue
        else:
            break
        
    else:
        print('Com os três lados, NÃO é possível formar um triângulo')
        cmd = input('\nDeseja reiniciar? -> ( r )\nSAIR do programa -> Qualquer outra tecla\n')
        if cmd == 'r':
            continue
        else:
            break