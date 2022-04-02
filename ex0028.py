from random import randint
valor = int(input('Escolha um número entre 1 e 5: ')) #Valor que o usuario escolhe
aleatorio = randint(0,5) #Valor aleatório que o computador irá escolher
if valor == aleatorio:
    print('Parabens você acertou o número!')
else:
    print(f'Você errou! O número escolhido foi {aleatorio}')
