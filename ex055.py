maior = 0
menor = 0
for ps in range(1, 6):
    peso = float(input(f'Peso da {ps} pessoa: '))
    if ps == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'''O maior peso lido foi de {maior}Kg
O menor peso lido ofoi de {menor}Kg''')
