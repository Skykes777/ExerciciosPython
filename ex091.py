from random import randint
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados...')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
print('=='*15)
print('= RANKING DOS JOGADORES =')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1:2}º: {v[0]} com {v[1]} pontos')
