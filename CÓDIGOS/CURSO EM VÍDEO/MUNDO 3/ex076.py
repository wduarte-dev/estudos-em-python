palavras = ('python', 'programacao', 'codigo', 'curso', 'gratis', 'aprender', 'linguagem', 'guanabara')
vogais = 'aeiou'
for palavra in palavras:
    vogais_das_palavras = ' '.join([letra for letra in palavra if letra in vogais])
    print(f'Vogais da palavra {palavra.upper()} -> {vogais_das_palavras}')
    