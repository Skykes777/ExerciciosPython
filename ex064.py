n = soma = contador = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        contador += 1
print(f'Você digitou {contador} número(s), a soma deles é {soma}.')

