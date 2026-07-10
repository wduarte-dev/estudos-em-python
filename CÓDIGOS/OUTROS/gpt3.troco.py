val = input('Valor do produto = ')
pag = input('Valor pago pelo cliente = ')
val = float(val)
pag = float(pag)
trc = pag-val
if trc>0:
    print('O troco a ser recebido é de',trc,'reais')
else:
    if trc<0:
        devendo = trc*-1
        print('Ops! O cliente ainda deve pagar',devendo,'reais')
    else:
        print('Pagamento exato, sem troco')
