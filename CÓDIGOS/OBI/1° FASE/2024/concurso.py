NK = list(map(int, input().split()))
N = NK[0]
K = NK[1]
NOTAS = list(map(int, input().split()))
print(sorted(NOTAS, reverse = True)[K-1])
