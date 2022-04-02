r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
retas = [r1, r2, r3]
maior = max(retas)
if (r1+r2+r3)-maior > maior:
    print('Pode formar um triangulo!')
    if r1 == r2 == r3:
        print('forma um triangulo EQUILATERO!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('form um tringulo ISÓSCELES!')
    else:
        print('forma um triangulo ESCALENO!')
else:
    print('Não pode formar um triangulo!')
