# essa função lê um input com float/int e verifica se o usuário digitou alguma letra
def get_float(msg):
    while True:
        try:
            float(msg)
            return float(msg)
        except ValueError:
            print('\033[31mEntry error!\033[0m')
            msg = input('Try again: ')

# essa função lista elementos separados por espaço em um input em str
def list_that(msg):
    cmd = input(msg).replace(',','.').strip().split()
    return cmd
