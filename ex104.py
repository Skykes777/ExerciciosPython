def leiaInt(recebe):
    while True:
        n = input(recebe)
        if n.isnumeric() is False:
            print('\033[31m[ERRO]! Digite um número inteiro valido.\033[m')
        else:
            return n


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
