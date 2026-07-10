txt = input('Digite aqui um palíndromo: ').strip().lower().replace(' ','')
txt_inv = txt[::-1]
print(txt, txt_inv)
if txt == txt_inv:
    print('Isso é um palíndromo!')
else:
    print('Isso não é um palíndromo!')
