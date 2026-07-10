genero = input('Digite seu gênero [M/F]: ').upper()
while genero != 'M' and genero != 'F':
    genero = input('Gênero inválido, tente novamente [M/F]: ').upper()
print('Masculino' if genero == 'M' else 'Feminino')