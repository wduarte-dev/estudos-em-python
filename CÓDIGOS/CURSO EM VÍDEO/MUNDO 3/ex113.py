def leiaInt():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
            return num
        except ValueError:
            print('\033[31mERRO! Digite um número válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\nEncerrando...\n')
            return 0


def leiaFloat():
    while True:
        try:
            num = float(input('Digite um número real: '))
            return num
        except ValueError:
            print('\033[31mERRO! Digite um número válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\nEncerrando...\n')
            return 0


inteiro = leiaInt()
real = leiaFloat()
print(f'O valor inteiro foi {inteiro} e o valor real foi {real}')
    