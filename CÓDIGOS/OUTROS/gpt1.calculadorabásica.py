#calculadora básica
num1 = input('Olá, bem-vindo à calculadora básica de dois números INTEIROS.\nEla realizará várias operações, que são: soma, subtração (do 1° pelo 2° e vice-versa) e multiplicação.\n Para começar, digite o primeiro número = ')
num2 = input('Agora, digite o segundo número = ')
num1 = int(num1)
num2 = int(num2)
soma = num1+num2
dif = num1-num2 #poderia ter deixado a variável com nome melhor, evitando confusões, exemplo: dif_1_2
dif1 = num2-num1 #poderia ter deixado a variável com nome melhor, evitando confusões, exemplo: dif_2_1
mul = num1*num2


print('Perfeito!\nA soma dos dois números é',soma,'\nA subtração do 1° pelo 2° é',dif,'\nA subtração do 2° pelo 1° é',dif1,'\nE a multiplicação é',mul)
