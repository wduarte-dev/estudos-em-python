counter = 0
sum = 0
number_list = []
while True:
    n = int(input('Type an integer number: '))
    sum += n
    number_list.append(n)
    counter += 1
    cmd = input('Continue? [Y/N]: ').upper()
    if cmd == 'N':
        break
mean = sum/counter
print(f'''Mean: {round(mean, 2)}
Highest number: {max(number_list)}
Lowest number: {min(number_list)}
''')