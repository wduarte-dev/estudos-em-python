n = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
cmd = int(input('Digite um número inteiro de 0 a 20\n > '))
while cmd > 20 or cmd < 0:
    cmd = int(input('Entrada inválida!\nDigite um número inteiro de 0 a 20\n > '))
print(f'Você digitou o número {n[cmd]}')

