somaidade = 0
media_idade = 0
maior_idade_homem = 0
nome_do_mais_velho = ''
totmulher20 = 0
for ps in range(1, 5):
    print(f'----- {ps} PESSOA -----')
    nome = input('Nome: ').strip().title() #NOME DA PESSOA
    idade = int(input('Idade: ')) #IDADE DA PESSOA
    sexo = input('Sexo [M/F]: ').strip().lower()
    somaidade += idade
    if ps == 1 and sexo in 'm':
        maior_idade_homem = idade
        nome_do_mais_velho = nome
    if sexo in 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_do_mais_velho = nome
    if sexo in 'f' and idade < 20:
        totmulher20 += 1
media_idade += somaidade / 4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_do_mais_velho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')