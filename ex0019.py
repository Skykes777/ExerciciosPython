from random import choice
aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('Nome do aluno: '))
aluno3 = str(input('Nome do aluno: '))
aluno4 = str(input('Nome do aluno: '))
lista = (aluno1, aluno2, aluno3, aluno4)
ordem = choice(lista)
print('Ordem de apresentação do trabalho: {}'.format(ordem))
