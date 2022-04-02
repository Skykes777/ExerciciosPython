sexo = input('Qual seu sexo [\033[31mM\033[m(Masculino)/\033[31mF\033[m(Feminino)]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Valor invalido, por favor, digite o seu sexo: ').strip().upper()[0]
if sexo == 'M':
    print(f'Sexo masculino resgistrado!')
if sexo == 'F':
    print(f'Sexo feminino registrado!')
