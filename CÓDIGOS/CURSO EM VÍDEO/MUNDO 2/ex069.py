total_price = higher_than_1000 = 0
price_list = []
name_list = []
while True:
    name = input('Digite o nome do produto\n> ')
    price = input('Digite o preço do produto\n> ').replace(',', '.')
    price = float(price)
    price_list.append(price)
    name_list.append(name)
    if price > 1000:
        higher_than_1000 += 1
    total_price += price 
    while True:
        cmd = input('Deseja continuar? (s)/(n)\n> ')
        if cmd == 'n':
            break
        elif cmd != 's':
            continue
        else:
            break
    if cmd == 'n':
        break
name_list[price_list.index(min(price_list))]
print(f'''
Total: R${total_price:.2f}
Quantidades de produtos acima de R$1000,00: {higher_than_1000}
Produto de menor valor -> {name_list[price_list.index(min(price_list))]}: R${min(price_list):.2f}
''')