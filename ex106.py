def titulo(msg):
    """
    -> Função para titulo formatado.
    param (msg): Mensagem que irá aparecer como titulo.
    :return: Retorna um titulo formatado e centralizado.
    """
    print('='*len(msg))
    print(msg)
    print('='*len(msg))


def ajuda(comando):
    help(comando)


while True:
    titulo('  SISTEMA DE AJUDA PyHELP  ')
    mostrar = input('Visualizar função ou biblioteca (sair)> ').strip()
    if mostrar.lower() == 'sair':
        titulo('  PROGRAMA FECHADO  ')
        break
    else:
        titulo(f'  Acessando o manual do comando <{mostrar}>  ')
        ajuda(mostrar)
