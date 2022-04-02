print('=-='*7)
print('ANALISE DE TRIANGULOS')
print('=-='*7)

r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))
reta = [r1, r2, r3]
maximo = max(reta)
if (r1+r2+r3)-maximo > maximo:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')