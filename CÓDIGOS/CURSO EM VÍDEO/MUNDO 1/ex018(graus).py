from math import pi, sin, cos, tan
while True:
    def converter_rad(x):
        x = (x*pi)/180
        return x
    
    angulo_graus = float(input('\nDigite um ângulo em graus: '))
    angulo_rad = converter_rad(angulo_graus)
    seno = sin(angulo_rad)
    cosseno = cos(angulo_rad)
    tangente = tan(angulo_rad)
    print(f'Ângulo: {angulo_graus}°\nSeno = {seno:.2f}\nCosseno = {cosseno:.2f}')
    if abs(cosseno) < 1e-10:
        print(f'Tangente = indefinida')
    else:
        print(f'Tangente = {tangente:.2f}')

    cmd = input('\nDeseja reiniciar a operação? ( r )\nQualquer outra tecla -> Sair. ')
    if cmd == 'r':
        continue
    else:
        break

