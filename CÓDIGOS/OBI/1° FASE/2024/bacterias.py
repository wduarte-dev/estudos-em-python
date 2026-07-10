N = int(input())
P = int(input())
bacterias = 1
counter = 0
while bacterias <= N:
    bacterias *= P
    counter += 1
print(counter - 1)