preço = float(input('Valor da casa: '))
valorfinanciado = int(input('Quantos anos de financiamento? '))
salario = float(input('Salario do comprador: '))

valorapagar = preço / valorfinanciado
prestaçãomensal = valorapagar / 12

excede = salario * 0.30

if prestaçãomensal > excede:
    print(f'Para pagar uma casa de \033[33mR${preço :.2f}\033[m em \033[33m{valorfinanciado :.0f}\033[m anos, a prestação será de \033[31mR${prestaçãomensal :.2f}\033[m, EMPRÉSTIMO NEGADO, O valor excedeu 30% do seu salário mensal.')
else:
    print(f'Para pagar uma casa de \033[33mR${preço :.2f}\033[m em \033[33m{valorfinanciado :.0f}\033[m anos, a prestação será de \033[31mR${prestaçãomensal :.2f}\033[m, EMPRÉSTIMO CONCLUIDO!')

