números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Escolha um número de 0 a 20: '))
    if n >= 0 and n <= 20:
        break
    print('Tente novamente! ', end='')
print(f'O número que você digitou foi {números[n]}')
