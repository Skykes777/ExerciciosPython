def soma(a=0, b=0, c=0):
    """
    --> Soma os valores dos parametros e apresenta na tela.
    :param a: primeiro valor.
    :param b: segundo valor.
    :param c: terceiro valor.
    :return: com retorno.
    """
    s = a + b + c
    return s


n1 = soma(10, 4, 5)
n2 = soma(2, 3)
n3 = soma(5)
print(f'A soma dos valores n1 = {n1}, n2 = {n2} e n3 = {n2}')
