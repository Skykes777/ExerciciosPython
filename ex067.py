while True:
    print('-'*33)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*33)
    if n > 0:
        for x in range(1, 11):
            print(f'{n} x {x:2} = {n*x :2}')
    else:
        break
print('Programa tabuada en encerrado, volte sempre!')
