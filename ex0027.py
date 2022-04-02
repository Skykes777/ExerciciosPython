n = input('Digite seu nome: ').strip()
nome = n.split()
n1 = nome[0]
n2 = nome[len(nome)-1]
print('O primeiro nome é {} e o ultimo nome é {}.'.format(n1, n2))
