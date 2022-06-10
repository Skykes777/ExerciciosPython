def ficha():
    print('--'*20)
    nome = input('Nome do jogador: ').strip().title()
    if len(nome) == 0:
        nome = '<desconhescido>'
    gols = input('Número de gols: ')
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.') 


ficha()
