n = 0
sum = 0
counter = 0
while n != 999:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n != 999:
        sum += n
        counter += 1
print(f'Quantidade de números: {counter}\nSoma dos números: {sum}')