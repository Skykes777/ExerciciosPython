lista_idade_18 = 0
lista_homem = 0
lista_mulher = 0
seguimento = ''

while True:
    print('\033[34m=' * 19)
    print('CADASTRO DE PESSOAS')
    print('=' * 19)
    idade = int(input('\033[mDigite sua idade: '))
    sexo = input('Qual seu sexo >> [\033[31mM\033[m(masculino)/\033[31mF\033[m(feminino)]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Qual seu sexo >> [\033[31mM\033[m(masculino)/\033[31mF\033[m(feminino)]: ').strip().upper()[0]
    if idade >= 18:
        lista_idade_18 += 1
    if sexo == 'M':
        lista_homem += 1
    if sexo == 'F' and idade < 20:
        lista_mulher += 1
    print('=-='*15)
    seguimento = input('Quer continuar cadastrando >> [\033[31mS\033[m(sim)/\033[31mN\033[m(não)]: ').strip().upper()[0]
    print('=-=' * 15)
    while seguimento not in 'SN':
        print('=-=' * 15)
        seguimento = input('Quer continuar cadastrando >> [\033[31mS\033[m(sim)/\033[31mN\033[m(não)]: ').strip().upper()[0]
        print('=-=' * 15)
    if seguimento == 'S':
        print()
    if seguimento == 'N':
        break

print('===== FIM DO PROGRAMA =====')
print(f'''Total de pessoas com mais de 18 anos: {lista_idade_18}
Total de homens cadastrados: {lista_homem}
Total de mulheres com menos de 20 anos: {lista_mulher}''')
