from random import randint
from time import sleep


def sorteia(lista):
    print('Soeteando 5 valores da lista: ', end='')
    for x in range(1, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')
# -DEF DE SORTEAR VALORES ALEATÓRIOS


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares temos de {lista}, temos {soma}')
# -DEF DE SOMAR VALORES PARES QUE FORAM SORTEADOS


# -PROGRAMA PRINCIPAL
numeros = []
sorteia(numeros)
somaPar(numeros)
