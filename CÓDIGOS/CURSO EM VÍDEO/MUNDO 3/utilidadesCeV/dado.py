def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.')
        try:
            saida = entrada
            saida = float(entrada)
            return saida
        except ValueError:
            print(f'\033[31mERRO! "{saida}" é um valor inválido.\033[0m')
            continue


if __name__ == '__main__':
    print(leiaDinheiro('Digite um preço: '))


