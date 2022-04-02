from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual você escolhe? '))

print('PEDRA!')
sleep(0.5)
print('PAPEL!')
sleep(0.5)
print('TESOURA!')
sleep(0.5)

print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)

if computador == 0: #Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #Papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #Tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')