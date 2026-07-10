dist = float(input('Digite a distância da viagem em kilômetros: '))
if dist <= 200:
    preco = dist*0.50
    print(f'O preço da viagem será de R${preco:.2f}.')
else:
    preco = (dist-200)*0.45 + 100
    print(f'O preço da viagem será de R${preco:.2f}.')