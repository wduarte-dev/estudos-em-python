class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
meu_carro = Carro('Ford', 'Ka', '1999')
meu_carro.ligar()
if meu_carro.ligado:
    print(f'Meu carro está ligado! Ele é um {meu_carro.marca} {meu_carro.modelo} do ano de {meu_carro.ano}')
else:
    print(f'Meu carro está desligado...Me ajude a ligá-lo!')

meu_carro.desligar()
if meu_carro.ligado:
    print('Eu desliguei meu carro e ele está ligado, como assim?')
else:
    print('Consegui desligar meu carro!')