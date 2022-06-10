def fatorial(num=0, show=False):
    """
    -> Calcula o fatorial de um número.
    :param (n): O número a ser calculado.
    :param (show): (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número.
    """
    fat = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= n
    return fat


# -Programa principal
n1 = fatorial(4, show=True)
print(n1)
