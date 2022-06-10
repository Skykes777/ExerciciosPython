def titutlo(msg):
    print('='*30)
    print('{:^30}'.format(msg))
    print('='*30)
# -Função para titulos


def multT(a, b):
    res = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {res:.1f}m².')
# -Função para multiplicação da area


# -Programa principal abaixo 
titutlo('CONTROLE DE TERRENO')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
multT(largura, comprimento)
