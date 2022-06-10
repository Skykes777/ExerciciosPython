from distutils.log import info
from operator import le
from time import sleep


def infoNum(*valores):
    print('-='*30)
    if len(valores) == 0 or valores == 0:
        print('Nem um valor foi passado neste parametro...')
    else:
        print('Analizando os valores informados...')
        for n in valores:
            print(n, end=' ', flush=True)
            sleep(0.3)
        print(f'''Foram informados {len(valores)} valores ao todo.
O maior valor informado foi {max(valores)}.''')
# -FUNÇÃO PARA ANALIZAR VALORES COMO PARAMETRO


# -PROGRAMA PRINCIPAL ABAIXO
infoNum(2, 9, 4, 5, 7, 1)
infoNum(0)
