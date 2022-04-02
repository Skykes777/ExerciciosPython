print('=-='*8)
print('NOTA FISCAL DA PASSAGEM')
print('=-='*8)
distancia = float(input('Distancia da viagem: '))
mais200 = distancia * 0.50
menos200 = distancia * 0.45
if distancia > 200:
    print(f'Preço da passagem a pagar é de R${mais200 :.2f}')
else:
    print(f'Prço da passagem a pagar é de R${menos200 :.2f}')
