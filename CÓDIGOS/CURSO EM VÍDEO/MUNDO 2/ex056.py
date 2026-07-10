soma = 0
homens = []
idades_homens = []
mulheres_com_menos_de_vinte = []
for p in range(1, 5):
    print(f'-=-= {p}° PESSOA =-=-')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    genero = input('Gênero [M/F]: ').upper()
    soma += idade
    if genero == 'M':
        homens.append(nome)
        idades_homens.append(idade)
    elif genero == 'F' and idade < 20:
        mulheres_com_menos_de_vinte.append(nome)
        


media = soma/4
qntd_mulheres_com_menos_de_vinte = len(mulheres_com_menos_de_vinte)
try:
    homem = True
    posicao = idades_homens.index(max(idades_homens))
    nome_homem_mais_velho = homens[posicao]
except:
    homem = False

print(f'A média de todas as idades é {media}')
if homem == True:
    print(f'O nome do homem mais velho é {nome_homem_mais_velho}.')
print(f'Há {qntd_mulheres_com_menos_de_vinte} mulheres com menos de 20 anos.')