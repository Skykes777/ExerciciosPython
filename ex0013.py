salario = float(input('Salario do funcionario: '))
am = salario * 0.15
aumento = salario + am
print('O salario de RS{:.2f}, recebeu um aumento de 15%, valor total a receber é de R${:.2f}.'.format(salario, aumento))