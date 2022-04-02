salario = float(input('Salario do funcionario: '))

smaior = salario * 0.10
aumento1 = salario + smaior #Para salários acíma de 1250

smenor = salario * 0.15
aumento2 = salario + smenor #Para salários de 1250 para baixo ou igual

if salario > 1250:
    print(f'seu salário de R${salario :.2f} recebeu um aumento de 10%, valot total a receber é de R${aumento1 :.2f}')
else:
    print(f'seu salário de R${salario :.2f} recebeu um aumento de 15%, valot total a receber é de R${aumento2 :.2f}')
