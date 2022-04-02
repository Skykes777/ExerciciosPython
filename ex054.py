from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for dt in range(1, 8):
    ddn = int(input(f'Data de nascimento da {dt} pessoa: '))
    idade = ano_atual - ddn
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'''Quantidade de pessoas de maior: {maior}
Quantidade de pessoas menor de idade: {menor}''')
