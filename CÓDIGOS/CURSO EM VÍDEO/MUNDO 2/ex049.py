n = int(input('Digite um número inteiro (tabuada): '))
i = int(input('Digite o começo da tabuada: '))
f = int(input('Digite o final da tabuada: '))
for c in range(i, f+1):
    print(f'{n} x {c} = {n*c}')
