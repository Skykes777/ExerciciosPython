numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o ultimo número: ')))
print(f'O número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 está na posição {numeros.index(3)}')
else:
    print('Nem um número 3 foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
