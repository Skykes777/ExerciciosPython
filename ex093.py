jogador = {}
partidas = []
jogador['nome'] = input('Nome do jogador: ').strip().title()
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for g in range(1, tot + 1):
    partidas.append(int(input(f'Quantos gols na partida {g}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=='*27)
print(jogador)
print('=='*27)
for x, v in jogador.items():
    print(f'O campo {x} tem o valor {v}')
print('=='*27)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])}.')
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}º, fez {v} gol(s)')
print(f'Foi um total de {jogador["total"]} de gols.')
