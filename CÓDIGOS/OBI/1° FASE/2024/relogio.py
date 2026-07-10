H = int(input())
M = int(input())
S = int(input())
T = int(input())
S += T
while S >= 60:
    M += 1
    S -= 60
while M >= 60:
    H += 1
    M -= 60
while H >= 24:
    H -= 24
print(H)
print(M)
print(S)
