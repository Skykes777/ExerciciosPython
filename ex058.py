from random import randint
print('\033[33m=-='*6)
print('ADIVINHE O NÚMERO!')
print('=-='*6)
jogador = int(input('\033[mEscoha um número de 0 a 10: '))
computador = randint(0, 10)
contador = 0
while jogador != computador:
    if computador > jogador:
        jogador = int(input('Mais alto, escolha um número de 0 a 10: '))
    if computador < jogador:
        jogador = int(input('Mais baixo, escolha um número de 0 a 10: '))
    contador += 1
if contador == 0:
    print(f'Parabens, você venceu DE PRIMEIRA! o número escolhido foi {computador}')
elif computador <= 5:
    print(f'Parabens, você acertou com {contador} tentativas, o número erá o {computador}')
else:
    print(f'Você acertou com {contador} tentativas, o número erá o {computador}, tem que melhorar na adivinhação')
