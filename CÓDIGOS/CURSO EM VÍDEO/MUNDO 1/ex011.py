altura = float(input('Altura da parede em metros: '))
largura = float(input('Largura da parede em metros: '))
area = altura*largura
litros_tinta = area/2
print(f'A area da parede é de {area}m² e são necessários {litros_tinta:.2f}litros de tinta para pintá-la totalmente.')
