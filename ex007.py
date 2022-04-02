p1 = float(input('Primeiro semestre= '))
s2 = float(input('Segundo semestre= '))
m = (p1 + s2)/2
print("A média entre {} e {} é {:.1f}".format(p1, s2, m))
if m < 6:
    print('Reprovado!')
else:
    print('Aprovado!')