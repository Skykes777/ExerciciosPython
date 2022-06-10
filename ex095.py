jogador = {}
partidas = []
jogadores = []

while True:
    jogador['nome'] = input('Nome do jogador: ').strip().title()
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for g in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols na partida {g}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    cond = input('Desejá adicionar mais jogadores? >>> [S/N]: ').strip().upper()[0]
    while cond not in 'SN':
      cond = input('Desejá adicionar mais jogadores? >>> [S/N]: ').strip().upper()[0]
    if cond == 'N':
        break

print('=='*27)
print('cod nome', '{:>20}'. format('gols'), '{:>20}'.format('total'))
print('=='*27)
for i, v in enumerate(jogadores):
    print(f'{i+1:2} ', end='')
    for d in v.values():
        print(f'{str(d):<22}', end='')
    print()
print('--'*27)

while True:
    busca = int(input('Qual jogador desejá visualizar? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('Não existe jogador com esse código!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('--'*27)
