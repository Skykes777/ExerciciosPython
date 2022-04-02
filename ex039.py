from datetime import date
ano = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = ano - nascimento
falta = 18 - idade
passou = idade - 18
alistamento = ano + falta
passoualistamento = ano - passou

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}')
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    print(f'Você ainda não tem 18 anos, faltam {falta} ano(s) para o alistamento!')
    print(f'Seu alistamento será em {alistamento}.')
elif idade > 18:
    print(f'Você deveria ter se alistado há {passou} ano(s)')
    print(f'Seu alistamento foi em {passoualistamento}.')
