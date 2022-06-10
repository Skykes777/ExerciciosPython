aluno = {}
aluno['nome'] = input('Nome do aluno: ').strip().title()
aluno['media'] = float(input(f'média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['aprorepro'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['aprorepro'] = 'Recuperação'
else:
    aluno['aprorepro'] = 'Reprovado'
print('=='*20)
for k, v in aluno.items():
    print(f'{k}: {v}')
