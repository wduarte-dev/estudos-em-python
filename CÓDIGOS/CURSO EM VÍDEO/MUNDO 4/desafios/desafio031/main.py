from desafio031 import Retangulo
def main():
    r1 = Retangulo(3, 4)
    r1.base = 8
    r1.altura = 9
    r1.medidas = (10, 12)
    r1.medidas = (-9, -19)
    print(r1.medidas)


if __name__ == '__main__':
    main()