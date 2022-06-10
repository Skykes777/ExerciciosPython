def voto(ddn=0):
    """
    -> Com base no ano de nascimento o programa mostrará se é possivel o voto do individuo,
    com base no ano de nascimento.
    :param (ddn): ano de nascimento.
    :return: sem retorno.
    """
    from datetime import date
    if ddn == 0:
        print('Nem uma dada de nascimento foi enformada.')
    else:
        anoAtual = date.today().year
        idade = anoAtual - ddn
        print(f'Com {idade} anos: ', end='')
        if idade < 16:
            print('NÃO VOTA.')
        elif idade < 18 or idade > 65:
            print('VOTO OPCIONAL.')
        else:
            print('VOTO OBRIGATÓRIO.')


# -PROGRAMA PRINCIPAL
while True:
    print('='*20)
    adn = int(input('Ano de nascimento: '))
    voto(adn)
    continuar = input('Desejá continuar? >>> [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Desejá continuar? >>> [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
