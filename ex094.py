total_pessoas = []
pessoa = {}
totIdades = 0

while True:
    pessoa['nome'] = input('Nome: ').strip().title()
    pessoa['sexo'] = input('Qual seu sexo [M/F]: ').strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
      pessoa['sexo'] = input('Qual seu sexo [M/F]: ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    totIdades += pessoa['idade']
    total_pessoas.append(pessoa.copy())
    pessoa.clear()

    cond = input('Desejá adicionar mais pessoas? [S/N]: ').strip().upper()[0]
    while cond not in 'SN':
        cond = input('Desejá adicionar mais pessoas? [S/N]: ').strip().upper()[0]
    if cond == 'N':
        break

print('=='*20)
print(f'''[A] O grupo tem {len(total_pessoas)} pessoas
[B] a média de idades é {totIdades / len(total_pessoas):.1f} anos
[C] As mulheres cadastradas foram: ''', end='')
for m in total_pessoas:
    if m['sexo'] == 'F':
        print(m["nome"], end=' ')
print('\nLista de pessoas címa da média: ')
for p in total_pessoas:
    if p['idade'] >= totIdades / len(total_pessoas):
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
    print()
