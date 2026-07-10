velocidade = int(input('Velocidade do carro: '))
if velocidade <= 0:
    print('Informe um valor válido. Reinicie o programa e tente novamente.')
elif velocidade <= 80 and velocidade > 0:
    print('Velocidade dentro do limite.')
else:
    multa = (velocidade-80)*7
    print(f'Multa de R${multa:.2f} por ultrapassar o limite de 80km/h.')