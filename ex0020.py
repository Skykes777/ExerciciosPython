import random
aluno1 = input('Aluno: ')
aluno2 = input('Aluno: ')
aluno3 = input('Aluno: ')
aluno4 = input('Aluno: ')
lista = (aluno1, aluno2, aluno3, aluno4)
sorteio = random.sample(lista,4)
print(f'A ordem do sorteio é\n{sorteio}')