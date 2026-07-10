from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'''
Lista dos números gerados: {numeros}
Menor valor: {min(numeros)}
Maior valor: {max(numeros)}''')
