n = int(input('Digite um número inteiro: '))
print(f'O número escolhido foi {n}.')
print('-='*10)
print('     CONVERSÃO')
print('-='*10)
cmd = input('1 -> Converter em binário\n2 -> Converter em octal\n3 -> Converter em hexadecimal ')
if cmd == '1':
    bin_n = bin(n)
    print(f'O número em binário é {bin_n}.')
elif cmd == '2':
    oct_n = oct(n)
    print(f'O número em octal é {oct_n}')
elif cmd == '3':
    hex_n = hex(n)
    print(f'O número em hexadecimal é {hex_n}')
else:
    print('Entrada inválida! Reinicie o programa e tente novamente')
    