from time import sleep
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

print(f'''   [1] somar
   [2] multiplicar
   [3] maior
   [4] novos números
   [5] sair do programa''')

escolha = int(input('>>>>> Qual é a sua opção? ')) #....ESCOLHA DO USUARIO

while escolha != 5:
    if escolha == 1: #....ESCOLHA 1
        soma = n1 + n2
        print(f'\033[34mA soma de {n1} + {n2} é {soma}')
        sleep(1)
    elif escolha == 2: #....ESCOLHA 2
        multi = n1 * n2
        print(f'\033[34mA multiplicação do número {n1} X {n2} é {multi}')
        sleep(1)
    elif escolha == 3: #....ESCOLHA 3
        if n1 == n2:
            print('\033[34mOs dois valores são iguaus')
            sleep(1)
        else:
            números = [n1, n2]
            maior = max(números)
            print(f'\033[34mEntre {n1} e {n2}, o maior número é {maior}')
            sleep(1)
    elif escolha == 4: #....ESCOLHA 4
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        sleep(1)
    else:
        print('Valor invalido, tente de novo!')
    print('\033[31m=-='*10)
    print(f'''\033[m   [1] somar
   [2] multiplicar
   [3] maior
   [4] novos números
   [5] sair do programa''')
    escolha = int(input('>>>>> Qual é a sua opção? '))  # ....ESCOLHA DO USUARIO

print('Finalizando o programa....')
sleep(1)
print('Programa finalizado!')
