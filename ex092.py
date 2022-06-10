from datetime import date
anoAtual = date.today().year

trabalhador = {}
trabalhador['nome'] = input('Nome: ').strip().title()
ddn = int(input('Ano de nascimento: '))
trabalhador['idade'] = anoAtual - ddn
trabalhador['ctps'] = int(input('Número da carteira de trabalho(0 caso não tenha): '))
if trabalhador['ctps'] == 0:
    for k, v in trabalhador.items():
        print(f'-{k} tem {v}')
else:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35 - ddn
    for k, v in trabalhador.items():
        print(f'-{k} tem {v}')
