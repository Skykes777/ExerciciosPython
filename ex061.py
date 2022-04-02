a1 = int(input('Primeiro número: '))
razão = int(input('Razão da PA: '))
termo = a1
contador = 1
while contador <= 10:
    print(f'{termo} > ', end='')
    termo += razão
    contador += 1
print('FIM!')