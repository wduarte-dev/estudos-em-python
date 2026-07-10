n = int(input())
alturas = input().split()
alturas = list(map(int, alturas))
maior_altura = counter = 0
for n in range(n - 1, -1, -1):
    if alturas[n] > maior_altura:
        maior_altura = alturas[n]
    else:
        counter += 1
print(counter)