frase = 'Curso em Vídeo Python' # a variável frase tem uma coleção de (n) strings, cada uma com um caracter e com posição 0 a (n-1)
# FATIAMENTO
print(frase[0]) # pega o primeiro elemento, que seria o 'C'
print(frase[9:13]) # exibe do elemento 9 até o elemento 12 (13-1) ou o intervalo semiaberto [9,13[
print(frase[9:21]) # embora não exista o elemento 21, ele subtrai e printa até o último elemento (20)
print(frase[9:13:2]) # exibe do elemento 9 até o elemento 12 (13-1) 'pulando' de 2 em 2 caracteres
print(frase[0:5]) # também pode ser print(frase[:5]), vai do elemento 0 até o especificado (nesse caso, 5)
print(frase[15:]) # exibe do 15° elemento até o último elemento de uma lista
print(frase[9::3]) # exibe do 9 até o último elemento (como na situação anterior), mas 'pulando' de 3 em 3 caracteres

# ANÁLISE
print(len(frase)) # comprimento ou quantidade de elementos em uma lista
print(frase.count('o')) # mostra quantas vezes o elemento indicado aparece, literalmente count = contar
print(frase.count('o', 0, 13)) # mostra quantas vezes o elemento indicado aparece, num intervalo do 0° a 12° caractere (13-1)
print(frase.find('deo')) # mostra a posição onde o elemento especificado aparece
print(frase.find('Wellington')) # como o elemento especificado não existe, retorna o valor -1
print('Curso' in frase) # Basicamente, significa "existe o elemento 'Curso' na variavel frase?" e retorna True ou False (booleano)

# TRANSFORMAÇÃO
print(frase.replace('Python', 'Android')) # substitui o elemento 'Python' pelo elemento 'Android' na lista toda
print(frase.upper()) # coloca em maiúsculo todos os elementos da variavel (frase.lower() é o oposto)
print(frase[0:5].upper()) # coloca em maiúsculo apenas do elemento 0 ao 4 (5-1)
print(frase.capitalize()) # a primeira letra torna minúscula e todo o resto minúsculo
print(frase.title()) # analisa a quantidade de palavras pela posição dos espaços e capitaliza CADA palavra e o resto fica tudo minúsculo

frase2 = '      wellington 123    ' # exemplo de frase com espaços excedentes, para explicarmos a próxima função
print(frase2.strip()) # remove todos os espaços antes e depois do elemento principal (rstrip -> remove à direita; lstrip -> remove à esquerda)

# DIVISÃO
frase.split() # separa a lista em elementos de acordo com o argumento fornecido, por exemplo:
print(frase.split()) # saída: ['Curso', 'em', 'Vídeo', 'Python']

# JUNÇÃO
print('-'.join(frase.split())) # junta todos os elementos separados na lista pela string fornecida (nesse caso, ' - ')
# objetivo do comando acima: separar os elementos por espaço e juntar/substituir pelo hífen.