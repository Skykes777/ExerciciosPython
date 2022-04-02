número = contador = soma = 0
while True:
    número = int(input('Digite um número (999 para parar): '))
    if número == 999:
        break
    contador += 1
    soma += número
print(f'Você digitou {contador} números, a soma deles deu {soma}')
