soma = 0
for n in range (1, 501):
    if n % 3 == 0 and n % 2 != 0:
        soma += n
print(soma)