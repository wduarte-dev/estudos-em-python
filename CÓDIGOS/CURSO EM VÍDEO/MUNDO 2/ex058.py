from random import randint
computer_n = randint(1, 9)
user_n = int(input('Tente adivinhar o número inteiro de 1 a 9: '))
counter = 0
while user_n != computer_n:
    counter += 1
    user_n = int(input('Errou! Tente novamente: '))
print(f'Você acertou! Foram necessárias {counter} tentativas.')
