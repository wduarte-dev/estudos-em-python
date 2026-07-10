from sys import exit
first_term = float(input('Type the first term of the PA: '))
c_difference = float(input('Type the common difference of it: '))
n = 0
while n < 11:
    if n == 0:
        print(f'1° term: {first_term}.')
        n += 2
    else:
        first_term += c_difference
        print(f'{n}° term: {first_term}.')
        n += 1

while True:
    cmd = int(input('''
Do you want more terms?
[0] No. (exit program)
[Any value] Show the next x terms.
> '''))
    if cmd == 0:
        exit()
    else:
        cmd += n
        while n < cmd:
            first_term += c_difference
            print(f'{n}° term: {first_term}.')
            n += 1
        