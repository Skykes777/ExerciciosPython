from random import randint
computador = randint(1, 5)
jogador = soma = contador = 0

print('=-='*15)
print('           VAMOS JOGAR PAR OU IMPAR!')
print('=-='*15)

while True:
    jogador = int(input('Digite um número de 1 a 5: '))
    par_impar = input('Par[\033[31mP\033[m] ou impar[\033[31mI\033[m]? ').strip().upper()[0]
    while par_impar not in 'PI':
        par_impar = input('Par[\033[31mP\033[m] ou impar[\033[31mI\033[m]? ').strip().upper()[0]
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}, o total de {soma} É PAR!')
    else:
        print(f'Você jogou {jogador} e o computador {computador}, o total de {soma} É IMPAR!')
    if par_impar == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            contador += 1
            print('Vamos jogar de novo..')
            print('=-=' * 15)
        else:
            print('VOCÊ PERDEU!')
            print('=-=' * 15)
            break
    elif par_impar == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            contador += 1
            print('Vamos jogar de novo...')
            print('=-=' * 15)
        else:
            print('VOCÊ PERDEU!')
            print('=-=' * 15)
            break

if contador > 5:
    print(f'GAME OVER! VOCÊ VENCEU {contador} vezes, parabens, você é MUITO BOM!')
elif contador > 2:
    print(f'GAME OVER! você venceu {contador} vezes.')
else:
    print(f'GAME OVER! Você venceu {contador}, você é muito ruim! precissa melhorar! ')
