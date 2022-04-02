n = int(input('Digite um número inteiro para calcular seu fatorial: '))
f = 1
while n > 0:
    print(n, end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print(f, end='')
