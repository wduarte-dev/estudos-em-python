pesos = []
for c in range(1, 6):
    peso = float(input(f'Digite o {c}° peso: '))
    pesos.append(peso)
maior = max(pesos)
menor = min(pesos)
print(f'O menor peso é {menor}kg e o maior é {maior}kg.')
    