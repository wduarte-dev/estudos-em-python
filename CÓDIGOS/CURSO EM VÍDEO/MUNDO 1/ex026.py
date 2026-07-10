frase = input('Digite uma frase: ').strip()
print(f'''Essa frase tem {frase.upper().count('A')} letras A sem acento gráfico.''')
print(f'''O primeiro A está na posição {frase.upper().find('A')}.''')
print(f'''O último A está na posição {frase.upper().rfind('A')}.''')
