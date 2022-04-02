num = int(input('Digte um número: '))
total = 0
for x in range(1, num + 1):
    if num % x == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{x}',end='  ')
print(f'\n\033[33mO número {num} foi divisivel {total} vezes.')
if total == 2:
    print('Ele é PRIMO!')
else:
    print('Ele NÃO É PRIMO!')