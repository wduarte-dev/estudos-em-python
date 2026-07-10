N = int(input())
lances = []
nomes = []
for _ in range(N):
    nome = input()
    lance = int(input())
    nomes.append(nome)
    lances.append(lance)
maior_lance = max(lances)
print(nomes[lances.index(maior_lance)])
print(maior_lance)