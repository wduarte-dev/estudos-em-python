from math import sqrt, ceil
elements = int(input('Type an integer number: '))
n = 0
counter = 1
while elements > n:
    binet_formula = round((((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n) / sqrt(5))
    print(f'{counter}° term: {binet_formula}')
    n += 1
    counter += 1



