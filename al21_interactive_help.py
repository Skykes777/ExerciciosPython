def contadorP(i, f, p):
    """
    -> Faz uma contagem de um determinado inicio até um fim,
    sendo apresentado na tela.
    :param i: inico da contagem
    :param f: fim da contagem
    :param p: passo de contagem (de quanto em quanto deseja contar)
    :return: sem retorno
    """
    while i <= f:
        print(i, end=' ')
        i += p
    print('FIM!')


contadorP(0, 100, 10)
