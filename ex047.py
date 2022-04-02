from time import sleep
print('Todos os valores pares de 1 a 50:')
for x in range(2,51, 2):
    if x % 2 == 0:
        print(x, end=' ')
        sleep(0.5)
print('Acabou!')


