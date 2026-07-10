import numpy
a1 = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))
a10 = a1 + 9*razao
if razao < 0:
    for c in numpy.arange(a1, a10-1, razao):
        print(round(c, 2))
if razao > 0:
    for c in numpy.arange(a1, a10+1, razao):
        print(round(c, 2))
if razao == 0:
        for c in numpy.arange(1,11):
            print(a1)
