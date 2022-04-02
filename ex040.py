n1 = float(input('Primeiro semestre: '))
n2 = float(input('Segundo semestre: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'sua nota foi de {media :.1f}, média abaixo de 5.0: REPROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Sua nota foi de {media :.1f}, Está em recuperação!')
elif media >= 7:
    print(f'Sua nota foi de  {media}, APROVADO!')
