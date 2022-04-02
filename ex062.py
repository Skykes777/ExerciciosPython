a1 = int(input('Promeiro termo: '))
razão = int(input('Razão da PA: '))
termo = a1
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} > ', end='')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progresção finalizada com {total} termos mostrados.')
