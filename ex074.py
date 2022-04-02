from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = max(num)
menor = min(num)
print('Os valore sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
print(f'''\nO maior valor é {maior}
O menor vaor é {menor}''')
