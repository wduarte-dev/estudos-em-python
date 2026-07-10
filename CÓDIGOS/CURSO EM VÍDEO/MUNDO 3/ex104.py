def leiaInt(msg) -> int:
    while True:
        try:
            n = float(input(msg))
            return n
        except ValueError:
            print('\033[31mERRO! Digite um número válido.\033[0m')
            continue


num = leiaInt('Digite um número: ')
print(num)
