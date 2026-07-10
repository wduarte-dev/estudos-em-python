from utilidadesCeV.moeda import *
from utilidadesCeV.dado import *
valor = float(leiaDinheiro('Digite o preço: R$'))
aumento = float(leiaDinheiro('Digite o aumento (0-100): '))
reducao = float(leiaDinheiro('Digite a redução (0-100): '))
tabela(valor, aumento, reducao)