# adicionar minha função de verificação de caracteres errados nos inputs desse programa; impedir valores negativos
from myfunctions import get_float as validar
preco = validar(input('Digite o valor em reais do produto a ser pago: ').replace(',','.'))
preco = int(preco)
print('1 -> Pagamento à vista em dinheiro\n2 -> Pagamento à vista no cartão\n3 -> Pagamento em até 2x no cartão sem juros')
cmd = input('4 -> Pagamento em 3x ou mais no cartão com juros ')
if cmd == '1':
    print(f'O cliente deverá pagar R${preco:.2f}.')
elif cmd == '2':
    preco = preco * 0.95
    print(f'O cliente deverá pagar R${preco:.2f}.')
elif cmd == '3':
    parcela = preco/2
    print(f'O cliente pagará em duas parcelas de R${parcela:.2f} sem juros.')
elif cmd == '4':
    while True:
        n = int(input('Digite o número de parcelas (mín 3): '))
        if n < 3:
            print('Número de parcelas menor que 3, tente novamente.\n')
            continue
        parcelas = preco*1.20/n
        print(f'O cliente pagará em {n} parcelas de R${parcelas:.2f} com 20% de juros.')
        break

else:
    input('Comando inválido, pressione ENTER e reinicie o programa.')
