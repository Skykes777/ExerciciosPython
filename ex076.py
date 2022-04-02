listaC = ('Lapís', 1.50,
          'Estojo', 3.79,
          'Mochila', 115.99,
          'kit Lapis', 25.50,
          'Caderno', 20.80)
for x in range(0, len(listaC)):
    if x % 2 == 0:
        print(f'{listaC[x]:.<15}', end='')
    else:
        print(f'R${listaC[x]:>8.2f}')
