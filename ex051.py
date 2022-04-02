a1 = int(input('Primeiro termo (a1): '))
razão = int(input('Razão: '))
décimo = a1 + (10 -1) * razão
for x in range(a1, décimo + razão, razão):
    print(f'{x}',end=' > ')
print('ACABOU!')