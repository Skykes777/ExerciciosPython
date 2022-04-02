km = float(input('Quilometros rodados: '))
alugado = int(input('Quantos dias alugados: '))
total = (km * 0.15) + (alugado * 60)
print('Valor total a pagar é de R${:.2f}'.format(total))