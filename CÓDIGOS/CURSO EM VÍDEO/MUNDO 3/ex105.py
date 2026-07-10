def notas(*notas_fornecidas, mostrar_situacao=False):
    '''
    -> Função para análise detalhada das notas dos alunos.
    :param notas_fornecidas: Uma ou mais notas dos alunos, base para as informações.
    :param mostrar_situacao: Mostra se a situação do aluno é BOA, RAZOÁVEL ou RUIM.
    :return: Retorna o dicionário ao usuário.
    '''
    if not notas_fornecidas:
        return {}
    total_de_notas = len(notas_fornecidas)
    maior_nota = max(notas_fornecidas)
    menor_nota = min(notas_fornecidas)
    media = round(sum(notas_fornecidas) / total_de_notas, 2)
    informacoes = {
        'Total': total_de_notas,
        'Maior': maior_nota,
        'Menor': menor_nota,
        'Média': media,
    }
    if mostrar_situacao:
        if media >= 7:
            situacao = 'BOA' 
        elif media >= 6:
            situacao = 'RAZOÁVEL' 
        else:
            situacao = 'RUIM'

        informacoes['Situação'] = situacao
    return informacoes
