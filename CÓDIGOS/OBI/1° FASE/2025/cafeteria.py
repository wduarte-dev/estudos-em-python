A = int(input())
B = int(input())
C = int(input())
D = int(input())
casos = []
for ab in range(A, B+1):
    r1 = C-ab 
    r2 = r1%D
    casos.append(r2)
if 0 in casos:
    print('S')
else:
    print('N')