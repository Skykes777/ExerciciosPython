from datetime import date
ano = date.today().year
ddn = int(input('Data de nascimento: '))
idade = ano - ddn
print(f'O atleta tem {idade}')
if idade <= 9:
    print('Atleta mirin!')
elif idade <= 14:
    print('Atleta infantil!')
elif idade <= 19:
    print('Atleta junior!')
elif idade <= 25:
    print('Atleta sênior!')
else:
    print('Atleta MASTER!')
